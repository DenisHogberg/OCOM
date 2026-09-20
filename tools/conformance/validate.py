#!/usr/bin/env python3
"""Run the Conformance Test Suite against an exported model and write a Test Report.

`Conformance-Test-Suite.md` specifies the suite and `Test-Catalogue.md` binds each Statement to a
Test kind. This is the procedure side: it reads an implementation's exported model, the
Representation Map that says how the OCOM vocabulary appears in that export, and the
implementation's Conformance Statement, and it produces the report Section 4 describes.

It decides only what the inputs allow it to decide, and says so where they do not. A Test whose
kind is mechanical but whose evidence is absent from the export is reported as awaiting a
reviewer, never as Pass: the standing rule in this repository is that a checker which cannot check
must not report ok. Core Conformance is reported as established only when every mandatory Test is
Pass or Review Pass, which is Section 3's criterion and not this tool's.

  validate.py --model model.json --map representation-map.md --statement conformance-statement.md
              [--reviews reviews.md] [--report report.md]

Standard library only, no network.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "docs" / "Governance" / "Test-Catalogue.md"
REGISTER = ROOT / "docs" / "Governance" / "Requirement-Register.md"

ARTICLES = ("a ", "an ", "the ")
ADJECTIVES = ("unique ", "stable ", "defined ", "explicit ", "valid ", "primary ", "single ",
              "exactly one ", "one or more ", "at least one ", "one ", "its ", "their ", "each ")
THING_VERBS = ("possess", "contain", "define", "have", "carry", "include", "specify", "record",
               "reference", "assign", "state", "identify", "be assigned")


def read_table(path, header_starts):
    """Rows of the first Markdown table whose header line starts with header_starts."""
    rows, in_table = [], False
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith(header_starts):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                if rows:
                    break
                continue
            if set(line.replace("|", "").strip()) <= set("-: "):
                continue
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def load_catalogue():
    rows = read_table(CATALOGUE, "| Alias | Document | Section | Class | Kind |")
    if not rows:
        raise SystemExit("%s carries no test rows; a run over nothing cannot pass" % CATALOGUE)
    return [{"alias": r[0], "document": r[1].strip("`"), "section": r[2], "class": r[3], "kind": r[4]} for r in rows]


def load_register():
    text = REGISTER.read_text(encoding="utf-8")
    out = {}
    for line in text.splitlines():
        if not line.startswith("| REQ-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5:
            out[cells[0]] = cells[4]
    if not out:
        raise SystemExit("%s yielded no Statements" % REGISTER)
    return out


def load_map(path):
    types, fields = {}, {}
    for cells in read_table(path, "| OCOM type | Kind | Where it is in this export |"):
        if len(cells) < 3 or cells[1] != "collection":
            continue
        where = cells[2]
        if where.startswith("*"):            # the map says the export does not carry this type
            types[cells[0].lower()] = []
            continue
        types[cells[0].lower()] = [w.strip().strip("`") for w in where.split(",")]
    for cells in read_table(path, "| OCOM element | Kind | Field in the export |"):
        if len(cells) < 3 or cells[1] != "field":
            continue
        fields[cells[0].lower()] = cells[2].strip("`")
    if not types:
        raise SystemExit("%s declares no type; the map is what makes the test possible" % path)
    return types, fields


def load_statement(path):
    out = {}
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\*\*([A-Za-z ]+):\*\*\s*(.*)", line.strip())
        if m:
            out[m.group(1).strip().lower()] = m.group(2).strip()
    return out


def instances(model, paths):
    """Every record the map's collection paths point at, as (path, record)."""
    out = []
    for p in paths:
        if "[]." in p:
            parent, child = p.split("[].", 1)
            for rec in model.get(parent, []):
                for sub in rec.get(child, []):
                    out.append((p, sub))
        else:
            for rec in model.get(p, []):
                out.append((p, rec))
    return out


def normalize(phrase):
    """A list item or object phrase reduced to the vocabulary element it names."""
    low = re.sub(r"\s+", " ", phrase.lower()).strip(" .;")
    for verb in THING_VERBS:
        if low.startswith(verb + " "):
            low = low[len(verb) + 1:]
            break
    changed = True
    while changed:
        changed = False
        for prefix in ARTICLES + ADJECTIVES:
            if low.startswith(prefix):
                low = low[len(prefix):]
                changed = True
    return low.strip()


def subject_of(text, types):
    """The OCOM type a Statement is about, as the map spells it."""
    m = re.match(r"\s*(?:Every|Each|All|An|A|The)?\s*([A-Za-z][A-Za-z ]*?)\s+(?:shall|should|may)\b", text)
    if not m:
        return None
    words = m.group(1).strip().split()
    for n in range(len(words), 0, -1):
        candidate = " ".join(words[-n:]).lower().rstrip("s") or " ".join(words[-n:]).lower()
        for name in (candidate, candidate + "s", " ".join(words[-n:]).lower()):
            if name in types:
                return name
    return None


def required_elements(text):
    """The elements a Presence Statement requires, normalized."""
    if ":" in text:
        items = [i for i in re.split(r"[;,]", text.split(":", 1)[1]) if i.strip(" .;")]
        return [normalize(i) for i in items]
    m = re.search(r"shall\s+(?:%s)\s+(.+)" % "|".join(THING_VERBS), text)
    if m:
        return [normalize(m.group(1))]
    return []


# a phrase carrying a clause is a condition, not an element: "when an Object is created"
CLAUSE = re.compile(r"\b(when|where|unless|while|after|before|if|through|within|that|which)\b")


def presence(test, text, model, types, fields):
    subject = subject_of(text, types)
    if subject is None:
        return None, "the Statement's subject is not a type the Representation Map declares"
    paths = types.get(subject) or []
    if not paths:
        return "Fail", "the Representation Map declares no representation for %s" % subject
    elements = required_elements(text)
    if not elements:
        return None, "no element could be read out of the Statement"
    tail = text.split(":", 1)[1] if ":" in text else ""
    if tail and ";" not in tail and "," not in tail and len(tail.split()) > 3:
        # the source document's bullets carry no separator, so the register absorbed them into one
        # run of words and the item boundaries are gone: a machine cannot invent them back
        return None, "the Statement's list items are not separated in the source, so its elements cannot be read"
    unread = [e for e in elements if CLAUSE.search(e)]
    if unread:
        return None, "the Statement states a condition rather than an element (%s); a reviewer decides it" % unread[0][:60]
    recs = instances(model, paths)
    if not recs:
        return "Fail", "the export carries no %s record" % subject
    missing = []
    for element in elements:
        key = "%s.%s" % (subject, element)
        field = fields.get(key) or fields.get("object.%s" % element)
        if field is None:
            missing.append("%s (the map binds no field to %s)" % (element, key))
            continue
        for path, rec in recs:
            value = rec.get(field)
            if value in (None, "", [], {}):
                missing.append("%s (%s record %s carries no %s)" % (element, path, rec.get("id", "?"), field))
                break
    if missing:
        return "Fail", "; ".join(missing[:4])
    return "Pass", "%d %s record(s) carry %s" % (len(recs), subject, ", ".join(elements))


def transition(test, text, model, types, fields):
    lifecycles = {lc["id"]: lc for lc in model.get("lifecycles", [])}
    if not lifecycles:
        return "Fail", "the export carries no Lifecycle"
    low = text.lower()
    if "initial state" in low:
        bad = [lc["id"] for lc in lifecycles.values() if not lc.get("initial_state")]
        return ("Fail", "no initial State: %s" % ", ".join(bad)) if bad else ("Pass", "%d Lifecycle(s) define one initial State" % len(lifecycles))
    if "exactly one" in low and "state" in low:
        bad = [e["id"] for e in model.get("entities", []) if not isinstance(e.get("state"), str)]
        return ("Fail", "not in exactly one State: %s" % ", ".join(bad)) if bad else ("Pass", "%d Entities occupy exactly one State" % len(model.get("entities", [])))
    events = model.get("events", [])
    if not events:
        return None, "the export carries no event history, so no recorded State change can be checked"
    permitted = {}
    for lc in lifecycles.values():
        for t in lc.get("transitions", []):
            permitted.setdefault(lc["entity"], set()).add((t["from"], t["to"]))
    bad = []
    for e in events:
        subject = e.get("subject")
        if e.get("from_state") is None or subject not in permitted:
            continue
        if (e["from_state"], e["to_state"]) not in permitted[subject]:
            bad.append("%s: %s to %s" % (e.get("id"), e["from_state"], e["to_state"]))
    if bad:
        return "Fail", "State change the Lifecycle does not permit: %s" % "; ".join(bad[:3])
    return "Pass", "%d recorded State change(s), every one permitted" % len([e for e in events if e.get("from_state")])


def invariant(test, text, model, types, fields):
    low = text.lower()
    if "identity" in low and ("reused" in low or "not be reused" in low):
        seen, dupes = {}, []
        for name, paths in types.items():
            for path, rec in instances(model, paths):
                ident = rec.get("id")
                if ident is None:
                    continue
                if ident in seen and seen[ident] != path:
                    dupes.append(ident)
                seen[ident] = path
        return ("Fail", "identity used by two records: %s" % ", ".join(sorted(set(dupes))[:3])) if dupes else ("Pass", "%d identities, none reused" % len(seen))
    return None, "deciding this prohibition needs evidence the export does not carry (a history, or a refusal record)"


def declaration(clause, statement):
    low = clause.lower()
    if "specification version" in low:
        v = statement.get("supported specification version")
        return ("Pass", "the Conformance Statement names version %s" % v) if v else ("Fail", "no supported specification version is declared")
    if "multiple versions" in low:
        v = statement.get("supported specification version", "")
        return ("Pass", "one version declared: %s" % v) if v else ("Fail", "no version declared")
    if "extension" in low:
        e = statement.get("supported extensions")
        return ("Pass", "extensions declared: %s" % e) if e else ("Fail", "supported extensions are not declared")
    if "shall not claim conformance" in low:
        return None, "decided by the outcome of every other mandatory Test, reported in the summary"
    return None, "no procedure is bound to this clause"


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--model", required=True)
    p.add_argument("--map", required=True)
    p.add_argument("--statement", required=True)
    p.add_argument("--report")
    p.add_argument("--today", default="20 September 2026")
    a = p.parse_args(argv)

    model = json.loads(pathlib.Path(a.model).read_text(encoding="utf-8"))
    types, fields = load_map(a.map)
    statement = load_statement(a.statement)
    catalogue = load_catalogue()
    register = load_register()

    results = []
    for test in catalogue:
        text = register.get(test["alias"], "")
        kind = test["kind"]
        if kind == "Review":
            outcome, reason = None, "awaiting a named reviewer, per the kind this Test carries"
        elif kind == "Presence":
            outcome, reason = presence(test, text, model, types, fields)
        elif kind == "Transition":
            outcome, reason = transition(test, text, model, types, fields)
        elif kind == "Invariant":
            outcome, reason = invariant(test, text, model, types, fields)
        else:
            outcome, reason = None, "no procedure is bound to this kind"
        results.append({**test, "outcome": outcome, "reason": reason, "text": text})

    for cells in read_table(CATALOGUE, "| Test | Section | Clause |"):
        if len(cells) < 3:
            continue
        outcome, reason = declaration(cells[2], statement)
        results.append({"alias": cells[0], "document": "Language/Conformance.md", "section": cells[1],
                        "class": "mandatory", "kind": "Declaration", "outcome": outcome,
                        "reason": reason, "text": cells[2]})

    mandatory = [r for r in results if r["class"] == "mandatory"]
    passed = [r for r in mandatory if r["outcome"] == "Pass"]
    failed = [r for r in mandatory if r["outcome"] == "Fail"]
    pending = [r for r in mandatory if r["outcome"] is None]
    established = not failed and not pending

    lines = []
    lines.append("# Test Report")
    lines.append("")
    lines.append("**Run on:** %s" % a.today)
    lines.append("")
    lines.append("**Implementation:** %s" % statement.get("implementation name", "(not declared)"))
    lines.append("")
    lines.append("**Specification version claimed:** %s" % statement.get("supported specification version", "(not declared)"))
    lines.append("")
    lines.append("**Model:** `%s`  **Representation Map:** `%s`" % (a.model, a.map))
    lines.append("")
    lines.append("**Published by:** the party that ran the suite. A report published by the claimant is "
                 "self-validation; `Conformance-Test-Suite.md` Section 4 says the suite does not tell the two "
                 "apart and the publisher does.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| | Count |")
    lines.append("|---|---|")
    lines.append("| Mandatory Tests | %d |" % len(mandatory))
    lines.append("| Pass | %d |" % len(passed))
    lines.append("| Fail | %d |" % len(failed))
    lines.append("| Awaiting a reviewer or evidence the export does not carry | %d |" % len(pending))
    lines.append("")
    lines.append("**Core Conformance: %s.** Section 3 establishes it when every mandatory Test is Pass or "
                 "Review Pass. %s" % ("established" if established else "not established",
                                      "" if established else
                                      "%d mandatory Test(s) fail and %d await a reviewer or evidence this export "
                                      "does not carry." % (len(failed), len(pending))))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append("| Test | Document | Kind | Class | Outcome | Why |")
    lines.append("|---|---|---|---|---|---|")
    for r in results:
        lines.append("| %s | `%s` | %s | %s | %s | %s |"
                     % (r["alias"], r["document"], r["kind"], r["class"],
                        r["outcome"] or "pending", (r["reason"] or "").replace("|", "\\|")[:180]))
    report = "\n".join(lines) + "\n"

    if a.report:
        pathlib.Path(a.report).write_text(report, encoding="utf-8")
        print("wrote %s" % a.report)
    print("mandatory %d: Pass %d, Fail %d, pending %d. Core Conformance %s."
          % (len(mandatory), len(passed), len(failed), len(pending),
             "established" if established else "not established"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

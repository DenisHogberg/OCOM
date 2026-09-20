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


def transition_predicate(text, model, lifecycles):
    """Each Statement gets the procedure its own predicate asks for, or none.

    A single catch-all answered every Transition Statement with "every recorded State change is
    permitted", so "Transitions shall be explicitly defined" was reported Pass on the strength of a
    check it does not make. One procedure per predicate, and a predicate with no procedure is
    pending rather than passed.
    """
    low = text.lower()

    if "initial state" in low:
        bad = [lc["id"] for lc in lifecycles.values() if not lc.get("initial_state")]
        if bad:
            return "Fail", "no initial State: %s" % ", ".join(bad)
        if "one and only one" in low or "one initial" in low:
            multiple = [lc["id"] for lc in lifecycles.values() if isinstance(lc.get("initial_state"), list)]
            if multiple:
                return "Fail", "more than one initial State: %s" % ", ".join(multiple)
        outside = [lc["id"] for lc in lifecycles.values()
                   if lc.get("initial_state") not in [s.get("name") for s in lc.get("states", [])]]
        if outside:
            return "Fail", "initial State is not one of the Lifecycle's States: %s" % ", ".join(outside)
        return "Pass", "%d Lifecycle(s) define exactly one initial State, each among their own States" % len(lifecycles)

    if "exactly one" in low and "state" in low:
        entities = model.get("entities", [])
        if not entities:
            return "Fail", "the export carries no Entity"
        bad = []
        for e in entities:
            state = e.get("state")
            lc = lifecycles.get(e.get("lifecycle"))
            if not isinstance(state, str) or not state:
                bad.append("%s occupies no single State" % e.get("id"))
            elif lc and state not in [s.get("name") for s in lc.get("states", [])]:
                bad.append("%s is in %s, which its Lifecycle does not define" % (e.get("id"), state))
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Entities each occupy exactly one State defined by their Lifecycle" % len(entities))

    if "explicitly defined" in low or "define valid state transitions" in low or "define permitted" in low:
        bad = []
        for lc in lifecycles.values():
            transitions = lc.get("transitions") or []
            if not transitions:
                bad.append("%s defines no Transition" % lc["id"])
                continue
            names = [s.get("name") for s in lc.get("states", [])]
            for tr in transitions:
                if not tr.get("from") or not tr.get("to"):
                    bad.append("%s has a Transition with no from or to" % lc["id"])
                elif tr["from"] not in names or tr["to"] not in names:
                    bad.append("%s: %s to %s names a State the Lifecycle does not define" % (lc["id"], tr["from"], tr["to"]))
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Lifecycle(s) define %d Transitions, every endpoint a State they declare"
                % (len(lifecycles), sum(len(lc.get("transitions") or []) for lc in lifecycles.values())))

    if "terminal" in low:
        permitted = {}
        for lc in lifecycles.values():
            for tr in lc.get("transitions", []):
                permitted.setdefault(lc["entity"], []).append(tr["from"])
        left = []
        for lc in lifecycles.values():
            for terminal in lc.get("terminal_states", []):
                if terminal in permitted.get(lc["entity"], []):
                    left.append("%s: %s is terminal and has an outgoing Transition" % (lc["id"], terminal))
        return ("Fail", "; ".join(left[:3])) if left else \
               ("Pass", "no terminal State is left in %d Lifecycle(s)" % len(lifecycles))

    if "prohibit undefined" in low or "only perform" in low or "permitted by the lifecycle" in low:
        events = model.get("events", [])
        if not events:
            return None, "the export carries no event history, so no recorded State change can be checked"
        permitted = {}
        for lc in lifecycles.values():
            for tr in lc.get("transitions", []):
                permitted.setdefault(lc["entity"], set()).add((tr["from"], tr["to"]))
        bad = []
        for e in events:
            subject, before = e.get("subject"), e.get("from_state")
            if before is None or subject not in permitted:
                continue
            if (before, e.get("to_state")) not in permitted[subject]:
                bad.append("%s: %s to %s" % (e.get("id"), before, e.get("to_state")))
        return ("Fail", "State change the Lifecycle does not permit: %s" % "; ".join(bad[:3])) if bad else \
               ("Pass", "%d recorded State change(s), every one permitted by the Lifecycle"
                % len([e for e in events if e.get("from_state")]))

    if "belong to exactly one entity" in low:
        bad = [lc["id"] for lc in lifecycles.values()
               if not isinstance(lc.get("entity"), str) or not lc.get("entity")]
        return ("Fail", "no single Entity: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) each belong to exactly one Entity" % len(lifecycles))

    if "operational state" in low or "one or more state" in low:
        bad = [lc["id"] for lc in lifecycles.values() if len(lc.get("states") or []) < 2]
        return ("Fail", "fewer than two States: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) define %d States between them"
                % (len(lifecycles), sum(len(lc.get("states") or []) for lc in lifecycles.values())))

    return None, "no procedure is bound to this predicate; a reviewer decides it"


def transition(test, text, model, types, fields):
    """Every part of the Statement gets its own procedure, and one unanswered part makes it pending.

    A stem with a list states several requirements at once. Answering it with the procedure for
    whichever phrase matched first reports Pass on the strength of a check the other items never
    received, which is the same defect as passing a Presence list over an item nothing resolves.
    """
    lifecycles = {lc["id"]: lc for lc in model.get("lifecycles", [])}
    if not lifecycles:
        return "Fail", "the export carries no Lifecycle"
    parts = [i.strip(" .;") for i in re.split(r"[;,]", text.split(":", 1)[1]) if i.strip(" .;")] \
        if ":" in text else [text]
    outcomes, reasons, unanswered = [], [], []
    for part in parts:
        outcome, reason = transition_predicate(part, model, lifecycles)
        if outcome is None:
            unanswered.append(part[:60])
        else:
            outcomes.append(outcome)
            reasons.append(reason)
    if "Fail" in outcomes:
        return "Fail", "; ".join(r for o, r in zip(outcomes, reasons) if o == "Fail")[:200]
    if unanswered:
        return None, "no procedure is bound to %d of this Statement's %d parts (%s); a reviewer decides it" \
                     % (len(unanswered), len(parts), unanswered[0])
    return "Pass", "; ".join(reasons)[:200]


def invariant_predicate(text, model, types, lifecycles):
    """One prohibition, one procedure, or none. Never a verdict borrowed from another check."""
    low = text.lower()

    if "identity" in low and "reused" in low:
        seen, dupes = {}, []
        for name, paths in types.items():
            for path, rec in instances(model, paths):
                ident = rec.get("id")
                if ident is None:
                    continue
                if ident in seen and seen[ident] != path:
                    dupes.append(ident)
                seen[ident] = path
        return ("Fail", "identity used by two records: %s" % ", ".join(sorted(set(dupes))[:3])) if dupes else \
               ("Pass", "%d identities, none reused across collections" % len(seen))

    if "ownership" in low and ("never be undefined" in low or "not be undefined" in low):
        governed = [(p, r) for p in ("entities", "domains") for r in model.get(p, [])]
        bad = [r.get("id") for _, r in governed if not r.get("owner")]
        return ("Fail", "no owner: %s" % ", ".join(str(b) for b in bad[:3])) if bad else \
               ("Pass", "%d governed records each name an owner" % len(governed))

    if "primary governance" in low and "shared" in low:
        bad, seen = [], {}
        for e in model.get("entities", []):
            domain = e.get("domain")
            if isinstance(domain, list) and len(domain) > 1:
                bad.append("%s names %d primary Domains" % (e.get("id"), len(domain)))
        for d in model.get("domains", []):
            for name in d.get("entity_types", []):
                if name in seen and seen[name] != d["id"]:
                    bad.append("%s is governed by %s and %s" % (name, seen[name], d["id"]))
                seen[name] = d["id"]
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Entities each name one primary Domain, and no Entity type is governed twice"
                % len(model.get("entities", [])))

    if "multiple initial state" in low:
        bad = [lc["id"] for lc in lifecycles.values() if isinstance(lc.get("initial_state"), list)]
        return ("Fail", "more than one initial State: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s), none with more than one initial State" % len(lifecycles))

    if "unreachable state" in low:
        bad = []
        for lc in lifecycles.values():
            names = [s.get("name") for s in lc.get("states", [])]
            reached, frontier = {lc.get("initial_state")}, [lc.get("initial_state")]
            while frontier:
                here = frontier.pop()
                for tr in lc.get("transitions", []):
                    if tr.get("from") == here and tr.get("to") not in reached:
                        reached.add(tr["to"])
                        frontier.append(tr["to"])
            unreachable = [n for n in names if n not in reached]
            if unreachable:
                bad.append("%s: %s" % (lc["id"], ", ".join(unreachable)))
        return ("Fail", "States no Transition reaches from the initial State: %s" % "; ".join(bad[:3])) if bad else \
               ("Pass", "every State of %d Lifecycle(s) is reachable from its initial State" % len(lifecycles))

    if "undefined transition" in low or "undefined state transition" in low:
        bad = []
        for lc in lifecycles.values():
            names = [s.get("name") for s in lc.get("states", [])]
            for tr in lc.get("transitions", []):
                if tr.get("from") not in names or tr.get("to") not in names:
                    bad.append("%s: %s to %s" % (lc["id"], tr.get("from"), tr.get("to")))
        for wf in model.get("workflows", []):
            for tr in wf.get("transitions", []):
                lc = next((l for l in lifecycles.values() if l.get("entity") == tr.get("entity")), None)
                if lc and (tr.get("from"), tr.get("to")) not in {(x.get("from"), x.get("to")) for x in lc.get("transitions", [])}:
                    bad.append("%s performs %s to %s, which %s does not define" % (wf.get("id"), tr.get("from"), tr.get("to"), lc["id"]))
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "no Transition in %d Lifecycle(s) or %d Workflow(s) names an undefined State"
                % (len(lifecycles), len(model.get("workflows", []))))

    if "violate entity lifecycle" in low or "violate lifecycle" in low:
        bad = []
        for wf in model.get("workflows", []):
            for tr in wf.get("transitions", []):
                lc = next((l for l in lifecycles.values() if l.get("entity") == tr.get("entity")), None)
                if lc is None:
                    bad.append("%s acts on %s, which has no Lifecycle" % (wf.get("id"), tr.get("entity")))
                elif (tr.get("from"), tr.get("to")) not in {(x.get("from"), x.get("to")) for x in lc.get("transitions", [])}:
                    bad.append("%s: %s to %s is not in %s" % (wf.get("id"), tr.get("from"), tr.get("to"), lc["id"]))
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Workflow(s) perform only Transitions their Entity's Lifecycle defines"
                % len(model.get("workflows", [])))

    return None, "deciding this prohibition needs evidence the export does not carry (a history, or a refusal record)"


def invariant(test, text, model, types, fields):
    """As with Transition, every part of a compound prohibition is answered or the Statement is pending."""
    lifecycles = {lc["id"]: lc for lc in model.get("lifecycles", [])}
    parts = [i.strip(" .;") for i in re.split(r"[;,]", text.split(":", 1)[1]) if i.strip(" .;")] \
        if "never:" in text or "shall not:" in text else [text]
    outcomes, reasons, unanswered = [], [], []
    for part in parts:
        outcome, reason = invariant_predicate(part, model, types, lifecycles)
        if outcome is None:
            unanswered.append(part[:60])
        else:
            outcomes.append(outcome)
            reasons.append(reason)
    if "Fail" in outcomes:
        return "Fail", "; ".join(r for o, r in zip(outcomes, reasons) if o == "Fail")[:200]
    if unanswered:
        return None, ("deciding %d of this Statement's %d parts needs evidence the export does not carry (%s)"
                      % (len(unanswered), len(parts), unanswered[0]))
    return "Pass", "; ".join(reasons)[:200]


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

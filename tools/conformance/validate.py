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
    rows = read_table(CATALOGUE, "| Alias | Document | Section | Class | Kind | Disposition |")
    if not rows:
        raise SystemExit("%s carries no test rows; a run over nothing cannot pass" % CATALOGUE)
    return [{"alias": r[0], "document": r[1].strip("`"), "section": r[2], "class": r[3], "kind": r[4],
             "disposition": r[5] if len(r) > 5 else ""} for r in rows]


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
    """Every record the map's collection paths point at, as (path, record), each record once."""
    out, seen = [], set()
    for p in dict.fromkeys(paths):
        if "[]." in p:
            parent, child = p.split("[].", 1)
            for rec in model.get(parent, []):
                for sub in rec.get(child, []):
                    if id(sub) not in seen:
                        seen.add(id(sub))
                        out.append((p, sub))
        else:
            for rec in model.get(p, []):
                if id(rec) not in seen:
                    seen.add(id(rec))
                    out.append((p, rec))
    return out


# Object's own characteristics, the only elements a Type.<element> miss may fall back to. A wider
# fallback let one Object row in the map answer for every type and point a Test at another field.
OBJECT_ELEMENTS = ("identity", "identifier", "metadata")

EMPTY_STRINGS = {"", "null", "none", "n/a", "-", "tbd"}


def is_absent(value):
    """Structural emptiness. false and 0 are values a field can legitimately hold nowhere in this
    vocabulary, and a string reading "null" is an absence written down."""
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, str):
        return value.strip().lower() in EMPTY_STRINGS
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) == 0
    return False


class Resolver:
    """The only way the engines touch the export, so every kind honours the Representation Map."""

    def __init__(self, model, types, fields):
        self.model, self.types, self.fields = model, types, fields

    def declared(self, type_name):
        return type_name.lower() in self.types

    def records(self, type_name):
        return instances(self.model, self.types.get(type_name.lower()) or [])

    def field(self, type_name, element):
        """(field name, whether it came from the Object fallback), or (None, False)."""
        key = "%s.%s" % (type_name.lower(), element.lower())
        if key in self.fields:
            return self.fields[key], False
        if element.lower() in OBJECT_ELEMENTS and "object.%s" % element.lower() in self.fields:
            return self.fields["object.%s" % element.lower()], True
        return None, False

    def value(self, record, type_name, element):
        name, _ = self.field(type_name, element)
        return None if name is None else record.get(name)

    def all_paths(self):
        """Every distinct collection path the map declares. The map lists one collection under
        several type names (entities are Objects and carry Identity), so counting per type name
        counts the same record several times."""
        return list(dict.fromkeys(p for paths in self.types.values() for p in paths))

    def all_records(self):
        return instances(self.model, self.all_paths())

    def identity_of(self, path, record):
        for type_name, paths in self.types.items():
            if path in paths:
                name, _ = self.field(type_name, "identity")
                if name:
                    return record.get(name)
        return record.get("id")

    def ids(self):
        """Every identity the export declares, as {id: [paths]}, each record counted once."""
        out = {}
        for path, rec in self.all_records():
            ident = self.identity_of(path, rec)
            if ident is not None and not is_absent(ident):
                out.setdefault(ident, [])
                if path not in out[ident]:
                    out[ident].append(path)
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


def presence(test, text, r):
    subject = subject_of(text, r.types)
    if subject is None:
        return None, "the Statement's subject is not a type the Representation Map declares"
    if not r.types.get(subject):
        return "Fail", "the Representation Map declares no representation for %s" % subject
    elements = required_elements(text)
    if not elements:
        return None, "no element could be read out of the Statement"
    tail = text.split(":", 1)[1] if ":" in text else ""
    if tail and ";" not in tail and "," not in tail and len(tail.split()) > 3:
        return None, "the Statement's list items are not separated in the source, so its elements cannot be read"
    unread = [e for e in elements if CLAUSE.search(e)]
    if unread:
        return None, "the Statement states a condition rather than an element (%s); a reviewer decides it" % unread[0][:60]
    records = r.records(subject)
    if not records:
        return "Fail", "the export carries no %s record" % subject
    missing, borrowed = [], []
    for element in elements:
        name, fallback = r.field(subject, element)
        if name is None:
            missing.append("%s (the map binds no field to %s.%s)" % (element, subject, element))
            continue
        if fallback:
            borrowed.append("%s resolved through Object.%s" % (element, element))
        for path, rec in records:
            if is_absent(rec.get(name)):
                missing.append("%s (%s record %s carries no %s)" % (element, path, rec.get("id", "?"), name))
                break
    if missing:
        return "Fail", "; ".join(missing[:4])
    note = "" if not borrowed else " (%s)" % "; ".join(borrowed)
    return "Pass", "%d %s record(s) carry %s%s" % (len(records), subject, ", ".join(elements), note)


def lifecycle_index(r):
    """Lifecycles by identity, and the Lifecycle each Entity names, both read through the map."""
    lifecycles = {}
    for _, lc in r.records("lifecycle"):
        ident = r.value(lc, "lifecycle", "identifier") or lc.get("id")
        if ident:
            lifecycles[ident] = lc
    by_entity = {}
    for _, e in r.records("entity"):
        ident = r.value(e, "entity", "identity") or e.get("id")
        named = r.value(e, "entity", "lifecycle")
        if ident:
            by_entity[ident] = named
    return lifecycles, by_entity


def state_names(r, lc):
    out = []
    for s in r.value(lc, "lifecycle", "states") or []:
        out.append(s.get(r.field("state", "name")[0] or "name") if isinstance(s, dict) else s)
    return out


def transitions_of(r, lc):
    out = []
    for tr in r.value(lc, "lifecycle", "transitions") or []:
        if isinstance(tr, dict):
            out.append((tr.get(r.field("transition", "from")[0] or "from"),
                        tr.get(r.field("transition", "to")[0] or "to")))
    return out


def transition_predicate(text, r, lifecycles, by_entity):
    low = text.lower()

    if "initial state" in low:
        bad = [k for k, lc in lifecycles.items() if is_absent(r.value(lc, "lifecycle", "initial state"))]
        if bad:
            return "Fail", "no initial State: %s" % ", ".join(bad)
        if "one and only one" in low or "one initial" in low:
            multiple = [k for k, lc in lifecycles.items() if isinstance(r.value(lc, "lifecycle", "initial state"), list)]
            if multiple:
                return "Fail", "more than one initial State: %s" % ", ".join(multiple)
        outside = [k for k, lc in lifecycles.items()
                   if r.value(lc, "lifecycle", "initial state") not in state_names(r, lc)]
        if outside:
            return "Fail", "initial State is not one of the Lifecycle's States: %s" % ", ".join(outside)
        return "Pass", "%d Lifecycle(s) define exactly one initial State, each among their own States" % len(lifecycles)

    if "exactly one" in low and "state" in low:
        entities = r.records("entity")
        if not entities:
            return "Fail", "the export carries no Entity"
        bad = []
        for _, e in entities:
            ident = r.value(e, "entity", "identity") or e.get("id")
            state = r.value(e, "entity", "state")
            named = by_entity.get(ident)
            lc = lifecycles.get(named)
            if not isinstance(state, str) or is_absent(state):
                bad.append("%s occupies no single State" % ident)
            elif named and lc is None:
                bad.append("%s names Lifecycle %s, which the export does not carry" % (ident, named))
            elif lc is not None and state not in state_names(r, lc):
                bad.append("%s is in %s, which its Lifecycle does not define" % (ident, state))
            elif lc is None:
                bad.append("%s names no Lifecycle, so its State cannot be checked against one" % ident)
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Entities each occupy exactly one State defined by their Lifecycle" % len(entities))

    if "explicitly defined" in low or "define valid state transitions" in low or "define permitted" in low:
        bad = []
        total = 0
        for k, lc in lifecycles.items():
            pairs = transitions_of(r, lc)
            total += len(pairs)
            if not pairs:
                bad.append("%s defines no Transition" % k)
                continue
            names = state_names(r, lc)
            for a, b in pairs:
                if is_absent(a) or is_absent(b):
                    bad.append("%s has a Transition with no from or to" % k)
                elif a not in names or b not in names:
                    bad.append("%s: %s to %s names a State the Lifecycle does not define" % (k, a, b))
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Lifecycle(s) define %d Transitions, every endpoint a State they declare" % (len(lifecycles), total))

    if "terminal" in low:
        left = []
        for k, lc in lifecycles.items():
            outgoing = {a for a, _ in transitions_of(r, lc)}
            for terminal in r.value(lc, "lifecycle", "terminal states") or []:
                if terminal in outgoing:
                    left.append("%s: %s is terminal and has an outgoing Transition" % (k, terminal))
        return ("Fail", "; ".join(left[:3])) if left else \
               ("Pass", "no terminal State is left in %d Lifecycle(s)" % len(lifecycles))

    if "prohibit undefined" in low or "only perform" in low or "permitted by the lifecycle" in low:
        events = r.records("event")
        permitted = {k: set(transitions_of(r, lc)) for k, lc in lifecycles.items()}
        compared, bad, unresolved = 0, [], []
        for _, e in events:
            subject = r.value(e, "event", "subject")
            before = e.get("from_state")
            after = e.get("to_state")
            if before is None:
                continue
            named = by_entity.get(subject)
            if named is None or named not in permitted:
                unresolved.append(str(subject))
                continue
            compared += 1
            if (before, after) not in permitted[named]:
                bad.append("%s: %s to %s" % (e.get("id"), before, after))
        if bad:
            return "Fail", "State change the Lifecycle does not permit: %s" % "; ".join(bad[:3])
        if unresolved:
            return None, ("%d recorded State change(s) name a subject no Lifecycle can be resolved for (%s), "
                          "so they were not compared" % (len(unresolved), unresolved[0]))
        if compared == 0:
            return None, "no event records a prior State, so no recorded State change could be compared"
        return "Pass", "%d recorded State change(s) compared, every one permitted by the Lifecycle" % compared

    if "belong to exactly one entity" in low:
        bad = [k for k, lc in lifecycles.items() if is_absent(r.value(lc, "lifecycle", "entity"))]
        return ("Fail", "no single Entity: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) each belong to exactly one Entity" % len(lifecycles))

    if "operational state" in low or "one or more state" in low:
        bad = [k for k, lc in lifecycles.items() if len(state_names(r, lc)) < 2]
        return ("Fail", "fewer than two States: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) define %d States between them"
                % (len(lifecycles), sum(len(state_names(r, lc)) for lc in lifecycles.values())))

    return None, "no procedure is bound to this predicate; a reviewer decides it"


def compound(text):
    return [i.strip(" .;") for i in re.split(r"[;,]", text.split(":", 1)[1]) if i.strip(" .;")] \
        if ":" in text else [text]


def combine(parts, run_one):
    outcomes, reasons, unanswered = [], [], []
    for part in parts:
        outcome, reason = run_one(part)
        if outcome is None:
            unanswered.append((part[:60], reason))
        else:
            outcomes.append(outcome)
            reasons.append(reason)
    if "Fail" in outcomes:
        return "Fail", "; ".join(r for o, r in zip(outcomes, reasons) if o == "Fail")[:200]
    if unanswered:
        if len(parts) == 1:
            return None, unanswered[0][1]
        return None, "%d of this Statement's %d parts are undecided (%s)" % (len(unanswered), len(parts), unanswered[0][0])
    return "Pass", "; ".join(reasons)[:220]


def transition(test, text, r):
    lifecycles, by_entity = lifecycle_index(r)
    if not lifecycles:
        return "Fail", "the export carries no Lifecycle"
    return combine(compound(text), lambda part: transition_predicate(part, r, lifecycles, by_entity))


def invariant_predicate(text, r, lifecycles, by_entity):
    low = text.lower()

    if "identity" in low and "reused" in low:
        counts = {}
        for path, rec in r.all_records():
            ident = r.identity_of(path, rec)
            if ident is not None and not is_absent(ident):
                counts[ident] = counts.get(ident, 0) + 1
        dupes = [i for i, n in counts.items() if n > 1]
        return ("Fail", "identity carried by %d records: %s" % (len(dupes), ", ".join(sorted(dupes)[:3]))) if dupes else \
               ("Pass", "%d identities, each carried by exactly one record" % len(counts))

    if "ownership" in low and ("never be undefined" in low or "not be undefined" in low):
        governed = r.records("entity") + r.records("domain")
        bad = []
        for _, rec in governed:
            owner = rec.get(r.field("entity", "owner")[0] or "owner")
            if is_absent(owner):
                bad.append(str(rec.get("id")))
        return ("Fail", "no owner: %s" % ", ".join(bad[:3])) if bad else \
               ("Pass", "%d governed records each name an owner" % len(governed))

    if "primary governance" in low and "shared" in low:
        bad, seen = [], {}
        for _, e in r.records("entity"):
            domain = r.value(e, "entity", "domain")
            if isinstance(domain, list) and len(domain) > 1:
                bad.append("%s names %d primary Domains" % (e.get("id"), len(domain)))
        for _, d in r.records("domain"):
            for name in d.get("entity_types", []):
                if name in seen and seen[name] != d.get("id"):
                    bad.append("%s is governed by %s and %s" % (name, seen[name], d.get("id")))
                seen[name] = d.get("id")
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Entities each name one primary Domain, and no Entity type is governed twice"
                % len(r.records("entity")))

    if "multiple initial state" in low:
        bad = [k for k, lc in lifecycles.items() if isinstance(r.value(lc, "lifecycle", "initial state"), list)]
        return ("Fail", "more than one initial State: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s), none with more than one initial State" % len(lifecycles))

    if "unreachable state" in low:
        bad = []
        for k, lc in lifecycles.items():
            names = state_names(r, lc)
            start = r.value(lc, "lifecycle", "initial state")
            reached, frontier = {start}, [start]
            pairs = transitions_of(r, lc)
            while frontier:
                here = frontier.pop()
                for a, b in pairs:
                    if a == here and b not in reached:
                        reached.add(b)
                        frontier.append(b)
            unreachable = [n for n in names if n not in reached]
            if unreachable:
                bad.append("%s: %s" % (k, ", ".join(unreachable)))
        return ("Fail", "States no Transition reaches from the initial State: %s" % "; ".join(bad[:3])) if bad else \
               ("Pass", "every State of %d Lifecycle(s) is reachable from its initial State" % len(lifecycles))

    if "undefined transition" in low or "undefined state transition" in low:
        bad = []
        for k, lc in lifecycles.items():
            names = state_names(r, lc)
            for a, b in transitions_of(r, lc):
                if a not in names or b not in names:
                    bad.append("%s: %s to %s" % (k, a, b))
        bad += workflow_violations(r, lifecycles, by_entity)
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "no Transition in %d Lifecycle(s) or %d Workflow(s) names an undefined State"
                % (len(lifecycles), len(r.records("workflow"))))

    if "violate entity lifecycle" in low or "violate lifecycle" in low:
        bad = workflow_violations(r, lifecycles, by_entity)
        return ("Fail", "; ".join(bad[:3])) if bad else \
               ("Pass", "%d Workflow(s) perform only Transitions their Entity's Lifecycle defines"
                % len(r.records("workflow")))

    return None, "deciding this prohibition needs evidence the export does not carry (a history, or a refusal record)"


def workflow_violations(r, lifecycles, by_entity):
    bad = []
    for _, wf in r.records("workflow"):
        for tr in wf.get("transitions", []) or []:
            entity = tr.get("entity")
            lc = lifecycles.get(by_entity.get(entity))
            if lc is None:
                bad.append("%s acts on %s, for which no Lifecycle resolves" % (wf.get("id"), entity))
            elif (tr.get("from"), tr.get("to")) not in set(transitions_of(r, lc)):
                bad.append("%s: %s to %s is not a Transition of %s's Lifecycle"
                           % (wf.get("id"), tr.get("from"), tr.get("to"), entity))
    return bad


def invariant(test, text, r):
    lifecycles, by_entity = lifecycle_index(r)
    parts = compound(text) if ("never:" in text or "shall not:" in text) else [text]
    return combine(parts, lambda part: invariant_predicate(part, r, lifecycles, by_entity))


def dangling_references(r):
    """Every id-valued field that names an identity the export does not declare.

    No Statement binds this check, so it is reported as an observation rather than a Test outcome:
    a report that verified every field of every record while the fields point at nothing would be
    true and useless.
    """
    known = set(r.ids())
    external = set(p for p in r.types.get("reference") or [])
    out = []
    for path, rec in r.all_records():
        if path in external:
            continue          # a Reference may legitimately name a target in another system
        for key, value in rec.items():
            if not isinstance(value, str) or not value or value in known:
                continue
            if re.match(r"^[A-Z][A-Z0-9-]{2,}$", value) and key not in ("id", "type", "name"):
                out.append("%s %s.%s names %s, which the export does not declare"
                           % (path, rec.get("id", "?"), key, value))
    return sorted(set(out))


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
    r = Resolver(model, types, fields)
    statement = load_statement(a.statement)
    catalogue = load_catalogue()
    register = load_register()

    results = []
    for test in catalogue:
        text = register.get(test["alias"], "")
        kind = test["kind"]
        if "descriptive" in (test.get("disposition") or "").lower():
            # Section 3: a Statement dispositioned Descriptive is Not Applicable, and the governance
            # record that dispositioned it is the authority, not this tool
            outcome, reason = "Not Applicable", "dispositioned Descriptive in the Alias File"
        elif kind == "Review":
            outcome, reason = None, "awaiting a named reviewer, per the kind this Test carries"
        elif kind == "Presence":
            outcome, reason = presence(test, text, r)
        elif kind == "Transition":
            outcome, reason = transition(test, text, r)
        elif kind == "Invariant":
            outcome, reason = invariant(test, text, r)
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

    mandatory = [r for r in results if r["class"] == "mandatory" and r["outcome"] != "Not Applicable"]
    not_applicable = [r for r in results if r["class"] == "mandatory" and r["outcome"] == "Not Applicable"]
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
    lines.append("| Not Applicable, dispositioned Descriptive | %d |" % len(not_applicable))
    lines.append("")
    lines.append("**Core Conformance: %s.** Section 3 establishes it when every mandatory Test is Pass or "
                 "Review Pass. %s" % ("established" if established else "not established",
                                      "" if established else
                                      "%d mandatory Test(s) fail and %d await a reviewer or evidence this export "
                                      "does not carry." % (len(failed), len(pending))))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Reference Integrity")
    lines.append("")
    dangling = dangling_references(r)
    if dangling:
        lines.append("%d field(s) name an identity the export does not declare. No Statement binds this "
                     "check, so it is an observation and not a Test outcome, but a model whose owner, "
                     "Domain or Lifecycle references resolve to nothing satisfies its Presence Tests while "
                     "meaning nothing." % len(dangling))
        lines.append("")
        for d in dangling[:20]:
            lines.append("- %s" % d)
    else:
        lines.append("Every identity-shaped field resolves to a record the export declares.")
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

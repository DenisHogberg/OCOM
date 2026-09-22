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
import datetime
import hashlib
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
    types, fields, declarations = {}, {}, {}
    for cells in read_table(path, "| OCOM type | Kind | Where it is in this export |"):
        if len(cells) < 3 or cells[1] != "collection":
            continue
        where = cells[2]
        if where.startswith("*"):            # the map says the export does not carry this type
            types[cells[0].lower()] = []
            continue
        types[cells[0].lower()] = [w.strip().strip("`") for w in where.split(",")]
    for cells in read_table(path, "| OCOM element | Kind | Field in the export |"):
        # a row of kind method names how records demonstrate integrity; it is read like a field
        # binding but its value is a method name, not a field of the export
        if len(cells) < 3:
            continue
        if cells[1] == "declaration":
            # a row of kind declaration states something about the export as a whole, such as the
            # scope of its identities (CAND-026); it names no field and is read by Declaration Tests
            declarations[cells[0].lower()] = cells[2].strip("`")
            continue
        if cells[1] not in ("field", "method"):
            continue
        fields[cells[0].lower()] = cells[2].strip("`")
    if not types:
        raise SystemExit("%s declares no type; the map is what makes the test possible" % path)
    return types, fields, declarations


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
            coll = model.get(p, [])
            if not isinstance(coll, list) or any(not isinstance(rec, dict) for rec in coll):
                raise SystemExit("the export's %s is not a list of records, so nothing in it can be checked" % p)
            for rec in coll:
                if id(rec) not in seen:
                    seen.add(id(rec))
                    out.append((p, rec))
    return out


# Object's own characteristics, the only elements a Type.<element> miss may fall back to. A wider
# fallback let one Object row in the map answer for every type and point a Test at another field.
OBJECT_ELEMENTS = ("identity", "identifier", "metadata")

EMPTY_STRINGS = {"", "null", "none", "n/a", "-", "tbd"}


def is_absent(value):
    """Structural emptiness, all the way down.

    No element of this vocabulary is satisfied by false, by zero or by the word null, and a list
    whose every member is one of those is a list of absences rather than a value.
    """
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, (int, float)):
        return value == 0
    if isinstance(value, str):
        return value.strip().lower() in EMPTY_STRINGS
    if isinstance(value, dict):
        return not value or all(is_absent(v) for v in value.values())
    if isinstance(value, (list, tuple, set)):
        return not value or all(is_absent(v) for v in value)
    return False


class Resolver:
    """The only way the engines touch the export, so every kind honours the Representation Map."""

    def __init__(self, model, types, fields, declarations=None):
        self.model, self.types, self.fields = model, types, fields
        self.declarations = declarations or {}

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

    GENERIC = ("object", "identity")

    def identity_of(self, path, record):
        """The identity the map binds for the records at `path`, resolved through the most specific
        type the path is listed under. Reading it through the first type in map order let the
        generic `Object` row, which every collection is listed under, answer for a collection that
        spells its identity otherwise: `identity_of` then returned None for every record there and
        the identity-reuse Invariant passed having counted them zero times. There is no fallback to
        a literal key: a record whose identity the map does not bind has no identity here, and the
        engines say so rather than guessing that it is called `id`."""
        # the most specific type's own bindings first, both elements, before any generic row:
        # asking self.field() took the generic Object row ahead of the type's own identifier row,
        # and looping elements outside types took Identity.identity ahead of Domain.identifier
        for type_name in self.specific_types(path):
            for element in ("identity", "identifier"):
                name = self.fields.get("%s.%s" % (type_name, element))
                if name:
                    return record.get(name)
        return None

    def specific_types(self, path):
        """The types the map lists `path` under, most specific first and deterministically ordered:
        a verdict must not depend on the order of rows in the map's Types table."""
        return sorted(t for t, paths in self.types.items() if path in paths and t not in self.GENERIC) \
               + sorted(t for t in self.GENERIC if path in self.types.get(t, []))

    def namespace_of(self, path):
        """The (scope, system) the map declares for the identities at `path`: a declaration keyed
        by the collection path first, then by the most specific OCOM type the path is listed under,
        then the export-wide `Identity.scope`; ("", "") when the map declares none. CAND-026 binds
        every identity to a declared scope, and an External System names the system, so two
        systems' keys coexist in one export as identities of two scopes."""
        d = self.declarations
        keys = [path.lower()] + self.specific_types(path) + ["identity"]
        # the scope and the system are resolved separately along the same order, so a type may
        # declare the scope once and each of its collections name its own source system
        scope = system = ""
        for key in keys:
            prefix = "%s.identity " % key if key != "identity" else "identity."
            if not scope and d.get(prefix + "scope"):
                scope = d[prefix + "scope"].strip().lower()
            if not system and d.get(prefix + "system"):
                system = d[prefix + "system"].strip()
        return (scope, system) if scope else ("", "")

    def identities(self):
        """Every identity the export declares, keyed by (scope, system, id), each record counted
        once: the same bare id under two declared systems is two identities, not one reused."""
        out = {}
        for path, rec in self.all_records():
            ident = self.identity_of(path, rec)
            if ident is not None and not is_absent(ident):
                key = self.namespace_of(path) + (ident,)
                out.setdefault(key, [])
                if path not in out[key]:
                    out[key].append(path)
        return out

    def object_paths(self):
        """The collection paths the map lists under Object or Identity. The no-reuse rule is about
        Objects, and a nested value record (a State, a Transition) carries no Identity of its own."""
        return [p for p in self.all_paths() if p in set(self.types.get("object", [])) | set(self.types.get("identity", []))]

    def undeclared_paths(self):
        """The collection paths the map declares no identity scope for. An empty scope is not a
        scope: keying uniqueness by it made "no declaration" a namespace of its own, so declaring a
        scope for one type exempted every other collection from the identity-reuse Invariant."""
        return [p for p in self.all_paths() if self.namespace_of(p) == ("", "")]

    def ids(self):
        """Every bare identity the export declares, as {id: [paths]}, for resolving references."""
        out = {}
        for (scope, system, ident), paths in self.identities().items():
            out.setdefault(ident, [])
            out[ident].extend(p for p in paths if p not in out[ident])
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

# a Statement that asks for one of something: "Every Entity shall have one responsible owner"
ONE = re.compile(r"\bshall (?:have|possess|define|carry|reference|belong to|contain|include) (?:exactly )?(?:one|a single)\b", re.I)


def one_of(subject, element, records, r):
    """The cardinality leg CAND-025 added to Presence. Every record carries exactly one value for
    the element, and, when the element is an owner and the map binds Ownership.owned object, the
    owner resolves to the one Ownership record that names the record: an Ownership record it names
    must name it back, and where several Ownership records name it (Shared Ownership) its owner
    must say which one is accountable. Returns (failure reason or None, note for the Pass reason)."""
    name, _ = r.field(subject, element)
    own_id, _ = r.field("ownership", "identifier")
    owned, _ = r.field("ownership", "owned object")
    owner_party, _ = r.field("ownership", "owner")
    ownership = [o for _, o in r.records("ownership")] if r.types.get("ownership") and owned else []
    resolved = 0
    for path, rec in records:
        value = rec.get(name)
        if isinstance(value, list):
            if len(value) != 1:
                return ("%s record %s carries %d values for %s where the Statement asks for one"
                        % (subject, rec.get("id", "?"), len(value), element)), ""
            value = value[0]
        if not ownership or "owner" not in element:
            continue
        ident = r.identity_of(path, rec)
        naming = [o for o in ownership if o.get(owned) == ident]
        by_id = [o for o in ownership if own_id and o.get(own_id) == value]
        if by_id:
            resolved += 1
            if not any(o is x for o in by_id for x in naming):
                return ("%s record %s names Ownership record %s, which names %s as its owned object and not it"
                        % (subject, ident, value, by_id[0].get(owned, "nothing"))), ""
        elif len(naming) > 1:
            accountable = [o for o in naming if owner_party and o.get(owner_party) == value]
            if len(accountable) != 1:
                return ("%d Ownership records name %s record %s and its %s (%s) says which of them is accountable to none of them"
                        % (len(naming), subject, ident, element, value)), ""
            resolved += 1
        elif len(naming) == 1:
            # exactly one Ownership record names it: the owner value must be that record or its party
            one = naming[0]
            if owner_party and one.get(owner_party) == value:
                resolved += 1
            else:
                return ("%s record %s names %s as its %s, which is neither the Ownership record that names it (%s) "
                        "nor the party that record names (%s)"
                        % (subject, ident, value, element, one.get(own_id, "?") if own_id else "?",
                           one.get(owner_party, "?") if owner_party else "?")), ""
        else:
            # no Ownership record names it and its owner names no Ownership record: nothing resolved,
            # and counting it as resolved let the Pass reason claim a resolution that never happened
            return ("%s record %s names %s as its %s, and no Ownership record names either it or that value"
                    % (subject, ident, value, element)), ""
    if not ownership or "owner" not in element:
        return None, ""
    return None, (", each resolving to the one Ownership record that names it" if resolved == len(records)
                  else ", %d of %d resolving to the one Ownership record that names it" % (resolved, len(records)))


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
    # a Statement asking for one of something is not established by the value being there either
    one_note = ""
    if ONE.search(text):
        for element in elements:
            failure, one_note = one_of(subject, element, records, r)
            if failure:
                return "Fail", failure
        one_note = ", one each" + one_note
    # a Statement asking for a unique value is not established by the value being there
    unique_note = ""
    if re.search(r"\bunique\b", text, re.I):
        for element in elements:
            name, _ = r.field(subject, element)
            if name is None:
                continue
            # unique within the scope the map declares for each record's collection (CAND-026):
            # the same bare value under two declared systems is two identities
            counts = {}
            for path, rec in records:
                key = r.namespace_of(path) + (rec.get(name),)
                counts[key] = counts.get(key, 0) + 1
            repeated = sorted({str(k[2]) for k, n in counts.items() if n > 1})
            if repeated:
                return "Fail", "%s is not unique across %s: %s" % (element, subject, ", ".join(repeated[:3]))
        unique_note = ", each distinct"
    note = "" if not borrowed else " (%s)" % "; ".join(borrowed)
    return "Pass", "%d %s record(s) carry %s%s%s%s" % (len(records), subject, ", ".join(elements), one_note, unique_note, note)


def lifecycle_index(r):
    """Lifecycles by identity, and the Lifecycle each Entity names, both read through the map."""
    lifecycles, collisions = {}, []
    for _, lc in r.records("lifecycle"):
        ident = r.value(lc, "lifecycle", "identifier") or lc.get("id")
        if not ident:
            collisions.append("a Lifecycle carries no identifier")
            continue
        if ident in lifecycles:
            collisions.append("two Lifecycles carry the identifier %s" % ident)
        lifecycles[ident] = lc
    if collisions:
        lifecycles["__collisions__"] = collisions
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
        field, _ = r.field("lifecycle", "terminal states")
        if field is None:
            return None, ("the Representation Map binds no field to Lifecycle.terminal states, so no terminal State "
                          "could be read; an export that declares none says so through the map")
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
        compared, bad, unresolved, destination_only = 0, [], [], []
        for _, e in events:
            subject = r.value(e, "event", "subject")
            before = r.value(e, "event", "from state")
            after = r.value(e, "event", "to state")
            if before is None and after is None:
                continue                      # records no State change at all
            named = by_entity.get(subject)
            if named is None or named not in permitted:
                unresolved.append(str(subject))
                continue
            if before is None:
                # a destination without a prior State is a creation when it names the initial State,
                # and Models/Lifecycle.md makes entering the initial State the start rather than a
                # Transition. Anything else is a State change that was not compared, and skipping it
                # silently let an Event move an Entity into a State its Lifecycle does not define
                if after not in state_names(r, lifecycles[named]):
                    bad.append("%s: to %s, a State the Lifecycle does not define" % (e.get("id"), after))
                elif after != r.value(lifecycles[named], "lifecycle", "initial state"):
                    destination_only.append(str(e.get("id")))
                continue
            compared += 1
            if (before, after) not in permitted[named]:
                bad.append("%s: %s to %s" % (e.get("id"), before, after))
        if bad:
            return "Fail", "State change the Lifecycle does not permit: %s" % "; ".join(bad[:3])
        if destination_only:
            return None, ("%d recorded State change(s) name a destination and no prior State (%s), so they could not "
                          "be compared against a Transition; every destination is a State its Lifecycle defines"
                          % (len(destination_only), destination_only[0]))
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
    if "__collisions__" in lifecycles:
        return "Fail", "; ".join(lifecycles["__collisions__"][:3])
    if not lifecycles:
        return "Fail", "the export carries no Lifecycle"
    return combine(compound(text), lambda part: transition_predicate(part, r, lifecycles, by_entity))


def invariant_predicate(text, r, lifecycles, by_entity):
    low = text.lower()

    if "identity" in low and "reused" in low:
        if not r.all_records():
            return "Fail", "the export carries no record, so no identity could be compared"
        paths = r.object_paths()
        if not paths:
            return None, ("the Representation Map lists no collection under Object or Identity, so the export "
                          "carries no Object whose identity could be compared")
        counts, unreadable, undeclared_ids = {}, {}, {}
        for path, rec in instances(r.model, paths):
            ident = r.identity_of(path, rec)
            if ident is None or is_absent(ident):
                unreadable[path] = unreadable.get(path, 0) + 1
                continue
            scope = r.namespace_of(path)
            counts[scope + (ident,)] = counts.get(scope + (ident,), 0) + 1
            if scope == ("", ""):
                undeclared_ids.setdefault(ident, 0)
                undeclared_ids[ident] += 1
        dupes = sorted({k[2] for k, n in counts.items() if n > 1})
        # a record whose scope the map does not declare is compared against every namespace, since
        # nothing says it is in a namespace of its own; otherwise one declaration row exempted the rest
        crossing = sorted(i for i, _ in undeclared_ids.items()
                          if sum(n for k, n in counts.items() if k[2] == i) > 1 and i not in dupes)
        if dupes or crossing:
            named = (dupes + crossing)[:3]
            return "Fail", ("%d identit%s carried by more than one record: %s%s"
                            % (len(dupes) + len(crossing), "y" if len(dupes) + len(crossing) == 1 else "ies",
                               ", ".join(named),
                               "" if not crossing else " (%d of them in a collection whose scope the map does not declare)" % len(crossing)))
        if unreadable:
            return None, ("%d Object record(s) carry no identity the Representation Map binds, so they could not "
                          "be compared (%s); bind the identity of every collection the map lists under Object"
                          % (sum(unreadable.values()), ", ".join(sorted(unreadable)[:3])))
        undeclared = [p for p in paths if r.namespace_of(p) == ("", "")]
        note = "" if not undeclared else (", %d of them in collection(s) whose scope the map does not declare (%s), compared against every namespace"
                                          % (sum(undeclared_ids.values()), ", ".join(sorted(undeclared)[:3])))
        return "Pass", "%d Object identities, each carried by exactly one record within its declared scope%s" % (len(counts), note)

    if "ownership" in low and ("never be undefined" in low or "not be undefined" in low):
        governed = [("entity", rec) for _, rec in r.records("entity")] + \
                   [("domain", rec) for _, rec in r.records("domain")]
        if not governed:
            return "Fail", "the export carries no governed record, so no Ownership could be checked"
        bad = []
        for type_name, rec in governed:
            field, _ = r.field(type_name, "owner")
            if field is None:
                return None, "the Representation Map binds no field to %s.owner" % type_name
            if is_absent(rec.get(field)):
                bad.append(str(rec.get("id")))
        return ("Fail", "no owner: %s" % ", ".join(bad[:3])) if bad else \
               ("Pass", "%d governed records each name an owner" % len(governed))

    if "primary governance" in low and "shared" in low:
        if not r.records("entity"):
            return "Fail", "the export carries no Entity"
        bad, seen = [], {}
        for _, e in r.records("entity"):
            domain = r.value(e, "entity", "domain")
            if isinstance(domain, list) and len(domain) > 1:
                bad.append("%s names %d primary Domains" % (e.get("id"), len(domain)))
        types_field, _ = r.field("domain", "entity types")
        if types_field is None:
            return None, "the Representation Map binds no field to Domain.entity types, so no overlap could be read"
        for path, d in r.records("domain"):
            ident = r.identity_of(path, d)
            for name in d.get(types_field) or []:
                if name in seen and seen[name] != ident:
                    bad.append("%s is governed by %s and %s" % (name, seen[name], ident))
                seen[name] = ident
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
    """Every step a Workflow records, read through the map, against the Lifecycle it acts on.

    The map is the only thing that knows where a Workflow keeps its steps. Reading them by the
    literal key `transitions` passed an export that calls them anything else, having looked at
    nothing, which is the defect this engine was refactored to remove and kept in one corner.
    """
    steps_field, _ = r.field("workflow", "transitions")
    if steps_field is None:
        return ["the Representation Map binds no field to Workflow.transitions, so no Workflow step could be read"]
    from_field, _ = r.field("transition", "from")
    to_field, _ = r.field("transition", "to")
    entity_field, _ = r.field("transition", "entity")
    bad = []
    for _, wf in r.records("workflow"):
        for tr in wf.get(steps_field) or []:
            entity = tr.get(entity_field or "entity")
            lc = lifecycles.get(by_entity.get(entity))
            if lc is None:
                bad.append("%s acts on %s, for which no Lifecycle resolves" % (wf.get("id"), entity))
            elif (tr.get(from_field or "from"), tr.get(to_field or "to")) not in set(transitions_of(r, lc)):
                bad.append("%s: %s to %s is not a Transition of %s's Lifecycle"
                           % (wf.get("id"), tr.get(from_field or "from"), tr.get(to_field or "to"), entity))
    return bad


def invariant(test, text, r):
    lifecycles, by_entity = lifecycle_index(r)
    if "__collisions__" in lifecycles:
        return "Fail", "; ".join(lifecycles["__collisions__"][:3])
    parts = compound(text) if ("never:" in text or "shall not:" in text) else [text]
    return combine(parts, lambda part: invariant_predicate(part, r, lifecycles, by_entity))


def dangling_references(r):
    """Every value that names something, and whether the export declares it.

    The first version of this check asked whether a string looked like one of the example's
    identifiers, which answered nothing for an export that writes identifiers any other way and
    still printed that every reference resolved. It now asks the only question worth asking, over
    every scalar and every member of every list: is this value an identity this export declares?
    """
    known = set(r.ids())
    if not known:
        return ["the export declares no identity, so no reference could be resolved"], 0
    scopes = {}
    for (scope, system, ident), _ in r.identities().items():
        scopes.setdefault(ident, set()).add((scope, system))
    external = set(r.types.get("reference") or [])
    # fields the map binds to prose are not references. Reading them off a list of literal key names
    # was the one place in the engine that did not go through the map, so an export that spelled a
    # reference "note" had it skipped and one that spelled prose "owner" had it resolved
    PROSE = ("name", "purpose", "meaning", "note", "rule", "expression", "trigger", "description",
             "responsibility scope", "classification name", "label", "type", "event type",
             "relationship type", "classification type", "data type")
    mapped_prose = set()
    for type_name in r.types:
        for element in PROSE:
            field = r.fields.get("%s.%s" % (type_name, element))
            if field:
                mapped_prose.add(field)
    skip_keys = mapped_prose | {"id", "type", "name", "label", "purpose", "meaning", "note", "rule",
                                "expression", "trigger", "data_type", "state", "initial_state"}
    # what a reference looks like is read off this export's own identities rather than assumed:
    # an export whose identities all carry a separator is one where a bare word is not a reference
    separated = sum(1 for i in known if "-" in i or "_" in i)
    needs_separator = separated > len(known) / 2
    def scalars(value, prefix):
        """Every string reachable through nested objects and lists, with the path that holds it.
        Reading only top-level values left a reference inside a provenance block unexamined while
        the report said every reference resolved."""
        if isinstance(value, dict):
            for k, v in value.items():
                if k in skip_keys:
                    continue
                for item in scalars(v, "%s.%s" % (prefix, k)):
                    yield item
        elif isinstance(value, list):
            for v in value:
                for item in scalars(v, prefix):
                    yield item
        elif isinstance(value, str) and value.strip():
            yield (prefix, value.strip())

    out, examined = [], 0
    for path, rec in r.all_records():
        if path in external:
            continue          # a Reference may legitimately name a target in another system
        ident = r.identity_of(path, rec) or rec.get("id", "?")
        for key, value in rec.items():
            if key in skip_keys:
                continue
            for where, item in scalars(value, key):
                if " " in item:
                    continue   # a sentence is not a reference
                if re.match(r"^\d{4}-\d{2}-\d{2}([T ]|$)", item):
                    continue   # a date carries separators and names nothing
                if item not in known:
                    # the shape heuristic decides only what an unknown value is: a value the export
                    # declares is a reference whatever it looks like, which is how a bare SAP or
                    # ServiceNow number reaches the ambiguity check at all
                    if needs_separator and "-" not in item and "_" not in item and not re.fullmatch(r"[0-9a-f]{64}", item):
                        continue
                    examined += 1
                    out.append("%s %s.%s names %s, which the export does not declare" % (path, ident, where, item))
                    continue
                examined += 1
                if len(scopes.get(item, ())) > 1:
                    out.append("%s %s.%s names %s, an identity the export declares in %d scopes (%s); the reference does not say which"
                               % (path, ident, where, item, len(scopes[item]),
                                  "; ".join(" ".join(x for x in s if x) for s in sorted(scopes[item]))))
    return sorted(set(out)), examined


# The demonstration clause 1 of CAND-024 asks for is to a party holding the record and its
# identity and nothing else. A digest stored inside the record shows that the record matches its
# own digest, which is consistency of the export and not evidence that nothing changed: alter the
# record, recompute the digest, and the export verifies again. An identity that IS the digest of
# the content is different: alter the content and the identity changes, so the holder of the old
# identity can tell. The tool therefore verifies both methods and passes only the second.
CONTENT_ADDRESSED = "content-addressed-identity"
SELF_CONTAINED = "sha256-canonical-json"
METHODS = (CONTENT_ADDRESSED, SELF_CONTAINED)


def canonical_digest(record, field):
    """SHA-256 over the record's JSON with `field` removed: keys sorted, separators without
    whitespace, non-ASCII kept as is, UTF-8, numbers as Python's json module writes them. This is
    a stated encoding, not RFC 8785 canonical JSON; a map that declares this method commits to it."""
    body = {k: v for k, v in record.items() if k != field}
    text = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def erasure_records(r):
    """Every erasure record the map declares (`Erasure` is the collection; `Erasure.erased record`,
    `Erasure.policy` and `Erasure.actor` its fields), as (identity, erased identity, reasons). The
    reasons are why the record grants no exclusion; an empty list grants it. Memory/Retention.md's
    Deleted state requires an erasure record to name a Policy the organization has declared and the
    actor who issued it (AO-085, a postscript to CAND-024), so a record naming neither is reported
    and the record it names is verified like any other."""
    if not r.types.get("erasure"):
        return []
    ident_f, _ = r.field("erasure", "identifier")
    erased_f, _ = r.field("erasure", "erased record")
    policy_f, _ = r.field("erasure", "policy")
    actor_f, _ = r.field("erasure", "actor")
    pol_id, _ = r.field("policy", "identifier")
    policies = {p.get(pol_id) for _, p in r.records("policy")} if r.types.get("policy") and pol_id else set()
    declared = set(r.ids())
    out = []
    for path, rec in r.records("erasure"):
        why = []
        ident_here = rec.get(ident_f) if ident_f else None
        if is_absent(ident_here):
            ident_here = r.identity_of(path, rec)
        if erased_f is None or is_absent(rec.get(erased_f)):
            why.append("names no erased record")
        elif rec.get(erased_f) == ident_here:
            why.append("names itself, so it would exclude itself from the verification it authorizes")
        elif declared and rec.get(erased_f) not in declared:
            why.append("names %s, which the export does not declare, so it excludes nothing" % rec.get(erased_f))
        if policy_f is None:
            why.append("the map binds no field to Erasure.policy")
        elif is_absent(rec.get(policy_f)):
            why.append("names no Policy")
        elif not policies:
            why.append("names Policy %s, but the export declares no Policy records to check it against" % rec.get(policy_f))
        elif rec.get(policy_f) not in policies:
            why.append("names Policy %s, which the export does not declare" % rec.get(policy_f))
        if actor_f is None:
            why.append("the map binds no field to Erasure.actor")
        elif is_absent(rec.get(actor_f)):
            why.append("names no actor")
        out.append((ident_here, rec.get(erased_f) if erased_f else None, why))
    return out


def erased_records(r):
    """Identities whose erasure record grants the exclusion Retention.md provides."""
    return {erased for _, erased, why in erasure_records(r) if erased and not why}


def integrity(test, text, r):
    """Verify the demonstration an implementation declares for the records a Statement calls
    immutable. The suite verifies a demonstration and never supplies one, so an export that
    declares none is pending, not passed (`Conformance-Test-Suite.md` Section 3)."""
    low = text.lower()
    if "audit record" in low:
        subject = "audit record"
    else:
        subject = subject_of(text, r.types) or pathlib.Path(test["document"]).stem.lower()
    if not r.types.get(subject):
        return None, "the Representation Map declares no %s records, so no demonstration could be verified" % subject
    method = (r.fields.get("integrity.method") or "").strip()
    if not method:
        return None, "the Representation Map declares no demonstration method (Integrity.method); a reviewer verifies the demonstration"
    if method not in METHODS:
        return None, "the declared method %s is not one this tool can verify; a reviewer verifies the demonstration" % method
    field, _ = r.field(subject, "integrity")
    if field is None:
        return None, "the Representation Map binds no field to %s.integrity, so no demonstration could be read" % subject
    records = r.records(subject)
    if not records:
        return "Fail", "the export carries no %s record" % subject
    erased = erased_records(r)
    bad, skipped = [], 0
    for path, rec in records:
        ident = r.identity_of(path, rec)
        if ident in erased:
            skipped += 1          # an erased record no longer verifies by design; Retention.md says what its demonstration means
            continue
        claimed = rec.get(field)
        if is_absent(claimed):
            bad.append("%s carries no demonstration" % (ident or "?"))
        elif claimed != canonical_digest(rec, field):
            bad.append("%s does not verify" % (ident or "?"))
    if bad:
        return "Fail", "%d of %d %s record(s) fail their demonstration: %s" % (len(bad), len(records), subject, "; ".join(bad[:3]))
    if skipped and len(records) - skipped == 0:
        return None, ("every %s record in the export (%d) is named by an erasure record, so no demonstration was "
                      "verified; the exclusion is granted by records the claimant writes, and a reviewer decides "
                      "whether the erasures are genuine" % (subject, len(records)))
    note = "" if not skipped else ", %d erased record(s) excluded as Retention.md's Deleted state provides" % skipped
    if method == SELF_CONTAINED:
        return None, ("%d %s record(s) match their own digest%s. That shows the export is consistent and not that a "
                      "record is unaltered: alter the record, recompute the digest, and it matches again. Clause 1 of "
                      "CAND-024 asks for a demonstration to a party holding only the record and its identity, which "
                      "content-addressed identity provides; a reviewer decides whether this digest is anchored elsewhere"
                      % (len(records) - skipped, subject, note))
    # the demonstration must be the identity this export resolves for the record, not a second field
    # beside it: comparing two map rows let a map bind Type.identity to the same column as
    # Type.integrity while every other leg resolved a different, mutable identity for the record
    for path, rec in records:
        if r.identity_of(path, rec) in erased:
            continue
        if r.identity_of(path, rec) != rec.get(field):
            return None, ("%s binds %s.integrity to %s, but the identity this export resolves for record %s is not "
                          "that value, so the identity does not address the content and the digest is a field beside "
                          "it; a reviewer decides whether it is anchored elsewhere"
                          % (subject, subject, field, r.identity_of(path, rec) or "?"))
    return "Pass", "%d %s record(s) are identified by the digest of their own content, so an altered record is a different record%s" % (len(records) - skipped, subject, note)


SCOPES = ("organization", "business domain", "registry", "external system", "global ecosystem")


def scope_declaration(test, text, r):
    """CAND-026: `Organizations shall define the appropriate scope for each Identity` is decided by
    the scope the Representation Map declares, in a row `Identity.scope` of kind declaration (or
    `<Type>.identity scope` for one type). One of the five scopes Meta/Identity.md names passes;
    any other fails; External System must also name its system; a map that declares none is pending,
    since the suite reads a declaration and never supplies one."""
    decl = {k: v for k, v in r.declarations.items() if k == "identity.scope" or k.endswith(".identity scope")}
    if not decl:
        return None, ("the Representation Map declares no Identity scope (a row `Identity.scope` of kind declaration); "
                      "CAND-026 asks the map to declare one of the five scopes Meta/Identity.md names")
    for key, value in sorted(decl.items()):
        if value.strip().lower() not in SCOPES:
            return "Fail", "%s declares %r, which is not one of the five scopes Meta/Identity.md names" % (key, value)
        if value.strip().lower() == "external system":
            system_key = key[:-len("scope")] + "system"
            if is_absent(r.declarations.get(system_key)):
                return "Fail", "%s declares External System and names no system (a row %s of kind declaration)" % (key, system_key)
    uncovered = [p for p in r.all_paths() if r.namespace_of(p) == ("", "")]
    if uncovered:
        return "Fail", ("the map declares %s, which covers no identity in %d of the export's collections (%s); "
                        "CAND-026 binds every identity the export carries to a declared scope"
                        % ("; ".join("%s = %s" % (k, v) for k, v in sorted(decl.items())), len(uncovered),
                           ", ".join(sorted(uncovered)[:3])))
    return "Pass", "the map declares %s" % "; ".join(
        "%s for %s" % (v, "every identity the export carries" if k == "identity.scope" else "%s identities" % k.split(".")[0])
        for k, v in sorted(decl.items()))


REVIEW_OUTCOMES = ("Review Pass", "Review Fail")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December")


def readable_date(value):
    """A date the tool can read and that exists: the shape check accepted 2026-13-45."""
    m = re.match(r"^(\d{1,2}) (%s) (\d{4})$" % "|".join(MONTHS), value)
    if m:
        day, month, year = int(m.group(1)), MONTHS.index(m.group(2)) + 1, int(m.group(3))
    else:
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", value)
        if not m:
            return False
        year, month, day = (int(x) for x in m.groups())
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    return True


def review_tables(path):
    """Every table under the Reviewer Record's header, not just the first. read_table reads one
    table, so a second table of judgments sat in the file unread and unreported."""
    text = pathlib.Path(path).read_text(encoding="utf-8")
    header = "| Test | Outcome | Reviewer | Date | Reason |"
    return text.count(header)


def load_reviews(path, known_aliases):
    """The Reviewer Record: one named judgment per Test, read fail-closed. Section 3 makes a Review
    Pass a named reviewer's recorded judgment with a reason, and Section 4 makes the reviewer's
    identity part of the report, so a row without a Test the catalogue carries, a permitted outcome,
    a name, a readable date or a reason, and a second row for one Test, stop the run rather than
    being skipped: a judgment that cannot be attributed is not a judgment."""
    tables = review_tables(path)
    if tables != 1:
        raise SystemExit("%s carries %d tables under the header '| Test | Outcome | Reviewer | Date | Reason |'; "
                         "a Reviewer Record is one table, so that no judgment sits in the file unread" % (path, tables))
    rows = read_table(path, "| Test | Outcome | Reviewer | Date | Reason |")
    if not rows:
        raise SystemExit("%s carries no reviewer row under the header '| Test | Outcome | Reviewer | Date | Reason |'" % path)
    out = {}
    for cells in rows:
        if len(cells) != 5:
            raise SystemExit("%s: a reviewer row has %d cell(s) and five are required: %s" % (path, len(cells), " | ".join(cells)[:80]))
        alias, outcome, reviewer, date, reason = (c.strip() for c in cells)
        if alias not in known_aliases:
            raise SystemExit("%s: %s names a Test the catalogue does not carry" % (path, alias))
        if outcome not in REVIEW_OUTCOMES:
            raise SystemExit("%s: %s records %r; a reviewer records Review Pass or Review Fail" % (path, alias, outcome))
        if len(re.sub(r"[^0-9A-Za-z\u0400-\u04ff]", "", reviewer)) < 2 or reviewer.lower() in EMPTY_STRINGS:
            raise SystemExit("%s: %s carries no reviewer this tool can read (%r); a Review outcome is a named "
                             "reviewer's judgment and the report carries the name" % (path, alias, reviewer[:40]))
        if not readable_date(date):
            raise SystemExit("%s: %s carries a date this tool cannot read: %r (D Month YYYY or YYYY-MM-DD, and a date that exists)" % (path, alias, date))
        if len(re.sub(r"[^0-9A-Za-z\u0400-\u04ff]", "", reason)) < 10 or reason.lower() in EMPTY_STRINGS:
            raise SystemExit("%s: %s carries no reason this tool can read (%r); a judgment without one cannot be contested" % (path, alias, reason[:40]))
        if alias in out:
            raise SystemExit("%s: two rows judge %s; a Test carries one judgment" % (path, alias))
        out[alias] = {"outcome": outcome, "reviewer": reviewer, "date": date, "reason": reason}
    return out


def short_reason(reason):
    """A reason cut at a byte boundary with no marker hid the half of a reviewer's judgment that
    qualified it. The cut is now visible and says where the whole of it lives."""
    reason = (reason or "").replace("|", "\\|")
    return reason if len(reason) <= 180 else reason[:160].rstrip() + " ... (cut here; the whole reason is in the Reviewer Record)"


def file_digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()[:16]


def manifest_release():
    """The Release Identifier and Commit of the last Manifest entry that names a commit. Section 4
    requires both in a report, and the report carried neither."""
    text = (ROOT / "docs" / "Governance" / "Publication-Manifest.md").read_text(encoding="utf-8")
    release, commit = "(not recorded)", "(not recorded)"
    for m in re.finditer(r"## Release: `([^`]+)`(.*?)(?=\n## |\Z)", text, re.S):
        c = re.search(r"\| \*\*Commit\*\* \| `([0-9a-f]{7,40})`", m.group(2))
        if c:
            release, commit = m.group(1), c.group(1)
    return release, commit


def register_count():
    return sum(1 for line in REGISTER.read_text(encoding="utf-8").splitlines() if line.startswith("| REQ-"))


def alias_revision():
    """The Alias File is append-only and carries no version, so its revision is the date it was last
    updated and the number of aliases it holds: what a later reader needs to reproduce this run."""
    text = (ROOT / "docs" / "Governance" / "Requirement-Aliases.md").read_text(encoding="utf-8")
    m = re.search(r"(?m)^\*\*Last Updated:\*\* (.+)$", text)
    dates = re.findall(r"(?m)^\| REQ-[^|]+\|[^|]*\|[^|]*\|[^|]*\| (\d{1,2} [A-Z][a-z]+ \d{4}) \|", text)
    rows = sum(1 for line in text.splitlines() if line.startswith("| REQ-"))
    last = sorted(set(dates))[-1] if dates else (m.group(1).strip() if m else "(no date)")
    return "%d aliases, last appended %s" % (rows, last)


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
    p.add_argument("--reviews", help="the Reviewer Record: a Markdown table of named judgments on the Tests no procedure decided")
    a = p.parse_args(argv)

    model = json.loads(pathlib.Path(a.model).read_text(encoding="utf-8"))
    types, fields, declarations = load_map(a.map)
    r = Resolver(model, types, fields, declarations)
    statement = load_statement(a.statement)
    catalogue = load_catalogue()
    register = load_register()

    results = []
    for test in catalogue:
        text = register.get(test["alias"], "")
        kind = test["kind"]
        if (test.get("disposition") or "").strip().lower() == "descriptive":
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
        elif kind == "Integrity":
            outcome, reason = integrity(test, text, r)
        elif kind == "Declaration":
            outcome, reason = scope_declaration(test, text, r)
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

    # the Reviewer Record decides what no procedure decided: a Review Test, or a mechanical Test the
    # export could not settle. It never overrides a mechanical Pass or Fail (Section 3 binds Review
    # Pass to Statements no mechanical procedure can decide), and the rows it could not apply are reported
    reviews = load_reviews(a.reviews, {r["alias"] for r in results}) if a.reviews else {}
    not_applied = []
    for row in results:
        judgment = reviews.get(row["alias"])
        if not judgment:
            continue
        if row["outcome"] is None:
            row["outcome"] = judgment["outcome"]
            row["reason"] = "%s, %s: %s" % (judgment["reviewer"], judgment["date"], judgment["reason"])
        else:
            not_applied.append("%s: %s recorded %s, but the Test decided %s mechanically and a judgment does not override it"
                               % (row["alias"], judgment["reviewer"], judgment["outcome"], row["outcome"]))

    mandatory = [r for r in results if r["class"] == "mandatory" and r["outcome"] != "Not Applicable"]
    not_applicable = [r for r in results if r["class"] == "mandatory" and r["outcome"] == "Not Applicable"]
    passed = [r for r in mandatory if r["outcome"] == "Pass"]
    failed = [r for r in mandatory if r["outcome"] == "Fail"]
    review_passed = [r for r in mandatory if r["outcome"] == "Review Pass"]
    review_failed = [r for r in mandatory if r["outcome"] == "Review Fail"]
    pending = [r for r in mandatory if r["outcome"] is None]
    established = not failed and not review_failed and not pending
    reviewers = sorted({j["reviewer"] for j in reviews.values()})

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
    lines.append("**Inputs, by content:** model `%s`, map `%s`, Conformance Statement `%s` (SHA-256 of each file as read). "
                 "A Review outcome below was recorded against these three; a judgment carried to a different export is a "
                 "judgment about something else." % (file_digest(a.model), file_digest(a.map), file_digest(a.statement)))
    lines.append("")
    release, commit = manifest_release()
    lines.append("**Tested against:** Release %s, commit `%s`, per `Governance/Publication-Manifest.md`. "
                 "Requirement Register: %d Statements. Alias File revision: %s."
                 % (release, commit, register_count(), alias_revision()))
    lines.append("")
    lines.append("**Published by:** the party that ran the suite. A report published by the claimant is "
                 "self-validation; `Conformance-Test-Suite.md` Section 4 says the suite does not tell the two "
                 "apart and the publisher does.")
    lines.append("")
    if reviews:
        lines.append("**Reviewer Record:** `%s`, %d judgment(s) by %s. Whether a reviewer is independent of the "
                     "claimant is a fact about the reviewer, not something this tool can read." % (a.reviews, len(reviews), ", ".join(reviewers)))
    else:
        lines.append("**Reviewer Record:** none supplied; every Review Test is pending. Section 3 makes a Review "
                     "outcome a named reviewer's recorded judgment, supplied to this tool as `--reviews`.")
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
    lines.append("| Review Pass | %d |" % len(review_passed))
    lines.append("| Review Fail | %d |" % len(review_failed))
    lines.append("| Awaiting a reviewer or evidence the export does not carry | %d |" % len(pending))
    lines.append("| Not Applicable, dispositioned Descriptive | %d |" % len(not_applicable))
    lines.append("")
    lines.append("**Core Conformance: %s.** Section 3 establishes it when every mandatory Test is Pass or "
                 "Review Pass. %s" % ("established" if established else "not established",
                                      "" if established else
                                      "%d mandatory Test(s) fail, %d carry a Review Fail, and %d await a reviewer or "
                                      "evidence this export does not carry." % (len(failed), len(review_failed), len(pending))))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Reference Integrity")
    lines.append("")
    dangling, examined = dangling_references(r)
    if dangling:
        lines.append("%d field(s) name an identity the export does not declare, or one it declares in more "
                     "than one scope. No Statement binds this check, so it is an observation and not a Test "
                     "outcome, but a model whose owner, Domain or Lifecycle references resolve to nothing, or to "
                     "two records, satisfies its Presence Tests while meaning nothing." % len(dangling))
        lines.append("")
        for d in dangling[:20]:
            lines.append("- %s" % d)
    else:
        lines.append("%d field value(s) were resolved against the %d identities this export declares, and "
                     "every one of them names a record it carries in exactly one declared scope. Fields holding "
                     "prose, and a Reference's target, which may legitimately name another system, are not resolved."
                     % (examined, len(r.identities())))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Erasure Records")
    lines.append("")
    erasures = erasure_records(r)
    if not r.types.get("erasure"):
        lines.append("The Representation Map declares no Erasure records, so no record was excluded from an "
                     "Integrity Test on that ground. `Memory/Retention.md` is outside the requirement set, so "
                     "this is an observation and not a Test outcome.")
    else:
        granted = [e for e in erasures if not e[2]]
        lines.append("%d erasure record(s); %d grant the exclusion `Memory/Retention.md`'s Deleted state provides, "
                     "naming a Policy the export declares and an actor. The records the others name were verified "
                     "like any other. `Memory/Retention.md` is outside the requirement set, so this is an observation "
                     "and not a Test outcome." % (len(erasures), len(granted)))
        lines.append("")
        for ident, erased, why in erasures[:20]:
            if why:
                lines.append("- %s names %s and grants no exclusion: %s" % (ident or "?", erased or "no record", "; ".join(why)))
            else:
                lines.append("- %s names %s: exclusion granted" % (ident or "?", erased))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Reviewers")
    lines.append("")
    if not reviews:
        lines.append("No Reviewer Record was supplied. Section 4 requires the reviewer's identity for every Review outcome, "
                     "so a report without one carries no Review outcome.")
    else:
        for name in reviewers:
            judged = [alias for alias, j in reviews.items() if j["reviewer"] == name]
            lines.append("- %s: %d judgment(s), %s" % (name, len(judged), ", ".join(sorted(judged)[:12]) + (" ..." if len(judged) > 12 else "")))
        for line in not_applied:
            lines.append("- not applied, %s" % line)
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
                        r["outcome"] or "pending", short_reason(r["reason"])))
    report = "\n".join(lines) + "\n"

    if a.report:
        pathlib.Path(a.report).write_text(report, encoding="utf-8")
        print("wrote %s" % a.report)
    print("mandatory %d: Pass %d, Fail %d, pending %d, reviewed %d pass and %d fail. Core Conformance %s."
          % (len(mandatory), len(passed), len(failed), len(pending), len(review_passed), len(review_failed),
             "established" if established else "not established"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

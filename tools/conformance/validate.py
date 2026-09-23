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
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "docs" / "Governance" / "Test-Catalogue.md"
REGISTER = ROOT / "docs" / "Governance" / "Requirement-Register.md"
ALIASES = ROOT / "docs" / "Governance" / "Requirement-Aliases.md"

ARTICLES = ("a ", "an ", "the ")
ADJECTIVES = ("unique ", "stable ", "defined ", "explicit ", "valid ", "primary ", "single ",
              "exactly one ", "one or more ", "at least one ", "one ", "its ", "their ", "each ")
THING_VERBS = ("possess", "contain", "define", "have", "carry", "include", "specify", "record",
               "reference", "assign", "state", "identify", "be assigned")


def read_table(path, header_starts, whole_file=True):
    """Every row of the table whose header starts with `header_starts`.

    Reading it as one contiguous block stopped at the first line that is not a row, so a single
    blank line inside the Tests table dropped every row below it: the run reported no error and the
    report computed the size of the measured set from the same truncated read."""
    rows, in_table, width = [], False, None
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith(header_starts):
            in_table = True
            width = len(line.strip().strip("|").split("|"))
            continue
        if in_table and line.startswith("#"):
            break                       # the table ends with its section, not with its first gap
        if not in_table or not line.startswith("|"):
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if width is not None and len(cells) != width:
            continue                    # a row of another table under the same heading
        rows.append(cells)
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
        if cells[0].lower() == "integrity.method" and cells[1] != "method":
            # `Adoption/Reference Serialization.md` called this row a declaration until 23 September
            # 2026, and a map written to that page had every Integrity Test report pending with a
            # reason saying the map declares no method, which is a silence the map did not intend
            raise SystemExit("%s carries Integrity.method as kind %r; it is kind `method`, and read as anything "
                             "else it declares no demonstration method at all" % (path, cells[1]))
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


def keyable(value):
    """An identity this tool can use as a dictionary key, or None.

    A record carrying a list or an object where its identity should be is a record the engines
    cannot index, and every leg that keyed on it directly raised TypeError and wrote no report at
    all. The legs that decide identity (the uniqueness leg, the reuse Invariant) report it; the
    legs that only index by it skip it."""
    return None if isinstance(value, (list, dict)) else value


def collection_at(node, path):
    """The records of the collection `path` names, resolved from `node`.

    A path is a key, with `[]` to step through each record of a list and `{}` through each value of
    an object, and dots between the steps: `entities`, `lifecycles[].states`, `staging.shadow`,
    `by_id{}`. The walk that finds collections the map does not list emits this same grammar, and
    it emitted paths this function could not read, which came back empty and read as "this
    collection carries no identity" rather than "this collection was not examined"."""
    if not isinstance(node, dict):
        return []
    step, _, rest = path.partition(".")
    through = step[-2:] if step.endswith(("[]", "{}")) else ""
    value = node.get(step[:-2] if through else step)
    if rest:
        if through == "[]":
            return [rec for item in (value if isinstance(value, list) else [])
                    if isinstance(item, dict) for rec in collection_at(item, rest)]
        if through == "{}":
            return [rec for item in (value.values() if isinstance(value, dict) else [])
                    if isinstance(item, dict) for rec in collection_at(item, rest)]
        return collection_at(value, rest)
    if through == "{}":
        return [x for x in value.values() if isinstance(x, dict)] if isinstance(value, dict) else []
    if isinstance(value, dict):
        return [value]          # one record, stored as an object value rather than in a list
    return [x for x in value if isinstance(x, dict)] if isinstance(value, list) else []


def parents_of(model, path):
    """Every node a path's last step is resolved from, so the leaf can be checked where it lives."""
    head, _, leaf = path.rpartition(".")
    if not head:
        return [model]
    out = []
    node = model
    for step in head.split("."):
        through = step[-2:] if step.endswith(("[]", "{}")) else ""
        key = step[:-2] if through else step
        nodes = [node] if not isinstance(node, list) else node
        nxt = []
        for item in nodes:
            if not isinstance(item, dict):
                continue
            value = item.get(key)
            if through == "[]":
                nxt += [x for x in (value if isinstance(value, list) else []) if isinstance(x, dict)]
            elif through == "{}":
                nxt += [x for x in (value.values() if isinstance(value, dict) else []) if isinstance(x, dict)]
            elif isinstance(value, dict):
                nxt.append(value)
        node = nxt
        out = nxt
    return out if out else []


def instances(model, paths, strict=True):
    """Every record the collection paths point at, as (path, record), each record once.

    `strict` is for the paths the Representation Map states: a map that lists a collection which is
    not a list of records has said something false about the export, and the run stops. The walk
    over collections the map does not list reads the same grammar without that demand."""
    out, seen = [], set()
    for p in dict.fromkeys(paths):
        if strict:
            # the refusal applied to top-level paths only, so every nested collection the map
            # states (`entities[].attributes`, `lifecycles[].states`) was exempt from it and a
            # non-record member there was filtered away instead of stopping the run
            for parent in parents_of(model, p):
                leaf = p.rsplit(".", 1)[-1]
                leaf = leaf[:-2] if leaf.endswith(("[]", "{}")) else leaf
                coll = parent.get(leaf, [])
                if p.endswith("{}"):
                    if not isinstance(coll, dict) or any(not isinstance(rec, dict) for rec in coll.values()):
                        raise SystemExit("the export's %s is not a collection of records, so nothing in it can be checked" % p)
                elif isinstance(coll, dict):
                    continue    # one record stored as an object value, which collection_at reads and
                                # the walk emits: refusing it here meant the map could not state the
                                # one shape the Declaration Test failed the export for not stating
                elif not isinstance(coll, list):
                    raise SystemExit("the export's %s is not a list of records, so nothing in it can be checked" % p)
                elif any(isinstance(rec, dict) for rec in coll) and any(not isinstance(rec, dict) for rec in coll):
                    raise SystemExit("the export's %s mixes records with values that are not records, so what the "
                                     "map says lives there cannot be read" % p)
                elif coll and not any(isinstance(rec, dict) for rec in coll):
                    continue    # States written as bare strings: the map is right about where they
                                # live, and the legs that read scalars read them
        for rec in collection_at(model, p):
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
        # the model is read once and never written, so what is derived from it is derived once.
        # `identities()` walks every record, and the ownership leg called it per record: a
        # 5,000-entity export produced no report in fifteen minutes because of it
        self._identities = None
        self._namespaces = {}
        self._specific = {}

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
        if path not in self._specific:
            self._specific[path] = sorted(t for t, paths in self.types.items()
                                          if path in paths and t not in self.GENERIC) \
                                   + sorted(t for t in self.GENERIC if path in self.types.get(t, []))
        return self._specific[path]

    def namespace_of(self, path):
        if path in self._namespaces:
            return self._namespaces[path]
        out = self._namespace_of(path)
        self._namespaces[path] = out
        return out

    def _namespace_of(self, path):
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
                # the scope was folded and the system was not, so SAP and sap were two namespaces
                # and one reused identity was counted as two identities
                system = d[prefix + "system"].strip().casefold()
        # only an External System scope is split by the system it names. Keying every scope by a
        # declared system let one map row turn one Organization into two namespaces, and a reused
        # identity then passed the no-reuse Invariant
        if scope != "external system":
            system = ""
        return (scope, system) if scope else ("", "")

    def identities(self):
        """Every identity the export declares, keyed by (scope, system, id), each record counted
        once: the same bare id under two declared systems is two identities, not one reused."""
        if self._identities is not None:
            return self._identities
        out = {}
        for path, rec in self.all_records():
            ident = self.identity_of(path, rec)
            if isinstance(ident, (list, dict)):
                ident = "%s (%d values)" % (path, len(ident))   # unhashable, and reported as one identity
            if ident is not None and not is_absent(ident):
                key = self.namespace_of(path) + (ident,)
                out.setdefault(key, [])
                if path not in out[key]:
                    out[key].append(path)
        self._identities = out
        return out

    def object_paths(self):
        """Every collection whose records carry an identity the map binds. Restricting this to the
        rows listed under Object or Identity excluded collections the map does binds an identity for
        (the example's lifecycles and ownership), so the report counted 38 identities and compared
        30. A nested value record with no identity binding (a State, a Transition) still falls out,
        because identity_of returns None for it."""
        declared = set(self.types.get("object", [])) | set(self.types.get("identity", []))
        names = self.identity_field_names()
        out = []
        for path in self.all_paths():
            if path in declared:
                out.append(path)            # an Object collection stays in even if nothing resolves,
                continue                    # so the unresolved records are reported rather than dropped
            records = instances(self.model, [path])
            # a collection listed only under a type for which the map binds no identity resolved
            # nothing here and was skipped by the unlisted-collection rule for being listed, so it
            # fell out of both identity Tests; its records carry identities all the same
            if records and any(self.identity_of(p, rec) is not None or
                               any(not is_absent(rec.get(name)) for name in names) for p, rec in records):
                out.append(path)
        return out

    def identity_field(self, path):
        """The field name the map binds as the identity of the records at `path`, or None."""
        for type_name in self.specific_types(path):
            for element in ("identity", "identifier"):
                name = self.fields.get("%s.%s" % (type_name, element))
                if name:
                    return name
        return None

    def identity_field_names(self):
        """Every field name the map binds as an identity or identifier, for any type. A collection
        the map does not list is outside every Test; whether its records carry identities decides
        which Statement that offends, and the map is the only thing that says what an identity is
        called in this export."""
        return {v for k, v in self.fields.items()
                if (k.endswith(".identity") or k.endswith(".identifier")) and v}

    def record_collections(self):
        """Every collection of records the export carries, at any depth, in the map's own path
        notation (`entities`, `lifecycles[].states`). The unlisted-collection rule read the top
        level only, so a collection of records placed inside a record was listed by nothing,
        reached no Test, and reused an identity with both identity Tests passing."""
        out = []

        names = self.identity_field_names()

        def walk(value, prefix):
            if not isinstance(value, dict):
                return
            for key, sub_value in value.items():
                path = prefix + key
                if isinstance(sub_value, list):
                    # one non-record member beside the records made the whole collection invisible,
                    # and a list of lists was neither listed nor descended into
                    if any(isinstance(x, dict) for x in sub_value):
                        out.append(path)
                        for record in sub_value:
                            if isinstance(record, dict):
                                walk(record, path + "[].")
                    elif any(isinstance(x, list) and any(isinstance(y, dict) for y in x) for x in sub_value):
                        out.append(path)          # records nested in a list of lists: no path names them
                elif isinstance(sub_value, dict):
                    members = list(sub_value.values())
                    # a single record stored as an object value is a collection of one: walking
                    # into it as though it were a container emitted nothing, so the identity it
                    # carries was compared against none of the others
                    if any(not is_absent(sub_value.get(name)) for name in names):
                        out.append(path)
                        walk(sub_value, path + ".")
                    # an object keyed by identity is a collection of records however it is spelled
                    elif members and all(isinstance(x, dict) for x in members) \
                            and any(not is_absent(x.get(name)) for x in members for name in names):
                        out.append(path + "{}")
                        for record in members:
                            walk(record, path + "{}.")
                    else:
                        walk(sub_value, path + ".")

        walk(self.model, "")
        # one path per collection, not one per parent record: `lifecycles[].states` is one
        # collection of the map's grammar however many Lifecycles carry it
        return list(dict.fromkeys(out))

    def unlisted_collections(self):
        """Three populations, because they are three different offences and each needs its own
        sentence: collections of records the map lists nowhere; collections the map lists only
        under a type for which it binds no identity, whose records carry an identity it binds
        elsewhere; and collections whose records carry no identity this map binds at all. Returning
        the first two as one list told a map author to list a collection their map already lists."""
        names = self.identity_field_names()
        listed = set(self.all_paths())
        unlisted, unbound, without = [], [], []
        for path in self.record_collections():
            records = instances(self.model, [path], strict=False)
            # a collection this tool could not read is not a collection that carries no identity:
            # classifying it as harmless is how a reused identity was named in a Pass reason
            carries = not records or any(not is_absent(rec.get(name)) for _, rec in records for name in names)
            if path not in listed:
                (unlisted if carries else without).append(path)
            elif not self.identity_field(path) and carries:
                unbound.append(path)
        return sorted(unlisted), sorted(unbound), sorted(without)

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


PROCESS_NOUNS = ("governance", "management", "enforcement", "resolution", "integration",
                 "communication", "evolution", "assessment", "review", "validation", "conformance")


def subject_of(text, types):
    """The OCOM type a Statement is about, as the map spells it."""
    m = re.match(r"\s*(?:Every|Each|All|An|A|The)?\s*([A-Za-z][A-Za-z ]*?)\s+(?:shall|should|may)\b", text)
    if not m:
        return None
    words = m.group(1).strip().split()
    # a phrase whose head noun is a process is about the process, not about a type: "Constraint
    # governance shall define: ownership; approval" asks what an organization's governance defines,
    # and resolving it to the Constraint type made a Presence Test look for those as fields
    if words and words[-1].lower().rstrip("s") in PROCESS_NOUNS:
        return None
    # otherwise both ends of the phrase: reading only the trailing words left "Every Ownership
    # assignment shall define:" unresolved, and the tool then said the map declares no such type
    for n in range(len(words), 0, -1):
        for phrase in (" ".join(words[-n:]), " ".join(words[:n])):
            candidate = phrase.lower().rstrip("s") or phrase.lower()
            for name in (candidate, candidate + "s", phrase.lower()):
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
    the element, and, when the element is an owner, the owner resolves to the one Ownership record
    that names the record: an Ownership record it names must name it back, and where several
    Ownership records name it (Shared Ownership) its owner must say which one is accountable.
    Returns (failure, note, pending), where pending is a reason the leg could not run: returning it
    as a note appended it to a Pass, which is what a leg that ran nothing must never produce."""
    name, _ = r.field(subject, element)
    own_id, _ = r.field("ownership", "identifier")
    owned, _ = r.field("ownership", "owned object")
    owner_party, _ = r.field("ownership", "owner")
    # CAND-025 counts "exactly one Ownership record of the accountable Type per Entity". Which
    # Ownership Type an organization declares accountable is the organization's own (Meta/Ownership.md
    # lists eight), so the map declares it, in a row `Ownership.accountable type` of kind declaration,
    # and binds `Ownership.type`. Nothing read either, so the Type half of the Decision was enforced
    # by nothing and the reason said otherwise
    type_field, _ = r.field("ownership", "type")
    accountable_type = (r.declarations.get("ownership.accountable type") or "").strip().lower()
    reads_type = bool(type_field and accountable_type)
    # half a declaration is not a declaration: with one row present and the other missing the leg
    # silently stopped counting Ownership Types and its reason said the map declared neither
    half_declared = ("the map declares an accountable Ownership Type (%s) and binds no field to Ownership.type"
                     % r.declarations.get("ownership.accountable type")) if accountable_type and not type_field else (
                    "the map binds a field to Ownership.type and declares no accountable Ownership Type "
                    "(a row `Ownership.accountable type`)" if type_field and not accountable_type else "")
    declares_ownership = bool(r.types.get("ownership"))
    ownership = [(p, o) for p, o in r.records("ownership")] if declares_ownership and owned else []
    if "owner" in element and half_declared:
        return None, "", ("%s, so the one Ownership record of the accountable Type could not be counted" % half_declared)
    if "owner" in element and not ownership:
        # the leg used to disappear silently whenever the map said nothing. Round 2 closed two of
        # the three ways out and left the third: a map that lists no Ownership collection at all
        # skipped the whole resolution, so the same export Failed with the row and Passed without
        # it, and the claimant, who writes the map, chose the verdict in one line
        return None, "", ("%s, so no owner could be resolved to the Ownership record that names it"
                          % ("the Representation Map lists no Ownership collection" if not declares_ownership
                             else "the map declares an Ownership collection but binds no field to Ownership.owned object"
                             if not owned else
                             "the map declares an Ownership collection but the export carries no Ownership record"))
    # one index for the whole leg: rebuilt per record, this walked every identity in the export
    # once per record and made the run quadratic
    by_identity = {}
    for s, sy, i in r.identities():
        by_identity.setdefault(i, set()).add((s, sy))
    resolved, shared = 0, 0
    failures, undecided = [], []
    for path, rec in records:
        value = rec.get(name)
        if isinstance(value, list):
            if len(value) != 1:
                failures.append("%s record %s carries %d values for %s where the Statement asks for one"
                                % (subject, rec.get("id", "?"), len(value), element))
                continue
            value = value[0]
        if not ownership or "owner" not in element:
            continue
        ident = r.identity_of(path, rec)
        if ident is None or is_absent(ident) or not keyable(ident):
            # None == None matched an Entity with no identity to an Ownership record with no owned
            # object, and the Pass reason then said "the one Ownership record that names it"
            undecided.append("%s record %s carries no identity the map binds, so no Ownership record could be "
                             "resolved to it" % (subject, rec.get("id", "?")))
            continue
        spaces = by_identity.get(ident) or set()
        if len(spaces) > 1:
            # `Adoption/Reference Serialization.md`: a bare reference to an identity the export
            # declares in two namespaces is ambiguous and is not resolved to either. Comparing the
            # scope alone put every source system in one namespace, so a ServiceNow Entity resolved
            # to the SAP Entity's Ownership record and the reason claimed the one record that names it
            undecided.append("%s record %s carries an identity the export declares in %d namespaces (%s), so a bare "
                             "reference to it names no one record and the Ownership record that names it could not "
                             "be resolved"
                             % (subject, ident, len(spaces),
                                "; ".join(sorted(" ".join(x for x in s if x) or "no declared scope" for s in spaces))))
            continue
        naming = [o for _, o in ownership if not is_absent(o.get(owned)) and o.get(owned) == ident]
        by_id = [o for _, o in ownership if own_id and o.get(own_id) == value]
        if by_id and not any(o is x for o in by_id for x in naming):
            failures.append("%s record %s names Ownership record %s, which names %s as its owned object and not it"
                            % (subject, ident, value, by_id[0].get(owned, "nothing")))
            continue
        if reads_type and naming:
            # the accountable Type is declared: the count CAND-025 asks for is over the records of
            # that Type, whatever the owner value points at
            of_type = [o for o in naming if str(o.get(type_field, "")).strip().lower() == accountable_type]
            if len(of_type) != 1:
                failures.append("%d of the %d Ownership record(s) naming %s record %s carry the accountable Ownership "
                                "Type the map declares (%s), where exactly one is accountable"
                                % (len(of_type), len(naming), subject, ident,
                                   r.declarations.get("ownership.accountable type")))
                continue
            if not ((own_id and of_type[0].get(own_id) == value) or (owner_party and of_type[0].get(owner_party) == value)):
                failures.append("%s record %s names %s as its %s, and the one Ownership record of the accountable "
                                "Type that names it is %s, held by %s"
                                % (subject, ident, value, element, of_type[0].get(own_id, "?") if own_id else "?",
                                   of_type[0].get(owner_party, "?") if owner_party else "?"))
                continue
            resolved += 1
            if len(naming) > 1:
                shared += 1
        elif len(naming) > 1:
            # Shared Ownership with no accountable Type declared. Reaching this leg only when the
            # owner named a party let an Entity whose owner named a record by its identifier pass
            # with a second accountable owner beside it, and the Pass reason then said "the one
            # Ownership record that names it"
            accountable = [o for o in naming
                           if (own_id and o.get(own_id) == value) or (owner_party and o.get(owner_party) == value)]
            if len(accountable) != 1:
                failures.append("%d Ownership records name %s record %s, and its %s (%s) singles out %d of them "
                                "where exactly one is accountable"
                                % (len(naming), subject, ident, element, value, len(accountable)))
                continue
            resolved += 1
            shared += 1
        elif by_id:
            resolved += 1
        elif len(naming) == 1:
            # exactly one Ownership record names it: the owner value must be that record or its party
            one = naming[0]
            if owner_party and one.get(owner_party) == value:
                resolved += 1
            else:
                failures.append("%s record %s names %s as its %s, which is neither the Ownership record that names "
                                "it (%s) nor the party that record names (%s)"
                                % (subject, ident, value, element, one.get(own_id, "?") if own_id else "?",
                                   one.get(owner_party, "?") if owner_party else "?"))
        else:
            # no Ownership record names it and its owner names no Ownership record: nothing resolved,
            # and counting it as resolved let the Pass reason claim a resolution that never happened
            failures.append("%s record %s names %s as its %s, and no Ownership record names either it or that value"
                            % (subject, ident, value, element))
    # a violation already found outranks a record that could not be read: returning on the first
    # unreadable record discarded the Fail a later record had already produced
    if failures:
        return "; ".join(failures[:3]), "", None
    if undecided:
        return None, "", ("%d of %d %s record(s) could not be resolved: %s"
                          % (len(undecided), len(records), subject, "; ".join(undecided[:2])))
    if not ownership or "owner" not in element:
        return None, "", None
    note = (", each resolving to the one Ownership record that names it" if resolved == len(records)
            else ", %d of %d resolving to the one Ownership record that names it" % (resolved, len(records)))
    if shared:
        note += (" (%d of them shared between several Ownership records, resolved to the one %s)"
                 % (shared, "of the accountable Ownership Type the map declares" if reads_type
                    else "its owner names as accountable"))
    if not reads_type:
        # CAND-025 counts records of the accountable Type; where the map declares none, the count is
        # by the owner's own pointer, and a reason that did not say so claimed the Decision's rule
        note += (", with no accountable Ownership Type declared (rows `Ownership.type` and "
                 "`Ownership.accountable type`), so accountability is read from each record's owner")
    return None, note, None


# The OCOM types a Statement can be about, so that a subject the map lists nowhere is told apart
# from a sentence whose subject this tool cannot read. `Meta/` and `Models/` define these; a map
# that carries no row for one of them says nothing about it, which is not the same as a map that
# says the export does not represent it, and the two produced different outcomes on one export.
VOCABULARY = ("object", "organization", "entity", "domain", "workflow", "state", "lifecycle",
              "ownership", "owner", "relationship", "event", "attribute", "identity", "identifier",
              "metadata", "classification", "reference", "capability", "policy", "contract",
              "constraint", "registry", "model", "memory record", "audit record", "evidence record",
              "transition", "department", "erasure")


def presence(test, text, r):
    subject = subject_of(text, r.types)
    if subject is None:
        named = subject_of(text, {name: [] for name in VOCABULARY})
        if named is not None:
            # a map row reading "not represented" already Fails; deleting the row outright went
            # pending, so three ways of saying the same thing about one export gave two answers
            return "Fail", ("the Representation Map carries no row for %s, so the Statement's subject is "
                            "represented by nothing in this export" % named)
        return None, "the Statement's subject is not a type the Representation Map declares"
    if not r.types.get(subject):
        return "Fail", "the Representation Map declares no representation for %s" % subject
    elements = required_elements(text)
    if not elements:
        return None, "no element could be read out of the Statement"
    # "Each attribute shall have: name; meaning; data type; optional constraints." asks for three
    # things and offers a fourth. Requiring the fourth would fail an export the Statement permits
    optional = [e for e in elements if e.startswith("optional ")]
    elements = [e for e in elements if not e.startswith("optional ")]
    if not elements:
        return None, "every element this Statement names is optional, so it requires nothing of an export"
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
            failure, one_note, undecided = one_of(subject, element, records, r)
            if failure:
                return "Fail", failure
            if undecided:
                return None, undecided
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
            counts, undeclared = {}, {}
            for path, rec in records:
                value = rec.get(name)
                if isinstance(value, (list, dict)):
                    # an unhashable value killed the run before any report was written, and "every
                    # Object shall possess a unique identity" is the Statement that input is about
                    return "Fail", ("%s record %s carries %d values for %s where the Statement asks for a unique one"
                                    % (subject, rec.get("id", path), len(value), element))
                scope = r.namespace_of(path)
                key = scope + (value,)
                counts[key] = counts.get(key, 0) + 1
                if scope == ("", ""):
                    undeclared[value] = undeclared.get(value, 0) + 1
            # the reuse Invariant compares a record whose scope the map does not declare against
            # every namespace, "otherwise one declaration row exempted the rest"; this leg had no
            # such rule, so one declared collection and one undeclared made two keys of one identity
            crossing = {value for value in undeclared
                        if sum(c for k, c in counts.items() if k[2] == value) > 1}
            repeated = sorted({str(k[2]) for k, n in counts.items() if n > 1} | {str(v) for v in crossing})
            if repeated:
                return "Fail", "%s is not unique across %s: %s" % (element, subject, ", ".join(repeated[:3]))
        unique_note = ", each distinct"
    note = "" if not borrowed else " (%s)" % "; ".join(borrowed)
    if optional:
        note += " (%s: the Statement calls %s optional)" % (", ".join(optional), "them" if len(optional) > 1 else "it")
    return "Pass", "%d %s record(s) carry %s%s%s%s" % (len(records), subject, ", ".join(elements), one_note, unique_note, note)


class EntityIndex:
    """The Lifecycle each Entity names, keyed by the namespace that Entity's identity is in.

    Keyed by the bare identity alone, the ServiceNow twin of an SAP Entity overwrote the SAP one
    and the SAP record's State was checked against the ServiceNow record's Lifecycle: two mandatory
    Transition Tests passed over a violation, through the door `CAND-026` opens for two systems'
    keys. A bare reference from an Event or a Workflow step resolves only where the identity is in
    one namespace, which is the rule `Adoption/Reference Serialization.md` states for a reference."""

    def __init__(self):
        self.by_key, self.spaces = {}, {}

    def add(self, namespace, ident, named):
        if isinstance(ident, (list, dict)):
            return          # not an identity this tool can key by; the uniqueness leg Fails on it
        self.by_key[(namespace, ident)] = named
        self.spaces.setdefault(ident, set()).add(namespace)

    def named(self, ident, namespace=None):
        if isinstance(ident, (list, dict)):
            return None     # two identities are not one Entity, and keying on them killed the run
        if namespace is not None:
            return self.by_key.get((namespace, ident))
        spaces = self.spaces.get(ident) or set()
        return self.by_key.get((next(iter(spaces)), ident)) if len(spaces) == 1 else None

    def get(self, ident, default=None):
        out = self.named(ident)
        return default if out is None else out

    def ambiguous(self, ident):
        return len(self.spaces.get(ident) or set()) > 1


def lifecycle_for(lifecycles, named, namespace=None):
    """The Lifecycle a bare reference names, or None where it is unknown or ambiguous.

    The index is keyed by (namespace, identity) like every other index in this module, so a
    reference resolves in its own namespace first and by bare key only where the export carries
    that identity in one namespace; `Adoption/Reference Serialization.md` states that rule."""
    if named is None:
        return None
    if namespace is not None and tuple(namespace) + (named,) in lifecycles:
        return lifecycles[tuple(namespace) + (named,)]
    hits = [lc for key, lc in lifecycles.items() if isinstance(key, tuple) and key[-1] == named]
    return hits[0] if len(hits) == 1 else None


def lifecycle_index(r):
    """Lifecycles by identity, and the Lifecycle each Entity names, both read through the map."""
    lifecycles, collisions = {}, []
    for path, lc in r.records("lifecycle"):
        # through the map, with no fallback to a literal `id`: the module reads the export only
        # through the Resolver, and the corners that still guessed passed a map that spells the
        # identity otherwise while comparing nothing
        ident = r.identity_of(path, lc)
        if isinstance(ident, (list, dict)):
            collisions.append("a Lifecycle carries %d identifiers where an identity is one value" % len(ident))
            continue
        if is_absent(ident):
            collisions.append("a Lifecycle carries no identifier")
            continue
        # keyed by the bare identifier, two Lifecycles from two declared systems were a collision,
        # which every other leg of this tool treats as two identities (CAND-026)
        key = r.namespace_of(path) + (ident,)
        if key in lifecycles:
            collisions.append("two Lifecycles carry the identifier %s in one declared scope" % ident)
        lifecycles[key] = lc
    if collisions:
        lifecycles["__collisions__"] = collisions
    by_entity = EntityIndex()
    for path, e in r.records("entity"):
        ident = r.identity_of(path, e)
        named = r.value(e, "entity", "lifecycle")
        if not is_absent(ident):
            by_entity.add(r.namespace_of(path), ident, named)
    return lifecycles, by_entity


def state_names(r, lc):
    """The States a Lifecycle defines, read through the map. A State written as a bare string needs
    no field; one written as a record is read through State.name and never through a literal key."""
    name, _ = r.field("state", "name")
    out = []
    for s in r.value(lc, "lifecycle", "states") or []:
        out.append(s.get(name) if isinstance(s, dict) else s)
    return out


def transitions_of(r, lc):
    from_field, _ = r.field("transition", "from")
    to_field, _ = r.field("transition", "to")
    out = []
    for tr in r.value(lc, "lifecycle", "transitions") or []:
        if isinstance(tr, dict):
            out.append((tr.get(from_field), tr.get(to_field)))
    return out


def lifecycle_reading(r, lifecycles):
    """Why a Lifecycle's States or Transitions cannot be read through the map, or "".

    `state_names` and `transitions_of` read the literal keys `name`, `from` and `to` when the map
    bound no row for them, which is the guess the Resolver exists to remove: an export that spells
    them otherwise was compared against fields its records do not carry, every value came back None,
    and the legs passed over nothing. Seven map rows could be deleted with no verdict changing."""
    need = []
    states = [s for lc in lifecycles.values() for s in (r.value(lc, "lifecycle", "states") or [])]
    steps = [tr for lc in lifecycles.values() for tr in (r.value(lc, "lifecycle", "transitions") or [])]
    if any(isinstance(s, dict) for s in states) and r.field("state", "name")[0] is None:
        need.append("State.name")
    if any(isinstance(tr, dict) for tr in steps):
        for element in ("from", "to"):
            if r.field("transition", element)[0] is None:
                need.append("Transition.%s" % element)
    if not need:
        return ""
    return ("the Representation Map binds no field to %s, so the States and Transitions a Lifecycle defines "
            "could not be read" % " or ".join(need))


def transition_predicate(text, r, lifecycles, by_entity):
    low = text.lower()
    unreadable = lifecycle_reading(r, lifecycles)
    if unreadable:
        return None, unreadable

    if "initial state" in low:
        bad = [k[-1] for k, lc in lifecycles.items() if is_absent(r.value(lc, "lifecycle", "initial state"))]
        if bad:
            return "Fail", "no initial State: %s" % ", ".join(bad)
        if "one and only one" in low or "one initial" in low:
            multiple = [k[-1] for k, lc in lifecycles.items() if isinstance(r.value(lc, "lifecycle", "initial state"), list)]
            if multiple:
                return "Fail", "more than one initial State: %s" % ", ".join(multiple)
        outside = [k[-1] for k, lc in lifecycles.items()
                   if r.value(lc, "lifecycle", "initial state") not in state_names(r, lc)]
        if outside:
            return "Fail", "initial State is not one of the Lifecycle's States: %s" % ", ".join(outside)
        return "Pass", "%d Lifecycle(s) define exactly one initial State, each among their own States" % len(lifecycles)

    if "exactly one" in low and "state" in low:
        entities = r.records("entity")
        if not entities:
            return "Fail", "the export carries no Entity"
        bad = []
        for path, e in entities:
            # through the map, like every other leg: reading `id` when the map binds the identity
            # elsewhere looked the Entity up in by_entity under a key the map binds to nothing, so a
            # stale `id` left in the record checked its State against another Entity's Lifecycle
            ident = r.identity_of(path, e)
            state = r.value(e, "entity", "state")
            named = by_entity.named(ident, r.namespace_of(path))
            lc = lifecycle_for(lifecycles, named, r.namespace_of(path))
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
                bad.append("%s defines no Transition" % (k[-1],))
                continue
            names = state_names(r, lc)
            for a, b in pairs:
                if is_absent(a) or is_absent(b):
                    bad.append("%s has a Transition with no from or to" % (k[-1],))
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
            declared = r.value(lc, "lifecycle", "terminal states")
            # one terminal State written as a string was iterated character by character, so the
            # leg compared nothing and reported that no terminal State is left
            terminals = declared if isinstance(declared, list) else ([] if is_absent(declared) else [declared])
            for terminal in terminals:
                if terminal in outgoing:
                    left.append("%s: %s is terminal and has an outgoing Transition" % (k[-1], terminal))
        return ("Fail", "; ".join(left[:3])) if left else \
               ("Pass", "no terminal State is left in %d Lifecycle(s)" % len(lifecycles))

    if ("only perform" in low or "permitted by the lifecycle" in low) and subject_of(text, r.types) == "workflow":
        # a Statement about Workflows is decided from Workflow steps: routing it into the Event leg
        # left an illegal Workflow step passing a Test whose subject is the Workflow
        bad, steps, unread = workflow_violations(r, lifecycles, by_entity)
        if unread:
            return None, unread
        if bad:
            return "Fail", "; ".join(bad[:3])
        if not steps:
            return None, ("no Workflow step could be read: %d Workflow record(s) carry none under the field the "
                          "map binds to Workflow.transitions" % len(r.records("workflow")))
        return "Pass", "%d Workflow step(s) perform only Transitions the Lifecycle permits" % steps

    if "prohibit undefined" in low or "only perform" in low or "permitted by the lifecycle" in low:
        events = r.records("event")
        # keyed by the bare identifier, two declared systems collapse into whichever the map
        # listed last, and a State change is compared against the other system's Lifecycle
        permitted = {k: set(transitions_of(r, lc)) for k, lc in lifecycles.items()}
        by_name = dict(lifecycles)
        compared, bad, unresolved, destination_only = 0, [], [], []
        for _, e in events:
            subject = r.value(e, "event", "subject")
            before = r.value(e, "event", "from state")
            after = r.value(e, "event", "to state")
            if before is None and after is None:
                continue                      # records no State change at all
            named = by_entity.get(subject)
            key = next((k for k in lifecycles if k[-1] == named), None) if named is not None else None
            if key is None or len([k for k in lifecycles if k[-1] == named]) > 1:
                unresolved.append(str(subject))
                continue
            named = key
            if before is None:
                # a destination without a prior State is a creation when it names the initial State,
                # and Models/Lifecycle.md makes entering the initial State the start rather than a
                # Transition. Anything else is a State change that was not compared, and skipping it
                # silently let an Event move an Entity into a State its Lifecycle does not define
                if after not in state_names(r, by_name[named]):
                    bad.append("%s: to %s, a State the Lifecycle does not define" % (e.get("id"), after))
                elif after != r.value(by_name[named], "lifecycle", "initial state"):
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
        bad = [k[-1] for k, lc in lifecycles.items() if is_absent(r.value(lc, "lifecycle", "entity"))]
        return ("Fail", "no single Entity: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) each belong to exactly one Entity" % len(lifecycles))

    if "operational state" in low or "one or more state" in low:
        # the Statement says "one or more"; the leg demanded two and failed a lawful export. A
        # stricter rule than the text is a requirement, and a requirement goes through governance
        bad = [k[-1] for k, lc in lifecycles.items() if len(state_names(r, lc)) < 1]
        return ("Fail", "defines no State: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s) define %d States between them"
                % (len(lifecycles), sum(len(state_names(r, lc)) for lc in lifecycles.values())))

    return None, "no procedure is bound to this predicate; a reviewer decides it"


def compound(text):
    return [i.strip(" .;") for i in re.split(r"[;,]", text.split(":", 1)[1]) if i.strip(" .;")] \
        if ":" in text else [text]


def combine(parts, run_one):
    if not parts:
        # a stem that ends in a colon and carries no list has no part to run, and falling through
        # to the final Pass reported a mandatory Test as passed having executed no procedure
        return None, "the Statement is a stem with no list, so no part of it could be run"
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
    if "__collisions__" in lifecycles and reads_lifecycles(text):
        return "Fail", "; ".join(lifecycles["__collisions__"][:3])
    lifecycles.pop("__collisions__", None)
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
        outside, unbound_paths, _ = r.unlisted_collections()
        outside = outside + unbound_paths
        if outside:
            # every path this leg compares comes from the map, so identities in a collection the map
            # does not list were never counted: the reuse Invariant passed over an export carrying
            # the same identity twice, and said so
            return None, ("%d collection(s) carry identities the Representation Map binds and are outside the "
                          "scopes it declares, either because the map lists them nowhere or because it lists them "
                          "only under a type it binds no identity for (%s), so not every identity the export "
                          "carries could be compared" % (len(outside), ", ".join(outside[:3])))
        counts, unreadable, undeclared_ids = {}, {}, {}
        for path, rec in instances(r.model, paths):
            ident = r.identity_of(path, rec)
            if isinstance(ident, (list, dict)):
                # a record carrying two identities is not one identity this leg can compare, and
                # keying a dict on it killed the run; the uniqueness leg reports the record itself
                return "Fail", ("a %s record carries %d identities where an identity is one value, so it could "
                                "not be compared against the others" % (path, len(ident)))
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
        if not counts:
            # every sibling engine refuses to pass over nothing, and this leg reported "0 Object
            # identities, each carried by exactly one record" as a Pass toward Core Conformance
            return "Fail", ("the export carries no Object identity the Representation Map binds, so no identity "
                            "could be compared against another")
        undeclared = [p for p in paths if r.namespace_of(p) == ("", "")]
        note = "" if not undeclared else (", %d of them in collection(s) whose scope the map does not declare (%s), compared against every namespace"
                                          % (sum(undeclared_ids.values()), ", ".join(sorted(undeclared)[:3])))
        return "Pass", "%d Object identities, each carried by exactly one record within its declared scope%s" % (len(counts), note)

    if "ownership" in low and ("never be undefined" in low or "not be undefined" in low):
        governed = [("entity", rec) for _, rec in r.records("entity")] + \
                   [("domain", rec) for _, rec in r.records("domain")]
        if not governed:
            return "Fail", "the export carries no governed record, so no Ownership could be checked"
        # every field resolved before the loop: resolving inside it returned pending on the first
        # unbound row and discarded the violations already found, which is the escape the sibling
        # leg below had closed
        fields = {name: r.field(name, "owner")[0] for name in {t for t, _ in governed}}
        unbound = sorted(name for name, field in fields.items() if field is None)
        bad = [str(rec.get("id")) for type_name, rec in governed
               if fields[type_name] is not None and is_absent(rec.get(fields[type_name]))]
        if bad:
            return "Fail", "no owner: %s" % ", ".join(bad[:3])
        if unbound:
            return None, "the Representation Map binds no field to %s" % " or ".join("%s.owner" % n for n in unbound)
        return "Pass", "%d governed records each name an owner" % len(governed)

    if "primary governance" in low and "shared" in low:
        if not r.records("entity"):
            return "Fail", "the export carries no Entity"
        domain_field, _ = r.field("entity", "domain")
        if domain_field is None:
            return None, ("the Representation Map binds no field to Entity.domain, so no Entity's primary Domain "
                          "could be read")
        if all(is_absent(e.get(domain_field)) for _, e in r.records("entity")):
            # the leg flagged an Entity only when its domain was a list of more than one, so an
            # absent field flagged nothing and the reason then asserted the opposite: that every
            # Entity names one primary Domain, over an export in which none names any
            return None, ("no Entity record carries a Domain under %s, so no Entity's primary governance could be "
                          "compared" % domain_field)
        bad, seen = [], {}
        for _, e in r.records("entity"):
            domain = e.get(domain_field)
            if isinstance(domain, list) and len(domain) > 1:
                bad.append("%s names %d primary Domains" % (e.get("id"), len(domain)))
            elif is_absent(domain):
                bad.append("%s names no primary Domain" % e.get("id"))
        types_field, _ = r.field("domain", "entity types")
        # a violation this leg has already found is a violation whatever the second half can read:
        # returning pending here discarded an Entity naming two primary Domains, so deleting one map
        # row turned a Fail into pending
        if bad:
            return "Fail", "; ".join(bad[:3])
        if types_field is None:
            return None, "the Representation Map binds no field to Domain.entity types, so no overlap could be read"
        if not any(d.get(types_field) for _, d in r.records("domain")):
            return None, ("no Domain record carries an entity type under %s, so no overlap could be compared"
                          % types_field)
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
        bad = [k[-1] for k, lc in lifecycles.items() if isinstance(r.value(lc, "lifecycle", "initial state"), list)]
        return ("Fail", "more than one initial State: %s" % ", ".join(bad)) if bad else \
               ("Pass", "%d Lifecycle(s), none with more than one initial State" % len(lifecycles))

    if "unreachable state" in low or "undefined transition" in low or "undefined state transition" in low \
            or "violate entity lifecycle" in low or "violate lifecycle" in low or "multiple initial state" in low:
        unreadable = lifecycle_reading(r, lifecycles)
        if unreadable:
            return None, unreadable

    if "unreachable state" in low:
        bad = []
        for k, lc in lifecycles.items():
            names = state_names(r, lc)
            start = r.value(lc, "lifecycle", "initial state")
            # several initial States is itself a violation, and this leg used to die on it with an
            # unhashable list, so the one input the Statement exists to catch wrote no report at all
            starts = start if isinstance(start, list) else [start]
            reached, frontier = set(starts), list(starts)
            pairs = transitions_of(r, lc)
            while frontier:
                here = frontier.pop()
                for a, b in pairs:
                    if a == here and b not in reached:
                        reached.add(b)
                        frontier.append(b)
            unreachable = [n for n in names if n not in reached]
            if unreachable:
                bad.append("%s: %s" % (k[-1], ", ".join(unreachable)))
        return ("Fail", "States no Transition reaches from the initial State: %s" % "; ".join(bad[:3])) if bad else \
               ("Pass", "every State of %d Lifecycle(s) is reachable from its initial State" % len(lifecycles))

    if "undefined transition" in low or "undefined state transition" in low:
        bad = []
        for k, lc in lifecycles.items():
            names = state_names(r, lc)
            for a, b in transitions_of(r, lc):
                if a not in names or b not in names:
                    bad.append("%s: %s to %s" % (k[-1], a, b))
        wf_bad, wf_steps, wf_unread = workflow_violations(r, lifecycles, by_entity)
        if wf_unread:
            return None, wf_unread
        bad += wf_bad
        if bad:
            return "Fail", "; ".join(bad[:3])
        if r.records("workflow") and not wf_steps:
            return None, ("%d Workflow record(s) carry no step under the field the map binds to "
                          "Workflow.transitions, so no Workflow step could be compared" % len(r.records("workflow")))
        return "Pass", ("no Transition in %d Lifecycle(s) or %d Workflow step(s) names an undefined State"
                        % (len(lifecycles), wf_steps))

    if "violate entity lifecycle" in low or "violate lifecycle" in low:
        bad, steps, unread = workflow_violations(r, lifecycles, by_entity)
        if unread:
            return None, unread
        if bad:
            return "Fail", "; ".join(bad[:3])
        if not steps:
            return None, ("no Workflow step could be read: %d Workflow record(s) carry none under the field the "
                          "map binds to Workflow.transitions" % len(r.records("workflow")))
        return "Pass", "%d Workflow step(s) perform only Transitions their Entity's Lifecycle defines" % steps

    return None, "deciding this prohibition needs evidence the export does not carry (a history, or a refusal record)"


def workflow_violations(r, lifecycles, by_entity):
    """Every step a Workflow records, read through the map, against the Lifecycle it acts on.

    Returns (violations, steps examined). A leg that iterated a field the records do not carry
    reported Pass over zero steps, so the count comes back and the caller refuses to pass on nothing.

    The map is the only thing that knows where a Workflow keeps its steps. Reading them by the
    literal key `transitions` passed an export that calls them anything else, having looked at
    nothing, which is the defect this engine was refactored to remove and kept in one corner.
    """
    steps_field, _ = r.field("workflow", "transitions")
    from_field, _ = r.field("transition", "from")
    to_field, _ = r.field("transition", "to")
    entity_field, _ = r.field("transition", "entity")
    unbound = [n for n, f in (("Workflow.transitions", steps_field), ("Transition.entity", entity_field),
                              ("Transition.from", from_field), ("Transition.to", to_field)) if f is None]
    if unbound:
        # reading the literal keys `entity`, `from` and `to` when the map bound none compared every
        # step against None and reported Pass over steps it had not read; and a map row the claimant
        # simply omits is not a violation the implementation committed, so it is pending, not Fail
        return [], 0, ("the Representation Map binds no field to %s, so no Workflow step could be read"
                       % " or ".join(unbound))
    bad, examined, unread = [], 0, 0
    for _, wf in r.records("workflow"):
        for tr in wf.get(steps_field) or []:
            examined += 1
            if not isinstance(tr, dict):
                # a Workflow may record its steps as references to Transition records, which the map
                # lists as their own collection; reading one as a record killed the run
                unread += 1
                continue
            entity = tr.get(entity_field)
            lc = lifecycle_for(lifecycles, by_entity.get(entity))
            if lc is None:
                bad.append("%s acts on %s, %s" % (
                    wf.get("id"), entity,
                    "an identity the export declares in %d namespaces, so no Lifecycle resolves without saying which"
                    % len(by_entity.spaces.get(entity) or ()) if by_entity.ambiguous(entity)
                    else "for which no Lifecycle resolves"))
            elif (tr.get(from_field), tr.get(to_field)) not in set(transitions_of(r, lc)):
                bad.append("%s: %s to %s is not a Transition of %s's Lifecycle"
                           % (wf.get("id"), tr.get(from_field), tr.get(to_field), entity))
    if unread and examined == unread:
        return [], 0, ("%d Workflow step(s) are not records, so none could be read against a Lifecycle; a step "
                       "written as a reference to a Transition record is not resolved by this tool" % unread)
    return bad, examined - unread, ""


LIFECYCLE_LEG = ("lifecycle", "initial state", "unreachable state", "undefined transition",
                 "undefined state transition", "terminal", "state change", "violate entity lifecycle",
                 "violate lifecycle", "operational state", "one or more state", "multiple initial state",
                 "prohibit undefined", "only perform", "permitted by the lifecycle", "exactly one")


def reads_lifecycles(text):
    """Whether a Statement's predicate consults the Lifecycle index at all.

    A collision in that index was returned as the Fail of whatever Statement was under test, so
    "Multiple Classifications shall not change the Identity of the Object" was reported unsatisfied
    because two Lifecycles carried one identifier."""
    low = text.lower()
    return any(marker in low for marker in LIFECYCLE_LEG)


def invariant(test, text, r):
    lifecycles, by_entity = lifecycle_index(r)
    if "__collisions__" in lifecycles and reads_lifecycles(text):
        return "Fail", "; ".join(lifecycles["__collisions__"][:3])
    lifecycles.pop("__collisions__", None)
    # `transition()` refuses an export with no Lifecycle and these legs did not, so three of them
    # reported Pass over zero Lifecycles ("none with more than one initial State")
    if not lifecycles and reads_lifecycles(text):
        return "Fail", "the export carries no Lifecycle, so no Lifecycle could be examined"
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
        the report said every reference resolved. Below the record's own fields only the map's prose
        bindings are skipped: the literal list applied at every depth, and `id` is the commonest
        spelling of a nested reference there is, so `supersedes: {id: <the old content address>}`
        was never resolved."""
        if isinstance(value, dict):
            for k, v in value.items():
                if k in mapped_prose:
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


# Memory/Retention.md governs Memory Records; an erasure record excludes a record from an Integrity
# Test because the record's content is gone by design. Applying that exclusion to any type let one
# erasure record remove a tampered Event from REQ-MODELS-EVENT-010 while its content sat in the file
MEMORY_TYPES = ("memory record", "audit record", "evidence record")


def one_value(value):
    """The single scalar a field holds, or None. An erasure record's fields were compared with `in`
    against a set, so a list-valued Policy or erased record raised TypeError and the run wrote no
    report at all for any of the 185 mandatory Statements."""
    if isinstance(value, (list, tuple)):
        return one_value(value[0]) if len(value) == 1 else None
    return value if not isinstance(value, dict) else None


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
    policies = {one_value(p.get(pol_id)) for _, p in r.records("policy")} if r.types.get("policy") and pol_id else set()
    declared = set(r.ids())
    out = []
    for path, rec in r.records("erasure"):
        why = []
        # the record's own identity is the one the rest of the tool resolves; reading it from
        # Erasure.identifier let a map point that row elsewhere and slip a self-naming erasure past
        ident_here = one_value(r.identity_of(path, rec))
        if is_absent(ident_here) and ident_f:
            ident_here = one_value(rec.get(ident_f))
        names = {ident_here} | ({one_value(rec.get(ident_f))} if ident_f else set())
        erased_value = one_value(rec.get(erased_f)) if erased_f else None
        if erased_f is not None and not is_absent(rec.get(erased_f)) and erased_value is None:
            why.append("names several erased records, so it does not say which record it erases")
        elif erased_f is None or is_absent(rec.get(erased_f)):
            why.append("names no erased record")
        elif erased_value in names:
            why.append("names itself, so it would exclude itself from the verification it authorizes")
        elif declared and erased_value not in declared:
            why.append("names %s, which the export does not declare, so it excludes nothing" % erased_value)
        policy_value = one_value(rec.get(policy_f)) if policy_f else None
        if policy_f is None:
            why.append("the map binds no field to Erasure.policy")
        elif is_absent(rec.get(policy_f)):
            why.append("names no Policy")
        elif policy_value is None:
            why.append("names several Policies, so it does not say under which policy it was issued")
        elif not policies:
            why.append("names Policy %s, but the export declares no Policy records to check it against" % policy_value)
        elif policy_value not in policies:
            why.append("names Policy %s, which the export does not declare" % policy_value)
        if actor_f is None:
            why.append("the map binds no field to Erasure.actor")
        elif is_absent(rec.get(actor_f)):
            why.append("names no actor")
        elif actor_f in {f for k, f in r.fields.items() if k.startswith("erasure.") and k != "erasure.actor"}:
            # one cell of the claimant's own map pointed the actor row at the field already holding
            # the Policy or the erased record, and the gate AO-085 added was satisfied by it
            why.append("names its actor in %s, which the map also binds to another element of the erasure record, "
                       "so the record names no actor of its own" % actor_f)
        elif not isinstance(rec.get(actor_f), (str, int, float)) or len(str(rec.get(actor_f))) > 120:
            why.append("carries %r under %s, which is not an actor this tool can read"
                       % (str(rec.get(actor_f))[:40], actor_f))
        # the exclusion belongs to the record the erasure names, so it is keyed by that record's
        # namespace. Keying it by the namespace of the erasures collection let an erasure record
        # stored in one scope excise a record that merely shares its key in another, and content
        # addressing makes exactly that pair: the same content in two systems is the same key
        named = erased_value
        spaces = {(s, sy) for s, sy, i in r.identities() if i == named} if named else set()
        if len(spaces) > 1:
            why.append("names %s, an identity the export declares in %d namespaces, so it does not say which record "
                       "it erases" % (named, len(spaces)))
        out.append((ident_here, named, why, next(iter(spaces)) if len(spaces) == 1 else None))
    return out


def erased_records(r):
    """Identities whose erasure record grants the exclusion Retention.md provides, keyed by the
    namespace of the record each one names. A set of bare identities excluded a record that merely
    shared a key with the erased one in another declared scope."""
    return {(space, erased) for _, erased, why, space in erasure_records(r)
            if erased and not why and space is not None}


def erasure_incomplete(r, subject, path, rec, demonstration):
    """Why the record an erasure record names does not show the Deleted state `Memory/Retention.md`
    describes, or [] when it does.

    Retention.md grants the exclusion to a record that made its content irrecoverable "while
    preserving the record's identity, its creation time and creator, and its demonstration of
    integrity". The exclusion was granted on the identity alone, so a record that still carried its
    whole content, altered, was excluded from the one Test that would have caught the alteration:
    an erasure record the claimant writes laundered a tampered record into a Pass."""
    why = []
    created, _ = r.field(subject, "creation time")
    creator, _ = r.field(subject, "creator")
    unbound = [name for name, f in (("%s.creation time" % subject, created), ("%s.creator" % subject, creator))
               if f is None]
    if unbound:
        return ["the Representation Map binds no field to %s, so the preservation Retention.md requires cannot be "
                "read and the exclusion cannot be granted" % " or ".join(unbound)]
    if is_absent(rec.get(created)):
        why.append("carries no creation time")
    elif not readable_time(rec.get(created)):
        # the check asked only that the field was non-empty, so pointing `<Type>.creation time` at
        # the field still holding the content made the content count as preserved metadata
        why.append("carries %r under %s, which is not a time this tool can read, so the field the map "
                   "calls its creation time holds something else" % (str(rec.get(created))[:40], created))
    if is_absent(rec.get(creator)):
        why.append("carries no creator")
    elif not isinstance(rec.get(creator), (str, int, float)) or len(str(rec.get(creator))) > 120:
        # the creator had no readability check at all, so a map row pointed it at the field still
        # holding the record's content and the content counted as preserved metadata
        why.append("carries %r under %s, which is not a name this tool can read, so the field the map calls "
                   "its creator holds something else" % (str(rec.get(creator))[:40], creator))
    if is_absent(rec.get(demonstration)):
        why.append("carries no demonstration of integrity")
    preserved = {name for name in (r.identity_field(path), demonstration, created, creator) if name}
    # the identity may be the demonstration (that is what content addressing means), but a creation
    # time or a creator sharing a field with anything else is a map hiding content in a slot this
    # check already trusts
    for name, other in ((created, "creation time"), (creator, "creator")):
        twins = [label for field, label in ((r.identity_field(path), "identity"), (demonstration, "demonstration"),
                                            (created, "creation time"), (creator, "creator"))
                 if field == name and label != other]
        if twins:
            why.append("is preserved through one field the map binds to both its %s and its %s (%s), so one of "
                       "them holds something the Deleted state does not preserve" % (other, twins[0], name))
    remaining = sorted(k for k, v in rec.items() if k not in preserved and not is_absent(v))
    if remaining:
        # `Memory/Memory Record.md` makes six attributes mandatory and `Memory/Retention.md`'s
        # Deleted state names four preserved elements; a record that keeps the first is told it
        # kept content, and one that drops them is no longer a conforming Memory Record (`AO-095`)
        why.append("still carries content under %s, so nothing was made irrecoverable (Retention.md's Deleted "
                   "state names four preserved elements and Memory Record.md makes six attributes mandatory, a "
                   "tension `AO-095` records)" % ", ".join(remaining[:3]))
    # what Retention.md preserves is an identity, a time, a name and a demonstration: four scalars.
    # Checking the top-level keys only let the whole tampered record live inside one of them
    nested = sorted(k for k in preserved if isinstance(rec.get(k), (dict, list)))
    if nested:
        why.append("carries a nested value under %s, where the Deleted state preserves a scalar, so content "
                   "survives inside a field this check would otherwise trust" % ", ".join(nested[:3]))
    return why


def integrity(test, text, r):
    """Verify the demonstration an implementation declares for the records a Statement calls
    immutable. The suite verifies a demonstration and never supplies one, so an export that
    declares none is pending, not passed (`Conformance-Test-Suite.md` Section 3)."""
    low = text.lower()
    if "audit record" in low:
        # CAND-024 clause 2 defines an Audit Record by reference to Memory Record, so a map that
        # lists the collection under either name is naming the same records; demanding one spelling
        # reported an export that uses the other as carrying no Audit Record at all
        subject = next((name for name in ("audit record", "memory record") if r.types.get(name)), "audit record")
    else:
        subject = subject_of(text, r.types) or pathlib.Path(test["document"]).stem.lower()
    if not r.types.get(subject):
        # a map row reading "not represented" and an empty collection assert the same thing, and
        # answering pending to one and Fail to the other made the map's wording decide the outcome
        return "Fail", ("the Representation Map declares no %s records, so the export carries none and no "
                        "demonstration could be verified" % subject)
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
    # an erasure excludes a record only where Retention.md governs it, and only in the scope the
    # erasure record was declared in: applied to every type and by bare key, one erasure record
    # removed a tampered Event, and another removed a record that merely shared a key in another scope
    erased = erased_records(r) if subject in MEMORY_TYPES else set()
    ignored = [] if subject in MEMORY_TYPES else [e for _, e, why, _ in erasure_records(r) if e and not why]
    bad, skipped, refused, granted = [], 0, [], set()
    for path, rec in records:
        ident = keyable(r.identity_of(path, rec))
        uncovered = ""
        if (r.namespace_of(path), ident) in erased:
            not_erased = erasure_incomplete(r, subject, path, rec, field)
            if not not_erased:
                skipped += 1      # an erased record no longer verifies by design; Retention.md says what its demonstration means
                granted.add((r.namespace_of(path), keyable(ident)))
                continue
            # the record an erasure record names is excluded only where it shows the Deleted state;
            # otherwise it is verified like any other, and the refusal is reported beside it rather
            # than in a note at the end, which the reason's own length limit cut away
            uncovered = "; the exclusion an erasure record grants does not cover it: %s" % "; ".join(not_erased)
            refused.append("%s%s" % (ident or "?", uncovered))
        claimed = rec.get(field)
        if is_absent(claimed):
            bad.append("%s carries no demonstration%s" % (ident or "?", uncovered))
        elif claimed != canonical_digest(rec, field):
            bad.append("%s does not verify%s" % (ident or "?", uncovered))
    ignored_note = "" if not ignored else (
        "; %d erasure record(s) naming %s excluded nothing, since Retention.md's Deleted state governs Memory "
        "Records and not %s" % (len(ignored), ignored[0], subject))
    if refused:
        ignored_note += ("; %d record(s) named by an erasure record were verified like any other, since the "
                         "exclusion does not cover them: %s" % (len(refused), "; ".join(refused[:2])))
    if bad:
        return "Fail", ("%d of %d %s record(s) fail their demonstration: %s%s"
                        % (len(bad), len(records), subject, "; ".join(bad[:3]), ignored_note))
    if skipped:
        # the exclusion rests on records and map rows the claimant writes: which field holds the
        # creation time, which holds the creator, which record was erased. Every laundering path
        # round 5 found ends here, so a Test that excluded anything reports what it verified and
        # leaves the exclusion to a reviewer rather than passing on it
        return None, ("%d of %d %s record(s) verified; %d excluded as `Memory/Retention.md`'s Deleted state "
                      "provides, on the strength of erasure records and map rows the claimant writes, so a "
                      "reviewer decides whether the erasures are genuine%s"
                      % (len(records) - skipped, len(records), subject, skipped, ignored_note))
    note = "" if not skipped else ", %d erased record(s) excluded as Retention.md's Deleted state provides" % skipped
    note += ignored_note
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
        # the exclusion this loop honours is the one that was granted, not the one that was claimed:
        # keying it on "named by an erasure record" let an erasure that granted nothing switch off
        # the content-address check, and eight Integrity Tests went from pending to Pass
        if (r.namespace_of(path), keyable(r.identity_of(path, rec))) in granted:
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
            # the system may be declared at any level of the same chain, which is what namespace_of
            # resolves and what Reference Serialization.md permits; demanding it at the scope's own
            # level failed a map the engine itself resolved
            covered = [p for p in r.all_paths() if r.namespace_of(p)[0] == "external system"]
            unnamed = [p for p in covered if not r.namespace_of(p)[1]]
            if not covered or unnamed:
                return "Fail", ("%s declares External System and no level of the map names the system for %s "
                                "(a row `<collection>.identity system` or `<Type>.identity system` or `Identity.system`)"
                                % (key, (unnamed or ["it"])[0]))
    # a collection of records the map does not list at all is outside every identity Test, and the
    # Pass reason said "every identity the export carries" while such a collection sat beside it
    # the scan read the top level only, and the map's own grammar nests (`lifecycles[].states`), so
    # a collection of records placed inside a record was listed by nothing and reached no Test while
    # this Test passed saying the map declares a scope for every identity the export carries
    unlisted, unbound, no_identity = r.unlisted_collections()
    if unlisted:
        return "Fail", ("the export carries %d collection(s) of records the Representation Map does not list (%s), "
                        "so their identities are in no declared scope and reach no Test"
                        % (len(unlisted), ", ".join(unlisted[:3])))
    if unbound:
        return "Fail", ("the Representation Map lists %s only under type(s) for which it binds no identity, so the "
                        "identities those records carry are in no declared scope; add a `<Type>.identity` row for "
                        "the type the collection is listed under" % ", ".join(unbound[:3]))
    uncovered = [p for p in r.all_paths() if r.namespace_of(p) == ("", "")]
    if uncovered:
        return "Fail", ("the map declares %s, which covers no identity in %d of the export's collections (%s); "
                        "CAND-026 binds every identity the export carries to a declared scope"
                        % ("; ".join("%s = %s" % (k, v) for k, v in sorted(decl.items())), len(uncovered),
                           ", ".join(sorted(uncovered)[:3])))
    # a collection the map does not list whose records carry no identity this map binds offends no
    # Statement about identity scope, and failing it for one said something about records that carry
    # none; it is still outside every Test, so the Pass says so
    note = "" if not no_identity else (
        "; %d collection(s) the map does not list carry no identity it binds (%s), so they are in no Test either"
        % (len(no_identity), ", ".join(no_identity[:3])))
    return "Pass", ("the map declares %s%s" % ("; ".join(
        "%s for %s" % (v, "every identity the export carries" if k == "identity.scope" else "%s identities" % k.split(".")[0])
        for k, v in sorted(decl.items())), note))


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


def readable_time(value):
    """A creation time this tool can read: a date `readable_date` accepts, or an ISO timestamp.

    `Memory/Retention.md` preserves a record's creation time through an erasure, and the check that
    the erasure preserved it asked only that the field was non-empty, so a map row could point
    `<Type>.creation time` at the field still holding the record's content."""
    if not isinstance(value, str):
        return False
    value = value.strip()
    # anchored at both ends: prefix-matching accepted the whole record content with a timestamp
    # written in front of it, which is the hole this function was added to close
    m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})[T ](\d{2}):(\d{2})(:(\d{2})(\.\d+)?)?\s*(Z|[+-]\d{2}:?\d{2})?", value)
    if m:
        return readable_date(m.group(1)) and int(m.group(2)) < 24 and int(m.group(3)) < 60
    return readable_date(value)


REVIEW_HEADER = "| Test | Outcome | Reviewer | Date | Reason |"


def review_rows(path):
    """Every judgment row in the file, and the number of headers. read_table stops at the first line
    that is not a row, so a record whose rows were split by a blank line, or indented, or written
    below a paragraph, had everything after the break silently discarded, and what disappeared
    included Review Fails and the duplicates the grammar refuses."""
    raw = pathlib.Path(path).read_text(encoding="utf-8")
    if raw.count("<!--") != raw.count("-->"):
        # everything after an unterminated comment used to disappear, judgments included
        raise SystemExit("%s carries %d '<!--' and %d '-->': an unterminated comment hides every line "
                         "after it, and a judgment this tool cannot see is a judgment nobody recorded"
                         % (path, raw.count("<!--"), raw.count("-->")))
    # comments are removed as spans, so a row that merely mentions `<!--` in a cell is still a row;
    # testing the line for the marker dropped that row, and any row below an opener, without a word
    if (raw.count("```") % 2) or (raw.count("~~~") % 2):
        raise SystemExit("%s carries an unbalanced ``` or ~~~ fence; every judgment row after it is read as "
                         "illustration, and a judgment this tool cannot see is a judgment nobody recorded" % path)
    hidden = [line.strip() for span in re.findall(r"<!--.*?-->", raw, flags=re.S)
              for line in span.splitlines()
              if line.strip().startswith("|") and len(line.strip().strip("|").split("|")) == 5
              and not set("".join(line.strip().strip("|").split("|"))) <= set("-: ")]
    if hidden:
        # a comment opening inside one row's Reason cell and closing after a later row removed the
        # rows between them, Review Fails included, with the markers balanced and nothing printed
        raise SystemExit("%s hides %d judgment-shaped row(s) inside an HTML comment (%s); a judgment this tool "
                         "cannot see is a judgment nobody recorded"
                         % (path, len(hidden), hidden[0][:60]))
    text = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    headers, rows, dropped = 0, [], 0
    fenced, blank_before, indented = False, True, False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        # a row written inside a ``` fence illustrates the format; reading it as a judgment
        # credited a named reviewer who judged nothing and cleared a mandatory Test
        if line.startswith("```") or line.startswith("~~~"):
            fenced = not fenced
            blank_before = False
            continue
        # a Markdown indented code block is a fence written the other way, and a reader sees
        # literal text there too. Deciding it per line demoted the first row of such a block and
        # applied every row below it as a judgment
        if raw_line.startswith("    ") or raw_line.startswith("\t"):
            indented = indented or blank_before
        elif line:
            indented = False
        # a blockquoted or list-item row is a row a reader sees: stripping the marker reads it,
        # and skipping the line silently dropped Review Fails with nothing printed anywhere
        body = re.sub(r"^\s*(?:>\s?|[-*+]\s|\d+[.)]\s)+", "", raw_line).strip()
        blank_before = not line
        if not body.startswith("|"):
            continue
        line = body
        cells = [c.strip() for c in line.strip("|").split("|")]
        if fenced or indented:
            if len(cells) == 5 and not set("".join(cells)) <= set("-: ") and not line.startswith(REVIEW_HEADER):
                dropped += 1
            continue
        if line.startswith(REVIEW_HEADER):
            headers += 1
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    # a filter that silently removes something judgment-shaped is the defect this function has had
    # twice; what it removed is counted and printed beside the run
    if dropped:
        print("%s: %d judgment-shaped row(s) inside a fenced or indented block were read as illustration, not as "
              "judgments" % (path, dropped))
    return headers, rows, dropped


def recorded_against(path):
    """The digests a Reviewer Record declares it was made against:
    `**Recorded against:** model <digest>, map <digest>, statement <digest>`.

    None when the record carries no such line, which Section 3 permits and the report says; a
    dictionary otherwise, empty when the line is there and names nothing this tool can read. The
    two were one value, so a line that bound nothing read as no line at all."""
    raw = pathlib.Path(path).read_text(encoding="utf-8")
    # the binding is the one thing tying a signed record to an export, and it was read from the raw
    # file: a line inside an HTML comment or a fenced block overrode the visible one, and a second
    # visible line was never read at all
    text = re.sub(r"<!--.*?-->|```.*?```|~~~.*?~~~", " ", raw, flags=re.S)
    found = re.findall(r"(?mi)^\s{0,3}(?:>\s*)?\*\*\s*Recorded against\s*:?\s*\*\*\s*:?(.+)$", text)
    if len(found) > 1:
        raise SystemExit("%s carries %d lines binding it to an export; a record is recorded against one export, "
                         "and reading the first of several is reading whichever was written first" % (path, len(found)))
    m = re.search(r"(?mi)^\s{0,3}(?:>\s*)?\*\*\s*Recorded against\s*:?\s*\*\*\s*:?(.+)$", text)
    if not m:
        # two spaces of indentation, a blockquote marker or the colon outside the emphasis took the
        # most permissive branch of all: the record was accepted against any export and the report
        # said it declared nothing, of a file that says "Recorded against" in plain sight
        if re.search(r"(?i)recorded against", text):
            raise SystemExit("%s carries the words 'Recorded against' in a line this tool cannot read; the line "
                             "Section 3 fixes is `**Recorded against:** model <digest>, map <digest>, statement "
                             "<digest>, register <digest>, alias file <digest>, catalogue <digest>`" % path)
        return None
    # every name-and-digest pair on the line, not the three this tool knows: a record naming more
    # than three had the extra bindings silently dropped while the report said its inputs were
    # verified, and the extra digests could be anything at all
    return {k.lower(): v for k, v in re.findall(r"\b([A-Za-z][A-Za-z ]{2,30}?)\s+`?([0-9a-f]{8,64})`?", m.group(1))}


def load_reviews(path, known_aliases):
    """The Reviewer Record: one named judgment per Test, read fail-closed. Section 3 makes a Review
    Pass a named reviewer's recorded judgment with a reason, and Section 4 makes the reviewer's
    identity part of the report, so a row without a Test the catalogue carries, a permitted outcome,
    a name, a readable date or a reason, and a second row for one Test, stop the run rather than
    being skipped: a judgment that cannot be attributed is not a judgment."""
    headers, rows, dropped = review_rows(path)
    if headers != 1:
        raise SystemExit("%s carries %d headers reading '%s'; a Reviewer Record is one table, so that no judgment "
                         "sits in the file unread" % (path, headers, REVIEW_HEADER))
    if not rows:
        raise SystemExit("%s carries no reviewer row under the header '%s'" % (path, REVIEW_HEADER))
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
    # what a filter removed belongs in the published artifact, not only on the console
    out["__dropped__"] = dropped
    return out


def short_reason(reason, reviewed=False):
    """A reason cut at a byte boundary with no marker hid the half of a reviewer's judgment that
    qualified it. The cut is visible, and it points at the Reviewer Record only for a row a reviewer
    wrote: a mechanical Fail was sending the implementer to a document that never held its reason."""
    reason = (reason or "").replace("|", "\\|")
    if len(reason) <= 180:
        return reason
    where = "the whole reason is in the Reviewer Record" if reviewed else "the whole reason is in this run's output"
    return reason[:160].rstrip() + " ... (cut here; %s)" % where


def file_digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()[:16]


def checkout_state():
    """The commit this run read, and whether the tree was modified. Naming the Manifest's last
    Release as what the run was "tested against" stated a commit the run never verified."""
    try:
        head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True)
        dirty = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"], capture_output=True, text=True)
    except Exception:
        return "not a git checkout"
    if head.returncode != 0:
        return "not a git checkout"
    return "%s%s" % (head.stdout.strip(), ", with uncommitted changes" if dirty.stdout.strip() else "")


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


# Section 5 of `Conformance-Test-Suite.md`: the Declaration Tests on extensions check the four
# attestations Chapter 8 imposes. Both were decided by `Pass if the supported extensions field is
# non-empty`, so every value passed: "none", which this tool's own is_absent calls an absence and
# which Section 3 makes Not Applicable; "-"; and a sentence declaring the very violation the
# clauses forbid. A Declaration Test reads a declaration, so what it reads has to be there.
ATTESTATIONS = (
    ("that compatibility with the core language is preserved", "compatibility"),
    ("that normative semantics are unchanged", "semantics"),
    ("that the extension is clearly identifiable", "identifiability"),
    ("that the extension is fully documented", "documentation"),
)
# Chapter 8 imposes four attestations on an extension, and Section 5 of the suite reads each from
# its own field of the Conformance Statement, whose value is `yes` and nothing else. Reading them
# out of a sentence by keyword polarity was a losing game twice over: every marker the four look
# for appears verbatim in a sentence denying them, and a qualification outside a fixed blacklist
# ("preserved only in part", "clearly identifiable in name only") read as an assertion.
ATTESTED = ("yes", "attested", "confirmed")


def attested(statement, key):
    """Whether the Conformance Statement attests `key` in the closed vocabulary Section 5 fixes."""
    return (statement.get("extension attestation %s" % key) or "").strip().strip(".").lower() in ATTESTED


# the clause Chapter 8 states about claiming conformance at all. Its outcome is the run's own
# tally, so it is computed after every other Test and no reviewer may decide it.
NON_CONFORMANCE = "decided by the outcome of every other mandatory Test, reported in the summary"


def declaration(clause, statement):
    low = clause.lower()
    if "specification version" in low:
        v = statement.get("supported specification version")
        # "none", "-", "n/a" and "tbd" are absences by this module's own vocabulary, and both
        # version clauses passed on them, which is the defect the extension clauses were cured of
        if is_absent(v):
            return "Fail", "no supported specification version is declared (%r)" % (v if v is not None else "")
        return "Pass", "the Conformance Statement names version %s" % v
    if "multiple versions" in low:
        v = statement.get("supported specification version", "")
        if is_absent(v):
            return "Fail", "no version declared (%r)" % v
        if re.search(r"[,;]| and |\bor\b", str(v)):
            return "Fail", "more than one version declared: %s" % v
        return "Pass", "one version declared: %s" % v
    if "extension" in low:
        declared = statement.get("supported extensions")
        if declared is None:
            return "Fail", "the Conformance Statement carries no supported extensions field"
        if is_absent(declared):
            return ("Not Applicable", "the Conformance Statement declares no extension (%r), so what Chapter 8 "
                                      "imposes on extensions applies to nothing in it" % declared)
        if "invalidate" in low:
            if not attested(statement, "conformance"):
                return "Fail", ("the Conformance Statement declares extension(s) (%s) and does not carry "
                                "`Extension attestation conformance: yes`, the attestation that conformance with "
                                "the core specification is not invalidated" % declared[:60])
            return "Pass", ("extensions declared (%s), attested not to invalidate conformance with the core "
                            "specification" % declared[:60])
        missing = [(name, key) for name, key in ATTESTATIONS if not attested(statement, key)]
        if missing:
            return "Fail", ("the Conformance Statement declares extension(s) (%s) and attests %d of the four things "
                            "Chapter 8 imposes on them: it does not carry %s"
                            % (declared[:60], len(ATTESTATIONS) - len(missing),
                               "; ".join("`Extension attestation %s: yes` (%s)" % (key, name) for name, key in missing)))
        return "Pass", ("extensions declared (%s), with the four attestations Chapter 8 imposes, each carried in "
                        "its own field" % declared[:60])
    if "shall not claim conformance" in low:
        # decided after the tally, in main(); left pending here it blocked establishment forever and
        # a reviewer could Review Pass it in the same run that recorded a mandatory Fail
        return None, NON_CONFORMANCE
    return None, "no procedure is bound to this clause"


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--model", required=True)
    p.add_argument("--map", required=True)
    p.add_argument("--statement", required=True)
    p.add_argument("--report")
    # a hard-coded default stamped every report with one day in the past, including the report the
    # README tells a reader to produce and the committed example a Reviewer Record is bound to
    p.add_argument("--today", default=None)
    p.add_argument("--reviews", help="the Reviewer Record: a Markdown table of named judgments on the Tests no procedure decided")
    a = p.parse_args(argv)
    if a.today is None:
        a.today = datetime.date.today().strftime("%-d %B %Y")

    model = json.loads(pathlib.Path(a.model).read_text(encoding="utf-8"))
    types, fields, declarations = load_map(a.map)
    r = Resolver(model, types, fields, declarations)
    statement = load_statement(a.statement)
    catalogue = load_catalogue()
    register = load_register()

    missing_text = sorted(t["alias"] for t in catalogue if t["alias"] not in register)
    if missing_text:
        raise SystemExit("the Test Catalogue names %d Statement(s) the Requirement Register does not carry (%s); a "
                         "Test over an empty Statement is a Test about nothing, and the engines answered it with "
                         "sentences about the claimant's map" % (len(missing_text), ", ".join(missing_text[:3])))
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
    claim_aliases = {row["alias"] for row in results if row["reason"] == NON_CONFORMANCE}
    reviews = load_reviews(a.reviews, {r["alias"] for r in results}) if a.reviews else {}
    dropped_rows = reviews.pop("__dropped__", 0)
    a_reviews = a.reviews
    declared, binding = ({}, "")
    if a.reviews:
        declared = recorded_against(a.reviews)
        # the register decides what each Statement says, so a judgment recorded against another
        # register is a judgment about another sentence; the report digested it and compared nothing
        # the report's own sentence says the register, the Alias File and the Test Catalogue
        # "decide which Statements exist and which procedure each one gets", and only the register
        # was bound: one edited Kind cell turned a mechanical Fail into a Test a signed record
        # decided Review Pass
        actual = {"model": file_digest(a.model), "map": file_digest(a.map), "statement": file_digest(a.statement),
                  "register": file_digest(REGISTER), "alias file": file_digest(ALIASES),
                  "catalogue": file_digest(CATALOGUE)}
        if declared is not None and sorted(declared) != sorted(actual):
            # the run compared the keys the line happened to name, so a record naming one digest was
            # accepted against any map and any Conformance Statement while the report printed that
            # all three were verified. Section 3 fixes the grammar; a partial line is refused
            raise SystemExit("%s says it was recorded against %s; Section 3 of `Conformance-Test-Suite.md` writes "
                             "that line as `model <digest>, map <digest>, statement <digest>, register <digest>, "
                             "alias file <digest>, catalogue <digest>`, "
                             "and a record that names fewer binds its judgments to less than the export and the "
                             "Statements they were made against, while one that names more declares a binding "
                             "this tool cannot verify"
                             % (a.reviews, ", ".join(sorted(declared)) or "nothing this tool can read"))
        if declared is not None:
            wrong = [k for k, v in declared.items() if not actual[k].startswith(v) and not v.startswith(actual[k])]
            if wrong:
                raise SystemExit("%s says it was recorded against %s %s, and this run read %s; a judgment recorded "
                                 "against another export is a judgment about something else"
                                 % (a.reviews, wrong[0], declared[wrong[0]], actual[wrong[0]]))
            binding = ("The record declares the model, the map, the Conformance Statement, the Requirement "
                       "Register, the Alias File and the Test Catalogue it was made against, and they are the "
                       "six this run read: what a judgment is about is the Statement, and what decides which "
                       "Statements exist and which procedure each one gets is those three.")
        else:
            binding = ("The record declares no inputs, so nothing ties its judgments to this export beyond the word "
                       "of whoever published them (`AO-093`).")
    not_applied = []
    for row in results:
        judgment = reviews.get(row["alias"])
        if not judgment:
            continue
        if row["reason"] == NON_CONFORMANCE or row["alias"] in claim_aliases:
            # Section 3 gives a Review outcome to a Statement no mechanical procedure can decide;
            # this one is decided by the run's own tally, and a judgment on it asserted conformance
            # in the same report that listed the Fail the clause is about
            not_applied.append("%s: %s recorded %s, and this clause is decided by the run's own tally rather than "
                               "by a reviewer" % (row["alias"], judgment["reviewer"], judgment["outcome"]))
            continue
        if row["outcome"] is None:
            # the mechanical reason says what the procedure could not settle, and overwriting it
            # hid, for instance, that the export models nothing the Statement is about
            row["reason"] = "%s, %s: %s (the procedure returned no outcome: %s)" % (
                judgment["reviewer"], judgment["date"], judgment["reason"], row["reason"] or "no reason recorded")
            row["outcome"] = judgment["outcome"]
        else:
            not_applied.append("%s: %s recorded %s, but the Test decided %s mechanically and a judgment does not override it"
                               % (row["alias"], judgment["reviewer"], judgment["outcome"], row["outcome"]))

    # Chapter 8's own clause, computed from the rest: Pass when nothing else mandatory fails or is
    # undecided, Fail when something does, and pending only while the rest are still undecided
    claim = [row for row in results if row["reason"] == NON_CONFORMANCE]
    for row in claim:
        others = [o for o in results if o is not row and o["class"] == "mandatory"
                  and o["outcome"] != "Not Applicable"]
        bad = [o for o in others if o["outcome"] in ("Fail", "Review Fail")]
        undecided = [o for o in others if o["outcome"] is None]
        if bad:
            row["outcome"] = "Fail"
            row["reason"] = ("%d mandatory Test(s) are unsatisfied (%s), so this implementation may not claim "
                             "conformance with this version" % (len(bad), ", ".join(o["alias"] for o in bad[:3])))
        elif undecided:
            row["reason"] = ("%d mandatory Test(s) are undecided (%s), so whether a mandatory requirement is "
                             "unsatisfied is not yet known" % (len(undecided), ", ".join(o["alias"] for o in undecided[:3])))
        else:
            row["outcome"] = "Pass"
            row["reason"] = "no mandatory Test is unsatisfied, so the clause forbids nothing here"

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
    lines.append("**Inputs, by content:** model `%s`, map `%s`, Conformance Statement `%s`, Requirement Register `%s`, "
                 "Alias File `%s`, Test Catalogue `%s` (SHA-256 of each file as read). The last three decide which "
                 "Statements exist and which procedure each one gets, so a report that named only the first three did "
                 "not say what produced its outcomes.%s"
                 % (file_digest(a.model), file_digest(a.map), file_digest(a.statement),
                    file_digest(REGISTER), file_digest(ALIASES),
                    file_digest(CATALOGUE), " " + binding if binding else ""))
    lines.append("")
    release, commit = manifest_release()
    lines.append("**Read from:** the checkout at `%s`, whose `Governance/Publication-Manifest.md` names Release %s at "
                 "commit `%s` as its latest. The run reads the working tree, not that commit: where the two differ, "
                 "the digests above are what was read. Requirement Register: %d Statements. Alias File revision: %s."
                 % (checkout_state(), release, commit, register_count(), alias_revision()))
    lines.append("")
    lines.append("**Published by:** the party that ran the suite. A report published by the claimant is "
                 "self-validation; `Conformance-Test-Suite.md` Section 4 says the suite does not tell the two "
                 "apart and the publisher does.")
    lines.append("")
    if reviews:
        lines.append("**Reviewer Record:** `%s` (`%s`), %d judgment(s) by %s. Whether a reviewer is independent of the "
                     "claimant is a fact about the reviewer, not something this tool can read."
                     % (a.reviews, file_digest(a.reviews), len(reviews), ", ".join(reviewers)))
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
    lines.append("| Not Applicable (dispositioned Descriptive, or a capability the Conformance Statement does not "
                 "claim) | %d |" % len(not_applicable))
    lines.append("")
    lines.append("**Measured set:** %d of the %d mandatory Tests the catalogue carries; %d are Not Applicable, "
                 "dispositioned Descriptive in the Alias File or a capability this Conformance Statement does not "
                 "claim. A claim rests on what was measured, so the size of the measured set is stated beside the "
                 "outcome.\n" % (len(mandatory), len(mandatory) + len(not_applicable), len(not_applicable)))
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
                     "every one of them names a record it carries in exactly one declared scope. Not resolved: a "
                     "field the map binds to prose, at any depth; a record's own identity and the fields listed "
                     "beside it in this tool's skip list at the top level of a record (`id`, `type`, `name`, "
                     "`label`, `purpose`, `meaning`, `note`, `rule`, `expression`, `trigger`, `data_type`, "
                     "`state`, `initial_state`); a value carrying a space or shaped like a date; and a Reference's "
                     "target, which may legitimately name another system."
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
        lines.append("%d erasure record(s); %d are well formed in the sense `Memory/Retention.md` requires, naming "
                     "a Policy the export declares, an actor, and one record the export declares. The records the "
                     "others name were verified like any other. What is not checked: Retention.md also requires the "
                     "erasure to be recorded as a Memory Record, and no Test reaches the erasures collection itself, "
                     "so an erasure record carries no demonstration of its own here (`AO-094`). `Memory/Retention.md` "
                     "is outside the requirement set, so this is an observation and not a Test outcome."
                     % (len(erasures), len(granted)))
        lines.append("")
        listed = sorted(erasures, key=lambda e: (bool(e[2]), str(e[0])))
        for ident, erased, why, _ in listed[:50]:
            if why:
                lines.append("- %s names %s and grants no exclusion: %s" % (ident or "?", erased or "no record", "; ".join(why)))
            else:
                covered = [s for s in MEMORY_TYPES if any(r.identity_of(p, rec) == erased
                                                          for p, rec in r.records(s))]
                lines.append("- %s names %s: well formed, and %s"
                             % (ident or "?", erased,
                                "the Integrity Test covering that record grants the exclusion where the record "
                                "shows `Memory/Retention.md`'s Deleted state" if covered else
                                "no Integrity Test over a Memory type covers that record, so the exclusion "
                                "changes nothing: `Memory/Retention.md`'s Deleted state governs Memory Records"))
        if len(listed) > 50:
            lines.append("- (%d further erasure record(s) not listed; the ones that grant an exclusion are listed first)"
                         % (len(listed) - 50))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Reviewers")
    lines.append("")
    if a_reviews and dropped_rows:
        lines.append("%d judgment-shaped row(s) in `%s` sit inside a fenced or indented block and were read as "
                     "illustration rather than as judgments.\n" % (dropped_rows, a_reviews))
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
                        r["outcome"] or "pending", short_reason(r["reason"], r["alias"] in reviews)))
    report = "\n".join(lines) + "\n"

    if a.report:
        pathlib.Path(a.report).write_text(report, encoding="utf-8")
        print("wrote %s" % a.report)
    # `short_reason` cuts a long reason in the report's table and says the whole one is in this
    # run's output; nothing printed it, so the marker pointed at nothing. Every row the table had to
    # cut, and every mandatory Fail, is printed here in full
    for row in results:
        if row["class"] != "mandatory":
            continue
        cut = len(row.get("reason") or "") > 180
        if row["outcome"] in ("Fail", "Review Fail") or cut:
            print("%s %s: %s" % (row["outcome"] or "pending", row["alias"], row["reason"]))
    print("Not Applicable %d (dispositioned Descriptive, or a capability not claimed)" % len(not_applicable))
    print("mandatory %d: Pass %d, Fail %d, pending %d, reviewed %d pass and %d fail. Core Conformance %s."
          % (len(mandatory), len(passed), len(failed), len(pending), len(review_passed), len(review_failed),
             "established" if established else "not established"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

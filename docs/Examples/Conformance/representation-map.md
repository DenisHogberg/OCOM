<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / Conformance / Representation Map

[← Back](README.md) · [↑ Up](../README.md)

---
<!-- nav:end -->

# Representation Map — Library Lending Export

**Document ID:** EX-CONF-MAP-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 23 September 2026

---

# Purpose

`Conformance-Test-Suite.md` Section 1 says the suite reaches an implementation through its
Conformance Statement and one or more exported models in the implementation's own serialization,
accompanied by a Representation Map stating how each element of the OCOM vocabulary is represented
in that serialization. The suite prescribes no format; this map is what makes the test
format-independent, and it is the artifact an adopting organization writes for its own export
rather than changing its systems to match a format OCOM does not prescribe.

This map describes `model.json` beside it. It is Informative and makes no conformance claim of its
own.

---

# How to Read a Row

A row of kind `method`, `Integrity.method`, names the method by which records demonstrate they are unaltered, and a row `Type.integrity` of kind `field` names the field that carries the demonstration on each record of that type. `content-addressed-identity` means the record's identity field holds the SHA-256 of the record's own content (its JSON with the identity field removed, keys sorted, no whitespace, UTF-8; a stated encoding, not RFC 8785), so an altered record is a different record and a party holding the old identity can tell. It is the one method `tools/conformance/validate.py` passes. A record that merely carries its own digest (`sha256-canonical-json`) is verified and reported pending, because matching one's own digest shows consistency and not that nothing changed. Audit Records in this export carry a `label` beside the content address, for reading; Evidence Records keep a readable identity: a Memory Record's content includes the Evidence it references and an Evidence Record names its Memory Record, so the two cannot both be content-addressed, and the Evidence side names the Memory Record by its content address.

A row of kind `declaration` states something about the export as a whole rather than binding a field: `Identity.scope` declares which of the five Identity Scopes `Meta/Identity.md` names the export's identities carry (`CAND-026`); an export whose identities come from another system declares `External System` and names the system in a row `Identity.system`. A type may declare its own scope in a row `<Type>.identity scope`, and a type spread over several collections, one per source system, declares per collection in a row `<collection>.identity scope` (with `<collection>.identity system` for an External System). The suite keys identity uniqueness and reuse by the declared scope and system.

An export whose Objects carry several Owners declares which Ownership Type the organization holds
accountable (`CAND-025`; `Meta/Ownership.md` lists eight and the choice is the organization's), in a
row `Ownership.accountable type` of kind `declaration` beside a field row `Ownership.type`. The
Presence Test for `REQ-MODELS-ENTITY-004` then counts exactly one Ownership record of that Type per
Entity. This export gives each Entity one Ownership record and declares neither row, and the Test
says so in its reason: accountability is read from each record's owner instead.

An export that erases a record under `Memory/Retention.md` declares the erasure records the same
way: a row `Erasure | collection | <path>` says where they live, and rows `Erasure.identifier`,
`Erasure.erased record`, `Erasure.policy` and `Erasure.actor` bind their fields. The suite then
excludes an erased record from an Integrity Test, but only where the erasure record names a Policy
the export declares and an actor, names an identity the export declares in one namespace, and names
a record that shows the Deleted state: its identity, its creation time and creator (rows
`<Type>.creation time` and `<Type>.creator`) and its demonstration of integrity preserved, and
nothing else of its content left in it. This export erases nothing and carries none of those rows.

A row of kind `collection` names where instances of an OCOM type live in the export: one or more
top-level keys, or a path of the form `parent[].child` for instances nested inside another
collection. A collection of records the map lists nowhere is outside every Test, and the Declaration
Test on Identity scope fails an export that carries one whose records carry an identity this map
binds, at the top level or nested inside another record. A row of kind `field` names the field those instances carry for one element of the
vocabulary, written `Type.element`. An element the export does not carry has no row, and a Test
that needs it fails rather than passing over an absence.

---

# Types

| OCOM type | Kind | Where it is in this export |
|---|---|---|
| Object | collection | `entities`, `domains`, `relationships`, `references`, `events`, `policies`, `contracts`, `capabilities`, `registries`, `classifications`, `constraints`, `workflows`, `models`, `audit_records`, `evidence_records` |
| Identity | collection | `entities`, `domains`, `relationships`, `references`, `events`, `policies`, `contracts`, `capabilities`, `registries`, `classifications`, `constraints`, `workflows`, `models`, `audit_records`, `evidence_records` |
| Metadata | collection | `entities` |
| Entity | collection | `entities` |
| Domain | collection | `domains` |
| Relationship | collection | `relationships` |
| Reference | collection | `references` |
| Event | collection | `events` |
| State | collection | `lifecycles[].states` |
| Lifecycle | collection | `lifecycles` |
| Transition | collection | `lifecycles[].transitions` |
| Workflow | collection | `workflows` |
| Model | collection | `models` |
| Ownership | collection | `ownership` |
| Classification | collection | `classifications` |
| Capability | collection | `capabilities` |
| Policy | collection | `policies` |
| Contract | collection | `contracts` |
| Constraint | collection | `constraints` |
| Registry | collection | `registries` |
| Attribute | collection | `entities[].attributes` |
| Audit record | collection | `audit_records` |
| Evidence record | collection | `evidence_records` |
| Organization | collection | *(not represented: this export models one branch's lending service and carries no Organization records)* |

---

# Fields

| OCOM element | Kind | Field in the export |
|---|---|---|
| Object.identity | field | `id` |
| Object.identifier | field | `id` |
| Object.metadata | field | `metadata` |
| Identity.identity | field | `id` |
| Identity.identifier | field | `id` |
| Entity.identity | field | `id` |
| Entity.identifier | field | `id` |
| Entity.name | field | `name` |
| Entity.meaning | field | `meaning` |
| Entity.domain | field | `domain` |
| Entity.owner | field | `owner` |
| Entity.ownership | field | `owner` |
| Entity.attributes | field | `attributes` |
| Attribute.name | field | `name` |
| Attribute.meaning | field | `meaning` |
| Attribute.data type | field | `data_type` |
| Attribute.constraints | field | `constraints` |
| Entity.metadata | field | `metadata` |
| Entity.classification | field | `classification` |
| Entity.lifecycle | field | `lifecycle` |
| Entity.state | field | `state` |
| Entity.states | field | `state` |
| Domain.identifier | field | `id` |
| Domain.name | field | `name` |
| Domain.purpose | field | `purpose` |
| Domain.owner | field | `owner` |
| Relationship.identifier | field | `id` |
| Relationship.source object | field | `source` |
| Relationship.target object | field | `target` |
| Relationship.relationship type | field | `type` |
| Reference.identifier | field | `id` |
| Reference.source object | field | `source` |
| Reference.target object | field | `target` |
| Reference.reference direction | field | `direction` |
| Event.identifier | field | `id` |
| Event.event type | field | `type` |
| Event.timestamp | field | `occurred_at` |
| Event.subject | field | `subject` |
| Event.origin | field | `source` |
| Event.source | field | `source` |
| State.name | field | `name` |
| State.meaning | field | `meaning` |
| State.entity | field | `entity` |
| State.lifecycle | field | `lifecycle` |
| Lifecycle.identifier | field | `id` |
| Lifecycle.entity | field | `entity` |
| Lifecycle.initial state | field | `initial_state` |
| Lifecycle.states | field | `states` |
| Lifecycle.state transitions | field | `transitions` |
| Lifecycle.transitions | field | `transitions` |
| Lifecycle.terminal states | field | `terminal_states` |
| Transition.from | field | `from` |
| Transition.to | field | `to` |
| Transition.trigger | field | `trigger` |
| Workflow.identifier | field | `id` |
| Workflow.name | field | `name` |
| Workflow.purpose | field | `purpose` |
| Model.identifier | field | `id` |
| Model.name | field | `name` |
| Model.purpose | field | `purpose` |
| Ownership.identifier | field | `id` |
| Ownership.owner | field | `owner` |
| Ownership.owned object | field | `owned_object` |
| Ownership.responsibility scope | field | `responsibility_scope` |
| Ownership.effective date | field | `effective_date` |
| Classification.identifier | field | `id` |
| Classification.classification name | field | `name` |
| Classification.classification type | field | `type` |
| Capability.identifier | field | `id` |
| Capability.name | field | `name` |
| Capability.purpose | field | `purpose` |
| Policy.identifier | field | `id` |
| Policy.name | field | `name` |
| Policy.purpose | field | `purpose` |
| Policy.scope | field | `scope` |
| Policy.effective date | field | `effective_date` |
| Contract.identifier | field | `id` |
| Contract.name | field | `name` |
| Contract.purpose | field | `purpose` |
| Contract.parties | field | `parties` |
| Contract.effective date | field | `effective_date` |
| Constraint.identifier | field | `id` |
| Constraint.name | field | `name` |
| Constraint.expression | field | `expression` |
| Registry.identifier | field | `id` |
| Registry.name | field | `name` |
| Registry.purpose | field | `purpose` |
| Registry.scope | field | `scope` |
| Reference.direction | field | `direction` |
| Relationship.source | field | `source` |
| Relationship.target | field | `target` |
| Relationship.type | field | `type` |
| Relationship.source entity | field | `source` |
| Relationship.target entity | field | `target` |
| Relationship.cardinality | field | `cardinality` |
| Entity.responsible owner | field | `owner` |
| Entity.operational states | field | `state` |
| Domain.operational responsibility | field | `purpose` |
| Domain.owner responsible for governance and operational consistency | field | `owner` |
| Event.time at which it occurred | field | `occurred_at` |
| Event.affected entities | field | `subject` |
| State.meaning within the lifecycle | field | `meaning` |
| Contract.participants | field | `parties` |
| Contract.scope | field | `scope` |
| Constraint.purpose | field | `purpose` |
| Constraint.scope | field | `applies_to` |
| Registry.registry scope | field | `scope` |
| Registry.ownership | field | `owner` |
| Registry.owner | field | `owner` |
| Registry.registered object types | field | `registered_object_types` |
| Workflow.required inputs | field | `inputs` |
| Workflow.expected outputs | field | `outputs` |
| Workflow.transitions | field | `transitions` |
| Transition.entity | field | `entity` |
| Event.from state | field | `from_state` |
| Event.to state | field | `to_state` |
| Domain.entity types | field | `entity_types` |
| Domain.owner | field | `owner` |
| Registry.scope | field | `scope` |
| Audit record.identity | field | `id` |
| Audit record.integrity | field | `id` |
| Evidence record.identity | field | `id` |
| Audit record.label | field | `label` |
| Event.integrity | field | `id` |
| Integrity.method | method | `content-addressed-identity` |
| Identity.scope | declaration | `Organization` |

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 September 2026 | First map, written for `model.json` so the Conformance Test Suite can be run end to end against a real file. |
| 0.1 | 22 September 2026 | Row `Identity.scope` of kind `declaration`, declaring Organization as the scope of every identity this export carries, per `CAND-026`; the kind explained under How to Read a Row. |
| 0.1 | 22 September 2026 | How to Read a Row: declarations may be keyed by collection path, and the suite keys identity by the declared scope and system. |
| 0.1 | 23 September 2026 | The Attributes this export nests inside its Entities are listed (`entities[].attributes`) with their four fields: they were represented and named by no row, and a Statement whose subject the map lists nowhere used to be reported as unreadable rather than unrepresented. Round 4 of the all-packages test. |
| 0.1 | 23 September 2026 | How to Read a Row: the rows that declare the accountable Ownership Type, and the rows that declare an erasure record and what the exclusion requires of the record one names, and what a collection the map does not list costs. Round 3 of the all-packages test found that vocabulary written down nowhere outside the validator. The rows themselves are unchanged: this export erases nothing. |

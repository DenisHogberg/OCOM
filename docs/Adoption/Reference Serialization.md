<!-- nav:start -->
[Docs](../README.md) / [Adoption](README.md) / Reference Serialization

[↑ Up](README.md)

---
<!-- nav:end -->

# Reference Serialization

**Document ID:** ADOPTION-REFERENCE-SERIALIZATION-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 September 2026

---

## Purpose

An integration team asks three things of a specification before it writes a line: a file to validate against, a schema, and a rule that lets identifiers from two systems live in one export without colliding. OCOM prescribes no serialization format and no schema, on purpose (`Language/Serialization.md`; `Language/Schema.md`, Independence): a format is a technology, and implementations adapt to the model rather than the other way round. This document gives the three things without giving up that position.

It is Informative. It introduces no concept, defines no type and adds no requirement; where it says less than the normative documents it cites, they prevail.

## What is prescribed, and what is not

The specification prescribes what an export contains, through the mandatory Statements of its canonical documents, and the Conformance Test Suite (`Governance/Conformance-Test-Suite.md`) reads an export through a Representation Map that states how each element of the vocabulary appears in it. It does not prescribe the encoding. Any encoding whose map resolves every element the Tests need is as good as any other.

What this document adds is a starting point. The Reference Serialization is the JSON encoding of `docs/Examples/Conformance/model.json`, the export the suite is run against end to end in this repository. An implementation that has an encoding of its own keeps it and writes its map; an implementation that has none starts here. Authorized by `CAND-026` (Decided 22 September 2026) on the terms `CAND-012` set for Adoption pages.

## The Reference Serialization

One JSON document. Its top-level keys are the collections of the export, one per OCOM type it carries, each a list of records, and `export`, a block naming who produced the file, when, and against which specification version.

| Collection | OCOM type | What a record carries |
|---|---|---|
| `entities` | Entity | `id`, `name`, `type`, `meaning`, `domain`, `owner`, `classification`, `metadata`, `attributes`, `lifecycle`, `state` |
| `domains` | Domain | `id`, `name`, `purpose`, `owner`; `entity_types` names the Entity types the Domain governs |
| `lifecycles` | Lifecycle | `states` and `transitions` nested; `initial_state`, `terminal_states` |
| `relationships`, `references` | Relationship, Reference | `source`, `target`, and `type` or `direction` |
| `ownership` | Ownership | `owner`, `owned_object`, `responsibility_scope`, `effective_date`; an Entity's `owner` names the Ownership record that is accountable for it (`CAND-025`) |
| `classifications`, `capabilities`, `policies`, `contracts`, `constraints`, `registries`, `workflows`, `models` | the types of the same names | as `representation-map.md` binds them |
| `events` | Event | `type`, `subject`, `source`, `occurred_at`, `from_state`, `to_state`; identified by the SHA-256 of their own content |
| `audit_records`, `evidence_records` | Audit Record, Evidence Record | the Memory tier; Audit Records are content-addressed like Events, so an altered record is a different record (`CAND-024`) |

Identifiers are strings. Records that demonstrate they are unaltered are identified by the digest of their own content, which the map's `Integrity.method` row declares; every other identifier is whatever the organization assigns, under the scope rule below.

The file itself: [`model.json`](../Examples/Conformance/model.json). The map that describes it: [`representation-map.md`](../Examples/Conformance/representation-map.md). The report the suite produced from it: [`report.md`](../Examples/Conformance/report.md). How to run it: [`README.md`](../Examples/Conformance/README.md).

## The schema

[`schema.json`](../Examples/Conformance/schema.json) is a JSON Schema (draft 2020-12) derived from the example by `tools/conformance/reference_schema.py` and never written by hand; CI regenerates it, fails on a difference, and validates the example against it. Every record type is an object with the properties the example carries, required only where every example record of that type carries them and there are at least two records to compare, since one record cannot tell an optional property from a mandatory one; collections are optional, because an export carries the types it has and its map says which; content-addressed identifiers carry the pattern of a SHA-256 digest; additional properties are allowed everywhere, because an implementation extends the encoding before it replaces it. An export that carries only its `export` block and its `entities` satisfies the schema.

What the schema validates is a file in this encoding. It validates nothing about OCOM. A file can satisfy the schema and fail every Test in the catalogue, because the Tests read the model's content (does every Entity have one owner, is every recorded State change one its Lifecycle permits, does every Audit Record verify) and the schema reads its shape. The suite, not the schema, decides conformance; a validator that only checks the schema has checked nothing the specification requires.

```text
python3 tools/conformance/reference_schema.py --validate my-export.json
```

## The Representation Map

What every implementation owes the suite is not the Reference Serialization but a Representation Map: the table that says, for each element of the vocabulary, where it is in the export (`Conformance-Test-Suite.md`, Section 1). The example's map is the worked example of that artifact. It has four kinds of row: `collection`, where the instances of a type live; `field`, which field carries an element; `method`, the one row `Integrity.method`, naming how records demonstrate they are unaltered; and `declaration`, a statement about the export as a whole, such as the scope of the export's identities, the system an External System scope names, or the Ownership Type the organization holds accountable. Until 23 September 2026 this page called the integrity method a declaration, and a map written to it had every Integrity Test report that the map declares no method; the validator now refuses that row rather than reading it as silence. An implementation that uses the Reference Serialization unchanged can use the example's map unchanged; one that renames a field changes one row.

## Identities from other systems

`Meta/Identity.md` names five Identity Scopes (Organization, Business Domain, Registry, External System, Global Ecosystem) and requires the organization to define the appropriate scope for each Identity. The rule this document states for an export is the declaration of that choice:

1. Every identity the export carries is bound to one of the five scopes.
2. The scope is declared in the Representation Map, in a row `Identity.scope` of kind `declaration`; a type whose identities carry a different scope declares its own in a row `<Type>.identity scope`, and a type spread over several collections, one per source system, declares per collection in a row `<collection>.identity scope`.
3. An identity of scope External System names the system it comes from, in a row `Identity.system`, `<Type>.identity system` or `<collection>.identity system`.

So an SAP business-partner number and a ServiceNow record identifier coexist in one export as identities of two declared scopes naming two systems, and a reader knows which system to ask about each. The suite keys identity uniqueness and reuse by the declared scope and system, so `1000001` from SAP and `1000001` from ServiceNow are two identities and not one reused; a bare reference that names an identity the export declares in two scopes is ambiguous, and the report's Reference Integrity section says so rather than resolving it to either. The suite tests the declaration (`REQ-META-IDENTITY-005`, a Declaration Test since `CAND-026`): one of the five passes, any other fails, an External System that names no system fails, and a map that declares nothing is reported pending, since the suite reads a declaration and never supplies one.

What the rule does not do: it does not define what each scope means, or how identities are merged, split or resolved across systems; `AO-009` and `AO-010` record those as open, and `CAND-004` question 6 leaves Registry scope across Organizations to a Reference Case. It declares; it does not decide.

## What this document does not do

It does not make the encoding, the schema or the map's field names normative; `Language/Serialization.md` and `Language/Schema.md` are unchanged. It does not name a transport, a protocol or a storage. It does not certify anything: a file that validates has been validated against a shape, and conformance is a published Test Report (`Conformance-Test-Suite.md`, Section 4). It does not replace the Worked Example, which explains the concepts; this document assumes them.

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 September 2026 | First version, authorized by `CAND-026` (Decided 22 September 2026) on the form `CAND-012` set for Adoption pages: the Reference Serialization, its derived schema, the Representation Map as the artifact every implementation owes the suite, and the declaration rule for identity scope. |
| 0.1 | 22 September 2026 | The enterprise evaluation of the same day ran the suite on an SAP-and-ServiceNow-shaped export and found it comparing bare identifiers while this page promised coexistence, and found the derived schema demanding every collection. Both fixed in the tools; this page now says how the suite keys identity (declared scope and system, per type or per collection), that a bare reference to an identity present in two scopes is reported ambiguous, and that collections are optional in the schema. |

---

*Source: this document restates, and does not extend, `Language/Serialization.md`, `Language/Schema.md`, `Meta/Identity.md`, `Governance/Conformance-Test-Suite.md` and `docs/Examples/Conformance/`. The encoding, the schema and the map are Informative; the Statements the suite tests belong to the canonical documents. Authorized as an Adoption Projection under `Governance/ADR-Candidates.md#cand-026`, on the terms of `#cand-012`.*

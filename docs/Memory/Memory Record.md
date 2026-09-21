<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Memory Record

[← Back](Layered%20Memory.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Memory Record

**Document ID:** Memory-02

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 September 2026

---

# Purpose

This document defines the standardized structure of a Memory Record within the OCOM Memory Specification.

A Memory Record is the fundamental unit of operational memory used by AI Agents and business systems.

The Memory Record provides a consistent representation of retained knowledge regardless of storage technology or implementation.

---

# Definition

A Memory Record represents a single retained fact, observation, inference, or decision together with its operational metadata.

A Memory Record is immutable after creation. Corrections to previously retained information are represented as new Memory Records; an existing Memory Record is never modified.

Terminology note. `Core/Constitution.md` paragraph 4 names this concept Memory Entry. Per `Governance/Constitution-Step0-Summary.md` Decision 1, Memory Entry and Memory Record are one concept and Memory Entry is the canonical term; this document keeps its title pending the rename, tracked as `Governance/Documentation-Debt.md` GAP-004.

---

# Design Principles

Every Memory Record shall be:

- uniquely identifiable;
- immutable after creation;
- explainable;
- evidence-backed;
- confidence-aware;
- auditable;
- governed;
- technology independent.

---

# Mandatory Attributes

Every Memory Record shall define:

- Identifier
- Subject
- Memory Type
- Value
- Layer
- Created Date

Status is deliberately not in this list. It is a derived projection rather than a stored attribute; see the Status section below.

---

# Optional Attributes

A Memory Record may define:

- Description
- Category
- Tags
- Expiration Date
- Owner
- Related Entity
- Related Workflow
- Related Event

---

# Memory Types

A Memory Record may represent:

- Fact
- Observation
- Decision
- Preference
- Rule
- Relationship
- Summary
- Inference
- Prediction
- Exception

Additional types may be introduced by future specifications.

---

# Audit Record

An Audit Record is a Memory Record whose subject is a governance action on an Object: its creation, modification or retirement, an approval, a change of Ownership or Classification, or the application of a Policy.

Wherever this specification states that Audit records shall remain immutable, the clause is satisfied by Constitution Principle 4 together with the Conformance clause of this document that requires an implementation to be able to demonstrate that a Memory Record has not been altered. It requires nothing further of an implementation. Audit Record is defined here by reference to Memory Record and is not a term of the Core Vocabulary (`CAND-024`).

---

# Identity

Each Memory Record shall have a globally unique identifier.

The identifier shall remain stable throughout the lifetime of the record.

---

# Subject

The Subject identifies the entity or operational context to which the memory belongs.

Examples include:

- Customer
- Partner
- Vendor
- Employee
- Contract
- Payment
- Campaign

---

# Value

The Value represents the retained operational knowledge.

The value may be:

- structured;
- semi-structured;
- unstructured.

Implementations may choose any internal representation.

---

# Layer

Every Memory Record shall belong to exactly one memory layer.

Permitted values are:

- Transient
- Stage
- Long-Term
- Persistent

Layer transitions are governed by the Layered Memory specification.

---

# Status

Status is a derived projection, not a stored attribute of a Memory Record. It is computed at read time from the full append-only sequence of Memory Records for a subject, so a change of status is recorded by adding a new Memory Record and never by modifying an existing one, per Constitution Principle 4. This resolves `AO-003` as its Option B, decided in `Governance/ADR-Candidates.md` `CAND-014`.

Statuses typically computed include:

- Active
- Pending Verification
- Archived
- Expired
- Rejected

Organizations may extend the status model.

---

# Relationships

A Memory Record may reference:

- Entities
- Events
- Workflows
- Lifecycles
- AI Agents
- Other Memory Records

---

# Evidence

A Memory Record shall reference at least one Evidence Record.

Evidence provides the basis for explainability and confidence assessment.

The structure of Evidence is defined separately in the Evidence Overlay specification.

---

# Confidence

A Memory Record may include a confidence assessment.

Confidence expresses the estimated reliability of the retained knowledge.

The confidence model is defined in the Confidence specification.

---

# Governance

Every Memory Record shall define its governance policy.

Governance may include:

- write permissions;
- correction permissions;
- approval requirements;
- write-back policy;
- retention policy.

---

# Auditability

Every Memory Record shall preserve, at creation:

- creator;
- creation time.

A Memory Record's audit trail is established at creation and never changes. There is no modification, modifier, or modification reason to record, because a Memory Record is never altered after creation. Corrections to previously retained information are represented as new Memory Records; the audit trail of the retained knowledge is the append-only sequence of Memory Records itself.

---

# Independence

The Memory Record specification does not prescribe:

- storage engines;
- databases;
- vector representations;
- embedding models;
- serialization formats.

Implementations remain technology independent.

---

# Conformance

A compliant implementation shall:

- implement all mandatory attributes;
- preserve record identity;
- never modify a Memory Record after creation, and represent corrections as new Memory Records;
- support evidence references;
- support confidence assessment;
- preserve audit history;
- comply with governance policies;
- be able to demonstrate, to a party holding a Memory Record together with its identity and nothing else, that the record has not been altered since its creation.

The last clause names a property and no mechanism. Content-addressed identity and hash chaining are two mechanisms that satisfy it; an implementation that satisfies it another way conforms. It is stated identically for Evidence Records in `Evidence Overlay.md`, and it is what makes the immutability this document requires a checkable property rather than an assertion (`CAND-024`).

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 27 July 2026 | Removed "may evolve through controlled updates" from Definition; added immutability to Design Principles and Conformance; rewrote Auditability to remove modification/modifier/modification-reason language; replaced "update permissions" with "correction permissions" in Governance — per Constitution §4 and ARCH-001 (Step 0, Decision 1) |
| 0.1 | 27 July 2026 | Changed Evidence section from "may reference" to "shall reference at least one Evidence Record" — per Constitution §3 and ARCH-002 (Step 0, Decision 2) |
| 0.1 | 5 September 2026 | Added a terminology note: Memory Entry (Constitution paragraph 4) and Memory Record are one concept per Step 0 Decision 1; rename pending, tracked as GAP-004. No requirement changed. |
| 0.1 | 11 September 2026 | Status moved out of Mandatory Attributes and restated as a derived projection computed from the append-only sequence for a subject, per the resolution of `AO-003` as its Option B, decided in `CAND-014`. Integration of that decision's Layer 1 only; no other attribute, section or requirement changed. |
| 0.1 | 21 September 2026 | Conformance gains the integrity guarantee and an Audit Record section defines the subject of the clause "Audit records shall remain immutable" by reference to Memory Record, per `CAND-024` (Decided 21 September 2026). `AO-075` closes. |

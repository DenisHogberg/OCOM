<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Evidence Overlay

[← Back](Confidence.md) · [↑ Up](README.md) · [Next →](Layered%20Memory.md)

---
<!-- nav:end -->

# Evidence Overlay

**Document ID:** Memory-03

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 September 2026

---

# Purpose

This document defines the Evidence Overlay within the OCOM Memory Specification.

Evidence Overlay provides the supporting information that explains why a Memory Record holds a particular value and Confidence level.

Evidence Overlay enables explainability, traceability, and verification of retained operational knowledge.

---

# Definition

An Evidence Record is the retained account of why a Memory Record holds its value: what was observed or asserted, from which source, and how reliable that source was judged to be at the time.

Evidence explains; it does not decide.

A Memory Record without Evidence is a belief, and Constitution Principle 3 does not permit a retained belief without traceable Evidence.

---

# Design Principles

Evidence Overlay shall:

- remain evidence-based;
- be append-only;
- support explainable AI;
- preserve traceability;
- remain auditable;
- support governance decisions;
- remain independent of implementation technologies.

---

# Immutability

An Evidence Record is immutable after creation. Evidence is created once; an existing Evidence Record is never altered.

Corrections to previously recorded Evidence are represented as new Evidence Records, never as changes to an existing Evidence Record.

---

# Mandatory Attributes

Every Evidence Record shall define:

- Identifier
- Related Memory Record
- Description
- Created Date
- Source
- Reliability

Source is the origin of the Evidence, named as one of the Evidence Sources this document lists, with an identifier of the specific origin where one exists and the value unknown source where it does not.

Reliability is the recorded judgement of the source's reliability at the time of recording, on a scale the organization defines and declares, together with the actor who recorded the judgement. Reliability is a property of the Evidence; Confidence, which summarises it across the Evidence a Memory Record references, is defined in `Confidence.md`.

---

# Optional Attributes

An Evidence Record may define:

- Category
- Owner
- Tags
- Expiration Date

---

# Evidence Sources

Evidence may originate from:

- human verification;
- AI reasoning;
- business rules;
- historical consistency checks;
- independent supporting sources;
- unknown source (used when the origin of retained information cannot be determined; an explicit, honest record of unknown origin — the complete absence of an Evidence Record is never permitted).

---

# Relationship to Confidence

Evidence explains why Confidence exists.

Confidence summarizes the estimated reliability of the Evidence associated with a Memory Record.

Confidence shall not exist without supporting Evidence.

---

# Relationship to Memory Record

A Memory Record shall reference at least one Evidence Record, and may reference more than one.

Evidence provides the basis for explainability and confidence assessment.

---

# Relationship to Other Memory Components

Evidence Overlay interacts with:

- Memory Record
- Confidence
- Layered Memory
- Retention
- Write-back Governance

---

# Auditability

Every Evidence Record shall preserve, at creation:

- timestamp;
- actor.

An Evidence Record is never altered after creation; there is no previous value or new value to record for an individual Evidence Record. When previously recorded Evidence is corrected, the correction is captured as a new Evidence Record, and the audit trail is the append-only sequence of Evidence Records itself.

---

# Independence

Evidence is independent of:

- the Memory Record it supports, which may gain new Evidence without changing;
- Metadata, which Constitution Principle 3 forbids merging with Evidence;
- Confidence, which Evidence explains and does not replace;
- implementation technology.

---

# Conformance

A compliant implementation shall:

- implement the mandatory attributes;
- preserve an Evidence Record unaltered after creation, and represent corrections as new Evidence Records;
- support every Evidence Source this document lists, including unknown source;
- record Source and Reliability together with the actor who recorded them;
- be able to demonstrate, to a party holding an Evidence Record together with its identity and nothing else, that the record has not been altered since its creation.

The last clause names a property and no mechanism. Content-addressed identity and hash chaining are two mechanisms that satisfy it; an implementation that satisfies it another way conforms. It is stated identically for Memory Records in `Memory Record.md`.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 21 July 2026 | Reconstructed from existing Memory specifications (Design Principles, Attributes, Evidence Sources, Relationship to Confidence and Memory Record, Auditability). Definition, Independence, and Conformance reserved for a future version. |
| 0.1 | 27 July 2026 | Added "be append-only" to Design Principles and a new Immutability section explicitly stating that an Evidence Record is immutable after creation and corrections are new Evidence Records; rewrote Auditability to remove previous-value/new-value language — per Constitution §4 and ARCH-006 |
| 0.1 | 27 July 2026 | Added "unknown source" to Evidence Sources — per Constitution §3 and ARCH-002 (Step 0, Decision 2) |
| 0.1 | 5 September 2026 | Relationship to Memory Record: "may reference one or more" changed to "shall reference at least one Evidence Record, and may reference more than one", propagating ARCH-002 (Step 0, Decision 2), already applied to `Memory Record.md` on 27 July 2026 and to this document's Evidence Sources section ("the complete absence of an Evidence Record is never permitted"). |
| 0.1 | 21 September 2026 | The four sections reserved since 21 July 2026 are written, per `CAND-023` (Decided 21 September 2026): Definition; Source and Reliability added to the Mandatory Attributes; Independence; Conformance. The Conformance section carries the integrity guarantee of `CAND-024`. `FW-001` closes. |

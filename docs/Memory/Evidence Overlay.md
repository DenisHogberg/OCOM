<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Evidence Overlay

[← Back](Confidence.md) · [↑ Up](README.md) · [Next →](Layered%20Memory.md)

---
<!-- nav:end -->

# Evidence Overlay

**Document ID:** Memory-03

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Evidence Overlay within the OCOM Memory Specification.

Evidence Overlay provides the supporting information that explains why a Memory Record holds a particular value and Confidence level.

Evidence Overlay enables explainability, traceability, and verification of retained operational knowledge.

---

# Reserved Sections

Definition, the Source and Reliability attributes, Independence, and Conformance for Evidence Overlay are reserved for a future version of this specification.

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

A Memory Record may reference one or more Evidence Records.

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

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 21 July 2026 | Reconstructed from existing Memory specifications (Design Principles, Attributes, Evidence Sources, Relationship to Confidence and Memory Record, Auditability). Definition, Independence, and Conformance reserved for a future version. |
| 0.1 | 27 July 2026 | Added "be append-only" to Design Principles and a new Immutability section explicitly stating that an Evidence Record is immutable after creation and corrections are new Evidence Records; rewrote Auditability to remove previous-value/new-value language — per Constitution §4 and ARCH-006 |
| 0.1 | 27 July 2026 | Added "unknown source" to Evidence Sources — per Constitution §3 and ARCH-002 (Step 0, Decision 2) |

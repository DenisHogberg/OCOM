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
- support explainable AI;
- preserve traceability;
- remain auditable;
- support governance decisions;
- remain independent of implementation technologies.

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
- independent supporting sources.

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

Evidence Overlay changes shall record:

- previous value;
- new value;
- reason for change;
- timestamp;
- actor.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 21 July 2026 | Reconstructed from existing Memory specifications (Design Principles, Attributes, Evidence Sources, Relationship to Confidence and Memory Record, Auditability). Definition, Independence, and Conformance reserved for a future version. |

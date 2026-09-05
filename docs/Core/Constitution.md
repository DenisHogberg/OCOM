<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Constitution

[↑ Up](README.md) · [Next →](Governance.md)

---
<!-- nav:end -->

# Constitution

**Document ID:** Core-00

**Status:** Draft

**Version:** 1.0

**Last Updated:** 21 August 2026

**Adopted via:** `Governance/ADR-Candidates.md#cand-006`

---

# Purpose

OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations. This document defines the fundamental principles that make a system an implementation of OCOM. These principles are intentionally technology-independent and domain-independent. They apply regardless of programming language, storage engine, deployment model, AI model, or business domain. Implementation details may evolve. Architecture may evolve. These principles should not.

---

# Canonical Principles

1. **Object-Centric Reality.** Object is the universal abstraction of OCOM. Everything represented by OCOM is expressed as an Object or as a specialization of Object.
2. **Domain-Owned Identity.** An entity becomes an OCOM Object only when its identity belongs to the operational domain rather than to the implementation. Operational role takes precedence over ontological classification. The same entity may be represented differently depending on the operational question being answered.
3. **Evidence Before Belief.** Every operational fact must be traceable to Evidence. Evidence and Metadata are independent concepts and must never be merged.
4. **Immutable Memory.** Memory is append-only. A Memory Entry is immutable after creation. Corrections are represented as new Memory Entries, never by modifying historical records.
5. **Memory Precedes Knowledge.** Knowledge is always derived from Memory. World Models are always derived from Knowledge. Memory → Knowledge → World Model.
6. **Reconstructability.** Knowledge and World Models must always be reproducible from Memory without requiring access to the original external systems.
7. **Separation of Dimensions.** Architecture, Capability and Autonomy are independent dimensions. Progress in one dimension never implies progress in another.
8. **Static Before Dynamic.** Static World Modelling precedes Dynamic World Modelling.
9. **Domain-Neutral Core.** The OCOM Core must never contain domain-specific knowledge. The Core must never branch on organization-specific concepts or business entities. Domain knowledge belongs only to configuration, data and adapters.
10. **Extensibility Over Enumeration.** Business vocabularies are extensible. Organizations extend OCOM through specialization rather than modification of the Core.
11. **Structural Isolation.** Every architectural layer must be structurally incapable of exceeding its defined responsibilities. Boundaries are enforced by architecture rather than convention.
12. **Grounded Reasoning.** Statements derived from Memory and Knowledge must remain distinguishable from interpretation, inference or expert opinion. The system must communicate provenance and confidence appropriately.
13. **Adaptation Flows Toward the Model.** Implementations adapt to OCOM. OCOM never adapts to implementation-specific constraints.
14. **Professional Responsibility.** OCOM augments professional decision-making. Responsibility remains with the designated human role unless a higher Autonomy level has been explicitly delegated.

---

# Architectural Principles

- New sources integrate through Adapters and Normalizers.
- Identity Resolution thresholds are deployment configuration.
- Source trust is deployment configuration.
- Concept namespaces are deployment scoped.
- One deployment currently represents one organization.

---

# Implementation Principle

Every implementation must be evaluated against the Canonical Principles *before* architectural or implementation-specific optimizations are accepted. No optimization may violate the Canonical Principles.

---

# Meta-Principle

When a conflict exists between an implementation, an architectural decision and the Constitution, the Constitution prevails.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 27 July 2026 | Adopted as Core-00, per `CAND-006` (`Governance/ADR-Candidates.md`). Verbatim transcription of the Decision text — no wording changes. |
| 1.0 | 21 August 2026 | Added one identity sentence to Purpose ("OCOM is an open, technology-independent operating model for organizations"), aligning with the canonical identity used across `ocom.uno`, `llms.txt`, and `Core/Manifest.md`. Semantic positioning only — no Canonical Principle added, removed, or reworded; no constitutional meaning changed. |

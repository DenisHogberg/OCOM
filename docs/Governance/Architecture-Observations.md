<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Observations

[← Back](Architecture-Health.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Observations

**Document ID:** GOV-OBSERVATIONS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document records architectural inconsistencies, ambiguities, and potential improvements noticed by the CDKO.

The CDKO records observations. It does not resolve them. Resolution is the responsibility of the Chief Architect, recorded in the Architect Response field.

---

## OBS-001

**Title:** Content duplication between AI/Context/Overview.md and AI/Agents/Context.md

**Date observed:** 21 July 2026

**Description:** The two documents are textually identical in body content. They differ only in their Document ID field (`AI-Context-00` vs `AI-Agents-05`).

**Impact:** It is unclear whether this is an intentional cross-reference between the Agents and Context sections, or an accidental duplication that occurred during preparation of the source documents.

**Recommendation:** The Chief Architect should decide whether to keep the duplicate, replace `AI/Agents/Context.md` with an explicit reference to `AI/Context/Overview.md`, or give `AI/Agents/Context.md` distinct, Agent-specific content.

**Status:** Open — escalated, see ADR-Candidates.md#cand-001

**Architect Response:** *(pending)*

**Related:** `AI/Context/Overview.md`, `AI/Agents/Context.md`, `Documentation-Debt.md#OBS-001`, `ADR-Candidates.md#cand-001`

---

## OBS-002

**Title:** Reference Architecture layer name retains "Business Object" while internal vocabulary uses "Entity"

**Date observed:** 21 July 2026

**Description:** During terminology unification, "Business Object" was replaced with "Entity" throughout the specification, including the Reference Architecture layer name ("Business Object Architecture" → "Entity Architecture") and all internal section headers. On author review, the layer name was restored to "Business Object Architecture," while the internal section headers of `Object-Architecture.md` (Entity Identity, Entity Ownership, Entity Lifecycle, etc.) and body prose across the rest of the specification retained "Entity."

**Impact:** `Object-Architecture.md` now has a title using "Business Object" while its own section headers use "Entity" — a deliberate, author-approved duality rather than an unresolved inconsistency.

**Recommendation:** None — already resolved by explicit author decision.

**Status:** Closed

**Architect Response:** Restored "Business Object Architecture" as the layer name; all other terminology changes to "Entity" approved and kept. Author decision, 21 July 2026 (v0.1 Release Candidate review).

**Related:** `Reference Architecture/Object-Architecture.md` and 6 sibling Reference Architecture documents, `Documentation-Debt.md#OBS-002`

---

## OBS-003

**Title:** Reference Case — Object Attribute Lifecycle Categories

**Date observed:** 22 July 2026

**Description:** Submitted as a ready-formed normative clarification ("Attribute Categories"), documented here per the Reference Case template (`Standard Evolution Methodology.md`, Section 3) rather than adopted directly, per Rule 5 (a Reference Case shall not modify the Core directly).

| Field | Content |
|---|---|
| **Reference Case** | Object Attribute Lifecycle Categories |
| **Purpose** | Disambiguate what "required" means for an Object's attributes, distinguishing attributes required by the Object primitive itself from those required by a Type definition, those introduced after objects already exist, and those computed rather than stored. |
| **Expressive Coverage** | Partially expressible with existing concepts. `Models/Entity.md` defines Attributes generically (name, meaning, data type, optional constraints) without distinguishing categories. `Meta/Object.md` defines Identity and Metadata but does not separate "structural" identity fields from type-specific or business fields. Neither document has a concept of a versioned Object Type, or of migration semantics for attributes introduced after object creation. |
| **Boundary Conditions** | (1) No existing concept separates attributes whose presence is required for an artifact to be a valid Object at all, from attributes required only by a specific, versioned Type definition. (2) No existing concept addresses what happens when a new required attribute is introduced after Objects of that Type already exist. (3) No existing concept distinguishes stored from derived/computed attributes, or states how a derived attribute's validity depends on its source attributes. (4) The case references a "Type Versioning & Compatibility" document that does not exist anywhere in the current specification — i.e., it presumes a concept (versioned Object Type) that has not itself been established. |
| **Boundary Tags** | `structural-integrity` (validity of an artifact as an Object depends on structural fields being present); `set-scoped-constraint` (Type-level requirements apply to a bounded subset of Objects — those created under a given Type version — not universally); `temporal-dependency` (requiredness and migration handling depend on when an Object was created relative to a Type version change); `input-completeness` (the entire case is fundamentally about whether required information is present, and what to do when it is not, at various points in time). |
| **External Assurance** | None provided with this submission. The case arrived as a fully-formed proposed rule set, not as a report of an observed operational scenario, so it cannot currently be distinguished from hypothesis. This is itself recorded as a limitation of the case, not a judgment on its merit. |
| **Core Impact** | Possible, not Recommended. Per Rule 2 of `Standard Evolution Methodology.md`, a single Reference Case — independent or not — does not on its own justify a Core extension; independent corroborating cases would be needed. Per Rule 1, Core shall not be extended on this case alone. |

**Impact:** If the underlying boundary is real and recurring, it would eventually touch `Meta/Object.md` (Identity, Metadata) and `Models/Entity.md` (Attributes), and would require introducing a concept not currently in the specification: a versioned Object Type, distinct from Entity/Object as currently defined. That would be a Core extension, not a clarification.

**Recommendation:** Do not modify `Meta/` or `Models/` on the basis of this single case. If the Chief Architect has, or is aware of, independent Reference Cases demonstrating the same boundary (Rule 2), those should be submitted and linked here to test for a Repeated Pattern before an ADR Candidate is considered.

**Status:** Open — logged as a Reference Case observation; not escalated to ADR Candidates (insufficient independent corroboration per Rule 1/2)

**Architect Response:** *(pending)*

**Related:** `Standard Evolution Methodology.md` (Reference Case template, Rules 1, 2, 5), `Meta/Object.md`, `Models/Entity.md`

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial log, 2 entries |
| 0.1 | 22 July 2026 | Added OBS-003 (Reference Case: Object Attribute Lifecycle Categories) |

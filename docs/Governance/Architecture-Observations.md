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

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial log, 2 entries |

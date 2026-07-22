<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Standard Evolution Methodology

[← Back](Release-Readiness.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Standard Evolution Methodology

**Document ID:** GOV-EVOLUTION-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document defines the methodology by which the OCOM Core evolves.

The Core **shall** change on the basis of observed, repeated operational practice — not on the basis of a single hypothesis, a single example, or a single contributor's opinion. This methodology exists to make that discipline explicit and repeatable, rather than leaving it to be reconstructed in each individual discussion.

This is not an architectural specification. It defines no new modeling concepts. It defines how evidence is gathered, recorded, and — only where warranted — escalated into a change to the Core.

---

# Principles

## Evidence Before Architecture

A change to the Core **shall** be motivated by observed operational practice, expressed through one or more Reference Cases (Section 3), not by a hypothesis about what might be needed.

## Reference Cases Before Core Changes

No change to the Core **shall** be proposed without at least one Reference Case demonstrating the limitation it addresses. A Reference Case precedes discussion of a Core change; it is not produced to justify a change already decided.

## Repeatability Before Standardization

A single Reference Case documents an observation. It does not, by itself, justify standardization. A limitation **shall** be observed across multiple independent Reference Cases before it is treated as a pattern worth standardizing (see Section 5).

## Backward Compatibility

Changes to the Core **shall** maintain backward compatibility whenever practical, consistent with the Change Principles already established in `Core/Governance.md`. This methodology does not relax that requirement — it defines the evidentiary bar a change must clear before compatibility is even put at risk.

## Architectural Traceability

Every Core change **shall** be traceable to the Reference Cases, Observations, and ADR that motivated it, consistent with the Traceability by Design principle in `Governance-Manifest.md`. This methodology is the mechanism by which that traceability is produced for evolution decisions specifically.

## Single Source of Truth

A Reference Case **shall not** redefine or duplicate a concept already defined in the Core. Where a Reference Case appears to require a new definition, that need is itself the observation to be recorded — not an occasion to define the concept locally, consistent with the Single Source of Truth principle in `Core/Principles.md`.

## Minimal Core

The Core **should** remain as small as it can be while remaining sufficient. A Reference Case that can be fully expressed using existing Core concepts is evidence the Core is sufficient, not evidence that it is incomplete.

## Principle of Minimal Evolution

The OCOM Core **SHALL** evolve only when repeated evidence demonstrates that an existing architectural boundary cannot adequately express a recurring business reality.

The existence of a single implementation problem **SHALL NOT** justify architectural expansion.

Core grows because reality repeatedly demands it, not because one implementation found it convenient.

---

# Reference Case Methodology

A Reference Case is the unit of evidence this methodology operates on. Every Reference Case **shall** use the following template.

| Field | Description |
|---|---|
| **Reference Case** | Name and identifier of the case. |
| **Purpose** | The operational problem or scenario the case addresses. |
| **Expressive Coverage** | Which existing Core concepts (Object, Entity, Domain, Relationship, Policy, Contract, Lifecycle, etc.) were used to express the case, and how completely they covered it. |
| **Boundary Conditions** | Where the case reached the edge of what existing Core concepts could express, if anywhere. |
| **Boundary Tags** | Zero or more tags from the Controlled Boundary Vocabulary (Section 4) classifying each boundary condition. |
| **External Assurance** | Evidence that the case reflects observed practice rather than hypothesis — e.g. independent confirmation, an existing system it was drawn from, or an independent second case reaching the same boundary. |
| **Architectural Observations** | Links to any entries created in `Architecture-Observations.md` as a result of this case. |
| **Core Impact** | Assessment of whether the case implies a Core change: None / Possible / Recommended. |
| **Decision** | The outcome: Closed — no Core impact / Escalated to Observation / Escalated to ADR Candidate. |

A Reference Case that is fully expressible with existing Core concepts, with no Boundary Conditions, **shall** be recorded with Core Impact: None and closed. This is the expected, common outcome, and is itself valuable evidence that the Core is sufficient — a Reference Case is not a vehicle that must produce a Core change to be worthwhile.

---

# Controlled Boundary Vocabulary

Boundary Conditions **shall** be tagged using this controlled vocabulary. Tags classify the *type* of limitation encountered, not its resolution.

| Tag | Meaning |
|---|---|
| `set-scoped-constraint` | The case requires a rule or constraint that applies only to a bounded subset of instances, not universally. |
| `referential-integrity` | The case depends on guaranteeing that a reference between Objects remains valid. |
| `structural-integrity` | The case depends on the structural shape of a Model remaining consistent independently of its content. |
| `temporal-dependency` | The case depends on ordering or timing between states, events, or transitions. |
| `cross-object-dependency` | The case requires coordinated behavior or constraints spanning more than one Object. |
| `environmental-signal` | The case depends on information originating outside the operational model (e.g. an external system's state). |
| `external-attestation` | The case depends on confirmation or certification from a party outside the model. |
| `input-completeness` | The case depends on guaranteeing that required information is present before an operation proceeds. |
| `trust-boundary` | The case depends on distinguishing which participants or systems are authorized to act. |
| `repository-scope` | The boundary is specific to how this specification's repository is organized, not to the OCOM model itself. |
| `system-scope` | The boundary concerns a single implementing system, not the operational model in general. |

This list is deliberately closed by default. A new tag **should** only be proposed when an observed Boundary Condition does not fit any existing tag, and **shall** itself first appear as an Architectural Observation before being added here — the vocabulary evolves under the same evidence discipline as the Core. No additional tags are introduced by this document; the eleven above were judged sufficient at the time of writing.

---

# Architectural Decision Rules

1. Core **SHALL NOT** be extended on the basis of a single Reference Case.
2. Proposed Core extensions **SHOULD** be supported by multiple independent Reference Cases — independent meaning distinct authors, domains, or operational contexts, not repeated submissions of the same underlying case — demonstrating the same architectural limitation.
3. Architectural Observations **SHALL** be recorded, in `Architecture-Observations.md`, before any architectural decision is made.
4. A repeated boundary pattern, evidenced across independent Reference Cases, **MAY** initiate an ADR Candidate in `ADR-Candidates.md`. It does not initiate an ADR directly — an ADR Candidate is reviewed and, if promoted, an ADR is authored by the Chief Architect, per the existing Governance process.
5. A Reference Case **SHALL NOT** modify the Core directly, under any circumstance.
6. A Reference Case that demonstrates existing Core concepts are sufficient **SHALL** be closed without escalation, and is a valid, complete outcome.
7. Reference Cases **SHOULD** include External Assurance where practicable, to keep the evidentiary basis distinguishable from unverified hypothesis.

---

# Decision Lifecycle

```text
Reference Case
      │
      ▼
Observation
      │
      ▼
Repeated Pattern
      │
      ▼
ADR Candidate
      │
      ▼
Architecture Review
      │
      ▼
Specification Change (optional)
```

- **Reference Case** — a documented instance of applying OCOM to an operational scenario, using the template in Section 3.
- **Observation** — recorded in `Architecture-Observations.md` when a Reference Case's Boundary Conditions suggest something worth tracking. Recording an Observation is not itself a decision.
- **Repeated Pattern** — recognized when independent Reference Cases produce Observations with matching Boundary Tags.
- **ADR Candidate** — recorded in `ADR-Candidates.md` once a Repeated Pattern exists, per Rule 4.
- **Architecture Review** — the Chief Architect reviews the ADR Candidate and records a Decision, per the existing ADR Candidates process.
- **Specification Change (optional)** — the majority of paths through this lifecycle end before this stage. Only a Decision of "Promote to ADR," followed by the Chief Architect authoring the ADR, results in a Core change.

---

# Relationship to OCOM Specification

This document:

- does **not** change OCOM Core;
- does **not** introduce new architectural concepts;
- does **not** relocate business policies into Core — a Reference Case such as a Payment Prioritization Policy remains an external Operational Policy, expressed using existing Core concepts, exactly as concluded in the architectural review preceding this document;
- defines **only** the process by which evidence is gathered and, where warranted, escalated toward a Core decision.

It sits alongside, and depends on, the existing Governance apparatus: `Core/Governance.md` (the charter for specification evolution), `Governance-Manifest.md` (the principles this methodology operationalizes), `Architecture-Observations.md` and `ADR-Candidates.md` (the mechanisms this methodology feeds), and `Knowledge-Map.md` (where Reference Cases, once accumulated, may be reflected).

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial draft |
| 0.1 | 22 July 2026 | Added Principle of Minimal Evolution |

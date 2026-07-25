<!-- nav:start -->
[Docs](README.md) / OCOM Project Status

[↑ Up](README.md)

---
<!-- nav:end -->

# OCOM Project Status

**Document ID:** PROJECT-STATUS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

This is a snapshot, not a normative document. For the full history and forward-looking notes, see [`ROADMAP.md`](../ROADMAP.md). For the process by which any of this changes, see [`Governance/`](Governance/README.md).

## Current Version

**v0.1 Core Specification** — Released.

## Completed Subsystems

| Subsystem | Location | Status |
|---|---|---|
| Meta-model | `Meta/` | Released, part of v0.1 Core |
| Structural models | `Models/` | Released, part of v0.1 Core |
| Language & Conformance | `Language/` | Released, part of v0.1 Core |
| Domain profiles (12 domains) | `Domains/` | Released, part of v0.1 Core |
| Entity catalog | `Entities/` | Released, part of v0.1 Core |
| Reference Architecture | `Reference Architecture/` | Released, Informative |
| Worked example (iGaming) | `Examples/` | Released, Informative |
| Memory | `Memory/` | Released; two subsections (Definition, Independence, Conformance) intentionally deferred — see Future Work FW-001 |
| AI extension layer | `AI/` | Released, part of v0.1 Core |
| Workflows | `Workflows/` | Not started — folder exists, no content |

## Governance Status

**Baseline**, established and frozen 22 July 2026. 10 documents: Governance Manifest, Standard Evolution Methodology, Documentation Debt, Architecture Observations, ADR Candidates, Knowledge Map, Documentation Standards, Development Readiness, Release Readiness, Architecture Health. Further change to this section requires the process it defines — it does not change by direct edit.

## Adoption Status

**Complete (M021)**, 22 July 2026. `docs/Adoption/` — README, Getting Started, First Pilot, FAQ, Common Mistakes. Restates existing specification content for first-time readers; introduces no new concepts.

## Reader Status

**Complete (Specification v0.2)**, Architecture Committee Approved with Editorial Changes, 22 July 2026. `docs/Specification/` — nine-chapter reading path (Executive Overview through Conformance) plus the Committee Review Package. A compilation layer over the granular documents, not a replacement for them.

## What Is Stable

- The Meta-model and structural models (`Meta/`, `Models/`) — unchanged since v0.1 release, no open ADR affects their definitions.
- Governance and the Specification v0.2 reading path — Baseline.
- The Adoption Framework.

## What Is Under Exploration

- **OBS-003** (`Governance/Architecture-Observations.md`) — a Reference Case proposing Object attribute lifecycle categories and a versioned Object Type. Open. Not part of the Core; requires independent corroboration before further consideration.
- **Workflows** — folder exists, no content yet.
- Reference Implementation, SDK, and Reference Agent — not started, not yet scoped.

## What Is Normative vs. Informative

Per-document `Status` fields are authoritative; as a general guide:

- **Normative (Status: Draft):** `Meta/`, `Models/`, `Language/`, most of `Core/`, `Domains/`, `Entities/`, `AI/`, most of `Memory/`, the Governance rule-sets (e.g. `Standard Evolution Methodology.md`), and Specification Chapters 1–2, 4–8.
- **Informative (Status: Informative):** `Examples/`, `Reference Architecture/`, `Adoption/` in full, the Specification's Executive Overview and Committee Review Package, and most of `Governance/`'s registers and logs.

## Known Discrepancy (recorded, not corrected)

`Governance/Architecture-Health.md` lists "Governance: Draft" in its 22 July 2026 snapshot, recorded before Governance was declared Baseline later the same day. Per this Milestone's scope, `Governance/` is not edited to fix this — it is recorded here for visibility and will be corrected at the next Architecture Health snapshot, which is `Governance/`'s own process to run.

---

*This document restates the status recorded in `ROADMAP.md`, `Governance/Release-Readiness.md`, `Governance/Architecture-Observations.md`, and the commit history. It defines nothing and is not itself a source of truth for any status it reports.*

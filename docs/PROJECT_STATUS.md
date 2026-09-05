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
| Meta-model | `Meta/` | Released in v0.1 |
| Structural models | `Models/` | Released in v0.1 |
| Language & Conformance | `Language/` | Released in v0.1 |
| Domain profiles (12 domains) | `Domains/` | Released in v0.1 |
| Entity catalog | `Entities/` | Released in v0.1 |
| Reference Architecture | `Reference Architecture/` | Released, Informative |
| Worked example (iGaming) | `Examples/` | Released, Informative |
| Memory | `Memory/` | Released; two subsections (Definition, Independence, Conformance) intentionally deferred — see Future Work FW-001 |
| AI extension layer | `AI/` | Released in v0.1 |
| Workflows | `Workflows/` | Not started — folder exists, no content |

In this table, "v0.1" is the release named "v0.1: Core Specification" in `ROADMAP.md`. The word "Core" in that release name is a release label; it is not the Domain-Neutral Core of Constitution §9. For §9's purposes, `Governance/Constitution-Step0-Summary.md` Decision 4 defines Core by semantic invariance across industries: it includes `Core/`, `Meta/`, `Models/`, `Language/`, `Governance/`, `Memory/`, `AI/`, `Lifecycles/` and `Reference Architecture/`; it excludes `Entities/` and `Examples/`; it treats `Domains/` as a borderline case under ongoing per-document review. `Domains/` and `Entities/` are therefore released content of v0.1, normative by their own Status, and not part of the §9 Core. §9's own wording has not yet been updated to state its scope; that transcription is an open Backlog item (`Master-Architecture-Backlog.md` EPIC-D, `CAND-007` §3).

## Governance Status

**Baseline**, established and frozen 22 July 2026. 10 documents at the 22 July 2026 baseline (the directory has since grown through the same process; 25 files as of 5 September 2026): Governance Manifest, Standard Evolution Methodology, Documentation Debt, Architecture Observations, ADR Candidates, Knowledge Map, Documentation Standards, Development Readiness, Release Readiness, Architecture Health. Further change to this section requires the process it defines — it does not change by direct edit.

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

- **Normative (Status: Draft):** `Meta/`, `Models/`, `Language/`, most of `Core/`, `Domains/`, `Entities/`, `AI/`, most of `Memory/`, the Governance rule-sets (e.g. `Standard Evolution Methodology.md`), and Specification Chapters 1–8 (Chapter 3 contains no shall-statement and keeps Status Draft by Architecture Committee decision, `Specification/Committee Review Package.md` Section 8 item 5: status reflects chapter maturity as part of the normative specification, not shall-density).
- **Informative (Status: Informative):** `Examples/`, `Reference Architecture/`, `Adoption/` in full, the Specification's Executive Overview and Committee Review Package, and most of `Governance/`'s registers and logs.

## Known Discrepancy (recorded, not corrected)

`Governance/Architecture-Health.md` lists "Governance: Draft" in its 22 July 2026 snapshot, recorded before Governance was declared Baseline later the same day. Per this Milestone's scope, `Governance/` is not edited to fix this — it is recorded here for visibility and will be corrected at the next Architecture Health snapshot, which is `Governance/`'s own process to run.

---

*This document restates the status recorded in `ROADMAP.md`, `Governance/Release-Readiness.md`, `Governance/Architecture-Observations.md`, and the commit history. It defines nothing and is not itself a source of truth for any status it reports.*

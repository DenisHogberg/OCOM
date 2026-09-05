<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Publication Model

[← Back](Master-Architecture-Backlog.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Publication Model

**Document ID:** GOV-PUBLICATION-MODEL-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 August 2026

---

# Purpose

A re-verification of ocom.uno against this repository found that version identifiers, publication layers, normative references, and file statuses do not currently form one unambiguous chain from canonical source to public authoritative artifact. Specifically: the site shows "Core Vocabulary v0.1"; `Core/Constitution.md` is v1.0; the only GitHub tag/release is named `v1.0.0` and was cut on commit `f7a33e238e7c1b11482853fcbba648d350c20fa3` (22–23 July 2026) — **before** Constitution v1.0 was adopted (`CAND-006`, 26–27 July) and before the Architecture Freeze (`CAND-007`, 27 July). Three numbers currently describe overlapping-but-different things with no documented relationship between them.

This document is that relationship, stated once. It executes `Master-Architecture-Backlog.md`'s `EPIC-F` ("Specification Currency & Presentation") and is itself Informative — it documents governance/publication structure, it does not add a Canonical Principle, a Meta Object, or change Object/Memory/Evidence/Knowledge. Nothing here requires a Freeze exception under `CAND-007`.

---

# The Versioning Model

Four independent version tracks. The confusion the audit found comes from treating these as one axis; they are not, and are not meant to be.

| Track | Owner document | Current value | Changes via |
|---|---|---|---|
| **Constitution** | `Core/Constitution.md` (`Core-00`) | v1.0 | RFC-like amendment only — the process `Constitution.md`'s own Governance implication already states: Reference Case or direct proposal → ADR Candidate → Chief Architect Decision, never an editorial edit. |
| **Core Vocabulary** | the 13 `Meta/` term set (Capability, Classification, Constraint, Contract, Identity, Metadata, Object, Organization, Ownership, Policy, Reference, Registry, Relationship), published individually on ocom.uno | v0.1 | Ordinary ADR Candidate, per term — a term's own definition can be refined without touching a Canonical Principle, and vice versa. |
| **Specification** (compiled reading path) | `docs/Specification/*` (`SPEC-00` through `SPEC-08`, plus the Committee Review Package) | v0.2 | Editorial recompilation of the granular canonical documents — see "Publication Layers" below. Must record which Constitution and Core Vocabulary versions it was compiled from; this was not previously done and is closed by this document (see "Known Gaps"). |
| **Release** (public, citable identifier) | GitHub tag/release, resolved by `Publication-Manifest.md` | `v1.0.0` (mislabeled — see below) | An independent semver track. **Does not mirror any single component's version number.** Names one specific bundle: {this Constitution version + this Core Vocabulary version + this Specification version + this commit}. |

Treating Release as its own track, rather than assuming it equals Constitution's version, is the specific fix for how `v1.0.0` came to be cut before Constitution v1.0 existed: a Release identifier that numerically echoes one internal component's version invites exactly that kind of premature or misleading naming. Decoupling them means a future Release can be minted whenever a coherent, reviewed bundle is ready, independent of which internal track happens to have moved most recently.

---

# Answering the Six Authoritative-Version Questions

1. **Which version is authoritative?** Whichever entry `Publication-Manifest.md` lists as current (not superseded).
2. **Which documents are in that version?** Resolved by checking out the Manifest entry's declared `commit` — `Publication-Manifest.md` does not carry a separate document-list field; the commit itself pins the exact file set.
3. **Which Git commit corresponds to it?** The `commit` field on that Manifest entry.
4. **Which public artifact corresponds to it?** The `published_artifacts` field on that Manifest entry.
5. **Which machine-readable representations were generated from it?** The `projections` field on that Manifest entry.
6. **How can one confirm the site and GitHub publish the same version?** By comparing the Manifest entry's `commit` field against whatever commit or version marker the live site exposes. **This repository can state this contract; it cannot enforce it** — see "Known Gaps."

---

# Publication Layers

Five tiers, not two. Confusing "what OCOM says" with "what got compiled into a reading path" or "what got rendered onto a web page" is the direct cause of several findings in the re-verification audit (e.g., a `SHALL` sentence in `Specification/05 Object Model.md` referencing "Lifecycle" as if it had a Core Vocabulary term card, when Lifecycle is defined at `Models/` tier, not `Meta/` tier, and so has no card at all).

## 1. Canonical Source

The granular Markdown documents under `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Domains/`, `Entities/`, `Lifecycles/`, `AI/`, `Reference Architecture/`, and `Governance/` — git-tracked, PR-reviewed, individually versioned. This is the normative text. Nothing downstream of this tier introduces new requirements; everything downstream either restates or renders it.

## 2. Compiled Publication

`docs/Specification/*` — an editorial reading path over the canonical sources, already self-described in `Specification/Committee Review Package.md` as *"an editorial layer, not a new specification... every normative statement it contains is drawn from documents the committee has already implicitly accepted."* Must cite, per document, which canonical sources it compiles and at what version — `02 Design Principles.md` already does this correctly (*"Source: compiled from `Core/Principles.md`, verbatim"*); `01 Introduction.md`'s RFC 2119 section did not, until this document's companion fix (see Work Item 3/4 in the governing plan — `Core/Manifest.md` is now the single source; `01 Introduction.md` restates it by reference).

## 3. Projection

A machine-generated representation of a single canonical document, produced by the external Publication Engine (see "Known Gaps" — this repository contains no code, config, or documentation for that engine; it lives entirely outside this repository). Two instances currently recognized — recognizing a second instance does not create a new tier; both share the same mandatory fields (`Version`, `Status`, `source_file`, `source_url`, `history_url`) and the same rule that canonical source is GitHub and the projection itself is never edited directly:

- **Core Vocabulary term-cards** — the individual term-cards on ocom.uno (`/vocabulary/<term>`) — HTML, JSON, JSON-LD, and Markdown representations, generated from the Core Vocabulary (`Meta/`) canonical source.
- **Adoption pages** — `ocom.uno/adoption/<page>` — generated from an individually-authorized `docs/Adoption/*.md` file. A file qualifies only once it has its own separate Decision (`CAND-012`; e.g. `CAND-010` for the Worked Example, `CAND-011` for First Pilot) — directory membership in `docs/Adoption/` grants nothing by itself.

## 4. Convenience Representation

The homepage, `/changelog`, and `/comparisons/*` pages, together with the site-held informative records (`/why`, `/evidence-register`, `/specification/how-to-review`, `/api`, `/observatory` and their JSON records, whose canonical record lives in the external Publication Engine, not in this repository) — informative, illustrative, explicitly not carrying independent normative weight, and not required to cite a versioned canonical source the way a Projection of a specific term is.

## 5. Consumer Tool

An interactive, read-only tool published on the site (currently one instance: `ocom.uno/shape-check`), authorized by its own ADR Candidate (`CAND-013`, Decided 21 August 2026). A Consumer Tool consumes published projections, creates no normative requirements, is not a source of truth, and must state its non-normative status on its own page.

---

# Authoritative Source Per Publication Unit

| Field | Core Vocabulary | Specification |
|---|---|---|
| **Source of Truth** | `docs/Meta/*.md` (13 files) | `docs/Specification/*.md` (compiled from `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Governance/`) |
| **Release Identifier** | Resolved via `Publication-Manifest.md` | Resolved via `Publication-Manifest.md` |
| **Commit** | Resolved via `Publication-Manifest.md` | Resolved via `Publication-Manifest.md` |
| **Specification Version** | n/a (Core Vocabulary is its own track) | `0.2` (`docs/Specification/*` headers; the live site shows `0.2` as of 4 September 2026) |
| **Publication Date** | 2026-07-20 (site) — not independently confirmable against a repo commit; see "Known Gaps" | 2026-07-22 (Committee Review Package `Prepared` date) |
| **Publication URL** | `https://ocom.uno/vocabulary` and `https://ocom.uno/vocabulary/<term>` | `https://ocom.uno/specification` and `https://ocom.uno/specification/normative` |
| **Machine-readable Projection** | HTML, JSON, JSON-LD, Markdown (per `/changelog`'s own claim) — no versioned source file for the generated JSON-LD exists in this repository | None currently generated per-chapter; the compiled Markdown itself is the only machine-readable form |

---

# Known Gaps (Stated Honestly, Not Solved Here)

- **Resolved, 4 September 2026: the live site previously showed Specification `v0.1` while this repository stated `v0.2`.** The site was republished from the current repository state: `ocom.uno/specification`, `/executive`, `/normative` and `/annex` now carry the nine-chapter v0.2 reading path (SPEC-00..08) compiled verbatim from `docs/Specification/`, with per-chapter source-file citations. The remaining, unsolved part is the general one recorded in the next bullet: this repository still cannot verify from inside itself which commit the site was built from.
- **No exposed commit/version marker from the external Publication Engine.** This repository can declare, in `Publication-Manifest.md`, which commit a release corresponds to. It cannot verify from inside itself that the live site was actually built from that commit — the Publication Engine is confirmed to be entirely external (no deploy/publish workflow, no site-generator config, no GitHub Pages configured, "Publication Engine" appears nowhere in this repository). Closing this gap requires the external system to expose its own build/source marker; tracked as a Future Work item in `Documentation-Debt.md`, not solved by this document.
- **The generated JSON-LD projection has no versioned source file in this repository.** The site claims (`/changelog`) that each of the 13 Core Vocabulary terms carries an HTML/JSON/JSON-LD/Markdown projection. The Markdown source (`Meta/*.md`) is versioned and reviewable; the JSON-LD is not — it is generated by the external engine with no corresponding artifact here to diff or review against.
- **`v1.0.0`'s actual scope does not match its name.** Documented precisely in `Publication-Manifest.md`.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 August 2026 | Initial document — versioning model, publication-layer tiers, authoritative-source table, known gaps. Executes `Master-Architecture-Backlog.md` `EPIC-F`. |
| 0.1 | 4 September 2026 | Added tier 5 (Consumer Tool, per `CAND-013`); recorded the live site's republication of the v0.2 reading path and closed the corresponding Known Gap. |
| 0.1 | 20 August 2026 | Corrected on independent review: Status changed Informative → Draft (this is a `Governance/` process document, not an analysis document, per `Documentation-Standards.md`'s Status Taxonomy); question 2's answer no longer cites a nonexistent `canonical_sources` Manifest field; added a Known Gap disclosing the live site's Specification `v0.1` vs. this repository's `v0.2` |
| 0.1 | 5 September 2026 | Tier 4 now names the site-held informative records (`/why`, `/evidence-register`, `/specification/how-to-review`, `/api`, `/observatory`), which previously belonged to no tier. |

<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Publication Model

[← Back](Master-Architecture-Backlog.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Publication Model

**Document ID:** GOV-PUBLICATION-MODEL-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 22 September 2026

---

# Purpose

A re-verification of ocom.uno against this repository found that version identifiers, publication layers, normative references, and file statuses do not currently form one unambiguous chain from canonical source to public authoritative artifact. Specifically: the site shows "Core Vocabulary v0.1"; `Core/Constitution.md` is v1.0; at the time of that audit the only GitHub tag/release was named `v1.0.0` and was cut on commit `f7a33e238e7c1b11482853fcbba648d350c20fa3` (22–23 July 2026) — **before** Constitution v1.0 was adopted (`CAND-006`, 26–27 July) and before the Architecture Freeze (`CAND-007`, 27 July). Three numbers currently describe overlapping-but-different things with no documented relationship between them.

This document is that relationship, stated once. It executes `Master-Architecture-Backlog.md`'s `EPIC-F` ("Specification Currency & Presentation") and is itself a governance document, Status Draft per its Revision History — it documents governance/publication structure, it does not add a Canonical Principle, a Meta Object, or change Object/Memory/Evidence/Knowledge. Nothing here requires a Freeze exception under `CAND-007`.

---

# The Versioning Model

Four independent version tracks. The confusion the audit found comes from treating these as one axis; they are not, and are not meant to be.

| Track | Owner document | Current value | Changes via |
|---|---|---|---|
| **Constitution** | `Core/Constitution.md` (`Core-00`) | 1.0.1 (since 11 September 2026) | RFC-like amendment only — the process `Constitution.md`'s own Governance implication already states: Reference Case or direct proposal → ADR Candidate → Chief Architect Decision, never an editorial edit. |
| **Core Vocabulary** | the 13 `Meta/` term set (Capability, Classification, Constraint, Contract, Identity, Metadata, Object, Organization, Ownership, Policy, Reference, Registry, Relationship), published individually on ocom.uno | v0.1 | Ordinary ADR Candidate, per term — a term's own definition can be refined without touching a Canonical Principle, and vice versa. |
| **Specification** (compiled reading path) | `docs/Specification/*` (`SPEC-00` through `SPEC-08`, plus the Committee Review Package, which keeps the v0.2 review record) | 1.0 (since 17 September 2026) | Editorial recompilation of the granular canonical documents — see "Publication Layers" below. Must record which Constitution and Core Vocabulary versions it was compiled from; this was not previously done and is closed by this document (see "Known Gaps"). |
| **Release** (public, citable identifier) | GitHub tag/release, resolved by `Publication-Manifest.md` | `v1.4.0` (current, 22 September 2026; `v1.3.0`, `v1.2.0` and `v1.1.1` Superseded; `v1.0.0` was mislabeled, see below) | An independent semver track. **Does not mirror any single component's version number.** Names one specific bundle: {this Constitution version + this Core Vocabulary version + this Specification version + this commit}. |

Treating Release as its own track, rather than assuming it equals Constitution's version, is the specific fix for how `v1.0.0` came to be cut before Constitution v1.0 existed: a Release identifier that numerically echoes one internal component's version invites exactly that kind of premature or misleading naming. Decoupling them means a future Release can be minted whenever a coherent, reviewed bundle is ready, independent of which internal track happens to have moved most recently.

---

# Answering the Six Authoritative-Version Questions

1. **Which version is authoritative?** Whichever entry `Publication-Manifest.md` lists as current (not superseded).
2. **Which documents are in that version?** Resolved by checking out the Manifest entry's declared `Commit` — `Publication-Manifest.md` does not carry a separate document-list field; the commit itself pins the exact file set.
3. **Which Git commit corresponds to it?** The `Commit` field on that Manifest entry.
4. **Which public artifact corresponds to it?** The `Published Artifacts` field on that Manifest entry.
5. **Which machine-readable representations were generated from it?** The `Machine-readable Projections` field on that Manifest entry.
6. **How can one confirm the site and GitHub publish the same version?** By comparing the Manifest entry's `Commit` field against whatever commit or version marker the live site exposes. **This repository can state this contract; it cannot enforce it** — see "Known Gaps."

---

# Publication Layers

Five tiers, not two. Confusing "what OCOM says" with "what got compiled into a reading path" or "what got rendered onto a web page" is the direct cause of several findings in the re-verification audit (e.g., a `SHALL` sentence in `Specification/05 Object Model.md` referencing "Lifecycle" as if it had a Core Vocabulary term card, when Lifecycle is defined at `Models/` tier, not `Meta/` tier, and so has no card at all).

## 1. Canonical Source

The granular Markdown documents under `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Domains/`, `Entities/`, `Lifecycles/`, `AI/`, `Reference Architecture/`, and `Governance/` — git-tracked, PR-reviewed, individually versioned. This is the normative text. Nothing downstream of this tier introduces new requirements; everything downstream either restates or renders it.

## 2. Compiled Publication

`docs/Specification/*` — an editorial reading path over the canonical sources, already self-described in `Specification/Committee Review Package.md` as *"an editorial layer, not a new specification... every normative statement it contains is drawn from documents the committee has already implicitly accepted."* Must cite, per document, which canonical sources it compiles and at what version — `02 Design Principles.md` already does this correctly (*"Source: compiled from `Core/Principles.md`, verbatim"*); `01 Introduction.md`'s RFC 2119 section did not, until this document's companion fix (see Work Item 3/4 in the governing plan — `Core/Manifest.md` is now the single source; `01 Introduction.md` restates it by reference).

**What a chapter carries, and where the obligation sits (`CAND-018`, Decided 19 September 2026).** A compiled chapter may abridge the documents its Source line names, and states no obligation of its own. A mandatory Statement a chapter does not carry is unaffected by the omission: it lives in the canonical document, which this tiering calls the normative text, so an omission from a chapter is a defect of the reading path and never a discharge of the requirement. A chapter's Source line shall say which of three forms it takes:

- `synthesized from`: the chapter carries none of its sources' Statements as obligations.
- `compiled from`: the chapter carries them in summary and may abridge.
- `compiled from ... verbatim`: the chapter carries every mandatory Statement of the sections its Source line names.

All nine chapters declare one of the three today. The two that declare verbatim, `01 Introduction.md` and `02 Design Principles.md`, were checked against their sources on 19 September 2026 and carry every mandatory sentence of the sections they name; the fourth omission `AO-077` records was found in the second of them and corrected the same day. `tools/conformance/compilation_survey.py` now runs that check on every build: for a chapter declaring verbatim it is a gate, and for the other two forms it prints how much of its sources the chapter carries, since abridgement is permitted and worth knowing the size of. The first survey found the five chapters declaring plain `compiled from` carry 28 of the 249 mandatory Statements their sources hold; the figures per chapter are recorded in `AO-077`.

## 3. Projection

A machine-generated representation of a single canonical document, produced by the external Publication Engine (see "Known Gaps" — this repository contains no code, config, or documentation for that engine; it lives entirely outside this repository). Two instances currently recognized — recognizing a second instance does not create a new tier; both share the same mandatory fields (`Version`, `Status`, `source_file`, `source_url`, `history_url`) and the same rule that canonical source is GitHub and the projection itself is never edited directly:

- **Core Vocabulary term-cards** — the individual term-cards on ocom.uno (`/vocabulary/<term>`) — HTML, JSON, JSON-LD, and Markdown representations, generated from the Core Vocabulary (`Meta/`) canonical source.
- **Adoption pages** — `ocom.uno/adoption/<page>` — generated from an individually-authorized `docs/Adoption/*.md` file. A file qualifies only once it has its own separate Decision (`CAND-012`; e.g. `CAND-010` for the Worked Example, `CAND-011` for First Pilot, `CAND-026` for the Reference Serialization, `CAND-028` for The First 90 Days) — directory membership in `docs/Adoption/` grants nothing by itself.

**What a generated file's own names assert (`CAND-019`, Decided 19 September 2026).** A projection may coin names for its own structures, and those names are local to the publication: they assert nothing about the Core Vocabulary and create no governed term. Two rules follow, and both are checkable from the published file alone:

- A name a generated file coins shall expand to a URI that file's publisher defines, or the file shall use a fully qualified term from a vocabulary that defines it.
- A generated file shall not reuse the name of a governed Core Vocabulary term for a local construct, because a reader cannot tell the borrowing from a claim.

`AO-078` records the instance that produced the rules: `graph.jsonld` types its edges with a prefixed name that expands to a URI the site defines nowhere, and borrows the name of the governed term Reference to do it.

## 4. Convenience Representation

The homepage, `/changelog`, and `/comparisons/*` pages, together with the site-held informative records (`/why`, `/specification/how-to-review`, `/api`, `/observatory` and their JSON records, whose canonical record lives in the external Publication Engine, not in this repository; the Evidence Register left this tier on 19 September 2026 and is now the canonical `Governance/Evidence-Register.md`, per `CAND-022`, with its published URLs redirecting there) — informative, illustrative, explicitly not carrying independent normative weight, and not required to cite a versioned canonical source the way a Projection of a specific term is.

## 5. Consumer Tool

An interactive, read-only tool published on the site (currently one instance: `ocom.uno/shape-check`), authorized by its own ADR Candidate (`CAND-013`, Decided 21 August 2026). A Consumer Tool consumes published projections, creates no normative requirements, is not a source of truth, and must state its non-normative status on its own page.

---

# Authoritative Source Per Publication Unit

| Field | Core Vocabulary | Specification |
|---|---|---|
| **Source of Truth** | `docs/Meta/*.md` (13 files) | `docs/Specification/*.md` (compiled from `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Governance/`) |
| **Release Identifier** | Resolved via `Publication-Manifest.md` | Resolved via `Publication-Manifest.md` |
| **Commit** | Resolved via `Publication-Manifest.md` | Resolved via `Publication-Manifest.md` |
| **Specification Version** | n/a (Core Vocabulary is its own track) | `1.0` (`docs/Specification/*` headers; the live site shows `1.0` since 17 September 2026) |
| **Publication Date** | 2026-07-20 (site) — not independently confirmable against a repo commit; see "Known Gaps" | 2026-07-22 (Committee Review Package `Prepared` date) |
| **Publication URL** | `https://ocom.uno/vocabulary` and `https://ocom.uno/vocabulary/<term>` | `https://ocom.uno/specification` and `https://ocom.uno/specification/normative` |
| **Machine-readable Projection** | HTML, JSON, JSON-LD, Markdown (per `/changelog`'s own claim) — no versioned source file for the generated JSON-LD exists in this repository | None currently generated per-chapter; the compiled Markdown itself is the only machine-readable form |

---

# Known Gaps (Stated Honestly, Not Solved Here)

- **Resolved, 4 September 2026: the live site previously showed Specification `v0.1` while this repository stated `v0.2`.** The site was republished from the current repository state: `ocom.uno/specification`, `/executive`, `/normative` and `/annex` now carry the nine-chapter v0.2 reading path (SPEC-00..08) compiled verbatim from `docs/Specification/`, with per-chapter source-file citations. The remaining, unsolved part is the general one recorded in the next bullet: this repository still cannot verify from inside itself which commit the site was built from.
- **No exposed commit/version marker from the external Publication Engine.** This repository can declare, in `Publication-Manifest.md`, which commit a release corresponds to. It cannot verify from inside itself that the live site was actually built from that commit — the Publication Engine is confirmed to be entirely external (no deploy/publish workflow, no site-generator config, no GitHub Pages configured, "Publication Engine" appears nowhere in this repository). Closing this gap requires the external system to expose its own build/source marker; tracked as a Future Work item in `Documentation-Debt.md`, not solved by this document.
- **The generated JSON-LD projection has no versioned source file in this repository.** The site claims (`/changelog`) that each of the 13 Core Vocabulary terms carries an HTML/JSON/JSON-LD/Markdown projection. The Markdown source (`Meta/*.md`) is versioned and reviewable; the JSON-LD is not — it is generated by the external engine with no corresponding artifact here to diff or review against.
- **Narrowed, 18 September 2026: the site's own verification layer is reproducible again.** `/observatory/health.json` and `/observatory/publication-health.json` were produced by the lost Publication Engine and could not be recomputed by anyone, which made them claims no reader could check. `tools/site/publication_health.py` in this repository now recomputes both from the published site alone, reproducing every figure they carry (83 references, 35 mutual pairs, 13 references with no reverse, 13 terms, zero orphans, duplicates and broken links) and every one of their fourteen rows. The directed-cycle count stays carried forward, since its counting rule was never published. This does not close the gap above: the tool checks what the site publishes, not that the site was built from the commit the Manifest names.
- **Narrowed, 18 September 2026: the Specification projection now exposes its source commit.** `specification.json`, `specification.md` and the reading-path pages name the commit they were compiled from, so for that projection the sixth question can be answered from the site. The other projections still expose no marker.
- **Stewardship of the name is outside this specification (`CAND-017`, Decided in part, 19 September 2026).** Nothing here records who may use the words OCOM and OCOM-compatible, or what follows from a false claim of conformance. That is a right in a name rather than a property of the model: this specification holds no such right, `LICENSE` (Apache-2.0, Section 6) withholds the Licensor's marks, the text under `docs/` is CC BY 4.0, whose Section 2(b)(2) does not license trademark rights, and `Core/Manifest.md`'s Scope excludes the legal judgment. What a public conformance claim shall carry is a different question, inside scope at the Language tier, and its text waits on a second independent Reference Case.
- **Narrowed, 19 September 2026: the machine-facing files the Engine never generated now have a source here.** `llms.txt` is written by hand on the server and was sourced by nothing in this repository, which is how it came to publish `https://ocom.uno/why.`, a URL that answers 404 to every machine that harvested it. `publication/` now holds the canonical copy of each such file, `publication/README.md` names its published path and the rule that the served bytes shall match it, and `tools/site/published_source_parity.py` checks both halves: the lint needs no network and runs in CI, the comparison fetches the site and does not. `AO-083` records the instance. This narrows nothing above: the files a generator does produce still depend on an engine that is gone.
- **`v1.0.0`'s actual scope does not match its name.** Documented precisely in `Publication-Manifest.md`.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 August 2026 | Initial document — versioning model, publication-layer tiers, authoritative-source table, known gaps. Executes `Master-Architecture-Backlog.md` `EPIC-F`. |
| 0.1 | 4 September 2026 | Added tier 5 (Consumer Tool, per `CAND-013`); recorded the live site's republication of the v0.2 reading path and closed the corresponding Known Gap. |
| 0.1 | 20 August 2026 | Corrected on independent review: Status changed Informative → Draft (this is a `Governance/` process document, not an analysis document, per `Documentation-Standards.md`'s Status Taxonomy); question 2's answer no longer cites a nonexistent `canonical_sources` Manifest field; added a Known Gap disclosing the live site's Specification `v0.1` vs. this repository's `v0.2` |
| 0.1 | 5 September 2026 | Tier 4 now names the site-held informative records (`/why`, `/evidence-register`, `/specification/how-to-review`, `/api`, `/observatory`), which previously belonged to no tier. |
| 0.1 | 12 September 2026 | Release track current value updated from `v1.0.0` to `v1.1.1`, per `Publication-Manifest.md`. |
| 0.1 | 16 September 2026 | Release track current value updated from `v1.1.1` to `v1.2.0` and the Constitution track from v1.0 to 1.0.1, per `Publication-Manifest.md` and `Core/Constitution.md`; the six-question answers now name the Manifest's actual field labels (`Commit`, `Published Artifacts`, `Machine-readable Projections`); one audit-narrative sentence in Purpose put in the past tense and the document's Status named correctly. Found by the dogfooding audit of Release v1.2.0. |
| 0.1 | 17 September 2026 | Specification track current value updated from v0.2 to 1.0: the nine chapters recompiled against the canonical documents on 17 September 2026, per the Chief Architect's decision of the same day; the Committee Review Package keeps its v0.2 record. |
| 0.1 | 18 September 2026 | Known Gaps: two entries narrowed, the site's Observatory records are recomputable from this repository and the Specification projection names its source commit; the engine gap itself is unchanged. |
| 0.1 | 18 September 2026 | Release track current value updated to `v1.3.0` and the Specification Version cell of the authoritative-source table from `0.2` to `1.0`; both had been stale since the 17 September 2026 release. |
| 0.1 | 19 September 2026 | Step 2 of three Decisions of the same day: the Compiled Publication tier states what a chapter carries and which form its Source line declares (`CAND-018`); the Projection tier states that a generated file's coined names are local and carries the two rules that follow (`CAND-019`); Known Gaps records that stewardship of the name is outside this specification (`CAND-017`). |
| 0.1 | 19 September 2026 | Known Gaps: the machine-facing files the Publication Engine never generated now have canonical sources under `publication/` and a checker (`AO-083`); the Compiled Publication tier records that the backward check of `CAND-018`'s three forms is now a build-time check, with the first survey's figures. |
| 0.1 | 19 September 2026 | Tier 4: the Evidence Register is no longer a site-held record. `CAND-022` moved it to `Governance/Evidence-Register.md`, where it is versioned, reviewed and archived with each Release; `ocom.uno/evidence-register` and `/implementations` redirect to it. |
| 0.1 | 22 September 2026 | Tier 3, Adoption pages: `CAND-026` named as the Decision authorizing `docs/Adoption/Reference Serialization.md` and its page; no tier changed. |
| 0.1 | 22 September 2026 | Tier 3, Adoption pages: `CAND-028` named as the Decision authorizing `docs/Adoption/First 90 Days.md` and its page; no tier changed. |
| 0.1 | 22 September 2026 | Release track current value updated to `v1.4.0` (22 September 2026, Zenodo version DOI `10.5281/zenodo.22900969`). |

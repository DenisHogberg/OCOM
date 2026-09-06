<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Publication Manifest

[← Back](Publication-Model.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Publication Manifest

**Document ID:** GOV-PUBLICATION-MANIFEST-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 August 2026

---

# Purpose

The record of what each public Release actually contains, resolving the questions `Publication-Model.md` poses in the abstract into concrete values. Entries use a fixed field set so a script (or a human) can check consistency without ambiguity: `Release Identifier`, `Commit`, `Constitution Version`, `Core Vocabulary Version`, `Specification Version`, `Publication Date`, `Published Artifacts`, `Machine-readable Projections`, `Status`.

Entries are append-only, mirroring the same discipline already used for `ADR-Candidates.md` and `Architecture-Observations.md` — a superseded entry is marked `Superseded`, never edited to look like it always described what it now describes.

---

## Release: `v1.0.0`

| Field | Value |
|---|---|
| **Release Identifier** | `v1.0.0` |
| **Commit** | `f7a33e238e7c1b11482853fcbba648d350c20fa3` |
| **Constitution Version** | **None — Constitution did not exist at this commit.** This commit is dated 2026-07-22T16:39:29Z; `Core/Constitution.md` was added in commit `0045edc` (`docs(core): integrate Constitution into Core specification`) on 2026-07-27, roughly five calendar days later. |
| **Core Vocabulary Version** | 0.1 — precision note: `docs/Meta/Organization.md` was added in commit `efbd830` (25 July 2026, three days after this release's commit) under the same `0.1` label, with no version bump to mark the addition. "Core Vocabulary v0.1" therefore does not, by itself, distinguish the 12-term set present at this release's commit from the 13-term set that exists today; the `Commit` field above, not the version number, is what pins the exact file set. |
| **Specification Version** | 0.2 (this commit's own content — `docs(specification): add OCOM Specification v0.2 reading path`) |
| **Publication Date** | Created 2026-07-22T16:39:29Z, Published 2026-07-23T12:55:55Z (GitHub Release timestamps) |
| **Published Artifacts** | GitHub Release "OCOM v1.0.0: Object-Centric Operating Model" (`github.com/DenisHogberg/OCOM/releases/tag/v1.0.0`). Retitled on 6 September 2026: the release had been published as "Object-Centric Operational Model", which is not the name of the model. The title is presentation only; the tag, the commit and the timestamps are unchanged, and the Status below is unaffected. |
| **Machine-readable Projections** | None declared by this release itself — the live site's HTML/JSON/JSON-LD projections are generated on an ongoing basis by the external Publication Engine, not tied to this specific tag |
| **Status** | **Historical — name does not match scope.** Tagged and published as "v1.0.0" before Constitution v1.0 was adopted and before the Architecture Freeze (`CAND-007`). Contains the v0.1 Core Vocabulary and the v0.2 Specification reading path; contains no Constitution. Left unmodified in git history per explicit instruction — not deleted, not retagged. See `Publication-Model.md`, "Known Gaps," and `Documentation-Debt.md` for the follow-up item (cutting a correctly-scoped release) this Status intentionally does not resolve. |

**Corrected description, for citation purposes:** *"OCOM `v1.0.0`, as actually published, contains the OCOM Core Vocabulary v0.1 and the OCOM Specification v0.2 reading path. It does not contain OCOM Constitution v1.0, which was adopted 26 July 2026, after this release's 22 July 2026 commit. It should not be cited as containing the Constitution or the Architecture Freeze."*

---

## Release: *(next, not yet cut)*

| Field | Value |
|---|---|
| **Release Identifier** | `TBD` — per `Publication-Model.md`, this identifier is an independent track and should not be assumed to numerically mirror Constitution's `v1.0` |
| **Commit** | `TBD` |
| **Constitution Version** | `TBD` |
| **Core Vocabulary Version** | `TBD` |
| **Specification Version** | `TBD` |
| **Publication Date** | `TBD` |
| **Published Artifacts** | `TBD` |
| **Machine-readable Projections** | `TBD` |
| **Status** | Not yet cut. Cutting a new tag/release is explicitly deferred — see `Master-Architecture-Backlog.md` Part 8 (Release Readiness) for the criteria that should be met first, and `Documentation-Debt.md` for this item's tracked disposition. |

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 August 2026 | Initial manifest — corrected `v1.0.0` entry (actual scope, marked Historical), placeholder structure for the next release. |
| 0.1 | 20 August 2026 | Corrected on independent review: Status changed Informative → Draft; the Constitution-gap day-count corrected from an imprecise "four days" to explicit dates (five calendar days); added a Core Vocabulary Version precision note (`Meta/Organization.md` added under the same `0.1` label three days after this release's commit, no version bump) |
| 0.1 | 6 September 2026 | Published Artifacts updated after the GitHub Release was retitled from "Object-Centric Operational Model" to "Object-Centric Operating Model". Presentation only: the tag, the commit and the publication timestamps are unchanged, and the Historical Status is unaffected. |

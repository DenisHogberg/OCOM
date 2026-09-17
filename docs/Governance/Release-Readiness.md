<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Release Readiness

[← Back](Knowledge-Map.md) · [↑ Up](README.md) · [Next →](Standard%20Evolution%20Methodology.md)

---
<!-- nav:end -->

# Release Readiness

**Document ID:** GOV-RELEASE-READINESS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 17 September 2026

---

# Purpose

This is a running log. Before each release, the CDKO records an entry synthesizing documentation readiness, open observations, unresolved ADR candidates, critical documentation debt, and a recommendation.

## Pre-Release Checklist

Every release entry from this point forward **shall** confirm the following:

- [ ] Documentation readiness assessed (links, metadata, README coverage)
- [ ] Open Architecture Observations reviewed
- [ ] Unresolved ADR Candidates reviewed
- [ ] Critical Documentation Debt reviewed
- [ ] Standard Evolution Methodology reviewed

---

## Release: v0.1

**Date:** 21 July 2026

**Documentation Readiness:** Ready. 271 normative/informative documents, 0 broken internal links (of 2115), 0 duplicate Document IDs, 100% metadata completeness.

**Open Observations:** OBS-001 (AI/Context content duplication) — open, non-blocking.

**Unresolved ADR Candidates:** CAND-001 (same root cause as OBS-001) — pending Architect review, non-blocking.

**Critical Documentation Debt:** None.

**Known Deferred Content:** `Memory/Evidence Overlay.md` (Definition/Independence/Conformance reserved) and `Entities/Campaign/Campaign.md` (Business Rules removed) — both explicit author decisions, tracked as Future Work (FW-001, FW-002), not blockers.

**Standard Evolution Methodology reviewed:** Not applicable — the methodology was introduced after this release.

**Recommendation:** Approved for release.

**Status:** Released — published to origin/main, 21 July 2026.

---

## Release: v1.1.1

**Date:** 12 September 2026

**Documentation Readiness:** Ready. All CI checks green on the tagged commit `91d40db` (markdownlint, link check, required documents, publication-metadata consistency, REUSE compliance, OpenSSF Scorecard). The Release body's bundle claims are checkable against the `Publication-Manifest.md` entry: Constitution 1.0.1, Core Vocabulary 0.1 (13 governed terms), Specification 0.2.

**Open Observations:** 61 recorded (AO-001 to AO-061): 3 Closed, AO-042 Open in part, AO-008 Escalated to `CAND-009`, one Informative, the rest Open. None blocks a Release: each open item is a disclosed tension in the model, not a defect in a published rule, and the Architecture Freeze (`CAND-007`) holds the Core stable while they are worked.

**Unresolved ADR Candidates:** CAND-001, CAND-002, CAND-004 and CAND-008 Open; 9 Decided; CAND-009 Promoted to ADR; one Informative. Non-blocking: no open Candidate proposes a Core change this Release would pre-empt.

**Critical Documentation Debt:** None critical. FW-007 (a correctly-scoped next Release not yet cut) is discharged by this Release and closed on 12 September 2026. FW-006 (the external Publication Engine exposes no commit marker) stays open and is disclosed in the Manifest entry.

**Known Deferred Content:** `v1.1.0`, cut the same day from the same `docs/` tree, was tagged through the GitHub Release form outside this process: lightweight tag, no Manifest entry before tagging, Zenodo deposit rejected on the `CITATION.cff` license field. Recorded in the Manifest as Superseded; left in git history unmodified. This Release is a metadata-only patch over it: `.zenodo.json` added, `CITATION.cff` license narrowed to the specification text's `CC-BY-4.0`, annotated tag.

**Standard Evolution Methodology reviewed:** Yes. This Release changes no Core document. The two Governance decisions it carries (`CAND-014`, `CAND-015`) were recorded under the two-step discipline, with Core integration authorized separately. Independent Reference Cases toward Rule 2 still stand at zero, disclosed on the Evidence Register.

**Recommendation:** Approved for release.

**Status:** Released. GitHub Release `v1.1.1` published 2026-09-12T10:47:22Z; Zenodo version DOI `10.5281/zenodo.22724309`.

---

## Release: v1.2.0

**Date:** 16 September 2026

**Documentation Readiness:** Ready. All required checks green on the intended commit `e4a5a53` (required documents, Markdown structural lint, internal link integrity, publication-metadata consistency, REUSE 3.3, dependency review, DCO) and the weekly OpenSSF Scorecard run. The branch ruleset on `main` is active since 14 September 2026: every change from PR #4 to PR #16 reached `main` through a pull request under it, while the twelve commits of 12 to 14 September 2026 that precede it were pushed directly, before the ruleset existed. The Release body's bundle claims are checkable against the `Publication-Manifest.md` entry: Constitution 1.0.1, Core Vocabulary 0.1 (13 governed terms), Specification 0.2, commit named.

**Open Observations:** 71 recorded (AO-001 to AO-068 and OBS-001 to OBS-003): 7 Closed, 2 Open in part (AO-042, AO-062), 1 Escalated (AO-008, to `CAND-009`), 61 Open. None blocks a Release: each open item is a disclosed tension in the model, not a defect in a published rule, and the Architecture Freeze (`CAND-007`) keeps the Core stable while they wait for Reference Cases.

**Unresolved ADR Candidates:** CAND-004 (Open; each of its seven questions carries a v1.0 disposition) and CAND-008 (Open, Value Model) are the two open Candidates; 13 Decided, including CAND-009 promoted; CAND-003 promoted to ADR and integrated. Non-blocking: no open Candidate proposes a Core change this Release would pre-empt.

**Critical Documentation Debt:** None critical. GAP-002 closed on 16 September 2026. DEBT-DOC-001, GAP-001, FW-001, FW-002 and FW-005 carry not-required-for-v1.0 dispositions recorded in `Documentation-Debt.md`. FW-006 (the external Publication Engine exposes no commit marker) stays open and is disclosed in the Manifest entry.

**Known Deferred Content:** Layer 2 of `CAND-014` (the World Model document and the `AI/Knowledge/*` rewrite), gated behind the `CAND-007` pipeline; the Conformance Test Suite tooling and the `CAND-002` declaration Projection and CI validator, specified and not built; the `Memory/Evidence Overlay.md` reserved sections (FW-001). The Specification track label stays 0.2 in this Release; moving it to 1.0 is a separate decision.

**Standard Evolution Methodology reviewed:** Yes. This Release carries the six Backlog Epics of `Master-Architecture-Backlog.md` executed or dispositioned under `CAND-007` Section 3, with Decisions `CAND-001`, `CAND-002` and `CAND-016` and dispositions on `CAND-004` and `CAND-014`, each within its recorded scope. Core edits are transcription only: `Core/Terminology.md` restated as an index, one sentence in `Models/Relationship.md`, `Domains/Common/Domain.md` made Informative. No new Core concept entered; independent Reference Cases toward Rule 2 stand where `v1.1.1` left them.

**Recommendation:** Approved for release.

**Status:** Released. GitHub Release `v1.2.0` published 2026-09-16T18:04:46Z from the SSH-signed tag on `e4a5a53`, with the three signed assets verified from the public download; Zenodo version DOI `10.5281/zenodo.22807178`, record published 2026-09-17T07:02:57Z after the publication-day webhook deliveries failed on Zenodo's side and the release event was redelivered by hand.

---

## Release: v1.3.0

**Date:** 17 September 2026 (planned)

**Documentation Readiness:** Ready once the carrying pull request is merged: the nine chapters of the reading path recompiled as v1.0 against the canonical documents as of this date, each with a Revision History and a Source line naming what changed; a forward-traceability check of every chapter sentence against its sources was run on this date and every normative sentence is traceable; the publication-metadata check now expects Specification Version 1.0 in every chapter. The Release body's bundle claims are checkable against the `Publication-Manifest.md` entry: Constitution 1.0.1, Core Vocabulary 0.1 (13 governed terms), Specification 1.0.

**Open Observations:** 71 recorded (AO-001 to AO-068 and OBS-001 to OBS-003): 7 Closed, 2 Open in part (AO-042, AO-062), 2 Escalated (AO-005 to `CAND-008`, AO-008 to `CAND-009`), 60 Open. None blocks a Release: each open item is a disclosed tension in the model, not a defect in a published rule, and the Architecture Freeze (`CAND-007`) keeps the Core stable while they wait for Reference Cases.

**Unresolved ADR Candidates:** CAND-004 (Open; each question dispositioned for v1.0) and CAND-008 (Open, Value Model); 13 Decided, including CAND-009 promoted; CAND-003 promoted to ADR and integrated. Non-blocking: no open Candidate proposes a Core change this Release would pre-empt.

**Critical Documentation Debt:** None critical. GAP-007 (documents without a Revision History table) is closed for the nine chapters by this Release and stays open for the six remaining documents; DEBT-DOC-001, GAP-001, FW-001, FW-002, FW-005 and FW-009 carry not-required-for-v1.0 dispositions; FW-006 stays open and is disclosed in the Manifest entry.

**Known Deferred Content:** Layer 2 of `CAND-014`; the Conformance Test Suite tooling (in progress, not part of this Release); the `CAND-002` declaration Projection and CI validator; the `Memory/Evidence Overlay.md` reserved sections (FW-001). The Committee Review Package remains the v0.2 review record; the v1.0 recompilation carries the Chief Architect's approval through this Release rather than a second committee review.

**Standard Evolution Methodology reviewed:** Yes. This Release changes no canonical document: the recompilation is editorial work on the Compiled tier, permitted by `CAND-007` Section 3 as EPIC-F currency work, and every sentence it carries traces to a canonical source as of this date. No new Core concept entered; independent Reference Cases toward Rule 2 stand where `v1.2.0` left them.

**Recommendation:** Approved for release; the Manifest entry names commit `8235b85`.

**Status:** Prepared. Tag and GitHub Release to follow; timestamp and Zenodo version DOI are added once they exist.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Log initialized with the v0.1 release entry |
| 0.1 | 22 July 2026 | Added Pre-Release Checklist, including Standard Evolution Methodology review |
| 0.1 | 12 September 2026 | Added the v1.1.1 release entry (first entry to run the Pre-Release Checklist), with the same-day v1.1.0 recorded under Known Deferred Content. |
| 0.1 | 12 September 2026 | v1.1.1 entry: Status Prepared to Released, with the GitHub Release timestamp and the Zenodo version DOI. |
| 0.1 | 16 September 2026 | Added the v1.2.0 release entry (Pre-Release Checklist run; the Part 8 bar of `Master-Architecture-Backlog.md` met on its recorded terms; Status Prepared). |
| 0.1 | 16 September 2026 | v1.2.0 entry: Status Prepared to Released, with the GitHub Release timestamp; Zenodo DOI pending. |
| 0.1 | 17 September 2026 | v1.2.0 entry: Zenodo version DOI `10.5281/zenodo.22807178` recorded. |
| 0.1 | 17 September 2026 | Added the v1.3.0 release entry (Specification reading path 1.0; Pre-Release Checklist run; Status Prepared). |
| 0.1 | 17 September 2026 | v1.3.0 entry: Recommendation confirmed once the Manifest Commit field was filled. |

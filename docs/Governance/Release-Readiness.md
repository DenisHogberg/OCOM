<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Release Readiness

[← Back](Knowledge-Map.md) · [↑ Up](README.md) · [Next →](Standard%20Evolution%20Methodology.md)

---
<!-- nav:end -->

# Release Readiness

**Document ID:** GOV-RELEASE-READINESS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 12 September 2026

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

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Log initialized with the v0.1 release entry |
| 0.1 | 22 July 2026 | Added Pre-Release Checklist, including Standard Evolution Methodology review |
| 0.1 | 12 September 2026 | Added the v1.1.1 release entry (first entry to run the Pre-Release Checklist), with the same-day v1.1.0 recorded under Known Deferred Content. |
| 0.1 | 12 September 2026 | v1.1.1 entry: Status Prepared to Released, with the GitHub Release timestamp and the Zenodo version DOI. |

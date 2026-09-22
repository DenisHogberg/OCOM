<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Evidence Register

[← Back](Publication-Model.md) · [↑ Up](README.md) · [Next →](Release-Workflow.md)

---
<!-- nav:end -->

# Evidence Register

**Document ID:** GOV-EVIDENCE-REGISTER-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 September 2026

---

# Purpose

This register separates what can be verified about the OCOM Specification's use from published
material, what its owner declares but cannot prove publicly, and what does not exist yet. It names
no organizations and asserts no endorsement. It is the record every claim of use is checked
against.

It was published on `ocom.uno` from 5 September 2026 until 19 September 2026, first as
`/implementation-status` and then as `/evidence-register`, and lived only there: the site held the
text and this repository held none of it. `CAND-022` moved it here, where it is versioned,
reviewed through the same pull-request process as the specification, and carried into every Zenodo
deposit and Software Heritage archive of a Release. The published URLs redirect to this document.

---

# The Evidence Ladder

Every statement about use is placed on a four-step scale. The specification does not claim a step
it has not reached.

| Step | What it means | Reached |
|------|----------------|---------|
| 1. Owner declaration | Stated by the specification's author; not publicly verifiable | Yes, current level |
| 2. Public case study | A named organization describes its own use in public | No |
| 3. Verified implementation | A published implementation checked against the conformance clauses of Chapter 08 | No |
| 4. Independent validation | Review or conformance testing by a party unrelated to the author | No |

**Highest level reached: Owner declaration.** The reason is structural rather than incidental: the
Governance roles (`Governance-Manifest.md`, Roles) denote responsibilities rather than separate
people, and at this stage the author holds all three, so no review of this specification has yet
been performed by a party with no interest in its success. External reviews of the published site
and the corpus have been performed and are recorded as Architecture Observations; they are reviews,
not validations in the sense of step 4, and this register does not count them as such.

---

# Verifiable Today

Published artifacts any reader can count and check, in this repository or on the site.

| What | Count | Note |
|------|-------|------|
| Core Vocabulary terms | 13 | each with an HTML page, a canonical JSON record, JSON-LD and Markdown |
| Specification chapters | 9 | SPEC-00 to SPEC-08, compiled from the canonical documents |
| Informative comparisons | 9 | |
| Reference Cases published | 1 | distilled from real rollouts under NDA, with the organization and details changed; non-normative |
| Architecture Observations | 82 | recorded tensions, AO-001 to AO-083, AO-072 reserved |
| Mandatory Statements enumerated | 182 of 335 | `Requirement-Register.md`, regenerated and checked on every build |
| Reference implementations published | 0 | |
| Public case studies | 0 | |
| Independent validations | 0 | in the sense of step 4 above |

---

# Public Records Held by Third Parties

Records that exist outside this repository and the site, each checkable at its source. Every row is
a fact with a date; none is an assessment.

| Fact | Date | Source |
|------|------|--------|
| REUSE 3.3 compliant, 426 of 426 files | 2026-09-19 | `api.reuse.software/info/github.com/DenisHogberg/OCOM` |
| OpenSSF Scorecard published weekly | 2026-09-11 | `scorecard.dev/viewer/?uri=github.com/DenisHogberg/OCOM` |
| OpenSSF Best Practices, passing level | 2026-09-11 | `bestpractices.dev/projects/14573` |
| Release v1.3.0 published from an SSH-signed tag with three signed assets; Specification reading path 1.0 | 2026-09-17 | `github.com/DenisHogberg/OCOM/releases/tag/v1.3.0` |
| Release v1.3.0 archived in Zenodo, resource type Standard | 2026-09-17 | `doi.org/10.5281/zenodo.22809694` |
| Release v1.3.0 and the repository archived in Software Heritage, release SWHID `swh:1:rel:f4482014c65a6fe05e865c9f68b70c6cbae76b00` | 2026-09-17 | `archive.softwareheritage.org` |
| Release v1.4.0 published from an SSH-signed tag with three signed assets; the Memory tier, the Package 3 Decisions and the Conformance Test Suite tooling | 2026-09-22 | `github.com/DenisHogberg/OCOM/releases/tag/v1.4.0` |
| Release v1.4.0 archived in Zenodo, resource type Standard | 2026-09-22 | `doi.org/10.5281/zenodo.22900969` |
| Release v1.2.0 published from an SSH-signed tag with three signed assets | 2026-09-16 | `github.com/DenisHogberg/OCOM/releases/tag/v1.2.0` |
| Release v1.2.0 archived in Zenodo, resource type Standard | 2026-09-17 | `doi.org/10.5281/zenodo.22807178` |
| Release v1.2.0 and the repository archived in Software Heritage, release SWHID `swh:1:rel:78eb36465ed18b3bf8f2d0948712537a7a51ae89` | 2026-09-17 | `archive.softwareheritage.org` |
| Release v1.1.1 archived in Zenodo, resource type Standard | 2026-09-12 | `doi.org/10.5281/zenodo.22724309` |
| Wikidata item Q141439683 | 2026-09-12 | `wikidata.org` |
| OpenAIRE record | 2026-09-12 | `explore.openaire.eu` |
| OpenAlex work W7170189420, concept DOI | 2026-09-12 | `openalex.org` |
| Listed in MERLOT as Reference Material (Business / Management), CC BY 4.0, material 824240210 | 2026-09-17 | `merlot.org` |

---

# Declared, Not Verifiable

Owner declarations. They cannot be checked from public material and should be weighed with the
author's interest in view.

**Production use.** The specification's principles are applied in production settings under NDA.
Those rollouts cannot become public case studies from the author's side, which is why public
evidence has to come from independent implementations.

---

# What Would Change This

A public case study requires a named organization willing to describe its own use. A verified
implementation requires software checked against Chapter 08's conformance clauses, which
`Conformance-Test-Suite.md` and `Requirement-Register.md` now make mechanically possible. An
independent validation requires a reviewer with no interest in the outcome. None of the three can
be produced by the author, and this register exists so that the absence is stated rather than
implied.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 19 September 2026 | Moved into the repository from `ocom.uno/evidence-register`, where it had been published since 5 September 2026 with no source here, per `CAND-022`. Counts brought current: 82 Architecture Observations, REUSE 426 of 426. The enumerated mandatory Statements and the reason the ladder stands at step 1 are stated here for the first time; the published page carried neither. |
| 0.1 | 22 September 2026 | Two rows added for Release v1.4.0 (the signed release and its Zenodo DOI). The register was one release behind `publication/llms.txt`, which `CAND-022` makes it the record of; found by the all-packages test of 22 September 2026. No Software Heritage row: the v1.4.0 tag is not archived there yet. |

# Changelog

## v1.2.0 (16 September 2026)

- Content Release over v1.1.1, cut from commit e4a5a53. Same version tracks (Constitution 1.0.1, Core Vocabulary 0.1 with 13 governed terms, Specification 0.2); the `docs/` tree changes across Governance, Core, Models, Domains, Entities, AI, Language, Adoption, Examples and the Specification reading path.
- `docs/Governance/Master-Architecture-Backlog.md` Part 8, "OCOM Specification v1.0 Ready", is met on the terms recorded there: EPIC-D (Terminology 0.2 as a verbatim index of canonical definitions, GAP-002 closed), EPIC-C (CAND-001 decided and integrated, Domains Memory disposition, every Entity document bridged to Memory), EPIC-B (CAND-016: `Meta/Relationship.md` canonical, `Models/Relationship.md` its specialization; AO-002 closed; CAND-004 dispositioned per question; CAND-015 integrated), EPIC-F (reading path re-pointed to the Constitution, Chapter 4 gains Organization, CAND-002 integrated), EPIC-E (CAND-002 decided; `docs/Governance/Conformance-Test-Suite.md` specifies the Requirement Register as a derived projection, 335 Statements, and five Test kinds) and EPIC-A dispositioned (Layer 1 closes it for v1.0; the World Model document stays gated). The Specification track label stays 0.2.
- Governance registers: AO-062 to AO-068 recorded; AO-001, AO-002, AO-065, AO-066 and OBS-001 closed; AO-042 and AO-062 Open in part; an Entry Lifecycle for observations. Two new Governance documents: `Concept-Paper-Profile-Conformance.md` and `Conformance-Test-Suite.md`.
- Security and project baseline since v1.1.1: `SECURITY.md`, `GOVERNANCE.md` and `CONTRIBUTING.md` per the OpenSSF Baseline; `main` is pull-request-only under a branch ruleset with seven required checks; DCO sign-off and dependency review on every pull request; SSH-signed tags and signed release assets from 13 September 2026. This is the first Release cut with a signed tag and the three signed assets (`OCOM-v1.2.0.zip`, `SHA256SUMS`, `SHA256SUMS.sig`); verification commands are in `SECURITY.md`.
- Zenodo version DOI: added by a follow-up revision once the deposit is published.

## v1.1.1 (12 September 2026)

- Metadata-only patch over v1.1.0. Adds `.zenodo.json` so the Zenodo GitHub integration deposits each Release with the intended metadata (resource type Standard, CC-BY-4.0, ORCID-bound author, subjects, description from the Release body). Narrows the `CITATION.cff` license to the specification text's CC-BY-4.0: Zenodo's citation reader accepts that field only as a single value, and a CFF list means "either licence", which misstates the repository's scoped dual licensing.
- First Release cut per `docs/Governance/Release-Workflow.md`: Manifest entry recorded before tagging, annotated tag. The `docs/` tree is byte-identical to v1.1.0.
- Zenodo version DOI: `10.5281/zenodo.22724309` (concept DOI `10.5281/zenodo.21510450` resolves to it as the latest version).

## v1.1.0 (12 September 2026)

- First Release whose name matches its scope: Constitution 1.0.1, Core Vocabulary 0.1 (13 governed terms), Specification 0.2, the Governance layer (CAND-001 to CAND-015, AO-001 to AO-061), one Reference Case, REUSE compliance, OpenSSF Scorecard and Best Practices, security policy, code of conduct, issue and pull request templates, `CITATION.cff`.
- Superseded by v1.1.1 for citation: the Zenodo deposit for this tag was rejected on the `CITATION.cff` license field, so it carries no version DOI. Tag and release left as published.

## v1.0.0 (23 July 2026)

- First tagged GitHub Release, cut from commit f7a33e2 (22 July 2026) with a lightweight tag. As published it contains the Core Vocabulary 0.1 as it stood then (12 governed terms; Organization was added on 25 July 2026 under CAND-005) and the Specification 0.2 reading path, together with every other tier in `docs/` at that date: Core, Meta, Models, Memory, Lifecycles, Language, AI, Governance, Domains, Entities, Examples, Workflows and Reference Architecture.
- It predates Constitution v1.0 (adopted 26 July 2026) and the Architecture Freeze (CAND-007, 27 July 2026), which is why `docs/Governance/Publication-Manifest.md` records it as Historical: the name does not match the scope. Superseded for citation by v1.1.1.
- Archived in Zenodo as version DOI `10.5281/zenodo.21510451`, resource type Software, under concept DOI `10.5281/zenodo.21510450`.
- No security-relevant changes: the repository was documentation only and carried no CI workflows at that commit. Retitled on 6 September 2026 from "Operational Model" to "Operating Model"; tag, commit and timestamps unchanged.

## v0.1.0

- Initial repository
- Core documentation
- OCOM specification started

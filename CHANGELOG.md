# Changelog

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

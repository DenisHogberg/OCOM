# Changelog

## Unreleased

- Suite, after the acceptance evaluation of 22 September 2026: identity uniqueness and reuse are keyed by the scope and system the Representation Map declares (per type or per collection path), so two systems' keys coexist as `CAND-026` promised; a bare reference to an identity present in two scopes is reported ambiguous; the derived schema makes collections optional and requires a property only where at least two example records carry it. `AO-086` to `AO-088` recorded from the same evaluation. `README.md` no longer says the repository holds no code.
- `CAND-025` (Decided 22 September 2026): accountability is singular and responsibility is plural. One sentence each in `Models/Entity.md` (Ownership) and `Meta/Ownership.md` (Shared Ownership); the Presence Test counts one where a Statement says one, so `REQ-MODELS-ENTITY-004` fails on a second owner; `AO-015` Closed in part.
- `CAND-026` (Decided 22 September 2026): the specification prescribes no format and publishes one Reference Serialization as Informative Adoption material, `docs/Adoption/Reference Serialization.md` (site page `/adoption/reference-serialization`), with `docs/Examples/Conformance/schema.json` derived by `tools/conformance/reference_schema.py` and checked in CI, and the declaration rule for identity scope: the Representation Map's `Identity.scope` row decides `REQ-META-IDENTITY-005`, a Declaration Test.
- `CAND-027` (Decided 22 September 2026): legal form is Organization (Classification; Composition between Organizations) and internal structure is the Department Entity. `Entities/Department/Department.md` replaces the stub Employee and Team already required; one paragraph in `Meta/Organization.md`; one in `Adoption/First Pilot.md`; `CAND-004` postscript for questions 1 and 2.
- `AO-085` closed as a postscript to `CAND-024`: `Memory/Retention.md`'s erasure record names a Policy the organization has declared and the actor who issued it, and an implementation refuses one that names neither; the suite grants the Integrity exclusion only to such a record and reports every erasure record.
- Memory tier, per `CAND-023` and `CAND-024` (both Decided 21 September 2026 as `CAND-007` Section 5 Freeze exceptions, on Reference Case `RC-012`): `Memory/Evidence Overlay.md` carries the Definition, Source, Reliability, Independence and Conformance sections reserved since 21 July 2026; `Memory/Memory Record.md` and `Memory/Evidence Overlay.md` require an implementation to be able to demonstrate that a record is unaltered, naming no mechanism; `Memory/Memory Record.md` defines Audit Record by reference; `Memory/Retention.md`'s Deleted state is an erasure that preserves the record. `Governance/Conformance-Test-Suite.md` gains the Integrity Test kind. Constitution 1.0.1 and Core Vocabulary 0.1 unchanged; `AO-069`, `AO-075`, `AO-084` and `FW-001` closed.

## v1.3.0 (17 September 2026)

- Specification reading path 1.0: the nine chapters of `docs/Specification/` recompiled against the canonical documents as they stand on 17 September 2026. Chapter 1 now carries `Core/Manifest.md`'s sections verbatim, including the whole Normative Language section; Chapters 3 and 4 add Organization to the specializations of Object; Chapter 5 compiles the `CAND-016` specialization sentence and replaces an unsourced sentence about Domains with `Models/Domain.md`'s governance rules; Chapter 6 is restated from `Models/Lifecycle.md`, `Models/State.md`, `Lifecycles/Lifecycles.md`, `Models/Entity.md`, `Models/Domain.md` and `Models/Event.md` and no longer calls the Domains and Entities sections non-normative; Chapter 8's Purpose follows `Language/Conformance.md`; every chapter gains a Revision History and a Last Updated field (GAP-007 closed for the chapters). Constitution 1.0.1 and Core Vocabulary 0.1 unchanged.
- `Specification/Committee Review Package.md` keeps its v0.2 review record and Version, with a dated postscript; the CI version check skips it by name (`CI-DESIGN.md`).
- Root `README.md` badge and text, `docs/README.md`, `PROJECT_STATUS.md` and `Governance/Publication-Model.md` name Specification 1.0.
- GitHub Release published 2026-09-17T09:27:34Z from the SSH-signed tag on 8235b85 with the three signed assets. Zenodo version DOI: `10.5281/zenodo.22809694` (concept DOI `10.5281/zenodo.21510450` resolves to it as the latest version), record published 2026-09-17T09:27:43Z by the GitHub integration on the release event.

## v1.2.0 (16 September 2026)

- Content Release over v1.1.1, cut from commit e4a5a53. Same version tracks (Constitution 1.0.1, Core Vocabulary 0.1 with 13 governed terms, Specification 0.2); the `docs/` tree changes across Governance, Core, Models, Domains, Entities, AI, Language, Adoption, Examples and the Specification reading path.
- `docs/Governance/Master-Architecture-Backlog.md` Part 8, "OCOM Specification v1.0 Ready", is met on the terms recorded there: EPIC-D (Terminology 0.2 as a verbatim index of canonical definitions, GAP-002 closed), EPIC-C (CAND-001 decided and integrated, Domains Memory disposition, every Entity document bridged to Memory), EPIC-B (CAND-016: `Meta/Relationship.md` canonical, `Models/Relationship.md` its specialization; AO-002 closed; CAND-004 dispositioned per question; CAND-015 integrated), EPIC-F (reading path re-pointed to the Constitution, Chapter 4 gains Organization, CAND-002 integrated), EPIC-E (CAND-002 decided; `docs/Governance/Conformance-Test-Suite.md` specifies the Requirement Register as a derived projection, 335 Statements, and five Test kinds) and EPIC-A dispositioned (Layer 1 closes it for v1.0; the World Model document stays gated). The Specification track label stays 0.2.
- Governance registers: AO-062 to AO-068 recorded; AO-001, AO-002, AO-065, AO-066 and OBS-001 closed; AO-042 and AO-062 Open in part; an Entry Lifecycle for observations. Two new Governance documents: `Concept-Paper-Profile-Conformance.md` and `Conformance-Test-Suite.md`.
- Security and project baseline since v1.1.1: `SECURITY.md`, `GOVERNANCE.md` and `CONTRIBUTING.md` per the OpenSSF Baseline; `main` is pull-request-only under a branch ruleset with seven required checks; DCO sign-off and dependency review on every pull request; SSH-signed tags and signed release assets from 13 September 2026. This is the first Release cut with a signed tag and the three signed assets (`OCOM-v1.2.0.zip`, `SHA256SUMS`, `SHA256SUMS.sig`); verification commands are in `SECURITY.md`.
- GitHub Release published 2026-09-16T18:04:46Z. Zenodo version DOI: `10.5281/zenodo.22807178` (concept DOI `10.5281/zenodo.21510450` resolves to it as the latest version), record published 17 September 2026 after the publication-day webhook deliveries failed on Zenodo's side and the release event was redelivered by hand.

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

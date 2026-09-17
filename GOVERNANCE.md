# Governance

How this project makes decisions, who holds which role, and what happens if the maintainer is unavailable. The full governance framework lives in `docs/Governance/`; this page is the short version for people who arrive from the repository front page.

## How decisions are made

The core of the specification (Core Vocabulary terms, Canonical Principles, the Constitution) is frozen under ADR CAND-007. It changes only through the Standard Evolution Methodology: a Reference Case first, an Architecture Observation if the case shows a tension, an ADR Candidate if the observation is corroborated, and a decision after that. Editorial changes go through pull requests and the checks described in CONTRIBUTING.md.

- [Governance Manifest](docs/Governance/Governance-Manifest.md): principles and roles.
- [Standard Evolution Methodology](docs/Governance/Standard%20Evolution%20Methodology.md): how the core may change.
- [Architecture Observations](docs/Governance/Architecture-Observations.md) and [ADR Candidates](docs/Governance/ADR-Candidates.md): the open registers.

## Roles and who holds them

| Role | Responsibility | Held by |
|---|---|---|
| Chief Architect | decides: resolves Architecture Observations, accepts or rejects ADR Candidates, owns the Architect Response | Denis Petrenko |
| CDKO (Chief Documentation and Knowledge Officer) | records: maintains the governance registers, logs observations and documentation debt, does not resolve them | Denis Petrenko |
| Architecture Committee | reviews: approves baselines and releases | Denis Petrenko, acting alone at the current stage |
| Maintainer | merges, tags and archives releases, answers security reports | Denis Petrenko |
| Access to sensitive resources | holds the credentials for repository administration, the publication server, the domain registrar and the archive accounts (Zenodo, Software Heritage) | Denis Petrenko |

All roles are held by one person today. That is stated rather than hidden, and the next section exists because of it.

## Continuity

If the maintainer is unavailable for more than a week, the project can continue because:

1. The text is archived outside GitHub: each release Zenodo accepted under DOI 10.5281/zenodo.21510450, which today is v1.0.0, v1.1.1 and v1.2.0, and the repository in Software Heritage (origin `https://github.com/DenisHogberg/OCOM`; the snapshot of 17 September 2026 holds release `v1.2.0` as `swh:1:rel:78eb36465ed18b3bf8f2d0948712537a7a51ae89`). The deposit for v1.1.0 was rejected and that release carries no DOI, as `docs/Governance/Publication-Manifest.md` records. Both are readable and forkable without any account of the maintainer.
2. GitHub's Successor settings let the maintainer name a person who, after GitHub verifies the maintainer's death, can archive or transfer the public repositories. No successor is designated today, deliberately: naming one is a decision about a specific person, and the other three arrangements below do not depend on it. When a successor is named, the designation is recorded in the revision history of this page.
3. The maintainer keeps a sealed handover note for the successor, separate from the repository, covering the domain registrar, the hosting account, the Zenodo account and the ORCID record.
4. The licences (CC BY 4.0 for the text, Apache 2.0 for the repository) let anyone continue the work from the archives even if no handover happens.

## Access policy

No collaborator holds write access today. Before anyone is granted write, maintainer or administrative access, the maintainer reviews their contribution history on this repository (at least three merged pull requests) and their public identity, and records the grant in the revision history of this page. Access is granted at the lowest level that fits the task and is reviewed at each release. Two-factor authentication is enforced by GitHub for all collaborators.

## Contact

Security issues go through [SECURITY.md](SECURITY.md). Everything else goes through GitHub Issues, using the templates in `.github/ISSUE_TEMPLATE/`.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1 | 13 September 2026 | First version: decision path, roles and holders, continuity arrangement. |
| 0.1 | 13 September 2026 | Added the Access policy section and the sensitive-resources row in the roles table (OpenSSF Baseline OSPS-AC-01.01, OSPS-GV-01.01). |
| 0.1 | 14 September 2026 | Continuity item 2 restated: no successor is designated today, and the page says so instead of describing the designation as a standing arrangement. |
| 0.1 | 15 September 2026 | Continuity item 1 corrected: Zenodo holds the releases it accepted, v1.0.0 and v1.1.1, not every release; v1.1.0's deposit was rejected and it carries no DOI. |
| 0.1 | 17 September 2026 | Continuity item 1 updated: Zenodo now also holds v1.2.0; the Software Heritage archive is named by origin and by the SWHID of release v1.2.0, taken from the snapshot of 17 September 2026. |

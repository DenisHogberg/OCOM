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

All roles are held by one person today. That is stated rather than hidden, and the next section exists because of it.

## Continuity

If the maintainer is unavailable for more than a week, the project can continue because:

1. The text is archived outside GitHub: every release in Zenodo under DOI 10.5281/zenodo.21510450, and the repository in Software Heritage. Both are readable and forkable without any account of the maintainer.
2. The maintainer designates a successor in GitHub's account settings (Successor settings). GitHub lets that person archive or transfer the public repositories after verification. The designation is recorded in the revision history of this page when it is made.
3. The maintainer keeps a sealed handover note for the successor, separate from the repository, covering the domain registrar, the hosting account, the Zenodo account and the ORCID record.
4. The licences (CC BY 4.0 for the text, Apache 2.0 for the repository) let anyone continue the work from the archives even if no handover happens.

## Contact

Security issues go through [SECURITY.md](SECURITY.md). Everything else goes through GitHub Issues, using the templates in `.github/ISSUE_TEMPLATE/`.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1 | 13 September 2026 | First version: decision path, roles and holders, continuity arrangement. |

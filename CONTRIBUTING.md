# Contributing

Contributions are welcome. This file says how the repository takes them.

## What this repository is

OCOM is a specification, not software. The repository holds the canonical Markdown of the specification and the governance records around it. The site at ocom.uno is rendered from these files by a separate publication engine. There is no code to build and nothing to install.

## Before you change a normative document

The core is frozen (ADR CAND-007). Core Vocabulary terms, Canonical Principles and the Constitution are not changed by pull request. The path is the one in [Standard Evolution Methodology](docs/Governance/Standard%20Evolution%20Methodology.md): a Reference Case first, an Architecture Observation if the case shows a tension, an ADR Candidate if the observation is corroborated, and only then a change to the text.

Start with an issue, not a pull request:

- [Reference Case](.github/ISSUE_TEMPLATE/reference-case.md): a real situation where the specification did not hold, or held in a way worth recording.
- [Architecture Observation](.github/ISSUE_TEMPLATE/architecture-observation.md): two published rules conflict, or a rule cannot be applied as written.
- [Projection defect](.github/ISSUE_TEMPLATE/projection-defect.md): a page or machine record on ocom.uno disagrees with its canonical source.

Editorial corrections (typos, broken links, formatting) can go straight to a pull request.

## Pull requests

Discuss major architectural changes before opening one. The pull request template asks what changed and why; link the Reference Case, Architecture Observation or ADR Candidate behind the change. Each changed document gets a new row in its revision history and a moved "Last Updated" field, per [Documentation Standards](docs/Governance/Documentation-Standards.md).

## Checks

Every push and pull request runs the checks in `.github/workflows/ci.yml`: markdownlint over every Markdown file, lychee over every link, a publication-metadata job that keeps the Publication Manifest, the Specification version fields and the Status fields consistent with each other, and reuse lint over the licensing map. A failing check blocks the merge. [CI-DESIGN.md](CI-DESIGN.md) explains why each check exists and how to run the same checks locally. Every pull request runs the full check set before it can be merged; once the branch ruleset on `main` is active, it lists these checks as required.

Two rules follow from that:

- A change must pass all checks before it is merged. Do not disable a rule to get past a failure. If a rule is wrong for this repository, say so in the pull request with the evidence, the way the existing exceptions in `.markdownlint-cli2.jsonc` do.
- When a change introduces a rule that can be checked mechanically, the check comes in the same change. The publication-metadata job landed with the publication controls it verifies; the licensing map landed with the job that lints it.

## Anonymity

Do not name real organizations, clients, products or people anywhere in the repository. Describe a context so that it can be understood, not identified. This holds for Reference Cases, examples and commit messages alike.

## Licensing

Everything under `docs/` is CC BY 4.0 and everything else is Apache 2.0; the map is `REUSE.toml`. By contributing you agree that your contribution is licensed the same way as the files it changes.

## Sign-off

Contributions are accepted under the [Developer Certificate of Origin, version 1.1](https://developercertificate.org/). Sign off every commit with `git commit -s`, which adds a `Signed-off-by` line with your name and email address and states that you have the right to submit the work under the project's licences. Pull requests with unsigned commits will be asked to add the sign-off.

## Conduct and security

The [Code of Conduct](CODE_OF_CONDUCT.md) applies. Security issues go through [SECURITY.md](SECURITY.md), not the issue tracker.

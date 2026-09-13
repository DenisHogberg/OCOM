# CI Design Notes

Why `.github/workflows/ci.yml` looks the way it does — for anyone
extending it later, so decisions don't have to be re-derived from
scratch or, worse, guessed.

## What this repository actually is

401 Markdown files and zero code (September 2026). Outside Markdown
the repository holds only its own configuration and metadata, each
validated by the tool that consumes it: the workflows and Dependabot
file under `.github/`, `.markdownlint-cli2.jsonc`, `REUSE.toml`,
`CITATION.cff`, `.zenodo.json` (the deposit metadata Zenodo reads on
every Release), the licence texts and a few images. One Mermaid block
(`docs/Governance/Concept-Paper-Value-Model.md`) and external links in
eight documents, mostly the entry pages (all verified directly, not
assumed). Every check below exists because it checks something this
repository actually contains — none were copied from a generic
template.

The counts in this section are from the July 2026 design pass. The
repository has since grown to about 400 Markdown files, gained a
licensing map and picked up external links in README and the
governance records, which the link check covers too. The shape has not
changed: Markdown and its metadata, no code.

Two rules follow, and together they are the repository's test policy.
First, a check is added only when it verifies something that actually
exists here. Second, when a change introduces a rule that can be
checked mechanically, the check lands in the same change: the
`publication-metadata` job arrived in the commit that finalized the
publication controls it verifies (b564bf5, 21 August 2026), and
`reuse-compliance` arrived together with `REUSE.toml` (cebd793,
11 September 2026). CONTRIBUTING.md states both rules for
contributors.

## The five jobs

**`required-documents`** — confirms LICENSE, README, CONTRIBUTING,
CHANGELOG, ROADMAP, this file, and `docs/README.md` /
`docs/PROJECT_STATUS.md` still exist. Cheap, and the only one of the
five that would catch an accidental deletion — nothing else would.

**`markdown-lint`** — structural Markdown checks via markdownlint,
using `.markdownlint-cli2.jsonc`. Several default rules are disabled
there, each because it conflicts with an established, verified
repository convention (flat `#`-level sections instead of nested
headings, a `<!-- nav:start -->` HTML-comment block before every
title, 62 legitimately language-less fenced code blocks, and at least
three files with intentional duplicate heading text). See the config
file's own comments for the specifics — a default-configured
markdownlint would fail on the majority of existing files.

**`link-check`** — internal link integrity via lychee. This is the
highest-value check in this repository specifically: 359 of 373 files
depend on the nav-block convention (`[← Back]` / `[↑ Up]` /
`[Next →]`), and broken relative links from a renamed or moved file
have been a real, repeated, hand-caught problem in this project's own
history. `--include-fragments` is deliberately *not* enabled: no real
`file.md#anchor`-style links exist today (cross-references of that
shape are written as backtick-quoted text, which isn't a Markdown link
and isn't something lychee — or any link checker — can see), so the
flag would add a real risk (GitHub's and lychee's anchor-slug rules
can diverge) for zero current benefit.

One host is excluded from the link check: `doi.org`. It is a resolver
this project does not control, and it fails in bursts (13 September
2026: six consecutive probes, 30 s each, all 504, while the Zenodo
record behind the DOI was reachable). The DOI value is checked where it
can be checked deterministically, by keeping `.zenodo.json`,
`CITATION.cff` and the Publication Manifest in agreement, and its
resolution is confirmed by hand at each release. Excluding it keeps a
third-party outage from turning `main` red; no other host is excluded.

**`publication-metadata`** (added 21 August 2026) keeps the
repository's own publication metadata consistent with itself, per
`docs/Governance/Publication-Model.md` and `Release-Workflow.md`.
Three blocking steps and one advisory. Every commit named in
`docs/Governance/Publication-Manifest.md` must exist in this
repository's history. The manifest's current Specification Version
must match the `**Version:**` field of every file in
`docs/Specification/`. `docs/Entities/Overview.md` must keep Status
Draft, because its content stayed normative after Constitution
Decision 4 moved Entities out of Core scope. The advisory step is a
grep heuristic that warns about SHALL sentences naming a capitalized
term with no matching file under Meta, Models, AI, Core, Memory or
Lifecycles; it never fails the build, because it cannot tell a
dangling reference from an ordinary capitalized word. The job checks
this repository only. It cannot see whether ocom.uno matches the
repository, because the publication engine that renders the site lives
outside it.

**`reuse-compliance`** (added 11 September 2026) is described in its
own section below.

## Deliberately not included, and why

- **YAML / JSON / Mermaid validation** — the YAML and JSON that exist
  are configuration and metadata whose consumers already validate them:
  GitHub parses the workflows and `dependabot.yml` on every run and
  reads `CITATION.cff` for its citation widget; Zenodo validates
  `.zenodo.json` on every Release and fails the deposit visibly when a
  file is wrong, as `v1.1.0` showed for `CITATION.cff`. The one Mermaid
  block is illustrative. A second check here would duplicate those, not
  add safety margin.
- **A hard requirement that every document carry `**Document ID:**`**
  — not a universal convention: only 25 of 51 files in `Entities/`
  have it. Enforcing it today would fail on legitimate, existing
  content, not on a real problem.
- **Nav-chain consistency** (alphabetical Back/Up/Next ordering) —
  real and repository-specific, but no existing tool checks it; it
  would need bespoke, unreviewed script code. Deliberately deferred
  rather than rushed into a first CI pass.
- **Spell-checking / prose linting** — would need a curated
  domain-term dictionary (OCOM, OCOMObject, entity names, ...) first,
  or it produces noise, not signal.
- **A build matrix** — nothing in this repository varies by OS,
  runtime, or version the way code would; there is no dimension to
  matrix across.

## Action pinning policy

Risk-tiered, not blanket. `actions/checkout` is official, GitHub-owned,
and among the most-scrutinized actions in the entire ecosystem — kept
on its major-version tag (`@v7` today; Dependabot moves it). `DavidAnson/markdownlint-cli2-action`
and `lycheeverse/lychee-action` are third-party, single-maintainer
projects — each pinned to the exact commit SHA behind its tag at the
time it was added, verified directly against the GitHub API
(`git/refs/tags/...`) before pinning, never guessed. This also has a
second, independent benefit beyond supply-chain safety: it makes CI
runs on the same commit actually reproducible — a floating major tag
can silently pick up a new patch release between two runs and change
behavior on an unchanged commit; a pinned SHA cannot.

Dependabot (`.github/dependabot.yml`) proposes version bumps as a
reviewable PR — each one is a chance to re-verify the new SHA before
accepting it, not an argument against pinning in the first place.

## Known residual risk

markdownlint was configured from direct inspection of this
repository's conventions, not from an actual local run (no Node.js
runtime was available in the environment this was designed in). The
rules disabled above were chosen because they were positively
confirmed to conflict with real, existing content — not because a
clean run was observed. The first real CI run against this workflow
is the actual verification; if a rule not covered here turns out to
false-positive, disable it the same way, with the same evidence-first
reasoning, not by disabling `default: true` wholesale.

That first run and every run since have passed, so the configuration
is now verified by use, not only by inspection.

## Running the checks locally

The same tools, the same arguments, from the repository root:

```
npx markdownlint-cli2
lychee --no-progress --timeout 45 --max-retries 3 --exclude-path '\.github' '**/*.md'
python3 -m reuse lint
```

markdownlint-cli2 finds `.markdownlint-cli2.jsonc` on its own; the
globs in that file decide what is linted. The `publication-metadata`
steps are plain shell in `ci.yml`; copy a step's `run:` block into a
terminal at the repository root and it behaves the same, given a full
clone (the commit check needs history, hence `fetch-depth: 0` in CI).

## Licensing check (added 11 September 2026)

`reuse-compliance` runs `reuse lint` (fsfe/reuse-action, pinned to the
commit behind v5.0.0: `bb774aa9`). The repository carries two licences
and the split was previously stated only in prose in README.md.
`REUSE.toml` states it as data: everything is Apache-2.0, everything
under `docs/` is CC-BY-4.0, and `CODE_OF_CONDUCT.md` is credited to the
Contributor Covenant authors as well. Full licence texts live in
`LICENSES/` under their SPDX identifiers. The job fails if any file
stops resolving to a holder and a licence. This is the same discipline
the specification asks of an operating record, applied to the
repository's own licensing.

## Scorecard (added 11 September 2026)

`.github/workflows/scorecard.yml` runs OpenSSF Scorecard
(ossf/scorecard-action, pinned to the commit behind v2.4.4: `2d114668`)
on every push to `main` and weekly, and publishes the result so the
README badge shows a real number. It is a separate workflow because
publishing needs `id-token: write`, which CI deliberately does not
have. Checks about binaries, fuzzing, SAST, packaging and signed
releases do not apply to a Markdown repository and will score N/A or
low; the number is reported as it is.

# CI Design Notes

Why `.github/workflows/ci.yml` looks the way it does — for anyone
extending it later, so decisions don't have to be re-derived from
scratch or, worse, guessed.

## What this repository actually is

373 Markdown files, zero code, zero JSON/YAML, zero Mermaid, zero
external links (all verified directly, not assumed). Every check
below exists because it checks something this repository actually
contains — none were copied from a generic template.

## The three jobs

**`required-documents`** — confirms LICENSE, README, CONTRIBUTING,
CHANGELOG, ROADMAP, this file, and `docs/README.md` /
`docs/PROJECT_STATUS.md` still exist. Cheap, and the only one of the
three that would catch an accidental deletion — nothing else would.

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

## Deliberately not included, and why

- **YAML / JSON / Mermaid validation** — none of these exist anywhere
  in the repository. A check with nothing to check is dead weight, not
  safety margin.
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
on its major-version tag (`@v4`). `DavidAnson/markdownlint-cli2-action`
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

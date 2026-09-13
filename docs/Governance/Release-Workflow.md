<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Release Workflow

[← Back](Publication-Manifest.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Release Workflow

**Document ID:** GOV-RELEASE-WORKFLOW-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 13 September 2026

---

# Purpose

The normative flow from a document change to a verified public release, stated once, so that "how does a change become part of an authoritative release" has one answer instead of being reconstructed ad hoc each time. Every role named below already exists (Chief Architect, CDKO, CI) — this document introduces no new role. It is a `Governance/` process document per `Documentation-Standards.md`'s Status Taxonomy, and it does introduce one new procedural convention not established elsewhere: Step 6's annotated-tag requirement, stated there explicitly rather than left implicit.

---

# The Flow

```text
Document change
    ↓
Governance decision
    ↓
Version assignment
    ↓
Commit
    ↓
Validation
    ↓
Tag
    ↓
GitHub Release
    ↓
Publication
    ↓
Machine-readable projections
    ↓
Verification
```

## 1. Document change

- **Source:** A Reference Case, an Architecture Observation, an existing ADR Candidate, or (for non-normative work — presentation, publication metadata, editorial correction) direct authoring.
- **Responsibility:** Whoever proposes the change; CDKO drafts.
- **Result:** A candidate edit to one or more canonical-source documents.
- **Done when:** The change is expressible as a diff against a specific file, with its basis stated (which Decision, which Observation, or "editorial, no architectural content").

## 2. Governance decision

- **Source:** `Standard Evolution Methodology.md`'s pipeline (Reference Case → Observation → Repeated Pattern → ADR Candidate → Chief Architect Decision) for anything architectural; none required for purely editorial/presentational change (this document's own creation required none).
- **Responsibility:** Chief Architect decides; CDKO records the Decision in `ADR-Candidates.md` or `Architecture-Observations.md`.
- **Result:** A recorded Decision (or an explicit "no decision needed, editorial" note).
- **Done when:** Anyone reading only the Governance record can see why the change is authorized, without reconstructing a conversation.

## 3. Version assignment

- **Source:** `Publication-Model.md`'s four-track model — determine which track(s) the change touches (Constitution / Core Vocabulary / Specification / none of these, i.e. purely a Governance-internal document).
- **Responsibility:** CDKO proposes the version bump per track; Chief Architect confirms for Constitution-track changes specifically (per Constitution's own amendment discipline).
- **Result:** An updated `Version:` field on the changed document(s), and, if the change is release-worthy, a note of which Release the change should eventually belong to.
- **Done when:** No document's `Version:` field is ambiguous about whether it reflects this change.

## 4. Commit

- **Source:** The reviewed diff from steps 1–3.
- **Responsibility:** Whoever has write access; per `CONTRIBUTING.md`, major architectural changes are discussed before a Pull Request.
- **Result:** A commit on `main` (or a reviewed PR merged to `main`).
- **Done when:** `git log` shows the change, with a message stating what changed and why (matching this repository's existing commit-message convention).

## 5. Validation

- **Source:** `.github/workflows/ci.yml` — `required-documents`, `markdown-lint`, `link-check`, and the publication-metadata job this workflow adds (see `Publication-Model.md`, "Known Gaps," for what this job can and cannot check).
- **Responsibility:** CI, automatically, on every push.
- **Result:** A pass/fail signal.
- **Done when:** All CI jobs pass on the commit intended for release. A failing validation blocks every step after this one.

## 6. Tag

- **Source:** A validated commit on `main`, plus a completed `Publication-Manifest.md` entry for the intended Release (all fields filled, no `TBD`).
- **Responsibility:** Chief Architect authorizes; CDKO executes (`git tag`).
- **Result:** An annotated git tag pointing at the exact commit the Manifest entry names. From 13 September 2026 the tag is also signed with the maintainer's SSH key, per `SECURITY.md`; the public key is published in `.github/allowed_signers`, and `git tag -v <tag>` verifies it. Tags cut before that date (`v1.0.0`, `v1.1.0`, `v1.1.1`) stay unsigned by policy and are not re-tagged.
- **Done when:** `git cat-file -t <tag>` confirms an annotated tag (not lightweight — a correction from `v1.0.0`'s own precedent, which was lightweight and untraceable to a decision), the tag's target commit matches the Manifest entry's `Commit` field exactly, and, for tags created from 13 September 2026, `git tag -v <tag>` reports a good signature.

## 7. GitHub Release

- **Source:** The tag from step 6.
- **Responsibility:** Chief Architect authorizes the release text; CDKO publishes it (`gh release create`).
- **Result:** A public GitHub Release whose body states, at minimum, what it contains (per the Manifest entry) and, if applicable, what it explicitly does not contain yet — the omission that caused `v1.0.0`'s own mislabeling.
- **Done when:** The Release body's claims are checkable against the Manifest entry with no reader-side inference required, and, for Releases cut from 13 September 2026, the three assets below are attached and both verification commands succeed.

### Release assets (from 13 September 2026)

GitHub's auto-generated "Source code" archives are not the artifact of record: they are rebuilt on request and carry no checksum. The CDKO builds the archive from the tag outside the working tree, writes its SHA-256 checksum, signs the checksum file with the maintainer's SSH key (the same key that signs the tag, published in `.github/allowed_signers`), and attaches the three files to the GitHub Release:

```text
cd "$(mktemp -d)"
git -C /path/to/OCOM archive --format=zip --prefix=OCOM-<tag>/ -o "$PWD/OCOM-<tag>.zip" <tag>
shasum -a 256 OCOM-<tag>.zip > SHA256SUMS
ssh-keygen -Y sign -f ~/.ssh/id_ed25519 -n file SHA256SUMS
```

Building outside the repository keeps the archive, the checksum file and the signature out of the working tree, which has no `.gitignore`. The last command writes the detached signature `SHA256SUMS.sig`. Anyone verifies the three assets with the public key from `main`, holding nothing but the downloaded files:

```text
curl -fsSLO https://raw.githubusercontent.com/DenisHogberg/OCOM/main/.github/allowed_signers
ssh-keygen -Y verify -f allowed_signers -I stremshop@gmail.com -n file -s SHA256SUMS.sig < SHA256SUMS
shasum -a 256 -c SHA256SUMS
```

The second command proves the checksum file was signed by the maintainer's key; the third proves the archive matches the checksum. Verification needs `.github/allowed_signers` to permit the `file` signature namespace as well as `git`, so that change must be on `main` at or before the tagged commit. The Manifest entry's `Published Artifacts` field names the three assets when it is completed, at step 8. `SECURITY.md`, "Verifying releases", repeats the verification commands for readers who start from the Release page.

## 8. Publication

- **Source:** The published Release.
- **Responsibility:** **External to this repository** — the Publication Engine that builds ocom.uno is confirmed to have no code, workflow, or configuration inside this repository (`Publication-Model.md`, "Known Gaps"). This step's actual execution is out of this repository's control.
- **Result:** The live site reflecting the released content.
- **Done when:** *(Not verifiable from this repository today.)* The contract this repository can state: the Manifest entry's `Publication Date` and `Published Artifacts` fields should be filled in once this step is confirmed complete, by whoever operates the Publication Engine.

## 9. Machine-readable projections

- **Source:** The published site (step 8).
- **Responsibility:** **External**, same as step 8 — JSON/JSON-LD generation happens on the Publication Engine, with no versioned source file in this repository to check it against.
- **Result:** HTML/JSON/JSON-LD/Markdown term-card projections, per `/changelog`'s own claim.
- **Done when:** *(Not verifiable from this repository today.)* Same limitation as step 8 — recorded in the Manifest's `Machine-readable Projections` field once known, not enforced here.

## 10. Verification

- **Source:** The completed Manifest entry plus a live check of the published artifacts (steps 8–9), where reachable.
- **Responsibility:** CDKO, as a post-release check; Chief Architect reviews.
- **Result:** Either confirmation that the six authoritative-version questions (`Publication-Model.md`) are all answerable and consistent for this Release, or a logged discrepancy.
- **Done when:** Someone with no prior context can start from the Release tag and answer all six questions in under a minute, per `Publication-Model.md`'s own bar — the exact test the original re-verification audit failed.

---

# What This Workflow Does Not Cover

- The internal editorial process for compiling `docs/Specification/*` from canonical sources — that is `EPIC-F`'s and `Publication-Model.md`'s concern, not a release-cadence question.
- Conformance testing of third-party implementations — `EPIC-E`, explicitly separate, untouched by this document.
- Any criteria for *when* a new Release should be cut — that remains `Master-Architecture-Backlog.md` Part 8 (Release Readiness)'s decision, not this document's.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 August 2026 | Initial workflow, ten steps, grounded in existing roles and the current CI. Steps 8–9 explicitly marked unverifiable from this repository. |
| 0.1 | 20 August 2026 | Corrected on independent review: Status changed Informative → Draft, consistent with this document being a `Governance/` process document per `Documentation-Standards.md`'s own Status Taxonomy; Purpose's "imposes no new requirement" claim removed, since Step 6's annotated-tag rule is in fact new and is now stated as such |
| 0.1 | 13 September 2026 | Step 6: release tags are SSH-signed from 13 September 2026 per `SECURITY.md` (signed-release policy, commit `d3c4e43`); earlier tags stay unsigned. |
| 0.1 | 13 September 2026 | Step 7: release assets (archive of record built with `git archive`, `SHA256SUMS`, detached SSH signature `SHA256SUMS.sig`) required from 13 September 2026, with the verification commands. `.github/allowed_signers` widened to the `file` namespace on the same date so the signature on `SHA256SUMS` can be verified. |

<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Release Workflow

[← Back](Publication-Manifest.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Release Workflow

**Document ID:** GOV-RELEASE-WORKFLOW-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 August 2026

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
- **Result:** An annotated git tag pointing at the exact commit the Manifest entry names.
- **Done when:** `git cat-file -t <tag>` confirms an annotated tag (not lightweight — a correction from `v1.0.0`'s own precedent, which was lightweight and untraceable to a decision), and the tag's target commit matches the Manifest entry's `Commit` field exactly.

## 7. GitHub Release

- **Source:** The tag from step 6.
- **Responsibility:** Chief Architect authorizes the release text; CDKO publishes it (`gh release create`).
- **Result:** A public GitHub Release whose body states, at minimum, what it contains (per the Manifest entry) and, if applicable, what it explicitly does not contain yet — the omission that caused `v1.0.0`'s own mislabeling.
- **Done when:** The Release body's claims are checkable against the Manifest entry with no reader-side inference required.

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

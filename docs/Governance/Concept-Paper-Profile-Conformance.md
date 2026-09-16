<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Concept Paper — Profile Conformance

[← Back](ADR-Candidates.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Concept Paper — Profile Conformance

**Document ID:** GOV-CONCEPT-PROFILE-CONFORMANCE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 16 September 2026

---

# Purpose

`Specification/08 Conformance.md` and `Language/Conformance.md` both publish three Conformance Levels: Core, Extended and Profile. Core and Extended each carry stated obligations. Profile Conformance carries none: it is named, and the mechanics of a profile are deferred in the chapter's own words as "intentionally not fully specified in this revision".

`CAND-002`, open since 22 July 2026, asks how a profile is declared, bounded and validated. This paper is the grounding for that candidate's Decision. It records the options considered, the mechanism adopted, and the limits of what the mechanism achieves.

This paper imposes no requirement. It is Informative in the sense `Documentation-Standards.md` defines, and nothing downstream of the Canonical Source tier introduces requirements, per `Publication-Model.md`.

---

# 1. What the Decision Resolves, and What It Does Not

The Decision makes a profile claim addressable, resolvable and non-drifting. It does not make a profile claim true.

Nothing here establishes that any implementation satisfies any requirement. Verification is the other half of `EPIC-E`'s Definition of Done, the Conformance Test Suite specification, and it remains blocked on `AO-062`, which records that Core Conformance is defined by reference to a set of mandatory requirements that no document enumerates, and that the normative keywords cannot be separated mechanically from prose because `Core/Manifest.md` extends the RFC 2119 meanings to the lowercase forms.

A validated declaration proves that a claim is well formed, resolves at a pinned commit, and has not drifted. It proves nothing about behaviour.

---

# 2. The Mechanism

A profile is formally defined, in the sense `Specification/08 Conformance.md` already uses that phrase, if and only if the claimant has published a Profile Declaration satisfying the eight rules below. The declaration is published by the claimant, at a stable URL, under the claimant's own name. It is not an OCOM publication and occupies no tier of `Publication-Model.md`.

**R1. Declared.** A Profile Declaration carries seven fields: the profile name, prefixed by the claimant's own namespace and never a bare "OCOM *x* Profile"; the claimant's identity; the Release Identifier drawn from `Publication-Manifest.md`; that entry's Commit value; the Included Set; the Extensions list, which may be empty; and a statement that OCOM has not reviewed, approved, registered or certified the profile.

**R2. Pinned to a commit, not to a version label.** `Publication-Model.md` records that the commit, not the version number, pins the exact file set. A declaration naming a version and no commit is not a declaration.

**R3. Bounded by whole canonical source documents, each content addressed.** The Included Set is a list of repository paths under the Canonical Source tier, each carrying the SHA-256 of that file's bytes at the pinned commit. Clause-level scoping is not available, for the reason `AO-062` records: no statement in this repository carries an identifier, so a clause cannot be cited. A path can, and the hash makes a changed document break its own address instead of silently inheriting it. Paths under `docs/Specification/` are excluded, since that tier introduces no requirement and subsetting it would create a second statement of one.

**R4. Floor.** The Included Set shall contain the canonical documents that Chapters 4 to 6 compile, computed from those chapters' own Source lines at the pinned commit rather than from a list held here. At commit `91d40db` that set is twenty one documents: the twelve `Meta/` documents named in `Specification/04 Meta Model.md`, the seven `Models/` documents named in `Specification/05 Object Model.md`, and `Models/Lifecycle.md` with `Lifecycles/Lifecycles.md` named in `Specification/06 Lifecycle Model.md`. This is Chapter 8's phrase "while preserving compatibility with Core Conformance" expressed as set inclusion, and it is what keeps a profile claim from contradicting Chapter 8's own Non-Conformance clause.

**R5. Subset only.** A profile narrows scope by excluding documents. It does not narrow, restate, paraphrase, weaken or reinterpret any requirement in a document it includes. Specialization, which Chapter 8 names alongside subset, is out of scope for this version. A declaration that restates a requirement is invalid on its face, per Single Source of Truth.

**R6. Additions are Extensions, not profile content.** If the Extensions list is non-empty, the claim is Extended Conformance over a named profile and is labelled as such. Profile Conformance alone means subset with no additions. This reuses the Extension Conformance clause already published rather than opening a second extension route.

**R7. The Excluded Set is computed, never asserted.** The claimant publishes only the Included Set. The complement is derived from the checkout at the pinned commit, which removes the possibility of a declaration whose two halves disagree.

**R8. Append only.** A changed Included Set is a new profile version at a new stable URL, never an edit to a published one, mirroring the discipline already used for `ADR-Candidates.md`, `Architecture-Observations.md` and `Publication-Manifest.md`.

---

# 2.1 What a Profile Can and Cannot Express

248 documents in this repository carry a level-one Conformance section. Twenty one of them are the floor. A profile is therefore a named, published selection from the remainder, declared on top of the Core rather than carved out of it.

A profile cannot take less than the Core. Chapter 8's Non-Conformance clause already states that an implementation failing one or more mandatory requirements shall not claim conformance with the corresponding version. The adopter who wants to drop part of Chapters 4 to 6 was never served by this level and is not served by it now: that adopter stays where Chapter 8 already puts them, documenting partial support without a conformance claim.

Document granularity is coarse and real adoption is not. An adopter who implements most of `Models/Entity.md` but not one of its obligations cannot express that. Whether a finer unit is ever warranted is gated on `AO-062`'s requirement register existing.

---

# 3. Validation

A validator takes a published declaration and a checkout at the commit it names, runs offline, contacts no service, and asks the claimant for nothing. Ten blocking assertions and one advisory report.

| # | Assertion |
|---|---|
| A1 | All seven `R1` fields are present and non-empty. |
| A2 | The declared Release matches an entry in `Publication-Manifest.md`, and the declared commit equals that entry's Commit value. |
| A3 | The matched entry's Status is neither Historical nor Superseded. `v1.0.0` and `v1.1.0` fail this today by their own recorded Status. |
| A4 | Every included path exists at the pinned commit, lies under a Canonical Source directory, and is not under `docs/Specification/`. |
| A5 | Every included hash equals the SHA-256 of that file's bytes at the pinned commit. |
| A6 | The floor, computed from the Source lines of Chapters 4, 5 and 6 at the pinned commit, is a subset of the Included Set. Failure names each missing floor document. |
| A7 | The declaration asserts no Excluded Set. |
| A8 | The Extensions list and the Included Set are disjoint, and a non-empty Extensions list carries the Extended Conformance label and the four attestations Chapter 8 already imposes on extensions. |
| A9 | The profile name begins with the claimant's namespace, and the no-review, no-certification statement is present. |
| A10 | For a profile version previously seen, the set of included paths and hashes is unchanged. |

Advisory, never blocking: the count of included documents carrying a Conformance section, and a warning that `Meta/Organization.md` carries one while falling outside the computed floor, because Chapter 4 compiles twelve `Meta/` documents and the Core Vocabulary has thirteen governed terms. That discrepancy is recorded as `AO-065` and is reported rather than hidden.

---

# 4. Options Considered

**Option 1, profile as a governed document.** A profile becomes a document in the Governance tier with an identifier of the form `PROFILE-<publisher>-<name>-NN`, addressed by path plus optional section heading plus hash, with a Profile Register held in this repository recording Validated, Failed or Not Submitted.

Not adopted as a whole. Nothing in it establishes a floor: a publisher could declare a profile of one Domains directory, pass every assertion, and claim Profile Conformance while satisfying none of the mandatory requirements of Chapters 4 to 6. A register of third-party claims is also a compliance program in substance, which `Language/Conformance.md` Independence closes. One device is adopted from it and credited here: the content hash on every included path.

**Option 2, profile as a published claim.** Adopted, with `R3` amended to carry a per-path hash and the floor's relationship to `AO-032` stated rather than left implicit.

**Option 3, suspend the level and record Profile Conformance as Reserved.** Not adopted. It decides a third outcome the candidate never recorded: `CAND-002` weighs defining now against leaving open and referencing from the Conformance chapter, and withdrawing a published level is neither. Its diagnosis is accepted and is why the adopted mechanism is as narrow as it is. Profile Conformance today carries zero obligations against four for Core and five for Extended, while `Language/Conformance.md`'s own Design Principles require conformance to be objective, measurable and verifiable.

**Option 4, profile as an evidenced claim, with the claimant enumerating each obligation.** Not adopted. Its coverage assertion does not run against this corpus. The twelve `Meta/` floor documents carry a stem plus three to six bullets, but all eight `Models/` documents carry a prose pointer with nothing enumerable: `Models/Entity.md`'s Conformance section reads in full, "An Entity conforms to this specification only if all mandatory requirements defined in this document are satisfied." A claimant quotes one sentence per `Models/` document and passes with complete coverage having enumerated nothing.

---

# 5. Boundaries Taken Deliberately

`AO-032` records that `Core/Manifest.md`'s Conformance sentence implies every Draft document binds, contradicting Chapter 8's scoping to Chapters 4 to 6, and that no document resolves which governs. This paper adopts Chapter 8's scoping for the purpose of resolving a profile declaration and for that purpose only. `AO-032` remains Open. If it is later decided the other way, the computed floor widens and every declaration fails revalidation at the next Release, which is the intended behaviour of a pinned declaration rather than a defect in it.

No register of profiles is created. A profile published elsewhere and never submitted anywhere is still a profile; it is simply unlisted.

The naming rule in `R1` binds only the honest. `CAND-007` records that no stewardship model exists for the words OCOM and OCOM-compatible, and holds that question open as an unfiled Freeze exception. `R1` creates no naming-rights regime and prejudges nothing about it.

`docs/README.md` describes `Domains/` as business domain profiles. Those are not profiles in the conformance sense. The collision is recorded here, not fixed.

---

# 6. Failure Mode

If nobody publishes a declaration, this mechanism produces a defined form and a validator with nothing to validate. The Evidence Register publishes zero verified implementations and zero independent validations, so that is the expected case rather than an unlikely one. It is still a smaller risk than the status quo, in which a published conformance level carries no obligation anywhere.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 16 September 2026 | Initial paper, written as the grounding for `CAND-002`'s Decision: the eight declaration rules, the ten validator assertions, the four options considered, and the boundaries taken deliberately. |

<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Conformance Test Suite

[← Back](Concept-Paper-Profile-Conformance.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Conformance Test Suite

**Document ID:** GOV-CONFORMANCE-TEST-SUITE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 16 September 2026

---

# Purpose

`Specification/08 Conformance.md` defines Core Conformance as support for all mandatory requirements of Chapters 4 to 6, and `Language/Conformance.md` requires conformance to be objective, measurable and verifiable. `AO-062` records that no document enumerates those requirements, so a claim of Core Conformance has had nothing to be checked against. `Master-Architecture-Backlog.md` EPIC-E asks for a checkable Conformance Test Suite specification, tooled minimally or not at all, as the second half of making OCOM-compatible a claim that can be checked rather than asserted.

This document is that specification. It states how the requirements are enumerated without editing any normative document, what a test is, what the suite covers and does not, and how a result is reported. It imposes no requirement of its own: it is Informative in the sense `Documentation-Standards.md` defines, and nothing downstream of the Canonical Source tier introduces requirements, per `Publication-Model.md`. It prescribes no testing framework, certification body or compliance program, which `Language/Conformance.md` Independence excludes; it is the automated validation route that document's Validation of Conformance section names, published by OCOM so that a claimant, or anyone else, can run it. The rules this document states bind the suite, which OCOM publishes, and the form of its reports, which whoever runs the suite publishes; they impose nothing on an implementation beyond the Statements themselves, and the suite defers to Chapter 8 and the documents it compiles for what a conformance claim means.

---

# 1. Subject and Requirement Set

The subject of a test is an implementation, since Chapter 8 scopes conformance claims to implementations and not to individual models. The suite reaches the implementation through two artifacts it produces: its Conformance Statement, with the fields `Language/Conformance.md` lists (implementation name, supported specification version, implemented capabilities, supported extensions, known limitations), and one or more exported models in the implementation's own serialization, accompanied by a Representation Map that states how each element of the OCOM vocabulary is represented in that serialization. The suite prescribes no serialization format, per `Language/Serialization.md` and `Language/Conformance.md` Independence; the Representation Map is what makes a format-independent test possible.

The requirement set of Core Conformance is the set of canonical source documents that Chapters 4, 5 and 6 compile, read from those chapters' Source lines at the commit tested against, the same computation `Concept-Paper-Profile-Conformance.md` uses for the profile floor (`R4`). At the commit that records this document that set is twenty two documents: thirteen under `Meta/`, eight under `Models/` and `Lifecycles/Lifecycles.md`. The claim clauses Chapter 8 compiles from `Language/Conformance.md`, its Mandatory Requirements, Version Conformance, Extension Conformance and Non-Conformance sections, apply to every claim and are tested through the Conformance Statement (Section 3). `AO-014` and `AO-032` record that other chapters and `Core/Manifest.md` scope conformance differently; this document adopts Chapter 8's scoping for the purpose of the suite and for that purpose only, as the concept paper did, and both observations stay Open.

---

# 2. The Requirement Register, Derived and Never Edited

`AO-062` records that the normative keywords cannot be separated mechanically from the same words used descriptively, because `Core/Manifest.md` extends the RFC 2119 meanings to the lowercase forms. The register therefore does not try to. It over-includes by rule and records the exceptions as decisions, so that the Core stays untouched under `CAND-007` and the register stays derived, which is the route `AO-062`'s Recommendation names.

**Derivation.** For each document in the requirement set, the body between the navigation block and the Revision History section is read section by section under its level-one headings. Every paragraph or list item that contains at least one of the keywords shall, shall not, must, must not, should, should not, may, may not, in any letter case, yields one Statement; a paragraph that carries a keyword and ends with a colon absorbs the list that follows it, with or without an intervening blank line, so that a stem such as "Every Entity shall:" and its items are one Statement, while a list under a stem that carries no keyword, such as "Every Lifecycle:" in `Lifecycles/Lifecycles.md`, yields one Statement per item that carries one. Metadata lines, tables and headings yield nothing. The keyword found first classifies the Statement: shall and must as mandatory, should as recommended, may as optional. The list is wider than the lowercase extension `Core/Manifest.md` names, since it adds may not, which RFC 2119 does not define; over-inclusion is the strategy, so the wider list is deliberate.

**Identity.** A Statement's identity is the SHA-256 of its document path, its level-one section heading and its text, joined by newlines, so that a changed sentence breaks its own identity instead of silently inheriting it; the text is the paragraph's lines joined by single spaces, with each absorbed list item appended after a space without its list marker. A separate, append-only Alias File maps each identity to a stable alias of the form `REQ-<document>-<n>` and carries, per alias, at most one Disposition: Descriptive, for a Statement whose keyword imposes no obligation (for example "Additional relationship types may be introduced without affecting the model"), or Review, for a Statement that imposes an obligation no mechanical procedure can decide (Section 3). A Disposition is a recorded decision with a reason and a date; it never edits the source and never removes a Statement from the register.

**Census.** At the commit that records this document the derivation yields 335 Statements across the twenty two documents: 182 mandatory, 26 recommended and 127 optional. Per document the count runs from 2 (`Meta/Organization.md`) to 23 (`Meta/Ownership.md`). No Disposition has been recorded yet, so every Statement stands as derived.

**Tooling.** `tools/conformance/requirement_register.py` implements this section since 17 September 2026: it computes the requirement set from the Source lines of Chapters 4 to 6, derives the Statements, writes `Governance/Requirement-Register.md` and checks it against a regeneration, and keeps `Governance/Requirement-Aliases.md` covered; the CI job `Requirement register regenerates cleanly` runs both checks on every push and pull request (`CI-DESIGN.md`).

**Regeneration.** The register is a derived artifact in the sense `AO-064` uses, not a Projection-tier record of `Publication-Model.md`: it derives from twenty two documents rather than one, and the Publication Engine does not produce it. It is regenerated from the sources whenever it is used and compared against any published copy, and a divergence fails the run; this is the rule `AO-064` recommends for derived artifacts, applied here to one artifact before any general rule exists. The Alias File is not derived and is the only hand-written part.

---

# 3. Tests

A Test binds one Statement to one procedure with one pass criterion. Every mandatory and recommended Statement has exactly one Test; an optional Statement has a Test that applies only when the Conformance Statement claims the capability. A Test has one of five kinds, recorded beside the alias.

| Kind | What it decides | Input read | Example Statement |
|---|---|---|---|
| Presence | that a required element, attribute or section exists for every instance of an Object type | exported model, Representation Map | "Every Entity shall: possess a unique identity; ... belong to exactly one primary Domain; ..." (`Models/Entity.md`) |
| Invariant | that a prohibited condition never occurs in the exported model, or that the implementation refuses it where it exposes a refusal record | exported model, refusal record | "Every Event shall: ... remain immutable after creation" (`Models/Event.md`) |
| Transition | that every recorded State change is a transition the Lifecycle permits and that a terminal State is not left | exported model | "Every Lifecycle shall: ... define permitted State Transitions" (`Models/Lifecycle.md`) |
| Declaration | that the Conformance Statement declares what a claim clause requires to be declared | Conformance Statement | "An implementation shall identify the specification version against which conformance is claimed" (`Language/Conformance.md`, compiled by Chapter 8) |
| Review | that a reviewer has examined the evidence and recorded a judgment, for a Statement no mechanical procedure can decide | reviewer record | "Identity shall not depend on implementation technology" (`Models/Entity.md`) |

A Test's outcome is Pass, Fail, Not Applicable (an optional capability not claimed, or a Statement dispositioned Descriptive), or Review Pass and Review Fail for the fifth kind. The wording in the Example column is the Statement text at the commit that records this document; the register, not this table, is the reference.

The suite reports an implementation as passing Core Conformance when every mandatory Test is Pass or Review Pass; a Review Pass is a named reviewer's recorded judgment that the Statement is met, and Chapter 8's own criterion, support for all mandatory requirements, is not altered by it. One Fail on a mandatory Test is Non-Conformance and Chapter 8's clause applies: "it shall not claim conformance with the corresponding version of this specification", while "partial support may be documented without a conformance claim". Recommended and optional outcomes are reported and do not affect the Core claim.

---

# 4. Report

A Test Report carries: the Release Identifier and Commit from `Publication-Manifest.md` tested against; the implementation's identity and its Conformance Statement; the register's Statement count and the Alias File revision used; one row per alias with kind and outcome; the reviewer's identity for every Review outcome; and the summary counts. A report is published by whoever ran the suite, under that party's name, at a stable address, and is append-only: a new run is a new report. A report published by the claimant is self-validation; a report published by another party is the independent validation the Evidence Register on ocom.uno counts as its fourth evidence level. The suite does not tell the two apart; the publisher does.

---

# 5. Profiles and Extensions

For a claim of Profile Conformance the requirement set is the Included Set of the Profile Declaration (`Concept-Paper-Profile-Conformance.md`), which by `R4` contains the Core set, so the Core Tests always run and the profile adds the Statements of its further documents. For Extended Conformance, extensions are not tested against Statements of their own; Declaration Tests check the four attestations Chapter 8 imposes on extensions: compatibility preserved, normative semantics unchanged, clearly identifiable, fully documented.

---

# 6. What the Suite Does Not Do

It does not verify behaviour beyond what the exported artifacts and the Conformance Statement show. It does not decide whether a Descriptive disposition is right; that is a recorded decision anyone can contest through the governance process. It does not certify: `Language/Conformance.md` excludes certification procedures, and a Pass is a published report, not a mark. It does not close `AO-062`: the register makes the requirement set enumerable, and the keyword problem that observation records is handled by over-inclusion and disposition rather than solved. It does not test the World Model: the requirement set is the twenty two documents above, none of which is the Layer 2 document `CAND-014` leaves unauthored.

---

# 7. Tooling Not Required for v1.0

`Master-Architecture-Backlog.md` Part 8 requires this specification to be checkable in principle and does not require the tooling. Of the tooling the rules above call for, three items exist since 17 September 2026: the register generator implementing Section 2, the Alias File with its first population (335 aliases, no Disposition yet), and the CI job that regenerates the register and fails on divergence and on a Statement without an alias. What remains: a validator for the Representation Map, and the first submitted report. None of these edits a normative document.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 16 September 2026 | Initial specification, the second half of `EPIC-E`: the requirement set computed from Chapters 4 to 6, the Requirement Register derived by rule and never edited (335 Statements at this commit), five Test kinds, the Test Report, and the tooling that remains. |
| 0.1 | 16 September 2026 | After the dogfooding audit of Release v1.2.0: the derivation rule states that a colon stem absorbs its list across a blank line and that the identity uses the level-one heading; the keyword list is declared wider than `Core/Manifest.md`'s; the register is called a derived artifact rather than a Projection-tier record; the Purpose states that the document's rules bind the suite, not implementations; Chapter 8's Non-Conformance clause is quoted. Counts unchanged. |
| 0.1 | 17 September 2026 | Section 2: identity concatenation and text normalization stated; Tooling paragraph added. Section 7: the generator, the Alias File and the CI job exist; the Representation Map validator and the first report remain. |

<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Conformance Test Suite

[← Back](Concept-Paper-Profile-Conformance.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Conformance Test Suite

**Document ID:** GOV-CONFORMANCE-TEST-SUITE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 23 September 2026

---

# Purpose

`Specification/08 Conformance.md` defines Core Conformance as support for all mandatory requirements of Chapters 4 to 6, and `Language/Conformance.md` requires conformance to be objective, measurable and verifiable. `AO-062` records that no document enumerates those requirements, so a claim of Core Conformance has had nothing to be checked against. `Master-Architecture-Backlog.md` EPIC-E asks for a checkable Conformance Test Suite specification, tooled minimally or not at all, as the second half of making OCOM-compatible a claim that can be checked rather than asserted.

This document is that specification. It states how the requirements are enumerated without editing any normative document, what a test is, what the suite covers and does not, and how a result is reported. It imposes no requirement of its own: it is Informative in the sense `Documentation-Standards.md` defines, and nothing downstream of the Canonical Source tier introduces requirements, per `Publication-Model.md`. It prescribes no testing framework, certification body or compliance program, which `Language/Conformance.md` Independence excludes; it is the automated validation route that document's Validation of Conformance section names, published by OCOM so that a claimant, or anyone else, can run it. The rules this document states bind the suite, which OCOM publishes, and the form of its reports, which whoever runs the suite publishes; they impose nothing on an implementation beyond the Statements themselves, and the suite defers to Chapter 8 and the documents it compiles for what a conformance claim means.

---

# 1. Subject and Requirement Set

The subject of a test is an implementation, since Chapter 8 scopes conformance claims to implementations and not to individual models. The suite reaches the implementation through two artifacts it produces: its Conformance Statement, with the fields `Language/Conformance.md` lists (implementation name, supported specification version, implemented capabilities, supported extensions, known limitations), and one or more exported models in the implementation's own serialization, accompanied by a Representation Map that states how each element of the OCOM vocabulary is represented in that serialization. The suite prescribes no serialization format, per `Language/Serialization.md` and `Language/Conformance.md` Independence; the Representation Map is what makes a format-independent test possible. Since `CAND-026` (22 September 2026) the map also declares the scope of the export's identities, one of the five `Meta/Identity.md` names, in a row of kind `declaration`, and the Reference Serialization published as `Adoption/Reference Serialization.md` is the encoding an implementation starts from when it has none; the schema derived from it validates a file in that encoding and nothing about OCOM.

Core Conformance is defined by `Language/Conformance.md`, which states it as support for all mandatory language requirements; `CAND-021` (19 September 2026) records that `Specification/08 Conformance.md` names where those requirements are found and originates nothing, and that the enumeration below is the reading this suite adopts. The requirement set of Core Conformance is the set of canonical source documents that Chapters 4, 5 and 6 compile, read from those chapters' Source lines at the commit tested against, the same computation `Concept-Paper-Profile-Conformance.md` uses for the profile floor (`R4`). At the commit that records this document that set is twenty two documents: thirteen under `Meta/`, eight under `Models/` and `Lifecycles/Lifecycles.md`. The claim clauses Chapter 8 compiles from `Language/Conformance.md`, its Mandatory Requirements, Version Conformance, Extension Conformance and Non-Conformance sections, apply to every claim and are tested through the Conformance Statement (Section 3). `AO-014` and `AO-032` record that other chapters and `Core/Manifest.md` scope conformance differently; this document adopts Chapter 8's scoping for the purpose of the suite and for that purpose only, as the concept paper did, and both observations stay Open.

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

A Test binds one Statement to one procedure with one pass criterion. Every mandatory and recommended Statement has exactly one Test; an optional Statement has a Test that applies only when the Conformance Statement claims the capability. A Test has one of six kinds, recorded beside the alias.

| Kind | What it decides | Input read | Example Statement |
|---|---|---|---|
| Presence | that a required element, attribute or section exists for every instance of an Object type and, where the Statement asks for one of it, that exactly one is there (`CAND-025`) | exported model, Representation Map | "Every Entity shall: possess a unique identity; ... belong to exactly one primary Domain; ..." (`Models/Entity.md`) |
| Invariant | that a prohibited condition never occurs in the exported model, or that the implementation refuses it where it exposes a refusal record | exported model, refusal record | "Every Event shall: ... remain immutable after creation" (`Models/Event.md`) |
| Transition | that every recorded State change is a transition the Lifecycle permits and that a terminal State is not left | exported model | "Every Lifecycle shall: ... define permitted State Transitions" (`Models/Lifecycle.md`) |
| Declaration | that the Conformance Statement declares what a claim clause requires to be declared | Conformance Statement; the Representation Map for `Meta/Identity.md`'s scope rule (`CAND-026`) | "An implementation shall identify the specification version against which conformance is claimed" (`Language/Conformance.md`, compiled by Chapter 8) |
| Integrity | that a record the implementation claims immutable carries a demonstration that it is unaltered, and that the demonstration verifies against the record as exported; a record named by an erasure record is excluded from the Test only when that erasure record names a Policy the export declares and an actor (`AO-085`, a postscript to `CAND-024`) | exported model, Representation Map (which declares the demonstration's method and where each record carries it) | "Audit records shall remain immutable." (`Meta/Ownership.md`) |
| Review | that a reviewer has examined the evidence and recorded a judgment, for a Statement no mechanical procedure can decide | reviewer record | "Identity shall not depend on implementation technology" (`Models/Entity.md`) |

A Test's outcome is Pass, Fail, Not Applicable (an optional capability not claimed, or a Statement dispositioned Descriptive; the first such disposition is `REQ-LIFECYCLES-004`, recorded by `CAND-020` on 19 September 2026 because it and `REQ-MODELS-LIFECYCLE-002` cannot both be satisfied, which `AO-079` records), or Review Pass and Review Fail for the Review kind. An Integrity Test whose export declares no demonstration is pending rather than passed: the suite verifies a demonstration, it does not supply one. The wording in the Example column is the Statement text at the commit that records this document; the register, not this table, is the reference.

The suite reports an implementation as passing Core Conformance when every mandatory Test is Pass or Review Pass; a Review Pass is a named reviewer's recorded judgment that the Statement is met, supplied to the suite as a Reviewer Record: one row per Test with the Test, the outcome (Review Pass or Review Fail), the reviewer's name, the date and the reason, which `tools/conformance/validate.py --reviews` reads fail-closed and applies only to Tests no procedure decided, never over a mechanical Pass or Fail, keeping beside each judgment the reason the procedure gave for deciding nothing. A record may declare, in a line `**Recorded against:** model <digest>, map <digest>, statement <digest>`, the inputs its judgments were made against, and the suite refuses it against any other export, and Chapter 8's own criterion, support for all mandatory requirements, is not altered by it. One Fail on a mandatory Test is Non-Conformance and Chapter 8's clause applies: "it shall not claim conformance with the corresponding version of this specification", while "partial support may be documented without a conformance claim". Recommended and optional outcomes are reported and do not affect the Core claim.

---

# 4. Report

A Test Report carries: the Release Identifier and Commit from `Publication-Manifest.md` tested against, with the register's Statement count and the Alias File revision, and the digest of each input the run read (the model, the map, the Conformance Statement, the Requirement Register, the Alias File, the Test Catalogue, and the Reviewer Record when one is supplied), so that an outcome names what produced it and a Review outcome names what it was recorded against; the implementation's identity and its Conformance Statement; the register's Statement count and the Alias File revision used; one row per alias with kind and outcome; the reviewer's identity for every Review outcome, read from the Reviewer Record and listed in the report's Reviewers section; and the summary counts. A report is published by whoever ran the suite, under that party's name, at a stable address, and is append-only: a new run is a new report. A report published by the claimant is self-validation; a report published by another party is the independent validation `Governance/Evidence-Register.md` counts as its fourth evidence level (the register moved into this repository on 19 September 2026, `CAND-022`; the site's URLs redirect to it). The suite does not tell the two apart; the publisher does.

---

# 5. Profiles and Extensions

For a claim of Profile Conformance the requirement set is the Included Set of the Profile Declaration (`Concept-Paper-Profile-Conformance.md`), which by `R4` contains the Core set, so the Core Tests always run and the profile adds the Statements of its further documents. For Extended Conformance, extensions are not tested against Statements of their own; Declaration Tests check the four attestations Chapter 8 imposes on extensions: compatibility preserved, normative semantics unchanged, clearly identifiable, fully documented.

---

# 6. What the Suite Does Not Do

It does not verify behaviour beyond what the exported artifacts and the Conformance Statement show. It does not decide whether a Descriptive disposition is right; that is a recorded decision anyone can contest through the governance process. It does not certify: `Language/Conformance.md` excludes certification procedures, and a Pass is a published report, not a mark. It does not close `AO-062`: the register makes the requirement set enumerable, and the keyword problem that observation records is handled by over-inclusion and disposition rather than solved. It does not test the World Model: the requirement set is the twenty two documents above, none of which is the Layer 2 document `CAND-014` leaves unauthored.

---

# 7. Tooling Not Required for v1.0

`Master-Architecture-Backlog.md` Part 8 requires this specification to be checkable in principle and does not require the tooling. Of the tooling the rules above call for, three items exist since 17 September 2026: the register generator implementing Section 2, the Alias File with its first population (335 aliases, no Disposition yet), and the CI job that regenerates the register and fails on divergence and on a Statement without an alias. The validator exists since 20 September 2026 (`tools/conformance/validate.py`, run end to end against `Examples/Conformance/`), and since 22 September 2026 `tools/conformance/reference_schema.py` derives the schema of the Reference Serialization (`CAND-026`). What remains is the first submitted report. None of these edits a normative document.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 16 September 2026 | Initial specification, the second half of `EPIC-E`: the requirement set computed from Chapters 4 to 6, the Requirement Register derived by rule and never edited (335 Statements at this commit), five Test kinds, the Test Report, and the tooling that remains. |
| 0.1 | 16 September 2026 | After the dogfooding audit of Release v1.2.0: the derivation rule states that a colon stem absorbs its list across a blank line and that the identity uses the level-one heading; the keyword list is declared wider than `Core/Manifest.md`'s; the register is called a derived artifact rather than a Projection-tier record; the Purpose states that the document's rules bind the suite, not implementations; Chapter 8's Non-Conformance clause is quoted. Counts unchanged. |
| 0.1 | 17 September 2026 | Section 2: identity concatenation and text normalization stated; Tooling paragraph added. Section 7: the generator, the Alias File and the CI job exist; the Representation Map validator and the first report remain. |
| 0.1 | 19 September 2026 | Section 1 cites `Language/Conformance.md` as the definition of Core Conformance and names the enumeration as this suite's reading (`CAND-021`); Section 3 records the first Descriptive disposition (`CAND-020`). |
| 0.1 | 21 September 2026 | Section 3 gains a sixth Test kind, Integrity, per `CAND-024` (Decided 21 September 2026): a record the implementation claims immutable carries a demonstration that it is unaltered, and the suite verifies it against the exported record. It is the kind that can return Fail on immutability, which no earlier kind could. |
| 0.1 | 22 September 2026 | Section 1 records the Identity scope declaration and the Reference Serialization (`CAND-026`); Section 3's Presence row counts one where a Statement says one (`CAND-025`), its Declaration row reads the map for the scope rule, its Integrity row grants the erasure exclusion only to an erasure record naming a declared Policy and an actor (`AO-085`); Section 7 brought current. No Test kind added. |
| 0.1 | 22 September 2026 | Sections 3 and 4 name the Reviewer Record, the artifact that carries a named reviewer's judgments, read by the validator (`--reviews`); the first-90-days lens of the enterprise evaluation of the same day found the validator unable to accept one. No Test kind added, no requirement changed. |
| 0.1 | 22 September 2026 | Section 4: the report names the digests of the model, the map and the Conformance Statement it read, beside the Release, the register count and the Alias File revision it already required; the all-packages test of the same day found four of Section 4's six items missing from the generated report and a Review judgment bound to nothing. No requirement changed. |
| 0.1 | 22 September 2026 | Section 4 points at `Governance/Evidence-Register.md` rather than at the site, which `CAND-022` moved the register from on 19 September 2026; found by the all-packages test of the same day. |
| 0.1 | 23 September 2026 | Section 3: a Reviewer Record may declare the inputs it was recorded against, and the suite refuses it against another export; a judgment keeps the mechanical reason it replaced. Section 4: the report digests every input, including the Requirement Register, the Alias File, the Test Catalogue and the Reviewer Record, and names the checkout it read rather than the Manifest's latest Release. Round 2 of the all-packages test found the report naming a commit it never verified and judgments bound to nothing. |

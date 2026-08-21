<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Principles

[← Back](Architecture-Discovery-Summary.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Principles of OCOM

**Document ID:** GOV-ARCHITECTURE-PRINCIPLES-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

This is not an ADR Candidate, not Specification text, and not a Concept Paper analyzing a single open question. It is a small set of architectural-philosophy principles, distilled only from conclusions already reached in prior discussion (the Knowledge/World Model work, the long-term ecosystem analysis, and the architecture stress test), intended to guide how OCOM — as a Specification and as an ecosystem of implementations — evolves. Nothing here introduces a new idea; each principle traces to a specific, already-reasoned conclusion, cited in its explanation. A self-check against four questions follows each principle, and a consolidated self-check closes the document.

---

# Principle 1 — Specification Defines Contracts, Not Products

**The Specification defines an implementation-independent contract; it does not define, prescribe, or privilege any single product built against that contract.**

Established from the standards-analogy sweep (SQL, HTTP, OpenAPI, Kubernetes, BPMN, RDF, Git): every mature standard examined normatively fixes a data model or interface contract while leaving the executing system free. Applied to OCOM, the Specification's job is to state what must be true of an Object/Memory/Evidence/Knowledge/[World Model] structure and of the guarantees a conformant system provides — never how any particular system (Reader, an Agent, a BI Engine, a Rule Engine, a Digital Twin) is built internally.

Git's own history was named as a cautionary counter-example: for years, "compatible with Git" effectively meant "byte-compatible with the `git` binary," because the object model was never cleanly separated from the one shipping implementation. That drift is exactly what this principle exists to prevent for OCOM from the outset.

**Architectural consequences:** every OCOM-shaped product is evaluated against the same contract, not against each other. Specification changes must be justified by contract necessity, never by "this is what product X needs."

**Allows:** a Rule Engine implementing OCOM with a completely different internal reasoning approach than Reader, provided it satisfies the same observable guarantees.

**Forbids:** adding a Specification requirement whose only justification is "Reader already works this way"; writing Specification text that presumes a particular execution technology.

**Self-check:** (1) Derived from an existing conclusion — yes, the standards-analogy sweep. (2) Consistent with Constitution — yes, matches Manifest's existing Scope exclusion of software architecture/implementation technologies. (3) Risk of making Reader a hidden standard — no, this principle exists specifically against that risk. (4) Unnecessarily constrains future implementations — no; it is the least constraining of the principles in this set.

---

# Principle 2 — Observable Guarantees Over Internal Algorithms, With a Recording Exception

**The Specification defines guarantees observable at a system's boundary; the internal algorithm used to satisfy them is free — except that the process of recording provenance may carry minimal normative constraints where their absence would make a guarantee unfalsifiable.**

This is the stress-tested form of the earlier, unqualified "guarantees not algorithms" claim. The unqualified version did not survive stress testing: three concrete constructions were found that are formally compliant while substantively hollow — defaulting every Evidence source to "unknown" even when real provenance was available at recording time; reporting Confidence: Verified without any real verification process; and generating post-hoc, plausible-looking citations that were not the actual causal basis of an answer. In each case the loophole existed because the guarantee had no attached requirement on the process producing it, making it purely self-declared.

The resulting refinement: recording (what enters Memory/Evidence, and how faithfully) needs enough mechanism-level constraint to prevent gaming; interpretation (how an already-recorded corpus is read, ranked, and turned into an answer) does not.

**Architectural consequences:** a conformant implementation cannot default Evidence source classification to "unknown" as a matter of convenience when real provenance was available. Confidence must be demonstrably a function of the Evidence actually attached to a claim, not an independently set field.

**Allows:** two implementations using entirely different retrieval, ranking, or generation algorithms, both fully conformant, because neither choice touches the recording layer.

**Forbids:** satisfying the letter of "Evidence must exist" by attaching hollow, uninvestigated Evidence records purely to pass a conformance check.

**Open item, not resolved here:** the exact boundary of "minimal" mechanism constraint on recording is named, not precisely drawn. This principle states that the boundary exists and roughly where, not its final operational shape.

**Self-check:** (1) Derived from an existing conclusion — yes, the stress test, Parts 1–4. (2) Consistent with Constitution — yes. (3) Risk of making Reader a hidden standard — no, neutral. (4) Unnecessarily constrains future implementations — **possible risk, flagged**: because the recording-side exception is not yet precisely bounded, a future, careless expansion of "minimal" constraints could creep beyond what is necessary. This principle is kept, with the boundary explicitly marked open rather than pretended to be closed.

---

# Principle 3 — Recording Before Interpretation

**OCOM standardizes the recording of organizational truth; interpretation of that recorded truth is an implementation responsibility.**

This reframes Constitution §5's Memory → Knowledge → World Model chain in operational terms: Memory is the recording layer (what happened, evidenced), and everything downstream — Knowledge, World Model, and any answer an Agent produces — is interpretation built on top of it. The distinction gives a direct test for classifying any future proposed requirement: does it constrain what gets written, or how a written corpus gets read? The former may be normative (Principle 2's exception); the latter should not be (Principle 1, Principle 7).

**Architectural consequences:** provides the operative test for scoping every future Specification requirement.

**Allows:** any implementation to freely choose its own Knowledge-derivation or reasoning strategy, since these are interpretation.

**Forbids:** treating a specific interpretation strategy — a specific reasoning pipeline order, a specific confidence-scoring formula — as something the Specification should mandate.

**Self-check:** (1) Derived from an existing conclusion — yes, the stress test's write-path/read-path distinction (Part 3). (2) Consistent with Constitution — yes, it directly operationalizes §5. (3) Risk of making Reader a hidden standard — no. (4) Unnecessarily constrains future implementations — no.

---

# Principle 4 — Evidence Before Belief (Inherited from Constitution §3)

**No operational fact exists without Evidence — not independently asserted here; this is Constitution §3, named because Principles 2 and 3 depend on it directly.**

Unlike the other principles in this document, this is not a new conclusion synthesized from recent discussion — it is an already-adopted Canonical Principle. It is named here, not restated as an independent claim, because the "recording" layer Principles 2 and 3 describe is only meaningful because Evidence-backed recording is already mandatory. Restating a Canonical Principle independently at this document's level, rather than citing it, would risk the same kind of duplication this Specification already had to correct once, when `Core/Principles.md` Principle 11 duplicated content that belonged only to Constitution §14.

**Architectural consequences:** none beyond what §3 and ARCH-002 already establish.

**Allows / Forbids:** identical to Constitution §3 and ARCH-002 — see `Core/Constitution.md` and `Governance/Constitution-Step0-Summary.md`, Decision 2.

**Self-check:** (1) Derived from an existing conclusion — yes, but note it is not a *new* synthesis; it is a citation. (2) Consistent with Constitution — yes, it *is* Constitution. (3) Risk of making Reader a hidden standard — no. (4) Unnecessarily constrains future implementations — no more than §3 already does. **Form flagged for revision:** this entry should remain a citation, never be edited into an independent restatement of §3's wording, to avoid the exact duplication-drift pattern already found and fixed once in this Specification.

---

# Principle 5 — Reader Is Reference, Not Authority

**Reader demonstrates one valid way to implement OCOM; it never itself defines the Specification, and "this is how Reader does it" is never sufficient justification for a Specification change.**

Grounded directly in the Reader-as-trap analysis. The risk is not hypothetical: this same review already surfaced governance/approval content inside `AI/Knowledge/*` that plausibly leaked in from product-shaped (Reader-shaped) thinking rather than being derived from Constitution. Three structural mechanisms were identified as producing this drift over time, independent of anyone's intentions: documentation gravity (Reader as the only fully worked example), governance capture (one team currently maintains both Specification and Reader), and terminology drift (a Reader-coined term migrating into Specification prose without a decision ever being made to adopt it).

**Architectural consequences:** any Specification change citing Reader's behavior as justification must independently show which Constitution principle or ARCH decision it implements — "matches Reader" alone is not acceptable review language. A second, independent implementation, built by someone other than Reader's own team, using only the Specification text, was identified as the single most effective concrete de-risking action available — more valuable evidence that the contract is well-formed than any amount of additional Reader polish.

**Allows:** Reader to diverge from any other implementation in algorithm, UX, or product ambition (e.g. Reader's own Organizational Intelligence / "OCOM Expert" roadmap) without that divergence needing Specification sign-off.

**Forbids:** citing Reader's implementation choices as evidence in a Specification change proposal; building a future Conformance Test Suite that silently encodes Reader-specific behavior as a pass/fail criterion.

**Self-check:** (1) Derived from an existing conclusion — yes, stress test Part 5. (2) Consistent with Constitution — yes. (3) Risk of making Reader a hidden standard — this principle is the direct countermeasure to that exact risk. (4) Unnecessarily constrains future implementations — no; it protects them.

---

# Principle 6 — Conformance Is Demonstrated, Not Claimed

**A claim of OCOM compatibility must be verifiable against explicit, checkable criteria; self-declaration is not sufficient.**

The stress test's central finding was that, absent a mechanized way to verify guarantees, every guarantee in Principle 2 degrades into an unfalsifiable claim, and the ecosystem risk this creates (the "Confidence Race to the Bottom" scenario) is a plausible, causally traceable failure mode, not a generic worry. Constitution §12 and every `AI/*` document's descriptive "# Conformance" prose currently state what conformance *means*; none provide anything a third party can run to *prove* it.

**Architectural consequences:** motivates an eventual Conformance Test Suite (a checkable analogue to the CNCF Kubernetes Conformance Program) as a distinct governance deliverable, separate from the Specification's descriptive text.

**Allows:** third parties to seek and receive a genuine, checkable compatibility statement rather than relying on self-attestation.

**Forbids:** treating a document's own "# Conformance" prose section as sufficient proof of compatibility.

**Open item, not resolved here:** how such a Suite would be designed without itself becoming a barrier to entry for smaller or independent implementers.

**Self-check:** (1) Derived from an existing conclusion — yes, stress test Parts 1, 2, 6, 7. (2) Consistent with Constitution — yes. (3) Risk of making Reader a hidden standard — no, neutral; guards against exactly the self-attestation drift that would otherwise push the ecosystem toward "matches Reader" as the only trusted bar. (4) Unnecessarily constrains future implementations — **possible risk, flagged**: a poorly designed future Conformance Test Suite could become a resourcing barrier that favors well-funded vendors over independent implementers. This principle names the requirement, not the Suite's design; the design risk belongs to whoever specifies the Suite, not to this principle.

**No Conformance Test Suite exists today.** This document does not claim conformance is presently demonstrable for anything; it names a gap the ecosystem has not yet closed.

---

# Principle 7 — Architectural Independence

**The Specification remains independent of any specific LLM, product, orchestration framework, reasoning pipeline, or implementation.**

This is the ecosystem-wide statement of a pattern the Specification already applies locally — nearly every existing document (Memory, Knowledge, Agent) already carries its own "# Independence" section disclaiming a particular storage engine, LLM provider, or framework. The reasoning-pipeline case (no specific order in which an Agent gathers Objects, Knowledge, Memory, Evidence, and computes Confidence is privileged) is the same pattern, made explicit for a category the Specification had not previously named directly.

**Architectural consequences:** no future Specification text should presume execution technology. Existing per-document Independence sections are not redundant with this principle; this principle is their project-wide generalization.

**Allows:** BI Engine, Rule Engine, and Digital Twin implementations — none of which need be LLM-based at all — to be equally valid OCOM implementations alongside an LLM-based Agent.

**Forbids:** Specification language that names or presumes a specific model family, vendor, or execution framework.

**Self-check:** (1) Derived from an existing conclusion — yes, both the existing per-document pattern and the reasoning-pipeline conclusion from the boundary discussion. (2) Consistent with Constitution — yes, matches Manifest's Design Goals. (3) Risk of making Reader a hidden standard — no. (4) Unnecessarily constrains future implementations — no; strictly protective.

---

# Principle 8 — Evolution Without Lock-In

**New OCOM implementations must be able to appear without requiring changes to the Specification.**

A direct consequence of Principle 1: if the Specification is a genuine, sufficiently expressive contract, a new, previously unanticipated implementation (the hypothetical BI Engine, Rule Engine, or Digital Twin considered in the long-term evolution analysis) should be able to conform by mapping onto existing primitives, not by requiring the Specification's own governance process to first accommodate it. This is a stability property of the Specification itself, distinct from Principle 1: Principle 1 states what the Specification defines; Principle 8 states that what it defines should be sufficient without repeated amendment.

**Architectural consequences:** gives governance a concrete test for evaluating a Specification change requested by a new implementer: does satisfying this implementation genuinely require a new contract concept, or is the request implementation-specific accommodation that belongs in that implementation, not in the Specification?

**Allows:** a genuinely novel implementation category to build on OCOM without a Specification release cycle blocking it.

**Forbids:** growing the Specification reactively, one implementation's special case at a time, without asking whether the case reveals a real contract gap or just an implementation preference.

**Self-check:** (1) Derived from an existing conclusion — yes, the long-term evolution analysis (Question 1, Question 4). (2) Consistent with Constitution — yes. (3) Risk of making Reader a hidden standard — no; overlaps with, and reinforces, Principle 5's protection from a different angle. (4) Unnecessarily constrains future implementations — no; strictly protective.

---

# Consolidated Self-Check

| # | Principle | (1) Derived, not invented | (2) Consistent with Constitution | (3) Avoids hidden Reader authority | (4) Doesn't over-constrain |
|---|---|---|---|---|---|
| 1 | Specification Defines Contracts, Not Products | Yes | Yes | Yes | Yes |
| 2 | Observable Guarantees, With a Recording Exception | Yes | Yes | Yes | **Flagged** — recording-exception boundary not yet precisely drawn |
| 3 | Recording Before Interpretation | Yes | Yes | Yes | Yes |
| 4 | Evidence Before Belief (Inherited) | Yes (citation, not synthesis) | Yes (it is Constitution) | Yes | Yes |
| 5 | Reader Is Reference, Not Authority | Yes | Yes | Yes (direct countermeasure) | Yes |
| 6 | Conformance Is Demonstrated, Not Claimed | Yes | Yes | Yes | **Flagged** — a future Test Suite could become a resourcing barrier if designed carelessly |
| 7 | Architectural Independence | Yes | Yes | Yes | Yes |
| 8 | Evolution Without Lock-In | Yes | Yes | Yes | Yes |

Two flags were raised, on Principles 2 and 6, both on the same question (unnecessary future constraint), both already disclosed inline as "Open item, not resolved here" in their own sections. Neither is a reason to exclude the principle: both name a real boundary or a real design risk that belongs to a future, separate piece of work (precisely bounding the recording exception; designing the Conformance Test Suite), not to this document. No principle failed questions (1), (2), or (3).

Principle 4 was flagged on form, not substance: it must remain a citation of Constitution §3, never edited into an independent restatement, to avoid repeating a duplication error this Specification has already corrected once.

---

# Status

This document records architectural philosophy, not a decision. No Specification document has been changed. No ADR Candidate has been created. Two named open items (the recording-exception boundary in Principle 2; the Conformance Test Suite design in Principle 6) remain for future, separately authorized work.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial draft, eight principles, distilled from the Knowledge/World Model discussion, the long-term ecosystem analysis, and the architecture stress test |

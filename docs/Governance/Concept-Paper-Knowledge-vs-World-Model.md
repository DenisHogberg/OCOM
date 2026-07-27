<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Concept Paper — Knowledge vs World Model

[← Back](Constitution-Step0-Summary.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Concept Paper — Knowledge vs World Model

**Document ID:** GOV-CONCEPT-KNOWLEDGE-WORLDMODEL-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

Constitution §5 (Memory Precedes Knowledge) states a three-stage chain: **Memory → Knowledge → World Model.** The Knowledge Architecture Assessment (Constitution integration, Stage 3) found that `AI/Knowledge/*` currently describes Knowledge in a way that is, in several places, inconsistent with being a derived stage of that chain, and that "World Model" — the third named stage — has no corresponding document anywhere in the Specification.

This paper does not resolve that inconsistency. It describes, on the basis of the adopted Constitution and the current text of `AI/Knowledge/*`, what Knowledge currently does, which of those responsibilities read as more naturally belonging to World Model, which responsibilities cannot coherently belong to both layers at once, and what distinct ways of dividing the two are possible. No option is chosen. No specification document is changed. This is not an ADR Candidate.

---

# 1. Responsibilities Currently Placed on Knowledge

As written across `Knowledge.md`, `Knowledge Sources.md`, `Knowledge Lifecycle.md`, `Knowledge Governance.md`, and `Knowledge Quality.md`, Knowledge currently carries the following responsibilities:

1. **Semantic content representation.** Business concepts, organizational policies, business rules, operational procedures, reference data, taxonomies, classifications, definitions, best practices, decision guidelines (`Knowledge.md`, Knowledge Types).
2. **Provenance/origin classification.** A dedicated taxonomy of business-level origins — Organizational Documentation, Business Policies, Regulatory Requirements, Domain Experts, Historical Operational Experience, Approved External Sources — independent of Memory (`Knowledge Sources.md`).
3. **Human governance and approval.** Ownership, roles (Owner, Contributor, Reviewer, Approver, Consumer, Auditor), approval procedures, access control, compliance support (`Knowledge Governance.md`).
4. **Lifecycle state management.** A governed sequence — Proposed → Under Review → Approved → Active → Revised → Deprecated → Retired — with each transition gated by human review activity (`Knowledge Lifecycle.md`).
5. **Independent versioning of the artifact itself.** Knowledge carries its own version history (previous version, author, approval status, change description, timestamp), maintained through governed revision, not through recomputation (`Knowledge.md`, `Knowledge Lifecycle.md`).
6. **Quality management.** Quality dimensions (Accuracy, Completeness, Consistency, Relevance, Timeliness, Traceability, Explainability, Version Integrity), assessment methods, quality indicators, issue tracking (`Knowledge Quality.md`).
7. **Explainability.** What the Knowledge represents, who created/approved it, why it exists, which decisions depend on it (`Knowledge.md`).
8. **Access control and compliance.** Roles, permissions, security classifications, regulatory alignment (`Knowledge Governance.md`).
9. **Optional relationships to other constructs.** Entities, Events, Workflows, Memory Records, Context, AI Agents, Business Rules — all listed as things Knowledge *may* reference (`Knowledge.md`).
10. **The organizational-understanding value itself.** "What an organization knows rather than what happened during a particular execution" (`Knowledge.md`, Definition) — explicitly stated to be independent of individual Memory Records.

---

# 2. Responsibilities That Read as Belonging to World Model

Constitution text gives only two direct constraints on World Model: it is derived from Knowledge (§5), and it must be reconstructable from Memory without access to original external systems (§6). Reasoning from the ordering of the chain and from the term itself ("a model of the current state of the operational world"), the following currently-Knowledge responsibilities read as more naturally belonging to a downstream, computed World Model layer than to Knowledge as "reusable organizational understanding":

- **Live lifecycle status of a specific Knowledge item** (item 4 above) — "is this particular piece of understanding currently in effect" is a question about the current condition of one subject, structurally the same kind of question World Model would answer about any Entity's current state, not a statement of general reusable understanding.
- **Point-in-time quality indicators** (item 6, specifically "conflict count," "version currency," "evidence availability" as *current measured values*) — these are computed readings of present condition, not stable interpretive content.
- **The version currently in force** (part of item 5) — "which version is authoritative right now" is a current-state fact, distinct from the content of any given version.

The following responsibilities read as belonging to Knowledge, not World Model, under the same reasoning — they describe stable, generalizable understanding that does not vary per instance or per moment:

- Semantic content representation (item 1) — the definitions, rules, and taxonomies themselves.
- The interpretive relationship between a rule and the Memory it was drawn from, as a stable statement ("this is what we understand X to mean"), as opposed to any single current application of it.

---

# 3. Responsibilities That Cannot Belong to Both Layers Simultaneously

Four incompatibilities were identified. In each case, the two things named cannot both be true of the same layer at the same time without one of them changing meaning:

**(i) Directly-authored/approved content vs. a fully derived, reconstructable projection.** Constitution §6 requires that Knowledge (and World Model) be reproducible from Memory "without requiring access to the original external systems." `Knowledge Governance.md` and `Knowledge Lifecycle.md` currently describe Knowledge as edited and approved by named humans through a workflow that exists outside Memory. As written, these are not simultaneously satisfiable by one mechanism: either the human approval act is itself captured as Memory (making Knowledge still technically derived, at the cost of treating every approval as a Memory Entry), or Knowledge is not, in fact, purely derived from Memory as currently governed.

**(ii) "Independent of Memory Records" vs. "always derived from Memory."** `Knowledge.md`'s own Definition states Knowledge "is independent of individual AI Agents, Context, and Memory Records." Constitution §5 states the opposite for whatever is called Knowledge. Both cannot be literal statements about the same layer.

**(iii) Instance-specific current state vs. general reusable understanding.** "The current tier of Customer #123" and "what 'Gold Tier' means" are different in kind: one changes every time new Memory arrives about that one subject; the other changes only when the business rule itself changes. A single layer cannot serve both roles without an explicit internal split, because the two have different update cadences and different scopes (one instance vs. all instances).

**(iv) Reconstruction-oriented audit trail vs. accountability-oriented audit trail.** §6's audit concern is "can this be rebuilt from Memory." `Knowledge Governance.md`'s Auditability section ("ownership history; approval history; modification history; version history; access history") answers a different question — "who is accountable for this decision." Both are legitimate, but they are not the same trail, and currently only the second is described anywhere in `AI/Knowledge/*`.

---

# 4. Possible Divisions of Responsibility

The following are distinct, illustrative ways the responsibilities above could be divided between Knowledge and World Model. They are not exhaustive, not evaluated against each other here, and none is recommended.

**Option 1 — Knowledge keeps only stable content; World Model takes all current-state and instance data.** Knowledge retains semantic content representation and the interpretive link back to Memory. Every current-condition responsibility identified in Section 2 — live lifecycle status, point-in-time quality indicators, which version is currently in force — moves to a computed World Model layer, recomputed from Memory and Knowledge rather than stored as a governed field.

**Option 2 — Knowledge is left as currently written; World Model is introduced as an entirely separate, new layer alongside it.** Under this option, `AI/Knowledge/*`'s notion of "Knowledge" is treated as distinct from the Constitution's §5 use of the term — accepting a terminology fork rather than rewriting the existing governance/approval model. World Model is built new, independently, to satisfy §5/§6.

**Option 3 — Human governance is preserved by making the approval act itself Memory-sourced.** Ownership, approval, and lifecycle transitions remain as currently described, but each approval/transition event is captured as an Evidence-backed Memory Entry. Knowledge remains "derived from Memory" in the strict sense because the human decision is now part of Memory before Knowledge is derived from it. World Model is then a separate, later projection built on Memory and Knowledge together, used only for current-state queries.

**Option 4 — A three-way split by time horizon.** Memory records what happened; Knowledge holds why it matters (stable rules and meaning, changed only through a Memory-logged rule-change process, never edited directly); World Model holds what is true right now for a given subject, computed only, with no independent authorship or approval workflow of its own.

---

# Status

This paper records an analysis, not a decision. No specification document has been changed. No ADR Candidate has been created. Resolution — if pursued — belongs to the standard evolution process, on the same terms already used for `AO-003` (Mutable Status in an Immutable Memory Model), to which this paper is a direct continuation.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial concept paper, written from the Knowledge Architecture Assessment (Constitution integration, Stage 3) and `AO-003` |

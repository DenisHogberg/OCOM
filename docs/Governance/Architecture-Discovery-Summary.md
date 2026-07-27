<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Discovery Summary

[← Back](Architecture-Discussion-Knowledge-vs-World-Model.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Discovery Summary

**Document ID:** GOV-DISCOVERY-SUMMARY-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

This document exists to close one specific gap: an independent Committee review of `ADR-Candidates.md#cand-007` found that two of the four evidentiary passes cited there — referred to informally as the "standards-analogy sweep" and the "ecosystem-evolution stress test" — existed only in prior discussion, with no citable record anywhere in the repository. This is that record. It lists conclusions already reached; it does not re-derive them, and it introduces no new analysis, no new architecture, and no new decision. Anything below that reads as a conclusion was already reasoned to before this document was written — this is a transcription, not a fresh pass.

---

# 1. Reasoning-Pipeline Independence

From an analysis of whether independent OCOM implementations (a reference implementation, an autonomous agent, a third-party commercial engine, a BI engine, a rule engine, a digital twin) can each use a different internal reasoning approach and remain fully compatible:

- A conformant implementation may use any internal reasoning pipeline — any order of gathering Objects, Knowledge, Memory, and Evidence, and computing Confidence — provided compatibility is judged by checkable output/behavior at the system's boundary, never by replicating a specific algorithm.
- Every guarantee splits into a mandatory component (a property of the result) and a free component (the mechanism producing it). Examples: Evidence traceability is mandatory; the retrieval algorithm that locates Evidence is free. Confidence must never overstate what its Evidence supports (mandatory); the specific numeric scale or level scheme used is free.
- Reproducibility and reconstructability are mandatory at the level of structural derivation (the same Memory + Evidence must yield the same Knowledge / World Model projection) — not at the level of exact natural-language answer phrasing, which may legitimately vary between valid, equally-grounded expressions.

---

# 2. Minimal Conformance Checklist

The minimum a third party must satisfy to honestly claim "compatible with OCOM," while remaining free to use a different internal algorithm than any other implementation:

1. Retained facts are represented as Memory Entries, immutable after creation; corrections are new entries, never edits (§4, ARCH-001).
2. No fact is asserted without an Evidence Record; Evidence Records are immutable; unknown origin is an explicit, honest state, never silent absence (§3, ARCH-002, ARCH-006).
3. Derived outputs (Knowledge / current state) are reconstructable from Memory + Evidence without access to the original external system (§6).
4. Every output distinguishes evidenced, inferred, and expert-judgment content, and communicates that distinction (§12).
5. Confidence is never claimed higher than its attached Evidence supports, and its basis can be shown (§12, Memory/Confidence.md).
6. Everything managed is expressible as an Object or a specialization of Object (§1).
7. Responsibility remains with the designated human role unless a higher Autonomy level has been explicitly delegated (§14).

Explicitly not required: a specific retrieval algorithm, a specific confidence-scoring scheme, a specific reasoning pipeline, a specific natural-language generation approach, a specific orchestration framework.

---

# 3. Standards-Analogy Findings

Examined for what each mature standard treats as normative versus left to implementers:

| Standard | Normative | Free |
|---|---|---|
| SQL | The result set a given query must produce | Query planner, optimizer, storage engine |
| HTTP | Status-code and method semantics | Server architecture, threading model, language |
| OpenAPI | The endpoint/schema contract | The server implementation entirely |
| Kubernetes | API objects; that a controller drives actual state toward desired state; the CNCF Conformance Program (an executable, checkable test suite third parties must pass to say "Certified Kubernetes") | Scheduler algorithm, specific CNI plugin behavior |
| BPMN | The XML interchange format and its execution semantics | The executing workflow engine's internal architecture |
| RDF | The triple/graph data model and query semantics (SPARQL) | The triple store's internal indexing/reasoning engine |
| Git | *(cautionary counter-example, not a clean split)* — the object model (blobs/trees/commits/refs) is the part that turned out to be portable | For years, "compatible with Git" effectively meant byte-compatible with the `git` binary, because the object model was never cleanly separated from the one shipping implementation at the outset |

**Common pattern, stated as a conclusion:** in every standard examined, the normative part is always the data model, interchange format, or observable interface contract; the free part is always the internal algorithm or execution strategy. Git is the exception that proves the rule by omission — it shows what happens when a specification and its first implementation are never cleanly separated: the implementation becomes the de facto standard by default, and alternate implementations must reverse-engineer behavior rather than follow a contract.

---

# 4. Ten-Year Architect Recommendation

Asked what should be locked into the Specification as an unchangeable contract versus deliberately left to Reader and other implementations, over a ten-year horizon:

**Lock into Specification:** the Object/Memory/Evidence/Knowledge/World Model data model and its invariants; the behavioral guarantees already stated at Constitution level (§12, §14); a Conformance Test Suite (a checkable analogue to the CNCF Kubernetes Conformance Program) — named at the time as not yet existing, and still not existing.

**Leave free:** the reasoning pipeline and its execution order; the specific Confidence-scoring mechanism (only the principle — never overstate beyond Evidence — is fixed); natural-language generation, prompting technique, and LLM choice; a reference implementation's own product ambitions.

**One transfer insight, later load-bearing:** the same test used to justify excluding the reasoning pipeline from the Specification (governed content-management behavior — ownership, approval workflow, independent versioning — is implementation-shaped, not contract-shaped) was subsequently applied to `AI/Knowledge/*` and found to plausibly explain why that section's governance/approval model conflicts with Constitution §5/§6. This is the reasoning that seeded the later Knowledge vs. World Model investigation (`Concept-Paper-Knowledge-vs-World-Model.md`), not a new conclusion introduced by this document — recorded here because it was, until now, findable only in conversation.

---

# Status

This is a record of prior discussion, not a new analysis, decision, or architecture. No specification document has been changed. No ADR Candidate has been created or altered by this document; it exists so that other documents (`CAND-007` among them) can cite something real instead of unrecorded conversation.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial record, transcribing the standards-analogy sweep and ecosystem-evolution stress test conclusions, in response to a Committee-review finding that `CAND-007` cited them without a citable source |

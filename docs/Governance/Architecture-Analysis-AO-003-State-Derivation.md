<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Analysis — AO-003 State Derivation

[← Back](Concept-Paper-Knowledge-vs-World-Model.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Analysis — AO-003: Derived State in an Immutable Memory Model

**Document ID:** GOV-ANALYSIS-AO003-STATE-DERIVATION-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 28 July 2026

**Parent:** `Architecture-Observations.md#ao-003` ("Mutable Status in an Immutable Memory Model")

---

# Purpose

This document is an analytical input to the Chief Architect's review of `AO-003`. It derives a consistent answer to AO-003's open question from the Canonical Principles already adopted in `Core/Constitution.md` (`CAND-006`), without introducing new principles, new Meta Objects, or any change to accepted definitions. It is analytical, not normative — no specification document is changed by this document, and none of its conclusions take effect until reviewed and, if accepted, recorded as a separate Decision through the existing ADR Candidate process.

This work is explicitly within scope of the current Architecture Freeze (`CAND-007`): Section 3 of that Decision names "Decisions on already-open ... Architecture Observations (`AO-001`, `AO-002`, `AO-003`), provided the decision stays within each candidate's already-recorded scope" as a permitted change before v1.0. This document does not propose a redesign of Object, Memory, or Evidence (which Section 4 of `CAND-007` forbids outside Section 5); it proposes a reading of already-adopted principles applied to one already-recorded, already-scoped question.

---

# Background

`AO-003` was logged 27 July 2026 during Constitution integration (Stage 2, Memory/Evidence migration). It found that `Memory Record.md`'s `Status` attribute (`Active`, `Pending Verification`, `Archived`, `Expired`, `Rejected`) has undefined semantics relative to `Core/Constitution.md` §4 (Immutable Memory): is `Status` fixed at record creation (Option A), or a projection computed at read/derivation time from the full append-only sequence of Memory Records for a subject (Option B)?

`Concept-Paper-Knowledge-vs-World-Model.md` is recorded as "a direct continuation" of `AO-003`. Its Option 4 ("a three-way split by time horizon: Memory records what happened; Knowledge holds why it matters; World Model holds what is true right now for a given subject, computed only, with no independent authorship or approval workflow of its own") is the closest existing analysis to the position this document arrives at independently below. This document treats that Option 4 as already-recorded prior art, not as something it introduces.

---

# Existing Constitutional Principles (verbatim, `Core/Constitution.md`)

| # | Principle | Text |
|---|---|---|
| 3 | Evidence Before Belief | "Every operational fact must be traceable to Evidence. Evidence and Metadata are independent concepts and must never be merged." |
| 4 | Immutable Memory | "Memory is append-only. A Memory Entry is immutable after creation. Corrections are represented as new Memory Entries, never by modifying historical records." |
| 5 | Memory Precedes Knowledge | "Knowledge is always derived from Memory. World Models are always derived from Knowledge. Memory → Knowledge → World Model." |
| 6 | Reconstructability | "Knowledge and World Models must always be reproducible from Memory without requiring access to the original external systems." |
| 12 | Grounded Reasoning | "Statements derived from Memory and Knowledge must remain distinguishable from interpretation, inference or expert opinion. The system must communicate provenance and confidence appropriately." |

Also relevant, `Memory/Memory Record.md` (Memory-02): `Status` is currently listed as a **Mandatory Attribute** (§ Mandatory Attributes) with example values given (§ Status) but no stated transition rule. Separately, **`Memory Type` already enumerates `Decision` as one of ten record types** (Fact, Observation, Decision, Preference, Rule, Relationship, Summary, Inference, Prediction, Exception) — a Memory Record asserting a decision is already a recognized, existing case, not a new concept.

---

# Problem Statement

Under Option A, `Status` transitions (e.g., `Pending Verification → Active`) require modifying an existing Memory Record's field — which is disallowed by §4 read literally. Under Option B, "current status" is not stored on any single record; it is computed from the ordered set of all Memory Records about a given Subject. §4 and Option A cannot both be true of the same field. §5 and §6 are only satisfiable under Option B, or under Option A modified so that every status transition is itself a new Memory Record (which is Option B in substance, differently worded).

---

# Formal Analysis

**1. Identity and Subject are stable; Value and Status are not.** `Memory Record.md` already separates `Identity` (of the record itself — stable) from `Subject` (what the record is about) from `Value` (what is asserted). Nothing in the current text requires the *Subject's* state to be stable — only the record's own identity. This removes the apparent tension: §4's immutability is a property of the **record**, never of the **subject it describes**. A subject's state is expected to evolve; that is the entire reason Memory accumulates records about it.

**2. "Current Status" is a query over Memory, not an attribute of one record.** Given §5 (Memory → Knowledge → World Model) and §6 (Reconstructability), the only formulation of "current Status" consistent with both is:

```text
CurrentStatus(Subject) = f( ordered sequence of Memory Records where Subject = Subject )
```

where `f` selects the most recent record whose content asserts a Status value for that Subject, subject to Confidence and Governance (§12, `Memory Record.md` § Governance) having reached whatever threshold the deployment's Governance configuration requires. This is exactly Option B, and it requires no new Meta Object: a Memory Record whose `Memory Type` is `Fact`, `Observation`, or `Decision` and whose `Value` asserts a Status is already a fully described case under the existing `Memory Record.md` text.

**3. No new primitive is required to resolve this.** During this analysis, a broader design (introducing a distinct `Change` object, atomic per-property mutation records, split `change_confidence`/`value_confidence`, and a `Conflict` object for competing Memory Records about the same Subject) was explored in detail outside this repository. None of it is required to answer AO-003 as recorded. `Memory Record` already is the append-only atomic unit (§4); `Decision` is already an enumerated `Memory Type`; `Evidence` and `Confidence` are already mandatory/optional fields on every record (§ Evidence, § Confidence). AO-003's question is answerable entirely by clarifying how `Status` is *read*, not by adding anything to what is *written*.

**4. What genuinely is not yet covered.** `Memory Record.md`'s current `Confidence` and `Governance` sections address one record's own reliability, not what happens when two Memory Records about the same Subject assert **different** Status values with neither superseding the other in time (e.g., two sources reporting simultaneously). This is a real gap, distinct from AO-003 as recorded, and is named in Open Questions below rather than answered here.

---

# Derived Consequences

| Constitution Principle | Architectural Consequence |
|---|---|
| Evidence Before Belief (§3) | A Memory Record asserting a new Status is not itself sufficient to change `CurrentStatus(Subject)` until its required Evidence reference is present. |
| Immutable Memory (§4) | `Status` is never edited on an existing Memory Record. A status change is always a new Memory Record. |
| Memory Precedes Knowledge (§5) | `CurrentStatus(Subject)` is a Knowledge-layer (or World-Model-layer, per the still-open Concept Paper) computation, never a Memory-layer stored field in the sense of being independently authored. |
| Reconstructability (§6) | `CurrentStatus(Subject)` must be re-derivable at any time from the Memory Record sequence alone — no separate, independently-maintained status store may become the source of truth. |
| Grounded Reasoning (§12) | Any computed `CurrentStatus(Subject)` must remain traceable to the specific Memory Record(s) and Evidence it was derived from — an implementation must be able to answer "why do we believe this is the current status," not only report the value. |

---

# Alternative Models

| Model | Pros | Cons |
|---|---|---|
| **A — Mutable Status field** (edit `Status` in place on the existing Memory Record) | Simplest to implement; matches naive CRUD intuition | Directly violates §4 (Immutable Memory) as literally written; loses the history of prior statuses entirely |
| **B — Derived Status** (computed from the Memory Record sequence at read time, no independent status store) | Fully consistent with §4, §5, §6 as adopted; no new Meta Object; matches Concept Paper Option 4 | More expensive to compute at scale without a materialized cache; requires a defined selection rule (`f` above) that does not exist in text today |
| **C — Snapshot/materialized cache of Status, regenerable from Memory** | Same consistency as B in principle, with better read performance | Reintroduces a second store that must be explicitly documented as non-authoritative and regenerable, or it risks being treated as source of truth by implementers — a documentation, not architectural, risk |

Model B is the constitutionally minimal answer. Model C is an implementation strategy for realizing Model B efficiently, not a competing architectural answer — both derive the same value; C only caches it.

---

# Recommendation

**Accept AO-003 in the direction of Option B (Derived Status), refined as Model B/C above.** This does not require a new Canonical Principle, a new Meta Object, or a redefinition of any adopted principle — it requires only:

1. A Chief Architect Decision on `AO-003` itself, recorded through the existing ADR Candidate process, adopting Option B as the resolution.
2. A bounded, in-scope clarification to `Memory Record.md`'s `Status` section, stating explicitly that Status is computed, not stored-and-edited, and naming the selection rule at whatever level of precision the Chief Architect judges appropriate. This is a clarification of already-adopted principles applied to an already-Mandatory field — not a new principle.

**Not recommended for the Specification:** the richer apparatus explored alongside this analysis (a distinct `Change` object type, `Conflict` as a new Meta Object, split confidence fields, concrete field-level schemas). Per Architecture Principle 1 ("Specification Defines Contracts, Not Products") and Architecture Principle 5 ("Reader Is Reference, Not Authority"), this material reads as implementation-shaped rather than contract-shaped, and none of it is required to resolve AO-003 as recorded (see Formal Analysis, point 3). The existing precedent for this exact situation is `CAND-006` itself, whose own Related Documents note that its empirical grounding was "substantially developed in the implementation repository [OCOM-Reader] rather than purely within the Specification itself" (via `ADR-007`, `RF-001`). The same path is recommended here: if the richer model proves useful, it should be developed and tested as a Reference Case in an implementation repository (Reader or Vector), and only returned to the Specification as a future ADR Candidate if it survives that contact with real implementation — not adopted directly from this analysis.

---

# Open Questions

1. What is the precise selection rule `f` when more than one Memory Record about the same Subject asserts a Status, with neither dominating by time or by an existing Governance decision? This is the "Multiple Truths" case explored outside this repository; `Memory Record.md`'s current Confidence/Governance sections do not yet name a rule for it. Not resolved here — recommended as a distinct, future Reference Case rather than folded into the AO-003 decision.
2. Does resolving AO-003 as Option B also resolve, or merely narrow, `Concept-Paper-Knowledge-vs-World-Model.md`'s four-way division of Knowledge vs. World Model responsibilities? This analysis addresses only the Status/CurrentStatus question; the Concept Paper's broader scope (lifecycle governance, quality indicators, versioning-in-force) is not evaluated here.
3. Should `Memory Type: Decision` be given its own worked example in `Memory Record.md`, given that AO-003, this analysis, and the Concept Paper all use "decision" as a central case, yet no existing document shows a concrete Decision-typed Memory Record?

---

# Status

This document records an analysis, not a decision. No specification document has been changed by it. Resolution — if pursued — belongs to the standard evolution process (`Standard Evolution Methodology.md`): this analysis as input to a Chief Architect Decision on `AO-003`, recorded in `ADR-Candidates.md`, exactly as `CAND-006` and `CAND-007` were.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 28 July 2026 | Initial analysis, prepared as architectural input to `AO-003` |

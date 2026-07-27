<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Discussion — Knowledge vs World Model

[← Back](Concept-Paper-Knowledge-vs-World-Model.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Discussion — Knowledge vs World Model

**Document ID:** GOV-DISCUSSION-KNOWLEDGE-WORLDMODEL-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

This document prepares the ground for an eventual ADR Candidate on the relationship between Knowledge and World Model. It does not decide anything, does not change any specification document, and is not itself an ADR Candidate. It draws only on the OCOM Constitution v1.0, `AO-003`, `Concept-Paper-Knowledge-vs-World-Model.md`, `AI/Knowledge/*`, and `Memory/*`. Its purpose is that a Chief Architect can read this single document and write the corresponding ADR without re-reading the discussion history that produced it.

---

# 1. Problem Statement

**What was found:** `AI/Knowledge/*` describes Knowledge in terms that conflict with Constitution §5 (Memory Precedes Knowledge) and §6 (Reconstructability). `Knowledge.md`'s own Definition states Knowledge "is independent of individual AI Agents, Context, and Memory Records" — the literal opposite of §5's "Knowledge is always derived from Memory." Separately, `Constitution.md` §5 names a third stage — World Model — as the layer derived from Knowledge; no document anywhere in the Specification defines or implements World Model.

**Where it was found:** `AI/Knowledge/Knowledge.md` (Definition, Relationships), `AI/Knowledge/Knowledge Sources.md` (Source Categories — Memory is absent), `AI/Knowledge/Knowledge Governance.md` and `AI/Knowledge/Knowledge Lifecycle.md` (ownership, approval workflow, independent version history), `AI/Knowledge/Knowledge Quality.md` ("unsupported Knowledge" named as an ordinary, manageable quality issue rather than a structural impossibility). Documented in full in the Knowledge Architecture Assessment (Constitution integration, Stage 3) and `Concept-Paper-Knowledge-vs-World-Model.md`.

**Why a simple migration cannot resolve it:** The Memory/Evidence migration (Stage 2) succeeded because Memory Record and Evidence Record were already modeled as single, well-defined constructs, and the Constitution supplied an unambiguous replacement wording for each contradiction (`"may reference"` → `"shall reference"`, immutability language). Knowledge has no equivalent single point of correction. Its governance, approval, lifecycle, and independent-versioning responsibilities form one internally consistent model (a governed content artifact), and being "always derived from Memory" and "reconstructable without external systems" (§5, §6) implies a different, incompatible model (a computed projection). Correcting the wording in `Knowledge.md` alone, without deciding what happens to approval workflows, ownership, and independent version history, would leave the rest of the section contradicting whatever new wording was introduced. There is also no existing document to receive whatever responsibilities turn out not to belong to Knowledge, because World Model does not exist as a document.

---

# 2. Architectural Context

The following already-decided positions are what make this question visible; none of them, individually, decided it.

- **Constitution §3 — Evidence Before Belief.** Every operational fact must be traceable to Evidence. Completed for Memory via ARCH-002 (Memory Record now `shall reference at least one Evidence Record`; `Evidence Sources` includes `unknown source`). Raises the question of whether Knowledge — as a construct built from Memory — inherits the same requirement. It currently does not: `Knowledge Quality.md` treats evidence as an optional quality indicator, and explicitly names "unsupported Knowledge" as an ordinary, manageable issue rather than a disallowed state.
- **Constitution §4 — Immutable Memory**, realized as **ARCH-001**. Memory Entries are append-only; corrections are new entries, never edits. Establishes the pattern "state change = new record, not mutation" at the Memory layer. This pattern is the direct point of comparison for `Knowledge Lifecycle.md`'s Status field (`Proposed → ... → Retired`), which is currently a directly-set, governed attribute — the same shape of construct §4/ARCH-001 already required to change for Memory Record.
- **Constitution §5 — Memory Precedes Knowledge.** States the chain directly: Memory → Knowledge → World Model. This is the principle `Knowledge.md`'s Definition contradicts in as many words.
- **Constitution §6 — Reconstructability.** Requires Knowledge and World Model to be reproducible from Memory "without requiring access to the original external systems." This is the principle under the most direct strain from `Knowledge Governance.md`'s human approval workflow: an approval decision is, as currently described, an external input not captured anywhere as Memory.
- **ARCH-006 — Evidence Immutability.** Extended the §4 append-only pattern from Memory Entries to Evidence Records, on the reasoning that Evidence Overlay is itself part of the Memory Specification (`Memory/Overview.md`). Establishes precedent that append-only reasoning propagates to adjacent constructs once they are shown to be part of the same specification family — directly relevant to whether the same reasoning should propagate further, to Knowledge and to a Current Status construct.
- **AO-003 — Mutable Status in an Immutable Memory Model.** Found that Memory Record's own `Status` attribute (`Active`, `Pending Verification`, `Archived`, `Expired`, `Rejected`) has undefined semantics under append-only Memory: is it a fixed-at-creation record field, or a Knowledge/World-Model-layer derived projection? Recorded as open, unresolved, explicitly deferred.

Read together, these already-decided positions establish an append-only historical log at the base (Memory, then Evidence) and require everything above it to be reconstructable from that log. None of them decided what Knowledge or World Model themselves are. AO-003 is the point at which this gap first became visible, inside Memory Record alone. The Knowledge Architecture Assessment and the Concept Paper found the same underlying gap recurring one layer up, inside Knowledge Lifecycle's own Status field, and additionally found that the layer named by §5 to hold current, derived state — World Model — has no document at all. This discussion is the next link in that same chain, not a new, unrelated question.

---

# 3. Existing Responsibilities

## Knowledge

Responsibilities currently defined in `AI/Knowledge/*`:

| # | Responsibility | Source |
|---|---|---|
| 1 | Semantic content representation (business concepts, policies, rules, taxonomies, classifications, definitions, best practices) | `Knowledge.md`, Knowledge Types |
| 2 | Provenance/origin classification in business terms (Organizational Documentation, Domain Experts, Regulatory Requirements, etc.) | `Knowledge Sources.md` |
| 3 | Human governance and approval (ownership, roles, approval procedures, access control, compliance) | `Knowledge Governance.md` |
| 4 | Lifecycle state management (`Proposed → Under Review → Approved → Active → Revised → Deprecated → Retired`) | `Knowledge Lifecycle.md` |
| 5 | Independent versioning of the Knowledge artifact itself (previous version, author, approval status, change description) | `Knowledge.md`, `Knowledge Lifecycle.md` |
| 6 | Quality management (dimensions, assessment methods, indicators, issue tracking) | `Knowledge Quality.md` |
| 7 | Explainability (what it represents, who created/approved it, why it exists, dependent decisions) | `Knowledge.md` |
| 8 | Access control and compliance | `Knowledge Governance.md` |
| 9 | Optional relationships to Entities, Events, Workflows, Memory Records, Context, AI Agents, Business Rules | `Knowledge.md`, Relationships |
| 10 | The organizational-understanding value itself ("what an organization knows"), stated independent of Memory Records | `Knowledge.md`, Definition |

## World Model

No document defines World Model. The table below separates what the Constitution states explicitly from what is inferred by the reasoning in the Concept Paper; both are marked accordingly.

| # | Responsibility | Basis |
|---|---|---|
| 1 | Is derived from Knowledge | Explicit — Constitution §5 |
| 2 | Must be reconstructable from Memory without access to original external systems | Explicit — Constitution §6 |
| 3 | Represents current, instance-specific state (e.g., the present condition of a specific subject), as distinct from stable general understanding | Inferred — Concept Paper §2, from the term "World Model" and its position as the final stage of the chain |
| 4 | Holds point-in-time computed values (e.g., which version of a rule is currently in force, current lifecycle condition of a specific item) | Inferred — Concept Paper §2 |
| 5 | Has no independent authorship or approval workflow of its own; is computed, not directly edited | Inferred — Concept Paper §4, Option 4; follows from "derived" but not stated as a requirement anywhere |

---

# 4. Points of Tension

- **Authoritative document vs. Derived projection** — `Knowledge.md` describes Knowledge as governed content with its own authority (owner, approval); §5/§6 describe it as computed output of Memory.
- **Approval workflow vs. Reconstructability** — `Knowledge Governance.md`'s human approval step is an input from outside Memory; §6 requires reconstruction from Memory alone, without external systems.
- **Human ownership vs. Derived state** — Knowledge Governance assigns accountability (an owner responsible for accuracy, maintenance, retirement) to something §5 describes as an automatic consequence of Memory.
- **Version history vs. Replay** — Knowledge maintains its own independent version history (`Knowledge.md`, `Knowledge Lifecycle.md`); a purely derived construct would not need its own version history, only the ability to be recomputed (replayed) from Memory at any point.
- **Current status vs. Historical log** — `Knowledge Lifecycle.md`'s Status field is a live, current-condition attribute; Memory (§4, ARCH-001) is an append-only historical log. This is the same tension AO-003 raised for Memory Record, recurring at the Knowledge layer.
- **Business-category provenance vs. Addressable provenance** — `Knowledge Sources.md` names origins as business categories (e.g., "Domain Experts," "Regulatory Requirements"); Evidence (§3, ARCH-002, ARCH-006) is a specific, addressable, immutable record. It is not established whether these are the same kind of provenance or two unrelated notions of "source."

No resolution to any of these is discussed here.

---

# 5. Questions for Architect

- Может ли Knowledge существовать независимо от Memory?
- Где должен жить Current Status — в Memory, в Knowledge, или в World Model?
- Что именно означает "World Model" в этой спецификации, помимо двух формулировок Constitution §5 и §6?
- Является ли Knowledge частью World Model, слоем, ему предшествующим, или отдельной, параллельно управляемой сущностью?
- Может ли производный (derived) объект одновременно иметь собственный approval workflow?
- Если approval — это событие, должно ли оно фиксироваться как Memory Entry, чтобы Knowledge оставалась производной в строгом смысле §5?
- Относится ли Lifecycle Status в Knowledge к тому же явлению, что и Status в Memory Record (AO-003), или это два структурно разных вопроса?
- Может ли один и тот же слой одновременно быть "общим переиспользуемым пониманием" и "текущим состоянием конкретного экземпляра", или это требует структурного разделения на два слоя?
- Что происходит с текущей моделью `Knowledge Sources` (провенанс в бизнес-терминах), если Knowledge должна трассироваться до Evidence в том же смысле, что и Memory Record?

No answers are proposed.

---

# 6. Possible Directions

Carried over from `Concept-Paper-Knowledge-vs-World-Model.md`, Section 4, unchanged. Not ranked. Not evaluated against one another here.

**Option 1 — Knowledge keeps only stable content; World Model takes all current-state and instance data.** Knowledge retains semantic content representation and the interpretive link back to Memory. Every current-condition responsibility — live lifecycle status, point-in-time quality indicators, which version is currently in force — moves to a computed World Model layer, recomputed from Memory and Knowledge rather than stored as a governed field.

**Option 2 — Knowledge is left as currently written; World Model is introduced as an entirely separate, new layer alongside it.** `AI/Knowledge/*`'s notion of "Knowledge" is treated as distinct from the Constitution's §5 use of the term, accepting a terminology fork rather than rewriting the existing governance/approval model. World Model is built new, independently, to satisfy §5/§6.

**Option 3 — Human governance is preserved by making the approval act itself Memory-sourced.** Ownership, approval, and lifecycle transitions remain as currently described, but each approval/transition event is captured as an Evidence-backed Memory Entry. Knowledge remains "derived from Memory" in the strict sense because the human decision is now part of Memory before Knowledge is derived from it. World Model is a separate, later projection built on Memory and Knowledge together, used only for current-state queries.

**Option 4 — A three-way split by time horizon.** Memory records what happened; Knowledge holds why it matters (stable rules and meaning, changed only through a Memory-logged rule-change process, never edited directly); World Model holds what is true right now for a given subject, computed only, with no independent authorship or approval workflow of its own.

---

# 7. Open Questions

Matters this discussion does not resolve or investigate:

- Whether the implementation repository (OCOM Reader) already contains a de facto precedent for this split, in the way `ADR-007` (Memory Before Knowledge) preceded and informed Decision 1 for Memory.
- How many other parts of the Specification implicitly depend on the current, governance-centric model of Knowledge, and would require rework under any of the four Options.
- Whether the same tension (governed artifact vs. derived projection) extends to other `AI/*` sections not examined here (Context, Agents, Tools, Evaluation).
- Whether "World Model" has any meaning beyond the two Constitution sentences that name it — no other document in the Specification elaborates the term.

---

# 8. Decision Readiness

**Да.**

The problem is bounded (Section 1), grounded in already-decided Constitution principles and ARCH decisions rather than new speculation (Section 2), the responsibilities on both sides are enumerated (Section 3), the tensions are named concretely (Section 4), and a set of distinct, comparable options already exists in the same Option-A/B/C/D format used for every prior ARCH decision in this repository (Section 6). Nothing remains to be discovered before a choice can be made; the Open Questions (Section 7) are exploratory context, not blocking prerequisites, in the same way the `Domains/` boundary was left as an ongoing discipline rather than a blocker for Decision 4.

The one scope note for the architect, not a readiness blocker: unlike ARCH-001 through ARCH-006, which resolved the semantics of an already-modeled construct, this decision additionally requires defining World Model as a concept for the first time, since no prior document establishes one. The decision is accordingly closer in weight to a Core-shaping decision than to a routine ARCH resolution, and should be made with that in mind.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial discussion document, prepared from `AO-003`, the Knowledge Architecture Assessment, and `Concept-Paper-Knowledge-vs-World-Model.md` |

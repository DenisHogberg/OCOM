<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Audit — Current State

[← Back](Architecture-Principles.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Audit — Current State of the OCOM Specification

**Document ID:** GOV-ARCHITECTURE-AUDIT-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

This is an independent architectural inventory of the OCOM Specification as it stands today. It proposes no new architecture, resolves no open question, and creates no ADR Candidate. Every claim below is grounded in direct inspection of the repository (file counts, `Document ID` / `Status` / `Version` headers, explicit incompleteness markers, and cross-reference checks) plus the record of decisions already made in `Governance/`. Where a finding is new (not previously logged as an AO/ADR), this is stated explicitly.

---

# Part 1 — Map of the Specification

| Section | Purpose | Main objects | Links to other sections | Completeness |
|---|---|---|---|---|
| `Core/` | Foundational manifest, principles, governance rules, Constitution | Constitution, Manifest, Principles | Referenced by everything | Constitution complete; Principles/Manifest integrated with Constitution (Stage 1); Modeling-Rules/Naming/Terminology/Versioning not re-verified against Constitution |
| `Meta/` (15 docs) | Universal architectural primitives | Object, Identity, Metadata, Relationship, Capability, Contract, Policy, Constraint, Classification, Ownership, Reference, Registry, Organization | Declared foundation for Core, Models, Entities, Lifecycles, Memory, AI, Domains | Object.md Constitution-linked; the other 13 substantive docs are not |
| `Models/` (9 docs) | Meta-model instantiated for business modeling | Entity, Domain, Relationship, Event, Lifecycle, State, Workflow, Model | Entity.md declares itself a specialization of Object (Meta) | Functionally complete; only Entity.md cross-references Meta explicitly |
| `Memory/` (7 docs) | Operational memory: recording, evidence, confidence | Memory Record, Evidence Overlay, Confidence, Overview | Declared consumer of Meta/Object; consumed by AI/*, Domains/* | Migrated to Constitution §3/§4/§6 + ARCH-001/002/006 (Stage 2); internally consistent |
| `Language/` (11 docs) | Notation, vocabulary, syntax, serialization, validation, conformance | Vocabulary, Syntax, Notation, Schema, Serialization, Validation, Conformance | Declared representation layer for Meta, Core, Models, Entities, Lifecycles, Memory, AI, Domains | Functionally complete; never checked against Constitution or Stage 1/2 changes |
| `Lifecycles/` (7 docs) | Generic, reusable lifecycle patterns | Commercial, Content, Financial, Operational, Organizational Lifecycle | References "AI Agent" without defining it locally | Functionally complete; zero "Relationship to Other Specifications" sections anywhere in this directory |
| `Reference Architecture/` (8 docs) | Illustrative composition of the above into architecture views | Enterprise-, Object-, Domain-, AI-, Operational-Memory-, Business-Event-Architecture | Explicitly `Status: Informative`; internal cross-linkage only | Coherent, correctly non-normative; predates Stage 1/2 migrations, not re-verified since |
| `Domains/` (154 docs, 14 subdomains) | Business-domain boundaries and their capabilities/events/KPIs/policies | Domain, plus 9 files per subdomain (AI, Capabilities, Events, KPIs, Lifecycles, Objects, Policies, Processes, Relationships) | Memory/Evidence linkage present in 8/14 subdomains via a boilerplate "AI Memory" section; absent in 6 | `Domains/Common/Domain.md` duplicates `Models/Domain.md` with a different definition (AO-001, still open) |
| `Entities/` (51 docs, 24 entity types) | Catalog of standard business entities | Player, Payment, Wallet, Campaign, Affiliate, Employee, AI-Agent, etc. | Almost no reference to Memory/Evidence/Knowledge/Constitution anywhere (1 incidental hit across 51 files) | 23/24 entities have content; `Department` is an explicit empty stub |
| `Examples/` (15 docs) | Worked, non-normative examples | 12 iGaming example objects (Player, Wallet, KYC Case, Fraud Case, etc.) | Explicitly subordinate to the normative Specification | Only 1 of 6 industry collections promised in `Overview.md` (FinTech, Healthcare, iGaming, Manufacturing, Marketplace, SaaS) actually exists |
| `Adoption/` (5 docs) | Onboarding on-ramp | Getting Started, First Pilot, FAQ, Common Mistakes | Explicitly a restatement of Core/Meta/Models/`Specification/`; points to `Specification/01 Introduction.md` as "the actual entry point" | Coherent, but routes newcomers to a pre-Constitution document set |
| `Specification/` (10 docs) | Editorial compilation of v0.1 into a single 9-chapter reading path | Chapters 00–08, Committee Review Package | Explicitly "an editorial layer, not a new specification"; cites `Core/`, `Meta/`, `Models/`, `Language/`, `Governance/` (v0.1) | Approved 22 July 2026 — **before Constitution v1.0 (26–27 July) existed.** Contains no mention of Constitution, ARCH-001/002/006, or Stage 1/2 |
| `AI/Knowledge/` (5 docs) | Persistent organizational understanding | Knowledge, Knowledge Sources, Lifecycle, Governance, Quality | Declared derived from/related to Memory; **its own text states the opposite** | Functionally rich, architecturally self-contradictory (see Part 5) |
| World Model | The stage Constitution §5 names after Knowledge | — | Declared derived from Knowledge (§5); reconstructable from Memory (§6) | **No document exists.** Named twice, defined nowhere |
| `AI/Agents/` (7 docs) | AI Agent as a governed, identity-bearing entity | Agent, Agent Lifecycle, Agent Roles, Multi-Agent Collaboration, Context | Interacts with Entities, Memory, Knowledge, Context, Tools (per its own text) | Identity/governance model complete; `Context.md` is a near-verbatim duplicate of `AI/Context/Overview.md` (OBS-001, still open) |
| `AI/Context/`, `AI/Prompts/`, `AI/Tools/`, `AI/Evaluation/` (26 docs) | Context assembly, prompt construction, tool invocation, quality evaluation for AI operations | Context, Prompt, Tool, Evaluation and their Lifecycle/Governance sub-docs | Reference Memory/Knowledge only in prose enumeration, never by cross-reference; zero Constitution mentions anywhere in these 4 directories | Each internally coherent for its own narrow scope |
| `AI/Memory/` (1 doc) | Placeholder | — | Points to top-level `Memory/` | Explicit empty placeholder, honestly labeled |
| `Governance/` (16 docs incl. this one) | The process by which the Specification changes | ADR Candidates, Architecture Observations, Constitution, Concept Papers, Architecture Principles, this Audit | Governs changes to every other section | The methodology itself is proven (used successfully across CAND-001…006, AO-001…003, OBS-001…003); its content backlog legitimately contains multiple still-open items by design |
| `Workflows/` (11 docs) | Concrete business-process workflow specifications | Registration, First-Deposit, Withdrawal, Fraud-Investigation, etc. | Would sit atop Entities/Domains | **100% placeholder** — every file states "Planned for future versions," none contain content |
| Conformance (cross-cutting) | Verifiable proof of OCOM compatibility | — | Named as a need by `Language/Conformance.md` (conceptual) and Architecture Principle 6 (explicit gap) | **No executable/checkable test suite exists anywhere in the repository** |

Two categories named in the prompt's example list do not exist in this repository and are noted for completeness: **"Profiles"** (no such directory or concept found anywhere) and **"Reader references"** (the string "Reader"/"OCOM Reader" appears only inside three `Governance/` analysis documents written during this engagement — `Architecture-Discussion-Knowledge-vs-World-Model.md`, `ADR-Candidates.md`, `Constitution-Step0-Summary.md` — never in any normative Specification document).

---

# Part 2 — Maturity Assessment

Scale: **Draft** (exists, not yet verified for internal or Constitution consistency) → **Partial** (functionally coherent, but has a known unresolved gap, duplication, or missing cross-reference) → **Stable** (internally consistent and verified against Constitution) → **Mature** (Stable, plus proven by repeated successful use).

| Section | Rating | Why |
|---|---|---|
| Constitution | **Mature** | Ratified as v1.0 via a recorded Decision (CAND-006), integrated into Core, internally verbatim-verified (Review 1 of Stage 1) |
| Memory / Evidence / Confidence | **Stable** | Migrated against §3/§4/§6 and ARCH-001/002/006; verified line-by-line during Stage 2; only residual issue (AO-003) is explicitly logged and scoped |
| Meta/Object | **Stable** | Constitution-linked (§1), consistent with Models/Entity's specialization claim, consistent with the Object/Entity Step-0 decision (ARCH-003) |
| Governance (methodology) | **Mature** | The ADR/AO/Reference-Case pipeline has been used successfully and consistently across at least 9 recorded items (CAND-001–006, AO-001–003) over multiple weeks |
| Core/Manifest, Core/Principles | **Stable** | Explicitly reconciled with Constitution in Stage 1 (verified, corrected, re-verified) |
| Meta (non-Object docs) | **Partial** | Individually coherent, foundational per their own Overview, but never checked against Constitution the way Object was |
| Models/ | **Partial** | Functionally complete; structurally asymmetric (only Entity.md has a cross-reference section); generic unelaborated "future versions" boilerplate in nearly every file |
| Language/ | **Partial** | Complete-looking and declared foundational for Memory and AI, but never audited since Constitution or Stage 1/2 |
| Lifecycles/ | **Partial** | Functionally complete, but zero cross-referencing to any other section; references "AI Agent" without local definition |
| Reference Architecture/ | **Partial** | Coherent, correctly self-labeled Informative, but predates Stage 1/2 and not re-verified since |
| Domains/ | **Partial** | Uniform template and metadata; uneven execution (6/14 subdomains missing the Memory-linkage section the pattern implies); carries the still-open Domain/Domain duplication |
| Entities/ | **Partial** | Rich, near-complete catalog (23/24), but structurally disconnected from Memory/Evidence/Knowledge — almost no linkage exists |
| `AI/Knowledge/` | **Draft**, actively contradictory | Its own text ("independent of Memory Records") contradicts Constitution §5; formally assessed and left at "Requires Architecture Decision" (Concept Paper, Architecture Discussion) |
| World Model | **Below Draft** | Does not exist as a document; two Constitution sentences are its entire specification |
| `AI/Agents/` | **Partial** | Coherent identity/governance model; carries the live OBS-001 duplication with `AI/Context/Overview.md`; never touched by Constitution integration |
| `AI/Context/`, `AI/Prompts/`, `AI/Tools/`, `AI/Evaluation/` | **Draft** | Each is an internally coherent island; none reference Constitution; their stated relationship to Knowledge/Memory is prose-only |
| `Specification/` (v0.2) | **Draft, stale** | Explicitly non-normative editorial layer; approved before Constitution existed; not updated since |
| `Adoption/` | **Partial** | Coherent onboarding content; propagates the staleness of `Specification/` by routing newcomers there |
| `Examples/` | **Partial** | One complete, correctly-scoped worked example; 5 of 6 promised industry collections silently absent |
| `Workflows/` | **Draft (not started)** | 100% placeholder, honestly labeled |
| Conformance | **Draft (not started)** | No test suite; named explicitly as a gap by Architecture Principle 6 |

---

# Part 3 — Architectural Dependencies

**Foundation layer:** `Meta/Object` (Constitution §1) — every managed concept is a specialization of Object. `Language/` and `Meta/` (beyond Object) are cross-cutting infrastructure declared to underlie every other layer (representation and primitives, respectively), not a layer "above" Memory.

**Second layer, built on the foundation:** `Memory/` (Entries, Evidence, Confidence) — depends on Object (a Memory Entry's Subject is an Object/Entity) but is otherwise self-contained and, per Stage 2, internally consistent.

**Third layer, built on the foundation, largely NOT wired to the second:** `Models/`, `Entities/`, `Domains/` — Entity is a declared specialization of Object (Models/Entity.md), but almost none of these documents reference Memory/Evidence at all (Entities/: ~0 links; Domains/: partial, 8/14 subdomains).

**Fourth layer, contested position:** `AI/Knowledge/` is specified by Constitution §5 to be *derived from* Memory (third layer sits below it in the intended graph) — but as currently written, Knowledge declares itself *independent of* Memory Records. Its actual position in the dependency graph, as written, does not match its intended position, as specified. This mismatch is the root of Part 5's most critical finding.

**Fifth layer, absent:** World Model is specified to be derived from Knowledge (§5) and reconstructable from Memory (§6) — its dependencies are named, but since it has no content, nothing can be verified as correctly "built on" it.

**Sixth layer, built assuming the fourth and fifth are solid:** `AI/Agents/`, `AI/Context/`, `AI/Prompts/`, `AI/Tools/`, `AI/Evaluation/` all reference Knowledge/Memory in their own text as things an Agent consumes. Because the fourth layer is self-contradictory and the fifth doesn't exist, everything in this sixth layer that presumes a working Memory→Knowledge→World Model chain is standing on an incomplete foundation, even though each document is internally coherent on its own.

**Outside the graph, governing it:** `Governance/` is the process by which the graph changes, not a node within it.

**Above the graph, re-narrating it:** `Specification/` (v0.2) and `Adoption/` are presentation layers that do not add new dependencies — they restate existing ones. Because `Specification/` was frozen before Constitution existed, it currently re-narrates a version of the graph one generation out of date. `Reference Architecture/` and `Examples/` are the same kind of layer, correctly marked non-normative.

**Cannot be considered complete until lower layers are complete, by direct consequence of the above:**

- `AI/Knowledge/` cannot be resolved without resolving its relationship to Memory (already known — Concept Paper).
- Any Conformance Test Suite for guarantees above the Memory/Evidence layer cannot be meaningfully designed while Knowledge/World Model remain unresolved — there is nothing stable yet to test.
- `AI/Agents/`'s Explainability and Relationships sections, and all four of `AI/Context/`, `Prompts/`, `Tools/`, `Evaluation/`, cannot be verified as Constitution-consistent until the fourth/fifth layers they lean on are settled.
- Domains'/Entities' Memory-linkage cannot be completed uniformly while the third layer itself carries an unresolved foundational term duplication (Domain vs Domain, AO-001).

---

# Part 4 — Contract Sufficiency

For each section: could an independent team implement it correctly from the written text alone, without Reader or any other implementation?

| Section | Yes / Partially / No | Reason |
|---|---|---|
| Constitution | **Yes** | Canonical Principles are stated as testable MUST/SHOULD claims; verified directly in Stage 1 |
| Meta/Object | **Yes** | Proven — every downstream layer that references Object does so consistently |
| Memory / Evidence / Confidence | **Yes** | Directly tested in the "five years without Reader" analysis; this layer is genuinely self-sufficient |
| Meta (other docs) | **Partially** | Individually clear, but never checked for Constitution consistency — an implementer would have to guess whether they are still authoritative as written |
| Models/Entities | **Partially** | Clear attribute-level contract; zero contract for how an Entity connects to Memory/Evidence, so an implementer would have to invent that bridge themselves |
| Domains | **Partially** | Clear template; the Domain/Domain duplication means an implementer would not know which of two definitions is authoritative |
| `AI/Knowledge/` | **No** | Following the written contract literally produces a system that violates Constitution §5/§6 — worse than insufficient, actively wrong |
| World Model | **No** | Nothing to implement |
| `AI/Agents/` (identity/governance) | **Partially** | Identity/lifecycle/governance attributes are clear; Explainability/Relationships sections presume a working Knowledge/Memory linkage that is not itself well-specified; OBS-001 means part of its content is not reliably distinct from Context |
| `AI/Context/`, `Prompts/`, `Tools/`, `Evaluation/` | **Partially** | Each internally clear for its narrow scope; their fit into the overall epistemic chain is prose-only, not contractual |
| Governance methodology | **Yes** | Proven directly, repeatedly, across nine-plus recorded items |
| Conformance | **No** | Nothing checkable exists to implement against |
| `Specification/`, `Adoption/`, `Reference Architecture/`, `Examples/` | **N/A** | Not sources of contract by design (presentational/illustrative); flagged instead for pointing at a stale contract state |
| `Workflows/` | **No** | Empty |

---

# Part 5 — Contradictions Inventory

| ID | Location | Documents affected | Criticality | Blocking? | Existing record |
|---|---|---|---|---|---|
| C1 | `AI/Knowledge/*` vs Constitution §5/§6 | `Knowledge.md`, `Knowledge Sources.md`, `Knowledge Quality.md` | Critical | Yes — blocks Agent reasoning design and any Conformance work above Memory | `Concept-Paper-Knowledge-vs-World-Model.md`, `Architecture-Discussion-Knowledge-vs-World-Model.md` (analysis only, no ADR) |
| C2 | World Model named, never defined | Constitution §5, §6 | Critical | Yes — same blocking radius as C1 | Same as C1 |
| C3 | `Models/Domain.md` vs `Domains/Common/Domain.md` — two differently-worded normative definitions of "Domain" | `Models/Domain.md`, `Domains/Common/Domain.md` | High | Not immediately, but blocks confident Domain-layer conformance | `AO-001`, Open |
| C4 | `Meta/Relationship.md` (Object participants) vs `Models/Relationship.md` (Entity-only participants) — Organization cannot participate in a Relationship under current Models text | `Meta/Relationship.md`, `Models/Relationship.md`, `Meta/Organization.md` | High | Blocks Organization-to-anything relationship modeling | `AO-002`, Open, tied to CAND-004/CAND-005 |
| C5 | `AI/Context/Overview.md` and `AI/Agents/Context.md` are near-verbatim textual duplicates (12 lines differ, only nav/Doc-ID) | Both files | Medium | Not yet — live divergence risk if one is edited without the other | `OBS-001`, Open, escalated to `CAND-001` |
| C6 | Memory Record `Status` attribute semantics undefined against append-only immutability | `Memory/Memory Record.md` | Medium | Not immediately; blocks a fully rigorous Memory conformance test | `AO-003`, Open |
| C7 | `Knowledge Quality.md` names "unsupported Knowledge" as an ordinary, manageable issue rather than a disallowed state — direct tension with §3 (Evidence Before Belief), distinct from C1's §5/§6 framing | `Knowledge Quality.md` | High | Same blocking radius as C1 (same underlying document) | Covered by the same Concept Paper as C1, not separately numbered there |
| C8 | `Specification/` (v0.2) approved 22 July 2026, predates Constitution v1.0 (26–27 July); contains no mention of Constitution or Stage 1/2 migrations; `Adoption/` points to it as "the actual entry point" | `Specification/*` (10 docs), `Adoption/README.md` | High | Not blocking further Constitution work, but actively misleads anyone onboarding through the documented path today | **None — new finding, this audit** |
| C9 | Domains/ "AI Memory" boilerplate section present in 8 of 14 subdomains (CRM, Payments, BI, Compliance, Finance, Product, AI, Common), absent in 6 (Affiliate, HR, Legal, Marketing, Operations, Support) | `Domains/*/  *_AI.md` | Medium | No | **None — new finding, this audit** |
| C10 | `Entities/*` has almost no reference to Memory/Evidence/Knowledge anywhere (1 incidental hit across 51 files) | All of `Entities/` | High | Not immediately, but this is the primary business-object layer, and it is structurally disconnected from the epistemic layer this engagement has built | **None — new finding, this audit** |
| C11 | `Examples/Overview.md` names 6 industry example collections; only 1 (iGaming) exists; gap is not flagged in-document the way `Workflows/` flags its own emptiness | `Examples/Overview.md` | Low | No — Examples/ is explicitly non-normative | **None — new finding, this audit** |
| C12 | Constitution §14 uses "Autonomy level" and "delegation" without any document anywhere defining what an Autonomy level is or how delegation is recorded | Constitution §14; no implementing document | High | Blocks any conformance claim about Agent autonomy/delegation | **None — new finding, this audit** |

Resolved, included for completeness, not live debt: `OBS-002` (Business Object Architecture naming duality) — Closed by explicit author decision. `OBS-003` (Object Attribute Lifecycle Categories) — Open by design, correctly not escalated pending independent corroboration (Rule 1/2 of `Standard Evolution Methodology.md`); this is healthy governance discipline, not neglect.

---

# Part 6 — Gaps

Applying the Constitution's own test directly (a term used but nowhere defined counts as a gap):

- **World Model** — used in Constitution §5 and §6, defined nowhere. (= C2 above.)
- **Autonomy level** — used in Constitution §14 ("unless a higher Autonomy level has been explicitly delegated"), no document defines Autonomy levels or delegation mechanics. (= C12 above.)
- **Constitution §9's own text still lacks the scope clarification Decision 4 already resolved** — the *interpretation* (semantic invariance, not directory-based) was decided in `Constitution-Step0-Summary.md`, but §9's actual wording in `Core/Constitution.md` has not been updated to state it. Listed in that same summary's own remaining-work item #6, still open.
- **Constitution §11's own text still carries "architectural layer" language Decision 5 already found misleading** — same situation: the interpretation (a conformance/capability requirement, not an architecture mandate) was decided, the wording was not updated. Listed as remaining-work item #7 in the same summary, still open.
- **Conformance Test Suite** — named as a requirement by `Language/Conformance.md` conceptually and by Architecture Principle 6 explicitly; no executable or checkable artifact exists.
- **`Entities/Department`** — the specification's own entity catalog lists Department as a planned entity type; no content exists (self-admitted stub).
- **`Workflows/` in its entirety** — self-admitted, honestly labeled "Planned for future versions" in every one of its 11 files.
- **5 of 6 `Examples/` industry collections** (FinTech, Healthcare, Manufacturing, Marketplace, SaaS) — named in `Examples/Overview.md`, not present, and not flagged as absent the way Workflows flags itself.

---

# Part 7 — Technical Debt by Category

**Critical**

- C1/C7 — Knowledge contradicts Constitution §3/§5/§6 in its own text.
- C2 — World Model does not exist.
- No Conformance Test Suite exists (Part 6) — nothing above Memory/Evidence can be verified as compatible by anyone, for any implementation, today.

**High**

- C3 — Domain defined twice, differently, unreconciled.
- C4 — Relationship model cannot accommodate Organization, a first-class Object.
- C8 — `Specification/` v0.2 is stale relative to Constitution and is the documented onboarding entry point.
- C10 — `Entities/` (the primary business-object layer) has no defined bridge to Memory/Evidence/Knowledge.
- C12 — "Autonomy level" (§14) is undefined anywhere.

**Medium**

- C5 — OBS-001 live duplication risk (Context.md).
- C6 — AO-003, Memory Record Status semantics.
- C9 — Domains/ Memory-linkage executed in 8/14 subdomains only.
- Constitution §9/§11 wording not yet updated to reflect already-decided Step-0 interpretations.

**Low**

- C11 — 5/6 Examples/ industry collections missing, silently.
- Models/ generic unelaborated "future versions" boilerplate; Entity.md-only cross-reference section (structural asymmetry, not a logical error).
- `Workflows/` fully empty (self-admitted; more accurately "not started" than "debt").

**Resolved, not debt:** OBS-002 (Closed). OBS-003 (correctly parked, not escalated, by governance rule — not neglect).

---

# Part 8 — Ready / Not Ready

| Layer | Ready | Notes |
|---|---|---|
| Constitution | ✅ | Ratified, integrated, verbatim-verified |
| Meta/Object | ✅ | Constitution-linked, proven by downstream reliance |
| Memory / Evidence / Confidence | ✅ | Migrated, internally consistent; one open but scoped item (AO-003) |
| Governance (methodology) | ✅ | Proven, repeatedly, over multiple weeks |
| Core/Manifest, Core/Principles | ✅ | Reconciled with Constitution, re-verified |
| Meta (non-Object) | ⚠️ | Coherent, never checked against Constitution |
| Models/ | ⚠️ | Functionally complete, structurally asymmetric, no Memory bridge |
| Language/ | ⚠️ | Complete-looking, never audited post-Constitution |
| Lifecycles/ | ⚠️ | Functionally complete, zero cross-referencing |
| Reference Architecture/ | ⚠️ | Coherent, correctly Informative, pre-dates recent migrations |
| Domains/ | ⚠️ | Uniform template, uneven execution, live term duplication (C3) |
| Entities/ | ⚠️ | Rich catalog, structurally disconnected from Memory/Evidence (C10) |
| `AI/Knowledge/` | ❌ | Self-contradictory relative to Constitution (C1/C7) |
| World Model | ❌ | Does not exist (C2) |
| `AI/Agents/` | ⚠️ | Coherent identity model; live duplication (C5); reasoning layer correctly out of scope |
| `AI/Context/`, `Prompts/`, `Tools/`, `Evaluation/` | ⚠️ | Internally coherent islands; zero Constitution linkage; depend on unresolved Knowledge |
| `Specification/` (v0.2) | ❌ | Stale relative to Constitution (C8) |
| `Adoption/` | ⚠️ | Coherent, but routes to stale `Specification/` |
| `Examples/` | ⚠️ | One complete example; 5/6 promised collections silently missing |
| `Workflows/` | ❌ | Empty, not started |
| Conformance | ❌ | No test suite exists anywhere |

---

# Part 9 — Critical Path

Order only; no solutions proposed.

1. Resolve the Knowledge vs. Constitution contradiction (C1/C7). — Already the most analyzed, most decision-ready item in the entire inventory (Stage 4's own readiness check concluded "Yes"); everything in layers four through six depends on it.
2. Define World Model at least minimally (C2). — Coupled to (1): resolving Knowledge without giving it something real to derive into leaves the fix half-finished.
3. Reconcile Domain vs. Domain (C3) and the Relationship/Organization inconsistency (C4). — Independent of (1)/(2); foundational term-level fixes that can proceed in parallel, but must land before Domains/Entities conformance work is trusted.
4. Resolve AO-003, Memory Record Status semantics (C6). — Narrower scope; should close before any Conformance Test Suite work begins, since Memory is otherwise the most finished layer and should not carry a known ambiguity into a test suite.
5. Write the already-decided §9/§11 wording clarifications into Constitution's own text. — Pure transcription of Decisions 4/5, already made; low effort, closes a known stale gap, no new decision required.
6. Refresh or retire `Specification/` v0.2 and re-point `Adoption/` at current, Constitution-inclusive content (C8). — Independent of the above; should happen early because it is actively misleading newcomers for as long as it is left as-is, regardless of how long (1)–(5) take.
7. Define "Autonomy level" (C12). — Needed before any Agent-delegation conformance claim is meaningful; should land before or alongside step 8, not after.
8. Design the Conformance Test Suite (Architecture Principle 6). — Deliberately last among the substantive work: testing guarantees that are not yet stable (Knowledge, World Model, Autonomy) is not meaningful, so this step depends on 1, 2, and 7.
9. Systematically bridge Entities/Domains to Memory/Evidence/Knowledge (C9, C10). — Deliberately last: depends on Knowledge/World Model being real (1, 2) and the Domain-term conflict being resolved (3); doing this earlier would require redoing it once those land.

The ordering logic in one sentence: contradictions that block the most downstream work go first; foundational term-duplications independent of Knowledge/World Model run in parallel with that; actively misleading presentation-layer staleness is fixed early regardless of dependency position, because it costs newcomers now; anything about *verifying* guarantees comes only after the guarantees themselves are stable; and structural bridging work that would otherwise need to be redone comes last.

---

# Part 10 — Final Diagnosis

## Evolving Specification

Not **research work** — a research-stage effort would not already have a ratified Constitution, a self-consistent Memory/Evidence layer verified against it, and a governance methodology proven across nine-plus resolved decisions. Too much genuinely stable, load-bearing structure already exists.

Not an **engineering specification**, a **near-finished standard**, or a **mature standard** — each of those would require uniform completeness and, at minimum, a working Conformance mechanism. Neither exists: Knowledge and World Model are unresolved or absent, no Conformance Test Suite exists anywhere, `Workflows/` is entirely empty, and five of six promised Examples collections are missing.

**Evolving specification** fits because the evidence is genuinely mixed, in a specific and traceable way: some layers (Constitution, Memory/Evidence, the Governance methodology itself) are Stable-to-Mature and safe to build on today; others (Knowledge, World Model, Conformance) are actively being worked through, with the analysis already done and decisions pending, not neglected; and others still (Workflows, most of Examples, six of fourteen Domains' AI-Memory sections) are honestly not-yet-started rather than broken. This is precisely what a specification under active, disciplined, iterative development looks like partway through — not a finished artifact, and not an unstructured draft either.

---

# Status

This document is an inventory, not a decision. No Specification document has been changed. No ADR Candidate has been created. It is intended as the factual starting point for the next phase of work, per the request that produced it.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial audit, ten parts, based on direct repository inspection plus the full Governance/ decision record to date |

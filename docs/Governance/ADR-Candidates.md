<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / ADR Candidates

[↑ Up](README.md) · [Next →](Architecture-Health.md)

---
<!-- nav:end -->

# ADR Candidates

**Document ID:** GOV-ADR-CANDIDATES-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 26 July 2026

---

# Purpose

This document is a queue of questions that require a decision from the Chief Architect.

The CDKO does not create Architecture Decision Records. The CDKO proposes candidates. The Chief Architect reviews them and records a Decision. If the Decision is "Promote to ADR," the Chief Architect authors the actual ADR outside this document.

Every candidate uses the same template, so every candidate follows the same lifecycle regardless of where it originated:

| Field | Meaning |
|---|---|
| **ID** | Candidate identifier. |
| **Title** | Short name of the question to be decided. |
| **Status** | `Open` — queued, no decision yet. `Promoted to ADR-<ID>` / `Rejected` / `Merged` / `Closed without ADR` — per the Governance Proposal v1.1 decision set. |
| **Owner** | Who currently needs to act — the Chief Architect while `Open`. |
| **Created** | Date the candidate was queued. |
| **Related Documents** | Source Observation, specification chapters, or other documents involved. |
| **Discussion** | The question, why it cannot be resolved editorially, and the consequences of each plausible outcome. |
| **Next Action** | What has to happen for Status to change. |

---

## CAND-001

**Title:** Content duplication between `AI/Agents/Context.md` and `AI/Context/Overview.md`

**Status:** Open

**Owner:** Chief Architect

**Created:** 21 July 2026

**Related Documents:** `Architecture-Observations.md#obs-001`, `AI/Agents/Context.md`, `AI/Context/Overview.md`

**Discussion:** Should `AI/Agents/Context.md` remain a full duplicate of `AI/Context/Overview.md`, be replaced with an explicit reference, or be given distinct Agent-specific content? This cannot be resolved editorially — it requires a decision about whether the Agents section should own a description of Context distinct from the dedicated Context section, which is a question about section boundaries.

Consequences by outcome:
- *Keep as duplicate:* no immediate harm, but risk of future divergence if one copy is edited without the other.
- *Replace with reference:* removes duplication, but changes how a reader navigates the Agents section.
- *Give distinct content:* requires new normative text describing Context specifically from an Agent's perspective — new authoring work.

**Next Action:** Chief Architect to review and record a Decision.

---

## CAND-002

**Title:** Mechanics of set-scoped (profile-based) Conformance

**Status:** Open

**Owner:** Chief Architect

**Created:** 22 July 2026

**Related Documents:** `Language/Conformance.md`, `docs/Specification/08 Conformance.md`

**Discussion:** `Language/Conformance.md` already names "Profile Conformance" as a category, but does not define the mechanics of a profile — how it is declared, bounded, and validated against the Core. The author has explicitly stated this is a separate topic from the Core specification and should not be folded into it; the mechanism itself still needs to be decided.

Consequences by outcome:
- *Define now:* clarifies Conformance fully, but risks coupling the Core specification to a mechanism that may need to change independently.
- *Leave open, reference from the Conformance chapter:* keeps Core minimal, but leaves implementers without profile guidance until resolved.

**Next Action:** Chief Architect to review and record a Decision.

---

## CAND-003

**Title:** Principle 11 — Separation of Professional Responsibility

**Status:** Promoted to ADR — Integrated into Core (23 July 2026)

**Decision:** Promote to ADR (recorded 23 July 2026). Upon integration, this becomes **Core Principle 11 — Separation of Professional Responsibility** in `Core/Principles.md`.

**Owner:** Chief Architect (Decision recorded); CDKO (pending: Core integration, as a separate task)

**Created:** 23 July 2026

**Decided:** 23 July 2026

**Related Documents:** `Core/Principles.md`, `Core/Manifest.md`, `Meta/Policy.md`, `Memory/`, `Models/Workflow.md`, `AI/`

**Process note:** Submitted directly as an ADR Candidate, not via a Reference Case. Per the author's explicit direction, this is treated as an architectural decision already reached, not a boundary observed through repeated evidence — Rules 1–2 of `Standard Evolution Methodology.md` (no Core extension on a single Reference Case) are accordingly not the basis for this candidate. Recorded here for transparency, consistent with Decision Transparency (`Governance-Manifest.md`, Principle 5), not to imply the normal evidentiary bar was cleared.

**Discussion:**

Proposed new Core Principle, to be numbered **11** (Principle 10 is already "Evolvability"; no existing numbering is disturbed).

*Core idea:* OCOM is an Operational Memory / Knowledge Management / Object-Centric Operations system. It is not a system of professional expertise. The architecture deliberately separates operational memory from professional judgment.

*OCOM's responsibility:* knowledge extraction, object model construction, Operational Memory management, linking objects, context retention, decision tracking, action tracking, process routing, owner assignment, change history.

*Organization's responsibility:* professional decisions remain with the relevant specialist functions (Legal, Compliance, Finance, Risk Management, Information Security, HR, Internal Audit, Quality Assurance, others). OCOM does not substitute for their expertise.

*Architectural rule:* where a process requires specialized evaluation, OCOM records the fact, records the context, determines that review is needed, creates a corresponding review object, and assigns the responsible unit — it does not itself reach the professional conclusion.

*Worked example:* a meeting decision "the company is considering entering the German market" — OCOM extracts Strategic Initiative, Decision, Action, Target Market, Owners, and may create Legal Review / Compliance Review / Finance Review objects. It does not conclude whether the initiative is lawful, meets regulatory requirements, or should proceed — that remains the responsible units' call. (Illustrative; not an observed case.)

*Company Policy link:* the organization defines its own policies (Operational, Compliance, Security, Finance, HR, Governance, Product). OCOM uses these as part of the operational model but does not substitute for their professional interpretation.

*Explicitly out of scope for this candidate, per the author:* this is not an AI behavior constraint, not a safety mechanism, and not a description of any specific model's behavior. It is a Core architectural boundary, independent of whether AI is involved in operating the system.

**Impact assessment (for the Architect's review, not a recommendation to act):**

- `Core/Principles.md` — would add Principle 11.
- `Core/Manifest.md` — Scope already excludes software architecture, UI, infrastructure, business strategy, etc., but does not currently exclude professional/expert judgment (legal, compliance, financial conclusions). This is a genuine gap, not a conflict — nothing currently claims OCOM makes such judgments, but nothing currently rules it out either.
- `Meta/Policy.md` — substantial existing overlap. Its current definition ("a governed set of rules that defines expected behavior or constraints applicable to one or more Objects... independently of implementation technologies") already covers most of what "Company Policy" describes. The one genuinely new element is an explicit link from Policy to Memory (policies "becoming part of Operational Memory" and being used during Workflow execution) — today `Meta/Policy.md` and `Memory/` do not cross-reference each other.
- `Memory/` — same cross-reference gap, from the other side.
- `Models/Workflow.md` — the "create a review object, assign responsible unit" pattern is a Workflow-shaped concern; whether "Review" is meant as a new named Meta/Models concept or an illustrative Entity type using existing primitives is not stated in this submission and would need clarifying before any document is edited.
- `AI/` — per the author, this principle is explicitly not an AI-specific constraint. If adopted, a light cross-reference noting that AI/ inherits this Core boundary (rather than defining its own separate one) may be warranted; no AI/ document currently states or contradicts this.

**Next Action:** None — closed. Integrated 23 July 2026 into `Core/Principles.md` (Principle 11), `Core/Manifest.md` (Scope), `Meta/Policy.md` (Relationship to Memory), `Memory/Overview.md` (Relationship to OCOM), `Models/Workflow.md` (Professional Review Escalation), and `AI/Overview.md` (Relationship to Professional Responsibility). No new Meta Objects were created; no existing definitions were changed.

---

## CAND-004

**Title:** Modeling Cross-Organization Relationships

**Status:** Open

**Owner:** Chief Architect

**Created:** 23 July 2026 · **Rewritten:** 23 July 2026, following the CAND-005 Decision (Option C)

**History:** This candidate was originally framed as "Organization vs Domain as the Top-Level Architectural Boundary" (Option A vs. Option B). CAND-005 decided that question directly — Organization is a first-class, peer specialization of Object, not a new layer and not an attribute of Domain — with a third option neither A nor B anticipated. That made this candidate's original framing inapplicable; it was not rejected, and is rewritten here rather than closed. The original text is preserved in this document's revision history for traceability.

**Related Documents:** `Meta/Relationship.md`, `Meta/Reference.md`, `Meta/Ownership.md`, `Meta/Identity.md`, `Meta/Registry.md`, `Meta/Contract.md`, `Meta/Policy.md`, `Models/Domain.md`, `Models/Workflow.md`, `Entities/Partner/Partner.md`, `Memory/`, `AI/`, `Governance/ADR-Candidates.md#cand-005`

**Architectural basis (from CAND-005, not re-litigated here):** Object is the sole architectural root. Organization is a new peer specialization of Object, alongside Entity, Domain, Workflow, Event, Policy, Contract, and others. Domain keeps its existing semantics unchanged. Organization connects to other Objects only through the existing Relationship model — no new hierarchy, no ownership-based containment.

**Problem:**

OCOM now supports multiple independent Organization objects. The architectural model for how they interact must be defined. The question is no longer "Organization or Domain?" — it is:

**How do independent Organizations interact with one another while each retains the autonomy of its own operational model?**

**Research questions**

### 1. Inter-organizational relationships

What relationship types are valid between two Organizations — e.g., Contractor, Customer, Vendor, Supplier, Partner, Affiliate, Parent Company, Subsidiary, Regulator, Investor?

*What's already in place:* `Meta/Relationship.md`'s Relationship Types list is explicitly open: *"Organizations may define Relationship Types including: Ownership, Dependency, Composition, Association, Membership, Responsibility, Assignment, Delegation, Collaboration, Sequence. Additional relationship types may be introduced without affecting the model."* Every type named in this question can plausibly be added to this already-extensible list without a new mechanism. This part of the problem looks close to already solved by an existing, unmodified primitive.

*What's not yet decided:* whether this list needs to stay a free-text/example vocabulary (as it is today) or become a constrained enumeration specifically for inter-Organization relationships — an open design choice, not a gap in the model.

### 2. Ownership

What can an Organization own — Domain, Entity, Workflow, Policy, Asset, Contract, some subset?

*What's already in place:* `Meta/Ownership.md` already anticipates this: *"Ownership identifies the individual, team, **organizational unit**, or system responsible for governing an Object."* Once Organization exists as a first-class Object, it fits this definition without any change to `Meta/Ownership.md`'s text.

*What's not yet decided:* `Models/Entity.md` requires *"Every Entity shall have **one** responsible owner"* — singular. Whether an Organization can be that one owner for Domain, Workflow, Policy, etc. (likely yes, no conflict) is different from whether an object can have **more than one** owning Organization at once (see Question 4 — this is where a real tension with the existing single-owner invariant appears).

### 3. Cross-Organization references

Can an object belonging to one Organization reference an object belonging to another? If so, how, with what constraints, and how is each Organization's model independence preserved?

*What's already in place:* the existing distinction between `Meta/Reference.md` (a directed pointer, no implied meaning) and `Meta/Relationship.md` (a governed, meaningful association) already gives two different-weight mechanisms for one Organization's objects to point at another's, without merging anything.

*What's not yet decided:* nothing in either document today states that a Reference or Relationship crossing an Organization boundary must not, by itself, grant access to or merge the target Organization's Operational Memory. This is an omission, not a contradiction — worth deciding explicitly rather than assuming.

### 4. Shared objects

Are objects shared across Organizations permitted — e.g., Contract, SLA, Project, Campaign? If so, what governs their ownership, lifecycle, governance, and versioning?

*What's already in place:* `Meta/Contract.md` already defines a Contract as *"a governed agreement between **two or more** Objects"* — multi-party participation is already native to Contract. Campaign already exists as an Entity (`Entities/Campaign/`); SLA and Project do not exist anywhere yet.

*What's not yet decided, and in real tension:* the single-owner invariant in Question 2. A Contract naturally involves two or more Organizations as parties, but "party to a Contract" and "owner of a Contract" are not stated as the same thing anywhere today. Whether a shared object has exactly one owning Organization (with the others as parties, not owners) or requires a different ownership model is unresolved — this is the sharpest open question in this candidate.

### 5. Operational Memory

Is Operational Memory fully independent per Organization, or can shared memory regions exist?

*Status:* unresolved, carried over unchanged from the original CAND-004 and from CAND-005's impact assessment. No document in `Memory/` addresses per-organization isolation or sharing. This remains open.

### 6. Registry

How does a Registry identify objects belonging to different Organizations — global identifiers, or Organization as part of Identity?

*What's already in place:* `Meta/Identity.md` defines Identity as *"the persistent and unique representation of an Object"* but says nothing about namespacing or scope. `Meta/Registry.md` defines a Registry as a governed collection preserving identity and traceability, also silent on multi-Organization scope.

*Status:* genuinely undecided; existing text neither supports nor rules out either approach.

### 7. AI

How does AI operate across multiple Organizations at once, without mixing context, crossing organizational boundaries, or ambiguous object interpretation?

*What's already in place:* `AI/Overview.md` already requires AI Agents to *"operate within organizational governance"* and to *"respect organizational policies"* (Design Principles), and — per Principle 11's integration — to route matters requiring professional judgment to the responsible organizational function rather than deciding itself. None of this currently addresses operating across more than one Organization concurrently.

*Status:* genuinely undecided; this is new territory, not a gap in an existing multi-Organization design.

**Impact assessment**

| Area | Assessment |
|---|---|
| Object Model | No change required identified — Organization's introduction as a peer specialization was already settled by CAND-005; this candidate does not reopen it. |
| Relationship Model | Needs further architectural discussion — Question 1 suggests the existing extensible Relationship Types list is likely sufficient; whether it should be constrained specifically for inter-Organization use is an open design choice. |
| Identity | Needs further architectural discussion — Question 6; genuinely undecided whether Organization becomes part of Identity scope. |
| Registry | Needs further architectural discussion — same as Identity; no existing text addresses multi-Organization scope. |
| Memory | Needs further architectural discussion — Question 5, carried over unresolved from CAND-004's original version and from CAND-005. |
| Workflow | No change required identified — no current conflict found; would only need revisiting once Questions 3–4 are resolved, if a Workflow needs to act across Organizations. |
| Policy | No change required identified — `Meta/Policy.md`'s existing Policy Scope already lists "Organizations" as a valid scope; no contradiction found. |
| AI | Needs further architectural discussion — Question 7; genuinely new territory. |

**Explicitly out of scope for this candidate:** proposing an implementation mechanism, introducing any new Meta Object, and proposing any new Core Principle. This candidate's purpose is to enumerate the open questions precisely, using only what already exists, so the Architect can decide with full information — not to pre-select answers.

**Next Action:** Chief Architect to review the seven questions above and decide which require a Core change, which are already resolved by existing primitives (per the "what's already in place" notes), and which need further, separate architectural discussion before any decision is recorded.

---

## CAND-005 — ✅ Decided (was Blocking)

**Title:** Organization vs Domain as the Top-Level Architectural Boundary

**Status:** Decided — Option C

**Decision:** **Option C — Organization is a First-Class Object (a peer specialization of Object, alongside Entity, Domain, Workflow, Event, Policy, Contract, and others) — not a new Meta layer, and not an attribute or owner of Domain.** Recorded 23 July 2026.

**Editorial note on wording:** the Decision as submitted titled this "Organization is a First-Class Entity." Its own body and diagram describe Organization as a peer of `Entity` under `Object` — i.e., a new, independent specialization, not a kind of `Entity` in the sense `Models/Entity.md` defines the term. This record uses "Object" (not "Entity") to describe Organization's level, to match the Decision's own diagram and avoid conflating two specific, already-defined terms. The substance of the Decision is unchanged; this is a transcription clarification only.

**Rationale:**

- **Against Option A** (Domain as owner/attribute of Organization): Domain answers *what is governed*; Organization answers *who exists as an independent participant in the ecosystem*. These are different dimensions of the model. Collapsing them would make Domain represent organizational identity, which contradicts `Models/Domain.md`'s own definition ("what is governed, not who performs the work").
- **Against Option B** (Organization as a new layer above Domain): introducing `Object → Organization → Domain` would create a structural exception — today every specialization of Object sits at the same level. A second, superior tier would break that uniformity and sit in tension with Principle 2 (Entity-Centric Modeling) and the single-root Object Model.
- **Option C accepted because:** it preserves Object as the sole architectural root, introduces no second root and no new tier, and adds only what is actually missing — a specialization of Object that was never defined.

**Accepted model:**

```text
Object
├── Organization
├── Domain
├── Entity
├── Workflow
├── Event
├── Policy
├── Contract
└── ...
```

**Domain** keeps its existing, unchanged semantics — an operational boundary describing an area of responsibility (Payments, Compliance, Marketing, CRM). Domain does **not** become an organizational boundary.

**Organization** describes an independent participant in the ecosystem — for example a Bank, an Affiliate Network, a Payment Service Provider, a Supplier, a Regulator, a customer company. Organization is a first-class Object, at the same architectural level as Entity, Domain, Workflow, Event, Policy, and Contract — not superior to them, not a container for them.

**What connects them is Relationship, not hierarchy or ownership.** Example relationships, all expressed through the existing `Relationship` model (`Meta/Relationship.md`), not a new containment structure:

```text
Organization ── owns ─────► Domain
Organization ── contracts ─► Organization
Organization ── employs ───► Person
Organization ── owns ─────► Asset
```

**Owner:** Chief Architect (Decision recorded)

**Created:** 23 July 2026 · **Decided:** 23 July 2026

**Related Documents:** `Meta/Object.md`, `Models/Domain.md`, `Models/Entity.md`, `Meta/Relationship.md`, `Core/Principles.md` (Principle 2), `Governance/ADR-Candidates.md#cand-004`

**What is already established:**

`Domain` is an existing, formally defined architectural entity. `Models/Domain.md`: *"A Domain is an operational boundary responsible for governing one or more Entities."* The same document states directly: *"it represents what is governed, not who performs the work."* Domain, by its own definition, deliberately does not answer the question of organizational ownership.

**What is missing:**

No formal model exists for Organization, Organizational Boundary, Multiple Organizations, or Cross-Organization Architecture. "Organization" is used only as an ordinary-language word (e.g., in `Core/Manifest.md`'s Abstract, in `Entities/Partner/Partner.md`'s definition). No architectural entity named Organization currently exists anywhere in the repository.

**The architectural question:**

The system's top-level architectural boundary must be determined. Two directions:

### Option A — Domain remains the top-level boundary

Domain stays where it is; no new layer is introduced. This requires determining:
- how a Domain acquires organizational ownership;
- whether the existing `Relationship` model is sufficient to express that ownership;
- whether a new architectural entity, Organization, is needed at all.

### Option B — Organization becomes a new architectural layer

```text
Object
    ├── Organization
    │
    ├── Domain
    │
    ├── Entity
    │
    ├── Workflow
    │
    └── ...
```

This requires determining:
- the relationship between Organization and Domain;
- Organization's lifecycle;
- Organization's ownership model;
- Organization's governance;
- how multiple independent organizations coexist;
- the impact on the existing Object Model.

**Questions this ADR must answer, at minimum:**

1. Is Domain a sufficient top-level architectural boundary?
2. Is a new architectural layer, Organization, required?
3. If required, is Organization a new Meta Object, or a specialization of the existing Object primitive?
4. How do multiple independent organizations coexist architecturally?
5. What is the impact on: Object Model; Domain Model; Entity Ownership; Governance; Operational Memory; Workflow; Registry; AI?

**Impact assessment (for the Architect's review, not a recommendation to act):**

| Area | Assessment |
|---|---|
| Object Model | Needs further architectural discussion — depends entirely on whether Organization becomes a specialization of Object (Option B) or is not introduced (Option A). |
| Domain Model | Needs further architectural discussion — `Models/Domain.md`'s own text ("what is governed, not who performs the work") may need a companion statement once ownership is resolved, regardless of option. |
| Entity Ownership | Needs further architectural discussion — every Entity already requires an Owner (`Models/Entity.md`); whether that Owner can or must resolve to an Organization is unresolved. |
| Governance | No change required — this question is being handled correctly through the existing ADR Candidate process; no update to `Governance/` process documents is implied by either option. |
| Operational Memory | Needs further architectural discussion — same open question already logged in CAND-004: whether memory isolation across organizations needs explicit architectural support. |
| Workflow | No change required identified — no current conflict found; would only need revisiting if Option B changes what a Workflow's Entities can belong to. |
| Registry | Needs further architectural discussion — `Meta/Registry.md` defines governed collections of Objects; whether Registries are scoped per Organization under Option B is undetermined. |
| AI | No change required identified — no current AI/ document addresses or conflicts with either option. |

**Explicitly not the goal of this candidate:** to pre-select an option. The goal is to record the fork itself, so it can be decided deliberately rather than inherited implicitly by whichever way CAND-004 happens to be written. (Resolved: the Decision above answers the fork with a third option, not listed among A or B at the time this candidate was created.)

**Consequence for CAND-004:** CAND-004, as originally framed ("Organization vs Domain," Option A vs. Option B), is no longer accurate — this Decision answers that framing directly (neither A nor B; Organization is a peer Object of Domain, connected only through Relationship). CAND-004 requires rework, not just an unblock. Suggested reframing, per the Architect: **"Modeling Cross-Organization Relationships"** — the question is no longer "what sits above what," but how independent Organizations interact through the now-clarified object model (Relationship types such as `owns`, `contracts`, `employs`, per the diagram above). CAND-004's rework is a separate, subsequent task — not performed here.

**Next Action:** None on CAND-005 — decided and closed. CAND-004 is queued for rework under the new framing; `Core/`, `Meta/`, `Models/` remain unmodified until that rework is reviewed and its own Core integration is separately authorized.

---

## CAND-006 — ✅ Decided

**Title:** OCOM Constitution — Foundational Principles

**Status:** Decided — Adopted as v1.0 (26 July 2026)

**Owner:** Chief Architect (decided); CDKO to await separate authorization for Core integration.

**Created:** 26 July 2026

**Related Documents:** `Core/Principles.md` (Principle 11, referenced by Constitution §14), `Meta/Object.md` (Object as universal abstraction, §1), `Meta/Relationship.md` (§9's Core-Meta-Model boundary). Also draws on findings from the sibling implementation repository, OCOM-Reader — `ADR-007` (Memory Before Knowledge), `RF-001` (Domain-Owned Identity, tested against infrastructure and a business domain as neutral test-beds), and the M017/M019 structural-isolation precedent. Recorded transparently: this is the first Governance record in this repository whose empirical grounding was substantially developed in the implementation repository rather than purely within the Specification itself.

**Decision:**

# OCOM Constitution v1.0

**Purpose**

This document defines the fundamental principles that make a system an implementation of OCOM. These principles are intentionally technology-independent and domain-independent. They apply regardless of programming language, storage engine, deployment model, AI model, or business domain. Implementation details may evolve. Architecture may evolve. These principles should not.

**Canonical Principles**

1. **Object-Centric Reality.** Object is the universal abstraction of OCOM. Everything represented by OCOM is expressed as an Object or as a specialization of Object.
2. **Domain-Owned Identity.** An entity becomes an OCOM Object only when its identity belongs to the operational domain rather than to the implementation. Operational role takes precedence over ontological classification. The same entity may be represented differently depending on the operational question being answered.
3. **Evidence Before Belief.** Every operational fact must be traceable to Evidence. Evidence and Metadata are independent concepts and must never be merged.
4. **Immutable Memory.** Memory is append-only. A Memory Entry is immutable after creation. Corrections are represented as new Memory Entries, never by modifying historical records.
5. **Memory Precedes Knowledge.** Knowledge is always derived from Memory. World Models are always derived from Knowledge. Memory → Knowledge → World Model.
6. **Reconstructability.** Knowledge and World Models must always be reproducible from Memory without requiring access to the original external systems.
7. **Separation of Dimensions.** Architecture, Capability and Autonomy are independent dimensions. Progress in one dimension never implies progress in another.
8. **Static Before Dynamic.** Static World Modelling precedes Dynamic World Modelling.
9. **Domain-Neutral Core.** The OCOM Core must never contain domain-specific knowledge. The Core must never branch on organization-specific concepts or business entities. Domain knowledge belongs only to configuration, data and adapters.
10. **Extensibility Over Enumeration.** Business vocabularies are extensible. Organizations extend OCOM through specialization rather than modification of the Core.
11. **Structural Isolation.** Every architectural layer must be structurally incapable of exceeding its defined responsibilities. Boundaries are enforced by architecture rather than convention.
12. **Grounded Reasoning.** Statements derived from Memory and Knowledge must remain distinguishable from interpretation, inference or expert opinion. The system must communicate provenance and confidence appropriately.
13. **Adaptation Flows Toward the Model.** Implementations adapt to OCOM. OCOM never adapts to implementation-specific constraints.
14. **Professional Responsibility.** OCOM augments professional decision-making. Responsibility remains with the designated human role unless a higher Autonomy level has been explicitly delegated.

**Architectural Principles**

- New sources integrate through Adapters and Normalizers.
- Identity Resolution thresholds are deployment configuration.
- Source trust is deployment configuration.
- Concept namespaces are deployment scoped.
- One deployment currently represents one organization.

**Implementation Principle**

Every implementation must be evaluated against the Canonical Principles *before* architectural or implementation-specific optimizations are accepted. No optimization may violate the Canonical Principles.

**Meta-Principle**

When a conflict exists between an implementation, an architectural decision and the Constitution, the Constitution prevails.

**Governance implication of this Decision:**

- Future changes to the Canonical Principles require the same process used to establish them — a Reference Case or direct proposal → ADR Candidate → Chief Architect Decision — never an editorial edit to whatever document eventually carries the Constitution's text. This reuses the existing Standard Evolution Methodology rather than introducing a separate amendment process.
- New architectural proposals (Bot, Observer, Expert, multi-tenancy, and any future component, in either this Specification or an implementation repository) are to be evaluated against these Canonical Principles before acceptance — per the Constitution's own Implementation Principle. The Constitution is the standard proposals are checked against, not the other way around.
- The Architectural Principles and the two Meta-level principles are explicitly *not* frozen the same way the Canonical Principles are — they record the current architectural direction and may evolve through ordinary ADR Candidates, without amending the Constitution itself.

**Next Action:** Core integration — deciding where the Constitution's full text is authored as a standing document (e.g. a new `Core/Constitution.md`, or distributed across existing Core documents) and updating any documents that should reference it — is a separate, not-yet-authorized task. Recorded here first, per the same two-step discipline already used for CAND-003 (Principle 11) and CAND-005 (Organization): Decision recorded now, Core integration only on separate, explicit instruction.

---

## CAND-007 — ✅ Decided

**Title:** Architecture Freeze for OCOM v1.0 — Transition from Architecture Discovery to Architecture Stabilization

**Status:** Decided — Adopted (27 July 2026)

**Owner:** Chief Architect (Decision recorded); CDKO to await separate authorization for each Backlog work item and for the §9/§11 Core-text integration.

**Created:** 27 July 2026

**Decided:** 27 July 2026

**Related Documents:** `Architecture-Discovery-Summary.md`, `Architecture-Principles.md`, `Architecture-Audit-Current-State.md`, `Master-Architecture-Backlog.md`, `Architecture-Release-Review-v1.0.md`, `Standard Evolution Methodology.md`, `Development-Readiness.md`, `Release-Readiness.md`. Two source names used when this candidate was originally requested — "Agent Readiness Audit" and "Documentation Architecture" — do not correspond to standalone documents; they refer to material already covered by `Architecture-Health.md`'s Reference Agent tracking / the "OCOM without Reader" analysis in `Architecture-Release-Review-v1.0.md`, and by the Specification Map in `Architecture-Audit-Current-State.md`, Part 1, respectively. Recorded here for traceability, not as new sources.

**Revision note (27 July 2026):** an independent Committee review of this candidate's first draft found four defects: (i) two of the four cited evidentiary passes existed only in prior conversation, with no citable document; (ii) Sections 1–2 asserted that every finding fit an existing Epic, which `Architecture-Release-Review-v1.0.md` Part 2 itself contradicts for two of its three findings; (iii) Section 6 cited Architecture Principle 3, which does not support the claim made; (iv) Section 4's closing sentence was ambiguous about whether it was inherited or new. `Architecture-Discovery-Summary.md` was created to resolve (i). This is the corrected text; all four defects are fixed below, not merely re-asserted.

**Decision:**

# ADR — Architecture Freeze for OCOM v1.0

## 1. Why Architectural Discovery Is Considered Complete

Not because every question is answered — `Architecture-Release-Review-v1.0.md` (Part 3) explicitly found the Specification is not yet a closed system (Knowledge/World Model unresolved, "Autonomy level" undefined). Discovery is considered complete in a narrower, checkable sense: repeated, deliberately adversarial searches for *new fundamental architectural questions* have stopped finding them, and every finding either fits already-open work or is now explicitly named as an exception, none concealed.

Four independent search passes were run, each with a citable record: (1) the standards-analogy and reasoning-pipeline-independence analysis, recorded in `Architecture-Discovery-Summary.md`; (2) the architecture stress test (Red Team against the Specification/Reader boundary), whose conclusions are recorded principle-by-principle in `Architecture-Principles.md`; (3) `Architecture-Release-Review-v1.0.md` Part 2, a dedicated final search for gaps not covered by (1) or (2); (4) `Architecture-Release-Review-v1.0.md` Part 6, a Red Team pass against the Backlog itself.

Pass (3) — Release Review Part 2 — produced three findings, not zero. One, the `Layered Memory.md`/`Retention.md` mutability finding, widened `EPIC-A`'s Definition of Done rather than requiring a new Epic. The other two — **absence of a stewardship/naming-rights model for "OCOM"/"OCOM-compatible,"** and **absence of a tamper-evidence guarantee for Memory/Evidence** — do **not** fit inside any existing Epic, by Part 2's own explicit statement (*"sits outside all six Epics"*; *"distinct from every current Epic"*). This Decision does not claim otherwise. Both are carried forward as named, open Freeze-exception candidates under Section 5, not treated as resolved and not concealed.

Pass (4) — Release Review Part 6, the Red Team pass — did not produce discrete catalogued gaps the way Part 2 did; it produced a structural critique: that ecosystem-scale verification (an independent Reference Implementation, real adversarial external pressure) has not yet happened for any part of this architecture. Release Review Parts 1 and 7 both treat this as a real, named, permanent condition to be tested later (Section 8), not as a Backlog item to be closed now — this Decision does not claim otherwise either.

This is a measurable trend across the four passes, not an assertion of completeness: successive passes found progressively narrower, more boundable issues — contradictions, then gaps, then two residual, explicitly-named exceptions, plus one acknowledged, permanent verification limit — never a new question about the root shape of the model. The Object/Memory/Evidence/Knowledge-derivation shape itself was independently re-derived and stress-tested in all four passes and held every time, including under pass (4), whose strongest argument concerned unproven ecosystem-scale verification — a real, named limitation about *proof*, not about the *shape* of the model.

## 2. Criteria Confirming This

- `Architecture-Audit-Current-State.md` rated the root layers (Constitution, Memory/Evidence, the Governance methodology itself) Stable-to-Mature; every unresolved item traces to integration or sequencing, never to the root abstractions.
- `Master-Architecture-Backlog.md` normalized every open AO, ADR Candidate, and Documentation Debt entry into six Epics. Two items found after the Backlog was written (Section 1 above) are not yet in it — named as open exceptions, not as evidence the Backlog is already complete.
- `Architecture-Release-Review-v1.0.md` Part 8 recommended **B — freeze and execute the Backlog**, with one scope correction (`EPIC-A`) and the two exceptions named in Section 1 — after its own dedicated final-gap search (Part 2) and Red Team pass (Part 6). The same review explicitly declined to recommend either continued discovery (A) or a return to the fundamental model (C).
- No open item anywhere in the current record — Audit, Backlog, Release Review, `ADR-Candidates.md`, `Architecture-Observations.md`, `Documentation-Debt.md` — questions Object as root, Memory as append-only Evidence-backed log, or the Memory→Knowledge→World Model derivation direction. This claim is about the *root model* specifically, and is narrower than, and does not imply, "no open items remain" generally — Section 1 names two that do.

## 3. Permitted Changes Before v1.0

- Execution of `Master-Architecture-Backlog.md`'s existing Epics A–F, exactly as scoped there, including the `EPIC-A` Definition-of-Done correction named in `Architecture-Release-Review-v1.0.md` Part 2 (adding `Layered Memory.md` and `Retention.md`).
- Decisions on already-open ADR Candidates (`CAND-001`, `CAND-002`, `CAND-004`) and Architecture Observations (`AO-001`, `AO-002`, `AO-003`), provided the decision stays within each candidate's already-recorded scope.
- Writing Constitution §9 and §11's wording to match Decisions already recorded in `Constitution-Step0-Summary.md` (Decisions 4 and 5) — transcription of an existing decision, not a new one.
- Editorial, presentational, and documentation-currency work (`EPIC-F`): refreshing `Specification/`, re-pointing `Adoption/`, closing `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005`.

## 4. Forbidden Changes Before v1.0

Directly inherited from `Master-Architecture-Backlog.md` Part 9 (Stop List) — not restated with new reasoning, only reaffirmed as binding for the Freeze period: no new Domains subdomains beyond the existing 14; no new Entity types; no new AI/* subsections or capabilities; no new Workflows content; no new Examples industry collections; no new Canonical Principle or Constitution amendment beyond the §9/§11 transcription in Section 3 above; no new Conformance Profile ahead of `CAND-002`; no pulling Reader/product-roadmap concepts (e.g. persona-adaptive explainer work) into the Specification.

One further item is forbidden here that is **not** inherited from the Stop List — stated plainly as new, not represented as an existing norm: **no redesign of Object, Memory, Evidence, or the Knowledge/World Model derivation direction without going through Section 5.** This is not an independent new governance norm; it is this Decision's own Section 5 test (does a proposal fail to fit any existing Epic/ADR/AO) applied explicitly to the one category of proposal — root-model redesign — where the consequence of skipping that test would be most severe. Its source is Section 5 of this same Decision, not any prior document.

## 5. When Breaking the Freeze Is Permitted

Only when a genuinely new fundamental question is found — one that fails the same test Section 1 just applied: it does not fit inside any existing Epic, ADR Candidate, or Architecture Observation, and is not a bounded scope-correction to one. Meeting that bar does not itself authorize a change. It authorizes escalation through the existing pipeline (`Standard Evolution Methodology.md`: Reference Case → Repeated Pattern → ADR Candidate → Chief Architect Decision), with the escalation explicitly labeled a Freeze exception at the point it is raised — never absorbed silently into ordinary Backlog work.

Two candidates already meet this bar today, named in Section 1: the "OCOM"/"OCOM-compatible" stewardship gap, and the Memory/Evidence tamper-evidence gap. Naming them here is not the same as filing them — filing either through the Reference Case format is separate, not-yet-authorized follow-up work. They are recorded now so this Decision does not itself become a second instance of the defect it was revised to fix: claiming completeness while an unresolved item goes unmentioned.

A second, standing trigger: real contact with an independent implementation attempt (Milestone 4 in `Architecture-Release-Review-v1.0.md` Part 9) revealing the contract is not buildable as specified. This is the category of evidence Green Team (`Architecture-Release-Review-v1.0.md` Part 7) identified as the legitimate next test of the architecture — it is a valid Freeze-exception trigger precisely because it is evidence from outside the same two-party process that produced the Freeze decision itself.

## 6. How New Proposals Are Evaluated

Every new proposal, regardless of source, is checked in this order: (a) does it already fit inside a `Master-Architecture-Backlog.md` Epic or work item — if so, it is not new work, it is routed there under its existing ID; (b) if not, is it product- or implementation-shaped rather than contract-shaped, per Architecture Principle 1 (Specification Defines Contracts, Not Products) and Architecture Principle 5 (Reader Is Reference, Not Authority) — if so, it does not belong in the Specification and is redirected to Reader or another implementation, not queued here at all; (c) if it survives both checks, it is treated as a candidate Freeze exception under Section 5 and must go through the full Reference Case → ADR Candidate pipeline, explicitly flagged as such — it is never adopted directly into a document on the strength of the proposal alone.

## 7. The Backlog as the Sole Source of Architectural Work

Effective on this Decision, `Master-Architecture-Backlog.md` is the sole authoritative work queue for architectural work during the Freeze. No architectural document is edited for architectural (as opposed to purely editorial) reasons unless the change traces to a named Epic or work item there. Any item newly approved under Section 6 is added to the Backlog, under an existing Epic where it fits or, if Section 5's bar is met, a new Epic recorded through the same Decision process as this one — never executed ad hoc outside it. `Development-Readiness.md` and `Release-Readiness.md` entries reference Backlog item IDs going forward, consistent with their existing logging convention.

## 8. Criteria to Lift the Freeze After v1.0

The Freeze is scoped to reaching v1.0, not indefinite. It lifts, returning to a discovery-permitted phase, when v1.0 has shipped (per the Release Readiness criteria already logged in `Release-Readiness.md`) and at least one of: (a) Milestone 4 (`Architecture-Release-Review-v1.0.md` Part 9) is reached — an implementation independent of this Specification's own authors exists and has been run against Conformance criteria, surfacing real integration lessons; (b) the Chief Architect schedules a formal post-v1.0 review cycle; (c) an accepted Section 5 Freeze exception grows, on independent review, into a question broad enough to warrant reopening discovery generally rather than a single narrow amendment. None of these criteria is met today; this section records the condition, not a current event.

**Governance implication of this Decision:**

- This is a process/lifecycle decision, not a modeling decision — it changes how proposals are handled, not what OCOM's architecture is. It introduces no new Meta Object, no new Canonical Principle, and no new Epic.
- Sections 3, 4, and 7 are immediately binding on how the CDKO evaluates any future request, including requests from the same author who adopted this Decision — consistent with Decision Transparency (`Governance-Manifest.md`, Principle 5), a request to bypass Section 6's evaluation order is itself a Section 5 Freeze-exception question, not a reason to skip it.

**Next Action:** Execution of any individual Backlog work item (Section 3) requires its own separate, explicit authorization, per the two-step discipline already used for `CAND-003` and `CAND-006`. The §9/§11 Core-text transcription (Section 3) is likewise not authorized by this Decision alone.

---

## CAND-008

**Title:** OCOM Value Model — a Meta-level construct for self-describing Attribute values, with Measurement as its first realized Value Kind

**Status:** Open

**Owner:** Chief Architect

**Created:** 29 July 2026

**Related Documents:** `Architecture-Observations.md#ao-005`, `Concept-Paper-Value-Model.md`, `Models/Entity.md`, `Meta/Object.md`, `Meta/Classification.md`, `Meta/Relationship.md`, `Domains/Finance/Finance_KPIs.md`, `Domains/Operations/Operations_KPIs.md`, `Domains/BI/BI_Objects.md`. Filed under `CAND-007` (Architecture Freeze) §5/§6 as a named Freeze exception, not as ordinary Backlog work.

**Discussion:** `AO-005` found, via two independent Reference Cases (`RC-006`: a real operating company's meeting transcripts; `RC-007`: OCOM's own already-released `Domains/Finance/`, `Domains/Operations/`, `Domains/BI/` content), that `Models/Entity.md`'s Attribute "data type" facet has no structure for what a quantitative value must self-describe — an AI agent cannot determine whether "10000" is USD, EUR, or BTC, whether "35" is a percent, a fraction, or a plain score, or whether "30" is days or hours, from the Attribute alone.

This is filed as a Freeze exception under `CAND-007` because it does not survive check (a) of that Decision's §6 (no `Master-Architecture-Backlog.md` Epic covers value/data-type structure — the closest, `EPIC-D`, closes undefined *terms*, not undefined value *structure*), and it passes check (b): this is contract-shaped, not product-shaped, by Architecture Principle 1's own test ("does it constrain what gets written, or how a written corpus gets read?" — a Value's structure is what gets written; how any given Reader or Agent interprets it afterward remains free, consistent with Principle 5).

Rather than adopting the narrower Measurement concept the original submission proposed, this candidate proposes the smaller, more defensible ask that Minimal Core (`Standard Evolution Methodology.md`) argues for: a general **Value** Meta-construct (Value Kind / Representation / Semantics / Context / Resolution Status — the same five-characteristic shape `Meta/Object.md` uses for Object) with **Measurement** specified as its one fully-designed Value Kind, since that is the only kind with concrete Reference Case evidence. Three further Value Kinds (ScalarValue, ReferenceValue, CompositeValue) are named in the attached Concept Paper but deliberately left unspecified — no Reference Case evidences their boundaries yet, and speculatively designing them now would itself violate Minimal Core.

The full design — Value's Core Characteristics; Measurement's six kinds (Money, Percentage, Duration, Quantity, PhysicalUnit, Rate); `ExchangeRateObservation`; the unit-normalization comparison procedure; a conceptual diagram; worked examples; edge cases; integration with Objects/Attributes, Evidence, Lifecycle, Relationships, and Governance; and a migration strategy — is attached as `Concept-Paper-Value-Model.md`, Status: Informative, following the same non-normative pattern `Concept-Paper-Knowledge-vs-World-Model.md` used ahead of `AO-003`'s resolution. Nothing in `Meta/`, `Models/`, `Core/`, or `Domains/` is changed by this candidate.

Consequences by outcome:
- *Promote to ADR:* `Meta/Value.md` is authored (by the Chief Architect, per this document's own §6 / `CAND-004` precedent — "the CDKO proposes candidates... the Chief Architect authors the actual ADR"), Measurement is integrated as its first Value Kind, and a follow-up item is opened to eventually retype the bare Rate/Duration KPI names already in `Finance_KPIs.md`/`Operations_KPIs.md` — not required for this Decision, named so it isn't concealed.
- *Merged into an existing item:* if the Chief Architect judges this fits inside an Epic not surfaced during evaluation, or is better sequenced as part of one, `AO-005` and this candidate are re-pointed there rather than tracked separately.
- *Closed without ADR:* if the Chief Architect judges the two Reference Cases insufficient, or the boundary better left to Reader/Vector as implementation-specific accommodation (Principle 8's sufficiency test resolved the other way), both `AO-005` and this candidate close with that reasoning recorded in `AO-005`'s Architect Response.

**Next Action:** Chief Architect to review `Concept-Paper-Value-Model.md` and `AO-005`, and record a Decision.

---

## CAND-009

**Title:** Publication Governance Changeset — Freeze Exception for Version-Identity, Normative-Reference-Sourcing, and Release-Metadata Work Exceeding `EPIC-F`'s Literal Scope

**Status:** ✅ Decided — Promoted (Layer 1, Scope Authorization only, 20 August 2026). Path A (Section 6) completed: `AO-008`, grounded in `RC-008` and `RC-009`, recorded before this Decision. This Decision does not certify the underlying changeset's content correct — see Section 7 and Section 8.

**Owner:** Chief Architect

**Created:** 20 August 2026

**Revision note (20 August 2026):** an independent review of this candidate's first draft found eight defects: (i) a quoted test misattributed to Architecture Principle 1 when it is Principle 3's text, reproducing the exact defect class `CAND-007`'s own revision note records as already caught once before; (ii) an elliptical quotation of `CAND-007` §6(c) that silently dropped the clause naming the Reference Case pipeline as required; (iii) Sections 4 and 5 stated several items as already-accomplished fixes ("closes it," "correct... to match") for artifacts this same candidate's own Section 7 lists as still defective; (iv) the `Entities/Overview.md` item was characterized as a routine Status correction without flagging that it also changes the normative enforceability of that document's Conformance content; (v) Section 6 cited `CAND-006` and `CAND-007` as precedent for skipping the Reference Case pipeline, when `CAND-006` predates the pipeline requirement entirely and `CAND-007` cannot be precedent for its own rule; (vi) the Reference Case exclusion was unbounded, with no criteria limiting future filings from invoking the same reasoning; (vii) the Promote outcome's instruction for revising `Master-Architecture-Backlog.md`'s `EPIC-F` Execution note did not require removing language that frames this work as part of `EPIC-F` itself; (viii) this candidate relied on git-commit status as the operative boundary for "not yet adopted," without disclosing that the underlying changeset already edits governed documents in place in the working tree. This is the corrected text; all eight defects were fixed, not merely re-asserted.

**Second revision note (20 August 2026):** a second independent review confirmed all eight defects above were resolved, but found the fixes for (vi) and (vii) left two narrower gaps: the Reference Case waiver this filing had introduced ("Path B") was disclaimed in prose ("sets no precedent") but bound no future evaluator to honor that disclaimer — an assertion, not a mechanism; and the Promote instruction for `EPIC-F`'s Execution note named two phrases to remove but not its central "has been executed via [...]" claim, nor did it require the surviving content be structurally removed from the `## EPIC-F` block. Consistent with Section 6's own conclusion that no valid waiver exists, both are now fixed by removal rather than restriction: **the Reference Case waiver is removed entirely — this filing proposes no alternative to `CAND-007` §5's pipeline, for itself or for any future filing** — and the `EPIC-F` Execution-note instruction now names all three offending phrases for deletion and requires the surviving content be structurally relocated out of the `## EPIC-F` block, not merely reworded in place. The three-layer separation this candidate exists to establish, Scope Authorization / Content Validation / Commit Authorization, remains explicit throughout.

**Related Documents:** `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, `Governance/Release-Workflow.md`, `.github/workflows/ci.yml`, `Governance/Documentation-Standards.md` (Status Taxonomy section), `Entities/Overview.md`, `Domains/Overview.md`, `Core/Manifest.md`, `Specification/01 Introduction.md`, `Governance/Documentation-Debt.md` (`FW-006`, `FW-007`), `Governance/Master-Architecture-Backlog.md` (`EPIC-F`). Filed under `CAND-007` (Architecture Freeze) §5/§6 as a named Freeze exception, not as ordinary Backlog work, specifically in response to `CAND-007` §6(c)'s requirement that work not fitting an Epic's literal scope go through the ADR Candidate pipeline *before* being adopted into the authoritative record.

**Why this filing exists:** an independent scope review of this changeset (20 August 2026) found that the changeset's actual footprint exceeds what `CAND-007` §3 permits for `EPIC-F`. The changeset's working tree, disclosed plainly here rather than minimized, already contains complete edits to governed documents, made before any Decision: `Core/Manifest.md`'s Normative Language section rewritten in place, `Entities/Overview.md`'s Status field changed in the document body, three new Governance documents, and a new CI job. Separately, `Master-Architecture-Backlog.md` currently carries a same-commit "Execution note" asserting the work "has been executed via" the new documents, which is a self-authorization, the specific anti-pattern `CAND-007` §6(c) and §7 exist to prevent ("never adopted directly into a document on the strength of the proposal alone"; "never executed ad hoc outside" the Backlog). This filing requests the authorization `CAND-007` requires. It asks for that authorization to cover the *scope and category* of the drafted work; it does not ask the Chief Architect to certify the drafted work's *content*, and it does not itself authorize committing anything.

**Discussion:**

### 1. What `EPIC-F` actually permits, quoted exactly

`CAND-007` §3's `EPIC-F` bullet: *"Editorial, presentational, and documentation-currency work (`EPIC-F`): refreshing `Specification/`, re-pointing `Adoption/`, closing `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005`."* That is the entire literal grant. It does not mention new Governance documents, new CI jobs, a new Status Taxonomy, a Status change to any Entity document, or a change to `Core/Manifest.md`.

### 2. Item-by-item fit against that list

| Item | Fits `EPIC-F` §3 literally? | Note |
|---|---|---|
| `Specification/01 Introduction.md` RFC 2119 restatement | Yes, arguably | Falls inside "refreshing `Specification/`" |
| `Core/Manifest.md` Normative Language citation | No | Not `Specification/`; a substantive change to a `Core/` document's normative-language section |
| `Governance/Publication-Model.md` (new) | No | Not named in §3; not `Adoption/`, not one of the four named debt items |
| `Governance/Publication-Manifest.md` (new) | No | Same |
| `Governance/Release-Workflow.md` (new) | No | Same |
| `.github/workflows/ci.yml` new job | No | Not editorial/presentational; a new automated enforcement mechanism |
| `Governance/Documentation-Standards.md` Status Taxonomy | No | New interpretive content, not a `Specification/`/`Adoption/` refresh or one of the four named debt items |
| `Entities/Overview.md` Status field | No | Not `Specification/` or `Adoption/`. **Flagged, not just noted:** this is not a bare metadata change — under the Status Taxonomy this same changeset introduces, moving a document from Draft to Informative changes whether its Conformance section and "shall" requirements are treated as enforceable. This item carries more weight than the others in this table and should be evaluated on that basis, not waved through as routine (see Section 5). |
| `Domains/Overview.md` note | Borderline | No Status change, additive note only, closer to "editorial" in spirit, but still not literally named |
| `Governance/Documentation-Debt.md` `FW-006`/`FW-007` | No | New entries, not closure of `DEBT-DOC-001`/`GAP-001`/`FW-002`/`FW-005` (the only four §3 names) |
| `Master-Architecture-Backlog.md` `EPIC-F` Execution note | No | Not content work at all; a same-commit self-authorization, the specific defect this filing exists to correct |

Only one item (the `01 Introduction.md` restatement) fits `EPIC-F` §3 without qualification. Everything else requires this filing.

### 3. The `CAND-007` §6 test, applied

(a) *Does it fit an existing Epic exactly?* No, per the table above, with one exception noted.

(b) *Is it product- or implementation-shaped rather than contract-shaped?* `CAND-007` §6(b) itself names Architecture Principle 1 (Specification Defines Contracts, Not Products) and Architecture Principle 5 (Reader Is Reference, Not Authority) by title, without quoting either. Applying those two Principles directly: none of the items touch Reader, Vector, or any implementation; the new CI job validates Markdown field consistency inside this repository only, with zero new external dependency; every item constrains how this repository's own publication/version/status metadata is written, not how any downstream consumer reads or interprets it. On that basis this reads as contract-shaped, not product-shaped. (Principle 3, "Recording Before Interpretation," separately states a related test — "does it constrain what gets written, or how a written corpus gets read?" — which is consistent with this conclusion but is not itself part of `CAND-007` §6(b)'s test and is cited here only as supporting context, not as the test being applied.)

(c) `CAND-007` §6(c), quoted in full, no elision: *"if it survives both checks, it is treated as a candidate Freeze exception under Section 5 and must go through the full Reference Case → ADR Candidate pipeline, explicitly flagged as such — it is never adopted directly into a document on the strength of the proposal alone."* Two things follow from this, not one: this entry is the required flagging (satisfying the second half), **and** the Reference Case pipeline named in the first half has not been completed. Section 6 below addresses that gap directly rather than treating the test as already satisfied.

### 4. Why each item is proposed

The claims below describe what each item is *intended* to achieve, as drafted. None of them is a claim that the current wording already achieves it correctly — several do not, per Section 7's Content Validation list, which every bullet below is cross-referenced against.

- **`Publication-Model.md`, `Publication-Manifest.md`:** proposed to resolve a real, evidenced problem: `v0.1` (Core Vocabulary), `v1.0` (Constitution), and `v1.0.0` (the only GitHub Release) currently describe three different, overlapping things with no documented relationship, and the Release predates the Constitution by construction (`v1.0.0`'s commit, `f7a33e2`, dated 22 July 2026, predates `Core/Constitution.md`'s addition on 27 July 2026). Without some document stating this, the ambiguity is undocumented, not absent. *(Section 7 lists content defects in both documents; drafted, not verified correct.)*
- **`Release-Workflow.md`:** proposed to resolve the absence of any single stated path from a document change to a verified public release. *(Section 7 lists two internal self-contradictions in this document; drafted, not verified correct.)*
- **The new CI job:** proposed so that Manifest/Specification/Status consistency is checked automatically rather than aspirationally, since undetected drift is what produced the `v1.0.0` mislabeling in the first place. *(Independently confirmed to execute correctly against the current repository state; this is the one item where "proposed" and "verified working" currently coincide, though its plan-conformance and fail-open behavior have separate non-blocking notes from that review.)*
- **The Status Taxonomy section:** proposed because `Entities/Overview.md`'s Status question (below) cannot be evaluated against an undefined taxonomy. *(Section 7 lists a factual inaccuracy in this section's own Draft-directory list; drafted, not verified correct.)*
- **`Core/Manifest.md`'s RFC 2119/8174 citation:** proposed to single-source a definition the original re-verification found independently duplicated, uncited, in `01 Introduction.md`. *(Section 7 lists a self-contradiction in the drafted text: it cites RFC 8174's all-capitals restriction and then states lowercase forms carry identical meaning, negating the restriction just cited. This is not resolved by this filing.)*
- **`Entities/Overview.md`'s Status field:** proposed because `Constitution-Step0-Summary.md` Decision 4 excludes `Entities/` from Constitution §9's Core scope, and the prior `Draft` status had never been reconciled with that. *(Section 7 lists two separate concerns here: the note's characterization of Decision 4 drops its actual hedge, "mixed, mostly domain-specific," and — per the Section 2 flag above — the Status change's effect on Conformance-content enforceability has not been separately argued. Neither is resolved by this filing.)*
- **`Documentation-Debt.md` `FW-006`/`FW-007`:** proposed to record two real, otherwise-unrecorded residual gaps (no exposed external Publication-Engine commit marker; no correctly-scoped release cut yet), consistent with Governance Principle 8 (Minimal Technical Debt: "Documentation debt shall be explicitly recorded rather than left implicit"). *(Minor factual notes from that review, non-blocking.)*

### 5. Why each item is scoped as governance/documentation work, not Core work

None of the above, as proposed, adds a Meta Object, a Canonical Principle, a new Entity type, a new Domain, a new AI capability, or changes the Object/Memory/Evidence/Knowledge derivation direction, the specific things `CAND-007` §4 forbids outright regardless of Section 5/6. Every artifact either describes a relationship between already-existing documents (`Publication-Model.md`, `Publication-Manifest.md`, `Release-Workflow.md`), enforces an already-stated field format with plain bash (the CI job), or is scoped as a correction to a Status/citation field to align with an already-recorded Decision (`Entities/Overview.md`, `Core/Manifest.md`) — "scoped as," not "verified to already be," per Section 4. A dedicated scope-creep search of the full diff, run independently as part of that review, found zero structural or semantic changes to Object, Memory, Evidence, Knowledge, `CAND-008`, or `EPIC-E`, only incidental prose mentions.

**One qualification, carried over from Section 2:** the `Entities/Overview.md` item is the least clean fit in this list. Reclassifying a document's Status under the newly-introduced Taxonomy changes whether its own normative content (18 mandatory sections, a Conformance clause) is treated as enforceable — closer to a question about that Entity type's conformance regime than to pure publication metadata. This filing does not withdraw the item, but does not ask the Chief Architect to wave it through with the other, cleaner items either; it should be considered on its own terms, and the Chief Architect may Promote the remainder of this filing while holding this one item for separate review without that being a partial rejection of the rest.

### 6. The Reference Case requirement — full pipeline, Repeated Pattern included, no shortcut

`CAND-007` §5's operative sentence on escalation, quoted verbatim (not §5 in its entirety — §5's opening sentence states the qualifying bar for a Freeze exception generally, and its remaining two paragraphs name two already-identified exception candidates and a separate Milestone-4 trigger; neither bears on this filing's own path and neither is reproduced here): *"Meeting that bar does not itself authorize a change. It authorizes escalation through the existing pipeline (`Standard Evolution Methodology.md`: Reference Case → Repeated Pattern → ADR Candidate → Chief Architect Decision), with the escalation explicitly labeled a Freeze exception at the point it is raised — never absorbed silently into ordinary Backlog work."* No Reference Case (per `Standard Evolution Methodology.md` Section 3's template) and no corresponding `Architecture-Observations.md` entry currently exists for this changeset.

An honest check of whether any prior Decision excuses that gap, checking each candidate precedent directly rather than assuming one applies:

- **`CAND-006`** (the Constitution) was decided 26 July 2026, one day *before* `CAND-007` (27 July 2026) created the §5/§6 mechanism this filing invokes. It cannot be precedent for complying with, or being exempt from, a rule that did not yet exist when it was decided. Separately, `CAND-006` installs all fourteen Canonical Principles — it is the paradigm Core-modeling document, not a governance/process decision, so it would not support a "governance/process filings skip Reference Cases" reading even if the dates permitted the comparison.
- **`CAND-007`** cannot be cited as precedent for compliance with a rule it is itself the source of; that is circular.
- **`CAND-008`**, the only Freeze exception actually filed and evaluated under `CAND-007` §5/§6 to date, used the full pipeline: `AO-005`, grounded in **two** independent Reference Cases (`RC-006`, `RC-007`), forming a Repeated Pattern, before being escalated to an ADR Candidate. As the one real, tested precedent on record, it did not treat a single Reference Case as sufficient.

No valid precedent currently exists for skipping the Reference Case step, or the Repeated Pattern step, for a Freeze exception. **This filing does not claim one, and does not propose a waiver, exception, or any alternative to `CAND-007` §5's pipeline — for itself or for any future filing.** An earlier revision of this candidate offered a "Path B" one-time-waiver option; it was removed, not narrowed, because its only containment was disclaiming prose, which binds no future evaluator.

**Does the Repeated Pattern stage apply to a non-Core, governance/documentation Freeze exception specifically?** Checked directly, not assumed: `Standard Evolution Methodology.md`'s own Rules 1–2 ("Core **SHALL NOT** be extended on the basis of a single Reference Case"; "Proposed Core extensions **SHOULD** be supported by multiple independent Reference Cases") name "Core" explicitly, and the Methodology's own "Relationship to OCOM Specification" section states it "defines only the process by which evidence is gathered and, where warranted, escalated toward *a Core decision*." This filing is not a Core decision (Section 5). Read narrowly, Rules 1–2's specific multi-Reference-Case mandate could be argued inapplicable here on that basis. But `CAND-007` §5 borrows the same named pipeline, including Repeated Pattern, as its own mechanism for authorizing *any* Freeze exception, without itself stating a carve-out for non-Core work, and Methodology Rule 3 ("Architectural Observations **SHALL** be recorded... before any architectural decision is made") is not Core-limited in its own wording. No document in this repository resolves this tension explicitly for a non-Core Freeze exception; this is a genuinely open, first-instance question, not a settled one. **This filing does not resolve it by assumption.** Asserting the narrower reading (Repeated Pattern inapplicable here) would itself be introducing a new interpretive carve-out on this filing's own authority — exactly what this filing exists to stop happening. The strict, no-assumptions reading is therefore the literal one: `CAND-007` §5's quoted pipeline applies to this filing in full, Repeated Pattern included.

**Path A — the full pipeline, Repeated Pattern included.** Two independent sources of evidence already exist from earlier work on this repository. Neither has yet been formally written up as a Reference Case per `Standard Evolution Methodology.md`'s Section 3 template; both are described here, specifically, as the material Path A's two Reference Cases would be authored from:

- **Candidate Reference Case 1 — the external audit report.** *Source:* an external audit report, provided by the Chief Architect. Its own author and tooling are `not established in this filing`. *Date/period:* provided prior to this filing; the report's own preparation date is `not established in this filing`. *What was checked:* an eleven-point comparison of the live `ocom.uno` site against the canonical OCOM GitHub repository, covering version identifiers, publication content, and structural claims. *Result:* found multiple discrepancies between the live site and the repository; the report explicitly self-flagged three of its own eleven findings as unconfirmed ("[unconfirmed]") and requested independent re-verification.
- **Candidate Reference Case 2 — an independent verification pass.** *Source:* an independent three-part verification pass, undertaken specifically to re-verify Reference Case 1's findings — one part reading the local repository directly, one reading the live `ocom.uno` site, one querying the GitHub API. *Date/period:* 20 August 2026. *What was checked:* the same overall question (version-identity/publication consistency between `ocom.uno` and the repository), using direct repository, site, and API access rather than Reference Case 1's own (undisclosed) method. *Result:* confirmed most of Reference Case 1's findings, and corrected its most significant error — Reference Case 1 stated no GitHub tag or release existed; direct GitHub API access found that a real tag/release (`v1.0.0`) does exist, cut before Constitution v1.0 was adopted, a materially different and more severe finding than Reference Case 1 reached.
- **Why the two are independent of each other:** Reference Case 2's method is specifically known and independently verifiable — direct repository, site, and GitHub API access via an independent three-part verification pass — considered entirely on its own terms, not as a claimed contrast to Reference Case 1's method, which is `not established in this filing`. Independence is instead evidenced by result: Reference Case 2 reached a materially different, corrective conclusion — that a real GitHub tag/release exists, contradicting Reference Case 1's own claim on that specific point — rather than reproducing Reference Case 1's findings. Two reports of one underlying investigation would be expected to agree; Reference Case 2 instead corrected Reference Case 1's central claim, which is evidence against them being "repeated submissions of the same underlying case," per Methodology Rule 2's own test. **Neither authorship nor subject-matter distinctness is offered as a ground here** — both Reference Cases examined the same overall question (version-identity/publication consistency between `ocom.uno` and the repository), and Reference Case 1's own author is `not established in this filing`. Independence rests solely on Reference Case 2's own verifiable method and its corrective, non-reproducing result.

These two independent sources are offered as the basis for satisfying the independence requirement of Rule 2. These two sources are proposed as the evidence base for establishing a Repeated Pattern; the formal observation record has not yet been created. Formal Reference Case records, per the template in `Standard Evolution Methodology.md`'s "Reference Case Methodology" section (Purpose / Expressive Coverage / Boundary Conditions / Boundary Tags / External Assurance / Core Impact / Decision fields, tagged `repository-scope` from the Controlled Boundary Vocabulary — *"the boundary is specific to how this specification's repository is organized, not to the OCOM model itself"*, the closest-fitting existing tag), remain to be authored and recorded as a single `Architecture-Observations.md` entry, per Methodology Rule 3, before returning to this candidate for a Chief Architect Decision.

**Current status of Path A: not yet completed.** Two independent sources of evidence exist, described above; neither has been formally written up as a Reference Case per the template, and no `Architecture-Observations.md` entry exists for this changeset as of this revision. Completing that write-up is out of scope for this edit, which is limited to this entry in `ADR-Candidates.md`. This filing does not treat the existence of the underlying evidence as equivalent to having completed Rules 3–4, and, per the preceding paragraph, does not treat it as already satisfying Rule 2 either — only as the proposed basis for satisfying it once formally written up.

**Consequence: this filing is not yet ready for a Chief Architect Decision.** Completing both Reference Cases and recording them as a single `Architecture-Observations.md` entry is a prerequisite, to be done separately, before this candidate returns for Decision. This now precisely follows the same sequence `CAND-008` itself followed: `AO-005`, grounded in two independent Reference Cases (`RC-006`, `RC-007`), existed before `CAND-008` was filed as a Decision-ready candidate — not an approximation of that precedent, the same shape. Section 8's Decision Text is written for that later point, not for use now.

### 7. Three separate questions, kept explicitly separate

**Layer 1 — Scope Authorization (what this filing asks for):** that the items in Section 2 fall within governance/documentation scope, per Sections 3 and 5, and may proceed under `CAND-007` §5/§6 as a Freeze exception, with the `Entities/Overview.md` item considered on its own terms per Section 5's qualification, and with Section 6's Path A (both Reference Cases, forming a Repeated Pattern) completed first — not resolved by choice, completed as a precondition.

**Layer 2 — Content Validation (not asked for here, and not granted by any Promote decision):** the same review that produced this filing separately found ten content-level defects in the currently-drafted changeset: a self-contradiction in `Core/Manifest.md`'s RFC 8174 citation; a misrepresentation of Decision 4's actual (hedged) wording in `Entities/Overview.md`; a Status Taxonomy Draft-directory list that omits the three largest Draft populations in the repository; two internal self-contradictions in `Release-Workflow.md`; a `Publication-Model.md` version claim uncaveated against a live-site discrepancy; a `Publication-Manifest.md` reference to a field `Publication-Model.md` claims exists but does not; a Core-Vocabulary-version ambiguity across two different file sets; a factual date error in the drafted `v1.0.0` release note; a sequencing risk in that same note; and the Section 2/5 `Entities/Overview.md` conformance-regime concern noted above. None of these is resolved by a Promote decision on this filing. They are tracked and require independent correction and independent verification before Layer 3.

**Layer 3 — Commit Authorization (not asked for here, and cannot occur before Layer 2 is separately closed):** no part of the underlying changeset may be committed on the strength of a Promote decision on this filing alone. A separate, explicit confirmation that Layer 2's defect list has been closed is required first.

Consequences by outcome (available only once Section 6's Path A is complete):
- *Promote:* Layer 1 only is granted, for the items in Section 2 (with the `Entities/Overview.md` qualification from Section 5 in force), as a **standing Freeze exception under `CAND-007` §5/§6, filed and tracked separately from `EPIC-F`**. `Master-Architecture-Backlog.md`'s `EPIC-F` entry is *not* widened: its `Documents affected` and `Definition of Done` fields remain exactly as recorded before this filing. The current `EPIC-F` "Execution note" is **not edited in place — it is removed and replaced**, specifically:
  (i) the phrase *"the publication-governance slice of this Epic"* is deleted, not reworded;
  (ii) any framing that this work *"closes... a portion of `EPIC-F`'s own goal"* is deleted, not reworded;
  (iii) the specific phrase *"has been executed via `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, and `Governance/Release-Workflow.md`"* is deleted outright — no rewording that preserves an already-executed claim is acceptable while Layer 2 and Layer 3 remain open;
  (iv) the surviving content is not kept under the label "Execution note" inside the `## EPIC-F` block — it is either relocated to a new, separate "Freeze Exceptions" tracking section in `Master-Architecture-Backlog.md`, outside any Epic's own block, with at most one line left inside `EPIC-F`'s block reading "See Freeze Exceptions: `CAND-009`" and nothing further, **or** removed from `Master-Architecture-Backlog.md` entirely, with this `CAND-009` entry in `ADR-Candidates.md` serving as the sole authoritative record of the exception.
  Layers 2 and 3 remain open, tracked independently, per the Decision Text in Section 8.
- *Merged into an existing item:* if the Chief Architect judges some or all of this fits better as a formal, scoped addition to `EPIC-F` itself, `Master-Architecture-Backlog.md`'s `Documents affected` and `Definition of Done` fields are updated accordingly, as their own explicit edit, and this candidate is re-pointed there. This is the only outcome under which `EPIC-F`'s own scope changes.
- *Closed without promotion:* if the Chief Architect judges this work should not proceed under the Freeze at all in its current form, the changeset is held pending a post-Freeze review, per `CAND-007` §8.

### 8. Proposed Decision Text (for Chief Architect use, once Path A is complete — not usable now)

**Not usable until Section 6's Path A is complete.** No alternative path exists; this text has an empty, mandatory `Reference Cases` field for exactly that reason, and must not be signed with that field unfilled.

```text
Decision: CAND-009 — Promote (Layer 1, Scope Authorization, only)

Decided: [date]
Decided by: Chief Architect
Reference Cases: [Architecture-Observations.md entry ID and date —
  Path A, both Reference Cases (Section 6) completed and recorded
  together as one Observation, prior to this Decision. Mandatory;
  no alternative path exists. Do not sign with this field empty.]

This Decision authorizes the CATEGORY and SCOPE of work described in
CAND-009 Section 2 (the item-by-item EPIC-F fit table), with the
Entities/Overview.md item considered per Section 5's qualification,
as a standing Freeze exception under CAND-007 Section 5/6, tracked
separately from EPIC-F.

This Decision does NOT:
  - certify that any document currently drafted in the working tree
    is factually, logically, or normatively correct;
  - close, resolve, or supersede any of the Layer 2 (Content
    Validation) defects listed in CAND-009 Section 7;
  - authorize commit or push of any file in the underlying changeset;
  - extend, redefine, or widen EPIC-F's own "Documents affected" or
    "Definition of Done" fields in Master-Architecture-Backlog.md.

Action taken immediately as part of THIS Decision, at Layer 1 —
not deferred, not conditioned on Layer 2 or Layer 3: Master-
Architecture-Backlog.md's EPIC-F Execution note is removed and
replaced per CAND-009 Section 7's Promote consequence, items (i)-(iv).

Before any part of the underlying changeset may be committed:
  1. Every Layer 2 defect named in CAND-009 Section 7 must be
     independently fixed and re-verified.
  2. [Verification, not a trigger] Confirm the EPIC-F Execution-note
     replacement above was in fact carried out — this checks that the
     Layer 1 action happened, it is not the point at which it happens.
  3. A separate, explicit Layer 3 confirmation ("content now correct,
     ready to commit"), covering every Layer 2 defect named in
     CAND-009 Section 7, is required and is distinct from this
     Decision.

Next Action: CDKO executes the EPIC-F Execution-note replacement
immediately upon this Decision, then tracks the Layer 2 defect list
as a separate, checkable item before requesting Layer 3 authorization.
```

**Governance implication of this Decision:** mirroring `CAND-007`'s own framing of its Decision (*"a process/lifecycle decision, not a modeling decision... introduces no new Meta Object, no new Canonical Principle, and no new Epic"*), this is a process/authorization decision, not a modeling decision. Deciding it consistent with `Governance-Manifest.md` Principle 2 (Architecture Before Implementation) and Principle 5 (Decision Transparency) means the authorization, and confirmation that Section 6's Path A is complete, are recorded here, before the changeset is committed, not reconstructed afterward from the changeset's own text.

**Next Action:** Complete Section 6's Path A — author both Reference Cases per `Standard Evolution Methodology.md`'s template, tagged `repository-scope`, and record them together as one `Architecture-Observations.md` entry. This is a separate step, outside this revision's scope (limited to this entry in `ADR-Candidates.md`). Once complete, the Chief Architect reviews this Candidate together with that entry and records a Layer 1 Decision using Section 8's text. Independently of that Decision, the Layer 2 defect list in Section 7 must be closed, and a separate Layer 3 confirmation obtained, before any part of the underlying changeset is committed.

---

## CAND-010 — ✅ Decided

**Title:** Authorize one universal Informative Worked Example under docs/Adoption/

**Status:** Decided — Promote — Scope Authorization Only (21 August 2026)

**Owner:** Chief Architect

**Created:** 21 August 2026 · **Decided:** 21 August 2026

**Why this does not require the Reference Case → ADR Candidate pipeline:** Per `CAND-007` §7, items newly approved under §6 are "added to the Backlog, under an existing Epic where it fits." This item is an instance of the kind of work `EPIC-F` already does (re-pointing `Adoption/`, closing small content gaps) — not a new category, unlike `CAND-008` (Value Model) or `CAND-009` (publication governance), both of which needed the full pipeline because no existing Epic covered that kind of work at all. This entry exists to give the authorization a real, citable Decision record with its own Status lifecycle — not because §5's Freeze-exception bar is met.

**Related Documents:** `Master-Architecture-Backlog.md` (`EPIC-F`, and §7's Backlog-addition mechanism), `CAND-007` §3/§6/§7, `Adoption/README.md`, `Examples/Overview.md` ("Organization" section — grounds why this belongs under `Adoption/`, not `Examples/`), `Governance/Documentation-Standards.md` (Status Taxonomy — Informative definition).

**Decision:**

Authorize the addition of exactly one file, `docs/Adoption/Worked Example - Library Lending.md`, as a new `EPIC-F` work item.

Scope:
- one static worked example;
- Status: Informative;
- domain-neutral (no industry, no company, no real data);
- hand-authored, illustrative only;
- no normative changes;
- no Reference Implementation;
- no Conformance claims.

This decision does not:
- modify Core/Meta/Models;
- modify `CAND-008`;
- create new types, enums, cardinalities, or schema rules;
- change the Object Model;
- authorize additional Adoption artifacts beyond this one example.

**Scope authorization only — explicitly not asserted by this Decision:**
- that the content of the Worked Example is already correct;
- that the chosen Library Lending domain is the only valid choice;
- that Shape Check has received any authorization of any kind;
- that `EPIC-F` is automatically extended to any other Adoption artifact beyond this one file.

**Governance implication of this Decision:**
- A second or future worked example is a new `EPIC-F` work item requiring its own amendment and, if precedent is by then established, may not need a new CAND entry at all — that is a future question, not decided here.
- This Decision does not touch `Examples/Overview.md`'s industry-collection scope, `CAND-009`, or any Shape Check design work.

**Next Action:** Executed same-session, per author instruction: the corresponding `EPIC-F` scope amendment in `Master-Architecture-Backlog.md` is applied, and `docs/Adoption/Worked Example - Library Lending.md` is authored per the Library Lending design. Neither step draws on any authority beyond what this Decision records above.

---

## CAND-011 — ✅ Decided

**Title:** Authorize `docs/Adoption/First Pilot.md` as an Adoption Projection, with presentation-level navigation adaptation for the compiled /adoption/first-pilot page

**Status:** Decided — Promote (21 August 2026)

**Owner:** Chief Architect

**Created:** 21 August 2026 · **Decided:** 21 August 2026

**Revision note (21 August 2026):** a final focused review, run after `CAND-012` was decided, found this candidate's original draft authorized only the presentation-adaptation question and never stated the base grant `CAND-012`'s own Scope condition 2 requires ("that specific file has its own individual Decision authorizing it as an Adoption Projection"). Fixed below by adding an explicit base-grant clause, mirroring `CAND-010`'s own structure, and an explicit Decision Boundary clause separating publication authorization from content correctness, mirroring `CAND-012`'s own. Both fields verified directly against `docs/Adoption/First Pilot.md`'s current header, not assumed from memory.

**Why this does not require the Reference Case pipeline:** Same reasoning `CAND-010` already established — this is an instance of already-authorized Adoption-compilation work (per `CAND-010`'s own precedent for Worked Example, and per `CAND-012`'s own recognition of Adoption as a second Projection-tier instance), not a new kind of decision.

**Related Documents:** `CAND-010`, `CAND-012`, `First Pilot.md`, `Adoption/README.md` ("How to Read These Documents" — the sequence this adaptation breaks).

**Decision:**

Authorize `docs/Adoption/First Pilot.md` as an Adoption Projection under `CAND-012`.

Base grant (mirroring `CAND-010`'s structure for the one prior instance):
- Scope: exactly one file, `docs/Adoption/First Pilot.md`;
- Status: Informative (confirmed in the file's own header);
- Version: 0.1 (confirmed in the file's own header);
- hand-authored, pre-existing text — no new content is introduced by this Decision;
- canonical source remains GitHub; the compiled page is a projection, never edited directly.

Presentation-level adaptation, authorized for the compiled /adoption/first-pilot page only:
- omission of Back/Next navigation controls (Getting Started.md, FAQ.md are not being published);
- de-linkification of the "Getting Started.md §4" citation in Suggested Steps, step 3, to a plain, non-clickable parenthetical note.

This decision does not:
- modify `docs/Adoption/First Pilot.md` itself (canonical text unchanged);
- authorize `Getting Started.md`, `FAQ.md`, `Common Mistakes.md`, or `Adoption/README.md`;
- authorize navigation adaptation for any other Adoption file;
- extend `CAND-010`'s own scope or non-assertions;
- change Shape Check in any way;
- change the OCOM Specification, Core, Meta, Models, or Governance model.

**Decision Boundary:** This Decision authorizes publication (Projection status, plus the specific presentation adaptation above) only. It does not certify the factual, semantic, normative, or editorial correctness of First Pilot.md's content — that remains subject to its own, separate content/governance review.

**Governance implication:** Any future compiled Adoption page facing the same kind of dependency gap needs its own explicit instance of this reasoning — this is not a general policy, per file, per decision.

**Next Action:** /adoption/first-pilot may be published with this exact adaptation, disclosed in the page's own footer note.

---

## CAND-012 — ✅ Decided

**Title:** Recognize Adoption pages as a second instance of the existing Projection tier

**Status:** Decided — Promote — Scope / Publication Architecture Authorization (21 August 2026)

**Owner:** Chief Architect

**Created:** 21 August 2026 · **Decided:** 21 August 2026

**Why this does not require the Reference Case pipeline:** `Publication-Model.md` already defines a generic third publication tier, "Projection" — a machine-generated representation of a single canonical document, currently instantiated once (Core Vocabulary term-cards, generated from `Meta/`). This Decision recognizes a second instance of that same, already-existing tier. It does not create a new tier, layer, or publication concept, and is accordingly filed as an ordinary Decision rather than a `CAND-007` §5/§6 Freeze exception.

**Related Documents:** `CAND-010`, `CAND-011` (unchanged by this Decision), `Publication-Model.md` (tier 3 wording generalized per this Decision).

**Decision:**

CAND-012 is Promoted.

This Decision recognizes Adoption pages as a second instance of the existing Projection tier defined by the OCOM Publication Model.

This Decision authorizes only the publication architecture described by CAND-012.

**Scope**

The authorization applies only when both conditions are satisfied:

1. The source is an explicitly identified file under `docs/Adoption/`.
2. That specific file has its own individual Decision authorizing it as an Adoption Projection.

No blanket authorization of `docs/Adoption/` is granted.

**Currently authorized Projection instances**

The following files are recognized as Adoption Projections only under their existing individual Decisions:

- `docs/Adoption/Worked Example - Library Lending.md` — CAND-010
- `docs/Adoption/First Pilot.md` — CAND-011

No other Adoption file is authorized by this Decision.

**Editorial note (recorded at filing, superseded 21 August 2026):** at the time this Decision was recorded, `CAND-011` was Status: Proposed, and `docs/Adoption/First Pilot.md` did not yet qualify as an Adoption Projection under this Decision's own Scope test (condition 2). `CAND-011` was Decided the same day, correcting its original draft to include the base grant this Scope condition requires — `docs/Adoption/First Pilot.md` now qualifies. No amendment to this entry was needed, per the note's own original prediction.

**Non-authorization**

This Decision does not:

- authorize `Getting Started.md`;
- authorize `FAQ.md`;
- authorize `Common Mistakes.md`;
- authorize `Adoption/README.md`;
- authorize any future file under `docs/Adoption/` without its own individual Decision;
- grant Shape Check Projection status;
- establish Shape Check as a canonical OCOM repository artifact;
- change the OCOM Specification, Core, Meta, Models, Memory, Evidence, or Governance model.

**Canonical Source**

GitHub remains the canonical source for every Adoption Projection.

The production representation at `ocom.uno/adoption/*` is a projection only.

Changes must be made to the canonical source document and subsequently reflected through the Publication Engine.

**Publication-Model consequence**

Following this Decision, the Projection tier definition in `Publication-Model.md` may be generalized from its current single-instance wording to:

A Projection is a machine-generated representation of a single canonical document.

This wording does not create a new publication tier. It defines the existing boundary of the Projection tier sufficiently to represent both its current Core Vocabulary instance and the newly recognized Adoption instance.

**Decision Boundary**

This Decision authorizes publication architecture only.

It does not certify the factual, semantic, normative, editorial, or implementation correctness of any individual Adoption document.

Individual Adoption documents remain subject to their own content, status, and governance decisions.

**Next Action**

Update `Publication-Model.md` only as required to reflect this Decision.

No other Adoption file is authorized or published by this Decision.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial queue, 1 candidate |
| 0.1 | 22 July 2026 | Added CAND-002 (set-scoped Conformance), referenced from `docs/Specification/08 Conformance.md` |
| 0.1 | 22 July 2026 | Migrated both candidates to the uniform ID/Title/Status/Owner/Created/Related Documents/Discussion/Next Action lifecycle |
| 0.1 | 23 July 2026 | Added CAND-003 (Principle 11 — Separation of Professional Responsibility), submitted directly per author direction, bypassing the Reference Case stage |
| 0.1 | 23 July 2026 | Added CAND-004 (Organizational Boundaries) — number contingent on CAND-003 resolution; recorded that "Workspace" and `Meta/Organization.md` do not currently exist in the repository |
| 0.1 | 23 July 2026 | CAND-003: Decision recorded — Promote to ADR (becomes Core Principle 11); Core integration deferred to a separate task |
| 0.1 | 23 July 2026 | CAND-004: revised to remove Workspace framing; added Option A/B comparative analysis and three-way impact assessment |
| 0.1 | 23 July 2026 | CAND-003: marked Integrated — Core integration completed across 6 documents |
| 0.1 | 23 July 2026 | Added CAND-005 (Organization vs Domain as the Top-Level Architectural Boundary) — marked Blocking; CAND-004 marked Blocked pending its resolution |
| 0.1 | 23 July 2026 | CAND-005: Decision recorded — Option C (Organization as a first-class peer specialization of Object, connected via Relationship, not a new layer). CAND-004 marked Superseded, queued for rework as "Modeling Cross-Organization Relationships." |
| 0.1 | 23 July 2026 | CAND-004: fully rewritten as "Modeling Cross-Organization Relationships," on the CAND-005 Option C basis — old Organization-vs-Domain framing replaced with 7 research questions (relationship types, ownership, cross-org references, shared objects, memory, registry, AI) and a revised impact assessment |
| 0.1 | 26 July 2026 | Added CAND-006 (OCOM Constitution — Foundational Principles) — Decision recorded, adopted as v1.0. Fourteen Canonical Principles plus Architectural, Implementation, and Meta-Principles; establishes that future changes go through this same ADR Candidate process and that new proposals are evaluated against the Constitution, not the reverse. Core integration deferred to a separate, not-yet-authorized task. |
| 0.1 | 27 July 2026 | Added CAND-007 (Architecture Freeze for OCOM v1.0) — Decision recorded, adopted. Formalizes the transition from Architecture Discovery to Architecture Stabilization: architectural discovery considered complete per four independent adversarial search passes finding no new root-shape question; `Master-Architecture-Backlog.md` becomes the sole source of architectural work; permitted/forbidden changes, Freeze-exception criteria, new-proposal evaluation order, and post-v1.0 unfreeze criteria all recorded. No new Meta Object, Canonical Principle, or Epic introduced. |
| 0.1 | 29 July 2026 | Added CAND-008 (OCOM Value Model, with Measurement as its first realized Value Kind) — filed as a named Freeze exception under `CAND-007` §5/§6, on evidence from `AO-005` (`RC-006`, `RC-007`); full design attached as `Concept-Paper-Value-Model.md`; Decision pending |
| 0.1 | 20 August 2026 | Added CAND-009 (Publication Governance Changeset — Freeze Exception) — filed as a named Freeze exception under `CAND-007` §5/§6, requesting authorization for the portion of the Publication Governance changeset that exceeds `EPIC-F`'s literal §3 scope, prompted by a scope review finding the changeset had self-authorized via a same-commit `Master-Architecture-Backlog.md` Execution note; Decision pending; does not certify the changeset's content correctness, tracked separately |
| 0.1 | 20 August 2026 | Revised CAND-009 — independent review of the first draft found eight defects (misattributed Principle quote, an elliptical §6(c) quote, correctness claims for content later listed as defective, an under-flagged Entities/ conformance-regime effect, a false CAND-006/CAND-007 precedent claim, an unbounded Reference Case exclusion, an EPIC-F-widening risk in the Promote consequence, and an unexamined "committed" vs. "adopted" substitution); all eight fixed, three-layer Scope Authorization / Content Validation / Commit Authorization structure made explicit throughout, Reference Case question resolved as an explicit Path A/Path B choice for the Chief Architect rather than a claimed precedent |
| 0.1 | 20 August 2026 | Revised CAND-009 a second time — a second independent review confirmed all eight prior defects resolved but found "Path B" (the Reference Case waiver) contained only by prose disclaimer, not by any mechanism binding future evaluators, and found the EPIC-F Execution-note-rewrite instruction incomplete (didn't name the "has been executed via" phrase, didn't require structural removal from the EPIC-F block). Path B removed entirely, no alternative to CAND-007 §5's Reference Case pipeline offered; Candidate now explicitly marked not Decision-ready pending Path A completion. EPIC-F Promote instruction rewritten to require deleting all three offending phrases outright and relocating or removing the note from the EPIC-F block, not editing it in place |
| 0.1 | 20 August 2026 | Revised CAND-009 a third time — a focused review of the Path-B-removal edit found Section 6's Path A described only one Reference Case despite quoting CAND-007 §5's full four-stage pipeline (Reference Case → Repeated Pattern → ADR Candidate → Chief Architect Decision) and despite Section 6 itself correctly noting CAND-008's actual precedent used two, forming a Repeated Pattern — an internal inconsistency, not a false compliance claim. Checked Standard Evolution Methodology.md's Rules 1-2 and its own Core-decision self-scoping directly rather than assuming an exemption; found no clean textual carve-out for non-Core Freeze exceptions, so Path A now requires two independent Reference Cases (grounded in the external audit and the independent Workflow re-verification respectively), forming a Repeated Pattern, recorded as one Architecture-Observations.md entry — matching CAND-008's actual precedent exactly rather than approximating it. No new waiver or exemption introduced. Also fixed: the "§5 quoted in full" label now states precisely what is and isn't quoted; Section 8's Decision Text now states the EPIC-F Execution-note replacement is a Layer 1 action taken at Promote time, with the pre-commit checklist item verifying it happened rather than triggering it |
| 0.1 | 20 August 2026 | Revised CAND-009 a fourth time — a focused review of the Repeated Pattern fix found Section 6 claimed its two proposed Reference Cases were "already cited throughout this filing," which did not check out against the document's own text (neither source was actually described anywhere earlier in the filing), and prematurely asserted Methodology Rule 2 compliance while, one sentence later, correctly disclaiming Rules 3-4 compliance for the same unformalized material — an internal inconsistency in how much weight the same evidence was given from one sentence to the next. Fixed by removing the "already cited" claim and giving each candidate Reference Case its own specific, honestly-hedged description (source, date/period, what was checked, result, and why it is independent of the other), marking anything not actually established in this filing as such rather than guessing; and by replacing the premature Rule 2 compliance claim with "these two independent sources are offered as the basis for satisfying the independence requirement of Rule 2; formal Reference Case records remain to be created under Rules 3-4." No change to Section 8 or any other Section |
| 0.1 | 20 August 2026 | Revised CAND-009 a fifth time — a focused review found the independence bullet's "distinct authorship (an external party vs. this engagement's own Workflow tooling)" contradicted Reference Case 1's own description two lines earlier, which states authorship is not established in this filing — the same one-sentence-later inconsistency pattern recurring in a new location. Fixed conservatively: removed authorship as a ground for independence entirely (not softened to "presumed external" — dropped outright), keeping only method and subject/result differences, which the filing's own text actually supports; explicitly stated authorship is not offered as a ground, since it is not established. Also replaced "forming this filing's Repeated Pattern" (present tense, could read as already-formed) with "proposed as the evidence base for establishing a Repeated Pattern; the formal observation record has not yet been created," and corrected "records... under Rules 3-4" to cite Standard Evolution Methodology.md's "Reference Case Methodology" section by name, where the template obligation actually lives. No other change |
| 0.1 | 20 August 2026 | Revised CAND-009 a sixth time — a focused review found the "method" and "subject" grounds substituted for authorship in the fifth revision reproduced the identical defect: "distinct method" claimed a contrast against Reference Case 1's method, which the same sentence admits is not established, and "distinct subject" directly contradicted Reference Case 2's own "What was checked" field, which states both examined "the same overall question." Fixed by dropping every comparative claim against an unestablished or explicitly-shared property: independence is now grounded only in facts established for BOTH sides — Reference Case 2's own method considered on its own terms (not contrasted with Reference Case 1's, since that is unknown), and the two Reference Cases' divergent, established results (Reference Case 2 corrected rather than reproduced Reference Case 1's central claim) — with authorship and subject-matter distinctness both explicitly disclaimed as grounds |
| 0.1 | 21 August 2026 | Added CAND-011 (presentation-level navigation adaptation for /adoption/first-pilot) — Status: Proposed, awaiting Chief Architect Decision. Scoped explicitly narrower than CAND-010: authorizes adaptation of one file's presentation for one compiled page only, not new content; does not modify First Pilot.md itself |
| 0.1 | 21 August 2026 | Added CAND-012 (Adoption pages as a second instance of the existing Projection tier) — Status: Decided — Promote, Scope / Publication Architecture Authorization. Reclassified from an earlier "Compiled Publication tier" framing after independent review found the mechanical shape (single source file → HTML + source_file/source_url/history_url) matches the Projection tier, not the multi-source Compiled Publication tier. Authorization is conditional per-file (directory membership under docs/Adoption/ plus an individual Decision); currently covers Worked Example (CAND-010) and, once decided, First Pilot (CAND-011 — noted as not yet Decided at time of this filing). Explicitly excludes Shape Check and Getting Started/FAQ/Common Mistakes/README. Next Action: generalize Publication-Model.md's tier 3 wording only |

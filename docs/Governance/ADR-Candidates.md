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

**Organization** describes an independent participant in the ecosystem — for example UBT, Traffic Titans, AffVector, a PSP, a Supplier, a Regulator, a customer company. Organization is a first-class Object, at the same architectural level as Entity, Domain, Workflow, Event, Policy, and Contract — not superior to them, not a container for them.

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

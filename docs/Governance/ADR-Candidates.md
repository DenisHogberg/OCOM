<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / ADR Candidates

[↑ Up](README.md) · [Next →](Architecture-Health.md)

---
<!-- nav:end -->

# ADR Candidates

**Document ID:** GOV-ADR-CANDIDATES-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

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

**Title:** Principle 12 — Organizational Boundaries (provisional number: CAND-003 now occupies 11; this candidate is still undecided)

**Status:** Blocked — see CAND-005

**Owner:** Chief Architect

**Created:** 23 July 2026 · **Revised:** 23 July 2026 (Workspace framing removed; comparative analysis added, per author direction)

**Related Documents:** `Core/Principles.md`, `Core/Manifest.md`, `Meta/Relationship.md`, `Meta/Contract.md`, `Entities/Partner/Partner.md`, `Models/Domain.md`, `Models/Workflow.md`, `Memory/`, `Governance/`, `AI/`

**Process note:** This revision removes all framing of "Workspace" as an existing architectural entity, per author instruction. No document in the repository defines Workspace; it is not referenced below as part of the current model, and no argument here depends on it existing.

**Problem, as reformulated:**

OCOM today does not define an architectural model for how multiple independent organizations interact within one ecosystem. Specifically undefined:

- how independent organizations interact;
- where the architectural boundaries between them lie;
- how relationships between organizations are modeled;
- how the independence of each organization's operational memory is preserved.

**Comparative analysis**

### Option A — Existing primitives

Checked against the four named concepts:

- **Organization** — does not exist as a Meta primitive. No `Meta/Organization.md`, no equivalent, anywhere. `Entities/Partner/Partner.md` is the closest existing concept: *"A Partner is an operational entity representing an external individual, organization, or business that participates in one or more commercial relationships... exists independently of specific agreements, offers, campaigns, or operational systems."* An external organization could be modeled today as a `Partner` Entity — imperfectly (Partner's own definition treats "organization" as one of three possible things a Partner represents, not as its defining characteristic), but without inventing anything new.
- **Relationship** — `Meta/Relationship.md` already defines Identifier, Source Object, Target Object, Relationship Type, with optional Direction, Cardinality, Status, Validity Period, Constraints. Its Relationship Types list is explicitly open: *"Organizations may define Relationship Types including: Ownership, Dependency, Composition, Association, Membership, Responsibility, Assignment, Delegation, Collaboration, Sequence. Additional relationship types may be introduced without affecting the model."* The proposed types (Contractor, Customer, Vendor, Supplier, Affiliate, Parent Company, Subsidiary, Investor, Regulator, Internal Department, etc.) could be added to this existing, already-extensible vocabulary directly — this part of the submission does not appear to need a new Meta Object at all.
- **Contract** — `Meta/Contract.md` already defines governed agreements between Objects specifying interaction conditions. Covers the "Cross-Organization Objects" examples that are agreements (Contract, SLA, Purchase Order) without change.
- **Partner and other related entities** — Partner already covers "external organization in a commercial relationship" at the Entity level, independent of specific agreements or campaigns, which is most of what the submission asks for.

**What Option A does not cover:** operational memory partitioned per organization, never merging across organizations. `Models/Domain.md` partitions responsibility *within* one operational model (e.g., Finance vs. HR); it says nothing about multiple, independent operational models belonging to different organizations. No existing primitive — Relationship, Contract, Partner, or Domain — addresses memory isolation across organizational lines. This is the one part of the problem statement Option A does not answer.

### Option B — New Meta Object `OrganizationRelationship`

*What problem it would solve:* explicit, machine-checkable typing that a given relationship specifically connects two organizations (not any two arbitrary Objects), potentially carrying organization-specific rules — most importantly, a memory-isolation guarantee that generic `Relationship` does not carry.

*Why the existing model might be insufficient:* a generic `Relationship` can express an org-to-org link by convention, but nothing enforces or labels it as such, and nothing in `Relationship` or `Contract` states or enforces that the two sides' operational memories stay separate. `OrganizationRelationship` could carry that guarantee explicitly.

*Complication this option introduces:* `Relationship` requires two Objects as Source and Target. If "Organization" is not itself established as a Meta-level primitive (distinct from, or equivalent to, `Partner`), `OrganizationRelationship` has no well-defined thing to connect on one side. Option B is therefore not just "add one Meta Object" — it first requires deciding whether Organization is a new primitive, an alias for `Partner`, or unnecessary.

*Not treated as pre-decided.* Both options are presented for the Architect to weigh; this record does not recommend one.

**Impact assessment**

| Document | Assessment |
|---|---|
| `Core/Principles.md` | Change required *if* an ADR is approved — a new Principle (12, or the next open number) would be added, regardless of A or B. |
| `Core/Manifest.md` | Change required — Scope does not currently mention multi-organization modeling in either direction (neither claimed nor excluded). |
| `Meta/` | Needs further architectural discussion — contingent entirely on Option A vs. B, and on the Organization-primitive question raised in Option B. |
| `Models/` | Needs further architectural discussion — `Models/Domain.md`'s boundary concept is adjacent but answers a different question (responsibility within one model, not separation across organizations); whether that document should be extended or left alone is not resolved here. |
| `Memory/` | Needs further architectural discussion — no existing document addresses per-organization memory isolation; how to express it, if adopted, is undetermined. |
| `Governance/` | No change required — the ADR Candidate process itself is already handling this correctly; no update needed beyond this record. |
| `AI/` | No change required — no AI/ document currently addresses or conflicts with multi-organization modeling. |

**Next Action:** Blocked. `CAND-005 — Organization vs Domain as the Top-Level Architectural Boundary` must be decided first: it determines whether "Organization" is a new architectural layer, an alias for an existing concept, or unnecessary — which directly determines whether Option A or Option B above is even coherent. Once CAND-005 is decided, this candidate must be revisited to confirm whether it still applies as written or needs rework.

---

## CAND-005 — 🔴 Blocking ADR

**Title:** Organization vs Domain as the Top-Level Architectural Boundary

**Status:** Open

**Blocking:** This candidate blocks `CAND-004`. CAND-004 shall not be decided until CAND-005 is resolved.

**Owner:** Chief Architect

**Created:** 23 July 2026

**Related Documents:** `Meta/Object.md`, `Models/Domain.md`, `Models/Entity.md`, `Core/Principles.md`, `Governance/ADR-Candidates.md#cand-004`

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

**Explicitly not the goal of this candidate:** to pre-select an option. The goal is to record the fork itself, so it can be decided deliberately rather than inherited implicitly by whichever way CAND-004 happens to be written.

**Next Action:** Chief Architect to decide Option A or Option B (or an alternative not listed here). Upon decision, revisit CAND-004 to confirm whether it remains valid as written or requires rework.

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

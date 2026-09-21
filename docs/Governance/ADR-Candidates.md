<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / ADR Candidates

[↑ Up](README.md) · [Next →](Architecture-Health.md)

---
<!-- nav:end -->

# ADR Candidates

**Document ID:** GOV-ADR-CANDIDATES-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 September 2026

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

## CAND-001 — ✅ Decided

**Title:** Content duplication between `AI/Agents/Context.md` and `AI/Context/Overview.md`

**Status:** Decided — `AI/Agents/Context.md` is replaced with an explicit reference to `AI/Context/Overview.md`; the Agents section does not own a description of Context.

**Decision:** **`AI/Context/Overview.md` (`AI-Context-00`) is the single document describing Context within the AI framework. `AI/Agents/Context.md` (`AI-Agents-05`) keeps its path, its Document ID and its position in the Agents reading path, and its body becomes an Informative pointer to `AI/Context/Overview.md` and the four Context documents; it defines nothing and restates nothing. The Agents section does not own a description of Context distinct from the Context section.** Recorded 16 September 2026.

**Owner:** Chief Architect (Decision recorded)

**Created:** 21 July 2026 · **Decided:** 16 September 2026 · **Decided by:** Chief Architect

**Grounding:** `OBS-001`, `AO-035`, `Core/Principles.md` Principle 7, `Core/Terminology.md` (0.2), `Governance/Master-Architecture-Backlog.md` EPIC-C.

### The question

Should `AI/Agents/Context.md` remain a full duplicate of `AI/Context/Overview.md`, be replaced with an explicit reference, or be given distinct Agent-specific content? The candidate recorded on 21 July 2026 that this is a question about section boundaries, whether the Agents section should own a description of Context distinct from the dedicated Context section, and recorded the consequence of each outcome: a duplicate risks silent divergence; a reference changes how a reader navigates the Agents section; distinct content is new normative authoring.

### Rationale

1. `Core/Principles.md` Principle 7, Single Source of Truth: "Each operational concept shall have a single authoritative definition within the model." Two identical bodies under two Document IDs, each with its own Definition and Conformance sections, are two authoritative statements of Context by the specification's own rule.
2. `Core/Terminology.md` 0.2 already names `AI/Context/Overview.md` as the document that defines Context. `AO-035` counts three definitional sentences for Context and notes that the identical pair is already recorded as `OBS-001` and this candidate; it records only the verbatim copy as a duplicate. No chapter of `Specification/` cites `AI/Agents/Context.md` (`Specification/Committee Review Package.md`), and outside the governance registers no document does.
3. Distinct Agent-specific content, the third outcome, would be new normative text describing Context from an Agent's perspective. Under `CAND-007` new text of that kind enters through the pipeline in `Standard Evolution Methodology.md` and, per Rule 2, needs independent Reference Cases; none exists. `CAND-007` Section 3 permits deciding this candidate within its recorded scope, and new authoring is outside it.
4. Keeping the duplicate, the first outcome, preserves the divergence risk the register has carried since 21 July 2026. At commit `d9dc3f7` the two files still differ only in the navigation block and the Document ID field, so replacing the copy now loses no content.
5. The recorded cost of the second outcome, that a reader of the Agents section no longer finds Context there, is removed by keeping the path, the Document ID and the Back and Next chain: the Agents reading path still lands on a Context page, which now sends the reader to the one that governs.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 3 names `CAND-001` among the candidates that may be decided during the Freeze within recorded scope; this Decision selects one of the three outcomes the candidate recorded and no other. It introduces no Meta Object, no Canonical Principle and no Domains subdomain, so Section 4 is not engaged. No requirement is added or removed: the Conformance section of Context remains in `AI/Context/Overview.md` unchanged; what is removed is its second copy.

### What this decision does not do

It does not resolve the other definitional duplicates `AO-035` records, an Overview and a concept file each carrying a Definition heading in every `AI/` section; those are of a different kind and remain open under `AO-035`. It does not change `AI/Context/Overview.md` or any Context document.

**Next Action:** Two-step discipline, as used for `CAND-003`, `CAND-005`, `CAND-006`, `CAND-009`, `CAND-014` and `CAND-015`. Step 1 is done by this record: the Decision is recorded here and `OBS-001` is marked Closed with its Architect Response pointing to this candidate. Step 2, the integration, is performed in the same change under the authorization to execute EPIC-C recorded in `Master-Architecture-Backlog.md`'s execution note of 16 September 2026: `AI/Agents/Context.md` is rewritten as the pointer described above, Status Informative, version 0.2.

**Related Documents:** `OBS-001`, `AO-035`, `AI/Context/Overview.md`, `AI/Agents/Context.md`, `Core/Principles.md`, `Core/Terminology.md`, `Governance/Master-Architecture-Backlog.md` (EPIC-C).

---

## CAND-002 — ✅ Decided

**Title:** Mechanics of set-scoped (profile-based) Conformance

**Status:** Decided — profile mechanics defined as the form of a claimant's declaration, not as a profile this repository publishes (16 September 2026)

**Owner:** Chief Architect (Decision recorded); text integration pending separate authorization

**Created:** 22 July 2026 · **Decided:** 16 September 2026 · **Decided by:** Chief Architect

**Related Documents:** `Language/Conformance.md`, `docs/Specification/08 Conformance.md`

**Discussion:** `Language/Conformance.md` already names "Profile Conformance" as a category, but does not define the mechanics of a profile — how it is declared, bounded, and validated against the Core. The author has explicitly stated this is a separate topic from the Core specification and should not be folded into it; the mechanism itself still needs to be decided.

Consequences by outcome:

- *Define now:* clarifies Conformance fully, but risks coupling the Core specification to a mechanism that may need to change independently.
- *Leave open, reference from the Conformance chapter:* keeps Core minimal, but leaves implementers without profile guidance until resolved.

**Grounding:** `Governance/Concept-Paper-Profile-Conformance.md` (the eight declaration rules, the ten validator assertions, the four options considered, and the boundaries taken deliberately).

**Decision:**

**Profile Conformance is defined by the form of the claim, not by any profile this repository publishes.** OCOM defines no profile, approves none, certifies none, and keeps no list of them. What is defined is what a claimant shall publish before the words Profile Conformance resolve to anything, and the check any third party can run against that publication with nothing but a checkout of this repository and a SHA-256 implementation.

A declaration names a Release and its commit, lists whole canonical source documents each carrying the hash of its bytes at that commit, contains the documents Chapters 4 to 6 compile as a floor, adds nothing, restates nothing, and asserts no exclusions because the complement is computed. A validator answers the three verbs the candidate asks about, offline, from the declaration and a checkout alone.

### The question

`Specification/08 Conformance.md` and `Language/Conformance.md` both publish Profile Conformance as one of three levels while deferring its mechanics. Core Conformance carries four obligations and Extended five. Profile carries none, against `Language/Conformance.md`'s own Design Principles, which require conformance to be objective, measurable and verifiable.

### Rationale

Two constraints decided the shape. First, no statement in this repository carries an identifier, recorded as `AO-062`, so a profile cannot be bounded by citing clauses; the whole document is the finest unit that can be addressed today, and the content hash is what makes a declaration break loudly instead of drifting. Second, Chapter 8's own Non-Conformance clause forbids a conformance claim from an implementation that fails a mandatory requirement, so a profile cannot be a subset of the Core: it is the Core plus a named selection from the documents outside it. Three of the four options considered permitted a claim below that floor or defined nothing at all.

### Scope of this decision, and the Architecture Freeze

Filed under `CAND-007` §3, which permits a Decision on this candidate provided it stays inside the candidate's recorded scope. That scope is three verbs, and the Decision answers declared, bounded and validated without opening a fourth question. Both consequences the candidate records are respected: the Core is not coupled to the mechanism, because the mechanism lives in a Governance-tier Informative document and refers to the Core only by path, commit and hash; and implementers stop being left without guidance, because what a claimant shall publish is stated exactly. The author's recorded position, that profile mechanics are a separate topic and are not to be folded into the Core, is preserved literally: Chapter 8 gains a pointer where it now carries a deferral, and gains no mechanism.

§4 holds item by item. No new Domains subdomain, Entity type, `AI/` subsection, Workflows content, Examples collection or Canonical Principle; no Constitution amendment; no redesign of Object, Memory, Evidence or the derivation direction. The Stop List entry forbidding a new Conformance Profile ahead of this candidate is satisfied rather than waived: this Decision defines zero profiles and authorizes zero profiles, and each concrete profile would need its own Decision. No new Core concept is added: a Profile Declaration is a disclosure a claimant makes about its own scope, not a Meta Object, a Models concept, a term for `Core/Terminology.md` or a publication tier.

### What this decision does not do

It does not make any conformance claim true. A validated declaration is well formed, resolves at a pinned commit and has not drifted; it says nothing about behaviour. Verification remains the other half of `EPIC-E`'s Definition of Done and remains blocked on `AO-062`, which this Decision does not close. Specialization, which Chapter 8 names alongside subset, is left out of this version. Sub-document scoping is gated on a requirement register existing. `AO-032` is adopted only for the resolution of a profile declaration and stays Open. Who may attach the word OCOM to a profile belongs to the stewardship question `CAND-007` holds open, not here.

**Next Action:** Two-step discipline, as used for `CAND-003`, `CAND-006`, `CAND-009` and `CAND-014`. Step 1 is done by this entry. Step 2, each item requiring its own separate authorization: replace the Note on scope in `Specification/08 Conformance.md` with a pointer to the grounding paper; add the same pointer to `Language/Conformance.md`'s Profile Conformance section; correct `Adoption/FAQ.md`, whose answer to "Can I use only part of OCOM?" implies a conformance claim may sit below Chapters 4 to 6, which `R4` and Chapter 8 forbid; publish the declaration field set as a Projection; add the validator to CI beside the existing publication-metadata job; and mark `EPIC-E`'s `CAND-002` half satisfied in `Master-Architecture-Backlog.md`.

**Related Documents:** `Governance/Concept-Paper-Profile-Conformance.md`, `Language/Conformance.md`, `Specification/08 Conformance.md`, `Governance/Publication-Manifest.md`, `Governance/Publication-Model.md`, `Governance/Master-Architecture-Backlog.md` (EPIC-E), `Adoption/FAQ.md`, `AO-014`, `AO-032`, `AO-062`, `AO-065`, `CAND-007`

**Postscript (16 September 2026):** of the Step 2 items above, four are done under the authorization to execute EPIC-F recorded in `Master-Architecture-Backlog.md`: the Note on scope in `Specification/08 Conformance.md` now points to the grounding paper, `Language/Conformance.md`'s Profile Conformance section carries the same pointer, `Adoption/FAQ.md`'s answer no longer implies a claim below Chapters 4 to 6, and `EPIC-E`'s `CAND-002` half is marked satisfied. The declaration field set as a Projection and the validator in CI are tooling, not required for v1.0 per Part 8, and remain open. `AO-065` is Closed by the same EPIC-F change, so the advisory in the paper's Section 3 no longer fires.

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

**Status:** Open; each of the seven questions carries a disposition for v1.0, recorded in the Postscript of 16 September 2026

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

**Postscript (16 September 2026):** the review the Next Action asked for is done, under the authorization to execute EPIC-B recorded in `Master-Architecture-Backlog.md`, and its dependencies are met: `AO-001` was decided on 11 September 2026 (`CAND-015`) and `AO-002` on 16 September 2026 (`CAND-016`). Each question carries one of the two outcomes `Master-Architecture-Backlog.md` Part 8 allows, a decision or an explicit "not required for v1.0". No Core document is changed by this postscript.

1. Inter-organizational relationship types: resolved by existing primitives. `Meta/Relationship.md`'s Relationship Types list is open by its own words, "Additional relationship types may be introduced without affecting the model", and `Meta/Organization.md` defers Organization-specific Relationship Types to the governance process. No constrained enumeration is defined for v1.0.
2. Ownership: resolved by existing primitives for a single owner. `Meta/Ownership.md` names an organizational unit among the parties that may own an Object, so an Organization may be the one responsible owner `Models/Entity.md` requires. More than one owning Organization for one Object is not required for v1.0: it would change the single-owner rule and needs a Reference Case under `CAND-007`.
3. Cross-Organization references: resolved by existing primitives for the mechanism. `Meta/Reference.md` and `Meta/Relationship.md` already give two mechanisms of different weight, and `Meta/Relationship.md`'s Constraints section names organizational restrictions. The omission the question records, that a Reference or Relationship crossing an Organization boundary does not by itself grant access to the target Organization's Memory, is not required for v1.0: stating it is a new rule and needs a Reference Case.
4. Shared objects: not required for v1.0. Whether a Contract between two Organizations has one owner with the others as parties, or a different ownership model, needs a Reference Case; `Meta/Contract.md`'s "two or more Objects" stands as written.
5. Operational Memory per Organization: not required for v1.0. No document in `Memory/` addresses isolation or sharing across Organizations, and defining either needs a Reference Case.
6. Registry and Identity scope: resolved by existing primitives for Identity, not required for v1.0 for Registry. `Meta/Identity.md`'s Identity Scope section lists Organization, Business Domain, Registry, External System and Global Ecosystem as scopes and requires that "Organizations shall define the appropriate scope for each Identity"; Organization as an Identity scope is therefore available today. `Meta/Registry.md` is silent on multi-Organization scope, and a rule for it needs a Reference Case.
7. AI across Organizations: not required for v1.0. `AI/Overview.md` binds an AI Agent to organizational governance and policies; operating across several Organizations at once is new territory and needs a Reference Case.

The candidate stays Open for what still needs a Reference Case, questions 4, 5 and 7 in whole and questions 2, 3 and 6 in part, and is not blocked on anything inside the specification.

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

**Postscript (11 September 2026):** the fourteen Canonical Principles quoted above are the text as adopted on 26 July 2026 and are left unchanged as the record of what this Decision adopted. Principles 9 and 11 were subsequently transcribed in `Core/Constitution.md` per Decisions 4 and 5 of `Constitution-Step0-Summary.md`, the integration `CAND-007` §4 names as permitted, raising the Constitution to 1.0.1 on 11 September 2026. For the current wording of those two principles read `Core/Constitution.md`; for the wording this Decision adopted, read the list above.

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

**Postscript (18 September 2026):** the first of those two is now filed. `AO-071` records that the condition the Release Review attached to it has occurred, the Chief Architect authorized filing under this Section on 18 September 2026, and the question moved to `CAND-017` with `RC-011` as its Reference Case. The authorization covers the filing and no document change. The second candidate, the tamper-evidence guarantee, is untouched by it and stays unfiled.

**Postscript (21 September 2026):** the second is now filed too. `AO-084` records the Reference Case `RC-012`, the Chief Architect authorized filing under this Section on 21 September 2026 on the same terms, and the question moved to `CAND-024`, with the Evidence definition it depends on filed beside it as `CAND-023`. Both were decided as drafted later the same day, with integration authorized alongside; the Memory tier carries the three clauses and the four sections since 21 September 2026.

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

**Decided:** 20 August 2026 · **Decided by:** Chief Architect · **Reference Cases:** `AO-008` (20 August 2026), grounded in `RC-008` and `RC-009`, recorded before this Decision.

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

**Status of Path A at the sixth revision (20 August 2026): not yet completed.** *Postscript (5 September 2026): Path A was completed the same day; `AO-008` records both Reference Cases (`RC-008`, `RC-009`), and the Decision above was taken after it.* Two independent sources of evidence exist, described above; neither has been formally written up as a Reference Case per the template, and no `Architecture-Observations.md` entry exists for this changeset as of this revision. Completing that write-up is out of scope for this edit, which is limited to this entry in `ADR-Candidates.md`. This filing does not treat the existence of the underlying evidence as equivalent to having completed Rules 3–4, and, per the preceding paragraph, does not treat it as already satisfying Rule 2 either — only as the proposed basis for satisfying it once formally written up.

*Superseded (5 September 2026): the Decision was taken on 20 August 2026 after `AO-008` was recorded; see the Decided field above.* **Consequence at the sixth revision: this filing is not yet ready for a Chief Architect Decision.** Completing both Reference Cases and recording them as a single `Architecture-Observations.md` entry is a prerequisite, to be done separately, before this candidate returns for Decision. This now precisely follows the same sequence `CAND-008` itself followed: `AO-005`, grounded in two independent Reference Cases (`RC-006`, `RC-007`), existed before `CAND-008` was filed as a Decision-ready candidate — not an approximation of that precedent, the same shape. Section 8's Decision Text is written for that later point, not for use now.

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

*Postscript (5 September 2026): the Decision recorded in the Status and Decided fields above supersedes this template, which is retained for the record.* **Not usable until Section 6's Path A is complete.** No alternative path exists; this text has an empty, mandatory `Reference Cases` field for exactly that reason, and must not be signed with that field unfilled.

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

**Next Action:** None. Path A is complete (`AO-008`, grounded in `RC-008` and `RC-009`) and the Decision was taken on 20 August 2026; the Backlog carries the execution note (`Master-Architecture-Backlog.md`, EPIC-F execution note of 20 August 2026). *Original text of this field, superseded:* Complete Section 6's Path A — author both Reference Cases per `Standard Evolution Methodology.md`'s template, tagged `repository-scope`, and record them together as one `Architecture-Observations.md` entry. This is a separate step, outside this revision's scope (limited to this entry in `ADR-Candidates.md`). Once complete, the Chief Architect reviews this Candidate together with that entry and records a Layer 1 Decision using Section 8's text. Independently of that Decision, the Layer 2 defect list in Section 7 must be closed, and a separate Layer 3 confirmation obtained, before any part of the underlying changeset is committed.

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

## CAND-013 — ✅ Decided

**Title:** Recognize "Consumer Tool" as a new publication category and authorize native Shape Check at /shape-check

**Status:** Decided — Promote (21 August 2026)

**Owner:** Chief Architect

**Created:** 21 August 2026 · **Decided:** 21 August 2026

**Decision summary:** `CAND-013` is Promoted. `Publication-Model.md` gains a fifth category, **Consumer Tool**. **Shape Check is authorized as its one instance**, published at route `/shape-check`. Every non-assertion and the Decision Boundary below remain binding, unchanged from the reviewed draft. The terminology-drift risk named in the Governance implication remains an explicitly **named residual risk**, not a blocking condition — it is watched, not solved by any new mechanism. This Decision authorizes no other Consumer Tool, no other interactive page, no `/tools/` directory, no arbitrary JavaScript as a class, and no other top-level interactive route — each would need its own separate decision.

**Why this may NOT simply extend an existing authorization (stated honestly, not assumed away):** Unlike `CAND-010`/`CAND-011` (individual Adoption files) and `CAND-012` (a second instance of the already-existing Projection tier), Shape Check does not fit any of `Publication-Model.md`'s four existing tiers. It has no canonical source document at all — ruling out Canonical Source, Compiled Publication, and Projection (Projection always renders one canonical document 1:1; Shape Check's `CONCEPTS` list and matching logic are hand-maintained code, not a rendering of any `docs/` file). It also arguably exceeds Convenience Representation, which `Publication-Model.md` defines as informative/illustrative and static — Shape Check is interactive. This is a genuinely new category question, not an instance of one already answered.

**`CAND-007` §6 test, applied honestly, not assumed:**

- (a) *Does it fit an existing Epic?* `EPIC-F`'s literal scope (re-pointing Adoption, closing four named debt items) does not mention tools. `CAND-010`/`011`/`012`'s "kind of work" reasoning (small-scope, non-normative content added to the ocom.uno surface) arguably extends, but Shape Check is categorically different — a tool, not documentation. This filing does not assume (a) is satisfied.
- (b) *Product-shaped or contract-shaped?* Checked directly against both principles' primary text (`Architecture-Principles.md`, not just their titles), across two rounds of independent adversarial review. **Principle 1 — PASS:** no Specification requirement is added and no product is privileged in Specification text; the principle's own forbidden pattern (a Spec requirement justified only by "product X needs it") is not present, since nothing about the Specification changes. **Principle 5 — PASS, by analogy:** Shape Check isn't Reader-shaped in the sense the principle addresses (it implements nothing normative), but its three named drift mechanisms were checked regardless — documentation gravity and governance capture are structurally low risk given the tool's narrow, disclosed, read-only scope; terminology drift is real and is carried forward as a **named residual risk**, not an unresolved compliance question, in this filing's own Governance implication below.

(a) remains a genuine judgment call — whether `CAND-010`/`011`/`012`'s "kind of work" reasoning extends from documents to a tool is for the Chief Architect to decide, not something either review resolved by assumption. (b) has now been checked and passed on both principles. This is filed as an ordinary CAND entry that still asks the Chief Architect to make the (a) call, rather than one that pre-selects every answer.

**Related Documents:** `CAND-007` (§6 test, Architecture Principles 1 and 5), `CAND-010`, `CAND-011`, `CAND-012`, `Publication-Model.md` (four existing tiers), the existing Claude-artifact Shape Check (`https://claude.ai/code/artifact/b331b03b-1f22-4796-a907-8df6f66bd126`).

**Decision:**

1. `Publication-Model.md` gains a fifth category, **Consumer Tool** — outside the canonical-source chain (no `source_file`/`source_url`/`history_url`, because none exists), non-normative, not derived from compiling any specific document. A Consumer Tool may reference vocabulary terms and must state which vocabulary version it checks against, displayed to the user on the page itself.
2. Authorize exactly one instance: Shape Check, published at `/shape-check`, using the already-reviewed matching algorithm (unchanged from the Claude-artifact version), tied explicitly to Core Vocabulary v0.1 (`Meta/Object.md`'s seven Core Characteristics).
3. `/shape-check` intentionally sits outside `/adoption/` because Shape Check is a consumer tool, not an Adoption document or Adoption Projection. This is a statement about this one artifact's placement, not a new taxonomy rule for where future tools must live.

This decision does not authorize, and does not create a precedent for:

- any other Consumer Tool;
- any other interactive page;
- creation or authorization of a `/tools/` directory of any kind;
- arbitrary JavaScript as a class of permitted content;
- other consumer applications;
- other top-level interactive routes;
- automatic publication of any future interactive artifact — each needs its own separate decision, individually, the same way this one does;
- any loosening of `CAND-012`'s own blanket-authorization prohibition on `docs/Adoption/` — that prohibition is unrelated to and unaffected by this filing.

This decision also does not:

- change Core/Meta/Models/Specification/Governance;
- change First Pilot's or Worked Example's canonical Markdown source;
- remove the existing Claude-artifact Shape Check (retained as historical/prototype reference, linked from the native page's own footer);
- make Claude, or any external AI service, a production dependency of ocom.uno — the native page is fully self-contained static HTML/CSS/JS with no runtime calls to Claude or any backend;
- resolve the Architecture Principle 1/5 tension above by assumption.

**Decision Boundary:** This Decision authorizes publication architecture and category definition only. It does not certify the tool's algorithm as normatively correct or complete — Shape Check already, independently, discloses that it checks names only, with no fuzzy matching, and deliberately excludes Governance and Evidence from its current concept list. The page itself states, in plain unhedged terms: not part of the Specification; creates no normative requirements; not a source of truth (`Meta/Object.md` is); makes no conformance or validation claim.

**Governance implication:** Any future Consumer Tool needs its own individual decision, per the same no-blanket-authorization discipline `CAND-012` already established for Adoption Projections. **Residual risk, named and not solved by any new mechanism:** Shape Check's own terminology (`Shape Check`, `coverage`, `Required`, `Optional`, and similar UI labels) does not become part of OCOM Specification terminology automatically, and must not be carried into normative text without its own separate governance review — the same terminology-drift risk `Architecture-Principles.md` Principle 5 names for Reader, applied here by analogy, watched rather than assumed away.

**Next Action:** None: decided on 21 August 2026 and executed. `/shape-check` is published; `Publication-Model.md` records the Consumer Tool tier (revision of 4 September 2026); Worked Example's CTAs and the discovery pointers were switched to `/shape-check`. *Postscript (5 September 2026): the link to the historical prototype was removed from the published page on 4 September 2026 by owner decision; the prototype is no longer referenced from the site.* *Original text of this field, superseded:* Awaiting Chief Architect Decision. On Decision, the already-prepared `/shape-check` page (algorithm unchanged; version banner and First Pilot forward link added) is published, Worked Example's CTAs and the homepage/discovery pointers are switched to `/shape-check`, and the existing Claude artifact is kept live as a labeled historical/prototype reference, not removed.

## CAND-014 — ✅ Decided (Layer 1)

**Title:** Knowledge, World Model, and the Location of Current State (three-layer split by time horizon)

**Status:** Decided — Option 4, Layer 1 (derivation semantics). Layer 2 (Core authoring) explicitly not decided, gated; see Scope below.

**Decision:** **Option 4 — the three responsibilities are split by the horizon of the question each answers. Memory records what happened; Knowledge holds why it matters (stable rules and meaning, changed only through a rule-change process that is itself logged in Memory, never edited directly); World Model holds what is true right now for a given subject (current state, the version currently in force, point-in-time indicators), computed only from Memory and Knowledge, with no independent authorship or approval workflow of its own.** Recorded 10 September 2026.

**Owner:** Chief Architect (Decision recorded)

**Created:** 10 September 2026 · **Decided:** 10 September 2026 · **Decided by:** Chief Architect

**Grounding:** `Governance/Concept-Paper-Knowledge-vs-World-Model.md` (Option 4), `Governance/Architecture-Discussion-Knowledge-vs-World-Model.md` (Decision Readiness: Yes), `AO-003` (Mutable Status in an Immutable Memory Model), `Core/Constitution.md` §4 (Immutable Memory), §5 (Memory Precedes Knowledge), §6 (Reconstructability). Resolution vehicle for `Master-Architecture-Backlog.md` EPIC-A and the Architect Response to `AO-003`.

### The question

Constitution §5 states one chain: Memory produces Knowledge, Knowledge produces World Model. Three things in the current text contradict that chain, and `AO-003` is the narrowest of them:

1. `AI/Knowledge/Knowledge.md` defines Knowledge as "independent of ... Memory Records", the literal opposite of §5.
2. A single layer (Knowledge) is asked to hold both stable reusable understanding (what "Gold Tier" means, changes only when the rule changes) and instance current state (the tier of Customer #123, changes on every new Memory), which have different update cadences and scopes.
3. `AO-003`: the `Status` of a Memory Record has undefined semantics against the append-only model, readable either as a stored field (conflicts with §4) or as a derived projection.

World Model, the third named stage of the chain, is defined by no document.

### Rationale

Option 4 resolves all three contradictions with one structure. §5 holds because every change to Knowledge is preceded by a Memory entry, so Knowledge is derived from Memory in the strict sense. Contradiction 2 is removed because instance current-state leaves Knowledge for World Model. `AO-003` is answered with its own Option B: Status is a derived projection, computed in World Model, so no Memory Record is ever mutated and §4 is untouched. §6 holds because World Model is computed only, reconstructable from Memory without the original systems.

The line in `Knowledge.md` that reads "independent of ... Memory Records" is recorded as an inaccuracy to be corrected on integration: what was meant is independence from any single record or execution instance, not independence from Memory as the append-only log.

Options 1 to 3 were considered and not adopted: Option 1 is Option 4 without the explicit rule that Knowledge is never edited directly; Option 2 keeps two meanings of the word Knowledge and sits worst against `CAND-007`; Option 3 is a mechanism choice that Option 4 already subsumes (the rule-change process is Memory-logged).

### Scope of this decision, and the Architecture Freeze

Filed under `CAND-007`. This decision is deliberately split into two layers, following the precedent `CAND-009` set:

- **Layer 1, decided by this candidate.** The derivation semantics above: current state and Status are derived (World Model), not stored; Knowledge is Memory-logged and never edited directly; the derivation direction Memory to Knowledge to World Model is affirmed as §5 already states it. Layer 1 stays within `AO-003`'s recorded scope (the Status question) and within the completeness of a term the adopted Constitution already names (World Model, §5/§6). It introduces no new Canonical Principle and, at this layer, no new Meta Object; `CAND-007` §4 is not engaged, and `CAND-007` §3 permits a decision on `AO-003` within its recorded scope.
- **Layer 2, explicitly not decided here, gated.** Authoring the normative `Meta/World-Model.md` with its own Core Characteristics, and rewriting the `AI/Knowledge/*` governance, lifecycle and quality model to match Layer 1, are Core-shaping and are left open. Where Layer 2 adds genuinely new structure beyond completing §5/§6, it routes through the freeze-exception pipeline (`Standard Evolution Methodology.md`: Reference Case, Repeated Pattern, ADR Candidate, Decision), and per Rule 2 that pipeline needs independent Reference Cases, which do not yet exist. Layer 2 is therefore named, not scheduled.

### What this decision does not do

It changes no document outside this register and `Architecture-Observations.md`. `Core/`, `Meta/`, `Models/`, `AI/` and `Memory/` are untouched. It does not author `Meta/World-Model.md`. It does not rewrite the Knowledge governance model. It does not certify the current `AI/Knowledge/*` text correct; it records the direction its eventual rewrite must follow.

**Next Action:** Two-step discipline, as used for `CAND-003`, `CAND-005`, `CAND-006`, `CAND-009`. Step 1 is done by this record: the Decision is recorded here and `AO-003` is marked Closed with its Architect Response pointing to this candidate; nothing in Core is edited by that step. Step 2, Core integration of Layer 1 (the correction to `Knowledge.md`'s "independent of Memory Records" line, and a short statement of the three-layer derivation in the appropriate Core or Meta location, plus the corresponding note in `Memory/Memory Record.md` that Status is derived), is a separate, separately-authorized task, not performed by this candidate. Step 3, Layer 2 (authoring `Meta/World-Model.md`, rewriting `AI/Knowledge/*`), remains open, gated as above.

**Related Documents:** `AO-003`, `Core/Constitution.md` (§4, §5, §6), `AI/Knowledge/Knowledge.md`, `AI/Knowledge/Knowledge Lifecycle.md`, `AI/Knowledge/Knowledge Governance.md`, `AI/Knowledge/Knowledge Quality.md`, `Memory/Memory Record.md`, `Governance/Concept-Paper-Knowledge-vs-World-Model.md`, `Governance/Architecture-Discussion-Knowledge-vs-World-Model.md`, `Governance/Master-Architecture-Backlog.md` (EPIC-A), `Governance/ADR-Candidates.md#cand-009` (two-layer precedent).

**Postscript (11 September 2026):** Step 2 of the Next Action above is done. The Layer 1 Core integration was performed under separate authorization from the Chief Architect: `AI/Knowledge/Knowledge.md`'s Definition now states that Knowledge is independent of any individual Agent, Context or Memory Record but not of Memory, and `Memory/Memory Record.md` moves Status out of Mandatory Attributes and restates it as a derived projection. `AO-042` is resolved in part by the same integration. Step 3, Layer 2, remains open and gated.

**Postscript (16 September 2026):** Disposition for v1.0, Chief Architect decision recorded under `Master-Architecture-Backlog.md` Part 8: Layer 1, decided by this candidate and integrated on 11 September 2026, closes EPIC-A for the v1.0 claim. Layer 2, the `Meta/World-Model.md` document and the rewrite of `AI/Knowledge/*`, stays open and gated behind the `CAND-007` pipeline as Step 3 above states, and is not required for v1.0; `FW-001`'s reserved sections carry the same disposition. Nothing in this postscript changes the Decision.

**Postscript (18 September 2026):** the v1.0 disposition above is extended. `AO-069` records that `Architecture-Release-Review-v1.0.md` Part 2 routed `Memory/Layered Memory.md` and `Memory/Retention.md` into EPIC-A on 27 July 2026, that `CAND-007` Section 3 binds that correction to the Epic, and that neither document was addressed before the Epic was closed for the v1.0 claim. The Chief Architect's extension, 18 September 2026: both documents are covered by the disposition and do not block v1.0; the contradiction between `Memory/Retention.md`'s controlled-deletion Conformance clause and Constitution §4 and §6 stays open under `AO-069`, awaiting a Reference Case of the kind this candidate had for Status. Option 4's Layer 1 answered the Status manifestation only; the Layer and Retention manifestations the review named are not answered by it.

## CAND-015 — ✅ Decided

**Title:** Domain Definition Divergence: which of the two Domain documents is canonical

**Status:** Decided — `Models/Domain.md` is canonical; `Domains/Common/Domain.md` is informative and restates rather than extends.

**Decision:** **`Models/Domain.md` (`Model-02`) is the canonical normative definition of Domain. `Domains/Common/Domain.md` (`DOM-DOMAIN-01`) is not a second normative model and is not a specialization of the first. It is an informative description of how the Domain concept is applied within the `Domains/` tier: it restates the canonical definition, it does not extend it, it shall cross-reference `Model-02` as the definition, and the four characteristics it carries beyond `Model-02` (Capabilities, Policies, Constraints, Integration Points) carry no normative force unless and until they pass through the change process.** Recorded 11 September 2026.

**Owner:** Chief Architect (Decision recorded)

**Created:** 11 September 2026 · **Decided:** 11 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-001` (Domain Definition Divergence, logged 25 July 2026, the oldest unresolved observation in the register), `Models/Domain.md`, `Domains/Common/Domain.md`, `CAND-005`, `Governance/Knowledge-Map.md`, `Master-Architecture-Backlog.md` EPIC-B.

### The question

`AO-001` asked the Chief Architect to determine which of two independently written normative models of Domain is canonical, whether one is a specialization of the other, or whether consolidation is required. `Models/Domain.md` was written 20 July 2026 and defines a Domain as an operational boundary governing one or more Entities, with seven characteristics. `Domains/Common/Domain.md` was written 21 July 2026 and defines a Domain as a logical business boundary managing a coherent set of Objects, capabilities, policies, processes and operational outcomes, with ten characteristics. Neither cross-references the other as authoritative.

### Rationale

Six independent pieces of evidence point the same way, and none points the other way.

1. `Governance/Knowledge-Map.md` already names the source when it states the Domain rule: "**Domain** (`Models/Domain.md`) governs one or more Entities; every Entity belongs to exactly one primary Domain."
2. The compiled reading path cites `Models/Domain.md` in `Specification/03 Core Concepts.md` and `Specification/05 Object Model.md`.
3. The Adoption layer cites `Models/Domain.md` in `Getting Started.md`, `First Pilot.md` and `Common Mistakes.md`.
4. `CAND-005`, already decided, restates Domain in `Models/Domain.md`'s own terms: "Domain keeps its existing, unchanged semantics, an operational boundary describing an area of responsibility."
5. `Domains/Common/Domain.md` places itself downstream in its own Relationship to Other Specifications section, which lists Models among the specifications it builds upon.
6. No normative document and none of the thirteen domain profiles cites `Domains/Common/Domain.md`. Its only citations in the repository are the governance records that log it as a problem.

### Why consolidation was not chosen

Folding `DOM-DOMAIN-01`'s four additional characteristics into `Model-02` would add requirements to Domain, which is a change to the model rather than a resolution of an ambiguity. Under `CAND-007` that is a Freeze exception requiring the pipeline in `Standard Evolution Methodology.md`, and per Rule 2 that pipeline needs independent Reference Cases, of which none exist today. Consolidation therefore remains available as a future path and is not taken here. This Decision removes the divergence without changing what Domain requires.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. `CAND-007` §3 names `AO-001` among the observations on which a decision may be taken during the Freeze, provided the decision stays within the observation's recorded scope. This Decision answers exactly the three questions `AO-001` records and no others. It introduces no new Meta Object, no new Canonical Principle and no new Domains subdomain, so `CAND-007` §4 is not engaged. No requirement anywhere is added, removed or reworded by this Decision.

### What this decision does not do

It changes no document. `Models/Domain.md` and `Domains/Common/Domain.md` are both untouched by this record. It does not resolve `AO-002`. It does not unblock `CAND-004` by itself: `CAND-004` depends on `AO-001` and `AO-002` together, and `AO-002` remains open.

**Next Action:** Two-step discipline, as used for `CAND-003`, `CAND-005`, `CAND-006`, `CAND-009` and `CAND-014`. Step 1 is done by this record: the Decision is recorded here and `AO-001` is marked Closed with its Architect Response pointing to this candidate. Step 2, the integration, is a separate and separately authorized task: `Domains/Common/Domain.md`'s Status becomes Informative, its Definition section gains a cross-reference naming `Models/Domain.md` as the canonical definition, and its Core Characteristics section states that the four characteristics beyond `Model-02` are descriptive of the `Domains/` tier and carry no normative force. `Models/Domain.md` is not edited by that step.

**Related Documents:** `AO-001`, `AO-002`, `Models/Domain.md`, `Domains/Common/Domain.md`, `Governance/Knowledge-Map.md`, `Governance/ADR-Candidates.md#cand-004`, `Governance/ADR-Candidates.md#cand-005`, `Governance/Master-Architecture-Backlog.md` (EPIC-B).

**Postscript (16 September 2026):** Step 2 of the Next Action above is done, under the authorization to execute EPIC-B recorded in `Master-Architecture-Backlog.md`: `Domains/Common/Domain.md`'s Status is Informative, its Definition names `Models/Domain.md` as the canonical definition, and its Core Characteristics section states that the four characteristics beyond `Model-02` describe the `Domains/` tier and carry no normative force. `Models/Domain.md` is not edited.

**Postscript (16 September 2026, later the same day):** the dogfooding audit of Release v1.2.0 compared the ten shall-sentences of `Domains/Common/Domain.md` with `Models/Domain.md`: four restate it (responsibilities, ownership, boundaries, no assumed ownership of others' Objects) and six have no counterpart there (the Design Principles list, explicit Object ownership, independence from other Domains' implementation, evolution compatibility, the governance list, the Conformance list). The Decision's phrase "restates rather than extends" holds for the definition and the four characteristics it named and not for those six sentences; as the document is Informative they impose no requirement, and `Domains/Common/Domain.md` now says so. Recorded under `AO-025` as a further instance of that pattern. Nothing in this postscript changes the Decision.

---

## CAND-016 — ✅ Decided

**Title:** Relationship Participants: Object at the Meta level, Entity in the Object Model

**Status:** Decided — `Meta/Relationship.md` is the canonical definition of Relationship, with Objects as participants; `Models/Relationship.md` is its specialization for Relationships between Entities and restricts nothing else.

**Decision:** **`Meta/Relationship.md` defines Relationship: a governed semantic association between Objects, with a Source Object and a Target Object. `Models/Relationship.md` (`Model-03`) is a specialization of that definition for the case in which every participant is an Entity, as its own Purpose states, "the normative model of Relationships between Entities"; its Source Entity and Target Entity requirement binds Relationships within that case and does not restrict which Objects may participate in a Relationship. An Organization, or any other Object that is not an Entity, participates in Relationships under `Meta/Relationship.md`, as `Meta/Organization.md` already states. No requirement in either document changes.** Recorded 16 September 2026.

**Owner:** Chief Architect (Decision recorded)

**Created:** 16 September 2026 · **Decided:** 16 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-002` (Relationship Participant Inconsistency, logged 25 July 2026), `Meta/Relationship.md`, `Models/Relationship.md`, `Meta/Organization.md`, `CAND-005`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, `Governance/Master-Architecture-Backlog.md` EPIC-B.

### The question

`AO-002` records that `Meta/Relationship.md` defines Relationship participants as Objects while `Models/Relationship.md` requires a Source Entity and a Target Entity, so that Organization, a first-class Object per `CAND-005` that `Meta/Organization.md` says connects to other Objects exclusively through Relationships, cannot satisfy `Models/Relationship.md` as written. `AO-002` recorded two routes: broaden the participants of `Models/Relationship.md` to Object, or define an explicit specialization relationship between the Meta and Model layers.

### Rationale

1. The Meta-to-Model relation is already specialization. `Specification/05 Object Model.md` states that the Meta Model defines the abstract vocabulary and the Object Model defines the structure that vocabulary takes when used to build an operational model, and `Models/Entity.md` states that an Entity is a specialization of Object. Reading `Models/Relationship.md` as the specialization of `Meta/Relationship.md` for Entity participants applies the pattern the two tiers already use; it introduces none.
2. `Models/Relationship.md` limits its own scope in its Purpose: it "defines the normative model of Relationships between Entities". Its Entity-only participants describe that scope. Nothing in the document states that Relationships between other Objects are prohibited.
3. The Meta level already carries Organization participation. `Meta/Organization.md` states that an Organization participates "through the same governed Relationships available to any Object", and `Meta/Relationship.md`'s Relationship to Other Specifications section lists Organization and states that Organization connects to other Objects exclusively through Relationship. Nothing at the Meta level needs to change.
4. Broadening `Models/Relationship.md` to Object would make every requirement of that document, cardinality, direction and the Entity-level constraints, bind Relationships among Organizations, Policies, Contracts and every other Object. That is a change to what the Object Model requires, which under `CAND-007` enters through the pipeline in `Standard Evolution Methodology.md` and, per Rule 2, needs independent Reference Cases; none exists. The specialization route removes the contradiction `AO-002` records without adding or removing a requirement.
5. `Core/Terminology.md` 0.2 recorded the divergence in its Relationship entry and named `AO-002` as its tracker. Under this Decision the entry names `Meta/Relationship.md` as the document that defines the term and `Models/Relationship.md` as its specialization.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 3 names `AO-002` among the observations on which a decision may be taken during the Freeze within recorded scope; this Decision takes the second of the two routes `AO-002` recorded and no other. It introduces no Meta Object, no Canonical Principle and no Domains subdomain, so Section 4 is not engaged. No requirement anywhere is added, removed or reworded.

### What this decision does not do

It does not decide any of `CAND-004`'s seven questions, which carry their own dispositions. It does not define Organization-specific Relationship Types; `Meta/Organization.md` defers those to the governance process. It does not change the editorial note in `Specification/05 Object Model.md`, which belongs to the compiled tier and to EPIC-F. It does not touch the statement in `Models/Entity.md` and `Entities/Overview.md` that Entities may establish relationships with other Entities, which is an Entity-level statement consistent with the specialization.

**Next Action:** Two-step discipline, as used for `CAND-003`, `CAND-005`, `CAND-006`, `CAND-009`, `CAND-014`, `CAND-015` and `CAND-001`. Step 1 is done by this record: the Decision is recorded here and `AO-002` is marked Closed with its Architect Response pointing to this candidate. Step 2, the integration, is performed in the same change under the authorization to execute EPIC-B recorded in `Master-Architecture-Backlog.md`'s execution note of 16 September 2026: one sentence in the Purpose of `Models/Relationship.md` names the specialization, and the Relationship entry of `Core/Terminology.md` names `Meta/Relationship.md` as the defining document. `Meta/Relationship.md` is not edited.

**Related Documents:** `AO-002`, `CAND-004`, `CAND-005`, `Meta/Relationship.md`, `Models/Relationship.md`, `Meta/Organization.md`, `Core/Terminology.md`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, `Governance/Master-Architecture-Backlog.md` (EPIC-B).

---

## CAND-017 · ✅ Decided in part

**Title:** Stewardship of the Name OCOM and the Phrase OCOM-compatible

**Status:** Decided in part, 19 September 2026, on the form `CAND-014` set for a candidate decided in one layer with the rest gated. The half about a condition on a public conformance claim is answered in principle and its text is deferred for want of a second Reference Case. The half about a right in the name is answered by placing it outside the Specification. Filed 18 September 2026 as a `CAND-007` Section 5 Freeze exception, on the Chief Architect's authorization recorded in `AO-071`.

**Decision:** **The question splits at the line between a condition on a claim and a right in a name.**

**First, the condition.** What a public claim of conformance shall be accompanied by is a condition on the claim, and the specification already states conditions of that kind: `Language/Conformance.md` tells an implementation that fails a mandatory requirement that it shall not claim conformance, and requires a claim to identify the version it is made against. A rule about what a claim carries therefore belongs inside the Specification, at the Language tier, beside those clauses. The text of that rule is not written by this Decision. It is gated on the second, independent Reference Case that `RC-011` itself names as missing, under the standard `Standard Evolution Methodology.md` states as Repeatability Before Standardization and that `CAND-009` applied to itself as a non-Core Freeze exception. The natural second case is the first conformance declaration published from outside this repository.

**Second, the right.** Who owns the words OCOM and OCOM-compatible, and what follows when a claim is false, is a right in a name. This specification holds no such right and neither license it publishes under grants one: `LICENSE` is Apache-2.0, whose Section 6 withholds permission to use the Licensor's marks, and the specification text under `docs/` is CC BY 4.0, whose Section 2(b)(2) states that trademark rights are not licensed. Whether any instrument outside this repository could create such a right is a legal judgment that `Core/Manifest.md`'s Scope excludes from this specification, and this Decision does not make it. That half is outside the Specification and outside what an architecture decision can decide: it is work for counsel and for the publication, and a mark, if one is ever obtained, is held outside the specification.

**Third, the register of declarations is declined.** `Language/Conformance.md`'s Independence clause and the same exclusion compiled into `Specification/08 Conformance.md` both rule out compliance programs and certification schemes, and `CAND-002` decided on 16 September 2026 that OCOM "defines no profile, approves none, certifies none, and keeps no list of them". Nothing recorded since reopens either, so a list of declarations published by OCOM would contradict two standing decisions rather than extend them.

**Owner:** Chief Architect (Decision recorded); integration into any document awaits separate authorization.

**Created:** 18 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-071` and its Reference Case `RC-011`; `Architecture-Release-Review-v1.0.md` Part 2, finding 2 (27 July 2026); `CAND-007` Section 5; `CAND-002`; `Governance/Conformance-Test-Suite.md`; `Governance/Requirement-Register.md`; `Language/Conformance.md`; `Governance/Concept-Paper-Profile-Conformance.md`; `LICENSE`.

### The question

Who may state publicly that an implementation is OCOM-compatible, or conforms to the OCOM Specification, and what follows when the statement is false?

The specification answers everything around that question and not the question itself. `Language/Conformance.md` defines what conformance is and states that an implementation failing a mandatory requirement shall not claim it. `CAND-002` fixes the form a claimant's declaration takes. `Conformance-Test-Suite.md` says how requirements are enumerated and what a Test Report carries, and `Requirement-Register.md` enumerates the 335 Statements a claim is measured against. So a claim is now checkable by any reader. What no document records is who is entitled to make it, what the words OCOM and OCOM-compatible may be attached to, and what recourse exists when a claim is made without the evidence. `LICENSE` is Apache-2.0, whose Section 6 grants no trademark rights and says nothing about compatibility claims either way.

### Why this is a Freeze exception, and what that means here

Section 5 permits escalation when a question fits inside no existing Epic, ADR Candidate or Observation and is not a bounded scope correction to one. `Architecture-Release-Review-v1.0.md` Part 2 states in its own words that this one "sits outside all six Epics", and `CAND-007` Section 1 carries it forward as one of two named, not-yet-filed exception candidates. Section 6's second check also passes: the question is contract shaped rather than product shaped, because it governs what a third party may assert about the specification, not what any implementation does.

Meeting the bar authorizes escalation, not a change. This filing therefore changes no document. It carries one Reference Case, `RC-011`, whose External Assurance is recorded as weak: it is drawn from the publication's own artifacts by their author, and no independent implementation has yet made or been refused a claim. Repeatability Before Standardization asks for a second, independent case, and the natural one is the first real conformance declaration from outside this repository.

### The options, as they stand today

1. **Out of scope.** Stewardship of the name belongs to the publication and its licensing, not to the specification, because `Core/Manifest.md` excludes business strategy from scope. The specification would record that boundary explicitly, so the gap is named rather than silent, and the question moves to ocom.uno and the license.
2. **A claim rule at the Language tier.** `Language/Conformance.md` gains the conditions a public claim shall satisfy: a published declaration in the `CAND-002` form, naming the Release Identifier and Commit tested against, with the Test Report reachable. The rule stays technical and testable, and it binds the claim rather than the name.
3. **A register of declarations.** The publication lists declarations it can resolve, marks each as resolving or not resolving at a pinned commit, and endorses none. This makes a false claim visible without asserting authority over the words themselves.
4. **A mark.** A trademark or certification mark over OCOM and OCOM-compatible, with a policy stating who may use them. This is the only option that creates recourse, and the only one that is legal rather than architectural work, with cost and jurisdiction attached.

The options are not exclusive: 2 and 3 compose, and 1 can be recorded alongside 4 if the mark is held outside the specification.

### What this candidate does not do

It proposes no Core change and asserts no Core Impact: `RC-011` records Core Impact None. It does not decide whether OCOM is a trademark, and it does not authorize any document edit. It does not touch `CAND-002`, whose declaration form it relies on, and it does not reopen `Language/Conformance.md`'s definition of conformance. It says nothing about the second Section 5 candidate, the tamper-evidence guarantee for Memory and Evidence, which stays unfiled.

**Next Action:** Two-step discipline. Step 1 is done by the Decision above. Step 2, first item done 19 September 2026: `Governance/Publication-Model.md`'s Known Gaps records that stewardship of the name is outside this specification, so a reader meets the boundary where the question arises. The rest stands: `Language/Conformance.md` stays untouched until the second Reference Case exists, and when it does the claim rule is drafted as a Statement the Requirement Register can enumerate and the Test Suite can decide with a Declaration Test. Nothing about a mark is repository work.

**Related Documents:** `AO-071`, `RC-011`, `CAND-002`, `CAND-007`, `Governance/Architecture-Release-Review-v1.0.md`, `Governance/Conformance-Test-Suite.md`, `Governance/Requirement-Register.md`, `Governance/Concept-Paper-Profile-Conformance.md`, `Language/Conformance.md`, `Core/Manifest.md`, `LICENSE`

---

## CAND-018 · ✅ Decided

**Title:** What a Compiled Chapter Carries From Its Sources, and Where the Obligation Sits

**Status:** ✅ Decided, 19 September 2026. Filed the same day on the record of `AO-077`.

**Owner:** Chief Architect

**Created:** 19 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-077` (18 September 2026); `Governance/Publication-Model.md` (Publication Layers, tiers 1 and 2); `Specification/01 Introduction.md`; the Source lines of the nine chapters; `AO-051`; `AO-032`; `CAND-002`.

### The question

May a compiled chapter of `docs/Specification` abridge the documents its Source line names, or must it carry every mandatory Statement of them, and where does the obligation sit when a chapter omits one?

The corpus answers three different ways today. Two chapters, 00 and 03, declare "synthesized from" and state that they add no claims. Seven declare "compiled from", and one of those, Chapter 02, adds "verbatim". Nothing says what any of the three forms obliges. `AO-077` found three obligations missing from Chapter 5, which are now compiled; the survey behind this candidate found a fourth, in Chapter 02, whose Source line declares verbatim compilation while the chapter dropped `Core/Principles.md`'s subordination sentence. That one is corrected as editorial work by the change that files this candidate, because a chapter that declares verbatim compilation and abridges is a defect under every option below.

**Decision:** **A compiled chapter may abridge the documents its Source line names, and states no obligation of its own. The obligation lives in the canonical document, which `Publication-Model.md` calls the normative text and which Chapter 1 already calls the normative source of truth, so an omission from a chapter is a defect of the reading path and never a discharge of the requirement. A chapter's Source line shall say which of the three forms already in use it takes: `synthesized from`, the chapter carries none of its sources' Statements as obligations; `compiled from`, the chapter carries them in summary and may abridge; `compiled from ... verbatim`, the chapter carries every mandatory Statement of the sections it names. No Statement's binding force changes, none is added and none is removed.**

### Rationale

1. The tiering already says it. `Publication-Model.md` records the Compiled Publication as derived from the Canonical Source, and Chapter 1 tells a reader that the granular documents are the normative source of truth. A chapter that could discharge an obligation by omitting it would make the derived tier authoritative over its own source.
2. The requirement set is already computed from documents, not from chapters. `Governance/Requirement-Register.md` enumerates the Statements of the 22 canonical documents that Chapters 4 to 6 compile, and `tools/conformance/requirement_register.py` reads those chapters only for their Source lines. Under this Decision that stays true and becomes stated rather than implied.
3. Full fidelity costs more than it buys. Chapters 04 and 06 declare in their own text that they summarize and that domain patterns live elsewhere; requiring every mandatory Statement would make the reading path a second copy of the corpus, which is the drift `AO-051` records, and a backward check at Statement granularity would still have caught only one of the three omissions `AO-077` found, because two were items inside a Statement's list.
4. Declaring the form is the part that changes anything. Today a reader cannot tell an abridgement from a defect. After this Decision, a chapter that declares verbatim and abridges is a defect anyone can find, and a chapter that declares `compiled from` is honest about what it is.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 4 is untouched item by item: no new Core concept, no Constitution amendment, no change to Object, Memory, Evidence or the Knowledge derivation, and no requirement added, removed or reworded. The work this Decision authorizes is editorial and presentational work on `Specification/`, which Section 3 permits and `Master-Architecture-Backlog.md` EPIC-F already names. EPIC-F's Definition of Done is recorded executed, so Section 7 requires a scope note on that Epic before any document is edited, on the pattern `CAND-010` used.

### What this Decision does not do

It does not decide what "all mandatory requirements defined in Chapters 4 to 6" means for a conformance claim; `CAND-002` narrowed that reading for profile declarations only and `CAND-017` defers the general question. It does not build the backward check `AO-077` asks for, and it does not make one obligatory. It does not change any chapter's Status, which is `AO-051`'s question and is not decided here.

**Next Action:** Two-step discipline. Step 1 is the Chief Architect recording the Decision, after which `AO-077` moves to Open in part with its Architect Response pointing here. Step 2, each item requiring its own separate authorization: the EPIC-F scope note; a sentence in `Publication-Model.md`'s Compiled Publication tier stating the rule; the three Source lines that do not yet state their form; and a survey of the remaining chapters against their sources, which is where a backward check would start if one is ever built.

**Postscript (19 September 2026):** Step 2 items done under the authorization given the same day. The EPIC-F scope note `CAND-007` Section 7 requires is recorded in `Master-Architecture-Backlog.md`. `Governance/Publication-Model.md`'s Compiled Publication tier now states the rule and the three forms. The Source lines were surveyed: all nine chapters already declare one of the three forms, and the two that declare verbatim, Chapters 01 and 02, were checked sentence by sentence against the sections their Source lines name and carry every mandatory sentence of them. What remains, and is not authorized by this postscript: a survey of the seven chapters that declare `compiled from`, which is where a backward check would start if one is ever built, and which `AO-077` holds open.

**Related Documents:** `AO-077`, `AO-051`, `AO-032`, `AO-062`, `CAND-002`, `CAND-007`, `CAND-010`, `Governance/Publication-Model.md`, `Governance/Requirement-Register.md`, `Governance/Master-Architecture-Backlog.md` (EPIC-F), `Specification/01 Introduction.md`, `Specification/02 Design Principles.md`

---

## CAND-019 · ✅ Decided

**Title:** What the Published Graph's Prefixed Names Assert

**Status:** ✅ Decided, 19 September 2026. Filed the same day on the record of `AO-078`.

**Owner:** Chief Architect

**Created:** 19 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-078` (18 September 2026); `AO-057`; `AO-054`; `AO-045`; `AO-064`; `Meta/Reference.md`; `Meta/Relationship.md`; `Governance/Publication-Model.md` (Projection tier and Known Gaps); `https://ocom.uno/graph.jsonld` as published on 19 September 2026.

### The question

`graph.jsonld` declares `"ocom": "https://ocom.uno/vocabulary#"` and types its 83 edges `ocom:Reference` and its 7 governance candidates `ocom:ReferencedConcept`. Neither expands to anything the site defines. Behind the dangling URI sits the real question: does the publication assert that a cross reference between two term cards is an instance of the governed term Reference, defined in `Meta/Reference.md` and published at `https://ocom.uno/vocabulary/reference#term`? If it does, a generated file has decided that term cards are Objects. If it does not, the file borrows a governed term's name for something else, on the site that defines the term.

**Decision:** **The prefixed names in the publication's generated files are local names of the publication. They assert nothing about the Core Vocabulary and they create no governed term: the publication does not claim that an edge of that graph is a Reference in the sense of `Meta/Reference.md`, and nothing in this repository establishes that it is. Two rules follow for the machine-readable files the publication produces. First, a name a generated file coins shall expand to a URI that file's own publisher defines, or the file shall use a fully qualified term from a vocabulary that defines it. Second, a generated file shall not reuse the name of a governed Core Vocabulary term for a local construct, because a reader cannot tell the borrowing from a claim.**

### Rationale

1. The specification cannot afford the other reading. If an edge were an instance of the governed term Reference, then term cards would be Objects and a projection would have settled a Core question, which `CAND-007` Section 4 and the Standard Evolution Methodology both place behind a Reference Case.
2. The file already knows how to do this. Its other two node types are `https://schema.org/DefinedTerm` and `https://schema.org/DefinedTermSet`, fully qualified and resolvable. The defect is confined to the names the publication minted for itself.
3. The rules are checkable, which is the test this repository applies to its own machinery. A row in `tools/site/publication_health.py` can fetch the graph, expand every prefixed name and fail when one resolves to nothing the publisher defines, with a negative test in `tools/tests/` beside the others.
4. It leaves `AO-057` where it is. That entry records that the edges carry neither an identifier nor a Relationship type; this Decision says what their type does not assert and does not supply the missing one.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 4 is untouched: no Core concept is created or changed, and recording that a generated file's local names assert nothing removes nothing from the Core. The edits the Decision would authorize are to a generated file produced outside this repository and to this repository's own tooling and Governance records, which Section 3 permits as presentational and currency work under EPIC-F, subject to the same Section 7 scope note `CAND-018` needs.

### What this Decision does not do

It does not decide what an edge of the published graph is, which is `AO-057`'s question. It does not add a term, a type or a namespace to the Core Vocabulary. It does not change `Meta/Reference.md` or `Meta/Relationship.md`. It does not make the external Publication Engine regenerate anything: `FW-006` records that this repository cannot compel it, and the check proposed here reports the state rather than enforcing it.

**Next Action:** Two-step discipline. Step 1 is the Chief Architect recording the Decision, after which `AO-078` moves to Open in part. Step 2, each item separately authorized: the EPIC-F scope note; the rule sentence in `Publication-Model.md`; the new row and its negative test in the health tool; and the regeneration of `graph.jsonld` itself, which is publication work and is verified by running the tool against the live site.

**Postscript (19 September 2026):** every step 2 item is done, under the authorization given the same day. In this repository: the EPIC-F scope note, the rule sentences in `Governance/Publication-Model.md`'s Projection tier, and the row Coined names resolve in `tools/site/publication_health.py` with its negative tests. In the publication: `graph.jsonld` now binds the prefix `graph` to `https://ocom.uno/graph/names#`, its 83 edges are typed `graph:Edge` and its 7 concepts `graph:ReferencedConcept`, and `https://ocom.uno/graph/names` defines all eight names the file coins and states in its first paragraph that they assert nothing about the Core Vocabulary. The tool reports the row passing against the live site with 8 names checked, and `AO-078` is Closed on that evidence.

**Related Documents:** `AO-078`, `AO-057`, `AO-054`, `AO-045`, `AO-064`, `FW-006`, `CAND-007`, `CAND-018`, `Governance/Publication-Model.md`, `tools/site/publication_health.py`, `tools/tests/fake_site.py`

---

## CAND-020 · ✅ Decided

**Title:** Which of Two Mandatory Statements About Lifecycle Cardinality a Conformance Claim Is Measured Against

**Status:** ✅ Decided, 19 September 2026, on the record of `AO-079`. The wording was prepared by the CDKO and adopted without change; the choice between the options recorded below was delegated to that recommendation and taken on it.

**Owner:** Chief Architect (Decision recorded); each integration item separately authorized

**Created:** 19 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-079` (19 September 2026); `AO-028` (5 September 2026); `Models/Lifecycle.md` (Characteristics); `Lifecycles/Lifecycles.md` (Principles); `Governance/Requirement-Register.md`; `Governance/Requirement-Aliases.md`; `Governance/Conformance-Test-Suite.md` Sections 1, 2 and 3; `Specification/06 Lifecycle Model.md`; `CAND-015`.

### The question

Two mandatory Statements of the requirement set contradict each other. `REQ-MODELS-LIFECYCLE-002`, from `Models/Lifecycle.md`, requires every Lifecycle to "belong to exactly one Entity". `REQ-LIFECYCLES-004`, from `Lifecycles/Lifecycles.md`, requires every Lifecycle to "be reusable by multiple Entities". Both documents are inside the twenty-two that Chapters 4 to 6 compile, and `Specification/08 Conformance.md` defines Core Conformance as support for all mandatory requirements of those chapters, so the published level cannot be attained by any model. Which Statement binds a claimant while `AO-028`, which records the underlying divergence, waits for the Reference Case that would settle it?

**Decision:** **A claimant is measured against `REQ-MODELS-LIFECYCLE-002`. `REQ-LIFECYCLES-004` carries the Disposition Descriptive in `Governance/Requirement-Aliases.md`, with the note that it states the design intent of the reusable lifecycle patterns rather than an obligation on a Lifecycle in a conforming model, and a Test on it reports Not Applicable, which `Governance/Conformance-Test-Suite.md` already defines for a Statement dispositioned Descriptive. This settles which Statement binds and settles nothing else: no canonical document changes, both sentences stand as written, and `AO-028`'s question, whether Lifecycle names the reusable definition or the per-Entity progression, stays open and still needs a Reference Case.**

### Rationale

1. It removes the unattainability without deciding the substance. A Disposition is a Governance record about how the suite reads a Statement, which `Conformance-Test-Suite.md` Section 3 already provides for; restating either sentence would be a change to a canonical document, which the Freeze places behind a Reference Case neither entry has.
2. The tiers already point this way. `Specification/06 Lifecycle Model.md` states that Lifecycle is normative and that the specific lifecycle patterns are illustrations of it, and its editorial note of 18 September 2026 names this exact divergence. Measuring against the tier that defines the primitive rather than the tier that illustrates it follows the chapter as published.
3. The precedent is `CAND-015`. When two documents defined Domain differently, the Models-tier document was made canonical and the other informative. This Decision does less than that, because it changes no document's Status; it only records which Statement the suite measures.
4. It is checkable and it is visible. The Disposition sits in the append-only Alias File beside the Statement it concerns, so a claimant, a reviewer and the tool all read the same record, and `AO-079` stays open to say that the contradiction itself is unresolved.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 4 holds item by item: no Core concept, no Constitution amendment, no requirement added, removed or reworded, and no document's Status changed. What this Decision writes is one row in a Governance file and one note in a register. `Lifecycles/Lifecycles.md` keeps its Draft status and every sentence it carries.

### What this Decision does not do

It does not decide `AO-028`. It does not say that a Lifecycle may not be reusable, or that the Lifecycles tier is wrong. It does not remove `REQ-LIFECYCLES-004` from the register, which is generated and would regenerate it. It does not touch the other seven Statements of `Lifecycles/Lifecycles.md`, which keep binding.

**Next Action:** Two-step discipline. Step 1 is the Chief Architect recording the Decision. Step 2, each item separately authorized: the Disposition row in `Requirement-Aliases.md` with its note; a sentence in `Conformance-Test-Suite.md` Section 3 pointing at it as the first use of the Descriptive disposition; and a dated note in `AO-079` and `AO-028` recording that the conformance floor is attainable again while the divergence stands.

**Related Documents:** `AO-079`, `AO-028`, `AO-039`, `CAND-007`, `CAND-015`, `Models/Lifecycle.md`, `Lifecycles/Lifecycles.md`, `Governance/Requirement-Register.md`, `Governance/Requirement-Aliases.md`, `Governance/Conformance-Test-Suite.md`, `Specification/06 Lifecycle Model.md`

---

## CAND-021 · ✅ Decided

**Title:** Where the Sentence That Scopes Core Conformance Lives

**Status:** ✅ Decided, 19 September 2026, on the record of `AO-080`. The wording was prepared by the CDKO and adopted without change; the choice between the options recorded below was delegated to that recommendation and taken on it.

**Owner:** Chief Architect (Decision recorded); each integration item separately authorized

**Created:** 19 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-080` (19 September 2026); `CAND-018` (Decided 19 September 2026); `CAND-002`; `Language/Conformance.md` (Conformance Levels); `Specification/08 Conformance.md`; `Governance/Conformance-Test-Suite.md` Section 1; `Governance/Requirement-Register.md`; `Governance/Principle-Traceability.md`; `AO-014`; `AO-032`.

### The question

`Language/Conformance.md`, the canonical document, defines the level as "Supports all mandatory language requirements". `Specification/08 Conformance.md`, a compiled chapter, defines it as "supports all mandatory requirements defined in Chapters 4 to 6". `CAND-018` decided that a compiled chapter states no obligation of its own, so the second sentence now originates nothing, while the requirement set, the Test Suite and the traceability map all compute from it. Where does the scoping sentence live?

**Decision:** **The canonical definition of Core Conformance is the one in `Language/Conformance.md`. Chapter 8's sentence names where those requirements are found and originates nothing, consistently with `CAND-018`. The enumeration in `Governance/Requirement-Register.md`, the twenty-two documents Chapters 4 to 6 compile, is the operative reading adopted for the Conformance Test Suite and for claims measured by it, which `Conformance-Test-Suite.md` Section 1 already records for itself, and every artifact that computes from it shall say so rather than citing the chapter as the origin. Whether that reading becomes canonical text in `Language/Conformance.md` is deferred: it is a change to a canonical document, it is the same question `CAND-002` narrowed for profile declarations and `CAND-017` deferred for public claims, and it waits on the same second Reference Case.**

### Rationale

1. It keeps `CAND-018` intact. The alternative, naming Chapter 8 an exception that originates one obligation, would create a class of chapters that sometimes bind and sometimes do not, which is the ambiguity `CAND-018` was recorded to remove.
2. It changes no canonical document, so it needs no Reference Case, while the option that would change one is named and deferred rather than taken quietly.
3. It matches what the tooling already says about itself. `Conformance-Test-Suite.md` Section 1 adopts the reading "for the purpose of the suite and for that purpose only"; this Decision makes the register and the traceability map say the same, instead of asserting the chapter as canonical ground.
4. It leaves the reader better off immediately. Today three artifacts quote a chapter for a definition the chapter does not own. After step 2 they quote the canonical document and name the suite's reading as a reading.

### Scope, and the Architecture Freeze

Filed under `CAND-007`. Section 4 holds: no Core concept, no requirement changed, no canonical document edited. Every step 2 item is a wording change in a Governance file, which Section 3 permits as documentation-currency work under EPIC-F, subject to the scope note already recorded there on 19 September 2026.

### What this Decision does not do

It does not move the scoping sentence into `Language/Conformance.md`, and it does not decide whether it should be moved. It does not change what the Test Suite measures or the contents of the requirement set. It does not resolve `AO-032`, which records that no document states how the per-document Conformance sections aggregate, or `AO-014`, which records the widening the chapter performed in 2026.

**Next Action:** Two-step discipline. Step 1 is the Chief Architect recording the Decision. Step 2, each item separately authorized: `Requirement-Register.md`'s Purpose and `Principle-Traceability.md`'s How to Read It cite `Language/Conformance.md` for the level and name the twenty-two-document enumeration as the suite's reading; `Conformance-Test-Suite.md` Section 1 gains one sentence recording this Decision as its authority; and `AO-080` moves to Open in part, with the canonical-text question left open behind the same Reference Case `CAND-017` waits on.

**Related Documents:** `AO-080`, `AO-014`, `AO-032`, `AO-051`, `CAND-002`, `CAND-017`, `CAND-018`, `Language/Conformance.md`, `Specification/08 Conformance.md`, `Governance/Conformance-Test-Suite.md`, `Governance/Requirement-Register.md`, `Governance/Principle-Traceability.md`

## CAND-022 · ✅ Decided

**Title:** Where the Evidence Register Is Published

**Status:** ✅ Decided, 19 September 2026. The Chief Architect directed that the register stay in the repository and no longer be published on the site; the wording and the constraint below were prepared by the CDKO and adopted.

**Owner:** Chief Architect (Decision recorded); each integration item separately authorized

**Created:** 19 September 2026 · **Decided:** 19 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-083` (19 September 2026, machine-facing files with no source here); `AO-064` (a derived artifact nobody can recompute is a claim nobody can check); `Governance/Publication-Model.md` (tier 1 canonical source, tier 4 Convenience Representation); `Governance/Publication-Manifest.md`; `Governance/Release-Readiness.md`; `CAND-007` Section 3.

### The question

The Evidence Register separates what can be verified about the specification's use from what its owner declares and what does not exist. It was published at `ocom.uno/evidence-register` from 5 September 2026 and existed nowhere else: this repository referenced it from six documents and held none of its text. Two consequences followed. The record had no source, which is the defect `AO-083` closed for `llms.txt` earlier the same day and which mattered more here, because this register is the page every other claim of use on the site is checked against. And its most-quoted line was a ledger of three zeros, published on the surface an automated reader meets first, while the fourteen third-party records in the same document, REUSE, OpenSSF, the signed releases, the Zenodo DOIs, the Software Heritage archive, the Wikidata item, appeared in no machine-facing file at all. Where should the register live, and what should the site publish?

**Decision:** **The Evidence Register becomes a document of this repository, `Governance/Evidence-Register.md`, versioned and reviewed like every other governance record and carried into each Zenodo deposit and Software Heritage archive. The site stops publishing it and stops publishing `/implementations`; `/evidence-register`, `/evidence-register.json`, `/implementation-status` and `/implementations` redirect permanently to the repository document, so no citation of those URLs breaks. Not one count changes: the zeros stand as recorded, the ladder still reads Owner declaration, and the NDA production use stays disclosed. The constraint that makes this a publication decision rather than a concealment is binding and part of the Decision: the site shall not assert, imply or allow to be inferred any adoption, validation, implementation or endorsement it does not have, and the absence of the ledger from the site is never a licence to claim the opposite. The third-party records the register holds move into `llms.txt`, where they are as checkable as the zeros were.**

### Rationale

1. It puts the record where the model says records belong. `Publication-Model.md` calls the repository the canonical source and the site a projection; a record that existed only as a projection had no source. Fixing that is the same act `AO-083` recorded for `llms.txt`, applied to the informative record that carries the most weight.
2. It strengthens the record rather than weakening it. In the repository the register is versioned, reviewed through a pull request, checked by the metadata and link jobs, and archived under a DOI and a SWHID. On the site it was a hand-maintained page that nothing could reproduce.
3. Nothing is withdrawn from the public. The document is public, the `README` links it, the old URLs redirect to it, and its contents are unchanged.
4. What changes is which surface volunteers the ledger to an automated reader, and in what company. Order and placement are the publisher's editorial decision; the facts are not, and they stay put.
5. The move is symmetrical. The site loses a ledger of what is absent and gains, in `llms.txt`, fourteen records of what is present, each with a date and a source. A reader who wants either can reach both.

### Scope and the Architecture Freeze

Filed under `CAND-007`. Section 4 holds: no Core concept, no Canonical Principle, no requirement, no canonical document changed. Creating a governance document and changing what the site publishes is documentation and publication work, which Section 3 permits.

### What this Decision does not do

It does not change a single figure in the register, and it does not authorize any claim of adoption, validation, implementation or endorsement, now or later: that constraint is part of the Decision and binds every page of the site. It does not withdraw the disclosure of production use under NDA. It does not remove the register from public view, and it does not make the evidence ladder easier to climb: step 2, step 3 and step 4 still require a named organization, a checked implementation and a disinterested reviewer respectively. It does not decide what other site-held informative records (`/why`, `/specification/how-to-review`, `/api`, `/observatory`) should do.

**Next Action:** Two-step discipline. Step 1 is this Decision. Step 2, each item separately authorized and all executed on 19 September 2026: `Governance/Evidence-Register.md` created with the register's full content and current counts; `Publication-Model.md` tier 4 and `Governance/README.md` updated; `README.md` pointing at the repository document; `publication/llms.txt` carrying the third-party records and no longer the ledger line; the site's redirects, `sitemap.xml`, `discovery.json`, `resolve.json` and the pages that linked the register; `tools/site/publication_health.py` and its fixture no longer expecting `/evidence-register.json`; the Observatory records recomputed last, after every other change.

**Related Documents:** `Governance/Evidence-Register.md`, `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, `Governance/Release-Readiness.md`, `AO-083`, `AO-064`, `CAND-007`, `publication/README.md`

## CAND-023 · ✅ Decided

**Title:** Evidence Is Defined

**Status:** ✅ Decided, 21 September 2026, adopted as drafted. Filed the same day under `CAND-007` Section 5 on the Chief Architect's authorization recorded in `AO-084`; the wording was prepared by the CDKO and adopted without change, and integration was authorized together with the Decision, on the form `CAND-022` set. The wording below is the Decision.

**Owner:** Chief Architect (Decision); each integration item separately authorized

**Created:** 21 September 2026 · **Decided:** 21 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-084` and its Reference Case `RC-012`; `FW-001` (`Governance/Documentation-Debt.md`); `Memory/Evidence Overlay.md` (Reserved Sections, Evidence Sources, Auditability); `Memory/Memory Record.md` (Evidence); `Core/Constitution.md` Principle 3; `Core/Manifest.md` (Abstract); `Governance/Evidence-Register.md`; `CAND-014`; `Master-Architecture-Backlog.md` EPIC-A.

### The question

Evidence is the fourth word of the specification's identity statement, "identity, ownership, lifecycle and evidence", and the subject of Canonical Principle 3, Evidence Before Belief. `Memory/Evidence Overlay.md` reserves its Definition, its Source and Reliability attributes, its Independence and its Conformance for a future version, since the v0.1 release candidate review of 21 July 2026 (`FW-001`), and the disposition of 16 September 2026 writes them only as Layer 2 of `CAND-014` needs them. Every Memory Record shall reference at least one Evidence Record, and nothing says what an Evidence Record must contain beyond an identifier, a reference, a description and a date, nor how its reliability is to be recorded. An adopter's auditor who asks what the specification counts as evidence finds a reservation. Should the four sections be written now, ahead of EPIC-A, and on what text?

**Decision:** **The four reserved sections of `Memory/Evidence Overlay.md` are written now, as a Freeze exception, in the following form; EPIC-A Layer 2 inherits them rather than waiting for them.**

- *Definition.* An Evidence Record is the retained account of why a Memory Record holds its value: what was observed or asserted, from which source, and how reliable that source was judged to be at the time. Evidence explains; it does not decide. A Memory Record without Evidence is a belief, and Principle 3 does not permit a retained belief without traceable Evidence.
- *Source*, a mandatory attribute: the origin of the Evidence, named as one of the Evidence Sources this document lists, with an identifier of the specific origin where one exists, and the value unknown source where it does not.
- *Reliability*, a mandatory attribute: the recorded judgement of the source's reliability at the time of recording, on a scale the organization defines and declares, together with the actor who recorded the judgement. Reliability is a property of the Evidence; Confidence, which summarises it across the Evidence a Memory Record references, stays where `Memory/Confidence.md` puts it.
- *Independence.* Evidence is independent of the Memory Record it supports, which may gain new Evidence without changing; of Metadata, which Principle 3 forbids merging with it; of Confidence, which it explains and does not replace; and of implementation technology.
- *Conformance.* A compliant implementation shall implement the mandatory attributes; preserve an Evidence Record unaltered after creation and represent corrections as new Evidence Records; support every Evidence Source this document lists, including unknown source; record Source and Reliability with the actor who recorded them; and, once `CAND-024` is decided, be able to demonstrate that an Evidence Record has not been altered.

### Rationale

1. The gap is now visible from outside. The enterprise evaluation of 20 September 2026 scored the risk lens 3 of 10 and named the reserved Definition as its first decisive finding. `FW-001`'s disposition was written before that evaluation and answered a different question, whether v1.0 needed the sections; this candidate answers whether an adopter does.
2. Nothing here is new. Every element of the proposed text is already in the document in another place: the Evidence Sources list, the Auditability actor, the Immutability section, the Relationship to Confidence. The proposal states what the document already implies, in the sections that were reserved for it.
3. It keeps EPIC-A whole. Layer 2 of `CAND-014` needs Evidence defined in order to say what guarantees Knowledge inherits; writing the definition first gives that Layer a stated input instead of a reservation to fill on the way.
4. It costs one Freeze exception, which `AO-084`'s Reference Case grounds, and it is the smaller of the two candidates that case escalates.

### Scope and the Architecture Freeze

Filed under `CAND-007` Section 5, with filing authorized on 21 September 2026. Section 4 holds: no Canonical Principle is reworded, no Meta Object is added, Object, Memory, Evidence and Knowledge keep their shape; four reserved sections of one Memory-tier document are written. Rule 1 of `Standard Evolution Methodology.md` is met with a margin it does not require for a document completion: `RC-012` supplies the case and the Reader's `ADR-007` a second, implementation-side instance.

### What this Decision does not do

It does not decide what an implementation must be able to demonstrate about a record; that is `CAND-024`. It does not define Audit record. It does not change `Memory/Confidence.md` or move Confidence. It does not touch the Constitution. It does not close `AO-084`, which waits on both candidates.

**Next Action:** Two-step discipline. Step 1, the Decision, is recorded above. Step 2, authorized with it and executed on 21 September 2026: the four sections written into `Memory/Evidence Overlay.md` with a Revision History row citing this candidate; `FW-001` closed in `Documentation-Debt.md`; `Requirement-Register.md` and `Test-Catalogue.md` regenerated, since the new Conformance clause adds Statements; `AO-084` narrowed.

**Related Documents:** `AO-084`, `AO-021`, `CAND-024`, `CAND-014`, `CAND-007`, `FW-001`, `Memory/Evidence Overlay.md`, `Memory/Memory Record.md`, `Memory/Confidence.md`, `Core/Constitution.md`, `Governance/Evidence-Register.md`

---

## CAND-024 · ✅ Decided

**Title:** What an Implementation Must Be Able to Show About a Record: an Integrity Guarantee for Memory and Evidence, an Audit Record, and What Erasure Preserves

**Status:** ✅ Decided, 21 September 2026, adopted as drafted. Filed the same day under `CAND-007` Section 5 on the Chief Architect's authorization recorded in `AO-084`; the wording was prepared by the CDKO and adopted without change, and integration was authorized together with the Decision, on the form `CAND-022` set. This is the second of the two Freeze-exception candidates `CAND-007` Section 1 named on 27 July 2026, and the one its Section 5 postscript of 18 September 2026 recorded as still unfiled. The wording below is the Decision.

**Owner:** Chief Architect (Decision); each integration item separately authorized

**Created:** 21 September 2026 · **Decided:** 21 September 2026 · **Decided by:** Chief Architect

**Grounding:** `AO-084` and its Reference Case `RC-012`; `AO-069`; `AO-075`; `Governance/Architecture-Release-Review-v1.0.md` Part 2, finding 3 (27 July 2026); `CAND-007` Sections 1 and 5; `Governance/Architecture-Principles.md` Principle 2; `Core/Constitution.md` Principles 4 and 6; `Memory/Memory Record.md`; `Memory/Evidence Overlay.md`; `Memory/Retention.md`; `Governance/Conformance-Test-Suite.md` Sections 3 and 4; `OCOM-Reader` `ADR-007`.

### The question

Constitution Principle 4 makes Memory append-only and a Memory Entry immutable after creation, and twenty-two canonical documents require that Audit records remain immutable. No clause requires an implementation to be able to show that a record is unaltered, so two implementations can both claim immutability and a reader cannot tell which one is lying; the Release Review called this "an assertion, not a checkable property" on 27 July 2026. Around that gap sit two others the register already holds: Audit record is defined nowhere (`AO-075`), and `Memory/Retention.md`'s Deleted state stands against Principles 4 and 6 (`AO-069`) because nothing says what an erasure preserves. What must an implementation be able to demonstrate about a record, what is an Audit record, and what does erasure keep?

**Decision:** **Three clauses, at the Memory tier, naming a property each and a mechanism in none.**

1. *The guarantee.* A compliant implementation shall be able to demonstrate, to a party holding a Memory Record or an Evidence Record together with its identity and nothing else, that the record has not been altered since its creation. The Specification names no mechanism. Content-addressed identity and hash chaining are two that satisfy the clause; an implementation that satisfies it another way conforms.
2. *The Audit record.* An Audit record is a Memory Record whose subject is a governance action on an Object: its creation, modification or retirement, an approval, a change of Ownership or Classification, the application of a Policy. The clause "Audit records shall remain immutable", wherever it stands, is satisfied by Principle 4 together with clause 1 and requires nothing further of an implementation. No new term enters the Core Vocabulary; the definition is by reference to Memory Record.
3. *Erasure.* A Memory Record is never altered. Where law or organizational policy requires that retained content no longer be recoverable, an implementation shall make the content of the affected record irrecoverable while preserving the record's identity, its timestamp and actor, and its demonstration under clause 1, and shall record the erasure as a new Memory Record naming what was erased and under which policy. `Memory/Retention.md`'s Deleted state means this and nothing else. Reconstructability, Principle 6, holds for everything except the erased content, which is the purpose of the erasure.

### Rationale

1. It is a guarantee, not a mechanism, which is the only form the corpus permits it to take. Architecture Principle 2 frees every internal algorithm and excepts exactly one thing: "the process of recording provenance may carry minimal normative constraints where their absence would make a guarantee unfalsifiable". Without clause 1, immutable is unfalsifiable; with it, the Test Suite can fail an implementation.
2. It closes two open observations by reference rather than by addition. `AO-075` asked for Audit record to be defined, listed as Reserved, or removed; clause 2 defines it as a Memory Record with a named subject, so the twenty-two clauses acquire a subject and the eight of them in the mandatory Core Conformance set become decidable. `AO-069` recorded the Deleted state against Principles 4 and 6; clause 3 says what an erasure preserves, so Deleted stops contradicting append-only and Reconstructability keeps its meaning.
3. It answers the regulated adopter. An auditor asks for a demonstration and a lawyer asks for erasure; today the corpus offers a promise to the first and a contradiction to the second. The enterprise evaluation of 20 September 2026 named both as decisive.
4. An implementation has already had to invent it. The Reader's `ADR-007` gives each Memory Entry a content-hash identity and supersedes rather than edits, because the Specification gave it no property to satisfy. That is the second standing trigger `CAND-007` Section 5 names for breaking the Freeze.

### Scope and the Architecture Freeze

Filed under `CAND-007` Section 5, with filing authorized on 21 September 2026. Section 4 holds: no Canonical Principle is reworded, no Meta Object is added, the Memory → Knowledge → World Model direction is untouched, and Object, Memory, Evidence and Knowledge keep their shape. Three clauses are added to Memory-tier documents, each stating a property. `Standard Evolution Methodology.md` Rule 1 is met by `RC-012` and the Reader's `ADR-007`; Rule 2, Repeatability Before Standardization, is the Chief Architect's judgement here: two instances exist, both traceable to the same author, one of them code that runs. If that is judged insufficient, the form `CAND-017` set is available, deciding the guarantee in principle and gating its text on an independent implementation's report.

### What this Decision does not do

It does not mandate hashing, signing, a ledger or any storage technology. It does not define Evidence; that is `CAND-023`. It does not add a Core Vocabulary term: Audit record is defined by reference to Memory Record. It does not decide what personal data is or which law applies; it states what an erasure keeps, so that any erasure policy can be applied without breaking the record. It does not touch the Constitution.

**Next Action:** Two-step discipline. Step 1, the Decision, is recorded above. Step 2, authorized with it and executed on 21 September 2026: clause 1 written into the Conformance sections of `Memory/Memory Record.md` and `Memory/Evidence Overlay.md`; clause 2 written into `Memory/Memory Record.md` as a named Memory Type or a section of its own; clause 3 replacing the Deleted section of `Memory/Retention.md` and its Conformance item "support controlled deletion"; `Governance/Conformance-Test-Suite.md` Section 3 gains a sixth Test kind, Integrity, whose procedure obtains the demonstration clause 1 requires and can return Fail; `tools/conformance/validate.py` gains the procedure and `Test-Catalogue.md` is regenerated; `AO-069` and `AO-075` close; `AO-084` closes when both candidates are integrated.

**Related Documents:** `AO-084`, `AO-069`, `AO-075`, `AO-064`, `CAND-023`, `CAND-007`, `CAND-014`, `Governance/Architecture-Release-Review-v1.0.md`, `Governance/Architecture-Principles.md`, `Core/Constitution.md`, `Memory/Memory Record.md`, `Memory/Evidence Overlay.md`, `Memory/Retention.md`, `Governance/Conformance-Test-Suite.md`, `Governance/Evidence-Register.md`

**Postscript (21 September 2026, from the tests):** two things the suite made precise the same day. First, a digest stored inside the record it hashes shows that the export is consistent, not that the record is unaltered: alter the record, recompute the digest, and it matches again. Clause 1 asks for a demonstration to a party holding only the record and its identity, and among the mechanisms it names only content-addressed identity provides that with nothing else in hand; `tools/conformance/validate.py` therefore passes an Integrity Test on content-addressed identity and reports a self-contained digest as pending for a reviewer. Second, clause 3 preserves the demonstration through an erasure, and an erased record no longer verifies by design; `Memory/Retention.md` now says what the preserved demonstration means, that the content was what it was at creation and has since been erased, and the suite excludes a record named by an erasure record rather than failing it. Neither changes the three clauses.

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
| 0.1 | 21 August 2026 | CAND-011: final review found the original draft only authorized presentation adaptation, not the base per-file Projection grant CAND-012's own Scope condition 2 requires. Corrected (base grant + Decision Boundary added, both verified against First Pilot.md's actual header) and recorded as Decided — Promote. CAND-012's editorial note updated to reflect CAND-011 is now Decided |
| 0.1 | 21 August 2026 | Added CAND-013 (Consumer Tool publication category + native Shape Check authorization) — Status: Proposed, not Decided. Filed because Shape Check fits none of Publication-Model.md's four existing tiers (no canonical source document at all) and because Architecture Principles 1/5 (contracts not products; Reader is reference not authority) raise a genuine, unresolved question about whether an interactive tool belongs on the Specification's own domain — both points flagged for Chief Architect judgment, not resolved by this filing. Native /shape-check page prepared (algorithm unchanged from the Claude artifact; added version banner and First Pilot forward link) but explicitly not published pending this Decision |
| 0.1 | 21 August 2026 | Revised CAND-013 after a focused adversarial review: added two explicit page-level normative-boundary statements ("creates no normative requirements," "not a source of truth"), itemized non-assertions to name each excluded category individually (other tools, other interactive pages, /tools/, arbitrary JavaScript, other top-level interactive routes, automatic future publication, and preserved CAND-012's docs/Adoption/ blanket-authorization prohibition), added a named terminology-drift residual risk to the Governance implication, and added one sentence explaining why /shape-check sits outside /adoption/ without creating a general taxonomy rule. Algorithm/CONCEPTS list confirmed unchanged |
| 0.1 | 21 August 2026 | CAND-013: a second focused adversarial review confirmed all four fixes correctly applied and the algorithm still unchanged, verdict READY FOR DECISION. Synchronized the "why this may not simply extend an existing authorization" section's Principle 1/5 discussion with that review's findings (Principle 1 PASS, Principle 5 PASS by analogy, terminology drift reframed from open tension to named residual risk) without touching scope or decision architecture, then recorded as Decided — Promote: Publication-Model.md gains a fifth category (Consumer Tool), Shape Check authorized as its one instance at /shape-check, all non-assertions and the Decision Boundary binding as drafted |
| 0.1 | 5 September 2026 | CAND-009: recorded the Decided field (20 August 2026, Reference Cases `AO-008`) that the Status asserted but the entry never carried; Path A, Consequence, template and Next Action marked superseded with dated postscripts. CAND-013: removed the pre-Decision hedge from the Decision Boundary and replaced the stale "Awaiting Decision" Next Action; noted the removal of the prototype link. No decision changed. |
| 0.1 | 10 September 2026 | Added CAND-014 (Knowledge, World Model, and the Location of Current State) — Decision recorded, Option 4 (three-layer split by time horizon), Layer 1 only: derivation semantics decided, `AO-003` answered with its Option B (Status is a derived projection in World Model), the `Knowledge.md` "independent of Memory Records" line recorded as an inaccuracy for correction on integration. Layer 2 (authoring `Meta/World-Model.md`, rewriting `AI/Knowledge/*`) explicitly not decided and gated behind the `CAND-007` freeze-exception pipeline. Two-layer structure follows the `CAND-009` precedent. No document outside the two governance registers changed. Resolves `Master-Architecture-Backlog.md` EPIC-A's decision step; Core integration remains a separately authorized task. |
| 0.1 | 11 September 2026 | CAND-006: added a dated postscript recording that its quoted Canonical Principle list stays at the 26 July 2026 adoption wording, and that Principles 9 and 11 were transcribed into `Core/Constitution.md` (1.0.1) on 11 September 2026 per Decisions 4 and 5, the integration `CAND-007` §4 names as permitted. No Decision changed. |
| 0.1 | 11 September 2026 | CAND-014: postscript recording that Step 2, the Layer 1 Core integration, was performed (`Knowledge.md` Definition corrected, `Memory Record.md` Status restated as derived) and that `AO-042` is resolved in part by it. Step 3, Layer 2, unchanged and still gated. No Decision changed. |
| 0.1 | 11 September 2026 | Added CAND-015 (Domain Definition Divergence) — Decision recorded: `Models/Domain.md` is the canonical normative definition of Domain; `Domains/Common/Domain.md` is informative, restates rather than extends, and its four extra characteristics carry no normative force. Consolidation was considered and not taken, because folding those characteristics into `Model-02` would add requirements and needs the `CAND-007` freeze-exception pipeline, which has no independent Reference Cases today. Resolves `AO-001`, the oldest open observation. No document changed; integration is a separately authorized step. |
| 0.1 | 16 September 2026 | CAND-002 Decided: Profile Conformance is defined by the form of a claimant's declaration, not by any profile this repository publishes. Eight declaration rules and ten validator assertions recorded in `Governance/Concept-Paper-Profile-Conformance.md`; the Core is not coupled to the mechanism and no profile is defined or authorized. Satisfies half of `EPIC-E`'s Definition of Done. |
| 0.1 | 16 September 2026 | CAND-001 Decided: `AI/Agents/Context.md` is replaced with an explicit reference to `AI/Context/Overview.md`; the Agents section does not own a description of Context. Path, Document ID and reading-path position kept; no requirement added or removed. Closes `OBS-001`, open since 21 July 2026. Integration performed in the same change as EPIC-C work under `CAND-007` Section 3. |
| 0.1 | 16 September 2026 | Added CAND-016 (Relationship Participants), Decision recorded: `Meta/Relationship.md` is the canonical definition of Relationship with Objects as participants; `Models/Relationship.md` is its specialization for Relationships between Entities and restricts nothing else. Resolves `AO-002`; no requirement changed; integration in the same change as EPIC-B work. CAND-004: postscript recording a v1.0 disposition for each of the seven questions (each question resolved by existing primitives, not required for v1.0 pending a Reference Case, or split between the two); Status line updated. CAND-015: postscript recording that Step 2, the integration into `Domains/Common/Domain.md`, is done. |
| 0.1 | 16 September 2026 | CAND-002: postscript recording that four of the six Step 2 items are done under EPIC-F (Chapter 8, `Language/Conformance.md`, `Adoption/FAQ.md`, Backlog); the Projection and the CI validator remain open as tooling. |
| 0.1 | 16 September 2026 | CAND-014: postscript recording the Chief Architect's v1.0 disposition: Layer 1 closes EPIC-A for the v1.0 claim; Layer 2 stays open and gated, not required for v1.0. |
| 0.1 | 16 September 2026 | CAND-015: second postscript recording that six shall-sentences of `Domains/Common/Domain.md` have no counterpart in `Models/Domain.md`, contrary to the Decision's premise for those sentences; they bind nothing as the document is Informative. |
| 0.1 | 18 September 2026 | CAND-014: postscript recording that the Chief Architect extended the v1.0 EPIC-A disposition to `Memory/Layered Memory.md` and `Memory/Retention.md`, with the contradiction left open as `AO-069`. |
| 0.1 | 18 September 2026 | Added CAND-017 (Stewardship of the Name OCOM and the Phrase OCOM-compatible), Open, filed as a `CAND-007` Section 5 Freeze exception from `AO-071` and `RC-011`; CAND-007 gained a postscript recording that one of its two named Section 5 candidates is now filed. |
| 0.1 | 19 September 2026 | Added CAND-018 (what a compiled chapter carries from its sources) and CAND-019 (what the published graph's prefixed names assert), both Open, each carrying a proposed Decision text for the Chief Architect to record or to change; `AO-077` and `AO-078` are Escalated to them. |
| 0.1 | 19 September 2026 | CAND-017 Decided in part: a condition on a public conformance claim is inside scope at the Language tier with its text gated on a second Reference Case, a right in the name is outside the Specification, and a register of declarations is declined. CAND-018 and CAND-019 Decided as filed. |
| 0.1 | 19 September 2026 | CAND-017, CAND-018 and CAND-019: postscripts recording the step 2 items done the same day (the EPIC-F scope note, the two tier rules and the Known Gaps entry) and naming what each leaves open. |
| 0.1 | 19 September 2026 | CAND-019: postscript updated, every step 2 item is done and `AO-078` is Closed on the evidence the tool reports against the live site. |
| 0.1 | 19 September 2026 | Added CAND-020 (which of two contradicting mandatory Statements a conformance claim is measured against) and CAND-021 (where the sentence that scopes Core Conformance lives), both Open, each carrying a proposed Decision; `AO-079` and `AO-080` are Escalated to them. |
| 0.1 | 19 September 2026 | CAND-020 and CAND-021 Decided as drafted: a claimant is measured against `REQ-MODELS-LIFECYCLE-002` with `REQ-LIFECYCLES-004` dispositioned Descriptive, and the canonical definition of Core Conformance is `Language/Conformance.md`'s while the twenty-two-document enumeration is the suite's reading. |
| 0.1 | 19 September 2026 | Added CAND-022 (where the Evidence Register is published) and recorded it Decided: the register becomes `Governance/Evidence-Register.md`, the site redirects the published URLs to it, no figure changes, and the site is bound not to assert adoption, validation or implementation it does not have. |
| 0.1 | 21 September 2026 | Added CAND-023 (Evidence defined: the four reserved sections of `Memory/Evidence Overlay.md`) and CAND-024 (an integrity guarantee for Memory and Evidence, an Audit record by reference, and what erasure preserves), both filed Open as `CAND-007` Section 5 Freeze exceptions on the authorization `AO-084` records, each with a proposed Decision for the Chief Architect. `CAND-007` Section 5 carries a postscript that its second named candidate is now filed. |
| 0.1 | 21 September 2026 | CAND-023 and CAND-024 Decided as drafted, the same day they were filed, with integration authorized alongside on the form `CAND-022` set: `Memory/Evidence Overlay.md` carries its Definition, Source, Reliability, Independence and Conformance; `Memory/Memory Record.md` and `Memory/Evidence Overlay.md` carry the integrity guarantee; `Memory/Memory Record.md` defines Audit Record by reference; `Memory/Retention.md`'s Deleted state means erasure as defined; `Conformance-Test-Suite.md` gains the Integrity Test kind. |
| 0.1 | 21 September 2026 | CAND-024 postscript: the suite showed that only content-addressed identity meets clause 1 with nothing else in hand, and that an erased record's preserved demonstration shows the content at creation; `Memory/Retention.md` says so, the clauses are unchanged. |

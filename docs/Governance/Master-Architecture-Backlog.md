<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Master Architecture Backlog

[← Back](Architecture-Audit-Current-State.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Master Architecture Backlog — From Audit to OCOM v1.0

**Document ID:** GOV-MASTER-BACKLOG-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

This is the Chief Architect's backlog, not a product roadmap. It converts `Architecture-Audit-Current-State.md`, every still-open item in `ADR-Candidates.md` and `Architecture-Observations.md`, and every open entry in `Documentation-Debt.md` into a single, structured program of work. No new architectural idea, principle, or model is introduced here. Every item below traces to an existing record, cited by ID.

---

# Part 1 — Inventory of Open Architectural Work

Pulled from three sources, verified directly against each:

**From the Audit** (`Architecture-Audit-Current-State.md`, Parts 5–6): C1–C12, plus the gaps in Part 6.

**From `ADR-Candidates.md`**, still open: `CAND-001` (= C5, `OBS-001`), `CAND-002` (Profile Conformance mechanics — not previously surfaced in the Audit), `CAND-004` (Modeling Cross-Organization Relationships, 7 sub-questions — not previously surfaced in the Audit).

**From `Architecture-Observations.md`**, still open: `AO-001` (= C3), `AO-002` (= C4), `AO-003` (= C6), `OBS-001` (= C5/CAND-001), `OBS-003` (correctly parked, not escalated — included for completeness, not active work).

**From `Documentation-Debt.md`**, still open: `DEBT-DOC-001` (docs/README.md content regression), `GAP-001` (filename convention inconsistency), `GAP-002` (`Core/Terminology.md` missing Object/Capability/Policy/Contract/Context/Knowledge/Memory), `FW-001` (Evidence Overlay Definition/Independence/Conformance reserved), `FW-002` (Campaign.md Business Rules removed), `FW-003` (no Reference Agent exists anywhere), `FW-004` (no Reference Implementation exists anywhere), `FW-005` (Governance visibility in `docs/README.md`).

**From Constitution integration itself:** `Constitution-Step0-Summary.md` remaining-work items #6 and #7 (§9 and §11 wording never updated in `Core/Constitution.md` to match Decisions 4 and 5).

That is the complete raw list. Nothing below adds to it — Part 2 only groups it.

---

# Part 2 — Normalization

Fifteen-plus individually-tracked items collapse to six root causes:

| Root cause | Items absorbed |
|---|---|
| The Memory → Knowledge → World Model chain is broken or absent | C1, C2, C6/`AO-003`, C7, `FW-001` |
| A foundational term (Domain) is defined twice, and Relationship cannot yet accommodate the Object types Constitution already recognizes | C3/`AO-001`, C4/`AO-002`, `CAND-004` |
| AI/* subsections and the business-modeling layer (Domains/Entities) are internally coherent but not wired to Constitution or to each other | C5/`CAND-001`/`OBS-001`, C9, C10 |
| Constitution's own text has not caught up to decisions already made about it, and terms it uses are undefined elsewhere | §9/§11 wording, C12, `GAP-002` |
| No mechanism exists to verify a compatibility claim, and nothing has ever implemented the contract independently | Conformance Test Suite gap, `CAND-002`, `FW-003`, `FW-004` |
| The presentation/onboarding layer is stale relative to Constitution, and several small self-admitted content gaps remain | C8, C11, `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005`, `Entities/Department` stub, `Workflows/` (status only, not content) |

`OBS-002` (Closed) and `OBS-003` (correctly parked by governance rule) are not active work; they appear here only as a completeness note, not as backlog items.

---

# Part 3 — Epic Structure

| ID | Epic | Root cause |
|---|---|---|
| EPIC-A | Memory–Knowledge–World Model Derivation Chain | Broken/absent derivation chain |
| EPIC-B | Object Model & Cross-Organization Consolidation | Domain duplication, Relationship gap |
| EPIC-C | AI / Domain / Entity Integration | Unwired islands |
| EPIC-D | Constitution & Terminology Closure | Stale Constitution text, undefined terms |
| EPIC-E | Conformance & Reference Implementation | No verification mechanism, no independent build |
| EPIC-F | Specification Currency & Presentation | Stale onboarding, small self-admitted gaps |

This does not match the example structure given in the task ("Entry Point, Knowledge, World Model, Integration, Conformance, Governance") on purpose: the Audit shows Knowledge and World Model share one root cause and one Concept Paper/Discussion already in hand, so they are one Epic, not two; and Governance's own methodology was rated Mature in the Audit, with no open backlog-worthy item beyond continuing to use it — so there is no separate Governance Epic, only Epic F's smaller documentation-currency items.

---

# Part 4 — Epic Detail

## EPIC-A — Memory–Knowledge–World Model Derivation Chain

**Architectural goal:** make Knowledge and its downstream derivation actually satisfy Constitution §3, §5, §6, instead of contradicting them.

**Why it exists:** `Knowledge.md` states Knowledge "is independent of... Memory Records" — the literal opposite of §5. World Model, the chain's third stage, has no document. `AO-003` found the same write/derive ambiguity one layer down, in Memory Record's own `Status` field. `FW-001` left Evidence Overlay's Definition/Independence/Conformance sections unwritten, which this Epic's resolution will need in order to state what Evidence guarantees Knowledge inherits.

**Documents affected:** `AI/Knowledge/*` (5 docs), a new World Model document (does not yet exist), `Memory/Memory Record.md` (`AO-003` clause), `Memory/Evidence Overlay.md` (`FW-001` reserved sections).

**Related AO/ADR:** `AO-003`; analysis already complete in `Concept-Paper-Knowledge-vs-World-Model.md` and `Architecture-Discussion-Knowledge-vs-World-Model.md` (Decision Readiness: **Yes**, per that document's own Part 8) — no ADR Candidate has been filed yet for the actual choice among its four options.

**Definition of Done:** an ADR Candidate is filed and decided for the Knowledge/World Model split; `AI/Knowledge/*` no longer contradicts §5/§6/§3; a World Model document exists with at least a Definition and a stated relationship to Knowledge and Memory; `AO-003` is resolved as part of the same decision (the Discussion document already frames it as the same question at a smaller scale); `FW-001`'s reserved sections are written only as needed to support the decision, not before.

## EPIC-B — Object Model & Cross-Organization Consolidation

**Architectural goal:** one authoritative definition of Domain, a Relationship model that accommodates every Object type Constitution §1 already recognizes, and a decided answer to how independent Organizations interact.

**Why it exists:** `Models/Domain.md` and `Domains/Common/Domain.md` define Domain differently (`AO-001`). `Models/Relationship.md` restricts participants to Entity, so Organization — already a first-class Object per `CAND-005` — cannot participate in a Relationship (`AO-002`). `CAND-004` is a fully-scoped, seven-question research candidate already waiting on exactly these two fixes; it explicitly does not re-litigate the Object Model, only asks how Organizations connect once it is consistent.

**Documents affected:** `Models/Domain.md`, `Domains/Common/Domain.md`, `Meta/Relationship.md`, `Models/Relationship.md`, `Meta/Organization.md`, plus everything `CAND-004` already lists (`Meta/Reference.md`, `Meta/Ownership.md`, `Meta/Identity.md`, `Meta/Registry.md`, `Meta/Contract.md`, `Meta/Policy.md`).

**Related AO/ADR:** `AO-001`, `AO-002`, `CAND-004` (open, blocked on the first two), `CAND-005` (Decided — the basis `CAND-004` builds on).

**Definition of Done:** `AO-001` and `AO-002` each have a recorded Decision; `Models/Relationship.md` and `Meta/Relationship.md` no longer disagree on participant types; `CAND-004`'s seven questions each have either a recorded Decision or an explicit "not required for v1.0" disposition.

## EPIC-C — AI / Domain / Entity Integration

**Architectural goal:** remove the one confirmed live content duplication, and give the business-modeling layer (Domains/Entities) a real, consistent bridge to Memory/Evidence — not just a boilerplate paragraph present in some subdomains and absent in others.

**Why it exists:** `AI/Context/Overview.md` and `AI/Agents/Context.md` are still near-verbatim duplicates (`OBS-001`/`CAND-001`, open since 21 July). The "AI Memory" section pattern exists in 8 of 14 Domains subdomains and is absent in the other 6 (C9). `Entities/` (51 files) has almost no reference to Memory/Evidence/Knowledge at all (C10) — the layer that would actually be populated in a real deployment has no defined connection to the layer this Specification has spent the most effort making rigorous.

**Documents affected:** `AI/Context/Overview.md`, `AI/Agents/Context.md`; the six Domains subdomains missing the AI-Memory section (Affiliate, HR, Legal, Marketing, Operations, Support); `Entities/*` (structural addition, not full rewrite).

**Related AO/ADR:** `OBS-001`, `CAND-001`.

**Definition of Done:** `CAND-001` has a recorded Decision and is integrated (no duplicate content remains, or the duplication is explicitly justified and kept); the AI-Memory linkage pattern is either present uniformly across all 14 Domains subdomains or its absence in specific subdomains is an explicit, stated decision, not silence; every Entity document has an explicit statement of how it relates to Memory (even if the answer is "no direct relationship, mediated entirely through Domain-level AI-Memory linkage" — the point is that the silence itself is closed).

## EPIC-D — Constitution & Terminology Closure

**Architectural goal:** make Constitution's own text match decisions already made about it, and make sure every term Constitution uses is defined somewhere in the Specification.

**Why it exists:** `Constitution-Step0-Summary.md` decided §9's scope (semantic invariance, not directory-based) and §11's framing (conformance/capability, not architecture-mandate) — but §9 and §11's actual wording in `Core/Constitution.md` was never updated to say so; these are named as its own remaining-work items #6 and #7. Separately, the Audit found Constitution §14 uses "Autonomy level" with no document anywhere defining it (C12), and `GAP-002` already logged that `Core/Terminology.md` omits Object, Capability, Policy, Contract, Context, Knowledge, and Memory despite each having its own normative document.

**Documents affected:** `Core/Constitution.md` (§9, §11 wording only — meaning already decided, not reopened), `Core/Terminology.md`, and whatever new short document (or extension of an existing one) ends up defining Autonomy levels.

**Related AO/ADR:** `Constitution-Step0-Summary.md` (Decisions 4 and 5, already made), `GAP-002`.

**Definition of Done:** §9 and §11 read consistently with their own recorded interpretation; `Core/Terminology.md` defines every term Constitution uses, including Autonomy level; no Constitution term is used without a locatable definition anywhere in the Specification.

## EPIC-E — Conformance & Reference Implementation

**Architectural goal:** make "OCOM-compatible" a provable claim, not a self-declared one, per Architecture Principle 6 — and prove the contract is independently buildable, per Architecture Principle 5.

**Why it exists:** no Conformance Test Suite exists anywhere (named explicitly as a gap by Architecture Principle 6 itself). `CAND-002` has been open since 22 July, asking exactly how profile-based Conformance would work, with no mechanism decided. `FW-003` and `FW-004` record, in this Specification's own Documentation Debt register, that neither a Reference Agent nor a Reference Implementation exists anywhere in the repository — the "five years without Reader" analysis showed this is not a hypothetical risk but a documented, standing gap today.

**Documents affected:** every document with a `# Conformance` section (nearly all of them, as a consumer of whatever criteria this Epic defines); `Language/Conformance.md` and `Specification/08 Conformance.md` specifically for the profile mechanism; a new Conformance Test Suite artifact (does not yet exist); a Reference Implementation (does not yet exist, and is explicitly out of Specification scope to author directly — see Part 9).

**Related AO/ADR:** `CAND-002`, `FW-003`, `FW-004`.

**Definition of Done:** `CAND-002` has a recorded Decision; a checkable Conformance Test Suite specification exists (even if initial tooling is minimal); the guarantees it tests are stable (depends on EPIC-A, EPIC-D). A Reference Implementation existing is listed as Future Work here, not required for this Epic's own closure — see Part 8 for why.

## EPIC-F — Specification Currency & Presentation

**Architectural goal:** stop routing newcomers into a pre-Constitution picture of OCOM, and close the small, already-logged, self-admitted content gaps.

**Why it exists:** `Specification/` (v0.2) was approved 22 July 2026, before Constitution existed, and `Adoption/` still names it "the actual entry point" (C8). `Examples/Overview.md` promises six industry collections and silently has one (C11) — unlike `Workflows/`, which honestly labels itself "Planned for future versions." `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005`, and the `Entities/Department` stub are each individually small, already-tracked items in this same category.

**Documents affected:** `Specification/*` (10 docs), `Adoption/README.md`, `Adoption/Worked Example - Library Lending.md` (new), `Examples/Overview.md`, `docs/README.md`, `Entities/Department/`, `Entities/Campaign/Campaign.md`, `Governance/Knowledge-Map.md`.

**Related AO/ADR:** `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005`, `CAND-010`.

**Definition of Done:** `Specification/` either reflects Constitution or is explicitly marked superseded, with `Adoption/` re-pointed accordingly; `Examples/Overview.md`'s stated scope matches what actually exists, the same way `Workflows/README.md` already does; the four small Documentation-Debt items are closed or have a recorded disposition; one universal, Informative Worked Example exists under `Adoption/`, per `CAND-010`.

**Execution note (20 August 2026):** the publication-governance slice of this Epic — disambiguating Constitution/Core Vocabulary/Specification/Release as four independent version tracks, single-sourcing the RFC 2119/8174 definition to `Core/Manifest.md`, correcting `Entities/Overview.md`'s Status against `Constitution-Step0-Summary.md` Decision 4, adding a Status Taxonomy, and documenting (not silently fixing) the `v1.0.0` Release's scope mismatch — has been executed via `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, and `Governance/Release-Workflow.md`. This closes the version-identity and normative-reference portion of "stop routing newcomers into a pre-Constitution picture of OCOM." The `Specification/*`↔`Constitution` content re-pointing itself, `Adoption/README.md`'s entry-point claim, and `Examples/Overview.md`'s scope-parity gap remain open — this note does not close this Epic.

**Scope amendment (21 August 2026):** Adds one explicit work item to this Epic — a single universal, Informative Worked Example under `Adoption/` (not `Examples/`, which is reserved for industry-specific collections per `Examples/Overview.md`'s own "Organization" section). Authorized by `CAND-010` — Decided, 21 August 2026 (`Governance/ADR-Candidates.md#cand-010`), as a scope-authorization-only decision: it does not certify the example's content, does not privilege Library Lending as the only valid domain, grants no authorization to Shape Check, and does not itself authorize any second or future Adoption artifact.

---

# Part 5 — Work Items: Priority, Effort, Risk, Dependencies

| Work item | Epic | Priority | Effort | Risk | Dependencies |
|---|---|---|---|---|---|
| Decide Knowledge/World Model split (file + resolve ADR) | A | Critical | L | High — the largest single architectural decision left | None (already decision-ready) |
| Write World Model document | A | Critical | M | Medium — first-ever document for this concept | Knowledge/World Model decision |
| Resolve `AO-003` (Memory Record Status) | A | High | S | Low — narrow, well-scoped | Knowledge/World Model decision (same underlying question) |
| Complete `FW-001` (Evidence Overlay reserved sections) | A | Medium | S | Low | Knowledge/World Model decision (only what it needs) |
| Resolve `AO-001` (Domain vs Domain) | B | High | S | Medium — touches a widely-referenced term | None |
| Resolve `AO-002` (Relationship/Organization) | B | High | S | Medium | None |
| Decide `CAND-004` (7 questions) | B | Medium | L | Medium — broad surface, many documents | `AO-001`, `AO-002` |
| Resolve `CAND-001`/`OBS-001` (Context duplication) | C | Medium | S | Low | None |
| Close the 6-domain AI-Memory linkage gap | C | Medium | M | Low | None (independent of A/B, but low value until A is resolved) |
| Bridge `Entities/*` to Memory/Evidence | C | High | L | Medium — 51 files | EPIC-A decision (need a stable target to bridge to) |
| Update Constitution §9/§11 wording | D | High | S | Low — pure transcription of an existing decision | None |
| Define Autonomy level (C12) | D | High | M | Medium — genuinely new content, not transcription | None |
| Extend `Core/Terminology.md` (`GAP-002`) | D | Medium | S | Low | Autonomy-level definition (to include it) |
| Decide `CAND-002` (Profile Conformance mechanics) | E | High | M | Medium | None, but low value until A/D are stable |
| Design Conformance Test Suite | E | Critical | XL | High — largest single deliverable in the backlog | EPIC-A, EPIC-D (guarantees must be stable first) |
| Build a Reference Implementation (`FW-004`) | E | Medium (see Part 8) | XL | High | EPIC-A–D substantially complete; explicitly not Specification-authored, see Part 9 |
| Refresh or retire `Specification/` v0.2; re-point `Adoption/` | F | High | M | Low | Ideally after EPIC-D (so it reflects the closed §9/§11 wording too), but not blocked by it |
| Align `Examples/Overview.md` scope with reality | F | Low | S | Low | None |
| Close `DEBT-DOC-001`, `GAP-001`, `FW-002`, `FW-005` | F | Low | S | Low | None |

---

# Part 6 — Dependency Graph

```
EPIC-D (§9/§11 wording, Terminology)         EPIC-B (AO-001, AO-002)
        │  no upstream dependency                   │  no upstream dependency
        │                                            │
        ▼                                            ▼
   [can start immediately, parallel to each other and to EPIC-A's decision step]

EPIC-A — Knowledge/World Model decision
        │  (blocks everything below)
        ├──────────────────────────────┐
        ▼                              ▼
EPIC-A — World Model doc,       EPIC-C — Entities/Memory bridge
AO-003, FW-001                  (needs a stable target to bridge to)
        │                              │
        ▼                              ▼
EPIC-C — Context dedup (CAND-001), domain AI-linkage gap
   [low dependency on A, can run early, but low value until A lands]
        │
        ▼
EPIC-B — CAND-004 (7 questions)
   [depends on AO-001 + AO-002, not on EPIC-A]
        │
        ▼
EPIC-E — CAND-002 (Profile Conformance)
   [depends on EPIC-D being stable — profiles need stable terminology]
        │
        ▼
EPIC-E — Conformance Test Suite design
   [depends on EPIC-A (Knowledge/World Model guarantees) and EPIC-D
    (no undefined terms to test against) — cannot start meaningfully before both]
        │
        ▼
EPIC-E — Reference Implementation (FW-004)
   [depends on the Test Suite existing — otherwise nothing to prove compliance against]

EPIC-F — Specification currency
   [no architectural dependency on any of the above; should run in parallel,
    ideally finishing after EPIC-D so it can describe a fully-closed Constitution]
```

**Must happen before anything else:** the EPIC-A Knowledge/World Model decision. It is the single most-referenced dependency in the graph — EPIC-C's Entities bridge, EPIC-E's Test Suite, and (indirectly, through terminology completeness) EPIC-D's Autonomy definition all either need it directly or benefit from it being settled first.

**Can run in parallel, starting immediately:** EPIC-B's `AO-001`/`AO-002` (self-contained, no dependency on Knowledge/World Model), EPIC-D's §9/§11 wording update (pure transcription), EPIC-F (no architectural dependency at all).

**Does not make sense to start before its dependency lands:** `CAND-004` before `AO-001`/`AO-002` (it explicitly says so itself); the Conformance Test Suite before EPIC-A and EPIC-D are stable (nothing stable to test); a Reference Implementation before the Test Suite exists (nothing to prove compliance against — and per Architecture Principle 1/5, building it before the contract itself is settled risks the implementation silently becoming the de facto contract).

---

# Part 7 — Milestones (by Specification Maturity, Not Calendar Time)

**Milestone 1 — No Known Architectural Contradiction.** EPIC-A's decision is recorded and integrated; EPIC-B's `AO-001`/`AO-002` are resolved. Nothing in the Specification any longer says the opposite of what Constitution requires. (`AI/Knowledge/*` no longer contradicts §5/§6; `Models/Relationship.md` and `Meta/Relationship.md` agree.)

**Milestone 2 — Contract Closed.** EPIC-D is complete (Constitution's own text matches its own decisions; every term is defined somewhere); EPIC-C's integration items are closed (no live duplication, Entities bridged to Memory, Domains' AI-linkage pattern applied consistently or its exceptions are explicit). An independent team reading only Constitution + Specification could, in principle, build every layer without guessing.

**Milestone 3 — Conformance Operational.** EPIC-E's Test Suite design and `CAND-002` are both decided and specified. "OCOM-compatible" becomes a claim that can be checked, not just asserted.

**Milestone 4 — Independent Implementation Exists.** `FW-004`/`FW-003` are closed — at least one implementation, built independently of the Specification's own authors' existing product work, exists and passes the Milestone 3 Test Suite. This is the concrete test of Architecture Principle 1 and 5 actually holding, not just being stated.

Milestone order matches Part 6's dependency graph directly: 1 before 2 (EPIC-C's bridge needs EPIC-A's outcome), 2 before 3 (a Test Suite over undefined terms or unresolved duplication is not meaningful), 3 before 4 (nothing to prove an implementation compliant against otherwise).

---

# Part 8 — Release Readiness: "OCOM Specification v1.0 Ready"

Minimum mandatory set — not "desirable," not "complete every backlog item":

- **EPIC-A fully closed.** A Specification that contradicts its own Constitution in a core document cannot honestly be called v1.0, regardless of anything else.
- **EPIC-B's `AO-001` and `AO-002` closed.** A foundational term defined twice, and a first-class Object type that cannot participate in the Specification's own Relationship model, are the same category of defect as EPIC-A's. `CAND-004`'s seven questions do **not** all need to be closed — each may instead carry an explicit "not required for v1.0" disposition, per its own "Next Action."
- **EPIC-D fully closed.** An undefined term used by Constitution itself is a direct completeness failure of the document being versioned.
- **EPIC-C's `CAND-001`/`OBS-001` closed**, and Entities minimally bridged to Memory (does not require full 14-domain AI-linkage uniformity — that may carry an explicit disposition instead, same as `CAND-004`).
- **EPIC-E's Conformance criteria written and checkable in principle** (a decided `CAND-002` and a specified, even if not yet fully tooled, Test Suite). A fully automated Suite and a completed Reference Implementation (`FW-003`/`FW-004`) are **not** required for the v1.0 claim — the Specification and its conformance criteria are what is being versioned, not the existence of implementations against it. This is a judgment call, stated plainly as one: the counter-argument is that an unimplemented Test Suite is exactly the kind of unverifiable guarantee the stress test warned about, and a stricter reading would require Milestone 4 before any v1.0 claim.
- **EPIC-F's core item only** — `Specification/`/`Adoption/` re-pointed so the documented onboarding path is not actively misleading. The smaller items (`GAP-001`, filename conventions; `Examples/` scope-parity) are not required for v1.0.

Everything not listed above may remain open post-v1.0 with an explicit disposition, consistent with how this Specification has already treated `CAND-004`'s scope and `OBS-003`.

---

# Part 9 — Stop List

Only items architecturally blocked by the backlog above, per the instruction to include something here only if it is genuinely blocked, not merely deferrable by preference:

- **New Domains subdomains beyond the existing 14.** Blocked by EPIC-B: the definition of Domain itself is still disputed (`AO-001`). Adding more domains under a contested definition compounds exactly the debt EPIC-B exists to close.
- **New Entity types.** Blocked by EPIC-C: `Entities/` has no defined Memory bridge yet. Adding entities before the bridge exists means every new entity has to be retrofitted once EPIC-C lands.
- **New AI/* subsections or capabilities.** Blocked by EPIC-A: the layer they would build on (Knowledge/World Model) is not yet stable. This directly matches Architecture Principle 8 (Evolution Without Lock-In) read in reverse — new capability categories should map onto a settled contract, not an unsettled one.
- **New Workflows content.** Blocked by EPIC-C: Workflows sits atop Entities/Domains, which are not yet fully wired to Memory. Writing Workflows now means building on ground EPIC-C is still repairing.
- **New industry Examples collections.** Not blocked in the strict architectural sense (Examples is explicitly non-normative), but each would demonstrate an architecture that is mid-repair; writing five more now risks needing a rewrite once EPIC-A/B land. Included here because the cost of waiting is low and the cost of redoing is not.
- **Any new Constitution principle or amendment.** Blocked by EPIC-D: Constitution's own integration (§9/§11 wording) is not finished. Amending further before the current integration is closed is the exact drift pattern Architecture Principle 5 warns about.
- **Any new Profile definition for Conformance.** Blocked directly by `CAND-002`: the profile mechanism itself has not been decided, so no concrete profile can be defined yet.
- **Pulling Reader/product-roadmap concepts (e.g. persona-adaptive explainer work, "OCOM Bot") into the Specification.** Blocked by EPIC-E and Architecture Principle 5: the Specification/Reader boundary work (Test Suite, independent implementation) is not done, and product-shaped content entering the Specification before that boundary is proven is exactly the governance-capture risk already named.

---

# Part 10 — Final Recommendation

If leading OCOM's development starting tomorrow morning, the first three items, in this order:

**1. File and decide the ADR Candidate for Knowledge vs. World Model (EPIC-A).** This is the single highest-leverage item in the entire backlog: it is already fully analyzed (`Concept-Paper-Knowledge-vs-World-Model.md`, `Architecture-Discussion-Knowledge-vs-World-Model.md`, explicitly rated "Decision Readiness: Yes"), so no new research is needed — only the decision itself — and it unblocks more downstream work (EPIC-C's Entities bridge, EPIC-E's Test Suite, part of EPIC-D) than any other single item in the graph.

**2. Update Constitution §9 and §11's own wording (EPIC-D).** The lowest-cost item in the entire backlog — pure transcription of decisions already made (`Constitution-Step0-Summary.md`, Decisions 4 and 5) — and it closes a standing inconsistency in the single most authoritative document in the Specification. Near-zero risk, immediate credibility gain, and it can proceed in full parallel with item 1.

**3. Resolve `AO-001` (Domain vs. Domain).** The oldest unresolved item in the entire inventory (logged 25 July), self-contained, small in scope (two documents), and it directly unblocks `CAND-004` — a large, already fully-scoped body of work (seven research questions, already narrowed to exactly what remains undecided) that is otherwise just waiting.

These three share the same property: each is either already decision-ready or trivially small, and each unblocks work disproportionate to its own size. Nothing about EPIC-E (Conformance, Reference Implementation) belongs in the first three — it is the most expensive work in the backlog, and starting it before EPIC-A and EPIC-D land means designing a test suite against guarantees that are still moving.

---

# Status

This is a backlog, not a decision. No specification document has been changed. No new ADR Candidate has been created — every item above already exists as an AO, ADR Candidate, or Documentation Debt entry, or is transcribed directly from the Audit. Executing any item in this backlog requires its own separate, explicit authorization, per the two-step discipline already used throughout this Specification's governance.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial backlog, six Epics, normalized from the Architecture Audit plus the full open-item register in `ADR-Candidates.md`, `Architecture-Observations.md`, and `Documentation-Debt.md` |

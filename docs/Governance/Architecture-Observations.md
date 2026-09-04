<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Observations

[← Back](Architecture-Health.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Observations

**Document ID:** GOV-OBSERVATIONS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 29 July 2026

---

# Purpose

This document records architectural inconsistencies, ambiguities, and potential improvements noticed by the CDKO.

The CDKO records observations. It does not resolve them. Resolution is the responsibility of the Chief Architect, recorded in the Architect Response field.

---

## OBS-001

**Title:** Content duplication between AI/Context/Overview.md and AI/Agents/Context.md

**Date observed:** 21 July 2026

**Description:** The two documents are textually identical in body content. They differ only in their Document ID field (`AI-Context-00` vs `AI-Agents-05`).

**Impact:** It is unclear whether this is an intentional cross-reference between the Agents and Context sections, or an accidental duplication that occurred during preparation of the source documents.

**Recommendation:** The Chief Architect should decide whether to keep the duplicate, replace `AI/Agents/Context.md` with an explicit reference to `AI/Context/Overview.md`, or give `AI/Agents/Context.md` distinct, Agent-specific content.

**Status:** Open — escalated, see ADR-Candidates.md#cand-001

**Architect Response:** *(pending)*

**Related:** `AI/Context/Overview.md`, `AI/Agents/Context.md`, `Documentation-Debt.md#OBS-001`, `ADR-Candidates.md#cand-001`

---

## OBS-002

**Title:** Reference Architecture layer name retains "Business Object" while internal vocabulary uses "Entity"

**Date observed:** 21 July 2026

**Description:** During terminology unification, "Business Object" was replaced with "Entity" throughout the specification, including the Reference Architecture layer name ("Business Object Architecture" → "Entity Architecture") and all internal section headers. On author review, the layer name was restored to "Business Object Architecture," while the internal section headers of `Object-Architecture.md` (Entity Identity, Entity Ownership, Entity Lifecycle, etc.) and body prose across the rest of the specification retained "Entity."

**Impact:** `Object-Architecture.md` now has a title using "Business Object" while its own section headers use "Entity" — a deliberate, author-approved duality rather than an unresolved inconsistency.

**Recommendation:** None — already resolved by explicit author decision.

**Status:** Closed

**Architect Response:** Restored "Business Object Architecture" as the layer name; all other terminology changes to "Entity" approved and kept. Author decision, 21 July 2026 (v0.1 Release Candidate review).

**Related:** `Reference Architecture/Object-Architecture.md` and 6 sibling Reference Architecture documents, `Documentation-Debt.md#OBS-002`

---

## OBS-003

**Title:** Reference Case — Object Attribute Lifecycle Categories

**Date observed:** 22 July 2026

**Description:** Submitted as a ready-formed normative clarification ("Attribute Categories"), documented here per the Reference Case template (`Standard Evolution Methodology.md`, Section 3) rather than adopted directly, per Rule 5 (a Reference Case shall not modify the Core directly).

| Field | Content |
|---|---|
| **Reference Case** | Object Attribute Lifecycle Categories |
| **Purpose** | Disambiguate what "required" means for an Object's attributes, distinguishing attributes required by the Object primitive itself from those required by a Type definition, those introduced after objects already exist, and those computed rather than stored. |
| **Expressive Coverage** | Partially expressible with existing concepts. `Models/Entity.md` defines Attributes generically (name, meaning, data type, optional constraints) without distinguishing categories. `Meta/Object.md` defines Identity and Metadata but does not separate "structural" identity fields from type-specific or business fields. Neither document has a concept of a versioned Object Type, or of migration semantics for attributes introduced after object creation. |
| **Boundary Conditions** | (1) No existing concept separates attributes whose presence is required for an artifact to be a valid Object at all, from attributes required only by a specific, versioned Type definition. (2) No existing concept addresses what happens when a new required attribute is introduced after Objects of that Type already exist. (3) No existing concept distinguishes stored from derived/computed attributes, or states how a derived attribute's validity depends on its source attributes. (4) The case references a "Type Versioning & Compatibility" document that does not exist anywhere in the current specification — i.e., it presumes a concept (versioned Object Type) that has not itself been established. |
| **Boundary Tags** | `structural-integrity` (validity of an artifact as an Object depends on structural fields being present); `set-scoped-constraint` (Type-level requirements apply to a bounded subset of Objects — those created under a given Type version — not universally); `temporal-dependency` (requiredness and migration handling depend on when an Object was created relative to a Type version change); `input-completeness` (the entire case is fundamentally about whether required information is present, and what to do when it is not, at various points in time). |
| **External Assurance** | None provided with this submission. The case arrived as a fully-formed proposed rule set, not as a report of an observed operational scenario, so it cannot currently be distinguished from hypothesis. This is itself recorded as a limitation of the case, not a judgment on its merit. |
| **Core Impact** | Possible, not Recommended. Per Rule 2 of `Standard Evolution Methodology.md`, a single Reference Case — independent or not — does not on its own justify a Core extension; independent corroborating cases would be needed. Per Rule 1, Core shall not be extended on this case alone. |

**Impact:** If the underlying boundary is real and recurring, it would eventually touch `Meta/Object.md` (Identity, Metadata) and `Models/Entity.md` (Attributes), and would require introducing a concept not currently in the specification: a versioned Object Type, distinct from Entity/Object as currently defined. That would be a Core extension, not a clarification.

**Recommendation:** Do not modify `Meta/` or `Models/` on the basis of this single case. If the Chief Architect has, or is aware of, independent Reference Cases demonstrating the same boundary (Rule 2), those should be submitted and linked here to test for a Repeated Pattern before an ADR Candidate is considered.

**Status:** Open — logged as a Reference Case observation; not escalated to ADR Candidates (insufficient independent corroboration per Rule 1/2)

**Architect Response:** *(pending)*

**Related:** `Standard Evolution Methodology.md` (Reference Case template, Rules 1, 2, 5), `Meta/Object.md`, `Models/Entity.md`

---

## AO-001

**Title:** Domain Definition Divergence

**Date observed:** 25 July 2026

**Description:** `Models/Domain.md` (`Model-XX`) and `Domains/Common/Domain.md` (`DOM-DOMAIN-01`) contain two independent normative models of Domain, with differing scope:

- `Models/Domain.md`: "A Domain is an operational boundary responsible for governing one or more **Entities**... A Domain represents what is governed, not who performs the work."
- `Domains/Common/Domain.md`: "A Domain is a logical business boundary responsible for managing a coherent set of **Objects**, capabilities, policies, processes, and operational outcomes."

The two documents use separate Document ID schemes, define different Core Characteristics (`Domains/Common/Domain.md` additionally includes Capabilities, Policies, Constraints, and Integration Points), and neither cross-references the other as authoritative.

**Impact:** It is unclear which document is the canonical normative source for Domain, whether one is a specialization of the other, or whether the two require consolidation. No specification changes have been made pending this determination.

**Recommendation:** The Chief Architect should determine: (1) which of the two is canonical; (2) whether one is a specialization of the other; (3) or whether consolidation is required. No changes to be made to either document until this is decided.

**Status:** Open

**Architect Response:** *(pending)*

**Related:** `Models/Domain.md`, `Domains/Common/Domain.md`

---

## AO-002

**Title:** Relationship Participant Inconsistency

**Date observed:** 25 July 2026

**Description:** `Meta/Relationship.md` defines Relationship as a governed association between **Objects** (`Source Object` / `Target Object`). `Models/Relationship.md` (`Model-03`) normatively restricts participants to **Entity** only ("Every Relationship shall define: Source Entity; Target Entity").

Following the adoption of the Organization model (ADR CAND-005, Option C — Organization as a first-class peer specialization of Object) and the integration of `Meta/Organization.md`, this divergence has become architecturally significant: `Meta/Organization.md` states that Organization connects to other Objects "exclusively through ordinary, governed Relationships," yet Organization is explicitly not an Entity, so it cannot satisfy `Models/Relationship.md`'s current Source/Target Entity constraint.

**Impact:** As currently written, `Models/Relationship.md` does not permit Organization (or any non-Entity Object) to participate in a Relationship, which contradicts the architectural model established by CAND-005 and `Meta/Organization.md`. No specification changes have been made pending resolution.

**Recommendation:** A separate architectural decision is required to determine how `Models/Relationship.md` should accommodate non-Entity Object participants (e.g., broadening participants to Object, or defining an explicit specialization relationship between the Meta and Model layers). No changes to be made until that decision is recorded.

**Status:** Open — related to ADR CAND-005 and the pending CAND-004 rework (Modeling Cross-Organization Relationships)

**Architect Response:** *(pending)*

**Related:** `Meta/Relationship.md`, `Models/Relationship.md`, `Meta/Organization.md`, `ADR-Candidates.md#cand-005`, `ADR-Candidates.md#cand-004`

---

## AO-003

**Title:** Mutable Status in an Immutable Memory Model

**Date observed:** 27 July 2026

**Description:** Following adoption of Constitution §4 (Immutable Memory), §5 (Memory Precedes Knowledge), and §6 (Reconstructability), and their migration into `Memory/Memory Record.md` (ARCH-001) and `Memory/Evidence Overlay.md` (ARCH-006), the `Status` attribute of a Memory Record (`Active`, `Pending Verification`, `Archived`, `Expired`, `Rejected`) was found to have undefined semantics relative to the append-only model. Two readings are both defensible from the current text and neither is decided:

- **Option A — Status is part of the Memory Record.** A record's Status is fixed at creation. A transition such as `Pending Verification → Active` cannot occur without modifying an existing record, which conflicts directly with §4.
- **Option B — Status is not a record field but a derived projection.** "Current status" is computed at read/derivation time from the full append-only sequence of Memory Records for a given subject (Memory → Knowledge → Current Status), consistent with §5 and §6. This is a materially different model from what `Memory Record.md` currently describes.

**Impact:** As currently written, `Memory Record.md` lists `Status` as a Mandatory Attribute without resolving which reading applies, leaving an open contradiction between the Status model and §4 under Option A. No specification changes have been made pending resolution; this was deliberately left unresolved during the Memory/Evidence migration (Constitution integration, Stage 2) as out of scope for a migration task.

**Recommendation:** The Chief Architect should determine whether Status is a Memory Record attribute (with transition semantics to be defined) or a Knowledge-layer derived projection. This is a new architectural question, not a migration of an already-decided principle, and should be evaluated on its own via the standard evolution process before any document is changed.

**Status:** Open

**Architect Response:** *(pending)*

**Related:** `Memory/Memory Record.md`, `Governance/Constitution-Step0-Summary.md`, `Core/Constitution.md` (§4, §5, §6)

---

## AO-004

**Title:** Reader Produces No Memory-Record-Shaped Output

**Date observed:** 29 July 2026

**Description:** RC-005 (Vector repository, `reference/rc005/`) ran `OCOM-Reader`'s real, unmodified `FilesystemDocumentationAdapter` and `to_memory_entry()` against real documents and compared the resulting `MemoryEntry` (`ocom_reader/core/memory.py`) against `Memory Record.md`'s (Memory-02) Mandatory Attributes. Of 8 required attributes (Identifier, Subject, Memory Type, Value, Layer, Status, Created Date, Evidence), only Identifier and Evidence have a corresponding field on `MemoryEntry`. Subject, Memory Type, Value, Layer, and Status have no corresponding concept — not on `MemoryEntry`, and not on `OCOMObject` (`ocom_reader/core/object.py`), the output of Reader's one existing Normalizer stage (`FilesystemDocumentationNormalizer`), which targets OCOM's Object model (`Meta/Object.md`'s Core Characteristics: Identity, Metadata, Classification, Relationships, Lifecycle, Ownership, Governance), not Memory Record. Reader's own `ADR-007` frames `MemoryEntry` explicitly as a pre-Memory-Record staging concept ("Memory Before Knowledge"), and the existing Normalizer's docstring states it deliberately does not interpret document content, deferring that to a future LLM-based Normalizer.

**Impact:** Reader currently produces `MemoryEntry` objects that cannot be consumed as public Memory Records without implementation-specific adaptation. Any system (such as Vector) intending to consume Reader's output as OCOM Memory Records must either wait for Reader to implement that stage, or build an intermediary of its own — a real interoperability gap, demonstrated directly rather than assumed, though confined to one implementation's current stage of development, not the Specification.

**Recommendation:** None offered here. This is an observation, not a decision. At least three directions are visible and are explicitly not chosen or ranked by this entry: (a) Reader's own Normalizer pipeline evolves to eventually produce a full Memory Record; (b) a separate Memory Builder component is introduced between Reader and any Memory-Record consumer; (c) the Memory Record contract itself is reconsidered. Selecting among these is a Chief Architect / `OCOM-Reader` roadmap decision, not something this observation resolves.

**Status:** Open

**Architect Response:** *(pending)*

**Related:** `Memory/Memory Record.md`, `AO-003` (this observation follows directly from validating AO-003's Option B direction against real code), `OCOM-Reader` (`core/memory.py`, `core/object.py`, `adapters/filesystem_documentation.py`, `normalizers/filesystem_documentation_normalizer.py`, `ADR-007`), Vector (`reference/rc005/RESULTS.md`)

---

## AO-005

**Title:** Attribute Data-Type Facet Has No Self-Describing Value Structure — Evidenced Concretely by Quantitative Measurement Ambiguity

**Date observed:** 29 July 2026

**Description:** `Models/Entity.md` requires every Attribute to declare a "data type" (its Attributes section: "name; meaning; data type; optional constraints") but defines no structure for what a data type's content must self-describe beyond a bare label. Two independent Reference Cases surfaced the same boundary from unrelated sources.

| Field | Content |
|---|---|
| **Reference Case** | RC-006 — Quantitative Ambiguity in Real Operational Data |
| **Purpose** | Determine whether OCOM's existing Attribute/data-type concept can unambiguously carry the quantitative business facts surfaced in real internal operational data from an operating company in the traffic/UGC-agency sector. |
| **Expressive Coverage** | Partially expressible. `Models/Entity.md` names "data type" as a required Attribute facet but defines no structure for it; nothing in `Meta/` or `Models/` states what a numeric Attribute's content must self-describe beyond its bare value. |
| **Boundary Conditions** | (1) A stated debt figure and a tax obligation figure appear in the source material with no currency ever specified — an AI agent consuming these as plain Attribute values cannot determine USD/EUR/UAH/other. (2) Sales KPI targets and ROI figures appear as bare numbers with no indication of whether they are a percent, a fraction, or a plain score. (3) A vacation duration and a project timeline appear with no calendar anchor, so neither is safely convertible to the other or to a common base unit. |
| **Boundary Tags** | `structural-integrity`; `input-completeness`; `environmental-signal` (comparing money depends on an external market rate the model has nowhere to record); `cross-object-dependency` (a rate/ratio's meaning depends on two coordinated parts, not expressible as one bare Attribute). |
| **External Assurance** | Drawn from real, dated internal operational data from an existing operating company, not a hypothesis — the same underlying material was independently used to construct a real BI object model, where the ambiguity was directly encountered, not synthesized for this filing. Specific figures and the company's identity are withheld from this public record; the ambiguity class described above is fully reproducible without them. |
| **Architectural Observations** | This entry (`AO-005`). |
| **Core Impact** | Recommended. |
| **Decision** | Escalated to ADR Candidate — see `ADR-Candidates.md#cand-008`. |

| Field | Content |
|---|---|
| **Reference Case** | RC-007 — The Same Ambiguity Already Latent in OCOM's Own Released v0.1 Core |
| **Purpose** | Determine whether the RC-006 boundary is specific to one external system, or already present inside OCOM's own already-published Domain content — a second, independent source, per Rule 2 (Repeatability Before Standardization). |
| **Expressive Coverage** | Partially expressible, by the same gap as RC-006. `Domains/Finance/Finance_KPIs.md`, `Domains/Operations/Operations_KPIs.md`, and `Domains/BI/BI_Objects.md` all name quantitative KPI/Metric concepts without a representation model. |
| **Boundary Conditions** | (1) `Domains/Finance/Finance_KPIs.md` names "average processing time," "reconciliation cycle time," and "financial close duration" — Duration concepts with no unit. (2) `Domains/Operations/Operations_KPIs.md` names "Work Completion Rate," "Task Completion Rate," and "Milestone Achievement Rate" — Rate concepts with no numerator/denominator structure. (3) `Domains/BI/BI_Objects.md` lists "Ratio" as an example Metric Object with no representation rule distinguishing a percent from a fraction from a plain score. |
| **Boundary Tags** | `structural-integrity`; `input-completeness`. |
| **External Assurance** | Drawn from already-released, already-reviewed v0.1 Core content (`Domains/Finance/`, `Domains/Operations/`, `Domains/BI/`), independent of RC-006's source company and independent of this filing's own motivation — the boundary was already present in the Specification before this filing was written, not introduced by it. |
| **Architectural Observations** | This entry (`AO-005`). |
| **Core Impact** | Recommended. |
| **Decision** | Escalated to ADR Candidate — see `ADR-Candidates.md#cand-008`. |

RC-006 and RC-007 reach the same Boundary Condition from two independent sources — a real external company's operational data, and OCOM's own already-published Domain content — satisfying Repeatability Before Standardization without requiring a hypothetical second case. Neither Reference Case fits inside an existing `Master-Architecture-Backlog.md` Epic (A–F); the closest, `EPIC-D` (Constitution & Terminology Closure), closes undefined *terms*, not undefined value *structure*.

**Impact:** As currently written, no OCOM Attribute — in this Specification's own Domain content or in any conformant implementation — can express a Money, Percentage, Duration, Quantity, Physical Unit, or Rate value in a way that is self-describing enough for an AI agent to compare, aggregate, or normalize it without an undocumented assumption. This is a gap in the Meta-model (`Meta/`), not in any single Domain profile, since every Domain's KPI documents inherit it identically.

**Recommendation:** Per `Standard Evolution Methodology.md`'s Minimal Core principle, the recommended resolution is not a narrow Measurement-only addition, but a general **Value** Meta-construct (the self-describing content an Attribute's data-type facet holds — Value Kind, Representation, Semantics, Context, Resolution Status) with Measurement specified as its first fully-designed Value Kind, since that is the one with concrete, repeated evidence here. Other plausible Value Kinds (Scalar, Reference, Composite) should be named but left unspecified pending their own Reference Cases — this observation has no evidence for those boundaries and should not pre-design them. A full Concept Paper is attached to the escalation (`ADR-Candidates.md#cand-008` → `Concept-Paper-Value-Model.md`) for the Chief Architect's review; no change is made to `Meta/` or `Models/` by this entry.

**Status:** Open — escalated, see `ADR-Candidates.md#cand-008`

**Architect Response:** *(pending)*

**Related:** `Models/Entity.md`, `Domains/Finance/Finance_KPIs.md`, `Domains/Operations/Operations_KPIs.md`, `Domains/BI/BI_Objects.md`, `Standard Evolution Methodology.md` (Reference Case template, Repeatability Before Standardization, Minimal Core), `ADR-Candidates.md#cand-007` (Architecture Freeze — this is filed as a Freeze exception under its §5/§6), `ADR-Candidates.md#cand-008`, `Concept-Paper-Value-Model.md`

---

## AO-006

**Title:** Observation vs. Interpretation vs. Value vs. Meaning — Does an Attribute Hold a Value Directly, or an Interpretation of One or More Observations?

**Date observed:** 29 July 2026

**Description:** During Chief Architect review of `CAND-008` (the Value Model, filed on `AO-005`), a further architectural question was raised, independent of `AO-005`'s own boundary and not a defect in it: `CAND-008` assumes an Attribute directly holds a Value. That assumption is stated to be appropriate for a business data model, but may not hold as OCOM evolves toward an operational knowledge graph intended to support AI reasoning, where a Value is often not a primitive fact but the interpretation of one or more Observations. The conceptual pipeline offered for comparison is `Observation → Interpretation → Value → Meaning`, against the simpler `Attribute → Value` pipeline `CAND-008` currently assumes.

**Impact:** If a Value is, in general, derived from one or more Observations rather than held directly, `CAND-008`'s Value Model as designed has no place to record which Observation(s) a Value derives from, how conflicting Observations of the same fact are represented and resolved, how uncertainty in that derivation is carried, or how the derivation stays reproducible for AI reasoning — evidence traceability, conflicting observations, uncertainty handling, provenance, and reproducible AI reasoning were named specifically. This is recorded so `CAND-008`'s eventual promotion decision is made with the question visible, not silently closed — it is explicitly not raised as a defect requiring correction now.

**Recommendation:** No change to `CAND-008` or `Concept-Paper-Value-Model.md` on the basis of this observation alone — per `Standard Evolution Methodology.md` Rule 1 (Evidence Before Architecture), no Reference Case currently demonstrates the need for an Observation layer, so none is proposed here. This is recorded as a standing precondition check: before `CAND-008` is promoted to ADR (before Value becomes normative), this question should be checked against any Reference Case that surfaces an evidence-traceability, conflicting-observation, uncertainty, provenance, or reproducibility need that `Attribute → Value` cannot express. If such a case is filed and the boundary repeats independently (Rule 3 — Repeatability Before Standardization), `CAND-008` or a successor candidate would need to revisit whether Value sits atop an Observation/Interpretation layer rather than being held directly by an Attribute.

**Status:** Open — recorded per Chief Architect review of `CAND-008`; not escalated to an ADR Candidate (no Reference Case exists yet)

**Architect Response:** No Core impact at this time. No Reference Case currently demonstrates the need for an Observation layer, so `CAND-008` is not required to address it now. Recorded as an open architectural question to be checked against future Reference Cases before `CAND-008`'s promotion, not resolved here.

**Related:** `ADR-Candidates.md#cand-008`, `Concept-Paper-Value-Model.md`, `AO-005`, `Standard Evolution Methodology.md` (Rule 1 — Evidence Before Architecture, Rule 3 — Repeatability Before Standardization)

---

## AO-007

**Title:** Core Concepts Must Eliminate a Demonstrated Deficiency, Not Introduce a New Abstraction — a Candidate Refinement to Standard Evolution Methodology's Evidence Before Architecture Principle

**Date observed:** 29 July 2026

**Description:** During Chief Architect review of `AO-005` → `CAND-008` → `Concept-Paper-Value-Model.md` → `AO-006`, a further observation was made about the evolution methodology itself, not about any specific Core concept: `Standard Evolution Methodology.md`'s existing principles (Evidence Before Architecture, Minimal Core, Principle of Minimal Evolution) already argue against adding concepts speculatively, but do not yet state, as one explicit rule, the sharper distinction this session's work actually applied — a new Core concept must **eliminate** a demonstrated deficiency in the existing model, not merely **add** a new abstraction that happens to be elegant, general, or plausibly useful. The distinction was demonstrated directly, not hypothesized: the original submission proposed Measurement; only because the existing model could not express the boundary at all was Measurement generalized to Value; had Value also failed to resolve it, the correct next step would have been a further Observation, not a further concept. Architecture is stated to grow bottom-up — reality forcing an expansion — never top-down — a concept proposed first and a justification found for it after.

**Impact:** Not itself a deficiency in `Standard Evolution Methodology.md` — its existing principles already point in this direction, and the methodology already produced the correct outcome in this session's work without this rule being written down anywhere. This is a candidate sharpening of it: making explicit, as a checkable rule, a distinction the methodology currently implies but does not state directly. Recorded so the refinement is not lost, and so it is evaluated on its own evidentiary terms rather than adopted on the strength of one clean example.

**Recommendation:** Do not amend `Standard Evolution Methodology.md` on the basis of this single episode — both the Chief Architect's own framing ("оформить явно когда-нибудь," someday, not now) and the methodology's own Repeatability Before Standardization principle argue for waiting on further instances before formalizing this as an explicit rule. If a future episode independently reproduces the same shape (a concept proposed, found to be a symptom rather than a cause, and generalized or deferred to a further Observation instead of being adopted as proposed), that would be a second independent instance and sufficient grounds to open an ADR Candidate proposing new text for `Standard Evolution Methodology.md` itself — noting the Governance Framework is a reviewed, frozen baseline (`ROADMAP.md`: "further changes to this section go only through its own approved process"), so such a Candidate would need to satisfy that section's own approval process, not only the general Reference Case pipeline it describes.

**Status:** Open — recorded per Chief Architect observation; not escalated to an ADR Candidate (one instance only; awaiting independent repetition per Repeatability Before Standardization)

**Architect Response:** Agreed this should not be formalized yet. The distinction is real — a new concept should appear only when the existing model cannot express reality, this is confirmed by multiple independent Reference Cases, and a minimal extension genuinely removes the deficiency, never because a concept is "beautiful," "general," or "might be useful" — but it should be recorded as evidence toward a future, independently-corroborated refinement of `Standard Evolution Methodology.md`, not written into it now on one example.

**Related:** `Standard Evolution Methodology.md` (Evidence Before Architecture, Minimal Core, Principle of Minimal Evolution, Repeatability Before Standardization), `AO-005`, `ADR-Candidates.md#cand-008`, `Concept-Paper-Value-Model.md`, `AO-006`, `Governance-Manifest.md`

---

## AO-008

**Title:** Publication Version-Identity Has No Documented Relationship Between Core Vocabulary, Constitution, Specification, and Release — Evidenced by Two Independent Verification Passes Against `ocom.uno`

**Date observed:** 20 August 2026

**Description:** No document in this repository states the relationship between the four version identifiers a public reader of `ocom.uno` or this repository actually encounters — Core Vocabulary (`v0.1`), Constitution (`v1.0`), Specification (`v0.2`), and the sole GitHub Release (`v1.0.0`) — leaving it possible for a Release to be cut, named, and published before the Constitution it might be assumed to bundle actually existed. This is a `repository-scope` boundary (Controlled Boundary Vocabulary: *"the boundary is specific to how this specification's repository is organized, not to the OCOM model itself"*), not a Core-modeling one — no Object, Entity, Domain, or Relationship concept is implicated. Two independent Reference Cases surfaced this boundary.

| Field | Content |
|---|---|
| **Reference Case** | RC-008 — External Audit Comparison of `ocom.uno` Against the GitHub Repository |
| **Purpose** | Determine whether the publication artifacts on `ocom.uno` accurately and unambiguously reflect the canonical GitHub repository's current state — specifically version identifiers, publication content, and structural claims. |
| **Expressive Coverage** | Not applicable in Object/Entity/Domain/Relationship terms — this Reference Case concerns how this specification's own repository and publication artifacts are organized, not any OCOM-modeled concept. |
| **Boundary Conditions** | An eleven-point comparison of the live `ocom.uno` site against the `DenisHogberg/OCOM` GitHub repository found multiple discrepancies between the live site and the repository. |
| **Boundary Tags** | `repository-scope`. |
| **External Assurance** | Weak, and recorded honestly rather than concealed: this Reference Case is grounded in an external audit report provided by the Chief Architect; the report's own author, tooling, and preparation date are not established in this record. Three of the report's own eleven findings were self-flagged by the report itself as unconfirmed, and it explicitly requested independent re-verification — which RC-009 below provides. |
| **Architectural Observations** | This entry (`AO-008`). |
| **Core Impact** | None — this boundary is governance/publication-metadata-shaped, not Core-modeling-shaped; no Meta Object, Canonical Principle, Entity type, or Domain is implicated. |
| **Decision** | Escalated, together with `RC-009`, to an ADR Candidate — see `ADR-Candidates.md#cand-009`, filed as a `CAND-007` §5/§6 Freeze exception, not as a Core-extension proposal. |

| Field | Content |
|---|---|
| **Reference Case** | RC-009 — Independent Workflow Re-Verification of `ocom.uno` Against the Repository and the GitHub API |
| **Purpose** | Independently re-verify RC-008's findings using a distinct, technically direct method, per Repeatability Before Standardization — a single Reference Case does not, by itself, justify escalation. |
| **Expressive Coverage** | Not applicable in Object/Entity/Domain/Relationship terms, for the same reason as RC-008. |
| **Boundary Conditions** | An independent three-part verification pass, undertaken specifically to re-verify RC-008, read the local repository directly, the live `ocom.uno` site, and the GitHub API. It confirmed most of RC-008's findings and corrected RC-008's most significant claim: RC-008 stated no GitHub tag or release existed; direct GitHub API access found that a real tag/release (`v1.0.0`) does exist, cut before Constitution v1.0 was adopted — a materially different and more severe finding than RC-008 reached. |
| **Boundary Tags** | `repository-scope`. |
| **External Assurance** | Strong: drawn from direct, live technical access (GitHub API, live-site fetch, local repository read) at the time of execution (20 August 2026), independently reproducible by re-running the same queries against the same public sources. |
| **Architectural Observations** | This entry (`AO-008`). |
| **Core Impact** | None, for the same reason as RC-008. |
| **Decision** | Escalated, together with `RC-008`, to an ADR Candidate — see `ADR-Candidates.md#cand-009`, filed as a `CAND-007` §5/§6 Freeze exception, not as a Core-extension proposal. |

RC-008 and RC-009 reach the same boundary condition (undocumented version-identity relationships, most severely the Release-predates-Constitution gap) from two independent sources — an externally-provided audit of unestablished authorship, and an independently commissioned direct-access verification pass — satisfying Repeatability Before Standardization without requiring a hypothetical second case. Independence rests on method and result, not on an authorship claim RC-008 cannot support: RC-009 used a specifically-described, independently reproducible method, and reached a materially different, corrective conclusion rather than reproducing RC-008's findings — two reports of one investigation would be expected to agree, not to correct each other's central claim.

**Impact:** As things stand, a reader of `ocom.uno` or this repository cannot, from published material alone, determine the relationship between `v0.1` (Core Vocabulary), `v1.0` (Constitution), `v0.2` (Specification), and `v1.0.0` (the sole GitHub Release) — nor that the Release predates the Constitution by construction. This is a gap in this repository's own governance/publication documentation, not in any OCOM Core concept.

**Recommendation:** Per `CAND-007` §5/§6 (not the Core-extension pathway `EPIC-D`/Rule 4 describes, since Core Impact is None), escalate to an ADR Candidate proposing a documented version-identity model and publication manifest, filed as a Freeze exception. Full design attached as `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, and `Governance/Release-Workflow.md` (Status: Informative pending their own content review), for the Chief Architect's review via `ADR-Candidates.md#cand-009`. Nothing in `Meta/`, `Models/`, `Core/`, or `Domains/` is implicated by this Observation.

**Status:** Escalated, see `ADR-Candidates.md#cand-009`

**Architect Response:** *(recorded via the `CAND-009` Decision — see `ADR-Candidates.md#cand-009`)*

**Related:** `Governance/Publication-Model.md`, `Governance/Publication-Manifest.md`, `Governance/Release-Workflow.md`, `Standard Evolution Methodology.md` (Reference Case template, Repeatability Before Standardization, the `repository-scope` Controlled Boundary Vocabulary tag), `ADR-Candidates.md#cand-007` (Architecture Freeze — this is filed as a Freeze exception under its §5/§6), `ADR-Candidates.md#cand-009`

---

## AO-009

**Title:** Identity Scope Is Referenced but Not Formally Defined

**Date observed:** 4 September 2026

**Description:** `Meta/Identity.md` requires Identity to be unique and persistent, and the Identity Scope section describes scope-qualified uniqueness. An external adversarial review of the published site (4 September 2026) constructed the counterexample of two Objects carrying the same identifier value in two different scopes (for example, one in a CRM context and one in an ERP context). Under the current text, the effective identifier is the pair (scope, identifier), yet Scope itself is not defined as an Object, has no Identity of its own, and has no term record. The review framed this as an infinite-regress test: either Scope is an Object (introducing a further level of identity) or the fundamental model depends on an element that sits outside the model.

**Impact:** Two conforming implementations can disagree on whether identifier collisions across scopes are permitted, and on what identifies a scope. No specification text is currently wrong; the gap is that scope identity is unspecified.

**Recommendation:** Record only. If independently corroborated, a future Reference Case should propose either (1) defining scope as a governed attribute of Identity with its own uniqueness rules, or (2) explicitly stating that Identity uniqueness is always evaluated within a declared Registry, making Registry the scope carrier.

**Status:** Open; not escalated (single external source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Identity.md`, `Meta/Registry.md`

---

## AO-010

**Title:** Identity Merge and Split Have No Normative Semantics

**Date observed:** 4 September 2026

**Description:** `Meta/Identity.md` requires that Identity remain stable throughout the Object's lifetime and never be reused. `Examples/Implementation-Case/Performance-Marketing-Operator.md` describes alias handling on evidence, with no automatic merging. The external adversarial review (4 September 2026) posed the merge scenario: two Objects are created for what is later evidenced to be one real-world subject. Deleting one violates persistence; re-pointing historical Relationships rewrites history; keeping both with a sameAs assertion yields two unique Identities for one subject, which strains the canonical-identity promise. The split scenario (one Object later evidenced to be two subjects) is symmetric and equally unspecified.

**Impact:** Conforming implementations will inevitably face merge/split in production and will resolve it in incompatible ways. The Implementation Case demonstrates a practice (evidence-gated aliasing) but no normative document defines it.

**Recommendation:** Record only. A future Reference Case drawn from a real merge incident should propose normative alias semantics for Identity (assertion, evidence requirement, effect on Relationships and history) without weakening the no-reuse rule.

**Status:** Open; not escalated (single external source; the Implementation Case provides supporting but not independent evidence)

**Architect Response:** *(pending)*

**Related:** `Meta/Identity.md`, `Meta/Relationship.md`, `Examples/Implementation-Case/Performance-Marketing-Operator.md`

---

## AO-011

**Title:** Policy Exceptions Have No Precedence Model

**Date observed:** 4 September 2026

**Description:** `Meta/Policy.md` lists Exceptions among Policy characteristics and allows Policies to be mandatory, recommended, or optional. The external adversarial review (4 September 2026) constructed a stack of one Policy and three Exceptions whose pairwise overrides are individually plausible but jointly cyclic, producing simultaneously valid ALLOW and DENY evaluations. The specification defines no precedence, ordering, or conflict-resolution rule between a Policy and its Exceptions, or between overlapping Policies applying to the same Object.

**Impact:** Two conforming implementations can evaluate the same governed records to opposite decisions. This is consistent with the specification's position that it describes the governed record rather than an evaluation engine, but that position is not stated in `Meta/Policy.md` itself, so a reader can reasonably expect deterministic evaluation.

**Recommendation:** Record only. Candidate remedies for a future Reference Case: (1) an explicit statement in `Meta/Policy.md` that evaluation order and conflict resolution are implementation responsibilities to be declared per model; or (2) a minimal normative precedence rule (for example, most specific scope wins; on remaining conflict, escalate to the accountable Owner rather than auto-resolve).

**Status:** Open; not escalated (single external source)

**Architect Response:** *(pending)*

**Related:** `Meta/Policy.md`, `Meta/Constraint.md`, `Meta/Ownership.md`

---

## AO-012

**Title:** Temporal Boundary Semantics Are Undefined

**Date observed:** 4 September 2026

**Description:** Several term records carry validity periods: Ownership has Effective and Expiration Dates, Policy has Effective and Expiration Dates, Relationship has a Validity Period. The external adversarial review (4 September 2026) posed three boundary cases: (1) two consecutive Ownership records meeting exactly at one timestamp (who owns the Object at that instant); (2) one Policy expiring and another taking effect at the same timestamp (which applies at that instant); (3) an Event recorded on one date but effective at an earlier date (whether and how far derived projections must be recomputed). Interval closure (inclusive or exclusive bounds) and retroactive-effect rules are not defined anywhere in `Meta/` or `Models/`.

**Impact:** Implementations will pick different closure conventions and different backdating policies, producing divergent histories from identical records.

**Recommendation:** Record only. A future Reference Case should propose a single closure convention (for example, half-open intervals: inclusive start, exclusive end) and a stated rule for effective-dated records, both as small additive clauses.

**Status:** Open; not escalated (single external source)

**Architect Response:** *(pending)*

**Related:** `Meta/Ownership.md`, `Meta/Policy.md`, `Meta/Relationship.md`, `Models/Event.md`

---

## AO-013

**Title:** Event Immutability Needs a Validity and Trust Distinction

**Date observed:** 4 September 2026

**Description:** `Models/Event.md` defines Events as immutable records of fact, and the Implementation Case demonstrates state computed from immutable Events with corrections recorded as new Events. The external adversarial review (4 September 2026) pressed the fraudulent-event case: a correction Event neutralizes an erroneous amount, but a fraudulent Event poses a sharper question, whether it belongs in canonical history at all. If it stays, history contains records that are true as occurrences but false as claims; if it is removed, history is no longer immutable. The review's formulation: the model currently has one notion of Event where four are latent (the event occurred; the event was valid; the event is trusted; the event is currently effective).

**Impact:** Without this distinction, "history is immutable" and "history is truthful" can be read as the same promise, and implementations will conflate occurrence with validity in incompatible ways.

**Recommendation:** Record only. A future Reference Case drawn from a real correction or fraud incident should propose whether validity/trust status belongs on the Event (as governed Metadata), in a separate assessment record, or out of scope with an explicit statement.

**Status:** Open; not escalated (single external source; the Implementation Case's correction pattern is supporting evidence)

**Architect Response:** *(pending)*

**Related:** `Models/Event.md`, `Meta/Metadata.md`, `Examples/Implementation-Case/Performance-Marketing-Operator.md`

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial log, 2 entries |
| 0.1 | 22 July 2026 | Added OBS-003 (Reference Case: Object Attribute Lifecycle Categories) |
| 0.1 | 25 July 2026 | Added AO-001 (Domain Definition Divergence) and AO-002 (Relationship Participant Inconsistency) |
| 0.1 | 27 July 2026 | Added AO-003 (Mutable Status in an Immutable Memory Model), surfaced during Constitution integration Stage 2 (Memory/Evidence migration) |
| 0.1 | 29 July 2026 | Added AO-004 (Reader Produces No Memory-Record-Shaped Output), surfaced by RC-005 (Vector, `reference/rc005/`) |
| 0.1 | 29 July 2026 | Added AO-005 (Attribute Data-Type Facet Has No Self-Describing Value Structure), evidenced by RC-006 (real operating-company meeting data) and RC-007 (OCOM's own Finance/Operations/BI Domain KPI content); escalated to `CAND-008` |
| 0.1 | 29 July 2026 | Added AO-006 (Observation vs. Interpretation vs. Value vs. Meaning), recorded per Chief Architect review of `CAND-008`; no Reference Case yet, not escalated — a precondition check on `CAND-008`'s eventual promotion |
| 0.1 | 29 July 2026 | Added AO-007 (Core Concepts Must Eliminate a Demonstrated Deficiency, Not Introduce a New Abstraction), recorded per Chief Architect observation on the Measurement→Value episode; one instance only, not escalated — evidence toward a possible future refinement of `Standard Evolution Methodology.md` |
| 0.1 | 20 August 2026 | Added AO-008 (Publication Version-Identity Has No Documented Relationship), evidenced by RC-008 (external audit, weak External Assurance, honestly recorded) and RC-009 (independent Workflow re-verification, strong External Assurance); Core Impact None — a `repository-scope`, not Core-modeling, boundary; escalated to `CAND-009` as a `CAND-007` §5/§6 Freeze exception, completing that candidate's Path A |
| 0.1 | 4 September 2026 | Added AO-009 through AO-013 (identity scope, identity merge/split, policy exception precedence, temporal boundary semantics, event validity/trust), evidenced by an external adversarial review of the published site; all recorded, none escalated, per Standard Evolution Methodology Rules 1 and 2 |

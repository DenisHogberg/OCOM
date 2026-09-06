<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Observations

[← Back](Architecture-Health.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# Architecture Observations

**Document ID:** GOV-OBSERVATIONS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 5 September 2026

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

## AO-014

**Title:** Conformance Scope Differs Between Chapters 2, 5, 6 and 8

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Specification/08 Conformance.md` (from `Language/Conformance.md`) states "Conformance applies to implementations, not to individual models", while `02 Design Principles.md` states "All models created using this specification shall conform to these principles" and `05 Object Model.md` and `06 Lifecycle Model.md` state conditions under which an Entity, Domain, Relationship, Event, State, Workflow or Lifecycle "conforms to this specification". Chapter 8 also widened its Purpose to "an implementation, model, or repository" while keeping the implementation-only Definition, and scopes Core Conformance to Chapters 4 to 6, leaving the Chapter 2 principles outside the tested range.

**Impact:** A reader cannot tell whether a model, a model element, or only an implementation is the subject of a conformance claim; two conforming implementations could disagree on whether a non-conforming model invalidates an implementation's claim.

**Recommendation:** Record only. An editorial note was added to Chapter 8 on 4 September 2026 recording the difference. A future Reference Case should propose one scoping rule: the implementation claims conformance, and the models it produces are required to satisfy Chapters 2, 5 and 6 as part of that claim.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Specification/02 Design Principles.md`, `Specification/05 Object Model.md`, `Specification/06 Lifecycle Model.md`, `Specification/08 Conformance.md`, `Language/Conformance.md`

---

## AO-015

**Title:** Ownership Modality Is Inconsistent Across Meta, Models and the Reading Path

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Core/Principles.md` Principle 3: "Ownership shall never be implicit"; `Meta/Object.md`: "Objects should have defined ownership appropriate to organizational governance"; `Meta/Ownership.md` Conformance: "assign Ownership to managed Objects where applicable" and Shared Ownership: "Objects may have multiple Owners"; `Models/Entity.md`: "Every Entity shall have one responsible owner"; `Specification/04 Meta Model.md` lists Ownership among the seven core characteristics but omits it from the chapter's Conformance sentence. The same obligation is therefore shall, should, "where applicable" and, for Entities, singular.

**Impact:** An Entity with two Owners is conformant under `Meta/Ownership.md` and non-conformant under `Models/Entity.md`; the Chapter 4 characteristic list and its own conformance sentence do not match.

**Recommendation:** Record only. If corroborated, a future Reference Case should state whether Ownership is mandatory for every managed Object or only for Entities, and align the Chapter 4 conformance sentence with its characteristic list.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2) Independently corroborated by an external logic audit of commit 37c986a (5 September 2026), per Standard Evolution Methodology Rule 2; still awaiting a Reference Case.

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Meta/Ownership.md`, `Models/Entity.md`, `Specification/04 Meta Model.md`, `Core/Principles.md`

---

## AO-016

**Title:** Identity Replacement Clause Conflicts With the No-Reuse Rule

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Identity.md` Identity Assignment: "Once assigned, Identity shall not be reused for another Object. Replacement of an Object shall result in a new Identity unless organizational policy specifies otherwise." The Conformance section requires implementations to "prevent Identity reuse" and the Design Principles require Identity to "be immutable". The "unless organizational policy specifies otherwise" clause permits a policy to carry an Identity onto a replacement Object, which the preceding sentence forbids absolutely. Distinct from AO-009 (scope) and AO-010 (merge/split).

**Impact:** Two implementations can both claim conformance while one recycles identifiers on replacement and the other never does.

**Recommendation:** Record only. If corroborated, a future Reference Case should clarify whether "replacement" means a new Object (new Identity, no exception) or physical replacement of the same operational Object (same Object, same Identity), and remove the policy exception or bound it explicitly.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Identity.md`, `Adoption/Worked Example - Library Lending.md`

---

## AO-017

**Title:** Relationship Arity, Direction and Cardinality Modality Diverge Between Meta and Models

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Relationship.md`: "semantic association between two or more Objects", core characteristics Source Object and Target Object (binary), Direction may be Directed, Bidirectional or Undirected, "Relationships may define cardinality". `Models/Relationship.md`: "Every Relationship shall define cardinality", Source Entity and Target Entity only. Three divergences: n-ary versus a mandatory source/target pair; Undirected relationships that must still name a Source and a Target; cardinality optional at the Meta tier and mandatory at the Models tier. The Chapter 5 editorial note records only the meaning-versus-behaviour tension; AO-002 records only the Object-versus-Entity participant gap.

**Impact:** Conforming implementations can disagree on whether an n-ary or undirected Relationship is representable and on whether cardinality is required.

**Recommendation:** Record only. If corroborated, a future Reference Case should state whether the Models tier may tighten the Meta tier (cardinality mandatory for Entity relationships) and how n-ary and undirected relationships are represented with a Source/Target pair.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Relationship.md`, `Models/Relationship.md`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, AO-002

---

## AO-018

**Title:** Metadata Categories Overlap the Concepts Metadata Is Said Not to Define

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Metadata.md` Definition: "Metadata supplements an Object but does not define its identity or operational state"; the same record's Core Characteristics list "identity attributes" and "operational attributes", and its examples include Owner, Status, Classification and Policy References. Status, Owner and Classification therefore have candidate homes in Entity State, the Ownership record, the Classification record and Metadata. This is the Core-tier analogue of AO-003 (Memory Record Status).

**Impact:** Implementations can store the same fact in different Core constructs and disagree on which one is authoritative.

**Recommendation:** Record only. If corroborated, a future Reference Case should state that Metadata may carry non-authoritative copies (caches) of facts whose authoritative home is another record, or narrow the category list.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2) Independently corroborated by an external logic audit of commit 37c986a (5 September 2026), per Standard Evolution Methodology Rule 2; still awaiting a Reference Case.

**Architect Response:** *(pending)*

**Related:** `Meta/Metadata.md`, `Meta/Classification.md`, `Meta/Ownership.md`, AO-003

---

## AO-019

**Title:** Organization Is Restricted to Relationships While Contract and Reference Admit It

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Organization.md`: Organizations "participate in the operational model only through governed Relationships" and "connect to other Objects exclusively through ordinary, governed Relationships"; the same record's Business Meaning says interactions are "modeled using existing Relationship and Contract mechanisms". `Meta/Contract.md` lists Organizations among Contract participants, and `Meta/Object.md` allows any Object to hold References. Read literally, an Organization may not be a Contract participant and may not hold a Reference. Related to CAND-004 (Open).

**Impact:** Implementations can disagree on whether an Organization may appear as a Contract participant or as the source of a Reference.

**Recommendation:** Record only. If corroborated, a future Reference Case should restate the "exclusively through Relationships" clause as excluding hierarchy and containment, not Contracts or References, or resolve it under CAND-004.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Organization.md`, `Meta/Contract.md`, `Meta/Reference.md`, `ADR-Candidates.md#cand-004`

---

## AO-020

**Title:** Contract, Capability and Policy Participant Lists Name Parties the Core Does Not Define

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Contract.md` defines a Contract as "a governed agreement between two or more Objects" and then lists participants "Objects, Organizations, Departments, Teams, Employees, AI Agents, Tools, External Systems"; `Meta/Capability.md` and `Meta/Policy.md` carry similar lists (Business Units, Business Processes, Workflows, Memory, Knowledge, Domains). Only Organization is reconciled as a specialization of Object; Departments, Teams, Employees, Business Units, Business Processes and External Systems are defined nowhere in the Core, and `Specification/03 Core Concepts.md` states that AI-specific concepts are extensions, not Core.

**Impact:** A reader cannot tell whether a Department or an AI Agent may be a Contract party as such, or only once modelled as an Object.

**Recommendation:** Record only. If corroborated, a future Reference Case should add one sentence to the affected records: every participant, provider or scope entry is modelled as an Object (or a specialization) before it can take part.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Contract.md`, `Meta/Capability.md`, `Meta/Policy.md`, `Specification/03 Core Concepts.md`

---

## AO-021

**Title:** Evidence Is a Published Pillar Without a Core, Models or Language Definition

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). The site's tagline, `/why`, `llms.txt`, `Specification/01 Introduction.md` ("identity, ownership, lifecycle, and evidence") and every comparison capability matrix present Evidence as a defining characteristic of OCOM. `Core/Constitution.md` §3 (Evidence Before Belief) is adopted canon and `Models/Event.md` supplies the mechanism, but the word does not occur in `Meta/`, `Models/` or `Language/`; `Memory/Evidence Overlay.md` reserves the definition for a future version, and `Documentation-Debt.md` FW-001 records the definition as intentionally removed during the v0.1 release candidate review. The Worked Example and Shape Check disclose the gap.

**Impact:** A critical reader can quote a headline pillar that has no normative definition at the tiers the site publishes; comparisons score Evidence as an OCOM capability against that gap.

**Recommendation:** Record only. Track together with FW-001. If corroborated, a future Reference Case should either promote a minimal Evidence definition (per FW-001) or restate the public tagline in terms the Core defines (Identity, Ownership, Lifecycle, Governance) with Evidence named as a Constitution principle.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Constitution.md`, `Memory/Evidence Overlay.md`, `Documentation-Debt.md#FW-001`, `Specification/01 Introduction.md`

---

## AO-022

**Title:** Object Obligations Use Shall, Should and May for the Same Characteristic; "Managed Object" Is Undefined

**Date observed:** 4 September 2026

**Description:** Surfaced by an external pre-launch red-team review of the published site (4 September 2026). `Meta/Object.md` Design Principles: "Every Object shall: possess an identity, contain metadata, support relationships, participate in governance, support lifecycle management"; the same record: "Objects may contain descriptive metadata" and "Every managed Object should participate in a Lifecycle"; `Meta/Metadata.md`: "All managed Objects may possess Metadata"; `Specification/04 Meta Model.md` Conformance: "every managed Object ... supports metadata". The qualifier "managed Object", used in every Meta conformance clause, is defined nowhere, and no document states whether unmanaged Objects exist. Related: `Models/Entity.md` requires every Entity to "participate in relationships" while the minimum conforming Entity lists no Relationship.

**Impact:** RFC 2119 readers will not accept shall, should and may for the same clause; implementations can disagree on whether an Object without Metadata or without a Lifecycle is conformant.

**Recommendation:** Record only. If corroborated, a future Reference Case should define "managed Object" once (an Object under governance in a Registry) and settle each characteristic's modality in one place.

**Status:** Open; not escalated (single review source; awaiting independent corroboration per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Meta/Metadata.md`, `Meta/Ownership.md`, `Models/Entity.md`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, `Adoption/Worked Example - Library Lending.md`, `AO-018`

---

## AO-023

**Title:** Core Definitions Close on Each Other Through the Undefined Word "Governable"

**Date observed:** 5 September 2026

**Description:** Surfaced independently by two external reviews of the published site (5 September 2026). `Meta/Object.md` defines an Object as "an identifiable and governable element that exists within the operational model"; `Meta/Identity.md` defines Identity as "the persistent and unique representation of an Object". Neither "governable" nor "operational model" is defined at the Core, Models or Language tiers, and Governance is not a Core Vocabulary term and no OCOM document defines it as a per-Object characteristic; six term records (Identity, Metadata, Reference, Classification, Constraint, Policy) reference it, and `Adoption/Worked Example - Library Lending.md` (whose publication `CAND-010` authorizes) discloses the gap. No ADR Candidate records the gap itself. A third usage, Governance as an organizational framework for a class of Objects, appears in `AI/Evaluation/Evaluation Governance.md`, `AI/Prompts/Prompt Governance.md`, `AI/Tools/Tool Governance.md`; it is the per-Object sense applied to a class and is not covered by the two-sense note in `Specification/04 Meta Model.md`. The published relationship graph shows 44 directed cycles among the 13 terms (35 mutual pairs); cycles are expected where terms define each other, but they make the circularity visible to any reader who checks the definitions.

**Impact:** A reviewer applying the published review question on definitions can show that the two foundational definitions close on each other through a word the specification does not define; conformance clauses that require an Object to "support governance" (`Specification/04 Meta Model.md`) inherit the same gap.

**Recommendation:** Record only. If corroborated, a future Reference Case should either define "governable" once at the Core tier, in terms of the Core terms Ownership, Policy and Constraint, or restate the Object definition without it. Resolution requires a Reference Case; no ADR Candidate exists for it yet.

**Status:** Open; not escalated (external review sources; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Meta/Identity.md`, `Adoption/Worked Example - Library Lending.md`, `Specification/04 Meta Model.md`, `Specification/07 Governance.md`, `AI/Evaluation/Evaluation Governance.md`, `AI/Prompts/Prompt Governance.md`, `AI/Tools/Tool Governance.md`, `AO-021`

---

## AO-024

**Title:** Constitution's Architectural Principles Use Implementation Vocabulary Undefined at Any Tier and Carry No Marker Distinguishing Them From the Canonical Principles

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the canonical repository at commit 37c986a (5 September 2026). `Core/Constitution.md:25` states the principles "apply regardless of programming language, storage engine, deployment model, AI model, or business domain". The same document's Architectural Principles, `Core/Constitution.md:50-54`, read: "New sources integrate through Adapters and Normalizers.", "Identity Resolution thresholds are deployment configuration.", "Source trust is deployment configuration.", "Concept namespaces are deployment scoped.", "One deployment currently represents one organization."; Canonical Principle 9 (`:39`) adds "Domain knowledge belongs only to configuration, data and adapters." None of Adapter, Normalizer, Source trust, Concept namespace, deployment or threshold is defined in `Core/`, `Meta/`, `Models/`, `Language/`, `Memory/`, `AI/`, `Reference Architecture/` or `Specification/`. `Meta/Identity.md:127-136` defines Identity Resolution with no threshold concept; `Meta/Object.md:232-238` states the Object specification does not prescribe "deployment architectures"; `Core/Manifest.md:119-127` states the specification does not define software architecture, databases, APIs or implementation technologies. The only other occurrences of Adapter and Normalizer are in `AO-004` (`:175`), naming an implementation's `FilesystemDocumentationAdapter` and `FilesystemDocumentationNormalizer` classes as code facts. `Governance/ADR-Candidates.md:410` (CAND-006) records that the Architectural Principles "are explicitly *not* frozen the same way the Canonical Principles are" and "record the current architectural direction", but `Core/Constitution.md` itself, a "Verbatim transcription of the Decision text" (`:74`), carries no such marker, and its Meta-Principle (`:66`, "the Constitution prevails") does not say whether the Architectural Principles are part of what prevails. `Architecture-Release-Review-v1.0.md:57` closed the terminology check with "Terms used but not fully defined anywhere: two, both already tracked" (World Model, Autonomy level) and "No third was found beyond these in this pass."; Adapter, Normalizer and the other four terms were not caught by that pass, nor was the Memory Entry / Memory Record naming split (Constitution paragraph 4 against `Memory/Memory Record.md`, now GAP-004).

**Impact:** A reader of Core-00 alone cannot tell that lines 50-54 are architectural direction rather than model rules, and can cite them against Principle 6 (`Core/Principles.md:77`) and `Core/Manifest.md:119-127`; substantively the section defines no technology, so Principle 6 is not violated, but the gap of status and vocabulary is real. Canonical Principle 9 names a location for domain knowledge ("adapters") that is undefined, so an implementer cannot tell whether Adapter and Normalizer are Conformance concepts or a description of one implementation's ingestion architecture. The Release Review's closure statement is falsified, so Part 3 cannot be cited as evidence that Constitution terminology is closed.

**Recommendation:** Record only. If corroborated, a future Reference Case drawn from an independent implementation's ingestion layer should choose between (a) moving the Architectural Principles out of Core-00 into an Architecture document that Core-00 references, and (b) keeping them in Core-00 with the CAND-006 status marker and an explicit statement that their terms are implementation vocabulary outside the model, defining Adapter and Normalizer once at whichever tier holds source integration. Either path is a Constitution change under CAND-006's governance implication and CAND-007 §4. Fold Adapter, Normalizer, Source trust, Concept namespace, deployment and threshold into `EPIC-D`'s terminology-closure Definition of Done alongside Autonomy level and Memory Entry.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Constitution.md` (lines 25, 39, 50-54, 66, 74), `Core/Manifest.md` (Scope), `Core/Principles.md` (Principle 6), `Meta/Identity.md`, `Meta/Object.md`, `Architecture-Release-Review-v1.0.md` Part 3, `Master-Architecture-Backlog.md` EPIC-D, `ADR-Candidates.md#cand-004`, `ADR-Candidates.md#cand-006`, `ADR-Candidates.md#cand-007`, AO-004, AO-021, AO-023, `Constitution-Step0-Summary.md` Decision 1, GAP-004

---

## AO-025

**Title:** Decision Registers Carry Binding Decisions Under a Status That Declares Their Content Non-Normative

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the canonical repository (5 September 2026). `Governance/ADR-Candidates.md:13` and `Governance/Architecture-Observations.md:13` both read "**Status:** Informative". `Governance/Documentation-Standards.md:49` defines Informative as "non-normative. Explanatory, illustrative, or analytical material that imposes no requirement of its own. Used for `Examples/`, `Reference Architecture/`, and every `Governance/` analysis document", and `:48` assigns Draft to "`Governance/` (process documents)". Yet `ADR-Candidates.md:491` states "Sections 3, 4, and 7 are immediately binding on how the CDKO evaluates any future request", and `Core/Constitution.md:19` derives the Constitution's authority from that register ("**Adopted via:** `Governance/ADR-Candidates.md#cand-006`"). The taxonomy has been applied unevenly inside `Governance/`: `Publication-Model.md:113` records "Status changed Informative → Draft (this is a `Governance/` process document, not an analysis document, per `Documentation-Standards.md`'s Status Taxonomy)", and `Standard Evolution Methodology.md`, `Publication-Manifest.md` and `Release-Workflow.md` are Draft, while `ADR-Candidates.md`, `Architecture-Observations.md`, `Constitution-Step0-Summary.md` (which carries Decisions marked "Decided", `:39`), `Master-Architecture-Backlog.md` and `Governance-Manifest.md` (whose §9, `:65`, states "Every version of the specification shall be reproducible.") remain Informative. No document states where the binding force of a Decision resides: in the carrying register, in the Decision text, or in the Chief Architect role (`Governance-Manifest.md:75`). The four-value taxonomy has no value for a register whose individual entries are normative. `CAND-009` revision item (iv) (`ADR-Candidates.md:536`) recognises that a Status change alters enforceability, for `Entities/Overview.md` only.

**Impact:** A reader applying the Status Taxonomy literally concludes that the Constitution was adopted through, and the Architecture Freeze is enforced through, documents that by their own Status impose no requirement. The Informative/Draft split inside `Governance/` is a per-document judgment, not a rule, and `PROJECT_STATUS.md:70-71` publishes that split as settled.

**Recommendation:** Record only. If corroborated, a future Reference Case should either add one sentence to the Status Taxonomy locating the binding force of a Decision in the Chief Architect's recorded Decision text rather than in the Status of the register that carries it, or re-classify the decision registers as Draft under the existing "process documents" clause, following the `Publication-Model.md:113` precedent and the scope-authorization discipline `CAND-009` applied to `Entities/Overview.md`.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Governance/Documentation-Standards.md` (Status Taxonomy), `Governance/ADR-Candidates.md` (`CAND-006`, `CAND-007`, `CAND-009` item (iv)), `Core/Constitution.md`, `Governance/Governance-Manifest.md`, `Governance/Constitution-Step0-Summary.md`, `Governance/Publication-Model.md`, `PROJECT_STATUS.md` ("What Is Normative vs. Informative")

---

## AO-026

**Title:** Constitution v1.0 Was Edited Under the Architecture Freeze Without a Version Change or a Governance Record

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the canonical repository (5 September 2026). Commit `e0b54ed` (21 August 2026, "semantic: align OCOM public identity") added the sentence "OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations." to the Purpose section of `Core/Constitution.md` (`:25`). The document still reads "**Version:** 1.0" (`:15`); the only trace is the revision row at `:75`: "| 1.0 | 21 August 2026 | Added one identity sentence to Purpose ... Semantic positioning only - no Canonical Principle added, removed, or reworded; no constitutional meaning changed. |" (the "Last Updated: 27 July 2026" field at `:17` was stale and is corrected separately). Three rules in force at that date read against the edit: `CAND-007` §4 (`ADR-Candidates.md:464`), "no new Canonical Principle or Constitution amendment beyond the §9/§11 transcription in Section 3 above"; `Publication-Model.md:35`, Constitution changes via "RFC-like amendment only ... never an editorial edit"; `Core/Versioning.md:57`, Patch version "Incremented when documentation, examples, or editorial corrections are introduced." `Governance-Manifest.md:65` states "Every version of the specification shall be reproducible." No entry in `ADR-Candidates.md`, `Architecture-Observations.md` or `Documentation-Debt.md` records the edit. The label "Constitution v1.0" now denotes two different texts (27 July and 21 August 2026); the file set remains reproducible by commit, which `Publication-Model.md:47` names as the pinning mechanism, but not by version label. `CAND-006`'s amendment rule (`ADR-Candidates.md:408`) covers Canonical Principles only, so whether a Purpose sentence is an "amendment" is undefined; `CAND-007` §4 and `Publication-Model.md:35` use the broader word. `Publication-Manifest.md:36` already records the same no-bump pattern for `Meta/Organization.md`.

**Impact:** The apex document's version label is not a reliable citation key, and a reviewer with repository access can show in one command that an editorial commit crossed the Freeze's own "no Constitution amendment" rule with no Decision behind it. Whether editorial, non-Principle text in the Constitution is amendable at all, and at which version increment, is not decided anywhere.

**Recommendation:** Record only. If corroborated, a future Reference Case should decide whether the 21 August sentence is ratified retroactively by a Chief Architect Decision, with the Version raised to 1.0.1 per `Core/Versioning.md`, or reverted, and whether the Constitution track in `Publication-Model.md` admits a patch-level editorial class for non-Principle text.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Constitution.md`, `Core/Versioning.md`, `Governance/Publication-Model.md` (Versioning Model table), `Governance/Publication-Manifest.md`, `Governance/Governance-Manifest.md` §9, `ADR-Candidates.md#cand-006`, `ADR-Candidates.md#cand-007` §4, `Documentation-Debt.md#FW-007`, AO-008

---

## AO-027

**Title:** Object Obligations Applied to Lifecycle and Registry Themselves Have No Terminating Rule

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the published site and repository (5 September 2026). `Specification/03 Core Concepts.md:19` makes Lifecycle a specialization of Object and `:51` adds Registry; `Meta/Object.md:202` and `:210` list Lifecycle and Registry among Examples of Objects. `Meta/Object.md:51-57`: "Every Object shall: ... support lifecycle management"; `Meta/Object.md:128`: "Every managed Object should participate in a Lifecycle appropriate to its purpose." The only normative Lifecycle model is Entity-scoped: `Models/Lifecycle.md:31` "define the operational existence of an Entity", `:41` "belong to exactly one Entity". Read together, a Lifecycle, being an Object, must support lifecycle management, but the Lifecycle that a Lifecycle (or a Policy, Registry or Contract) participates in is defined nowhere, and no clause states whether the chain terminates. `Models/Lifecycle.md:101-105` ("Changes to a Lifecycle definition shall preserve consistency ... Breaking changes should be versioned") and `Models/Relationship.md:108` ("A Relationship may have its own lifecycle independent of the participating Entities") show that non-Entity Objects are intended to have lifecycles without naming the model that governs them. The same question exists for Registry: `Meta/Registry.md:33` defines a Registry as "a managed collection of identifiable Objects"; a Registry is an Object; no text states whether a Registry is itself registered, or in which Registry. The audit's stronger conclusions (an infinite regress; a Registry must contain itself) do not follow: no clause requires a distinct Lifecycle per Lifecycle, and no clause requires any Registry to hold every Object (`Meta/Registry.md:62-68` scopes each Registry by "Registry Scope" and "Registered Object Types"; `:90` "Organizations shall define the appropriate scope for each Registry"). `Architecture-Release-Review-v1.0.md:61` checked two self-references and found them ordinary; this pair was not among them.

**Impact:** A reader can show that the Core's universal obligations, applied to the Core's own constructs, have no stated stopping point; implementations can disagree on whether a Lifecycle, Policy or Registry object must carry a Lifecycle and what form it takes. The stronger charge is answerable, but the answer is not in the text.

**Recommendation:** Record only. If corroborated, a future Reference Case should state one terminating rule: definitional Objects (Lifecycle, Policy, Registry, Contract) participate in a definition-level lifecycle (versioning, as `Models/Lifecycle.md` Lifecycle Evolution already implies) that applies to itself, and a Registry may register Registries, itself included. Resolve together with AO-022: defining "managed Object" as an Object in a Registry would otherwise leave the root Registry unmanaged.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Meta/Registry.md`, `Models/Lifecycle.md`, `Models/Relationship.md`, `Specification/03 Core Concepts.md`, `Governance/Architecture-Release-Review-v1.0.md`, AO-009, AO-022, AO-023, AO-028

---

## AO-028

**Title:** Lifecycle Is Bound to Exactly One Entity at the Models Tier and Reusable by Many at the Lifecycles Tier

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the published site and repository (5 September 2026). `Models/Lifecycle.md:39-41`: "Every Lifecycle shall: - belong to exactly one Entity;" and `:31`: "the complete set of States and permitted State Transitions that define the operational existence of an Entity." `Lifecycles/Lifecycles.md:33`: "A Lifecycle is a reusable operational model describing the allowed States and valid State Transitions of an Entity."; `:46`: "shall be reusable by multiple Entities;"; `:53-55`: "An Entity references a Lifecycle rather than redefining its own lifecycle. Multiple Entities may share the same Lifecycle." Both documents carry Status Draft, which `Governance/Documentation-Standards.md:48` defines as "normative, currently in force". `Specification/06 Lifecycle Model.md:17` (live at `ocom.uno/specification.md:445`) compiles the two sources into one paragraph, keeping "Every Entity shall have exactly one Lifecycle" and "A Lifecycle is a reusable operational model" while omitting the "belong to exactly one Entity" characteristic; the reading path is internally consistent (many Entities to one Lifecycle) but silently selects one side of a shall-level divergence between its sources, and the source footnote at `:45` records no such choice. `Specification/06:13` also classes `docs/Lifecycles/` as "non-normative" Reference Material while `Documentation-Standards.md:48` lists `Lifecycles/` among Draft-normative directories, so the tier of the reuse rule is itself ambiguous. The underlying cause is that no document distinguishes a Lifecycle definition (a reusable type) from the Lifecycle an Entity follows (an instance): `Models/Lifecycle.md:97` reads at instance level, `Lifecycles/Lifecycles.md:53` at definition level, and `Domains/Operations/Operations_Lifecycles.md:214` ("Each Operational Entity owns its own Lifecycle") follows the instance reading.

**Impact:** An implementation that models one shared Lifecycle referenced by many Entities conforms to `Lifecycles/Lifecycles.md` and violates `Models/Lifecycle.md:41`; one that copies a Lifecycle per Entity does the reverse. A reviewer can quote the two shall clauses side by side, and can show that the compiled chapter resolved the divergence without saying so.

**Recommendation:** Record only. Add an editorial note to Chapter 6 recording the divergence, as was done for Chapter 8 under AO-014: "Editorial note (5 September 2026): the source documents diverge on Lifecycle cardinality. `Models/Lifecycle.md` requires every Lifecycle to 'belong to exactly one Entity'; `Lifecycles/Lifecycles.md` requires every Lifecycle to 'be reusable by multiple Entities'. This chapter states the Entity-side rule (every Entity shall have exactly one Lifecycle) and the reuse sentence; it does not resolve the divergence, which is recorded as AO-028. No requirement changed." If corroborated, a future Reference Case should state whether "Lifecycle" names the reusable definition or the per-Entity progression, restate `Models/Lifecycle.md:41` accordingly, and settle whether `Lifecycles/Lifecycles.md` is normative or Reference Material.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Models/Lifecycle.md`, `Models/State.md`, `Lifecycles/Lifecycles.md`, `Specification/06 Lifecycle Model.md`, `Governance/Documentation-Standards.md`, `Core/Terminology.md`, `Domains/Operations/Operations_Lifecycles.md`, AO-014, AO-022, AO-027

---

## AO-029

**Title:** Entity Names Four of Object's Seven Core Characteristics as Shared; the Minimal Entity Omits Metadata and Classification Although Specializations Shall Preserve Core Characteristics

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the published site (5 September 2026). `Meta/Object.md:65-73` lists seven core characteristics (Identity, Metadata, Classification, Relationships, Lifecycle, Ownership, Governance) and `Meta/Object.md:224` states "Specifications may extend Object but shall preserve its core characteristics" (restated in `Specification/04 Meta Model.md:23`). `Models/Entity.md:171` declares "An Entity is a specialization of Object as defined in the Meta specification.", and `:173` states that an Entity "shares the Identity, Ownership, Relationship, and Lifecycle principles defined for Object", naming four of the seven and omitting Metadata, Classification and Governance. The Characteristics list (`Models/Entity.md:41-51`) does require an Entity to "participate in relationships" and "be governed by the rules of this specification" but never mentions Metadata or Classification, and the Minimal Entity (`:156-164`: "Identifier, Name, Domain, Owner, Attributes, State, Lifecycle") contains neither. `Specification/03 Core Concepts.md:23` summarises Entity with six properties and none of the four; Chapter 3 is a self-declared at-a-glance orientation (`:13`), so the audit's chapter-level count is not itself a defect. Read against the Core Characteristics list the primary specialization is narrower than its base; read against `Meta/Object.md:98` ("Objects may contain descriptive metadata") and `:146` ("Objects may be classified") it is not. The Object-side modality split is AO-022; the Entity-side inheritance gap is recorded here.

**Impact:** A reviewer applying the published review questions can show that the specification's own preservation rule for specializations is not satisfied by its primary specialization as written, or is satisfiable only by reading Metadata and Classification as optional, which the Core Characteristics list does not say. Implementations can disagree on whether a conforming Entity must carry Metadata or Classification.

**Recommendation:** Record only. If corroborated, a future Reference Case should either restate `Models/Entity.md` Relationship to Other Specifications to name all seven characteristics and state which are inherited unchanged, or state once, at the Object tier, which of the seven are mandatory for every specialization and which are optional, resolving together with AO-022. Chapter 3 needs no change. An editorial note in `Specification/05 Object Model.md`, in the form of the existing Relationship note, may flag the difference: "Editorial note. `Meta/Object.md` lists seven core characteristics that every specialization shall preserve; this chapter's Entity summary names four of them as shared and the minimum conforming Entity lists neither Metadata nor Classification. The difference is recorded (AO-029), not resolved, per editorial policy."

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Models/Entity.md`, `Specification/03 Core Concepts.md`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, AO-005, AO-015, AO-022

---

## AO-030

**Title:** Domain and Entity Each Require the Other to Exist; No Text States How the First Pair Is Formed

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the published site (5 September 2026). `Models/Domain.md:31` defines a Domain as "an operational boundary responsible for governing one or more Entities"; `Models/Domain.md:45` requires every Domain to "govern one or more Entities" and `:121` forbids a Domain to "govern undefined Entities". `Models/Entity.md:45` requires every Entity to "belong to exactly one primary Domain", `:127` restates it ("Every Entity belongs to one primary operational Domain."), and the Minimal Entity (`:156-164`) lists Domain as a mandatory element. `Specification/03 Core Concepts.md:27` and `Specification/05 Object Model.md:37` (live at `ocom.uno/specification.md:394`) publish the same pair. Mutual reference between peer definitions is ordinary in a vocabulary; what makes this pair an implementation question is that both sides carry a shall with a cardinality floor. Read as existence conditions, a Domain is non-conforming until it governs an Entity and an Entity is non-conforming until it belongs to a Domain, so the first pair cannot be created one at a time under either record's shall. AO-023 covers definitional cycles among the 13 Meta terms only; Entity and Domain are Models-tier.

**Impact:** Low for readers, since mutual reference between peer definitions is expected; real for implementers, who must decide whether an empty Domain or a Domain-less Entity during creation is a conformance violation or a transient state, with no guidance. Registries and shape-checkers that validate on every write will reject the first Domain or the first Entity of every model.

**Recommendation:** Record only. If corroborated, a future Reference Case drawn from a real bootstrap of a model (first Domain, first Entity) should state either that "govern one or more Entities" is a steady-state expectation rather than a creation-time requirement, or that a Domain and its first Entity are established together, and place that sentence in `Models/Domain.md`.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Models/Domain.md`, `Models/Entity.md`, `Specification/03 Core Concepts.md`, `Specification/05 Object Model.md`, AO-001, AO-023

---

## AO-031

**Title:** Identifier Reuse After Retirement Is Governance-Permitted in Language but Absolutely Forbidden in Meta

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the repository (5 September 2026). `Meta/Identity.md` Identity Assignment: "Once assigned, Identity shall not be reused for another Object." (`:106`); Conformance: "prevent Identity reuse" (`:177`). `Language/Identifier Syntax.md` Identifier Lifecycle: "Identifiers shall remain associated with the same Identity throughout their effective lifetime." (`:132`) and "If an element is retired, its identifier should not be reassigned unless organizational governance explicitly permits reuse." (`:134`). `Identifier Syntax.md:35` defines an Identifier as "the syntactic representation of an Identity within an OCOM model", and `:39` allows one Identity to have several identifiers, so the two records are not literally about the same construct; but a reassigned identifier is, to every consumer of a serialized model, indistinguishable from a reused Identity, and the Language record turns Meta's unconditional shall-not into a should-not with a governance escape hatch. Under `Core/Manifest.md:178` lowercase shall/should carry RFC 2119 weight, so this is a modality downgrade across tiers, not a stylistic variance. Distinct from AO-016 (the replacement-policy exception inside `Meta/Identity.md` itself), AO-009 (scope) and AO-010 (merge/split); no register entry mentions `Language/Identifier Syntax.md`.

**Impact:** An implementation that recycles retired identifiers under a documented governance policy is conformant to `Language/Identifier Syntax.md` and non-conformant to `Meta/Identity.md` Conformance; two implementations exchanging serialized models can disagree on whether an identifier value denotes one Object or two across time.

**Recommendation:** Record only. If corroborated, a future Reference Case should state whether identifier reuse after retirement is ever permitted, and if so, define what distinguishes identifier reuse from Identity reuse (for example, a mandatory Version or Scope component that changes on reassignment); it should also settle whether Language may weaken a Meta obligation at all.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Identity.md`, `Language/Identifier Syntax.md`, `Core/Manifest.md` (Normative Language), AO-009, AO-010, AO-016

---

## AO-032

**Title:** Per-Document Conformance Sections Have No Stated Relationship to the Core Conformance Level

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the published site (5 September 2026). Sixty-one documents open a Conformance section with "A compliant implementation shall" (`Meta/Object.md:244-246`: "# Conformance / A compliant implementation shall ensure that every managed Object:"; 13 in `Meta/`, 34 in `AI/`, 6 in `Memory/`, 8 in `Language/`), 15 more with "A conforming implementation shall", and 70 `Domains/` documents with "A conforming <Domain> implementation shall". The only global statements are `Language/Conformance.md:77-85` ("A conforming implementation shall: implement the required language constructs; preserve language semantics; ... Mandatory requirements are normative.") and `Specification/08 Conformance.md:40` ("Core Conformance ... supports all mandatory requirements defined in Chapters 4–6"). No document states whether the per-document sections are the constituent Mandatory Requirements of Core Conformance, or which of them count: `Specification/03 Core Concepts.md:64` calls AI-specific concepts "extensions, not prerequisites", yet `AI/` holds 34 of the 61 blocks; `Memory/` and `Domains/` blocks fall outside Chapters 4-6 entirely. Chapter 8's editorial note (`:19`) addresses the model-versus-implementation question (AO-014) and its Note on scope (`:44`) addresses profile mechanics (CAND-002); neither addresses aggregation. `Core/Manifest.md:184` ("Conformance to this specification requires compliance with the normative documents that form part of this specification") implies all Draft documents bind, which contradicts the Chapters 4-6 limit in Chapter 8. `Master-Architecture-Backlog.md:133` already names every `# Conformance` section as a consumer of criteria EPIC-E has yet to define.

**Impact:** An assessor applying Chapter 8 (the clause the Evidence Register promises to check implementations against) cannot determine which of the 146 per-document Conformance sections constitute Core Conformance; two assessors could reach opposite verdicts on an implementation that satisfies every `Meta/` and `Models/` requirement but none in `AI/`, `Memory/` or `Domains/`.

**Recommendation:** Record only. If corroborated, a future Reference Case should propose one aggregation rule, for example: Core Conformance is satisfied by the Conformance sections of the documents compiled into Chapters 4 to 6 (`Meta/`, `Models/`); the Conformance sections of `Memory/`, `AI/`, `Domains/` and `Entities/` bind Extended or Profile Conformance only; and `Core/Manifest.md`'s Conformance sentence is to be read subject to that rule. Any change belongs to EPIC-E.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Language/Conformance.md`, `Specification/08 Conformance.md`, `Specification/03 Core Concepts.md`, `Core/Manifest.md`, `Meta/Object.md`, `Domains/` (70 profile Conformance sections carry no domain-specific obligation), `Entities/`, `Master-Architecture-Backlog.md` EPIC-E, `ADR-Candidates.md#cand-002`, AO-014, FW-003, FW-004

---

## AO-033

**Title:** Owner Is Untyped and Its Admissible Kinds Differ Between Core Terminology and the Ownership Record, so Identity, Governance and Audit Do Not Reach the Owner

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the repository (5 September 2026). `Core/Terminology.md:69` defines Owner as "The role, domain, or organizational unit accountable for an entity." `Meta/Ownership.md:35` states "Ownership identifies the individual, team, organizational unit, or system responsible for governing an Object during all or part of its lifecycle."; the word "role" does not occur in that document, and `Specification/04 Meta Model.md:61` (the published wording, live at `ocom.uno/specification.md:342`) repeats the Ownership.md list. The two lists share only "organizational unit": Terminology admits a Domain (defined at `Core/Terminology.md:50` as "A logical boundary responsible for governing one or more entities") and a role, and scopes Owner to an entity; Ownership.md admits an individual, a team and a system, and scopes Owner to any managed Object. `Core/Terminology.md:24` states "All terms defined here are authoritative", so the repository carries two authoritative and non-overlapping answers. `Meta/Ownership.md:64-70` requires every Ownership assignment to define an "Owner" with no type constraint; `Meta/Identity.md:33` defines Identity only for Objects ("the persistent and unique representation of an Object"), and `Meta/Ownership.md:195` ("Audit records shall remain immutable.") governs the assignment record, not the party named in it. `Meta/Organization.md:33` makes Organization an Object, and `Entities/` defines Employee, Team and Department, but no Core text requires an Owner to be an Object or any specialization; `Models/Entity.md:67` requires "one responsible owner" without saying what may fill the slot. This is the Ownership-record analogue of AO-020, which records the same defect for Contract, Capability and Policy participants. Neither AO-015 (modality) nor GAP-002 (missing glossary entries) records which kinds of party may hold Ownership.

**Impact:** An implementation recording a Domain or a role as Owner conforms to Core-03 but has no counterpart in `Meta/Ownership.md`; one recording a system or an individual conforms to `Meta/Ownership.md` but not to Core-03. An Owner can be a free-text role or an external system with no Identity, no Lifecycle, no Governance and no audit trail, while Principle 3 ("Ownership shall never be implicit") and every accountability clause assume the accountable party is itself identifiable. Two implementations can disagree on whether "Owner: Finance" (a string) is conformant. Whether a Domain may be an Owner has consequences for AO-001. The published site is internally consistent because only the Ownership.md wording is published.

**Recommendation:** Record only. If corroborated, a future Reference Case should state once, at the Meta tier and together with AO-020, that the Owner of an Ownership assignment is an Object (or a named specialization such as Organization or an Entity), which kinds of party may hold Ownership and whether a Domain is among them, and align `Core/Terminology.md`'s Owner entry to that record; track together with `GAP-002`, since the glossary entry will be revised in the same pass.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Terminology.md`, `Meta/Ownership.md`, `Meta/Identity.md`, `Meta/Object.md`, `Meta/Organization.md`, `Core/Principles.md`, `Models/Entity.md`, `Specification/04 Meta Model.md`, `ADR-Candidates.md#cand-004`, AO-001, AO-015, AO-020, GAP-002

---

## AO-034

**Title:** Reference and Relationship Are Distinguished Only by an Undefined Semantic Test

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the repository (5 September 2026). `Meta/Reference.md:33`: "A Reference is a directed association from one Object to another."; `Meta/Relationship.md:33`: "A Relationship is a governed semantic association between Objects." Core Characteristics overlap almost completely: Reference (`:64-75`) requires Source Object, Target Object, Reference Direction and may add Reference Type, Reference Purpose, Validity Period, Status; Relationship (`:64-78`) requires Identifier, Source Object, Target Object, Relationship Type and may add Direction, Cardinality, Status, Validity Period, Constraints, Governance Rules. Both records allow an independent lifecycle (`Meta/Reference.md:133`: "References may have their own lifecycle independent of the referenced Objects."; `Meta/Relationship.md:130`: "Relationships may possess an independent lifecycle."). The stated discriminator is `Meta/Relationship.md:37`: "Unlike a Reference, a Relationship conveys business meaning", restated in `Specification/03 Core Concepts.md:31` ("a Reference is a pointer, a Relationship carries business meaning") and relied on by `CAND-004` (`ADR-Candidates.md:180`) as an existing two-weight mechanism. "Business meaning" is not defined, and `Meta/Relationship.md:89` lists "Association" as a Relationship Type, so a typed Reference and an Association Relationship carry the same fields. The audit's word "indistinguishable" overstates: Relationship requires an Identifier and a Type, Reference requires a Direction and has no Identifier. The Chapter 5 editorial note (`Specification/05 Object Model.md:42`) addresses only the Meta-versus-Models framing of Relationship; AO-017 addresses arity, direction and cardinality. Neither addresses the Reference boundary.

**Impact:** Two conforming implementations can model the same link as a Reference in one and as a Relationship in the other, with different mandatory fields and different governance expectations, while both claim conformance. Reviewers applying the published review questions can show the distinction is asserted, not testable.

**Recommendation:** Record only. If corroborated, a future Reference Case should either state a structural criterion (for example: a Reference has no Identifier of its own and no Relationship Type; anything with a Type is a Relationship) or make Reference a named Relationship Type, so that the distinction becomes checkable.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Reference.md`, `Meta/Relationship.md`, `Models/Relationship.md`, `Specification/03 Core Concepts.md`, `Specification/05 Object Model.md`, `ADR-Candidates.md#cand-004`, AO-002, AO-017, AO-019

---

## AO-035

**Title:** Overview Documents Restate Definitions in Different Words, Contravening Principle 7 for AI Agent, Event, Context, Prompt, Tool, Evaluation and Knowledge

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the repository (5 September 2026). `Core/Principles.md:85`: "Each operational concept shall have a single authoritative definition within the model."; `Language/Vocabulary.md:35`: each term "shall have a single unambiguous meaning within the specification". Counted definitional sentences: AI Agent 5 (`AI/Overview.md:25` "an autonomous operational component ..." and `:33` "a software entity that performs business tasks ...", `AI/Agents/Overview.md:33` "an operational software component ...", `AI/Agents/Agent.md:31` "an autonomous operational entity ...", `Entities/AI-Agent/AI Agent.md:31` "a business Entity representing an artificial actor ..."); Event 3 (`Models/Event.md:31` "an immutable record describing something that has occurred"; `Entities/Event/Event.md:31` "a business Entity representing the occurrence of a business action"; `Domains/Common/Domain Events.md:31`); Context 3 (`AI/Context/Context.md:31` "a dynamically assembled collection of information relevant to a specific execution" plus the identical pair `AI/Context/Overview.md:33` and `AI/Agents/Context.md:33` already recorded as OBS-001 / CAND-001); Prompt 3 (`AI/Prompts/Overview.md:31` and `:33`, `AI/Prompts/Prompt.md:31`; the audit undercounts as 2); Tool, Evaluation and Knowledge 2 each (`AI/Tools/Overview.md:31` vs `AI/Tools/Tool.md:31`, `AI/Evaluation/Overview.md:31` vs `AI/Evaluation/Evaluation.md:31`, `AI/Knowledge/Overview.md:31` vs `AI/Knowledge/Knowledge.md:31`). The pattern is structural: every `AI/` section has an Overview.md and a concept file that each carry a "# Definition" heading. `PROJECT_STATUS.md:39` lists `AI/` as released v0.1 content with Status Draft, so these are normative texts, not commentary. Only the verbatim Context copy is recorded.

**Impact:** A reader cannot tell which sentence is authoritative; AI Agent is simultaneously a component, an entity and an Entity (a specialization of Object with a required Owner, State and Lifecycle), and Event is both an immutable record and a business Entity, which are different Object specializations under `Specification/04 Meta Model.md:23`. The specification's own Principle 7 is violated in its released text, which a launch-day reviewer will quote.

**Recommendation:** Record only. If corroborated, a future Reference Case should fix one authoritative Definition per term (the concept file), demote Overview.md "# Definition" sections to a cross-reference, and decide whether `Entities/AI-Agent` and `Entities/Event` are profiles of the `AI/` and `Models/` concepts or distinct Entities with their own names. Resolve CAND-001 in the same pass.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Principles.md` (Principle 7), `Language/Vocabulary.md`, `AI/Overview.md`, `AI/Agents/Overview.md`, `AI/Agents/Agent.md`, `Entities/AI-Agent/AI Agent.md`, `Models/Event.md`, `Entities/Event/Event.md`, `Domains/Common/Domain Events.md`, `AI/Context/Context.md`, `AI/Prompts/Overview.md`, `AI/Prompts/Prompt.md`, `AI/Tools/`, `AI/Evaluation/`, `AI/Knowledge/`, OBS-001, `ADR-Candidates.md#cand-001`, GAP-002

---

## AO-036

**Title:** Fifty-Nine Shall Clauses Are Per-Record Template Output Rather Than Subject-Specific Obligations

**Date observed:** 5 September 2026

**Description:** Surfaced by an external logic audit of the repository (5 September 2026). Three sentences recur verbatim as normative clauses: "Audit records shall remain immutable." (22 files: 8 in `Meta/` (Classification, Constraint, Contract, Ownership, Policy, Reference, Registry, Relationship), 14 in `AI/`; e.g. `Meta/Reference.md:163`); "Breaking semantic changes shall require explicit governance." (16 files, all `Domains/`, e.g. `Domains/HR/HR_KPIs.md:246` and `Domains/Finance/Finance_KPIs.md:207`, each closing an identical list "- improved calculation methods; - compatibility-preserving enhancements."); "Organizations shall preserve:" followed by a per-record list (21 files across `Meta/`, `AI/` and `Language/Schema.md:132`). In every case the sentence closes a template section ("# Auditability", a KPI evolution section, an "# Evolution" or "# Governance" section) whose preceding list items are also template text; 59 of the 2138 shall clauses in `docs/` are therefore template restatements. `Core/Manifest.md:178` already states, for the key-word definition, that restating rather than citing "is a duplication to be corrected, not a second source"; no equivalent rule covers cross-record obligations, and `Architecture-Health.md` counts these clauses as normative content. The clauses do not contradict each other and none is wrong on its own.

**Impact:** Normative weight is inflated, the same obligation can drift silently when one copy is edited, and a reviewer can show that record-level shall clauses were generated rather than derived from each concept. Consolidation would move obligations between tiers and is therefore not an editorial change.

**Recommendation:** Record only. If corroborated, a future Reference Case should either promote each template obligation to a single Core-tier clause (audit immutability under `Meta/Object.md` Auditability; semantic-change governance under `Core/Versioning.md`) with records citing it, or mark the template sections as non-normative structure per `Documentation-Standards.md`.

**Status:** Open; not escalated (external review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Manifest.md`, `Core/Versioning.md`, `Meta/Object.md`, `Meta/Reference.md`, `Language/Schema.md`, `Governance/Documentation-Standards.md`, `Governance/Architecture-Health.md`, AO-022, AO-035

---

## AO-037

**Title:** Process Is a Normative Domain-Tier Construct With No Core, Meta or Models Definition and No Stated Relationship to Workflow

**Date observed:** 5 September 2026

**Description:** Numbering note: the brief said AO-024 onward, but Governance/Architecture-Observations.md already holds AO-024 to AO-036 (5 September 2026 external audits), so drafts here start at AO-037. Every Domain profile ships a *_Processes.md whose line 37 delegates Process semantics to a specification that does not exist, in three variants: Domains/AI/AI_Processes.md:37 "Process semantics are defined by the Core Process specification." (also Affiliate, HR, Legal, Marketing, Operations, Support); Domains/BI/BI_Processes.md:37 "Process semantics are defined by the Meta specification." (also Finance); Product and Compliance cite "the Core specification". Core/ has no Process document (its only Process heading is Core/Governance.md:48 "Proposal Process", about specification evolution); Meta/ and Models/ have none; Core/Terminology.md has no Process entry but defines Workflow at :49-51 as "A defined sequence of operational actions that transforms the state of one or more entities." Domains/CRM/CRM Processes.md:33 defines "A CRM Process is a coordinated sequence of business activities that operates on one or more CRM Objects", materially the Workflow definition, and :51 opens "CRM Processes shall:". The only Core-adjacent text is Domains/Common/Domain Architecture.md:116-120 "The Domain may define business Processes ... Processes coordinate work but do not replace Object Lifecycles.", which gives no semantics. No Domain *_Processes.md cites Models/Workflow.md; six files list a bare "- Process" among the specifications they build upon (e.g. AI_Processes.md:251, Affiliate_Processes.md:228-230).

**Impact:** A reader following any Domain profile is sent to a specification that does not exist for its central construct, and the eleven profiles disagree on where it supposedly lives. Whether Process is a Domain-level synonym for Workflow, a composition of Workflows, or a distinct concept determines how Domain Processes relate to Lifecycles and State Transitions, and that determination is currently absent.

**Recommendation:** Record only. If corroborated by a Reference Case, decide between (a) declaring Process the Domain-level term for Workflow with a one-line mapping in Domain Architecture.md, or (b) defining Process in Models/ with its relation to Workflow and Lifecycle. The editorial pointer fix to Domain Architecture § Processes does not pre-empt this decision.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Domains/Common/Domain Architecture.md, Domains/*/*_Processes.md (11 files), Core/Terminology.md, Models/Workflow.md, Domains/Product/Product_Capabilities.md:211, AO-020, GAP-002, AO-032

---

## AO-038

**Title:** KPI Is Owned and Governed by Shall-Clauses in Twelve Domain Documents but Defined Nowhere Above the Domain Tier, and Its Ownership Is Claimed Both by BI and by Each Domain

**Date observed:** 5 September 2026

**Description:** Seven Domain KPI documents delegate KPI semantics to a non-existent document: Domains/AI/AI_KPIs.md:37 "Metric definitions are governed by the Core KPI specification.", Domains/Affiliate/Affiliate_KPIs.md:37 "KPI semantics are defined by the Core KPI specification." (also HR, Legal, Marketing, Operations, Support); the other five (BI, Compliance, Finance, Payments, Product) carry no such sentence. No KPI concept exists in Core/, Meta/, Models/, Language/ or Domains/Common; Core/Terminology.md:25 "All terms defined here are authoritative." with no KPI entry. KPI is nonetheless the subject of Ownership rules: Affiliate_KPIs.md:184-186 "Every KPI shall have an owning Domain." / "The Affiliate Domain owns KPIs evaluating Affiliate Objects, Affiliate Processes, and Affiliate Capabilities." (the same clause recurs in nine KPI files), while Domains/BI/BI_Objects.md:33 defines an Analytical Object as "a business Object owned by the BI Domain", lists "- KPI" at :71 and states at :131 "The BI Domain owns Analytical Objects."; BI_KPIs.md:146 narrows this to "KPIs evaluating BI Capabilities and Analytical Objects". Meta/Ownership.md:33 scopes Ownership to managed Objects, and KPI is never declared an Object (Domains/Compliance/Compliance_KPIs.md:157, Domains/Payments/Payments_KPIs.md:131 assign Ownership to it regardless).

**Impact:** A reader cannot determine whether a KPI is an Object, which Domain owns a KPI that evaluates another Domain's Objects, or what a KPI is outside the local Definition of each file. The gap sits beneath AO-005/CAND-008 (value representation), which assume a KPI construct exists to carry values.

**Recommendation:** Record only. If corroborated, a Reference Case should decide whether KPI is a Domain-tier specialization of Object (and therefore Ownable) with a single home, and whether KPI ownership follows the evaluated Object's Domain or the BI Domain. The editorial removal of the phantom pointer and the BI_Objects.md qualification do not decide this.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Domains/*/*_KPIs.md (12 files), Domains/BI/BI_Objects.md, Domains/Affiliate/Affiliate_Objects.md:185, Core/Terminology.md, Meta/Ownership.md, AO-005, CAND-008, GAP-002

---

## AO-039

**Title:** Three Domains Require an Object to Participate in One or More Lifecycles While the Lifecycle Model Requires Exactly One

**Date observed:** 5 September 2026

**Description:** Domains/BI/BI_Lifecycles.md:64 "Every Analytical Object shall participate in one or more explicitly defined Lifecycles." recurs verbatim in Domains/BI/BI_Objects.md:157, Domains/Finance/Finance_Objects.md:157, Domains/Finance/Finance_Lifecycles.md:64 and Domains/Payments/Payments_Objects.md:144. Models/Lifecycle.md:33 "Every Entity shall have exactly one Lifecycle." and :97 "At any point in time an Entity shall occupy exactly one valid State defined by its Lifecycle."; Specification/06 Lifecycle Model.md:17 publishes the same rule. The BI document itself defers to the upstream model (BI_Lifecycles.md:37, :162 "build upon: Lifecycle"), so it cannot claim an independent cardinality. Other profiles already use the conforming wording: Domains/Product/Product_Lifecycles.md:191 "Each Product Object shall have one Lifecycle.", Domains/CRM/CRM Objects.md:143 "an explicitly defined Lifecycle". Multiple concurrent Lifecycles imply multiple concurrent States, which the Model forbids.

**Impact:** Both sides use shall. An implementation conforming to the BI, Finance or Payments profile by giving an Object two Lifecycles is non-conformant to Model-05 Lifecycle Integrity, and vice versa. This is the inverse direction of AO-028 (one Lifecycle reused by many Entities) and the two together leave Lifecycle cardinality undecided in both directions.

**Recommendation:** Record only. If corroborated, resolve together with AO-028 in one Reference Case; the most likely outcome is aligning the five Domain clauses to the Product wording, but that is a normative edit and is not proposed here.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Models/Lifecycle.md, Specification/06 Lifecycle Model.md, Domains/BI/BI_Lifecycles.md, Domains/Finance/Finance_Lifecycles.md, Domains/Payments/Payments_Objects.md, Domains/Product/Product_Lifecycles.md, AO-028, AO-022

---

## AO-040

**Title:** Domain Profiles Do Not Carry the Component Set Their Own Domain Architecture Imposes With Shall, and the Domain Concept Omits Three of Object's Core Characteristics

**Date observed:** 5 September 2026

**Description:** Domains/Common/Domain Architecture.md:60 "Every Domain shall define the following architectural components." followed by Identity (:64 "The Domain shall possess a unique Identity."), Constraints (:134 "The Domain shall define applicable Constraints."), Integration Points (:150) and Governance (:158 "The Domain shall define governance responsibilities including: - ownership; - change management; ..."), with Conformance at :240 "define all mandatory architectural components;". Domains/BI/Overview.md:89-103 lists Objects, Relationships, Events, Lifecycles, Processes, Capabilities, KPIs, Policies, AI and no Constraints or Governance component; no BI_*.md supplies them; the only Domain-level identifier is the document ID "DOMAIN-BI-README-01" (:11). Domains/CRM/Overview.md:86-99 has the same gaps and additionally omits Capabilities although CRM Capabilities.md exists. Domains/Affiliate/Overview.md:158 carries a "# Domain Governance" section, showing the component is expected in a profile. At the concept level, Domains/Common/Domain.md:64-75 "Every Domain has: Identity; Purpose; Scope; Ownership; Managed Objects; Business Capabilities; Policies; Constraints; Integration Points; Governance." omits Metadata, Classification and Relationships, which Meta/Object.md:65-73 lists as core characteristics of every Object and :224 requires specializations to preserve; Domain.md never states that Domain specializes Object, unlike Meta/Organization.md:63. Compliance is the only profile without a Lifecycles document while Compliance/Overview.md:38 and :96 claim one.

**Impact:** The Specification's own Domain profiles are the first test case of Domain Architecture's shall-list and do not pass it; a critic can quote the tier failing the architecture it mandates. AO-001 freezes edits to the two Domain concept documents until their canonical source is decided, so the Domain.md gap cannot be patched now.

**Recommendation:** Record only. Resolve after AO-001 settles which Domain definition is canonical; then either add the missing components to each profile (Constraints, Governance, Identity scheme) or relax Domain Architecture's list to what profiles actually carry. Do not invent a Domain identifier scheme editorially.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Domains/Common/Domain Architecture.md, Domains/Common/Domain.md, Models/Domain.md, Meta/Object.md, Domains/BI/Overview.md, Domains/CRM/Overview.md, Domains/Affiliate/Overview.md, Domains/Compliance/Compliance_Objects.md:170-174, AO-001, AO-022, AO-029

---

## AO-041

**Title:** Entity Profiles Reference Named Lifecycles That Do Not Exist and List States That Conflict With the Standard Lifecycle That Claims Them

**Date observed:** 5 September 2026

**Description:** Lifecycles/ contains Commercial, Content, Financial, Operational and Organizational Lifecycle only. Entities/Affiliate/Affiliate.md:118 "The Affiliate Lifecycle defines all valid state transitions." with states at :105-110 Registered, Pending Approval, Active, Suspended, Terminated, Archived, while Lifecycles/Commercial Lifecycle.md:33-40 names Affiliate among its applicable Entities with states Draft, Review, Approved, Active, Suspended, Retired, Archived and :143-144 requires a conforming Entity to implement "the defined States" and permit "only the defined State Transitions". The same pattern holds for Entities/Bonus/Bonus.md:121, Brand.md:115, Campaign.md:123, Offer.md:119, Transaction.md:118, Wallet.md:120 (each "The <X> Lifecycle defines all valid state transitions.", no such document), each followed by the template "Undefined transitions are prohibited." (11 files). Entities/Vendor/Vendor.md:96 names "**Procurement**" as governing Domain; no Domains/Procurement/ exists; Vendor.md:102 conforms to the Commercial Lifecycle whose applicable list names "Vendor Agreement", not Vendor. Affiliate.md:177 "Every Affiliate shall follow one defined Lifecycle." cannot be satisfied when the named Lifecycle is absent and the standard one lists different states.

**Impact:** An implementer of these Entities has two incompatible state sets under a prohibition on undefined transitions and no document to resolve them. Combined with AO-028 and AO-039, Lifecycle binding is undecided at three tiers.

**Recommendation:** Record only. A Reference Case should decide whether Entity profiles carry their own Lifecycle (then the named documents must be written) or reference a standard Lifecycle (then the state lists in the profiles must be dropped or mapped, as the Ticket profile would need for Resolved/Closed). Do not pick a state set editorially.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Entities/Affiliate/Affiliate.md, Entities/Bonus/Bonus.md, Entities/Brand/Brand.md, Entities/Campaign/Campaign.md, Entities/Offer/Offer.md, Entities/Transaction/Transaction.md, Entities/Wallet/Wallet.md, Entities/Vendor/Vendor.md, Lifecycles/Commercial Lifecycle.md, Entities/Overview.md, AO-028, AO-039, AO-029, AO-033, FW-002

---

## AO-042

**Title:** AI Knowledge Is Declared Independent of Memory Records and Sourced Directly From Enterprise Systems, Against Constitution Principles 5 and 6

**Date observed:** 5 September 2026

**Description:** Core/Constitution.md:35 "Memory Precedes Knowledge. Knowledge is always derived from Memory. World Models are always derived from Knowledge. Memory → Knowledge → World Model." and :36 "Reconstructability. Knowledge and World Models must always be reproducible from Memory without requiring access to the original external systems." AI/Knowledge/Knowledge.md:35 "Knowledge is independent of individual AI Agents, Context, and Memory Records." and :133 lists Memory Records only as something Knowledge "may reference". AI/Knowledge/Knowledge Sources.md:87-93 "Knowledge may originate from: - enterprise systems; - workflow platforms; - document repositories; - operational databases; - knowledge management systems." with :95 "System-generated Knowledge shall preserve system provenance." Neither document states that Knowledge is derived from Memory; Memory appears once in each as a build-upon item (Knowledge Sources.md:159, Overview.md:86). Both are Status Draft (normative under Documentation-Standards.md:48).

**Impact:** A conforming Knowledge implementation may hold Knowledge that no Memory Record backs and that cannot be reconstructed without the source system, which is exactly what Principles 5 and 6 forbid. This is a principle-level tension, not a wording defect, and the only one of its kind found in these four tiers.

**Recommendation:** Record only. Resolve through the same Reference Case pipeline that produced the Knowledge vs World Model concept paper; the likely outcome is restating Knowledge as a derivation over Memory Records with external systems admitted only as Memory sources, but that is a Core-adjacent decision under the Freeze and is not proposed editorially.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Core/Constitution.md (Principles 5, 6), AI/Knowledge/Knowledge.md, AI/Knowledge/Knowledge Sources.md, AI/Knowledge/Knowledge Lifecycle.md, Memory/Memory Record.md, AO-003, CAND-003, Concept-Paper-Knowledge-vs-World-Model.md, AO-035

---

## AO-043

**Title:** Reference Architecture Carries Ten Shall-Clauses Under a Status That Declares It Imposes No Requirement, and Promises Three Views That Do Not Exist

**Date observed:** 5 September 2026

**Description:** All eight Reference Architecture files are "**Status:** Informative" (line 13 of each). Governance/Documentation-Standards.md:49 defines Informative as "non-normative ... material that imposes no requirement of its own. Used for Examples/, Reference Architecture/ ...". The tier nonetheless contains ten shall-clauses: Reference Architecture/Object-Architecture.md:43 "Every Entity shall possess a unique and persistent identity."; Business-Event-Architecture.md:92 "Once recorded, a Business Event shall not be modified." and :94; Operational-Memory-Architecture.md:115 "Operational Memory shall remain subject to governance." and :126 "Every memory entry shall remain attributable to its origin."; Domain-Architecture.md:110; AI-Architecture.md:67, :106, :128, :149. Several restate Draft-tier rules in different words (memory entry vs Memory Record; "enriched" memory). Reference Architecture/Overview.md:77-113 lists nine views ending "Governance Architecture ↓ Integration Architecture ↓ Deployment Patterns", while README.md:17-22 lists six; the three are absent from the repository.

**Impact:** A reader cannot tell whether the ten clauses bind (they read as requirements) or illustrate (the Status says so); where they diverge from Meta/Models wording, an Informative document becomes a second source of normative text. The same Status-versus-content mismatch is recorded for Governance registers in AO-025.

**Recommendation:** Record only. If corroborated, either downgrade the ten clauses to descriptive wording in a future Reference Architecture revision or add a tier-level note that Informative text restates, and never extends, Draft-tier requirements. The editorial reconciliation of the six-versus-nine view lists does not touch the clauses.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** Reference Architecture/*.md (8 files), Governance/Documentation-Standards.md, Memory/Memory Record.md, Core/Constitution.md (Memory Entry vs Memory Record), OBS-002, AO-025, AO-032

---

## AO-044

**Title:** A Deprecated Tool Remains Operational While Tool Execution Requires the Active State

**Date observed:** 5 September 2026

**Description:** AI/Tools/Tool Lifecycle.md:126-128 "## Deprecated / The Tool remains operational but is no longer recommended for new implementations." AI/Tools/Tool Execution.md:79-81 lists as a precondition of execution "- the Tool shall be Active;". Both are Status Draft. A Tool in the Deprecated state therefore both may execute (Lifecycle) and shall not execute (Execution). The Prompts and Tools sub-tier also defines Tool ownership twice with different responsibility lists (Tool Governance.md:81-87 vs Tool Lifecycle.md:182-188) and Tool Registry.md:84-88 carries Status and Lifecycle State as two unexplained items; those are duplicate-definition items already characterised by AO-035 and are listed here only as Related.

**Impact:** An implementation cannot satisfy both documents for a Deprecated Tool; the state most likely to exist in a long-lived deployment is the one whose executability is undefined.

**Recommendation:** Record only. If corroborated, decide whether Deprecated is an executable state (then amend the Execution precondition to Active or Deprecated) or not (then amend the Lifecycle text); either is a normative edit under the Freeze.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** AI/Tools/Tool Lifecycle.md, AI/Tools/Tool Execution.md, AI/Tools/Tool Governance.md, AI/Tools/Tool Registry.md, AI/Tools/Tool.md, AO-035, AO-036

---

## AO-045

**Title:** The Publication Model Recognizes Two Projection Instances While the Site Publishes Four, and Places Comparisons in a Tier the Site Calls Canonical

**Date observed:** 5 September 2026

**Description:** Surfaced by a claim-provenance red-team of the published site (5 September 2026). Governance/Publication-Model.md:69 defines tier 3, Projection, as "A machine-generated representation of a single canonical document, produced by the external Publication Engine", and states "Two instances currently recognized", naming Core Vocabulary term-cards and individually authorized Adoption pages. Line 75 places the remaining site surface in tier 4: "The homepage, /changelog, and /comparisons/* pages, together with the site-held informative records", which are "informative, illustrative, explicitly not carrying independent normative weight". The published site nonetheless carries the tier-3 field set (source_file, source_url, history_url) and the word projection on two further routes: /examples/implementation-case (mirror examples/implementation-case/index.html:229, "This page is a compiled projection of docs/Examples/Implementation-Case/Performance-Marketing-Operator.md") and /evolution (mirror evolution/index.html, "This page is a compiled projection of ROADMAP.md"), and it labels every tier-4 comparison a canonical record (mirror comparisons/ddd/index.html, "This comparison is a canonical record; the page is a deterministic projection of it."). No Decision authorizes a projection of docs/Examples/ or of ROADMAP.md; CAND-012 and CAND-013 authorize only Adoption pages and the Consumer Tool.

**Impact:** The five-tier model exists precisely to stop "what OCOM says" being confused with "what got rendered onto a web page" (Publication-Model.md:57). A reader who applies the model to the live site finds two publication units it does not classify and one whole tier the site relabels, so the model cannot be used to decide what carries normative weight.

**Recommendation:** Record only. Track together with FW-006 and AO-008. If corroborated, a future Reference Case should either extend the Projection tier with an explicit instance list and an authorization rule for Examples and root-level documents, or state that anything outside the two recognized instances is tier 4 and must not use the tier-3 vocabulary.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Governance/Publication-Model.md`, `Governance/ADR-Candidates.md (CAND-012`, `CAND-013)`, `Governance/Documentation-Debt.md#FW-006`, AO-008

---

## AO-046

**Title:** No Canonical Document States Which Tier Defines Which Term, so "Core Vocabulary" Reads as the Whole Definition Set

**Date observed:** 5 September 2026

**Description:** Surfaced by a claim-provenance red-team of the published site (5 September 2026). The thirteen Meta tier terms carry term records; Entity, Domain, Event, State, Lifecycle and Workflow are defined at the Models tier and have no term record. Publication-Model.md:57 notes the consequence in passing, "Lifecycle is defined at Models/ tier, not Meta/ tier, and so has no card at all", but no canonical document states the split as a rule, and Core/Manifest.md:109 lists "entities; domains; workflows" among what the specification defines without saying where. Examples/Implementation-Case/Performance-Marketing-Operator.md:143 is the only place the repository spells it out for a reader: "Lifecycle, State and Domain, which are defined at the Models tier, are not mapped in this table." The absence is what let three site artefacts assert that "Every definition lives once in the Core Vocabulary and is referenced everywhere else" without contradicting any single canonical sentence.

**Impact:** A reviewer who reads Core Vocabulary as the definition set of OCOM will conclude that six of the concepts the specification most depends on are undefined; a reviewer who reads it as the Meta tier subset has no canonical sentence to cite for that reading.

**Recommendation:** Record only. If corroborated, a future Reference Case should add one tier-to-term statement at the Core tier naming which concepts are defined at Meta and which at Models, so that both the site and a reader can cite it.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Manifest.md`, `Governance/Publication-Model.md`, `Meta/Overview.md`, `Models/Overview.md`, `Examples/Implementation-Case/Performance-Marketing-Operator.md`, AO-002, AO-017

---

## AO-047

**Title:** "Reference Case" Names Both a Templated Evidence Unit and a Published Narrative That Uses None of Its Fields

**Date observed:** 5 September 2026

**Description:** Surfaced by a claim-provenance red-team of the published site (5 September 2026). Standard Evolution Methodology.md makes Reference Case a governed unit of evidence with a fixed template (Purpose, Expressive Coverage, Boundary Conditions, Boundary Tags, External Assurance, Core Impact, Decision), recorded inside Architecture-Observations.md; the register uses it that way at AO-008, whose Reference Case field reads "RC-008 - External Audit Comparison of ocom.uno Against the GitHub Repository". Examples/Implementation-Case/Performance-Marketing-Operator.md:25 uses the same words for something else: "It is a Reference Case. It demonstrates the model, it does not extend it." That document carries none of the template fields, has no RC identifier, and appears in no register. The site reprints the label on the page eyebrow and in the Evidence Register row "Reference Cases published: 1".

**Impact:** The methodology's central evidence unit shares a name with an informative narrative, so a reader counting Reference Cases can reach one or nine depending on which sense is meant, and the Evidence Register's own count is ambiguous.

**Recommendation:** Record only. If corroborated, a future Reference Case should either rename the published narrative (Implementation Case) or state in Standard Evolution Methodology.md that Reference Case is reserved for RC-nnn records and give the illustrative sense its own term.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Governance/Standard Evolution Methodology.md`, `Governance/Architecture-Observations.md (AO-008`, `RC-006 to RC-009)`, `Examples/Implementation-Case/Performance-Marketing-Operator.md`, `ROADMAP.md`

---

## AO-048

**Title:** AI Retrieval Is Presented as an OCOM Capability While the AI Tier Disclaims Retrieval Mechanics and No Tier Defines It

**Date observed:** 5 September 2026

**Description:** Surfaced by a claim-provenance red-team of the published site (5 September 2026). AI/Context/Context Assembly.md's Independence section states that the specification "does not prescribe: retrieval algorithms; vector search; graph traversal; ranking models", and no document at the Core, Meta, Models or Language tier defines retrieval as a concept. Every published concept-coverage matrix nonetheless scores "AI retrieval: Covered" for OCOM under a legend meaning the model defines the concept explicitly (mirror comparisons/ddd/index.html and eight sibling pages). The shape is identical to AO-021, which records the same defect for Evidence.

**Impact:** A second headline capability is scored as defined against a tier that explicitly declines to define it; a reviewer applying the published review question on definitions can falsify nine matrices at once.

**Recommendation:** Record only. Track together with AO-021. If corroborated, a future Reference Case should either define what OCOM does supply to a retrieval system (a governed, addressable record set) at a tier that can be cited, or restate the public capability claim in Context Assembly's own terms.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `AI/Context/Context Assembly.md`, AO-021, `Governance/Publication-Model.md`

---

## AO-049

**Title:** Notation Is Defined Normatively at the Language Tier but Appears in Neither List of Core/Manifest.md's Scope

**Date observed:** 5 September 2026

**Description:** Surfaced by a claim-provenance red-team of the published site (5 September 2026). Language/Notation.md (LANG-NOTATION-01, Status Draft) states at line 21 "This document defines the notation used by the OCOM Language", lists graphical notation among five Representation Types, and closes that section with "All representations shall preserve semantic equivalence." Core/Manifest.md:109 lists what the specification defines (operational concepts; entities; domains; workflows; operational relationships; modeling principles; semantic interpretation rules) and line 119 lists what it does not define (software architecture; databases; APIs; programming languages; user interface design; infrastructure; implementation technologies; business strategy; and two Constitution-scoped exclusions). Notation appears in neither list, so no canonical sentence says whether an implementer must adopt the OCOM notation or may ignore it.

**Impact:** A shall-clause at the Language tier binds a representation an implementer cannot tell is in scope; public positioning statements about whether OCOM is or is not a notation have no canonical sentence to rest on.

**Recommendation:** Record only. If corroborated, a future Reference Case should place Notation explicitly in one of Core/Manifest.md's two Scope lists and state its conformance modality once.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Core/Manifest.md`, `Language/Notation.md`, `Language/Overview.md`, AO-034

---

## AO-050

**Title:** Two Conformance Clauses Bind Governance, a Core Characteristic No Tier Defines

**Date observed:** 6 September 2026

**Description:** Surfaced by an external logic audit of the published site (6 September 2026), which reached the same gap AO-023 records from the conformance side rather than the definition side. `Meta/Object.md`:63 lists Governance as the seventh Core Characteristic of every Object. `Specification/04 Meta Model.md` restates it, and `Specification/08 Conformance.md` requires that "a compliant implementation shall ensure that every managed Object ... supports governance"; `Specification/04` additionally requires that specifications extending Object "shall preserve its core characteristics". No document at any tier defines Governance as a per-Object characteristic. `docs/Governance/` and `Specification/07 Governance.md` use the word in an unrelated sense, how the Specification itself evolves, which the terminology notes in chapters 4 and 7 acknowledge.

**Impact:** Two normative clauses cannot be checked, so a conformance claim that cites them cannot be evaluated. `Language/Conformance.md`:49 requires conformance criteria to be "objective, measurable, verifiable"; these two are none of the three. The specification's own review question 4, published at /specification/how-to-review, asks exactly this and fails on it.

**Recommendation:** Record only. If corroborated, a future Reference Case should either give Governance a Meta tier term record or remove it from the Core Characteristics list until one exists, and state which of the two senses the conformance clause means.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Object.md`, `Specification/04 Meta Model.md`, `Specification/08 Conformance.md`, `Language/Conformance.md`, `AO-023`

---

## AO-051

**Title:** The Compiled Reading Path Is Published as Normative and Simultaneously Disclaims Being the Normative Text

**Date observed:** 6 September 2026

**Description:** Surfaced by an external logic audit of the published site (6 September 2026). The compiled reading path is titled Normative Specification and carries Status Draft, which `Governance/Documentation-Standards.md` defines as "normative and currently in force". Chapter 1 of the same document states that it "is a compilation and editorial layer over that material, not a replacement for it" and that "the granular documents remain the normative source of truth and continue to evolve independently of this reading path". Chapter 2 asserts that "these eleven principles are normative and apply to every model created using this specification", and the compiled path carries 37 shall clauses of its own.

**Impact:** A reader satisfying a shall cannot establish whether the obligation binds as written or is a restatement of a source document that has since moved. Conformance is claimed against a version, and the two candidate texts carry different version numbers, 0.2 for the reading path and 0.1 for the granular documents.

**Recommendation:** Record only. If corroborated, a future Reference Case should either declare the reading path Informative and remove its shall clauses, or declare it normative for a stated version and pin the granular documents it was compiled from.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Specification/01 Introduction.md`, `Specification/02 Design Principles.md`, `Governance/Documentation-Standards.md`, `Governance/Publication-Model.md`, `AO-049`

---

## AO-052

**Title:** Chapters 4 and 5 Give Relationship Different Cardinality Modality and Different Arity

**Date observed:** 6 September 2026

**Description:** Surfaced by an external logic audit of the published site (6 September 2026), which found two conflicts the existing editorial note in chapter 5 does not cover. Modality: `Specification/04 Meta Model.md` states that a Relationship "may additionally define direction, cardinality, status, and constraints", while `Specification/05 Object Model.md` states that "every Relationship shall connect identifiable Entities, have a defined type, and define cardinality". Arity: chapter 4 defines the required fields as one Source Object and one Target Object, a binary association, while chapter 5 defines a Relationship as "an explicit operational association between two or more Entities", an n-ary one. `Meta/Relationship.md` itself also states the association is "between two or more Objects" in its Purpose while requiring exactly one Source and one Target.

**Impact:** Cardinality is optional and mandatory at once, and an implementation cannot tell whether a three-participant association is expressible. This sits on the term the specification uses second most often, and it is a second instance of the Design Principle 7 exception already recorded as AO-002 and AO-017.

**Recommendation:** Record only. If corroborated, a future Reference Case should settle the modality of cardinality once and state whether Relationship is binary or n-ary in the Meta tier document, with the Models tier following it.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Meta/Relationship.md`, `Models/Relationship.md`, `Specification/04 Meta Model.md`, `Specification/05 Object Model.md`, `AO-002`, `AO-017`

---

## AO-053

**Title:** Evidence Is Published as One of Four Pillars While Its Definition Is Reserved and It Is Not a Core Characteristic

**Date observed:** 6 September 2026

**Description:** Surfaced by an external logic audit of the published site (6 September 2026). The one-sentence formulation of OCOM used on the site and in `ROADMAP.md` names identity, ownership, lifecycle and evidence. Of the four, Identity and Ownership are Meta tier term records, Lifecycle is defined at the Models tier, and Evidence is specified at the Memory tier with `Memory/Evidence Overlay.md`:33 stating that its Definition is "reserved for a future version". Evidence does not appear in `Meta/Object.md`:63's list of an Object's Core Characteristics at all, so the four pillars are not a subset of any single canonical list.

**Impact:** The sentence a reader meets first rests on a term the specification has not defined, and pairs it with three terms defined at three different tiers. A reviewer checking the pillars against the Core Characteristics finds neither list contains the other.

**Recommendation:** Record only. If corroborated, a future Reference Case should either define Evidence or state, once and canonically, that the four pillar formulation is an informative summary and not a list of Core Characteristics.

**Status:** Open; not escalated (single review source; awaiting a Reference Case per Standard Evolution Methodology Rules 1 and 2)

**Architect Response:** *(pending)*

**Related:** `Memory/Evidence Overlay.md`, `Meta/Object.md`, `Core/Constitution.md`, `ROADMAP.md`, `AO-021`, `FW-001`

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
| 0.1 | 4 September 2026 | Added AO-014 through AO-022 (conformance scope, ownership modality, identity replacement clause, relationship arity/direction/cardinality, metadata categories, organization participation, participant lists, evidence pillar, object obligation modality), evidenced by an external pre-launch red-team review of the published site; all recorded, none escalated |
| 0.1 | 5 September 2026 | Added AO-023 (Core definitions close on each other through the undefined word "governable"), surfaced independently by two external reviews of the published site; record only, not escalated, tracked with CAND-010 and AO-021. |
| 0.1 | 5 September 2026 | Added AO-024 through AO-036 (Architectural Principles vocabulary, register Status, Constitution edit under the Freeze, no terminating rule for Object obligations on Lifecycle and Registry, Lifecycle cardinality, Entity versus Object characteristics, Domain and Entity bootstrap, identifier reuse, conformance aggregation, Owner typing, Reference versus Relationship, duplicated AI definitions, template shall clauses), surfaced by an external logic audit of commit 37c986a; all record only, not escalated. AO-015 and AO-018 marked independently corroborated; AO-016 and AO-022 Related extended; AO-023 corrected (no ADR Candidate records the Governance gap; CAND-010 is the Worked Example's publication authorization) and the third usage of Governance in `AI/` added. |
| 0.1 | 5 September 2026 | Added AO-037 through AO-044 (Process undefined above the Domain tier, KPI undefined and doubly owned, Lifecycle cardinality in three Domain profiles, profiles not carrying the components their Domain Architecture mandates, Entity profiles naming Lifecycles that do not exist, AI Knowledge declared independent of Memory against Constitution Principles 5 and 6, Reference Architecture carrying shall-clauses under an Informative Status, a Deprecated Tool remaining operational against the Active precondition), surfaced by a full read of the Domains, Entities, AI and Reference Architecture tiers; all record only, not escalated. |
| 0.1 | 5 September 2026 | Added AO-045 through AO-049 (the Projection tier recognizing two instances while the site publishes four and labelling Convenience Representations canonical, no canonical statement of which tier defines which term, Reference Case naming two different things, AI retrieval presented as a defined capability, Notation absent from both Scope lists), surfaced by a claim-provenance red-team of the published site; all record only, not escalated. AO-022 Related extended with `Meta/Ownership.md` and `AO-018`. |
| 0.1 | 6 September 2026 | Added AO-050 through AO-053 (two conformance clauses binding an undefined Governance characteristic, the reading path published as normative while disclaiming it, Chapters 4 and 5 disagreeing on Relationship cardinality modality and arity, Evidence published as a pillar while its Definition is reserved), surfaced by an external logic audit of the published site; all record only, not escalated. |

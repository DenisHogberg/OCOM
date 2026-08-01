<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Architecture Discussion — The Irreducible Core of OCOM

[← Back](Architecture-Observations.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Architecture Discussion — The Irreducible Core of OCOM

**Document ID:** GOV-DISCUSSION-IRREDUCIBLE-CORE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 31 July 2026

---

# Purpose

This document prepares the ground for an eventual ADR Candidate on the question "what is the irreducible Core of OCOM, and where does the boundary to pluggable modules sit?" It does not decide anything, does not change any specification document, and is not itself an ADR Candidate.

**Provenance note, stated plainly because it departs from this repository's usual evidentiary path:** this discussion did not originate from a Reference Case documenting an operational limitation, the normal entry point defined in `Standard Evolution Methodology.md`. It originated top-down, from a product-architecture conversation about how OCOM-based implementations should scope Dashboard, Prediction, AI-agent, and Workflow capabilities against a common Core. `Standard Evolution Methodology.md`'s own principles apply here without exception: "Evidence Before Architecture" and "Reference Cases Before Core Changes" mean nothing in this document may be promoted to an ADR Candidate on its own strength. Its purpose is narrower — to state the question precisely, propose one candidate framework for answering it, and identify what Reference Case evidence would actually be needed before any of it could become normative. This is consistent with how `Concept-Paper-Knowledge-vs-World-Model.md` and `Concept-Paper-Value-Model.md` were used: as Informative material a Chief Architect can react to, not as a substitute for the pipeline.

This discussion is closely related to `AO-007`'s still-open refinement ("a Core concept must eliminate a demonstrated deficiency, not introduce a new abstraction") — the framework proposed in Section 3 is, among other things, an attempt to state a test for *deficiency* in this specific context (composability and auditability of machine-generated claims) rather than an argument from elegance.

---

# 1. Problem Statement

**What was found:** implementations built on OCOM (observed directly in one such implementation, described in Section 2) tend to grow a set of "intelligent" capabilities — object scoring, influence/impact between objects, forecasting, causal inference, recommendation generation, and AI-driven reasoning — that do not obviously belong to any single layer. Treating all of them as Core risks Core never stabilizing (each is a fast-moving, domain-specific, frequently-revised capability). Treating all of them as plugins risks Core collapsing to a bare typed graph store with no defensible reason a plugin author or a client should trust its outputs at all — at which point "OCOM" is a schema, not a platform.

**Why a simple answer does not resolve it:** the intuitive split ("structural things are Core, smart things are plugins") does not survive contact with the actual list. Lifecycle state is unambiguously Core, but it is also the mechanism that makes every downstream "smart" output honest — removing it from Core to keep Core "just structural" would remove the one thing that gives a forecast or a recommendation any epistemic weight at all. Conversely, calling forecasting "Core" because it is central to the product's value proposition would freeze a fast-moving algorithmic surface into the ten-year-stable layer, which `Standard Evolution Methodology.md`'s Minimal Core principle argues directly against.

**Where it was found:** no Reference Case in this repository yet. The pattern was first noticed in a non-OCOM-repository implementation (Section 2) and is brought here because the question is architectural to OCOM generally, not specific to that implementation.

---

# 2. Architectural Context

The following already-decided or already-open positions are what make this question visible; none of them, individually, decided it.

- `Meta/Object.md` and `Models/Entity.md` already establish that Objects and Attributes carry identity, evidence, and (via `Concept-Paper-Value-Model.md`, still pending Chief Architect promotion) self-describing Value. This is the existing Core substrate any "intelligent" capability would sit on top of.
- `Standard Evolution Methodology.md`'s Minimal Core principle ("Core should remain as small as it can be while remaining sufficient") argues for pushing capabilities out of Core by default. Taken alone and without a countervailing test, this principle has no natural stopping point short of a bare graph store — which is the risk this discussion is about.
- `AO-007` (open, not yet promoted) argues Core should grow only to *eliminate a demonstrated deficiency*, never merely to *add* a plausible abstraction. This discussion proposes applying that same test in the other direction: a capability should be *kept out* of Core only if removing it from Core does not silently strip the honesty guarantees the rest of Core depends on.
- An implementation-level ADR is understood to exist, in a separate (non-Specification) repository, addressing whether OCOM-based systems may take write actions (approve / assign / reject / create) versus remaining observational — referred to here as the observational/operational question. This document cannot verify that ADR's current text from within this repository and does not rely on its specifics, but flags a direct dependency: Section 3's classification treats "reasoning AI" and any write-capable module as bound by the same evidence contract as read-only modules, which presumes that question is resolved deliberately, not by a product roadmap arriving at it implicitly. If a Reference Case is ever filed against this discussion, it should confirm that ADR's actual current status rather than rely on this document's characterization of it.
- No Reference Case, Architectural Observation, or ADR Candidate in this repository currently addresses Core/plugin boundary placement for scoring, influence, forecasting, causal, recommendation, or reasoning-AI capabilities. This is genuinely open ground, not a restatement of an existing filing.

---

# 3. A Candidate Framework: Contract vs. Realization

**Stated as a hypothesis to be tested against Reference Cases, not as a conclusion.**

The candidate test: for any capability under discussion, separate —

- **the contract** — the shape a capability's output must take to compose with the rest of the graph honestly: what evidence it must cite, what confidence/resolution status it must declare, what Lifecycle state it participates in, how it is versioned. This is Core, because Core's actual defensible value is not any specific algorithm but the guarantee that *every* machine-generated claim in the graph, regardless of which module produced it, can be audited the same way.
- **the realization** — the specific algorithm, model, or rule set that fills the contract for a given capability and domain. This is a plugin, because realizations are exactly what `Standard Evolution Methodology.md`'s Minimal Core principle correctly identifies as unstable, domain-specific, and improvable — freezing one into Core would violate that principle directly.

Applying this split to the capabilities that motivated this discussion:

| Capability | Candidate Core contract | Candidate plugin realization |
|---|---|---|
| Object model | The type/attribute schema and its governed evolution process | — (this is Core in full; not a candidate for splitting) |
| Lifecycle | The state machine itself (state semantics, transition rules, evidence-to-state binding) | Which named states apply to a given object type, proposed and governed the same way any Core extension is |
| Object "potential" | A carrier contract: an object may hold a derived score with evidence, confidence, and a cited method | The scoring method itself, which differs by object type and domain |
| Influence between objects | A typed, directional, evidenced relationship — treated as an extension of the existing Relationship model, not a new primitive | The inference method that assigns influence strength from raw signals |
| Forecasting | A contract: a forecast is a first-class object with value, confidence interval, cited method, and a Lifecycle state — never a special-cased type outside the graph's own honesty rules | The forecasting model itself |
| Causal relationships | The same typed-relationship contract as Influence | The discovery method (correlation analysis, causal inference, LLM-assisted reasoning) that proposes such relationships |
| Recommendations | A contract requiring every recommendation to cite the specific real condition that triggered it, carry a category, and be traceable | The rule set or model that generates recommendations |
| Reasoning AI | The same evidence/Lifecycle contract as every other module — an AI-produced claim earns no exemption from citing what it is based on | The specific model, prompting strategy, or reasoning framework, which is expected to be the fastest-changing element of all |

**What this framework does not resolve:** it does not by itself decide whether "Influence" and "Causal relationships" should be one Relationship extension or two, whether a forecast's contract needs a different shape than a recommendation's, or how contract versioning should work when a contract itself needs to change under a live ecosystem of plugins built against it. These are exactly the kind of questions `Standard Evolution Methodology.md` says should be answered by Reference Case evidence, not asserted here.

---

# 4. What Would Actually Ground This

Per `Standard Evolution Methodology.md` §"Reference Cases Before Core Changes," nothing in Section 3 may become an ADR Candidate without independent Reference Cases. Candidate Reference Case sources, named without commitment that they will in fact be filed:

- An implementation that attempted to add a scoring or forecasting capability using only existing Core concepts, and hit a specific, describable Boundary Condition (per the Controlled Boundary Vocabulary) — e.g. `structural-integrity` if nothing forces a forecast to carry a Lifecycle state, or `referential-integrity` if nothing forces a recommendation to reference the evidence that triggered it.
- A second, independent such attempt, in a different domain or by a different author, hitting the same or a related boundary — required before any Repeated Pattern can be recognized (Rule 3, Repeatability Before Standardization).
- Confirmation of the observational/operational ADR's actual current text (Section 2), since Section 3's treatment of Reasoning AI and any write-capable module assumes, but cannot itself verify, how that question was resolved.

Until such cases exist, the correct status of this document is Informative, and the correct action on it is "hold," not "adopt."

---

# 5. Relationship to OCOM Specification

This document:

- does **not** change OCOM Core;
- does **not** introduce new architectural concepts;
- does **not** decide the Core/plugin boundary for any capability named in Section 3;
- defines **only** a candidate framework and the evidentiary bar it would need to clear, consistent with `Standard Evolution Methodology.md` and the still-open `AO-007`.

It sits alongside, and depends on, `Governance-Manifest.md`, `Standard Evolution Methodology.md`, `Architecture-Observations.md` (`AO-007` specifically), and `ADR-Candidates.md` (the mechanism this discussion would need to feed if Reference Case evidence is later gathered).

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 31 July 2026 | Initial draft |

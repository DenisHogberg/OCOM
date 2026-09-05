# OCOM Roadmap

This roadmap reflects the actual history and current state of the project. It replaces an earlier version that described an initial plan rather than what was actually built; see the note at the end.

## Completed

**v0.1: Core Specification.** Released 21 July 2026.
Meta-model (`Meta/`), normative structural models (`Models/`), language and conformance rules (`Language/`), specification charter and principles (`Core/`), 12 business domain profiles (`Domains/`), a reference entity catalog (`Entities/`), Reference Architecture views (`Reference Architecture/`), the iGaming worked example (`Examples/`), and the Memory and AI extension layers (`Memory/`, `AI/`).

**Governance Framework.** Baseline, 22 July 2026.
10 documents at the 22 July 2026 baseline in `docs/Governance/` (the directory has since grown through the same process): the Governance Manifest, the Standard Evolution Methodology (how the Core may change), Documentation Debt, Architecture Observations, ADR Candidates, Knowledge Map, Documentation Standards, Development Readiness, Release Readiness, and Architecture Health. Reviewed and closed; further changes to this section go only through its own approved process.

**Specification v0.2 (Reading Path).** Baseline, Architecture Committee Approved with Editorial Changes, 22 July 2026.
`docs/Specification/`: a nine-chapter sequential entry point (Executive Overview through Conformance) compiling the existing normative documents above into one traceable reading path. It does not replace the granular documents and introduces no new architecture.

**Adoption Framework (M021).** 22 July 2026.
`docs/Adoption/`: a Getting Started guide, a First Pilot guide, an FAQ, and a Common Mistakes guide, restating the existing specification for a first-time reader.

**Publication Node: ocom.uno.** 3 August 2026.
Source-of-truth projections of this repository published as a machine-authoritative site: Vocabulary, Specification reading path, Comparisons, Knowledge API, Graph JSON-LD, Discovery, and llms.txt. The site is a rebuildable projection of the repository, never a second source of truth.

**Implementation Reference Case (EXAMPLES-CASE-PERFMKT-01).** 12 August 2026.
An anonymized end-to-end adoption narrative in `Examples/Implementation-Case/`: the sequence a real rollout follows (identity first, events and evidence second, the commercial layer last), including the mistakes. Distilled from real rollouts conducted under NDA; the organization, names, and details are fictionalized.

**Public Essay: "Your organization is not your software".** September 2026.
Published at ocom.uno/why: the motivation, origin, honest boundaries of applicability, and an open invitation to break the model.

## Current State

- The Standard Evolution Methodology is active. Its first Reference Case (OBS-003, *Object Attribute Lifecycle Categories*) is logged and Open, pending independent corroboration before any Core impact is considered; see `docs/Governance/Architecture-Observations.md`.
- Governance and Specification v0.2 are frozen baselines. Neither changes except through their own approved processes (editorial fixes, or ADR for architectural change).
- The canonical repository remains documentation only by design: the specification itself ships no runtime. Independent in-house implementations run privately in production under NDA. Tooling around the specification, where it exists, is developed and governed separately from it; it is not part of OCOM and places no obligation on an implementer.
- The specification's principles are applied in production settings under NDA (the author works as architect or consultant; in-house teams implement). No public case studies exist yet; converting private practice into public evidence is the explicit goal of the current phase.
- The specification has entered its public review phase: ocom.uno/why invites critique, and independent implementations are actively sought.

## Future Directions

These are directions for exploration, evidenced by observed need, not commitments or planned releases.

- Whether OBS-003 represents a real, repeated boundary: this depends on independent Reference Cases still to be submitted, not on a decision to build something.
- What a Reference Implementation and a Reference Agent would require, if and when the specification is judged stable enough to support them; not yet scoped.
- Whether further Domain-level practice (Business Intelligence, Operations, and others already present in `Domains/`) surfaces additional Reference Cases worth recording.
- Two items named in earlier planning were never realized as distinct deliverables and remain open, unscoped questions rather than committed work: an "Object Passport" concept (no corresponding document exists; `Meta/Identity.md` and `Meta/Metadata.md` cover related but not identical ground), and a dedicated Security specification (nothing currently exists under this name anywhere in the repository).
- Idea (not a governance artifact): Consider documenting the evidence thresholds and promotion criteria for Specification evolution if multiple independent governance reviews reveal recurring patterns not fully covered by Standard Evolution Methodology.
- Whether agent-facing access beyond the static Knowledge API (for example, a governed-context endpoint AI agents can consume directly) is warranted: depends on observed demand from the public review phase, not yet scoped.
- Public, independently authored case studies: the bar for claiming adoption maturity; sought, not scheduled.

---

*Note on this revision: the previous version of this roadmap listed a v0.1/v0.2/v1.0 plan drafted before this work began. Some items it named (Business Objects, Reference Architecture) were delivered, in some cases under revised terminology; others (Object Passport, Security, Enterprise Integration) were never started. This revision replaces that forward-looking plan with a record of what actually happened, per `docs/Governance/Standard Evolution Methodology.md`'s emphasis on evidence over prediction.*

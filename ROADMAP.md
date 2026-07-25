# OCOM Roadmap

This roadmap reflects the actual history and current state of the project. It replaces an earlier version that described an initial plan rather than what was actually built — see the note at the end.

## Completed

**v0.1 — Core Specification** — Released 21 July 2026.
Meta-model (`Meta/`), normative structural models (`Models/`), language and conformance rules (`Language/`), specification charter and principles (`Core/`), 12 business domain profiles (`Domains/`), a reference entity catalog (`Entities/`), Reference Architecture views (`Reference Architecture/`), the iGaming worked example (`Examples/`), and the Memory and AI extension layers (`Memory/`, `AI/`).

**Governance Framework** — Baseline, 22 July 2026.
10 documents in `docs/Governance/`: the Governance Manifest, the Standard Evolution Methodology (how the Core may change), Documentation Debt, Architecture Observations, ADR Candidates, Knowledge Map, Documentation Standards, Development Readiness, Release Readiness, and Architecture Health. Reviewed and closed; further changes to this section go only through its own approved process.

**Specification v0.2 (Reading Path)** — Baseline, Architecture Committee Approved with Editorial Changes, 22 July 2026.
`docs/Specification/` — a nine-chapter sequential entry point (Executive Overview through Conformance) compiling the existing normative documents above into one traceable reading path. It does not replace the granular documents and introduces no new architecture.

**Adoption Framework (M021)** — 22 July 2026.
`docs/Adoption/` — a Getting Started guide, a First Pilot guide, an FAQ, and a Common Mistakes guide, restating the existing specification for a first-time reader.

## Current State

- The Standard Evolution Methodology is active. Its first Reference Case (OBS-003, *Object Attribute Lifecycle Categories*) is logged and Open, pending independent corroboration before any Core impact is considered — see `docs/Governance/Architecture-Observations.md`.
- Governance and Specification v0.2 are frozen baselines. Neither changes except through their own approved processes (editorial fixes, or ADR for architectural change).
- The repository is documentation only. There is no reference implementation, SDK, or runtime, and none is in progress.

## Future Directions

These are directions for exploration, evidenced by observed need, not commitments or planned releases.

- Whether OBS-003 represents a real, repeated boundary — this depends on independent Reference Cases still to be submitted, not on a decision to build something.
- What a Reference Implementation and a Reference Agent would require, if and when the specification is judged stable enough to support them — not yet scoped.
- Whether further Domain-level practice (Business Intelligence, Operations, and others already present in `Domains/`) surfaces additional Reference Cases worth recording.
- Two items named in earlier planning were never realized as distinct deliverables and remain open, unscoped questions rather than committed work: an "Object Passport" concept (no corresponding document exists; `Meta/Identity.md` and `Meta/Metadata.md` cover related but not identical ground), and a dedicated Security specification (nothing currently exists under this name anywhere in the repository).

---

*Note on this revision: the previous version of this roadmap listed a v0.1/v0.2/v1.0 plan drafted before this work began. Some items it named (Business Objects, Reference Architecture) were delivered, in some cases under revised terminology; others (Object Passport, Security, Enterprise Integration) were never started. This revision replaces that forward-looking plan with a record of what actually happened, per `docs/Governance/Standard Evolution Methodology.md`'s emphasis on evidence over prediction.*

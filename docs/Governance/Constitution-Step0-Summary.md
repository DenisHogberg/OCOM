<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Constitution Step 0 Summary

[← Back](Architecture-Observations.md) · [↑ Up](README.md) · [Next →](Development-Readiness.md)

---
<!-- nav:end -->

# OCOM Constitution — Step 0 Architecture Decision Summary

**Document ID:** GOV-CONSTITUTION-STEP0-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 27 July 2026

---

# Purpose

`CAND-006` (`ADR-Candidates.md`) recorded the Decision to adopt the OCOM Constitution v1.0. Before Core integration could begin, five points of friction between the Constitution and the existing Specification needed resolving — three direct contradictions, two questions of scope. This document is the single record of those five resolutions: Step 0 of the Constitution's integration plan, now complete. Its purpose is to let the next stage (actual Core integration) build on these decisions rather than re-derive them.

This document does not itself change any Specification content, and is not a new ADR Candidate — it summarizes decisions already reasoned through, so they are not lost or re-litigated.

---

# Decision 1 — Memory: Entry, not Record, and Append-Only

**Problem:** Constitution §4 requires strict, unconditional immutability. `Memory/Memory Record.md`'s own Definition states a Memory Record "is immutable in identity but may evolve through controlled updates" — a real behavioral conflict, not a naming difference.

**Decision:** Memory Entry and Memory Record are the same concept. The canonical term is **Memory Entry**. Memory is append-only. A Memory Entry is immutable after creation. Corrections are represented as new Memory Entries, never as edits to existing ones.

**Rationale:** Matches the already-implemented, working architecture in OCOM Reader (`ADR-007`, `M021` — content-hash identity, `frozen=True`). Pushes the hard "is this new information or an update to the same thing" decision to read/derivation time (cheap to correct by recomputing) rather than write time (where a wrong decision destroys the original record). Makes Reconstructability (§6) and audit history automatic properties of the data rather than a separately-maintained guarantee — `Memory Record.md`'s own existing, separately-mandated `# Auditability` section is itself evidence that the current mutable model doesn't provide this for free.

**Consequences for Specification:** `Memory/Memory Record.md` needs its Definition and `# Status` sections rewritten to remove "may evolve through controlled updates," and likely renaming to align on "Memory Entry." Its `# Auditability` section becomes largely redundant once append-only is adopted. Other documents referencing "Memory Record" (at least `AI/Overview.md`) need review at integration time.

**Status:** Decided. Core integration not yet performed.

---

# Decision 2 — Evidence: MUST, Not MAY

**Problem:** Constitution §3 requires every operational fact to be traceable to Evidence. `Memory Record.md` currently states a record "may reference" Evidence — optional, not required.

**Decision:** Evidence is mandatory (**MUST**) for every operational fact. **Unknown Source / Unattributed origin is a valid Evidence state — an explicit, honest record that origin is not known — but the complete absence of an Evidence record is never permitted.**

**Rationale:** Tested directly against the four hardest cases — manual user input, LLM-derived information, import from external systems without metadata, and historical data of unknown origin. None require an actual exception; each is expressible through an appropriately (possibly minimal) typed Evidence entry, including an explicit "unknown" type for the historical-data case. Requiring existence of a record (even a minimal one) is a materially different, and stronger, requirement than requiring the record to be *reliable* — the latter remains the separate, already-existing job of the Confidence model. This keeps Evidence and Confidence independent dimensions, consistent with Constitution §3's own wording.

**Consequences for Specification:** `Memory Record.md`'s Evidence section: "may reference" → "shall reference." `Memory/Evidence Overlay.md`'s `# Evidence Sources` list needs a new, currently-absent source type for unattributed/unknown origin. `Memory/Confidence.md` needs a cross-reference note only, no structural change.

**Status:** Decided. Core integration not yet performed.

---

# Decision 3 — Object Is the Root; Entity Is a Specialization

**Problem:** Constitution §1 states Object as OCOM's universal abstraction, with Entity as one specialization among others. `Core/Principles.md` Principle 2 ("Entity-Centric Modeling") states Entity is "the primary building block of the operational model" — read on its own, a competing claim about what is foundational.

**Decision:** Entity is a specialization of Object, not an independent, competing primary abstraction. `Core/Principles.md` Principle 2 requires rewording to reflect this.

**Rationale:** Three independent lines of evidence agree. The repository's own structure: `Object` lives in `Meta/` (the foundational layer), `Entity` lives in `Models/` (models built using Meta primitives) — a structural fact, not styling. `Meta/Object.md`'s own "Examples of Objects" list already, explicitly, includes Entity as one specialization among several (Domain, Workflow, Event, Organization, ...). This project's own terminology history: `OBS-002` (already closed) records that "Business Object" was unified to "Entity" before "Object" was established as the later, more abstract Meta-root — Principle 2's current wording predates that later step and was never updated to match it. Entity's heavy real-world usage (51 files in `Entities/`, all ten rules in `Modeling-Rules.md`) reflects how much business modeling happens at the Entity level, not architectural primacy — the same distinction already applied to Organization in `CAND-005`, which is rarely instantiated yet correctly holds peer status.

**Consequences for Specification:** `Core/Principles.md` Principle 2 needs rewording. `Models/Entity.md` needs one added sentence stating the specialization relationship explicitly, matching the pattern already used in `Meta/Organization.md`. `Meta/Object.md` needs no change — already consistent. `Core/Modeling-Rules.md` and the `Entities/` catalog need no substantive change. `Reference Architecture/Object-Architecture.md` — cross-reference the already-closed `OBS-002`, do not reopen it.

**Status:** Decided. Core integration not yet performed.

---

# Decision 4 — Domain-Neutral Core: Scope Is Semantic, Not Directory-Based

**Problem:** Constitution §9 uses the bare term "Core" without definition. A literal, directory-based reading (`Core/` + `Meta/` + `Models/` only) would incorrectly exclude `Memory/` — which contains exactly the material several Canonical Principles (§3, §4, §12) are directly built from, despite being itself entirely domain-neutral.

**Decision:** "Core," for the purposes of §9, is defined by **semantic invariance across industries**, not by directory location: the set of content that would remain unchanged if OCOM were adopted by an organization in a completely different industry. This includes `Core/`, `Meta/`, `Models/`, `Language/`, `Governance/`, `Memory/`, `AI/`, `Lifecycles/`, and `Reference Architecture/`. It excludes `Entities/` (mixed, mostly domain-specific by design) and `Examples/iGaming/` (entirely domain-specific by design). `Domains/` is a genuine borderline case — most domain names (CRM, Payments, Compliance, ...) are universal business-function categories, but at least one (`Affiliate`) leans toward a specific business model — this requires ongoing, per-document judgment rather than a single blanket ruling.

**Rationale:** Verified directly against `Memory/` as the decisive counter-example to a pure directory reading. Confirmed by direct inspection that none of the newly-included directories currently contain anything industry-specific — the reclassification requires no content changes today, only a corrected boundary.

**Consequences for Specification:** §9's own text needs an explicit scope clarification written directly into the principle, not left to an external, easily-missed definition elsewhere — because §9 will be read and applied in isolation as a gating test for future proposals. `Domains/` requires continued, per-document review as an ongoing discipline, not a one-time closed decision.

**Status:** Decided. Core integration (including the §9 wording clarification) not yet performed. The `Domains/` boundary remains an operating discipline, not something this decision closes permanently.

---

# Decision 5 — Structural Isolation Is a Conformance Requirement, Not an Architecture Mandate

**Problem:** §11's wording ("architectural layer," "boundaries are enforced by architecture rather than convention") risks being read as the Constitution prescribing implementation architecture — which would conflict directly with `Core/Manifest.md`'s own Scope: "This specification does not define software architecture, APIs, implementation details or technology choices."

**Decision:** §11 is a conformance/behavioral requirement: a component's actual **capability** must never exceed its defined **responsibility**, verifiably, regardless of the technology used to achieve this. It does not prescribe how.

**Rationale:** Consistent with every other Canonical Principle's level of abstraction — all state properties, none prescribe implementation. Consistent with already-proven precedent in OCOM Reader (`M017`, `M019`'s structural-incapability discipline — itself expressed and verified as an observable property, e.g. "has no handle to Retrieval/Registry," not as a specific technology choice). Consistent with `Core/Modeling-Rules.md` Rules 9–10's own established pattern of technology-independent "shall" requirements.

**Consequences for Specification:** §11's wording needs tightening at integration time — away from "layer/architecture" language and toward "capability / verifiable absence of means" language — for the same reason as Decision 4: it will be read and applied in isolation and should not depend on external precedent to be understood correctly.

**Status:** Decided. Core integration not yet performed.

---

# Final Verdict — Is the Constitution Ready for Integration?

**Yes.** Every item that began Step 0 as an open architectural question now has a recorded decision. Nothing below is a re-opened question — each is a scoped, well-specified integration task.

**Remaining work, as integration tasks:**

1. Decide and authorize the Constitution's physical location in Core (proposed earlier: `Core/Constitution.md`, `Document ID: Core-00`, positioned first in the Core nav order) — a placement decision, not an open architectural question.
2. Rewrite `Memory/Memory Record.md` (Definition, `# Status`, `# Evidence`, `# Auditability`) per Decisions 1 and 2.
3. Add an explicit "Unknown Source" / "Unattributed" entry to `Memory/Evidence Overlay.md`'s `# Evidence Sources` list per Decision 2.
4. Reword `Core/Principles.md` Principle 2 per Decision 3.
5. Add one sentence to `Models/Entity.md` per Decision 3.
6. Add an explicit scope clarification into Constitution §9's own text per Decision 4.
7. Tighten Constitution §11's wording toward capability/conformance language per Decision 5.
8. Audit remaining cross-references to "Memory Record" and to the current Principle 2 wording across the wider Specification (not exhaustively done in Step 0).
9. Treat the `Domains/` boundary (Decision 4) as an ongoing, per-document discipline whenever those documents are next touched — not a task with a completion state.

Per the same two-step discipline already used throughout this Specification's governance (`CAND-003`, `CAND-005`): this document records that Step 0 is complete. Performing the integration tasks above is Step 1, and requires its own separate, explicit authorization — not implied by this summary.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 27 July 2026 | Initial summary — Step 0 complete, five decisions recorded (Memory, Evidence, Object/Entity, Domain-Neutral Core scope, Structural Isolation) |

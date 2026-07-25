# Frequently Asked Questions

**Document ID:** ADOPTION-FAQ-01

**Status:** Informative

**Version:** 0.1

---

## Do I need to rewrite my systems?

No. OCOM describes the operational model, not the software that implements it. "Technology implements the model but never defines it" *(`Core/Manifest.md`, Design Philosophy)*, and the model is explicitly required to stay separable from software architecture, databases, APIs, and infrastructure *(`Core/Principles.md`, Principle 6 — Separation of Model and Implementation)*. You can model your operations in OCOM terms while your existing systems keep running unchanged.

## Do I need Event Sourcing?

No. An Event in OCOM is "an immutable record describing something that has occurred" *(`Models/Event.md`)* — that's a modeling concept, not a storage architecture. OCOM does not prescribe how (or whether) you persist events, and explicitly leaves implementation technology, including storage engines, undefined *(see the Independence clauses throughout `Meta/` and `Models/`)*.

## Do I need to use AI?

No. Core Conformance does not require AI in any form. `docs/Specification/03 Core Concepts.md` states plainly that "AI-specific concepts (Agent, Context, Knowledge, Memory) or runtime/execution semantics" are deliberately not part of the Core — they are a separate, optional layer (`docs/AI/`) you can adopt later, or never.

## Can I adopt OCOM gradually?

Yes. Evolvability is one of the ten Design Principles: "The framework shall support organizational evolution without requiring redesign of the underlying operational model" *(`Core/Principles.md`, Principle 10)*. Nothing about OCOM requires an all-at-once adoption — see `First Pilot.md` for a deliberately small starting scope.

## Can I use only part of OCOM?

Yes, and this is formally supported, not just tolerated. `Language/Conformance.md` defines three Conformance Levels: **Core Conformance** (the mandatory requirements only), **Extended Conformance** (Core plus documented extensions), and **Profile Conformance** (a bounded, named subset of the specification). You do not need Memory, AI, or every Meta concept to have a conforming model — Core Conformance alone is a valid, complete destination.

## How is OCOM different from BPMN, DDD, and a CMDB?

These comparisons are for orientation only — OCOM's own documents do not define themselves against these tools, so treat this as a helpful analogy, not a normative statement.

- **BPMN** models processes — the flow of activity. OCOM models Entities first: "Every operational concept shall be represented through identifiable entities" *(`Core/Principles.md`, Principle 2 — Entity-Centric Modeling)*, and treats a Workflow as something that acts *on* Entities, not the primary subject of the model *(`Models/Workflow.md`)*. A process diagram answers "what happens." An OCOM model answers "what exists, and what state is it in."
- **DDD (Domain-Driven Design)** shares vocabulary — Entity, Domain — because both trace to the same general modeling tradition, but the resemblance stops at the words. In DDD, Entities and bounded contexts are typically project-specific design choices made by a single team. In OCOM, Entity, Domain, and their required characteristics are fixed by the specification itself, so that the same concept means the same thing across teams and organizations *(`Core/Principles.md`, Principle 8 — Semantic Consistency)*.
- **CMDB** (Configuration Management Database) typically tracks IT assets and their configuration relationships. OCOM's Entities are not limited to IT assets — a Customer, a Campaign, and a Payment are as valid as a server — and OCOM is a specification for describing operational meaning, not a database product or schema *(`Core/Manifest.md`, Abstract)*.

---

*Source: answers restate `Core/Manifest.md`, `Core/Principles.md`, `Models/Event.md`, `Models/Workflow.md`, `Language/Conformance.md`, and `docs/Specification/03 Core Concepts.md`. The BPMN/DDD/CMDB comparison is interpretive orientation, not a claim made anywhere in the normative specification.*

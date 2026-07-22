<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Knowledge Map

[← Back](Governance-Manifest.md) · [↑ Up](README.md) · [Next →](Release-Readiness.md)

---
<!-- nav:end -->

# Knowledge Map

**Document ID:** GOV-KNOWLEDGE-MAP-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document is the map of the OCOM Specification: how its sections and concepts relate to one another, independent of directory hierarchy.

Repository navigation (breadcrumbs, README indexes) shows folder structure. This document shows meaning.

---

# Repository Map

```
docs/
├── AI/                      — AI agents, context, evaluation, knowledge, prompts, tools
├── Core/                    — Governance, manifest, modeling rules, naming, principles, terminology, versioning
├── Domains/                 — 12 business domains + Common
├── Entities/                — Core business entities
├── Examples/                — Worked examples (iGaming)
├── Governance/               — This section
├── Language/                — Notation, syntax, schema, vocabulary, conformance
├── Lifecycles/               — Cross-cutting lifecycle patterns
├── Memory/                  — Layered memory, evidence, confidence, retention
├── Meta/                    — Foundational meta-model constructs
├── Models/                  — Normative structural models
├── Reference Architecture/  — Illustrative enterprise architecture views
└── Workflows/                — Planned (not yet populated)
```

---

# Concept Map

Established relationships between foundational concepts, as currently stated in the specification:

- **Object** (`Meta/Object.md`) is the universal abstraction. Meta declares 14 concepts as specializations of Object: Entity, Domain, Workflow, Event, Lifecycle, Agent, Tool, Prompt, Context, Knowledge, Memory Record, Policy, Registry, Contract.
- **Entity** (`Models/Entity.md`) is explicitly a specialization of Object (cross-reference added during v0.1 stabilization).
- **Relationship** (`Meta/Relationship.md`, `Models/Relationship.md`) is a governed, meaningful association — explicitly distinct from **Reference** (`Meta/Reference.md`), which carries no business meaning.
- **Domain** (`Models/Domain.md`) governs one or more Entities; every Entity belongs to exactly one primary Domain.
- **Capability**, **Policy**, **Contract** are Meta-level concepts consistently referenced by Domain-level documents (each Domain's `*_Policies.md`, `*_Capabilities.md` explicitly cites "Meta specification" as the source of semantics).
- **Context**, **Knowledge**, **Memory Record** are explicitly and mutually differentiated in `AI/Context/Context.md`, `AI/Knowledge/Knowledge.md`, and `Memory/Memory Record.md`.

---

# Traceability Matrix

Linear reading order of the chain:

```
Meta
  ↓
Core
  ↓
Models
  ↓
Reference Architecture
  ↓
Examples
  ↓
Reference Implementation
  ↓
Reference Agent
```

Governance is not a stage in this chain — it is a cross-cutting layer that applies to every stage at once:

```
                 Governance
                      │
 ┌────────────────────┼────────────────────┐
 │                    │                    │
Meta ─ Core ─ Models ─ Reference Architecture ─ Examples
 │                    │                    │
 └────────────────────┼────────────────────┘
                      │
         Reference Implementation
                      │
               Reference Agent
```

| Concept | Meta | Core | Models | Reference Architecture | Examples | Reference Implementation | Reference Agent |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Object / Entity | ✅ | — | ✅ | ✅ | ✅ | ⬜ Future Work | ⬜ Future Work |
| Relationship | ✅ | — | ✅ | ✅ | ✅ | ⬜ Future Work | ⬜ Future Work |
| Lifecycle | — | — | ✅ | — | ✅ | ⬜ Future Work | ⬜ Future Work |
| Capability | ✅ | — | — | — | ✅ | ⬜ Future Work | ⬜ Future Work |
| Context | — | — | — | — | — | ⬜ Future Work | ⬜ Future Work |

`—` means no dedicated document exists at that layer for the concept (not necessarily a gap — some concepts are not expected at every layer). `⬜ Future Work` means the layer itself does not exist yet in the repository (see `Documentation-Debt.md`, FW-003/FW-004).

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial map |
| 0.1 | 22 July 2026 | Added cross-cutting Governance diagram |

# OCOM Specification v0.2 — Core Concepts

**Document ID:** SPEC-03

**Status:** Draft

**Version:** 0.2

---

## Purpose

This chapter orients the reader before the detailed Meta Model (Chapter 4) and Object Model (Chapter 5). It introduces, at a glance, the concepts that everything else in this specification is built from.

## Object

**Object** is the universal abstraction within OCOM. It is an identifiable and governable element that exists within the operational model — something that can be described, managed, related, evaluated, or governed throughout its lifecycle, independently of implementation technology or business domain.

All managed concepts defined by this specification — Entity, Domain, Workflow, Event, Lifecycle, Policy, Contract, and others — are specializations of Object.

## Entity

**Entity** is the primary operational construct built from Object. Every operational model defined by this specification is composed of entities and the relationships between them. An entity possesses identity, belongs to exactly one primary Domain, has defined ownership, contains attributes, defines one or more states, and follows a lifecycle.

## Domain

**Domain** is an operational boundary responsible for governing one or more entities. A Domain organizes responsibility rather than organizational structure — it represents *what* is governed, not *who* performs the work.

## Relationship and Reference

**Relationship** is a governed, semantic association between Objects — it expresses meaning ("Campaign targets Player"). **Reference** is a directed association that identifies a target Object without carrying semantic meaning. The two are deliberately distinct: a Reference is a pointer, a Relationship carries business meaning.

## Lifecycle, State, and Event

**State** is a discrete operational condition describing an entity's status at a point in time. **Lifecycle** is the complete set of states and permitted state transitions that define an entity's operational existence — every entity has exactly one. **Event** is an immutable record of something that has occurred; events describe facts and do not themselves define behavior.

## Workflow

**Workflow** is a structured sequence of operational activities that performs defined state transitions. Where Relationship and Event describe structure and facts, Workflow represents behavior.

## Capability, Policy, and Contract

**Capability** is a governed description of an ability possessed or provided by an Object — potential functionality, not a specific execution. **Policy** is a governed rule defining expected behavior or constraints applicable to one or more Objects. **Contract** is a governed agreement between two or more Objects specifying the conditions under which they interact.

## How These Concepts Relate

```text
Object
  |
  |-- is specialized by ----> Entity, Domain, Workflow, Event, Lifecycle,
  |                            Policy, Contract, Registry, ...
  |
  |-- is described by ------> Identity, Metadata, Classification, Ownership
  |
  |-- is connected by ------> Relationship (meaningful) / Reference (structural)
  |
  `-- is governed by -------> Policy, Constraint, Contract
```

An Entity belongs to a Domain, follows a Lifecycle expressed through States, is affected by Events, participates in Relationships with other Entities, and may be acted upon by Workflows.

## What Is Deliberately Not Introduced Here

This specification does not define AI-specific concepts (Agent, Context, Knowledge, Memory) or runtime/execution semantics as part of the Core. Where they exist elsewhere in the repository, they are extensions, not prerequisites for understanding Chapters 4–6.

---

*Source: synthesized from `Meta/Object.md`, `Meta/Relationship.md`, `Meta/Reference.md`, `Meta/Capability.md`, `Meta/Policy.md`, `Meta/Contract.md`, `Models/Entity.md`, `Models/Domain.md`, `Models/Relationship.md`, `Models/Event.md`, `Models/State.md`, `Models/Lifecycle.md`, `Models/Workflow.md`. No new concepts introduced.*

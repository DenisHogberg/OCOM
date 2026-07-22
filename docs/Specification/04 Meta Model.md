# OCOM Specification v0.2 — Meta Model

**Document ID:** SPEC-04

**Status:** Draft

**Version:** 0.2

---

## Purpose

The Meta Model defines the foundational, technology- and domain-independent abstractions shared across the entire specification. Every other document — Object Model, Domain profiles, Reference Architecture — is built on these definitions without redefining them.

## Object — The Universal Abstraction

An **Object** is an identifiable and governable element that exists within the operational model. Objects are independent of implementation technologies and business domains.

Every Object is defined by these core characteristics: **Identity, Metadata, Classification, Relationships, Lifecycle, Ownership, Governance.** Objects may additionally support Evaluation, Versioning, Capabilities, Policies, Contracts, and Constraints.

> **Note on terminology.** "Governance" here means the oversight and accountability applied to an individual Object. Chapter 7 uses the same word for a different, unrelated sense: how the OCOM Specification itself evolves over time. The two are not connected.

**Architectural Role:** Object is the universal abstraction within OCOM. All managed concepts defined by the specification — including Entity, Domain, Workflow, Event, Lifecycle, Policy, Registry, and Contract — are specializations of Object. Specifications may extend Object but **shall** preserve its core characteristics.

## Identity

Identity is the persistent and unique representation of an Object. Identity distinguishes one Object from all others regardless of changes to its metadata, state, relationships, or implementation, and **shall** remain stable throughout the Object's lifetime.

## Metadata

Metadata is structured information describing the characteristics, context, or management attributes of an Object. It supplements an Object but does not define its identity or operational state.

## Classification

Classification is the assignment of one or more descriptive categories to an Object, enabling grouping, filtering, governance, and operational organization without altering the Object's identity.

## Relationship and Reference

A **Relationship** is a governed semantic association between Objects — it expresses how Objects are connected within the operational model and, unlike a Reference, conveys business meaning. Every Relationship defines an Identifier, Source Object, Target Object, and Relationship Type; it may additionally define direction, cardinality, status, and constraints.

A **Reference** is a directed association from one Object to another. A Reference identifies a target Object but does not define the semantic nature of the association — that meaning, if any, is defined separately by Relationship.

## Capability

A Capability is a governed description of an ability possessed or provided by an Object. Capabilities represent potential functionality rather than specific executions, and may support one or more business objectives.

## Policy

A Policy is a governed set of rules defining expected behavior or constraints applicable to one or more Objects. Policies express organizational intent independently of implementation technology, and may be mandatory, recommended, or optional.

## Contract

A Contract is a governed agreement between two or more Objects. It specifies the conditions under which participating Objects interact, exchange information, perform activities, or provide Capabilities — the rules governing an interaction, not the interaction itself.

## Constraint

A Constraint is a governed condition that restricts or requires specific characteristics, states, or behaviors. A Constraint defines *what must remain true*, not *how it is enforced*.

## Ownership

Ownership is the assignment of responsibility for one or more managed Objects — the individual, team, organizational unit, or system accountable for governing an Object during all or part of its lifecycle. Ownership does not necessarily imply authorship or implementation responsibility.

## Registry

A Registry is a managed collection of identifiable Objects, organized according to defined governance rules, providing controlled access while preserving identity, traceability, and operational consistency.

## Conformance

A compliant implementation **shall** ensure that every managed Object possesses a unique identity, supports metadata, can participate in relationships, supports governance, preserves traceability, and remains technology independent.

---

*Source: compiled from `Meta/Object.md`, `Meta/Identity.md`, `Meta/Metadata.md`, `Meta/Classification.md`, `Meta/Relationship.md`, `Meta/Reference.md`, `Meta/Capability.md`, `Meta/Policy.md`, `Meta/Contract.md`, `Meta/Constraint.md`, `Meta/Ownership.md`, `Meta/Registry.md`. Full detail — including Design Principles, Auditability, and Independence clauses for each concept — remains in those source documents; this chapter is a normative summary, not a replacement. (Committee Review, 22 July 2026: added a terminology note disambiguating "Governance" from Chapter 7's unrelated use of the same word; no definition changed.)*

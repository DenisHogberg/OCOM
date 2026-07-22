# OCOM Specification v0.2 — Object Model

**Document ID:** SPEC-05

**Status:** Draft

**Version:** 0.2

---

## Purpose

Where the Meta Model (Chapter 4) defines the abstract vocabulary, the Object Model defines the normative *structure* that vocabulary takes when used to build an operational model. A **Model** is an organized collection of Entities, Domains, Relationships, States, Lifecycles, Workflows, and Events that together describe an operational system — representing operational reality, not software implementation.

## Entity

An Entity is a specialization of Object and the primary operational construct of this specification: an identifiable operational object that represents something with business meaning, existing independently of software implementations.

Every Entity **shall**:

- possess a unique identity;
- have operational meaning;
- belong to exactly one primary Domain;
- have defined ownership;
- contain attributes (each with a name, meaning, data type, and optional constraints);
- define one or more states;
- define a lifecycle;
- participate in relationships.

The minimum conforming Entity consists of: Identifier, Name, Domain, Owner, Attributes, State, Lifecycle.

An Entity **shall not** exist without identity, without ownership, without a lifecycle, or belong to multiple primary Domains.

## Domain

A Domain is an operational boundary responsible for governing one or more Entities. A Domain organizes responsibility rather than organizational structure — it represents what is governed, not who performs the work. Domains do not own other Domains.

## Relationship

A Relationship is an explicit operational association between two or more Entities. It defines structural connections and does not itself represent operational behavior. Every Relationship **shall** connect identifiable Entities, have a defined type, and define cardinality; direction **shall** be explicit whenever operational meaning depends on it.

> **Editorial note.** `Meta/Relationship.md` (Chapter 4) frames Relationship in terms of the business *meaning* it conveys ("unlike a Reference, a Relationship conveys business meaning"), while `Models/Relationship.md` (this chapter) frames it as a *structural* connection that "does not represent operational behavior." Read together, these are not stated as contradictory in the source documents — meaning and behavior are different properties, and a structural connection can still carry business meaning without describing behavior. This chapter records the difference in emphasis rather than resolving it, per editorial policy: apparent tensions between source documents are flagged, not corrected, in this reading path.

## Event

An Event is an immutable record describing something that has occurred within the operational model. Events describe facts; they do not define behavior and do not replace state.

## State

A State is a discrete operational condition describing an Entity's status at a specific point in time. Every Entity exists in exactly one State at any given moment unless explicitly defined otherwise.

## Workflow

A Workflow is a structured sequence of operational activities that performs defined state transitions according to the rules of this specification. A Workflow represents behavior rather than structure — the counterpart to Relationship (structure) and Event (fact).

## Relationship to the Meta Model

An Entity is a specialization of Object as defined by the Meta Model. It shares the Identity, Ownership, Relationship, and Lifecycle principles defined for Object, and extends them with the Domain, Attributes, and State requirements defined in this chapter.

## Conformance

An Entity, Domain, Relationship, Event, State, or Workflow conforms to this specification only if all mandatory requirements defined for it are satisfied.

---

*Source: compiled from `Models/Model.md`, `Models/Entity.md`, `Models/Domain.md`, `Models/Relationship.md`, `Models/Event.md`, `Models/State.md`, `Models/Workflow.md`. The Entity↔Object cross-reference reflects the explicit link added to `Models/Entity.md` during v0.1 stabilization. (Committee Review, 22 July 2026: "shall never," inherited verbatim from `Models/Entity.md`, normalized to "shall not" to match Chapter 1's keyword glossary; no requirement changed.)*

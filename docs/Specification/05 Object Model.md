# OCOM Specification v1.0 — Object Model

**Document ID:** SPEC-05

**Status:** Draft

**Version:** 1.0

**Last Updated:** 18 September 2026

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
- participate in relationships;
- be governed by the rules of this specification.

The minimum conforming Entity consists of: Identifier, Name, Domain, Owner, Attributes, State, Lifecycle.

An Entity **shall not** exist without identity, without ownership, without a lifecycle, belong to multiple primary Domains, or have ambiguous meaning.

## Domain

A Domain is an operational boundary responsible for governing one or more Entities. A Domain organizes responsibility rather than organizational structure — it represents what is governed, not who performs the work. A Domain may govern multiple Entities; primary governance **shall not** be shared between Domains, and relationships between Domains define cooperation but do not transfer governance.

## Relationship

A Relationship is an explicit operational association between two or more Entities. It defines structural connections and does not itself represent operational behavior. Every Relationship **shall** connect identifiable Entities, have a defined type, and define cardinality; direction **shall** be explicit whenever operational meaning depends on it. A Relationship **shall not** connect undefined Entities, have ambiguous meaning, duplicate another Relationship without justification, or exist without a defined type. This chapter's Relationship specializes the Relationship defined in `Meta/Relationship.md`, whose participants are Objects, for the case in which every participant is an Entity; a Relationship with a participant that is not an Entity, including an Organization, is governed by `Meta/Relationship.md` (`CAND-016`).

> **Editorial note.** `Meta/Relationship.md` (Chapter 4) frames Relationship in terms of the business *meaning* it conveys ("unlike a Reference, a Relationship conveys business meaning"), while `Models/Relationship.md` (this chapter) frames it as a *structural* connection that "does not represent operational behavior." Read together, these are not stated as contradictory in the source documents — meaning and behavior are different properties, and a structural connection can still carry business meaning without describing behavior. This chapter records the difference in emphasis rather than resolving it, per editorial policy: apparent tensions between source documents are flagged, not corrected, in this reading path.
>
> **Editorial note (17 September 2026).** The difference recorded above was settled on 16 September 2026 by `CAND-016`: `Meta/Relationship.md` is the canonical definition of Relationship and `Models/Relationship.md` its specialization for Entity participants, as the paragraph above now compiles from the latter's Purpose. The earlier note is kept as the record of what this reading path flagged.

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

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.2 | 22 July 2026 | Compiled reading path, approved by the Architecture Committee with editorial changes (`Specification/Committee Review Package.md`). |
| 0.2 | 22 July 2026 | Committee Review: "shall never," inherited verbatim from `Models/Entity.md`, normalized to "shall not" to match Chapter 1's keyword glossary; no requirement changed. |
| 1.0 | 17 September 2026 | "shall never", inherited verbatim from `Models/Domain.md`, normalized to "shall not" as the Committee Review of 22 July 2026 directed for this chapter; no requirement changed. Relationship section compiles the specialization sentence `Models/Relationship.md` gained under `CAND-016`, with a dated editorial note closing the earlier one; the Domain section's unsourced sentence about Domains owning Domains replaced by the governance rules of `Models/Domain.md`; every other sentence verified against its `Models/` source as of this date. |
| 1.0 | 18 September 2026 | Three obligations its sources carry and this chapter did not: the ninth item of `Models/Entity.md`'s "Every Entity shall" list, the fifth of its prohibitions, and the four prohibitions of `Models/Relationship.md`. The traceability check of 17 September 2026 ran forward, from chapter to source, so an obligation the chapter never compiled was invisible to it; recorded as `AO-077`. No requirement changed in any source document. |

---

*Source: compiled from `Models/Model.md`, `Models/Entity.md`, `Models/Domain.md`, `Models/Relationship.md`, `Models/Event.md`, `Models/State.md`, `Models/Workflow.md`. The Entity↔Object cross-reference reflects the explicit link added to `Models/Entity.md` during v0.1 stabilization. (Committee Review, 22 July 2026: "shall never," inherited verbatim from `Models/Entity.md`, normalized to "shall not" to match Chapter 1's keyword glossary; no requirement changed.) (17 September 2026: recompiled as v1.0 against the canonical documents as of this date; see Revision History)*

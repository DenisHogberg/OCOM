# OCOM Specification v1.0 — Lifecycle Model

**Document ID:** SPEC-06

**Status:** Draft

**Version:** 1.0

**Last Updated:** 17 September 2026

---

## Purpose

This chapter defines how Entities change over time. It sits between the structural Object Model (Chapter 5) and the sections outside the Core chapters (1 to 8) that apply the Core to concrete scenarios: `docs/Domains/`, `docs/Entities/`, `docs/Lifecycles/`, `docs/Examples/`, `docs/Workflows/` and `docs/Reference Architecture/`, which the Committee Review of 22 July 2026 called Reference Material. Each of those carries its own Status field, Draft (normative) or Informative, per `Governance/Documentation-Standards.md`. Lifecycle itself is normative; specific lifecycle patterns (Commercial, Financial, Operational, ...) are illustrations of it.

## Definition

A Lifecycle is the complete set of States and permitted State Transitions that define the operational existence of an Entity. Every Entity **shall** have exactly one Lifecycle. A Lifecycle is a reusable operational model describing the allowed States and valid State Transitions of an Entity; it defines how an Entity evolves over time while preserving operational consistency.

## States

A Lifecycle **shall** define one and only one initial State, and may define one or more terminal States; a terminal State represents the completion or permanent termination of the Entity Lifecycle. Each State **shall** have a unique meaning within the Lifecycle. At any point in time an Entity **shall** occupy exactly one valid State defined by its Lifecycle.

## Transitions

A Transition defines movement from one State to another. Transitions **shall** be explicitly defined; undefined transitions are invalid. A Lifecycle **shall not** contain multiple initial States, contain unreachable States, contain undefined Transitions, or permit ambiguous State progression.

## Lifecycle Ownership

Every Entity **shall** belong to exactly one primary Domain, and the Domain governs ownership, responsibility, and operational rules (`Models/Entity.md`). A Domain's responsibilities include ensuring lifecycle governance, and primary governance **shall not** be shared between Domains (`Models/Domain.md`).

## Events and Lifecycle

An Event is an immutable record describing something that has occurred within the operational model; Events do not define behavior (`Models/Event.md`). A State does not define how transitions occur; transitions are defined by the Entity Lifecycle (`Models/State.md`). Which transitions are valid is therefore the Lifecycle's role alone.

## Relationship to Domain-Specific Lifecycle Patterns

This chapter defines Lifecycle as a primitive. The specification's Reference Material demonstrates typical lifecycle patterns for recurring business scenarios — for example, a Commercial Lifecycle or a Campaign Lifecycle with states such as Draft, Approved, Active, Completed, Suspended, or Cancelled. Those patterns **apply** this chapter's rules; they do not extend or modify them.

## Conformance

A Lifecycle conforms to this specification only if all mandatory requirements defined in `Models/Lifecycle.md` are satisfied, among them that no State it defines is unreachable and that no Transition is undefined.

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.2 | 22 July 2026 | Compiled reading path, approved by the Architecture Committee with editorial changes (`Specification/Committee Review Package.md`). |
| 0.2 | 22 July 2026 | Committee Review: added an inline definition of "Reference Material" at first use, per committee direction; no source document changed. |
| 1.0 | 17 September 2026 | "shall never", inherited verbatim from `Models/Domain.md`, normalized to "shall not" as the Committee Review of 22 July 2026 directed for Chapter 5; no requirement changed. Purpose no longer calls the Domains, Entities and Lifecycles sections non-normative (their Status fields decide, per `Documentation-Standards.md`); Definition, States, Transitions and Conformance restated from `Models/Lifecycle.md`, `Models/State.md` and `Lifecycles/Lifecycles.md` ("shall never" normalized to "shall not" as Chapter 5 did on 22 July 2026); Lifecycle Ownership now compiles `Models/Entity.md` and `Models/Domain.md` instead of an unsourced rule, and Events and Lifecycle compiles `Models/Event.md` and `Models/State.md`; Source line extended accordingly. |

---

*Source: compiled from `Models/Lifecycle.md`, `Models/State.md`, `Lifecycles/Lifecycles.md`, `Models/Entity.md`, `Models/Domain.md`, `Models/Event.md`. Domain-specific lifecycle patterns (Commercial, Financial, Operational, Organizational, Content) remain in `docs/Lifecycles/` as Reference Material, per the Part I / Part II separation established for v0.2. (Committee Review, 22 July 2026: added an inline definition of "Reference Material" at first use, per committee direction; no source document changed.) (17 September 2026: recompiled as v1.0 against the canonical documents as of this date; see Revision History)*

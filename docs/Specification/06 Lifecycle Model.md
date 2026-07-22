# OCOM Specification v0.2 — Lifecycle Model

**Document ID:** SPEC-06

**Status:** Draft

**Version:** 0.2

---

## Purpose

This chapter defines how Entities change over time. It sits between the structural Object Model (Chapter 5) and the domain-specific lifecycle patterns found in the Reference Material — the non-normative, illustrative sections of the repository (`docs/Domains/`, `docs/Entities/`, `docs/Lifecycles/`, `docs/Examples/`, `docs/Workflows/`, `docs/Reference Architecture/`) that demonstrate the Core applied to concrete scenarios, as distinct from the normative Core chapters (1–8) themselves. Lifecycle itself is normative; specific lifecycle patterns (Commercial, Financial, Operational, ...) are illustrations of it.

## Definition

A Lifecycle is the complete set of States and permitted State Transitions that define the operational existence of an Entity. Every Entity **shall** have exactly one Lifecycle. A Lifecycle is a reusable operational model describing how an Entity evolves over time while preserving operational consistency.

## States

A State represents the current operational condition of an Entity. Every Entity exists in exactly one State at any given moment unless explicitly defined otherwise.

## Transitions

The Lifecycle specifies all valid state transitions for the Entities that follow it. Transitions not defined by the Lifecycle **are invalid** — an Entity **shall not** move between states outside its declared Lifecycle.

## Lifecycle Ownership

Every Entity shall have one owning Domain responsible for its Lifecycle. Lifecycle transitions are governed by that Domain's applicable Policies.

## Events and Lifecycle

Operational Events may affect an Entity's progression through its Lifecycle, but Events describe facts — they record that a transition occurred; they do not themselves define which transitions are valid. That is the Lifecycle's role alone.

## Relationship to Domain-Specific Lifecycle Patterns

This chapter defines Lifecycle as a primitive. The specification's Reference Material demonstrates typical lifecycle patterns for recurring business scenarios — for example, a Commercial Lifecycle or a Campaign Lifecycle with states such as Draft, Approved, Active, Completed, Suspended, or Cancelled. Those patterns **apply** this chapter's rules; they do not extend or modify them.

## Conformance

A Lifecycle conforms to this specification only if every state it defines is reachable through a valid transition path, and no transition exists that is not explicitly declared.

---

*Source: compiled from `Models/Lifecycle.md`, `Models/State.md`, `Lifecycles/Lifecycles.md`. Domain-specific lifecycle patterns (Commercial, Financial, Operational, Organizational, Content) remain in `docs/Lifecycles/` as Reference Material, per the Part I / Part II separation established for v0.2. (Committee Review, 22 July 2026: added an inline definition of "Reference Material" at first use, per committee direction; no source document changed.)*

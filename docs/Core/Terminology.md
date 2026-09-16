<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Terminology

[← Back](Principles.md) · [↑ Up](README.md) · [Next →](Versioning.md)

---
<!-- nav:end -->

# Terminology

**Document ID:** Core-03

**Status:** Draft

**Version:** 0.2

**Last Updated:** 16 September 2026

---

# Purpose

This document indexes the normative terminology used throughout the specification.

Each term is defined by the document named beside it. This index restates that document's Definition sentence verbatim and adds nothing to it; where the two ever differ, the named document governs, per the Single Source of Truth principle in `Core/Principles.md` and the Decision recorded as `CAND-015`. Terms the Constitution uses that no document yet defines are listed under Reserved Terms at the end, each with the observation that tracks it, so that every Constitution term is locatable here even where it is not yet defined.

---

# Object

An Object is an identifiable and governable element that exists within the operational model.

Defined in `Meta/Object.md`.

---

# Organization

An Organization is an identifiable and governable Object that represents an independent participant within the operational ecosystem.

Defined in `Meta/Organization.md`; a specialization of Object at the same architectural level as Entity, Domain and Workflow, per `CAND-005`.

---

# Entity

An Entity is an identifiable operational object that represents something with business meaning.

Defined in `Models/Entity.md`.

---

# Domain

A Domain is an operational boundary responsible for governing one or more Entities.

Defined in `Models/Domain.md`, the canonical definition per `CAND-015`; `Domains/Common/Domain.md` is informative.

---

# Workflow

A Workflow is a structured sequence of operational activities that performs defined State Transitions according to the rules of this specification.

Defined in `Models/Workflow.md`.

---

# State

A State is a discrete operational condition that describes the status of an Entity at a specific point in time.

Defined in `Models/State.md`.

---

# Lifecycle

A Lifecycle is the complete set of States and permitted State Transitions that define the operational existence of an Entity.

Defined in `Models/Lifecycle.md`.

---

# Ownership

Ownership is the assignment of responsibility for one or more managed Objects.

Defined in `Meta/Ownership.md`.

---

# Owner

The party named by the Owner field of an Ownership assignment.

Described in `Meta/Ownership.md`, which lists Owner among the fields every Ownership assignment shall define. See Ownership.

---

# Relationship

A Relationship is an explicit operational association between two or more Entities.

Defined in `Models/Relationship.md`. `Meta/Relationship.md` separately defines a Relationship as a governed semantic association between Objects; the difference in participant types is tracked as `AO-002`.

---

# Event

An Event is an immutable record describing something that has occurred within the operational model.

Defined in `Models/Event.md`.

---

# Attribute

Attributes describe the properties of an Entity.

Described in `Models/Entity.md`, section Attributes; no document carries a Definition section for Attribute.

---

# Identity

Identity is the persistent and unique representation of an Object.

Defined in `Meta/Identity.md`.

---

# Identifier

An Identifier is the syntactic representation of an Identity within an OCOM model.

Defined in `Language/Identifier Syntax.md`.

---

# Metadata

Metadata is structured information that describes the characteristics, context, or management attributes of an Object.

Defined in `Meta/Metadata.md`.

---

# Classification

Classification is the assignment of one or more descriptive categories to an Object.

Defined in `Meta/Classification.md`.

---

# Reference

A Reference is a directed association from one Object to another.

Defined in `Meta/Reference.md`.

---

# Capability

A Capability is a governed description of an ability possessed or provided by an Object.

Defined in `Meta/Capability.md`.

---

# Policy

A Policy is a governed set of rules that defines expected behavior or constraints applicable to one or more Objects.

Defined in `Meta/Policy.md`.

---

# Contract

A Contract is a governed agreement between two or more Objects.

Defined in `Meta/Contract.md`.

---

# Constraint

A Constraint is a governed condition that restricts or requires specific characteristics, states, or behaviors.

Defined in `Meta/Constraint.md`.

---

# Registry

A Registry is a managed collection of identifiable Objects organized according to defined governance rules.

Defined in `Meta/Registry.md`.

---

# Model

A Model is an organized collection of Entities, Domains, Relationships, States, Lifecycles, Workflows, and Events that together describe an operational system.

Defined in `Models/Model.md`.

---

# Memory

Memory is the operational capability to retain information beyond a single execution context.

Defined in `Memory/Overview.md`.

---

# Memory Record

A Memory Record represents a single retained fact, observation, inference, or decision together with its operational metadata.

Defined in `Memory/Memory Record.md`. `Core/Constitution.md` names this concept Memory Entry; `Constitution-Step0-Summary.md` Decision 1 rules the two names one concept, and the pending rename is tracked as `GAP-004`.

---

# Confidence

Confidence is a measurable assessment of the likelihood that a Memory Record accurately represents reality.

Defined in `Memory/Confidence.md`.

---

# Knowledge

Knowledge is governed, persistent, and reusable organizational understanding.

Defined in `AI/Knowledge/Knowledge.md`; derived from Memory per `Core/Constitution.md` Principle 5 and `CAND-014`.

---

# Context

Context is the collection of information made available to an AI Agent during the execution of a specific task.

Defined in `AI/Context/Overview.md`.

---

# Specification

The complete collection of normative documents defining the operational modeling framework.

Defined here; no other document carries a Definition for the term.

---

# Reserved Terms

`Core/Constitution.md` uses the following terms for which no document in this specification carries a Definition. Each is reserved for a future version in the sense `Governance/Documentation-Standards.md` gives that word, and the observation that tracks it is named, so that the term is locatable here even where it is not yet defined. Nothing in this section defines anything.

- **Evidence** (Canonical Principle 3): Definition reserved in `Memory/Evidence Overlay.md`; tracked as `AO-021` and `AO-053`.
- **World Model** (Canonical Principles 5 and 6): its relationship to Memory and Knowledge is decided by `CAND-014` Layer 1; the document itself is Layer 2 and not yet authored.
- **Autonomy level** (Canonical Principles 7 and 14): no scale is defined anywhere; tracked as `AO-067`.
- **Provenance** (Canonical Principle 12): three AI documents carry a Provenance section and none defines the term; tracked as `AO-068`.
- **Static World Modelling** and **Dynamic World Modelling** (Canonical Principle 8): defined nowhere; tracked as `AO-068`.
- **Adapter**, **Normalizer**, **Identity Resolution threshold**, **Source trust** and **Concept namespace** (Architectural Principles): implementation vocabulary defined at no tier; tracked as `AO-024`.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 25 July 2026 | Corrected Organization definition to align with ADR CAND-005 (Option C) |
| 0.2 | 16 September 2026 | Restated as a verbatim index of canonical definitions, per `AO-066`: every existing entry now carries the Definition sentence of the document that owns the term, with that document named; the Purpose no longer claims this document is authoritative. Added Object, Ownership, Identity, Metadata, Classification, Reference, Capability, Policy, Contract, Constraint, Registry, Memory, Memory Record, Confidence, Knowledge and Context, closing `GAP-002`. Added Reserved Terms for the Constitution terms no document defines (Evidence, World Model, Autonomy level, Provenance, Static and Dynamic World Modelling, and the Architectural Principles vocabulary), each naming the observation that tracks it. EPIC-D, executed under `CAND-007` Section 3. |

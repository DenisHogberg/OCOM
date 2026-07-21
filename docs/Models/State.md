<!-- nav:start -->
[Docs](../README.md) / [Models](README.md) / State

[← Back](Relationship.md) · [↑ Up](README.md) · [Next →](Workflow.md)

---
<!-- nav:end -->

# State

**Document ID:** Model-04

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative model of an Entity State.

A State represents the current operational condition of an Entity.

---

# Definition

A State is a discrete operational condition that describes the status of an Entity at a specific point in time.

Every Entity exists in a State throughout its operational lifetime.

---

# Characteristics

Every State shall:

- have a unique name;
- have a defined meaning;
- belong to exactly one Entity;
- participate in a Lifecycle;
- be observable.

---

# State Identity

Each State shall be uniquely identifiable within the Lifecycle of an Entity.

---

# Initial State

Every Lifecycle shall define one initial State.

The initial State represents the creation or activation of an Entity.

---

# Terminal State

A Lifecycle may define one or more terminal States.

A terminal State indicates that no further transitions are permitted unless explicitly defined.

---

# State Transitions

A State does not define how transitions occur.

Transitions are defined by the Entity Lifecycle.

---

# State Constraints

States may define operational constraints.

Constraints shall be explicit and measurable.

---

# State Attributes

A State may define:

- entry conditions;
- exit conditions;
- validation rules;
- operational restrictions.

---

# Immutability

The definition of a State shall remain stable.

Only the current State of an Entity may change during operation.

---

# Constraints

A State shall never:

- exist independently of an Entity;
- exist outside a Lifecycle;
- have ambiguous meaning;
- duplicate another State within the same Lifecycle.

---

# Conformance

A State conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Future Extensions

Future versions of this specification may introduce additional State capabilities while preserving the fundamental State model.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
|0.1|20 July 2026|Initial draft|

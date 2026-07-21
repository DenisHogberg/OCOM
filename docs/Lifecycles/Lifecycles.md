<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Lifecycles

[← Back](Financial%20Lifecycle.md) · [↑ Up](README.md) · [Next →](Operational%20Lifecycle.md)

---
<!-- nav:end -->

# Lifecycles

**Document ID:** Lifecycle-00

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines how Lifecycles are modeled and reused within the OCOM Specification.

A Lifecycle describes the valid progression of an Entity through a sequence of operational States.

Lifecycles provide a standardized mechanism for defining state transitions independently of individual Entity specifications.

---

# Definition

A Lifecycle is a reusable operational model describing the allowed States and valid State Transitions of an Entity.

A Lifecycle defines how an Entity evolves over time while preserving operational consistency.

---

# Principles

Every Lifecycle:

- shall define one or more States;
- shall define valid State Transitions;
- shall prohibit undefined transitions;
- shall be reusable by multiple Entities;
- shall remain independent of implementation technologies.

---

# Relationship to Entities

An Entity references a Lifecycle rather than redefining its own lifecycle.

Multiple Entities may share the same Lifecycle.

An Entity may define a custom Lifecycle when no reusable Lifecycle is applicable.

---

# Lifecycle Components

Every Lifecycle consists of:

- States
- State Transitions
- Entry Conditions
- Exit Conditions
- Terminal States

---

# Conformance

A Lifecycle conforms to this specification only if:

- all States are explicitly defined;
- all valid Transitions are explicitly defined;
- undefined Transitions are prohibited.

---

# Standard Lifecycles

This specification currently defines the following reusable Lifecycles:

- Financial
- Commercial
- Content
- Operational
- Organizational

Additional Lifecycles may be introduced in future versions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
|0.1|20 July 2026|Initial draft|

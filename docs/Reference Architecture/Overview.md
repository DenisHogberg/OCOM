<!-- nav:start -->
[Docs](../README.md) / [Reference Architecture](README.md) / Reference Architecture

[← Back](Operational-Memory-Architecture.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Reference Architecture

**Document ID:** REF-README-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

The Reference Architecture demonstrates how the concepts defined by the OCOM Specification can be composed into a coherent enterprise architecture.

Unlike the normative sections of the specification, this section is informative.

It does not prescribe implementation technologies or deployment strategies.

Instead, it illustrates architectural patterns that preserve the principles of object-centric enterprise operation.

---

# Scope

The Reference Architecture describes:

- enterprise composition;
- Entity collaboration;
- Domain responsibilities;
- Business Event flow;
- Operational Memory integration;
- AI participation;
- governance boundaries;
- integration patterns.

---

# Objectives

The Reference Architecture aims to:

- demonstrate end-to-end architecture;
- provide implementation guidance;
- establish reusable architectural patterns;
- promote interoperability between implementations;
- illustrate enterprise-scale object-centric design.

---

# Relationship to the Specification

This section complements:

- Core Principles
- Meta Model
- Models
- Memory
- AI
- Examples

Normative behavior remains defined by the Specification itself.

---

# Architecture Layers

The Reference Architecture consists of the following views:

```text

Enterprise Architecture

↓

Domain Architecture

↓

Business Object Architecture

↓

Business Event Architecture

↓

Operational Memory Architecture

↓

AI Architecture

↓

Governance Architecture

↓

Integration Architecture

↓

Deployment Patterns

```

Each view focuses on one architectural concern while remaining consistent with the overall object-centric operating model.

---

# Architectural Principles

The Reference Architecture follows the principles defined by OCOM:

- Entities are the primary architectural units.
- Domains own Entities.
- Business Events record state transitions.
- Operational Memory augments business context.
- AI assists but does not replace business authority.
- Governance applies across all architectural layers.

---

# Informative Status

The Reference Architecture is informative.

Implementations may vary provided they preserve the normative principles defined by the OCOM Specification.

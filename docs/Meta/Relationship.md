<!-- nav:start -->
[Docs](../README.md) / [Meta](README.md) / Relationship

[← Back](Registry.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Relationship

**Document ID:** META-RELATIONSHIP-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Relationship within the OCOM Specification.

Relationship represents the semantic association between two or more Objects.

Relationships enable organizations to model operational structures, dependencies, ownership, collaboration, and business meaning independently of implementation technologies.

---

# Definition

A Relationship is a governed semantic association between Objects.

A Relationship expresses how Objects are connected within the operational model.

Unlike a Reference, a Relationship conveys business meaning.

---

# Business Meaning

Relationships enable organizations to describe operational reality as interconnected Objects rather than isolated elements.

They provide the structural foundation for business models, workflows, governance, memory, knowledge, and artificial intelligence.

---

# Design Principles

A Relationship shall:

- connect identifiable Objects;
- express business semantics;
- remain explicit;
- support governance;
- preserve traceability;
- remain technology independent.

---

# Core Characteristics

Every Relationship shall define:

- Identifier;
- Source Object;
- Target Object;
- Relationship Type.

A Relationship may additionally define:

- Direction;
- Cardinality;
- Status;
- Validity Period;
- Constraints;
- Governance Rules.

---

# Relationship Types

Organizations may define Relationship Types including:

- Ownership;
- Dependency;
- Composition;
- Association;
- Membership;
- Responsibility;
- Assignment;
- Delegation;
- Collaboration;
- Sequence.

Additional relationship types may be introduced without affecting the model.

---

# Direction

Relationships may be:

- Directed;
- Bidirectional;
- Undirected.

Organizations shall define direction according to business semantics.

---

# Cardinality

Relationships may define cardinality.

Examples include:

- One-to-One;
- One-to-Many;
- Many-to-One;
- Many-to-Many.

Cardinality rules are organization-specific.

---

# Lifecycle

Relationships may possess an independent lifecycle.

Creating, modifying, or retiring a Relationship shall not change the Identity of participating Objects.

Relationship history should be preserved.

---

# Constraints

Relationships may define operational constraints including:

- mandatory participation;
- optional participation;
- uniqueness;
- temporal validity;
- organizational restrictions.

Constraint definitions are governed by the Constraint specification.

---

# Governance

Relationship creation, modification, and retirement shall comply with applicable organizational policies.

Organizations should define approval requirements according to business risk.

---

# Auditability

Organizations shall preserve:

- relationship history;
- participating Objects;
- lifecycle history;
- governance decisions;
- policy references.

Audit records shall remain immutable.

---

# Relationship to Other Specifications

Relationship interacts with:

- Object
- Identity
- Reference
- Metadata
- Registry
- Ownership
- Policy
- Constraint

Relationship defines business semantics, while Reference provides object connectivity.

---

# Independence

The Relationship specification does not prescribe:

- database relationships;
- graph technologies;
- object models;
- APIs;
- implementation technologies.

Organizations remain free to implement Relationships using any compatible architecture.

---

# Conformance

A compliant implementation shall:

- define Relationships explicitly;
- preserve business semantics;
- support lifecycle management;
- maintain traceability;
- support governance;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

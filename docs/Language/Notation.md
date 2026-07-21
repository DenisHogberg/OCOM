<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Notation

[← Back](Namespace.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Notation

**Document ID:** LANG-NOTATION-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the notation used by the OCOM Language.

Notation establishes a consistent representation of OCOM models for both human interpretation and machine processing.

The notation is independent of visualization tools, serialization formats, and implementation technologies.

---

# Definition

Notation is the standardized representation of OCOM model elements and their relationships.

Notation defines how concepts are expressed without changing their meaning.

Multiple notations may represent the same model while preserving semantic equivalence.

---

# Business Meaning

A common notation enables stakeholders to communicate operational models consistently across organizations, industries, and technologies.

Notation improves readability, collaboration, documentation, and interoperability.

---

# Design Principles

The notation shall:

- be unambiguous;
- be human-readable;
- support machine processing;
- remain implementation independent;
- preserve semantic consistency;
- support extensibility.

---

# Representation Types

OCOM models may be represented using:

- textual notation;
- tabular notation;
- graphical notation;
- structured notation;
- serialized notation.

All representations shall preserve semantic equivalence.

---

# Textual Representation

Textual notation represents model elements using structured text.

Example:

Object Customer

belongs to Domain Commercial

owned by Department Sales

---

# Graphical Representation

Graphical notation represents Objects and Relationships visually.

Typical graphical elements include:

- Objects;
- Relationships;
- References;
- Containers;
- Boundaries.

Graphical symbols are implementation-specific.

---

# Tabular Representation

Model information may be represented using tables.

Example columns include:

- Identifier;
- Name;
- Type;
- Owner;
- Status.

Table layout is implementation-specific.

---

# Structured Representation

Structured notation represents models using hierarchical structures.

Examples include:

- trees;
- nested structures;
- object hierarchies.

The structure shall preserve semantic meaning.

---

# Semantic Equivalence

Multiple representations shall be considered equivalent if they describe identical semantics.

Changing notation shall not alter:

- Object Identity;
- Relationships;
- Policies;
- Constraints;
- Lifecycle definitions.

---

# Symbols

Implementations may define graphical symbols.

Symbols shall:

- represent a single concept;
- remain visually distinguishable;
- preserve semantic consistency.

The OCOM Specification does not prescribe symbol libraries.

---

# Readability

Notation should:

- minimize ambiguity;
- support visual clarity;
- remain understandable by business and technical audiences;
- avoid unnecessary complexity.

---

# Extensibility

Organizations may introduce additional notation elements.

Extensions shall:

- preserve compatibility;
- avoid semantic conflicts;
- document new notation elements.

---

# Relationship to Other Specifications

Notation represents concepts defined by:

- Meta
- Core
- Models
- Entities
- Lifecycles
- Memory
- AI
- Domains

Notation defines representation rather than semantics.

---

# Independence

The Notation specification does not prescribe:

- diagramming tools;
- modeling software;
- graphical standards;
- serialization formats.

Organizations remain free to implement notation using any compatible approach.

---

# Conformance

A compliant implementation shall:

- preserve semantic meaning across representations;
- support consistent notation;
- avoid ambiguity;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

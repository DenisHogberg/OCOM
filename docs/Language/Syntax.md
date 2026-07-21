<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Syntax

[← Back](Serialization.md) · [↑ Up](README.md) · [Next →](Validation.md)

---
<!-- nav:end -->

# Syntax

**Document ID:** LANG-SYNTAX-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the syntax of the OCOM Language.

Syntax establishes the structural rules for constructing valid OCOM models while remaining independent of specific serialization formats, programming languages, or implementation technologies.

---

# Definition

Syntax is the formal set of rules governing the arrangement and composition of OCOM language elements.

Syntax defines how language constructs may be combined to produce semantically valid models.

Syntax does not define business meaning.

Business semantics are defined by the corresponding OCOM specifications.

---

# Business Meaning

A consistent syntax enables organizations to exchange, validate, interpret, and automate OCOM models across diverse tools and operational environments.

Common syntax improves interoperability and reduces ambiguity.

---

# Design Principles

The syntax shall:

- be deterministic;
- be unambiguous;
- support validation;
- support extensibility;
- remain implementation independent;
- preserve semantic consistency.

---

# Language Elements

The OCOM Language consists of identifiable elements including:

- Objects;
- Relationships;
- References;
- Attributes;
- Classifications;
- Constraints;
- Policies.

Additional language elements may be introduced by future specifications.

---

# Structural Rules

Every valid model shall:

- contain identifiable Objects;
- preserve Object Identity;
- define valid References;
- define valid Relationships;
- satisfy applicable Constraints.

Organizations may define additional structural requirements.

---

# Object Composition

Objects may contain:

- Metadata;
- Classifications;
- References;
- Relationships;
- Capabilities;
- Policies;
- Constraints.

Object composition rules are defined by the corresponding specifications.

---

# Naming Rules

Names should:

- be unique within their applicable scope;
- remain stable where practical;
- avoid ambiguity;
- follow organizational naming conventions.

Identifier syntax is defined separately.

---

# References

References shall:

- identify existing Objects;
- preserve direction where applicable;
- remain valid throughout their effective period.

Reference semantics are defined by the Reference specification.

---

# Relationships

Relationships shall:

- connect valid Objects;
- define explicit semantics;
- satisfy applicable Constraints.

Relationship semantics are defined separately.

---

# Extensibility

Organizations may extend the language by introducing:

- additional Object types;
- additional Attributes;
- additional Constraints;
- additional Policies;
- additional Classifications.

Extensions shall preserve compatibility with the core language.

---

# Validation

A syntactically valid model shall satisfy:

- structural correctness;
- identifier correctness;
- reference integrity;
- required element presence;
- language consistency.

Semantic validation is defined separately.

---

# Error Handling

Implementations should report syntax violations in a manner that:

- identifies the affected language element;
- describes the violated rule;
- supports correction;
- preserves diagnostic information.

Error reporting mechanisms are implementation-specific.

---

# Relationship to Other Specifications

Syntax provides structural rules for:

- Meta
- Core
- Models
- Entities
- Lifecycles
- Memory
- AI
- Domains

Syntax governs language construction rather than business semantics.

---

# Independence

The Syntax specification does not prescribe:

- parser implementations;
- parser generators;
- serialization formats;
- programming languages.

Organizations remain free to implement syntax processing using any compatible technology.

---

# Conformance

A compliant implementation shall:

- construct syntactically valid models;
- preserve structural consistency;
- support validation;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

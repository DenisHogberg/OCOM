<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Identifier Syntax

[← Back](Conformance.md) · [↑ Up](README.md) · [Next →](Namespace.md)

---
<!-- nav:end -->

# Identifier Syntax

**Document ID:** LANG-IDENTIFIER-SYNTAX-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the syntax rules for identifiers used within the OCOM Language.

Identifier syntax establishes consistent naming conventions that support uniqueness, readability, validation, interoperability, and automated processing.

Identifier syntax defines representation only.

Identifier semantics are defined by the Identity specification.

---

# Definition

An Identifier is the syntactic representation of an Identity within an OCOM model.

Identifiers uniquely reference language elements within their applicable scope.

The same Identity may be represented by different identifiers in different implementation environments.

---

# Business Meaning

Consistent identifier syntax enables organizations to exchange models reliably across tools, repositories, platforms, and operational environments.

Standardized identifiers improve traceability, automation, validation, and long-term maintainability.

---

# Design Principles

Identifier syntax shall:

- be deterministic;
- be unambiguous;
- support uniqueness;
- remain stable where practical;
- support machine processing;
- remain implementation independent.

---

# Identifier Characteristics

Identifiers shall:

- uniquely identify an element within their scope;
- be immutable whenever practical;
- remain independent of business meaning;
- support validation.

Identifiers should not encode operational state.

---

# Scope

Identifiers may exist within different scopes including:

- local scope;
- namespace scope;
- organizational scope;
- ecosystem scope.

Uniqueness requirements depend on the applicable scope.

---

# Naming Rules

Identifiers should:

- use a consistent character set;
- avoid whitespace;
- avoid reserved language keywords;
- remain concise;
- remain stable.

Organizations may define additional naming conventions.

---

# Reserved Identifiers

The OCOM Language may reserve identifiers for:

- language keywords;
- core specifications;
- predefined namespaces;
- future standard extensions.

Reserved identifiers shall not be redefined.

---

# Identifier Resolution

Implementations shall resolve identifiers according to:

- Namespace;
- Scope;
- Version;
- applicable language rules.

Resolution mechanisms are implementation-specific.

---

# Identifier Lifecycle

Identifiers shall remain associated with the same Identity throughout their effective lifetime.

If an element is retired, its identifier should not be reassigned unless organizational governance explicitly permits reuse.

---

# Validation

Identifier validation may include:

- syntax correctness;
- uniqueness;
- namespace consistency;
- scope validation;
- reserved identifier checks.

Validation mechanisms are implementation-specific.

---

# Governance

Organizations shall establish governance for:

- identifier allocation;
- identifier ownership;
- identifier reuse;
- identifier retirement;
- conflict resolution.

Governance policies are organization-specific.

---

# Relationship to Other Specifications

Identifier Syntax works together with:

- Identity
- Namespace
- Vocabulary
- Syntax
- Schema
- Validation
- Conformance

This specification defines identifier representation rather than identity semantics.

---

# Independence

The Identifier Syntax specification does not prescribe:

- UUID;
- GUID;
- URI;
- database keys;
- programming language identifiers;
- implementation technologies.

Organizations remain free to adopt identifier formats appropriate to their environments.

---

# Conformance

A compliant implementation shall:

- assign identifiers consistently;
- preserve identifier uniqueness within the applicable scope;
- support identifier validation;
- maintain compatibility with Namespace rules;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../README.md) / [Meta](README.md) / Reference

[← Back](Policy.md) · [↑ Up](README.md) · [Next →](Registry.md)

---
<!-- nav:end -->

# Reference

**Document ID:** META-REFERENCE-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Reference within the OCOM Specification.

A Reference enables one Object to identify, locate, or associate with another Object without defining the business meaning of their relationship.

References support navigation, interoperability, traceability, and object connectivity throughout the OCOM ecosystem.

---

# Definition

A Reference is a directed association from one Object to another.

A Reference identifies a target Object but does not define the semantic nature of the association.

The meaning of the association is defined separately by the Relationship specification.

---

# Business Meaning

References enable Objects to interact without embedding implementation details.

They provide stable connections between Objects while preserving object independence and modularity.

---

# Design Principles

A Reference shall:

- identify a target Object;
- remain independent of implementation technology;
- support traceability;
- preserve object independence;
- support interoperability;
- remain reusable.

---

# Core Characteristics

Every Reference shall define:

- Source Object;
- Target Object;
- Reference Direction.

A Reference may additionally define:

- Reference Type;
- Reference Purpose;
- Validity Period;
- Status.

---

# Reference Direction

Every Reference is directional.

A Reference always originates from a Source Object and points to a Target Object.

Organizations may derive reverse references where appropriate.

---

# Reference Types

Organizations may define Reference Types including:

- Internal Reference;
- External Reference;
- Cross-Domain Reference;
- Cross-System Reference;
- Historical Reference.

Additional types may be introduced without affecting the Reference model.

---

# Reference Validity

References may be:

- Active;
- Deprecated;
- Archived;
- Temporary.

Organizations may define additional validity states.

---

# Reference Integrity

A Reference should point to an identifiable Object.

Organizations should define procedures for handling:

- missing references;
- invalid references;
- obsolete references;
- migrated references.

Reference integrity should be periodically validated.

---

# Lifecycle

References may have their own lifecycle independent of the referenced Objects.

Creating, updating, or removing a Reference shall not change the identity of either participating Object.

---

# Governance

Organizations shall define policies governing:

- reference creation;
- modification;
- validation;
- retirement;
- audit.

Reference history should be preserved.

---

# Auditability

Organizations should retain:

- source object;
- target object;
- creation history;
- modification history;
- retirement history.

Audit records shall remain immutable.

---

# Relationship to Other Specifications

Reference interacts with:

- Object
- Identity
- Relationship
- Registry
- Metadata
- Ownership
- Governance

Reference provides connectivity between Objects without defining business semantics.

---

# Independence

The Reference specification does not prescribe:

- storage mechanisms;
- pointer formats;
- database keys;
- communication protocols;
- implementation technologies.

Organizations remain free to implement References using any compatible approach.

---

# Conformance

A compliant implementation shall:

- support directed References;
- preserve reference traceability;
- maintain reference integrity;
- support governance;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

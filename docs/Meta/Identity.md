<!-- nav:start -->
[Docs](../README.md) / [Meta](README.md) / Identity

[← Back](Contract.md) · [↑ Up](README.md) · [Next →](Metadata.md)

---
<!-- nav:end -->

# Identity

**Document ID:** META-IDENTITY-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 29 October 2026

---

# Purpose

This document defines Identity within the OCOM Specification.

Identity provides the mechanism by which Objects are uniquely recognized, referenced, and managed throughout their existence.

Identity enables interoperability, traceability, governance, and consistent object management across the OCOM ecosystem.

---

# Definition

Identity is the persistent and unique representation of an Object.

Identity distinguishes one Object from all others regardless of changes to its metadata, state, relationships, or implementation.

Identity shall remain stable throughout the lifetime of an Object.

---

# Business Meaning

Identity allows organizations to reliably identify and manage Objects across systems, workflows, and business domains.

A stable Identity ensures that operational history, governance, evaluations, and relationships remain attached to the same Object over time.

---

# Design Principles

Identity shall:

- be unique;
- be persistent;
- be immutable;
- be globally distinguishable within its defined scope;
- support interoperability;
- remain technology independent.

---

# Core Characteristics

Every Identity shall:

- uniquely identify an Object;
- remain unchanged during the Object Lifecycle;
- support references from other Objects;
- support auditability;
- support traceability.

---

# Identity Scope

Identity scope may include:

- Organization
- Business Domain
- Registry
- External System
- Global Ecosystem

Organizations shall define the appropriate scope for each Identity.

A scope is the range within which the assigner of an identity guarantees that the identity names one Object, and the assigner carries it. Where a Registry assigns or registers the identity, the scope is that Registry's declared scope, and the guarantee is the unique Object registration `Meta/Registry.md` requires of it. Where the organization assigns identities without a Registry, the scope is the Organization or the Business Domain that assigns them. Where the identity comes from another system, the scope is External System and that system is named. Where the assigner is outside every organization, a standards body or a public registry, the scope is Global Ecosystem and the guarantee is that assigner's. Scope is a property of an identity's assignment rather than an Object of its own: the regress stops at the Registry, which is an Object with an Identity in the scope of the Organization that operates it. Uniqueness is evaluated within a scope, an identity is the pair of its scope and its value, and identities of different scopes do not collide. This passage clarifies the five scopes above and carries no obligation of its own (`CAND-030`).

---

# Identity Types

Examples include:

- Internal Identity
- External Identity
- Global Identity
- Local Identity
- Composite Identity

Organizations may define additional Identity types.

---

# Identity Assignment

Identity shall be assigned when an Object is created.

Once assigned, Identity shall not be reused for another Object.

Replacement of an Object shall result in a new Identity unless organizational policy specifies otherwise.

---

# Identity Persistence

Identity shall survive changes to:

- metadata;
- ownership;
- lifecycle state;
- relationships;
- capabilities;
- implementation technology.

Identity represents the continuity of the Object rather than its current characteristics.

---

# Identity Resolution

Organizations may implement mechanisms for resolving:

- aliases;
- migrated identities;
- external mappings;
- historical references.

Identity resolution shall preserve traceability.

---

# Relationship to Other Specifications

Identity is used by:

- Object
- Metadata
- Relationship
- Reference
- Registry
- Lifecycle
- Governance
- Evaluation

All managed Objects shall possess an Identity.

---

# Independence

The Identity specification does not prescribe:

- identifier formats;
- UUID standards;
- database keys;
- naming conventions;
- implementation technologies.

Organizations remain free to implement Identity using any compatible mechanism.

---

# Conformance

A compliant implementation shall:

- assign a unique Identity to every managed Object;
- preserve Identity throughout the Object Lifecycle;
- prevent Identity reuse;
- support traceability;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 29 October 2026 | Identity Scope gains one clarifying paragraph: a scope is the range within which the assigner of an identity guarantees that it names one Object, and the assigner carries it. It carries no keyword and adds no obligation; the register is unchanged at 335 Statements. Integration of `CAND-030`, under `EPIC-B`, `CAND-007` Section 3. |

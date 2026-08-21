<!-- nav:start -->
[Docs](../README.md) / [Entities](README.md) / Entities

[↑ Up](README.md)

---
<!-- nav:end -->

# Entities

**Document ID:** Entity-00

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 August 2026

---

# Purpose

**Status note (20 August 2026):** `Constitution-Step0-Summary.md` Decision 4 excludes `Entities/` from Constitution §9's Domain-Neutral Core, describing it as *"mixed, mostly domain-specific by design."* That decision concerns Constitution §9's Core-scope test only; it does not itself address this document's own Status field, and this document's own content, the mandatory structure, attributes, and Conformance requirements below, remains normative ("shall") throughout. Status is therefore left as `Draft`, reflecting that content, rather than reclassified to `Informative` on the strength of a Core-scope decision alone. See `Governance/Documentation-Standards.md`'s Status Taxonomy.

This document defines how Entities shall be specified within the OCOM Specification.

An Entity is uniquely identifiable and has its own identity, lifecycle, attributes, responsibilities, and relationships.

Entity specifications shall follow a standardized structure to ensure consistency, interoperability, and reusability across all Domains.

---

# Definition

An Entity exists independently within the operational model.

An Entity may represent a physical object, digital object, business concept, organizational object, financial object, or any other operationally significant object.

Each Entity shall have its own identity throughout its lifecycle.

---

# Entity Structure

Every Entity specification shall contain the following sections:

1. Metadata
2. Purpose
3. Definition
4. Business Meaning
5. Core Principles
6. Mandatory Attributes
7. Optional Attributes
8. Ownership
9. Domain
10. Lifecycle
11. Relationships
12. Events
13. Business Rules
14. Invariants
15. Constraints
16. Conformance
17. Examples
18. Revision History

---

# Lifecycle

Every Entity shall reference a Lifecycle defined in the **Lifecycles** section of the OCOM Specification.

An Entity should reuse an existing Lifecycle whenever applicable.

An Entity may define additional lifecycle constraints or specialized states if required by its business semantics.

---

# Ownership

Every Entity shall have a clearly defined Owner responsible for its business integrity and governance.

Ownership defines accountability rather than technical implementation.

---

# Domains

Every Entity belongs to one primary Domain.

An Entity may interact with multiple Domains but shall have only one governing Domain.

---

# Relationships

Entities may establish relationships with other Entities.

Relationships shall be defined explicitly and shall not be implied.

---

# Events

Entities may emit, receive, or react to Events.

Events represent business facts and shall not directly modify Entity definitions.

---

# Business Rules

Business Rules define the operational policies governing an Entity.

Business Rules shall be expressed independently of software implementation.

---

# Invariants

Invariants define conditions that shall always remain true throughout the Entity lifecycle.

Violation of an Invariant indicates an invalid operational state.

---

# Constraints

Constraints define operational limitations, validation requirements, and compliance obligations applicable to an Entity.

---

# Conformance

An Entity conforms to this specification if it:

- follows the standard Entity structure;
- references a valid Lifecycle;
- defines mandatory attributes;
- specifies ownership and governing Domain;
- defines applicable business rules;
- defines applicable invariants;
- complies with the OCOM Core and Modeling Rules.

---

# Standard Lifecycle Categories

Entities typically reference one of the following Lifecycle categories:

- Financial
- Commercial
- Content
- Operational
- Organizational

Additional Lifecycle categories may be introduced in future versions of the specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 20 August 2026 | Status briefly changed to Informative, then reverted to Draft on independent review: Decision 4 governs Constitution §9 Core scope only, not this document's own Status, and this document's normative "shall" content was never actually reduced. Status note corrected to quote Decision 4's actual hedged wording ("mixed, mostly domain-specific") |

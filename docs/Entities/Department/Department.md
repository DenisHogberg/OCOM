<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Department](README.md) / Department

[↑ Up](README.md)

---
<!-- nav:end -->

# Department

**Document ID:** Entity-015

**Status:** Draft

**Version:** 0.1

**Last Updated:** 22 September 2026

---

# Purpose

This document defines the Department Entity within the OCOM Specification.

A Department represents a unit of an organization's internal structure: the people and responsibilities grouped under one accountable lead, at any size from a single function to a business unit.

---

# Definition

A Department is a business Entity representing an organizational unit inside an Organization.

Its Classification names the kind of unit (Department, Division, Business Unit, Function, Shared Service); Composition Relationships between Departments express the hierarchy; a Membership Relationship binds a Department to the Organization it serves.

A Department is internal structure, not a participant in the ecosystem. A unit that is also a legal person is an Organization as well, and the Department is the part of it that carries people (`CAND-027`).

---

# Business Meaning

The Department Entity provides a standardized representation of organizational structure independently of HR systems, organization charts, or implementation technologies.

A Department organizes people and accountability; a Domain organizes responsibility (`Models/Domain.md`). The two are related and not the same: a Department's Employees may work in several Domains, and one Domain may be served by several Departments.

---

# Core Principles

A Department:

- shall possess a unique identity;
- shall have a clearly defined business purpose;
- shall belong to one Organization;
- may be composed of other Departments;
- shall remain independent of organizational implementation.

---

# Mandatory Attributes

Every Department shall define:

- Identifier
- Name
- Owner
- Organization
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Department may define:

- Description
- Classification
- Parent Department
- Head
- Members
- Business Capabilities
- Cost Center
- Tags

---

# Ownership

The Department shall have a clearly defined Owner responsible for its governance and organizational accountability.

---

# Domain

The governing Domain is:

**HR**

---

# Lifecycle

This Entity shall conform to the **Organizational Lifecycle** unless otherwise specified.

---

# Relationships

A Department may be related to:

- Organization
- Department
- Employee
- Team
- Task
- Event

---

# Events

Typical Events include:

- Department Created
- Department Updated
- Department Activated
- Department Merged
- Department Split
- Department Retired

---

# Memory

A Department holds no Memory of its own. Memory about a Department is held in Memory Records that name it as their Related Entity, per `Memory/Memory Record.md`; such records are governed by the Memory specification and do not modify its attributes, States or Lifecycle. This Entity follows the default relationship to Memory defined in `Entities/Overview.md` and adds nothing to it.

---

# Business Rules

- A Department shall belong to one Organization.
- A Department may contain Employees and Teams.
- A Department may be composed of other Departments; the composition shall not be circular.
- A second reporting line of an Employee is a Relationship to a Department or to another Employee, and does not change the Employee's primary Department.

---

# Invariants

The following conditions shall always remain true:

- Every Department shall have a unique Identifier.
- Every Department shall belong to one governing Domain.
- Every Department shall reference a valid Lifecycle.
- Every Department shall belong to one Organization.

---

# Constraints

A Department shall comply with applicable organizational policies, governance rules, labor laws, and security requirements.

---

# Conformance

A Department conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Organizational Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Finance Department
- Customer Support Department
- Marketing Division
- Payments Business Unit
- Shared Services Function

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 September 2026 | First content, replacing the stub reserved since 20 July 2026, per `CAND-027` (Decided 22 September 2026). `Entities/Employee/Employee.md` and `Entities/Team/Team.md` already required a primary Department; this document defines it. EPIC-B and EPIC-C, under `CAND-007` Section 3. |

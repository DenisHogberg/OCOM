<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Employee](README.md) / Employee

[↑ Up](README.md)

---
<!-- nav:end -->

# Employee

**Document ID:** Entity-016

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Employee Entity within the OCOM Specification.

An Employee represents an individual who performs organizational responsibilities on behalf of an organization.

---

# Definition

An Employee is a business Entity representing a person assigned one or more organizational responsibilities.

An Employee participates in business operations through assigned roles, teams, departments, and workflows.

---

# Business Meaning

The Employee Entity provides a standardized representation of human organizational resources independently of HR systems or implementation technologies.

An Employee performs business capabilities rather than representing an employment record.

---

# Core Principles

An Employee:

- shall possess a unique identity;
- shall perform one or more organizational roles;
- may belong to one or more Teams;
- shall belong to one primary Department;
- shall remain independent of HR software implementations.

---

# Mandatory Attributes

Every Employee shall define:

- Identifier
- Name
- Owner
- Department
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

An Employee may define:

- Employee Number
- Job Title
- Email
- Phone Number
- Manager
- Skills
- Certifications
- Employment Type
- Time Zone
- Tags

---

# Ownership

The Employee shall have a clearly defined Owner responsible for governance and organizational accountability.

---

# Domain

The governing Domain is:

**HR**

---

# Lifecycle

This Entity shall conform to the **Organizational Lifecycle** unless otherwise specified.

---

# Relationships

An Employee may be related to:

- Department
- Team
- Task
- Ticket
- AI Agent
- Event

---

# Events

Typical Events include:

- Employee Created
- Employee Assigned
- Employee Updated
- Employee Transferred
- Employee Suspended
- Employee Retired

---

# Business Rules

- An Employee shall belong to one primary Department.
- An Employee may belong to multiple Teams.
- An Employee may perform multiple organizational Roles.
- An Employee may own business Entities according to organizational policies.

---

# Invariants

The following conditions shall always remain true:

- Every Employee shall have a unique Identifier.
- Every Employee shall belong to one governing Domain.
- Every Employee shall reference a valid Lifecycle.
- Every Employee shall have one primary Department.

---

# Constraints

An Employee shall comply with applicable organizational policies, privacy regulations, labor laws, and security requirements.

---

# Conformance

An Employee conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Organizational Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Affiliate Manager
- CRM Manager
- Compliance Officer
- Finance Specialist
- Product Manager
- Customer Support Agent

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

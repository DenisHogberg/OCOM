<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Team](README.md) / Team

[↑ Up](README.md)

---
<!-- nav:end -->

# Team

**Document ID:** Entity-017

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Team Entity within the OCOM Specification.

A Team represents a group of individuals organized to achieve one or more shared business objectives.

---

# Definition

A Team is a business Entity representing an organizational unit composed of Employees, AI Agents, or both, working together under common responsibilities.

A Team exists to execute operational, tactical, or strategic activities.

---

# Business Meaning

The Team Entity provides a standardized representation of collaborative organizational structures independently of reporting lines or implementation technologies.

A Team enables coordinated execution of business capabilities and operational responsibilities.

---

# Core Principles

A Team:

- shall possess a unique identity;
- shall have a clearly defined business purpose;
- shall belong to one primary Department;
- may include Employees and AI Agents;
- shall remain independent of organizational implementation.

---

# Mandatory Attributes

Every Team shall define:

- Identifier
- Name
- Owner
- Department
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Team may define:

- Description
- Team Lead
- Members
- Business Capability
- Objectives
- KPIs
- Service Level Agreements
- Tags

---

# Ownership

The Team shall have a clearly defined Owner responsible for its governance and operational performance.

---

# Domain

The governing Domain is:

**HR**

---

# Lifecycle

This Entity shall conform to the **Organizational Lifecycle** unless otherwise specified.

---

# Relationships

A Team may be related to:

- Department
- Employee
- AI Agent
- Task
- Ticket
- Event

---

# Events

Typical Events include:

- Team Created
- Team Updated
- Team Activated
- Team Suspended
- Team Retired

---

# Business Rules

- A Team shall belong to one primary Department.
- A Team may contain multiple Employees.
- A Team may include one or more AI Agents.
- A Team may own or execute business Tasks and Workflows.

---

# Invariants

The following conditions shall always remain true:

- Every Team shall have a unique Identifier.
- Every Team shall belong to one governing Domain.
- Every Team shall reference a valid Lifecycle.
- Every Team shall belong to one primary Department.

---

# Constraints

A Team shall comply with applicable organizational policies, governance rules, and security requirements.

---

# Conformance

A Team conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Organizational Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Affiliate Team
- CRM Team
- Finance Team
- Compliance Team
- Product Team
- Customer Support Team

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

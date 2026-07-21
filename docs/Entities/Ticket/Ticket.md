<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Ticket](README.md) / Ticket

[↑ Up](README.md)

---
<!-- nav:end -->

# Ticket

**Document ID:** Entity-019

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Ticket Entity within the OCOM Specification.

A Ticket represents a formal request, issue, incident, or case that requires tracking, ownership, and resolution through a defined operational process.

---

# Definition

A Ticket is a business Entity representing a managed operational item created to record, monitor, and resolve a specific business request or issue.

A Ticket provides accountability, traceability, and operational visibility throughout its lifecycle.

---

# Business Meaning

The Ticket Entity standardizes the management of operational requests across all business Domains.

A Ticket exists independently of service desk platforms, issue trackers, or CRM systems.

---

# Core Principles

A Ticket:

- shall possess a unique identity;
- shall represent one operational issue or request;
- shall have a clearly defined Owner;
- may be assigned to an Employee, Team, or AI Agent;
- shall maintain a complete operational history;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Ticket shall define:

- Identifier
- Title
- Type
- Owner
- Assignee
- Lifecycle
- Priority
- Status
- Created Date

---

# Optional Attributes

A Ticket may define:

- Description
- Category
- Severity
- Resolution
- Due Date
- Closed Date
- Source
- Related Entity
- Tags

---

# Ownership

The Ticket shall have a clearly defined Owner responsible for ensuring the Ticket reaches a valid resolution.

---

# Domain

The governing Domain is:

**Operations**

---

# Lifecycle

This Entity shall conform to the **Operational Lifecycle** unless otherwise specified.

---

# Relationships

A Ticket may be related to:

- Employee
- Team
- AI Agent
- Task
- Event
- Workflow
- Vendor

---

# Events

Typical Events include:

- Ticket Created
- Ticket Assigned
- Ticket Updated
- Ticket Escalated
- Ticket Resolved
- Ticket Closed
- Ticket Cancelled

---

# Business Rules

- A Ticket shall have exactly one Owner.
- A Ticket may have one or more Assignees.
- Every Ticket shall have a defined Priority.
- A resolved Ticket shall include a Resolution.
- A closed Ticket shall not be reopened unless permitted by organizational policy.

---

# Invariants

The following conditions shall always remain true:

- Every Ticket shall have a unique Identifier.
- Every Ticket shall belong to one governing Domain.
- Every Ticket shall reference a valid Lifecycle.
- Every Ticket shall have one Owner.

---

# Constraints

A Ticket shall comply with applicable organizational policies, governance rules, audit requirements, and security requirements.

---

# Conformance

A Ticket conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Operational Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Customer Support Ticket
- Incident Ticket
- Compliance Case
- Fraud Investigation
- Infrastructure Issue
- Change Request

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

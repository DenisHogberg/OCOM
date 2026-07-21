<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Task](README.md) / Task

[↑ Up](README.md)

---
<!-- nav:end -->

# Task

**Document ID:** Entity-018

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Task Entity within the OCOM Specification.

A Task represents a discrete unit of work assigned to one or more responsible parties to achieve a specific business objective.

---

# Definition

A Task is a business Entity representing an actionable piece of work with defined ownership, execution status, and completion criteria.

A Task may be created manually or automatically as part of a Workflow or business Event.

---

# Business Meaning

The Task Entity provides a standardized representation of operational work across all Domains.

A Task exists independently of project management systems, ticketing platforms, or workflow engines.

---

# Core Principles

A Task:

- shall possess a unique identity;
- shall represent a single business objective;
- shall have a clearly defined Owner;
- may be assigned to an Employee, Team, or AI Agent;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Task shall define:

- Identifier
- Name
- Owner
- Assignee
- Lifecycle
- Priority
- Status
- Created Date

---

# Optional Attributes

A Task may define:

- Description
- Due Date
- Completion Date
- Category
- Parent Task
- Estimated Effort
- Actual Effort
- Tags

---

# Ownership

The Task shall have a clearly defined Owner responsible for its business outcome.

---

# Domain

The governing Domain is:

**Operations**

---

# Lifecycle

This Entity shall conform to the **Operational Lifecycle** unless otherwise specified.

---

# Relationships

A Task may be related to:

- Employee
- Team
- AI Agent
- Ticket
- Event
- Workflow

---

# Events

Typical Events include:

- Task Created
- Task Assigned
- Task Started
- Task Paused
- Task Completed
- Task Cancelled

---

# Business Rules

- A Task shall have exactly one Owner.
- A Task shall have at least one Assignee.
- A Task may be part of a Workflow.
- A completed Task shall not be modified except through an approved operational process.

---

# Invariants

The following conditions shall always remain true:

- Every Task shall have a unique Identifier.
- Every Task shall belong to one governing Domain.
- Every Task shall reference a valid Lifecycle.
- Every Task shall have one Owner.

---

# Constraints

A Task shall comply with applicable organizational policies, governance rules, and security requirements.

---

# Conformance

A Task conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Operational Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Review Affiliate Application
- Approve Payment
- Publish Content
- Verify Compliance Documents
- Generate Monthly Report
- Investigate Fraud Alert

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

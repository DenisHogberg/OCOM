<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Operations](README.md) / Operations Lifecycles

[← Back](Operations_KPIs.md) · [↑ Up](README.md) · [Next →](Operations_Objects.md)

---
<!-- nav:end -->

# Operations Lifecycles

**Document ID:** DOMAIN-OPERATIONS-LIFECYCLES-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Lifecycle principles governing Entities owned by the Operations Domain.

Operational Lifecycles define the controlled evolution of Operational Entities while preserving Object identity, governance, auditability, and enterprise interoperability.

Lifecycle semantics remain independent of implementation technologies.

---

# Definition

An Operational Lifecycle defines the permissible business states and transitions of an Operational Entity.

Every Operational Entity participates in a governed Lifecycle throughout its existence.

Lifecycle semantics are defined by the Core Lifecycle specification.

---

# Business Meaning

Operational Lifecycles provide a consistent framework for managing Work Items, Operational Tasks, Operational Plans, Assignments, Schedules, Resource Allocations, Procedures, and Operational Dependencies.

They ensure enterprise execution progresses predictably, consistently, and remains traceable throughout the organization.

---

# Design Principles

Operational Lifecycles shall:

- preserve Object identity;
- define explicit business states;
- define governed state transitions;
- produce Operational Events;
- support auditability;
- remain technology independent.

---

# Lifecycle Categories

Operational Entities may define individual Lifecycles appropriate to their business purpose.

---

## Work Item Lifecycle

A typical Work Item Lifecycle may include:

- Created
- Planned
- Ready
- In Progress
- Blocked
- Completed
- Cancelled
- Archived

Work Item identity shall remain preserved throughout the Lifecycle.

---

## Operational Task Lifecycle

A typical Operational Task Lifecycle may include:

- Created
- Assigned
- Accepted
- In Progress
- Waiting
- Completed
- Reopened
- Cancelled
- Archived

Tasks evolve independently while contributing to larger operational objectives.

---

## Operational Plan Lifecycle

A typical Operational Plan Lifecycle may include:

- Draft
- Planned
- Approved
- Active
- Suspended
- Completed
- Cancelled
- Archived

Operational Plans coordinate execution without owning operational work.

---

## Operational Schedule Lifecycle

A typical Operational Schedule Lifecycle may include:

- Draft
- Published
- Active
- Modified
- Completed
- Archived

Schedules coordinate execution timing.

---

## Assignment Lifecycle

A typical Assignment Lifecycle may include:

- Created
- Assigned
- Accepted
- Active
- Completed
- Released
- Archived

Assignments represent operational responsibility rather than workforce ownership.

---

## Queue Lifecycle

A typical Work Queue Lifecycle may include:

- Created
- Active
- Balanced
- Suspended
- Closed
- Archived

Queues coordinate execution prioritization.

---

## Resource Allocation Lifecycle

A typical Resource Allocation Lifecycle may include:

- Planned
- Reserved
- Allocated
- Active
- Released
- Closed
- Archived

Resource Allocations govern planned operational usage.

---

## Procedure Lifecycle

A typical Operational Procedure Lifecycle may include:

- Draft
- Under Review
- Approved
- Published
- Revised
- Retired
- Archived

Procedures preserve standardized operational knowledge.

---

# Lifecycle Transitions

Lifecycle transitions shall:

- comply with applicable Policies;
- preserve Object identity;
- produce appropriate Events;
- support traceability;
- maintain semantic consistency.

Invalid transitions shall be prevented through enterprise governance.

---

# Lifecycle Ownership

Each Operational Entity owns its own Lifecycle.

Processes coordinate Lifecycle progression but do not own the Lifecycle itself.

Ownership remains unchanged throughout the Lifecycle.

---

# Lifecycle Governance

Operational Lifecycles shall be governed through:

- Ownership;
- Policies;
- Constraints;
- Events;
- operational approvals.

Governance shall ensure predictable enterprise execution.

---

# Lifecycle Evolution

Operational Lifecycles may evolve through:

- additional business states;
- refined transition rules;
- compatibility-preserving improvements.

Breaking Lifecycle changes shall require explicit governance.

---

# Relationship to Other Specifications

Operational Lifecycles build upon:

- Lifecycle
- Object
- Event
- Policy
- Process
- Domain Governance

Additional Operations specifications define Lifecycles for individual Operational Entities.

---

# Independence

This specification does not prescribe:

- workflow engines;
- ERP systems;
- project management platforms;
- ticketing systems;
- implementation technologies.

Operational Lifecycles remain implementation independent.

---

# Conformance

A conforming Operations implementation shall:

- define Lifecycles for Operational Entities;
- preserve Object identity;
- govern Lifecycle transitions;
- emit appropriate Events;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

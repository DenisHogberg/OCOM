<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Support](README.md) / Support Lifecycles

[← Back](Support_KPIs.md) · [↑ Up](README.md) · [Next →](Support_Objects.md)

---
<!-- nav:end -->

# Support Lifecycles

**Document ID:** DOMAIN-SUPPORT-LIFECYCLES-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Lifecycle principles governing Support Objects.

Support Lifecycles define the controlled evolution of Support Objects from creation through completion while preserving Object identity, business meaning, governance, and enterprise interoperability.

Lifecycle semantics remain independent of implementation technologies.

---

# Definition

A Support Lifecycle defines the permissible business states and transitions of a Support Object.

Every Support Object participates in a governed Lifecycle throughout its existence.

Lifecycle semantics are defined by the Core Lifecycle specification.

---

# Business Meaning

Support Lifecycles ensure service interactions evolve predictably and consistently.

They provide a standardized model for managing Cases, Incidents, Service Requests, Resolutions, Knowledge Articles, and operational support activities across the enterprise.

---

# Design Principles

Support Lifecycles shall:

- preserve Object identity;
- define explicit business states;
- define governed state transitions;
- produce Support Events;
- support auditability;
- remain technology independent.

---

# Lifecycle Categories

Support Objects may define individual Lifecycles appropriate to their business purpose.

---

## Case Lifecycle

A typical Case Lifecycle may include:

- Draft
- Open
- Assigned
- In Progress
- Pending
- Escalated
- Resolved
- Closed
- Archived

A Case may transition between operational states as governed by Support Policies.

---

## Incident Lifecycle

A typical Incident Lifecycle may include:

- Reported
- Classified
- Prioritized
- Assigned
- Investigating
- Mitigated
- Resolved
- Closed

Major Incidents may include additional governed states.

---

## Service Request Lifecycle

A typical Service Request Lifecycle may include:

- Submitted
- Under Review
- Approved
- Assigned
- In Progress
- Fulfilled
- Closed
- Archived

Rejected requests terminate without fulfillment.

---

## Resolution Lifecycle

A typical Resolution Lifecycle may include:

- Proposed
- Reviewed
- Approved
- Applied
- Verified
- Completed
- Archived

Resolutions may be reused by future Cases.

---

## Knowledge Lifecycle

A typical Knowledge Article Lifecycle may include:

- Draft
- Under Review
- Approved
- Published
- Updated
- Retired
- Archived

Knowledge Articles preserve version history throughout their Lifecycle.

---

## Operational Lifecycle

Operational Objects such as Queues, Escalations, Assignments, and Support Sessions may define Lifecycles appropriate to their operational role.

Typical states include:

- Created
- Active
- Suspended
- Completed
- Archived

---

# Lifecycle Transitions

Lifecycle transitions shall:

- comply with applicable Policies;
- preserve Object identity;
- produce appropriate Events;
- maintain auditability;
- preserve semantic consistency.

Invalid transitions shall be prevented by enterprise governance.

---

# Lifecycle Ownership

Each Support Object owns its own Lifecycle.

Processes coordinate Lifecycle progression but do not own the Lifecycle itself.

Ownership remains unchanged throughout the Lifecycle.

---

# Lifecycle Governance

Support Lifecycles shall be governed through:

- Ownership;
- Policies;
- Constraints;
- Events;
- business approvals.

Governance shall ensure predictable enterprise behavior.

---

# Lifecycle Evolution

Support Lifecycles may evolve through:

- additional business states;
- refined transition rules;
- compatibility-preserving improvements.

Breaking Lifecycle changes shall require explicit governance.

---

# Relationship to Other Specifications

Support Lifecycles build upon:

- Lifecycle
- Object
- Event
- Policy
- Process
- Domain Governance

Additional Support specifications define Lifecycles for individual Object categories.

---

# Independence

This specification does not prescribe:

- workflow engines;
- ticketing software;
- state machines;
- BPM systems;
- implementation technologies.

Support Lifecycles remain implementation independent.

---

# Conformance

A conforming Support implementation shall:

- define Lifecycles for Support Objects;
- preserve Object identity;
- govern Lifecycle transitions;
- emit appropriate Events;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

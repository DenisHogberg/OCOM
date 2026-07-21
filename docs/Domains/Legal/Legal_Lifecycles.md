<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Legal](README.md) / Legal Lifecycles

[← Back](Legal_KPIs.md) · [↑ Up](README.md) · [Next →](Legal_Objects.md)

---
<!-- nav:end -->

# Legal Lifecycles

**Document ID:** DOMAIN-LEGAL-LIFECYCLES-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Lifecycle principles governing Entities owned by the Legal Domain.

Legal Lifecycles define the controlled evolution of legal Entities while preserving Object identity, governance, auditability, and enterprise interoperability.

Lifecycle semantics remain independent of implementation technologies.

---

# Definition

A Legal Lifecycle defines the permissible business states and transitions of a Legal Entity.

Every Legal Entity participates in a governed Lifecycle throughout its existence.

Lifecycle semantics are defined by the Core Lifecycle specification.

---

# Business Meaning

Legal Lifecycles provide a consistent framework for managing Contracts, Agreements, Obligations, Legal Entities, Intellectual Property, Legal Matters, Claims, and Regulatory Objects.

They ensure legal changes occur predictably, consistently, and remain traceable throughout the enterprise.

---

# Design Principles

Legal Lifecycles shall:

- preserve Object identity;
- define explicit business states;
- define governed state transitions;
- produce Legal Events;
- support auditability;
- remain technology independent.

---

# Lifecycle Categories

Legal Entities may define individual Lifecycles appropriate to their business purpose.

---

## Contract Lifecycle

A typical Contract Lifecycle may include:

- Draft
- Under Review
- Approved
- Executed
- Active
- Amended
- Renewed
- Expired
- Terminated
- Archived

Contract identity shall remain preserved throughout the Lifecycle.

---

## Agreement Lifecycle

A typical Agreement Lifecycle may include:

- Proposed
- Negotiation
- Approved
- Executed
- Active
- Modified
- Completed
- Archived

Agreements may evolve independently from individual Contracts.

---

## Obligation Lifecycle

A typical Obligation Lifecycle may include:

- Defined
- Assigned
- Active
- Fulfilled
- Violated
- Waived
- Closed
- Archived

Obligations evolve independently of operational execution.

---

## Legal Entity Lifecycle

A typical Legal Entity Lifecycle may include:

- Registered
- Active
- Modified
- Reorganized
- Dissolved
- Archived

Legal Entity identity shall remain historically preserved.

---

## Intellectual Property Lifecycle

A typical Intellectual Property Lifecycle may include:

- Identified
- Registered
- Protected
- Licensed
- Transferred
- Retired
- Archived

Intellectual Property may outlive Products or commercial agreements.

---

## Legal Matter Lifecycle

Legal Matters may include:

- Opened
- Under Review
- Active
- Resolved
- Closed
- Archived

Legal Matters coordinate legal activities independently of Contracts.

---

## Dispute Lifecycle

Dispute Objects may include:

- Filed
- Under Review
- Negotiation
- Arbitration
- Litigation
- Settled
- Closed
- Archived

Dispute history shall remain historically traceable.

---

## Regulatory Lifecycle

Regulatory Objects may include:

- Draft
- Submitted
- Under Review
- Approved
- Effective
- Expired
- Archived

Regulatory Lifecycles support enterprise legal governance.

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

Each Legal Entity owns its own Lifecycle.

Processes coordinate Lifecycle progression but do not own the Lifecycle itself.

Ownership remains unchanged throughout the Lifecycle.

---

# Lifecycle Governance

Legal Lifecycles shall be governed through:

- Ownership;
- Policies;
- Constraints;
- Events;
- legal approvals.

Governance shall ensure predictable legal evolution.

---

# Lifecycle Evolution

Legal Lifecycles may evolve through:

- additional business states;
- refined transition rules;
- compatibility-preserving improvements.

Breaking Lifecycle changes shall require explicit governance.

---

# Relationship to Other Specifications

Legal Lifecycles build upon:

- Lifecycle
- Object
- Event
- Policy
- Process
- Domain Governance

Additional Legal specifications define Lifecycles for individual Legal Entities.

---

# Independence

This specification does not prescribe:

- contract management systems;
- workflow engines;
- document repositories;
- electronic signature platforms;
- implementation technologies.

Legal Lifecycles remain implementation independent.

---

# Conformance

A conforming Legal implementation shall:

- define Lifecycles for Legal Entities;
- preserve Object identity;
- govern Lifecycle transitions;
- emit appropriate Events;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

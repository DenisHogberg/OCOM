<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [HR](README.md) / Human Resources Lifecycles

[← Back](HR_KPIs.md) · [↑ Up](README.md) · [Next →](HR_Objects.md)

---
<!-- nav:end -->

# Human Resources Lifecycles

**Document ID:** DOMAIN-HR-LIFECYCLES-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Lifecycle principles governing Entities owned by the Human Resources (HR) Domain.

HR Lifecycles define the controlled evolution of workforce-related Entities while preserving Object identity, governance, auditability, and enterprise interoperability.

Lifecycle semantics remain independent of implementation technologies.

---

# Definition

An HR Lifecycle defines the permissible business states and transitions of an HR Entity.

Every HR Entity participates in a governed Lifecycle throughout its existence.

Lifecycle semantics are defined by the Core Lifecycle specification.

---

# Business Meaning

HR Lifecycles provide a consistent framework for managing employees, organizational structures, positions, competencies, development, and workforce planning.

They ensure workforce changes occur predictably and remain traceable throughout the enterprise.

---

# Design Principles

HR Lifecycles shall:

- preserve Object identity;
- define explicit business states;
- define governed state transitions;
- produce HR Events;
- support auditability;
- remain technology independent.

---

# Lifecycle Categories

HR Entities may define individual Lifecycles appropriate to their business purpose.

---

## Employee Lifecycle

A typical Employee Lifecycle may include:

- Candidate
- Hired
- Onboarding
- Active
- Leave of Absence
- Returning
- Offboarding
- Former Employee
- Archived

Employee identity shall remain preserved throughout the Lifecycle.

---

## Employment Lifecycle

A typical Employment Lifecycle may include:

- Proposed
- Approved
- Active
- Modified
- Suspended
- Resumed
- Completed
- Archived

Employment may evolve independently from the Employee Object.

---

## Position Lifecycle

A typical Position Lifecycle may include:

- Planned
- Approved
- Open
- Filled
- Vacant
- Retired
- Archived

Positions exist independently of the Employees occupying them.

---

## Organizational Unit Lifecycle

A typical Organizational Unit Lifecycle may include:

- Proposed
- Approved
- Active
- Reorganized
- Merged
- Closed
- Archived

Organizational changes shall preserve historical traceability.

---

## Competency Lifecycle

A typical Competency Lifecycle may include:

- Defined
- Validated
- Active
- Updated
- Deprecated
- Archived

Competencies evolve independently of Employees.

---

## Development Lifecycle

Development Objects such as Training Programs and Development Plans may include:

- Planned
- Assigned
- In Progress
- Completed
- Reviewed
- Archived

Development supports continuous workforce improvement.

---

## Performance Lifecycle

Performance Objects may include:

- Planned
- Active
- Evaluated
- Reviewed
- Closed
- Archived

Performance history shall remain historically traceable.

---

## Planning Lifecycle

Planning Objects may include:

- Draft
- Under Review
- Approved
- Active
- Completed
- Archived

Planning Lifecycles support workforce strategy.

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

Each HR Entity owns its own Lifecycle.

Processes coordinate Lifecycle progression but do not own the Lifecycle itself.

Ownership remains unchanged throughout the Lifecycle.

---

# Lifecycle Governance

HR Lifecycles shall be governed through:

- Ownership;
- Policies;
- Constraints;
- Events;
- business approvals.

Governance shall ensure predictable workforce evolution.

---

# Lifecycle Evolution

HR Lifecycles may evolve through:

- additional business states;
- refined transition rules;
- compatibility-preserving improvements.

Breaking Lifecycle changes shall require explicit governance.

---

# Relationship to Other Specifications

HR Lifecycles build upon:

- Lifecycle
- Object
- Event
- Policy
- Process
- Domain Governance

Additional HR specifications define Lifecycles for individual workforce Objects.

---

# Independence

This specification does not prescribe:

- HR software;
- workflow engines;
- payroll systems;
- directory services;
- implementation technologies.

HR Lifecycles remain implementation independent.

---

# Conformance

A conforming HR implementation shall:

- define Lifecycles for HR Entities;
- preserve Object identity;
- govern Lifecycle transitions;
- emit appropriate Events;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

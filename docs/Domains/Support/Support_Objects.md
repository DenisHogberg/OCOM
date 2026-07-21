<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Support](README.md) / Support Objects

[← Back](Support_Lifecycles.md) · [↑ Up](README.md) · [Next →](Support_Policies.md)

---
<!-- nav:end -->

# Support Objects

**Document ID:** DOMAIN-SUPPORT-OBJECTS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Entities owned by the Support Domain.

Support Objects represent enterprise service interactions used to receive, investigate, coordinate, resolve, and document operational issues while preserving Object Ownership and enterprise interoperability.

Objects remain stable business concepts independent of implementation technologies.

---

# Definition

A Support Object is a business entity owned by the Support Domain.

Support Objects describe service interactions, operational issues, resolution activities, support knowledge, and service coordination.

Object semantics are defined by the Core Object specification.

---

# Business Meaning

Support Objects provide a consistent representation of enterprise support operations.

They enable organizations to deliver reliable customer assistance while maintaining governance, traceability, and accountability throughout the service lifecycle.

---

# Design Principles

Support Objects shall:

- possess stable business identity;
- preserve Object Ownership;
- participate in governed Lifecycles;
- support Relationships with other Objects;
- produce Events throughout their Lifecycles;
- remain technology independent.

---

# Object Categories

Support Objects may be organized into the following categories.

---

## Case Objects

Objects representing managed support activities.

Examples include:

- Case;
- Support Case;
- Customer Case;
- Internal Case;
- Case Portfolio.

---

## Incident Objects

Objects representing operational disruptions.

Examples include:

- Incident;
- Service Incident;
- Product Incident;
- Operational Incident;
- Major Incident.

Incidents describe service-impacting events rather than technical monitoring alerts.

---

## Service Request Objects

Objects representing requests for assistance.

Examples include:

- Service Request;
- Support Request;
- Information Request;
- Change Request;
- Access Request.

---

## Resolution Objects

Objects representing issue resolution.

Examples include:

- Resolution;
- Resolution Plan;
- Workaround;
- Corrective Action;
- Root Cause Analysis.

---

## Knowledge Objects

Objects representing reusable support knowledge.

Examples include:

- Knowledge Article;
- Troubleshooting Guide;
- FAQ;
- Resolution Template;
- Diagnostic Procedure.

---

## Operational Objects

Objects supporting service operations.

Examples include:

- Support Queue;
- Escalation;
- Service Task;
- Assignment;
- Support Session.

---

# Object Ownership

The Support Domain owns Support Objects.

Ownership includes:

- identity;
- lifecycle;
- governance;
- business semantics.

Other Domains may reference Support Objects without assuming Ownership.

---

# Cross-Domain Relationships

Support Objects commonly relate to:

- Customers;
- Products;
- Payments;
- Contracts;
- Compliance Assessments;
- Knowledge Assets;
- KPIs.

Relationships do not transfer Ownership.

---

# Object Governance

Support Objects shall be governed through:

- Ownership;
- Lifecycles;
- Policies;
- Relationships;
- Events.

Governance shall preserve consistency and traceability.

---

# Object Evolution

Support Objects may evolve through:

- additional attributes;
- refined classifications;
- compatibility-preserving enhancements;
- expanded Relationships.

Object identity shall remain stable throughout evolution.

---

# Relationship to Other Specifications

Support Objects build upon:

- Object
- Relationship
- Lifecycle
- Event
- Policy
- Domain Governance

Additional Support specifications define the behavior of individual Object categories.

---

# Independence

This specification does not prescribe:

- help desk software;
- ticketing systems;
- IT service management platforms;
- customer support software;
- implementation technologies.

Support Objects remain implementation independent.

---

# Conformance

A conforming Support implementation shall:

- define owned Support Objects;
- preserve Object Ownership;
- assign governed Lifecycles;
- support standardized Relationships;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

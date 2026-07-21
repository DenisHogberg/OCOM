<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [CRM](README.md) / CRM Objects

[← Back](CRM%20Lifecycles.md) · [↑ Up](README.md) · [Next →](CRM%20Policies.md)

---
<!-- nav:end -->

# CRM Objects

**Document ID:** DOMAIN-CRM-OBJECTS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the business Objects managed by the CRM Domain.

CRM Objects represent the entities required to establish, maintain, and improve customer relationships throughout the customer lifecycle.

These Objects form the operational foundation of the CRM Domain.

---

# Definition

A CRM Object is a business Object owned or governed by the CRM Domain for the purpose of managing customer relationships and engagement.

CRM Objects participate in enterprise operations while preserving their Identity, Lifecycle, and governance.

---

# Business Meaning

CRM Objects provide a consistent representation of customer relationships across the enterprise.

They enable customer engagement without duplicating responsibilities already owned by other Domains.

---

# Design Principles

CRM Objects shall:

- represent business concepts;
- have explicit ownership;
- possess persistent Identity;
- participate in defined Lifecycles;
- support interoperability;
- remain technology independent.

---

# Object Categories

CRM Objects may be organized into the following categories.

## Customer Objects

Objects representing customers and customer profiles.

Examples include:

- Customer
- Customer Profile
- Customer Segment
- Customer Preference

---

## Communication Objects

Objects representing customer communications.

Examples include:

- Communication
- Communication Channel
- Message
- Conversation

---

## Engagement Objects

Objects representing customer engagement activities.

Examples include:

- Campaign Participation
- Interaction
- Customer Journey
- Engagement Record

---

## Relationship Objects

Objects representing long-term customer relationships.

Examples include:

- Relationship
- Loyalty Membership
- Customer Status
- Customer Portfolio

---

# Object Ownership

The CRM Domain owns CRM-specific Objects.

A CRM Object shall have one owning Domain.

Objects owned by other Domains may be referenced but shall not become CRM-owned Objects.

---

# Object Relationships

CRM Objects may establish Relationships with Objects owned by other Domains.

Examples include:

- Customer ↔ Account
- Customer ↔ Payment Method
- Customer ↔ Product
- Customer ↔ Support Case

Relationship ownership remains explicit.

---

# Object Lifecycle

Every CRM Object shall participate in an explicitly defined Lifecycle.

Lifecycle definitions are provided in the CRM Lifecycle specification.

---

# Object Governance

CRM Objects shall be governed through:

- Policies;
- Constraints;
- Ownership;
- Contracts;
- Lifecycle management.

Governance ensures operational consistency.

---

# Object Evolution

CRM Objects may evolve through:

- attribute additions;
- capability expansion;
- relationship refinement;
- policy updates.

Evolution shall preserve Identity and compatibility whenever practical.

---

# Relationship to Other Specifications

CRM Objects build upon:

- Domain
- Domain Architecture
- Meta/Object
- Identity
- Relationship
- Lifecycle
- Policy
- Constraint

Additional CRM specifications further specialize these Objects.

---

# Independence

The CRM Objects specification does not prescribe:

- CRM software;
- databases;
- implementation technologies;
- storage models.

CRM Objects remain logical business Objects independent of implementation.

---

# Conformance

A conforming CRM implementation shall:

- define managed CRM Objects;
- preserve Object Identity;
- establish explicit ownership;
- support Lifecycle management;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

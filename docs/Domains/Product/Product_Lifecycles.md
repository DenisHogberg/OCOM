<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Product](README.md) / Product Lifecycles

[← Back](Product_KPIs.md) · [↑ Up](README.md) · [Next →](Product_Objects.md)

---
<!-- nav:end -->

# Product Lifecycles

**Document ID:** DOMAIN-PRODUCT-LIFECYCLES-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines Lifecycle principles applicable to Product Objects managed by the Product Domain.

Lifecycles describe the progression of Product Objects through governed business states from creation to retirement while preserving Object Identity, Ownership, commercial consistency, and enterprise interoperability.

Lifecycle semantics are defined independently of implementation technologies.

---

# Definition

A Product Lifecycle defines the governed sequence of business states through which a Product Object progresses during its existence.

Lifecycle transitions represent changes in commercial availability and governance rather than customer activity or operational execution.

Lifecycle semantics are defined by the Core specification.

---

# Business Meaning

Product Lifecycles provide a standardized representation of the maturity and availability of enterprise offerings.

They enable organizations to consistently introduce, evolve, publish, suspend, and retire Products while preserving commercial integrity across the enterprise.

---

# Design Principles

Product Lifecycles shall:

- preserve Object Identity;
- preserve Object Ownership;
- consist of explicitly defined business states;
- support governed state transitions;
- remain traceable;
- remain technology independent.

---

# Typical Lifecycle States

Product Objects may progress through states such as:

- Draft;
- Defined;
- Under Review;
- Approved;
- Published;
- Active;
- Suspended;
- Retired;
- Archived.

Organizations may define additional states consistent with business requirements.

---

# Example Lifecycles

## Product

Typical progression:

```text
Draft
   │
   ▼
Defined
   │
   ▼
Under Review
   │
   ▼
Approved
   │
   ▼
Published
   │
   ▼
Active
   │
 ┌─┴────────┐
 ▼          ▼
Suspended Retired
     │
     ▼
 Archived
```

---

## Commercial Offering

Typical progression:

```text
Draft
   │
   ▼
Configured
   │
   ▼
Approved
   │
   ▼
Published
   │
 ┌─┴────────┐
 ▼          ▼
Withdrawn Expired
     │
     ▼
 Archived
```

---

## Subscription Plan

Typical progression:

```text
Draft
   │
   ▼
Configured
   │
   ▼
Approved
   │
   ▼
Available
   │
 ┌─┴────────┐
 ▼          ▼
Suspended Retired
     │
     ▼
 Archived
```

---

## Bundle

Typical progression:

```text
Draft
   │
   ▼
Configured
   │
   ▼
Published
   │
 ┌─┴────────┐
 ▼          ▼
Updated  Retired
     │
     ▼
 Archived
```

---

# Lifecycle Ownership

Each Product Object shall have one Lifecycle.

The Product Domain owns Lifecycle definitions for Product Objects.

Referenced Objects owned by other Domains retain the Lifecycles defined by their respective Domains.

---

# Lifecycle Transitions

Lifecycle transitions shall:

- be explicitly governed;
- preserve Object Identity;
- comply with applicable Policies;
- produce appropriate Events where required.

Transition authorization is organization-specific.

---

# Lifecycle Governance

Product Lifecycles shall be governed through:

- Ownership;
- Policies;
- Constraints;
- commercial approval;
- version management.

Governance ensures enterprise-wide commercial consistency.

---

# Lifecycle Evolution

Product Lifecycles may evolve through:

- additional business states;
- refined commercial models;
- compatibility-preserving enhancements.

Breaking Lifecycle changes shall require explicit governance.

---

# Relationship to Other Specifications

Product Lifecycles build upon:

- Lifecycle
- Object
- Event
- Policy
- Relationship
- Domain Governance

Additional Product specifications define the Objects using these Lifecycles.

---

# Independence

This specification does not prescribe:

- product lifecycle management software;
- catalog platforms;
- workflow engines;
- implementation technologies.

Lifecycles remain logical business state models independent of implementation.

---

# Conformance

A conforming Product implementation shall:

- define governed Lifecycles for Product Objects;
- preserve Object Identity;
- preserve Object Ownership;
- support governed state transitions;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

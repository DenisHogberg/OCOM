<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [PSP](README.md) / PSP

[↑ Up](README.md)

---
<!-- nav:end -->

# PSP

**Document ID:** Entity-004

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the PSP (Payment Service Provider) Entity.

The PSP Entity represents an organization or service responsible for processing, authorizing, routing, settling, or facilitating payment operations.

---

# Definition

A Payment Service Provider (PSP) is an operational entity representing an external or internal payment processing service that enables payment execution.

A PSP provides payment capabilities but does not represent the payment itself.

---

# Business Meaning

A PSP acts as an operational participant responsible for enabling value transfer between parties.

A PSP may perform payment authorization, routing, settlement, fraud prevention, reconciliation, or related financial services.

The PSP represents a business participant rather than a software integration or API.

---

# Core Principles

A PSP:

- shall have a unique identity;
- shall provide one or more payment services;
- shall belong to exactly one primary Domain;
- may process multiple Payments;
- may participate in multiple Transactions;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Name | PSP name |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Provider Type | Payment gateway, acquirer, processor, etc. |
| Supported Currencies | Accepted currencies |
| Supported Payment Methods | Available payment methods |
| Region | Operating region |
| External Reference | External identifier |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every PSP shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every PSP shall belong to exactly one primary Domain.

---

# States

A PSP may include the following operational states:

- Registered
- Active
- Suspended
- Restricted
- Retired
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The PSP Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

A PSP may establish relationships with:

- Payment
- Transaction
- Wallet
- Vendor
- Partner
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a PSP include:

- PSP Registered
- PSP Activated
- PSP Updated
- PSP Suspended
- PSP Retired

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing PSPs are implementation-specific.

Examples include:

- supported payment methods;
- settlement schedules;
- processing fees;
- regional restrictions;
- compliance requirements.

---

# Invariants

The following conditions shall always remain true.

- Every PSP shall have exactly one Identifier.
- Every PSP shall belong to exactly one primary Domain.
- Every PSP shall follow one defined Lifecycle.
- Every PSP shall have one current State.

---

# Constraints

A PSP shall never:

- exist without an Identifier;
- exist without a Lifecycle;
- exist without a State;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

A PSP conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

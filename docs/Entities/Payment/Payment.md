<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Payment](README.md) / Payment

[↑ Up](README.md)

---
<!-- nav:end -->

# Payment

**Document ID:** Entity-001

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Payment Entity.

Payment is one of the fundamental operational entities used to represent the transfer of value within an operational model.

---

# Definition

A Payment is an operational entity representing the transfer of value between participating entities under defined business rules.

A Payment exists independently of implementation technologies and remains identifiable throughout its operational lifecycle.

---

# Business Meaning

A Payment represents the commitment, movement, or settlement of value between parties.

It provides a consistent operational representation of value transfer regardless of industry, technology, financial institution, or implementation method.

Payment is a business concept rather than a software object or financial protocol.

---

# Core Principles

A Payment:

- represents a transfer of value;
- shall have a unique identity;
- shall follow a defined lifecycle;
- shall exist in one operational state at any given time;
- shall be governed by exactly one primary Domain;
- may participate in multiple operational relationships;
- shall remain traceable throughout its lifecycle.

---

# Mandatory Attributes

Every Payment shall define the following attributes.

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity of the Payment |
| Amount | Value being transferred |
| Currency | Currency associated with the value |
| State | Current operational state |
| Lifecycle | Lifecycle governing the Payment |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

A Payment may define additional attributes including, but not limited to:

| Attribute | Description |
|------------|-------------|
| External Reference | Identifier in an external system |
| Description | Human-readable description |
| Fee | Processing fee |
| Exchange Rate | Applied exchange rate |
| Metadata | Additional implementation-specific information |
| Completed At | Completion timestamp |
| Expiration Time | Optional expiration |

---

# Ownership

Every Payment shall have one responsible Owner.

The Owner is accountable for operational governance, consistency, and lifecycle integrity.

---

# Domain

Every Payment shall belong to exactly one primary Domain.

The governing Domain defines operational rules and ownership.

---

# States

A Payment may include the following operational states:

- Created
- Pending
- Authorized
- Processing
- Completed
- Failed
- Cancelled
- Refunded
- Expired

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Payment Lifecycle defines all valid transitions between operational states.

Every transition shall be explicitly defined.

Undefined transitions are prohibited.

---

# Relationships

A Payment may establish relationships with:

- Account
- Customer
- Invoice
- Order
- Contract
- Transaction
- Balance
- Settlement
- Refund

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Payment include:

- Payment Created
- Payment Authorized
- Payment Started
- Payment Completed
- Payment Failed
- Payment Cancelled
- Payment Refunded
- Payment Expired

Events represent immutable operational facts.

---

# Invariants

The following conditions shall always remain true.

- Every Payment shall have exactly one Identifier.
- Amount shall be defined.
- Currency shall be defined.
- A completed Payment shall not return to Created.
- A cancelled Payment shall not become Completed unless explicitly permitted by the Lifecycle.
- Every State shall belong to the defined Lifecycle.
- Every Payment shall belong to exactly one primary Domain.

---

# Constraints

A Payment shall never:

- exist without an Identifier;
- exist without an Amount;
- exist without a Currency;
- exist without a Lifecycle;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

A Payment conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

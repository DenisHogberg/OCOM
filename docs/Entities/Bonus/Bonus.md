<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Bonus](README.md) / Bonus

[↑ Up](README.md)

---
<!-- nav:end -->

# Bonus

**Document ID:** Entity-009

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Bonus Entity.

The Bonus Entity represents an incentive granted to an eligible participant under predefined business conditions.

---

# Definition

A Bonus is an operational entity representing value granted in addition to a standard commercial transaction or business relationship.

A Bonus may consist of monetary value, credits, rewards, discounts, privileges, or other incentives intended to encourage or reward specific behaviors.

---

# Business Meaning

A Bonus represents conditional value.

Unlike a Payment, which transfers agreed value, a Bonus represents additional value granted according to defined business rules.

A Bonus exists independently of the mechanism used to calculate or deliver it.

---

# Core Principles

A Bonus:

- shall have a unique identity;
- shall define a measurable value;
- shall be governed by explicit business conditions;
- may be associated with one or more Offers;
- may be granted to one or more eligible entities;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Type | Classification of the Bonus |
| Value | Granted value |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Currency | Currency of the granted value |
| Valid From | Start of validity |
| Valid Until | End of validity |
| Eligibility Rules | Conditions for receiving the Bonus |
| Redemption Rules | Conditions for using the Bonus |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every Bonus shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Bonus shall belong to exactly one primary Domain.

---

# States

A Bonus may include the following operational states:

- Draft
- Available
- Granted
- Active
- Redeemed
- Expired
- Cancelled
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Bonus Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

A Bonus may establish relationships with:

- Offer
- Campaign
- Affiliate
- Partner
- Payment
- Transaction
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Bonus include:

- Bonus Created
- Bonus Granted
- Bonus Activated
- Bonus Redeemed
- Bonus Expired
- Bonus Cancelled

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Bonuses are implementation-specific.

Examples include:

- eligibility criteria;
- expiration policies;
- redemption requirements;
- usage limits;
- promotional restrictions.

---

# Invariants

The following conditions shall always remain true.

- Every Bonus shall have exactly one Identifier.
- Every Bonus shall belong to exactly one primary Domain.
- Every Bonus shall have one current State.
- Every Bonus shall follow one defined Lifecycle.
- Every Bonus shall define granted value.

---

# Constraints

A Bonus shall never:

- exist without an Identifier;
- exist without a Value;
- exist without a Lifecycle;
- exist without a State;
- violate its defined Lifecycle.

---

# Conformance

A Bonus conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

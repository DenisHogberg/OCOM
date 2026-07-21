<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Wallet](README.md) / Wallet

[↑ Up](README.md)

---
<!-- nav:end -->

# Wallet

**Document ID:** Entity-003

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Wallet Entity.

Wallet represents a container that maintains the current balance of value owned or controlled by an entity.

---

# Definition

A Wallet is an operational entity representing a managed store of value.

A Wallet maintains the current balance and records the effects of Transactions without representing the Transactions themselves.

---

# Business Meaning

A Wallet provides the operational representation of available value.

Unlike a Payment, which transfers value, and a Transaction, which records an operational action, a Wallet represents the current state of value held by an entity.

A Wallet is a business concept independent of implementation technology or storage mechanisms.

---

# Core Principles

A Wallet:

- shall have a unique identity;
- shall maintain a current balance;
- shall belong to exactly one primary owner;
- shall follow a defined lifecycle;
- shall belong to exactly one primary Domain;
- may participate in multiple Transactions;
- shall remain traceable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Balance | Current value stored |
| Currency | Wallet currency |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Available Balance | Available funds |
| Reserved Balance | Reserved funds |
| Credit Limit | Optional credit limit |
| Description | Human-readable description |
| Metadata | Additional implementation-specific information |
| Updated At | Last modification timestamp |

---

# Ownership

Every Wallet shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Wallet shall belong to exactly one primary Domain.

---

# States

A Wallet may include the following operational states:

- Created
- Active
- Suspended
- Locked
- Closed
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Wallet Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

A Wallet may establish relationships with:

- Transaction
- Payment
- Player
- Partner
- Vendor
- PSP
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Wallet include:

- Wallet Created
- Wallet Activated
- Wallet Balance Updated
- Wallet Locked
- Wallet Suspended
- Wallet Closed

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Wallets are implementation-specific.

Examples include:

- overdraft policy;
- balance limits;
- reservation rules;
- expiration policy;
- reconciliation procedures.

---

# Invariants

The following conditions shall always remain true.

- Every Wallet shall have exactly one Identifier.
- Every Wallet shall have one current State.
- Every Wallet shall belong to exactly one primary Domain.
- Every Wallet shall follow one defined Lifecycle.
- Every Wallet shall maintain one currency.
- Balance modifications shall occur only through valid operational Transactions.

---

# Constraints

A Wallet shall never:

- exist without an Identifier;
- exist without a Currency;
- exist without a Lifecycle;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

A Wallet conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Transaction](README.md) / Transaction

[↑ Up](README.md)

---
<!-- nav:end -->

# Transaction

**Document ID:** Entity-002

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Transaction Entity.

Transaction represents an immutable operational record describing a completed business operation that changes the state of one or more entities.

---

# Definition

A Transaction is an operational entity representing a recorded change of state within an operational system.

A Transaction documents that a business operation has occurred and provides a permanent record of that operation.

---

# Business Meaning

A Transaction captures the execution of an operational action.

Unlike a Payment, which represents the transfer of value, a Transaction represents the operational fact that a business action has been performed.

Transactions establish traceability, accountability, and auditability across the operational model.

---

# Core Principles

A Transaction:

- shall have a unique identity;
- shall represent one completed operational action;
- shall be immutable once recorded;
- shall remain traceable throughout its lifecycle;
- shall belong to exactly one primary Domain;
- may reference one or more related entities.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Type | Operational transaction type |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Timestamp | Time the transaction occurred |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Reference | External reference |
| Payment Reference | Associated Payment |
| Description | Human-readable description |
| Metadata | Additional implementation-specific information |
| Source System | Originating system |
| Correlation Identifier | Identifier linking related operations |

---

# Ownership

Every Transaction shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Transaction shall belong to exactly one primary Domain.

---

# States

A Transaction may include the following operational states:

- Created
- Pending
- Executed
- Failed
- Reversed
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Transaction Lifecycle defines all valid transitions between operational states.

Undefined transitions are prohibited.

---

# Relationships

A Transaction may establish relationships with:

- Payment
- Wallet
- Player
- Partner
- Vendor
- PSP
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Transaction include:

- Transaction Created
- Transaction Executed
- Transaction Failed
- Transaction Reversed
- Transaction Archived

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Transactions are implementation-specific.

Examples include:

- authorization requirements;
- reconciliation procedures;
- settlement windows;
- accounting policies;
- retention periods.

---

# Invariants

The following conditions shall always remain true.

- Every Transaction shall have exactly one Identifier.
- Every Transaction shall have one current State.
- Every Transaction shall belong to exactly one primary Domain.
- Every Transaction shall follow one defined Lifecycle.
- An Executed Transaction shall be immutable.
- A Reversed Transaction shall preserve the original Transaction history.

---

# Constraints

A Transaction shall never:

- exist without an Identifier;
- exist without a Lifecycle;
- exist without a State;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

A Transaction conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

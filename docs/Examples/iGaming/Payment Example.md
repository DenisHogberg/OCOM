<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Payment Example

[← Back](KYC%20Case%20Example.md) · [↑ Up](README.md) · [Next →](Responsible%20Gaming%20Case.md)

---
<!-- nav:end -->

# Payment Example

**Document ID:** EXAMPLES-IGAMING-PAYMENT-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Payment is represented as an Entity within the OCOM Specification.

The example illustrates how a Payment coordinates financial operations across multiple enterprise Domains while preserving ownership, governance, traceability, and operational integrity.

This example is informative and does not define normative behavior.

---

# Business Context

A Payment represents a regulated financial operation performed by a Player through an Account and Wallet.

Multiple enterprise Domains participate in processing the Payment, including Payments, Finance, Compliance, Fraud, Customer Support, BI, and AI.

The Payment remains a single Entity throughout its lifecycle.

---

# Entity

Object Type

Payment

Primary Owner

Payments Domain

---

# Identity

Example Identifier

```
PAY-500781
```

Payment Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Payment belongs to Wallet.
- Payment belongs to Account.
- Payment belongs indirectly to Player.
- Payment is processed by Payment Provider.
- Payment may generate Financial Ledger Entry.
- Payment may become subject to Fraud Case.
- Payment may require Compliance Review.
- Payment may create Support Case.

Relationships do not transfer Payment ownership.

---

# Lifecycle

Example lifecycle:

```text
Created
    │
    ▼
Authorized
    │
    ▼
Processing
    │
    ▼
Completed
```

Alternative outcomes:

```text
Processing
    │
    ├── Failed
    │
    ├── Cancelled
    │
    └── Refunded
```

Each transition is governed by organizational Policies.

---

# Events

Example Business Events include:

- Payment Created
- Payment Authorized
- Payment Submitted
- Payment Completed
- Payment Failed
- Payment Cancelled
- Payment Refunded

Business Events establish an immutable financial history.

---

# Capabilities

Example Capabilities include:

- Create Payment
- Authorize Payment
- Submit Payment
- Complete Payment
- Cancel Payment
- Refund Payment

Capabilities execute business operations on the Payment.

---

# Policies

Example Policies include:

- Payment authorization shall precede processing.
- Regulatory checks shall complete before settlement.
- Completed Payments shall remain immutable.
- Refunds shall require authorization.
- Every Payment operation shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- provider observations;
- reconciliation notes;
- operational investigations;
- dispute history;
- fraud indicators;
- supporting evidence;
- AI recommendations.

Operational Memory complements the Payment without modifying financial facts.

---

# AI Participation

AI may:

- detect payment anomalies;
- estimate fraud probability;
- recommend routing optimization;
- identify failed payment patterns;
- recommend manual investigation.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Payment remains the authoritative Entity representing a financial operation while preserving:

- single ownership;
- lifecycle integrity;
- immutable financial history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted analysis.

---

# Related Specifications

- Wallet Example
- Account Example
- Player Example
- Meta/Object
- Meta/Event
- Meta/Lifecycle
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Wallet Example

[← Back](Support%20Case%20Example.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Wallet Example

**Document ID:** EXAMPLES-IGAMING-WALLET-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Wallet is represented as an Entity within the OCOM Specification.

The example illustrates how a Wallet manages monetary value independently while remaining associated with an Account and participating in regulated financial operations.

This example is informative and does not define normative behavior.

---

# Business Context

A Wallet represents the financial container through which an Account performs monetary transactions.

The Wallet maintains balances, supports financial operations, and serves as the authoritative source for available funds.

The Wallet is governed independently from the Player and Account Entities.

---

# Entity

Object Type

Wallet

Primary Owner

Wallet Management Domain

---

# Identity

Example Identifier

```
WAL-300184
```

Wallet Identity uniquely identifies the Wallet throughout its lifecycle.

---

# Relationships

Example relationships include:

- Wallet belongs to Account.
- Wallet belongs indirectly to Player.
- Wallet receives Deposits.
- Wallet funds Game Sessions.
- Wallet issues Withdrawals.
- Wallet receives Bonus Credits.
- Wallet records Financial Adjustments.

Relationships do not transfer Wallet ownership.

---

# Lifecycle

Example lifecycle:

```text
Created
    │
    ▼
Active
    │
    ▼
Restricted
    │
    ▼
Frozen
    │
    ▼
Closed
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Wallet Created
- Funds Deposited
- Funds Withdrawn
- Bonus Credited
- Balance Adjusted
- Wallet Frozen
- Wallet Closed

Business Events provide an immutable financial history.

---

# Capabilities

Example Capabilities include:

- Create Wallet
- Credit Wallet
- Debit Wallet
- Freeze Wallet
- Unfreeze Wallet
- Close Wallet

Capabilities execute financial operations according to applicable Policies.

---

# Policies

Example Policies include:

- Wallet balances shall remain consistent.
- Financial operations shall be auditable.
- Restricted Wallets shall not perform prohibited operations.
- Balance adjustments shall require authorization.
- Every financial transaction shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- transaction investigations;
- operational observations;
- reconciliation notes;
- fraud indicators;
- AI recommendations;
- evidence references.

Operational Memory supplements financial operations without changing authoritative balances.

---

# AI Participation

AI may:

- identify unusual transaction patterns;
- estimate fraud probability;
- recommend financial reviews;
- detect operational anomalies;
- summarize Wallet activity.

AI shall not modify Wallet balances.

---

# Expected Outcome

The Wallet remains the authoritative Entity for monetary value while preserving:

- independent ownership;
- governed lifecycle;
- immutable financial history;
- policy compliance;
- operational traceability;
- enterprise memory.

---

# Related Specifications

- Account Example
- Payment Example
- Meta/Object
- Meta/Lifecycle
- Meta/Event
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

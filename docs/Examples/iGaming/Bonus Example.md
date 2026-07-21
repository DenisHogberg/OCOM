<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Bonus Example

[← Back](Affiliate%20Example.md) · [↑ Up](README.md) · [Next →](Campaign%20Example.md)

---
<!-- nav:end -->

# Bonus Example

**Document ID:** EXAMPLES-IGAMING-BONUS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Bonus is represented as an Entity within the OCOM Specification.

The example illustrates how a Bonus is managed independently while interacting with Players, Accounts, Wallets, Campaigns, and Payments through governed business relationships.

This example is informative and does not define normative behavior.

---

# Business Context

A Bonus represents a promotional entitlement offered to a Player.

A Bonus progresses through its own lifecycle, may be subject to eligibility rules, wagering requirements, expiration policies, and financial constraints.

The Bonus remains an independent Entity regardless of how it is delivered or consumed.

---

# Entity

Object Type

Bonus

Primary Owner

Bonus Management Domain

---

# Identity

Example Identifier

```
BON-400592
```

Bonus Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Bonus is assigned to Player.
- Bonus is associated with Account.
- Bonus may credit Wallet.
- Bonus originates from Campaign.
- Bonus may require Payment.
- Bonus may generate Bonus Transactions.
- Bonus may become subject to Fraud Review.

Relationships do not transfer Bonus ownership.

---

# Lifecycle

Example lifecycle:

```text
Created
    │
    ▼
Assigned
    │
    ▼
Activated
    │
    ▼
Consumed
```

Alternative outcomes:

```text
Assigned
    │
    ├── Expired
    │
    ├── Cancelled
    │
    └── Revoked
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Bonus Created
- Bonus Assigned
- Bonus Activated
- Bonus Credited
- Bonus Consumed
- Bonus Expired
- Bonus Revoked

Business Events establish an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Create Bonus
- Assign Bonus
- Activate Bonus
- Credit Bonus
- Consume Bonus
- Expire Bonus
- Revoke Bonus

Capabilities execute business operations on the Bonus.

---

# Policies

Example Policies include:

- Eligibility requirements shall be satisfied before assignment.
- Wagering conditions shall be enforced.
- Expiration rules shall be evaluated automatically.
- Revocation shall be auditable.
- Every Bonus operation shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- eligibility evaluations;
- fraud observations;
- campaign effectiveness;
- customer interaction history;
- operational recommendations;
- AI assessments.

Operational Memory supplements the Bonus without changing its authoritative business state.

---

# AI Participation

AI may:

- recommend personalized bonuses;
- identify bonus abuse;
- estimate campaign effectiveness;
- detect unusual redemption patterns;
- recommend bonus optimization.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Bonus remains an independent Entity while preserving:

- single ownership;
- governed lifecycle;
- immutable operational history;
- policy compliance;
- enterprise traceability;
- operational memory;
- AI-assisted optimization.

---

# Related Specifications

- Player Example
- Wallet Example
- Payment Example
- Campaign Example
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

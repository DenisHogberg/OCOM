<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Player Example

[← Back](Campaign%20Example.md) · [↑ Up](README.md) · [Next →](Fraud%20Case%20Example.md)

---
<!-- nav:end -->

# Player Example

**Document ID:** EXAMPLES-IGAMING-PLAYER-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Player is represented as an Entity within the OCOM Specification.

The example illustrates how multiple enterprise Domains collaborate around a single Player while preserving ownership, governance, lifecycle integrity, operational memory, and AI-assisted decision support.

This example is informative and does not define normative behavior.

---

# Business Context

A Player is the primary Entity within an iGaming enterprise.

Throughout the Player lifecycle, multiple Domains participate in delivering business capabilities including registration, verification, payments, gameplay, customer support, compliance, marketing, and responsible gaming.

Despite this collaboration, the Player remains a single Entity with a single Business Owner.

---

# Entity

Object Type

Player

Primary Owner

Player Management Domain

---

# Identity

Example Identifier

```
PLR-100245
```

Player Identity uniquely identifies the Entity throughout its entire lifecycle.

Identity remains immutable.

---

# Participating Domains

The following Domains may interact with the Player:

- Player Management
- Payments
- Wallet
- Compliance
- Responsible Gaming
- Fraud
- Affiliate
- Marketing
- Customer Support
- BI
- AI

Each Domain contributes business capabilities while preserving Player ownership.

---

# Relationships

The Player may establish relationships with multiple Entities.

Examples include:

- Player owns Account.
- Player owns Wallet.
- Player performs Payment.
- Player receives Bonus.
- Player participates in Game Session.
- Player creates Support Case.
- Player is associated with Affiliate.
- Player is evaluated through KYC Case.
- Player may become subject to Fraud Case.
- Player may become subject to Responsible Gaming Case.

Relationships evolve independently from Player ownership.

---

# Lifecycle

Example lifecycle:

```text
Registered
      │
      ▼
Verified
      │
      ▼
Active
      │
      ▼
Restricted
      │
      ▼
Self-Excluded
      │
      ▼
Closed
```

Each transition is governed by organizational Policies.

---

# Events

Example Business Events include:

- Player Registered
- Player Verified
- Player Activated
- Player Restricted
- Player Self-Excluded
- Player Closed

Events provide an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Register Player
- Verify Player
- Update Player
- Restrict Player
- Suspend Player
- Close Player
- Restore Player Access

Capabilities operate on the Player according to applicable Policies.

---

# Policies

Example Policies include:

- Player identity shall be unique.
- Identity verification shall precede activation.
- Responsible Gaming restrictions shall be enforced.
- Compliance requirements shall be satisfied before regulated activities.
- Every lifecycle transition shall be auditable.

Policies govern Player operations independently of implementation.

---

# Operational Memory

Operational Memory may preserve:

- interaction history;
- operational observations;
- AI recommendations;
- compliance evidence;
- support summaries;
- behavioral assessments;
- confidence evaluations.

Operational Memory supplements enterprise knowledge without changing Player ownership.

---

# AI Participation

AI may:

- summarize Player history;
- identify behavioral anomalies;
- estimate churn probability;
- recommend retention activities;
- identify responsible gaming indicators;
- recommend manual investigation.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Player remains the central Entity throughout its operational lifetime.

Enterprise Domains collaborate through Business Capabilities while preserving:

- single ownership;
- immutable identity;
- governed lifecycle;
- operational traceability;
- policy compliance;
- enterprise memory;
- AI-assisted decision support.

---

# Related Specifications

- Meta/Object
- Meta/Identity
- Meta/Relationship
- Meta/Lifecycle
- Meta/Capability
- Meta/Policy
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

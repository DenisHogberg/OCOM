<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Account Example

[↑ Up](README.md) · [Next →](Affiliate%20Example.md)

---
<!-- nav:end -->

# Account Example

**Document ID:** EXAMPLES-IGAMING-ACCOUNT-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how an Account is represented as an Entity within the OCOM Specification.

The example illustrates how an Account serves as the operational identity through which a Player accesses gaming services while preserving clear separation between Player and Account ownership.

This example is informative and does not define normative behavior.

---

# Business Context

An Account provides a Player with access to an iGaming platform.

An Account maintains operational status, authentication, security settings, and access permissions independently of the Player Entity.

A Player may own one or more Accounts according to organizational Policies.

---

# Entity

Object Type

Account

Primary Owner

Account Management Domain

---

# Identity

Example Identifier

```
ACC-200381
```

Account Identity uniquely identifies the Account throughout its lifecycle.

---

# Relationships

Example relationships include:

- Account belongs to Player.
- Account owns Wallet.
- Account initiates Game Sessions.
- Account performs Payments.
- Account receives Bonuses.
- Account participates in Marketing Campaigns.
- Account may become subject to KYC Case.
- Account may become subject to Fraud Case.

Relationships do not modify Account ownership.

---

# Lifecycle

Example lifecycle:

```text
Created
    │
    ▼
Verified
    │
    ▼
Active
    │
    ▼
Locked
    │
    ▼
Suspended
    │
    ▼
Closed
```

Each transition is governed by applicable Policies.

---

# Events

Example Business Events include:

- Account Created
- Account Verified
- Account Activated
- Account Locked
- Account Suspended
- Account Closed

Events provide an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Create Account
- Verify Account
- Lock Account
- Unlock Account
- Suspend Account
- Close Account

Capabilities operate on the Account Entity.

---

# Policies

Example Policies include:

- Every Account shall belong to a Player.
- Authentication shall satisfy organizational security requirements.
- Closed Accounts shall not perform regulated activities.
- Security actions shall be auditable.

---

# Operational Memory

Operational Memory may preserve:

- authentication history;
- security observations;
- access anomalies;
- operational notes;
- investigation summaries;
- AI recommendations.

Operational Memory complements the Account without changing its authoritative state.

---

# AI Participation

AI may:

- detect suspicious login patterns;
- identify compromised accounts;
- recommend additional verification;
- summarize account activity;
- estimate account risk.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Account represents the operational access point for a Player while preserving:

- independent identity;
- governed lifecycle;
- policy enforcement;
- operational traceability;
- enterprise memory;
- AI-assisted decision support.

---

# Related Specifications

- Player Example
- Meta/Object
- Meta/Relationship
- Meta/Lifecycle
- Meta/Policy
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

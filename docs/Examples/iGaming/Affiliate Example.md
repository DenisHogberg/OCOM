<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Affiliate Example

[← Back](Account%20Example.md) · [↑ Up](README.md) · [Next →](Bonus%20Example.md)

---
<!-- nav:end -->

# Affiliate Example

**Document ID:** EXAMPLES-IGAMING-AFFILIATE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how an Affiliate is represented as an Entity within the OCOM Specification.

The example illustrates how an Affiliate collaborates with Players, Campaigns, Contracts, Commissions, and Payments while maintaining independent ownership and governance.

This example is informative and does not define normative behavior.

---

# Business Context

An Affiliate represents an external business partner responsible for acquiring Players.

Throughout its lifecycle, the Affiliate participates in commercial agreements, marketing campaigns, commission calculations, and performance evaluation.

The Affiliate remains a single Entity regardless of the number of brands, campaigns, or Players associated with it.

---

# Entity

Object Type

Affiliate

Primary Owner

Affiliate Management Domain

---

# Identity

Example Identifier

```
AFF-700143
```

Affiliate Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Affiliate owns Contract.
- Affiliate participates in Campaign.
- Affiliate refers Player.
- Affiliate receives Commission.
- Affiliate is associated with Payment.
- Affiliate is evaluated through Performance Review.

Relationships do not transfer Affiliate ownership.

---

# Lifecycle

Example lifecycle:

```text
Registered
      │
      ▼
Approved
      │
      ▼
Active
      │
      ▼
Suspended
      │
      ▼
Closed
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Affiliate Registered
- Affiliate Approved
- Campaign Assigned
- Player Referred
- Commission Calculated
- Commission Paid
- Affiliate Suspended
- Affiliate Closed

Business Events establish an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Register Affiliate
- Approve Affiliate
- Assign Campaign
- Calculate Commission
- Process Commission Payment
- Suspend Affiliate
- Close Affiliate

Capabilities execute business operations on the Affiliate.

---

# Policies

Example Policies include:

- Affiliates shall satisfy onboarding requirements.
- Contracts shall be active before commission generation.
- Commission calculations shall be auditable.
- Suspended Affiliates shall not receive new Campaigns.
- Every commission payment shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- partner communication history;
- commercial observations;
- fraud indicators;
- payment investigations;
- performance assessments;
- AI recommendations.

Operational Memory supplements the Affiliate Entity without changing authoritative business information.

---

# AI Participation

AI may:

- identify traffic quality trends;
- estimate partner performance;
- detect fraudulent behavior;
- recommend commission optimization;
- identify partnership opportunities.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Affiliate remains the authoritative Entity representing a commercial partner while preserving:

- single ownership;
- governed lifecycle;
- immutable operational history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted decision support.

---

# Related Specifications

- Player Example
- Campaign Example
- Payment Example
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

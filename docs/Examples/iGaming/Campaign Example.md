<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Campaign Example

[← Back](Bonus%20Example.md) · [↑ Up](README.md) · [Next →](Examples_iGaming_Player.md)

---
<!-- nav:end -->

# Campaign Example

**Document ID:** EXAMPLES-IGAMING-CAMPAIGN-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Campaign is represented as an Entity within the OCOM Specification.

The example illustrates how a Campaign coordinates commercial activities across multiple enterprise Domains while preserving ownership, governance, lifecycle integrity, and operational traceability.

This example is informative and does not define normative behavior.

---

# Business Context

A Campaign represents a planned commercial initiative intended to achieve specific business objectives such as player acquisition, retention, reactivation, or promotional engagement.

A Campaign coordinates multiple Entities while remaining independently governed throughout its lifecycle.

---

# Entity

Object Type

Campaign

Primary Owner

Marketing Domain

---

# Identity

Example Identifier

```
CMP-900412
```

Campaign Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Campaign targets Players.
- Campaign involves Affiliates.
- Campaign distributes Bonuses.
- Campaign generates Commissions.
- Campaign influences Payments.
- Campaign produces Performance Metrics.

Relationships do not transfer Campaign ownership.

---

# Lifecycle

Example lifecycle:

```text
Planned
    │
    ▼
Approved
    │
    ▼
Active
    │
    ▼
Completed
```

Alternative outcomes:

```text
Approved
    │
    ├── Cancelled
    │
    └── Suspended
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Campaign Created
- Campaign Approved
- Campaign Activated
- Bonus Assigned
- Campaign Completed
- Campaign Cancelled

Business Events establish an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Create Campaign
- Approve Campaign
- Launch Campaign
- Suspend Campaign
- Complete Campaign
- Cancel Campaign

Capabilities execute business operations on the Campaign.

---

# Policies

Example Policies include:

- Campaign approval shall precede activation.
- Eligibility rules shall be defined before launch.
- Promotional conditions shall remain auditable.
- Campaign completion shall preserve historical records.
- Every lifecycle transition shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- planning decisions;
- execution observations;
- optimization recommendations;
- campaign performance analysis;
- operational issues;
- evidence references.

Operational Memory supplements Campaign management without changing authoritative business information.

---

# AI Participation

AI may:

- recommend audience segmentation;
- optimize campaign timing;
- estimate campaign performance;
- identify underperforming campaigns;
- recommend budget adjustments.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Campaign remains the authoritative Entity representing a commercial initiative while preserving:

- single ownership;
- governed lifecycle;
- immutable operational history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted optimization.

---

# Related Specifications

- Affiliate Example
- Bonus Example
- Player Example
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

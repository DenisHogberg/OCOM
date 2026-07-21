<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Fraud Case Example

[← Back](Examples_iGaming_Player.md) · [↑ Up](README.md) · [Next →](Game%20Session%20Example.md)

---
<!-- nav:end -->

# Fraud Case Example

**Document ID:** EXAMPLES-IGAMING-FRAUD-CASE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Fraud Case is represented as an Entity within the OCOM Specification.

The example illustrates how fraud investigations are managed independently while coordinating evidence, business decisions, and related Entities.

This example is informative and does not define normative behavior.

---

# Business Context

A Fraud Case represents a business investigation initiated when suspicious activity is detected.

The Fraud Case coordinates evidence collection, investigation activities, risk assessment, and business decisions while maintaining an independent lifecycle.

A Fraud Case may involve multiple Entities simultaneously.

---

# Entity

Object Type

Fraud Case

Primary Owner

Risk & Fraud Management Domain

---

# Identity

Example Identifier

```
FRD-700328
```

Fraud Case Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Fraud Case investigates Player.
- Fraud Case references Account.
- Fraud Case references Wallet.
- Fraud Case references Payments.
- Fraud Case references Game Sessions.
- Fraud Case references Bonuses.
- Fraud Case references Affiliate.
- Fraud Case may reference KYC Case.
- Fraud Case may generate Support Case.

Relationships do not transfer ownership.

---

# Lifecycle

Example lifecycle:

```text
Opened
    │
    ▼
Evidence Collection
    │
    ▼
Under Investigation
    │
    ▼
Decision Made
    │
    ▼
Closed
```

Alternative outcomes:

```text
Under Investigation
      │
      ├── Escalated
      │
      ├── Additional Evidence Required
      │
      └── Reopened
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Fraud Case Opened
- Evidence Collected
- Investigation Started
- Risk Score Updated
- Investigation Escalated
- Decision Recorded
- Fraud Case Closed

Business Events establish an immutable investigation history.

---

# Capabilities

Example Capabilities include:

- Open Fraud Case
- Collect Evidence
- Assess Risk
- Escalate Investigation
- Record Decision
- Reopen Case
- Close Fraud Case

Capabilities execute business operations on the Fraud Case.

---

# Policies

Example Policies include:

- Every investigation shall preserve supporting evidence.
- Decisions shall be auditable.
- Evidence shall remain immutable after submission.
- Case ownership shall be maintained throughout the lifecycle.
- Every lifecycle transition shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- investigator observations;
- behavioral patterns;
- linked incidents;
- historical investigation outcomes;
- AI recommendations;
- confidence assessments.

Operational Memory supplements the Fraud Case without replacing authoritative evidence.

---

# AI Participation

AI may:

- identify suspicious behavioral patterns;
- correlate related fraud cases;
- estimate fraud probability;
- recommend investigation priorities;
- summarize investigation findings.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Fraud Case remains the authoritative Entity representing fraud investigations while preserving:

- single ownership;
- governed lifecycle;
- immutable investigation history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted investigation support.

---

# Related Specifications

- Player Example
- Account Example
- Wallet Example
- Payment Example
- Bonus Example
- Affiliate Example
- Game Session Example
- KYC Case Example
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

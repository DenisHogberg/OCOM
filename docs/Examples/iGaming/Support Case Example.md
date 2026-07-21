<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Support Case Example

[← Back](Responsible%20Gaming%20Case.md) · [↑ Up](README.md) · [Next →](Wallet%20Example.md)

---
<!-- nav:end -->

# Support Case Example

**Document ID:** EXAMPLES-IGAMING-SUPPORT-CASE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Support Case is represented as an Entity within the OCOM Specification.

The example illustrates how customer support activities are coordinated independently while preserving ownership, governance, operational traceability, and service history.

This example is informative and does not define normative behavior.

---

# Business Context

A Support Case represents a customer service interaction initiated to resolve a business issue, answer a request, or assist a Player.

A Support Case coordinates communication, investigation, resolution activities, and related Entities while maintaining an independent lifecycle.

---

# Entity

Object Type

Support Case

Primary Owner

Customer Support Domain

---

# Identity

Example Identifier

```
SUP-300917
```

Support Case Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Support Case references Player.
- Support Case references Account.
- Support Case may reference Wallet.
- Support Case may reference Payment.
- Support Case may reference Bonus.
- Support Case may reference Game Session.
- Support Case may reference KYC Case.
- Support Case may reference Fraud Case.
- Support Case may reference Responsible Gaming Case.

Relationships do not transfer ownership.

---

# Lifecycle

Example lifecycle:

```text
Opened
    │
    ▼
Assigned
    │
    ▼
In Progress
    │
    ▼
Resolved
    │
    ▼
Closed
```

Alternative outcomes:

```text
In Progress
      │
      ├── Escalated
      │
      ├── Waiting for Customer
      │
      ├── Waiting for Third Party
      │
      └── Reopened
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Support Case Opened
- Agent Assigned
- Investigation Started
- Customer Contacted
- Information Received
- Case Escalated
- Resolution Recorded
- Support Case Closed

Business Events establish an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Open Support Case
- Assign Agent
- Investigate Issue
- Escalate Case
- Record Resolution
- Reopen Case
- Close Support Case

Capabilities execute business operations on the Support Case.

---

# Policies

Example Policies include:

- Every Support Case shall have an assigned owner.
- Escalations shall be traceable.
- Resolution decisions shall be documented.
- Customer communications shall be preserved.
- Every lifecycle transition shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- communication history;
- investigation notes;
- customer preferences;
- previous resolutions;
- AI recommendations;
- supporting evidence.

Operational Memory supplements the Support Case without replacing authoritative business information.

---

# AI Participation

AI may:

- classify incoming requests;
- recommend similar resolved cases;
- summarize conversations;
- recommend next actions;
- estimate escalation priority.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Support Case remains the authoritative Entity representing customer service activities while preserving:

- single ownership;
- governed lifecycle;
- immutable operational history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted service support.

---

# Related Specifications

- Player Example
- Account Example
- Wallet Example
- Payment Example
- Bonus Example
- Game Session Example
- KYC Case Example
- Fraud Case Example
- Responsible Gaming Case Example
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / Responsible Gaming Case Example

[← Back](Payment%20Example.md) · [↑ Up](README.md) · [Next →](Support%20Case%20Example.md)

---
<!-- nav:end -->

# Responsible Gaming Case Example

**Document ID:** EXAMPLES-IGAMING-RESPONSIBLE-GAMING-CASE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a Responsible Gaming Case is represented as an Entity within the OCOM Specification.

The example illustrates how responsible gaming interventions are coordinated independently while preserving governance, auditability, operational traceability, and player protection.

This example is informative and does not define normative behavior.

---

# Business Context

A Responsible Gaming Case represents an operational process initiated to assess or manage a Player's gambling-related risk.

The Responsible Gaming Case coordinates observations, assessments, interventions, restrictions, and business decisions while maintaining its own lifecycle.

The Responsible Gaming Case exists independently from the Player and other Entities.

---

# Entity

Object Type

Responsible Gaming Case

Primary Owner

Responsible Gaming Domain

---

# Identity

Example Identifier

```
RGC-500821
```

The Responsible Gaming Case Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- Responsible Gaming Case references Player.
- Responsible Gaming Case references Account.
- Responsible Gaming Case references Game Sessions.
- Responsible Gaming Case references Payments.
- Responsible Gaming Case may reference KYC Case.
- Responsible Gaming Case may reference Fraud Case.
- Responsible Gaming Case may generate Support Case.

Relationships do not transfer ownership.

---

# Lifecycle

Example lifecycle:

```text
Opened
    │
    ▼
Assessment
    │
    ▼
Intervention
    │
    ▼
Monitoring
    │
    ▼
Closed
```

Alternative outcomes:

```text
Assessment
      │
      ├── Escalated
      │
      ├── Additional Review Required
      │
      └── Reopened
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- Responsible Gaming Case Opened
- Assessment Started
- Risk Assessment Updated
- Intervention Applied
- Restriction Applied
- Restriction Removed
- Responsible Gaming Case Closed

Business Events establish an immutable operational history.

---

# Capabilities

Example Capabilities include:

- Open Responsible Gaming Case
- Perform Assessment
- Apply Intervention
- Apply Restriction
- Remove Restriction
- Reopen Case
- Close Responsible Gaming Case

Capabilities execute business operations on the Responsible Gaming Case.

---

# Policies

Example Policies include:

- Risk assessments shall be documented.
- Every intervention shall be traceable.
- Restrictions shall comply with applicable regulations.
- Case ownership shall be maintained throughout the lifecycle.
- Every lifecycle transition shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- behavioral observations;
- intervention history;
- assessment rationale;
- reviewer notes;
- AI recommendations;
- supporting evidence.

Operational Memory supplements the Responsible Gaming Case without modifying authoritative business information.

---

# AI Participation

AI may:

- identify behavioral risk indicators;
- detect changes in player activity;
- recommend interventions;
- estimate escalation priority;
- summarize case history.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The Responsible Gaming Case remains the authoritative Entity representing responsible gaming management while preserving:

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
- Account Example
- Game Session Example
- Payment Example
- KYC Case Example
- Fraud Case Example
- Memory
- AI

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

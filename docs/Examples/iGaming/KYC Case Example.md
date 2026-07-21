<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [iGaming](README.md) / KYC Case Example

[← Back](Game%20Session%20Example.md) · [↑ Up](README.md) · [Next →](Payment%20Example.md)

---
<!-- nav:end -->

# KYC Case Example

**Document ID:** EXAMPLES-IGAMING-KYC-CASE-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This example demonstrates how a KYC Case is represented as an Entity within the OCOM Specification.

The example illustrates how identity verification is managed through an independent Entity while preserving governance, auditability, evidence management, and operational traceability.

This example is informative and does not define normative behavior.

---

# Business Context

A KYC Case represents a regulated verification process associated with a Player.

The KYC Case coordinates document verification, identity validation, compliance reviews, and approval decisions while maintaining an independent lifecycle.

---

# Entity

Object Type

KYC Case

Primary Owner

Compliance Domain

---

# Identity

Example Identifier

```
KYC-600214
```

The KYC Case Identity uniquely identifies the Entity throughout its lifecycle.

---

# Relationships

Example relationships include:

- KYC Case belongs to Player.
- KYC Case references Account.
- KYC Case references Identity Documents.
- KYC Case may reference Payment history.
- KYC Case may create Compliance Decision.
- KYC Case may trigger Fraud Case.
- KYC Case may generate Support Case.

Relationships do not transfer ownership.

---

# Lifecycle

Example lifecycle:

```text
Opened
    │
    ▼
Documents Received
    │
    ▼
Under Review
    │
    ▼
Approved
```

Alternative outcomes:

```text
Under Review
      │
      ├── Additional Information Required
      │
      ├── Rejected
      │
      └── Expired
```

Lifecycle transitions are governed by organizational Policies.

---

# Events

Example Business Events include:

- KYC Case Opened
- Documents Uploaded
- Verification Started
- Additional Information Requested
- Verification Approved
- Verification Rejected
- KYC Case Closed

Business Events establish an immutable verification history.

---

# Capabilities

Example Capabilities include:

- Open KYC Case
- Receive Documents
- Verify Identity
- Request Additional Information
- Approve Verification
- Reject Verification
- Close KYC Case

Capabilities execute business operations on the KYC Case.

---

# Policies

Example Policies include:

- Required documents shall be submitted before review.
- Verification shall comply with applicable regulations.
- Approval decisions shall be traceable.
- Evidence shall remain associated with the KYC Case.
- Every lifecycle transition shall generate a Business Event.

---

# Operational Memory

Operational Memory may preserve:

- reviewer observations;
- verification notes;
- evidence assessments;
- document quality observations;
- AI recommendations;
- confidence assessments.

Operational Memory supplements the KYC Case without replacing regulatory evidence.

---

# AI Participation

AI may:

- assess document completeness;
- identify inconsistent information;
- estimate verification confidence;
- recommend manual review;
- summarize submitted evidence.

AI recommendations remain subject to organizational governance.

---

# Expected Outcome

The KYC Case remains the authoritative Entity representing identity verification while preserving:

- single ownership;
- governed lifecycle;
- immutable verification history;
- policy compliance;
- operational traceability;
- enterprise memory;
- AI-assisted verification support.

---

# Related Specifications

- Player Example
- Account Example
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

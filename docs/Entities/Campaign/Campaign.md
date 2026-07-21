<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Campaign](README.md) / Campaign

[↑ Up](README.md)

---
<!-- nav:end -->

# Campaign

**Document ID:** Entity-008

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the normative specification of the Campaign Entity.

The Campaign Entity represents a coordinated business initiative designed to achieve defined commercial, operational, or strategic objectives within a specified period.

---

# Definition

A Campaign is an operational entity representing a planned and managed initiative that coordinates one or more business activities toward measurable objectives.

A Campaign exists independently of the channels, participants, or technologies used to execute it.

---

# Business Meaning

A Campaign provides the organizational framework for executing business initiatives.

It defines objectives, duration, participants, and operational scope while coordinating Offers, Affiliates, Content, Creative assets, and other related entities.

A Campaign represents the initiative itself rather than the individual activities performed within it.

---

# Core Principles

A Campaign:

- shall have a unique identity;
- shall define one or more measurable objectives;
- shall operate within a defined timeframe;
- may coordinate multiple Offers;
- may involve multiple Affiliates and Partners;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Name | Campaign name |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Description | Business description |
| Objective | Primary campaign objective |
| Start Date | Campaign start |
| End Date | Campaign end |
| Budget | Planned budget |
| Priority | Operational priority |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every Campaign shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Campaign shall belong to exactly one primary Domain.

---

# States

A Campaign may include the following operational states:

- Draft
- Planned
- Under Review
- Approved
- Scheduled
- Active
- Completed
- Suspended
- Cancelled
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Campaign Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

A Campaign may establish relationships with:

- Offer
- Affiliate
- Partner
- Player
- Bonus
- Payment

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Campaign include:

- Campaign Created
- Campaign Approved
- Campaign Activated
- Campaign Completed
- Campaign Cancelled

Events represent immutable operational facts.

---

# Invariants

The following conditions shall always remain true.

- Every Campaign shall have exactly one Identifier.
- Every Campaign shall belong to exactly one primary Domain.
- Every Campaign shall have one current State.
- Every Campaign shall follow one defined Lifecycle.
- Every Campaign shall define at least one measurable objective.

---

# Constraints

A Campaign shall never:

- exist without an Identifier;
- exist without a Lifecycle;
- exist without a State;
- exist without a defined Domain;
- violate its defined Lifecycle.

---

# Conformance

A Campaign conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 21 July 2026 | Completed document structure (Domain, States, Lifecycle, Relationships, Events, Invariants, Constraints, Conformance, Examples) |

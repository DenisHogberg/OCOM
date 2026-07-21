<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Affiliate](README.md) / Affiliate

[↑ Up](README.md)

---
<!-- nav:end -->

# Affiliate

**Document ID:** Entity-006

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Affiliate Entity.

The Affiliate Entity represents a Partner responsible for acquiring, referring, or influencing potential customers or business opportunities in exchange for defined commercial compensation.

---

# Definition

An Affiliate is an operational entity representing a Partner that promotes products, services, or brands and receives compensation based on agreed business outcomes.

An Affiliate operates independently of specific campaigns, offers, or payment models.

---

# Business Meaning

An Affiliate extends the Partner Entity by introducing customer acquisition and referral responsibilities.

Affiliates create commercial value by generating qualified business opportunities through one or more marketing or distribution channels.

The Affiliate Entity represents the business relationship rather than the traffic source, website, advertising platform, or marketing technology used.

---

# Core Principles

An Affiliate:

- shall have a unique identity;
- shall be associated with one Partner;
- may participate in multiple Campaigns;
- may promote multiple Offers;
- may generate multiple Leads;
- may receive multiple Payments;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Partner | Associated Partner |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Affiliate Type | Classification of affiliate |
| Commission Model | CPA, CPL, Revenue Share, Hybrid, etc. |
| External Reference | External identifier |
| Contact Information | Business contact information |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every Affiliate shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Affiliate shall belong to exactly one primary Domain.

---

# States

An Affiliate may include the following operational states:

- Registered
- Pending Approval
- Active
- Suspended
- Terminated
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Affiliate Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

An Affiliate may establish relationships with:

- Partner
- Offer
- Campaign
- Lead
- Payment
- Transaction
- Bonus
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with an Affiliate include:

- Affiliate Registered
- Affiliate Approved
- Affiliate Activated
- Affiliate Suspended
- Affiliate Terminated

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Affiliates are implementation-specific.

Examples include:

- approval procedures;
- commission calculation;
- fraud prevention;
- payment schedules;
- performance requirements.

---

# Invariants

The following conditions shall always remain true.

- Every Affiliate shall have exactly one Identifier.
- Every Affiliate shall be associated with one Partner.
- Every Affiliate shall belong to exactly one primary Domain.
- Every Affiliate shall have one current State.
- Every Affiliate shall follow one defined Lifecycle.

---

# Constraints

An Affiliate shall never:

- exist without an Identifier;
- exist without a Partner;
- exist without a Lifecycle;
- exist without a State;
- violate its defined Lifecycle.

---

# Conformance

An Affiliate conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision

<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Partner](README.md) / Partner

[↑ Up](README.md)

---
<!-- nav:end -->

# Partner

**Document ID:** Entity-005

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Partner Entity.

The Partner Entity represents an external business party that establishes and maintains a commercial relationship with an organization.

---

# Definition

A Partner is an operational entity representing an external individual, organization, or business that participates in one or more commercial relationships.

A Partner exists independently of specific agreements, offers, campaigns, or operational systems.

---

# Business Meaning

A Partner represents a long-term business relationship rather than a single transaction or contract.

Partners may provide products, services, distribution, technology, marketing, financial services, or strategic collaboration.

The Partner Entity provides a unified representation of external business participants across operational domains.

---

# Core Principles

A Partner:

- shall have a unique identity;
- shall participate in one or more business relationships;
- shall belong to exactly one primary Domain;
- may be associated with multiple Contracts, Offers, Campaigns, Payments, and Transactions;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Name | Official partner name |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Legal Name | Registered legal entity |
| Partner Type | Supplier, Affiliate, Reseller, Vendor, Agency, etc. |
| Country | Primary operating country |
| Website | Official website |
| Contact Information | Business contact details |
| External Reference | External identifier |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every Partner shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Partner shall belong to exactly one primary Domain.

---

# States

A Partner may include the following operational states:

- Prospect
- Negotiating
- Active
- Suspended
- Terminated
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Partner Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

A Partner may establish relationships with:

- Affiliate
- Offer
- Campaign
- Payment
- Transaction
- Contract
- Vendor
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with a Partner include:

- Partner Registered
- Partner Approved
- Partner Activated
- Partner Suspended
- Partner Terminated

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Partners are implementation-specific.

Examples include:

- onboarding procedures;
- due diligence requirements;
- contract approval policies;
- payment schedules;
- compliance requirements.

---

# Invariants

The following conditions shall always remain true.

- Every Partner shall have exactly one Identifier.
- Every Partner shall belong to exactly one primary Domain.
- Every Partner shall have one current State.
- Every Partner shall follow one defined Lifecycle.
- Every Partner shall have one responsible Owner.

---

# Constraints

A Partner shall never:

- exist without an Identifier;
- exist without a Lifecycle;
- exist without a State;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

A Partner conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [TrafficSource](README.md) / Traffic Source

[↑ Up](README.md)

---
<!-- nav:end -->

# Traffic Source

**Document ID:** Entity-025

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Traffic Source Entity within the OCOM Specification.

A Traffic Source represents an origin from which visitors, users, customers, or business opportunities are acquired.

---

# Definition

A Traffic Source is a business Entity representing a channel, platform, partner, or mechanism responsible for generating inbound traffic.

A Traffic Source exists independently of marketing platforms, analytics tools, or advertising technologies.

---

# Business Meaning

The Traffic Source Entity provides a standardized representation of acquisition channels across marketing, sales, analytics, and business operations.

A Traffic Source enables consistent attribution, performance measurement, optimization, and governance of customer acquisition activities.

---

# Core Principles

A Traffic Source:

- shall possess a unique identity;
- shall represent one acquisition channel;
- may generate multiple Leads and Players;
- may participate in multiple Campaigns and Offers;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Traffic Source shall define:

- Identifier
- Name
- Type
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Traffic Source may define:

- Description
- Platform
- Medium
- Campaign Reference
- GEO
- Cost Model
- Tracking Identifier
- Tags

---

# Ownership

The Traffic Source shall have a clearly defined Owner responsible for governance and performance management.

---

# Domain

The governing Domain is:

**Marketing**

---

# Lifecycle

This Entity shall conform to the **Commercial Lifecycle** unless otherwise specified.

---

# Relationships

A Traffic Source may be related to:

- Campaign
- Lead
- Player
- Landing
- Offer
- Affiliate
- Partner
- GEO

---

# Events

Typical Events include:

- Traffic Source Created
- Traffic Source Activated
- Traffic Source Updated
- Traffic Source Suspended
- Traffic Source Retired

---

# Business Rules

- A Traffic Source shall have exactly one Owner.
- A Traffic Source may support multiple Campaigns.
- A Traffic Source may generate multiple Leads and Players.
- Performance metrics shall remain attributable to the originating Traffic Source.

---

# Invariants

The following conditions shall always remain true:

- Every Traffic Source shall have a unique Identifier.
- Every Traffic Source shall belong to one governing Domain.
- Every Traffic Source shall reference a valid Lifecycle.
- Every Traffic Source shall have one Owner.

---

# Constraints

A Traffic Source shall comply with applicable privacy regulations, attribution policies, marketing governance, and contractual obligations.

---

# Conformance

A Traffic Source conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Commercial Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Organic Search
- Paid Search
- Affiliate Network
- Social Media
- Email Marketing
- Referral Program
- Display Advertising
- Direct Traffic

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

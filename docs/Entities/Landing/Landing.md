<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Landing](README.md) / Landing

[↑ Up](README.md)

---
<!-- nav:end -->

# Landing

**Document ID:** Entity-013

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Landing Entity within the OCOM Specification.

A Landing represents a destination page designed to present information, promote an offer, capture user interaction, or initiate a business process.

---

# Definition

A Landing is a business Entity representing a web page or digital destination used to achieve a specific business objective.

A Landing may be associated with one or more Campaigns, Offers, Brands, or Creatives.

---

# Business Meaning

The Landing Entity provides a standardized representation of digital destinations used across marketing, sales, and operational activities.

A Landing exists independently of the technologies used to build or host it.

---

# Core Principles

A Landing:

- shall possess a unique identity;
- shall represent a single business destination;
- may support one or more business objectives;
- may be reused across multiple Campaigns;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Landing shall define:

- Identifier
- Name
- URL
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Landing may define:

- Description
- Language
- GEO
- Platform
- Version
- Tags
- Publication Date
- Expiration Date

---

# Ownership

The Landing shall have a clearly defined Owner responsible for its business integrity and lifecycle.

---

# Domain

The governing Domain is:

**Marketing**

---

# Lifecycle

This Entity shall conform to the **Content Lifecycle** unless otherwise specified.

---

# Relationships

A Landing may be related to:

- Brand
- Campaign
- Offer
- Creative
- Content
- GEO

---

# Events

Typical Events include:

- Landing Created
- Landing Updated
- Landing Reviewed
- Landing Approved
- Landing Published
- Landing Retired

---

# Business Rules

- A Landing shall have exactly one Owner.
- A Landing shall reference a valid URL.
- A published Landing shall conform to applicable branding and compliance requirements.
- A Landing may support multiple Campaigns and Offers.

---

# Invariants

The following conditions shall always remain true:

- Every Landing shall have a unique Identifier.
- Every Landing shall belong to one governing Domain.
- Every Landing shall reference a valid Lifecycle.
- Every Landing shall have one Owner.

---

# Constraints

A Landing shall comply with applicable legal, regulatory, branding, accessibility, and security requirements.

---

# Conformance

A Landing conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Content Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Product Landing Page
- Campaign Landing Page
- Registration Page
- Lead Capture Page
- Promotional Microsite

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

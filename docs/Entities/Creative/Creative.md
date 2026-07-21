<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Creative](README.md) / Creative

[↑ Up](README.md)

---
<!-- nav:end -->

# Creative

**Document ID:** Entity-012

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Creative Entity within the OCOM Specification.

A Creative represents a reusable marketing or promotional asset intended for communication, advertising, branding, or user engagement.

---

# Definition

A Creative is a business Entity representing a digital or physical asset used to deliver marketing or promotional content.

A Creative may consist of one or more files and associated metadata.

---

# Business Meaning

The Creative Entity serves as the standardized representation of marketing assets across operational Domains.

Creatives may be reused by multiple Campaigns, Offers, Brands, or other business Entities.

---

# Core Principles

A Creative:

- shall possess a unique identity;
- shall represent a reusable business asset;
- may have multiple versions;
- may be associated with multiple Campaigns;
- shall remain independent of storage technologies.

---

# Mandatory Attributes

Every Creative shall define:

- Identifier
- Name
- Type
- Format
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Creative may define:

- Description
- Language
- Resolution
- Dimensions
- File Size
- Version
- Tags
- Expiration Date
- Approval Date

---

# Ownership

The Creative shall have a clearly defined Owner responsible for its quality, governance, and lifecycle.

---

# Domain

The governing Domain is:

**Marketing**

---

# Lifecycle

This Entity shall conform to the **Content Lifecycle** unless otherwise specified.

---

# Relationships

A Creative may be related to:

- Brand
- Campaign
- Offer
- Content
- Landing

---

# Events

Typical Events include:

- Creative Created
- Creative Updated
- Creative Submitted for Review
- Creative Approved
- Creative Published
- Creative Retired

---

# Business Rules

- A Creative shall have exactly one governing Owner.
- A Creative may be reused across multiple Campaigns.
- A Creative shall not be published without approval when approval is required.
- Every published Creative shall reference a valid Brand where applicable.

---

# Invariants

The following conditions shall always remain true:

- Every Creative shall have a unique Identifier.
- Every Creative shall belong to one governing Domain.
- Every Creative shall reference a valid Lifecycle.
- Every Creative shall have one Owner.

---

# Constraints

A Creative shall comply with applicable branding, legal, regulatory, and compliance requirements.

---

# Conformance

A Creative conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Content Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Banner
- Video Advertisement
- Image Asset
- Social Media Creative
- Email Template
- Push Notification Image

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Lead](README.md) / Lead

[↑ Up](README.md)

---
<!-- nav:end -->

# Lead

**Document ID:** Entity-014

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Lead Entity within the OCOM Specification.

A Lead represents an identified prospective customer or business opportunity that has not yet become an active Customer or Player.

---

# Definition

A Lead is a business Entity representing an individual or organization that has demonstrated interest in a product, service, or business relationship.

A Lead progresses through qualification and conversion processes before becoming another business Entity, such as a Customer or Player.

---

# Business Meaning

The Lead Entity provides a standardized representation of prospective business opportunities across sales, marketing, and operational Domains.

A Lead exists independently of the channels through which it was acquired.

---

# Core Principles

A Lead:

- shall possess a unique identity;
- shall represent a prospective business opportunity;
- may originate from multiple acquisition channels;
- may progress through qualification stages;
- shall remain independent of CRM or marketing technologies.

---

# Mandatory Attributes

Every Lead shall define:

- Identifier
- Source
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Lead may define:

- Name
- Contact Information
- Company
- Country
- Language
- Campaign
- Score
- Qualification Date
- Notes
- Tags

---

# Ownership

The Lead shall have a clearly defined Owner responsible for qualification and business progression.

---

# Domain

The governing Domain is:

**CRM**

---

# Lifecycle

This Entity shall conform to the **Commercial Lifecycle** unless otherwise specified.

---

# Relationships

A Lead may be related to:

- Campaign
- Landing
- Traffic Source
- Partner
- Affiliate
- GEO
- Player

---

# Events

Typical Events include:

- Lead Created
- Lead Updated
- Lead Qualified
- Lead Assigned
- Lead Converted
- Lead Archived

---

# Business Rules

- A Lead shall have exactly one Owner.
- A Lead may originate from multiple acquisition channels.
- A Lead shall not be converted more than once.
- Every converted Lead shall maintain traceability to its originating source.

---

# Invariants

The following conditions shall always remain true:

- Every Lead shall have a unique Identifier.
- Every Lead shall belong to one governing Domain.
- Every Lead shall reference a valid Lifecycle.
- Every Lead shall have one Owner.

---

# Constraints

A Lead shall comply with applicable privacy, data protection, and regulatory requirements.

---

# Conformance

A Lead conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Commercial Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Marketing Lead
- Sales Lead
- Referral Lead
- Partner Lead
- Event Lead
- Qualified Prospect

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

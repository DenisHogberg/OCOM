<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [GEO](README.md) / GEO

[↑ Up](README.md)

---
<!-- nav:end -->

# GEO

**Document ID:** Entity-022

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the GEO Entity within the OCOM Specification.

A GEO represents a geographical market, jurisdiction, or region used for business operations, segmentation, targeting, reporting, and compliance.

---

# Definition

A GEO is a business Entity representing a geographical area to which business rules, commercial activities, products, or operational policies may apply.

A GEO may correspond to a country, territory, region, state, city, or any other defined geographic scope.

---

# Business Meaning

The GEO Entity provides a standardized representation of geographical classifications across all Domains.

A GEO enables consistent market targeting, localization, reporting, compliance, and operational decision-making.

---

# Core Principles

A GEO:

- shall possess a unique identity;
- shall represent a defined geographical scope;
- may participate in multiple business processes;
- may be hierarchical;
- shall remain independent of software implementations and external data providers.

---

# Mandatory Attributes

Every GEO shall define:

- Identifier
- Name
- Type
- Code
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A GEO may define:

- Parent GEO
- ISO Code
- Time Zone
- Currency
- Language
- Regulatory Status
- Market Tier
- Tags

---

# Ownership

The GEO shall have a clearly defined Owner responsible for governance and business classification.

---

# Domain

The governing Domain is:

**Marketing**

---

# Lifecycle

This Entity shall conform to the **Commercial Lifecycle** unless otherwise specified.

---

# Relationships

A GEO may be related to:

- Campaign
- Offer
- Landing
- Lead
- Player
- Partner
- Traffic Source
- Brand

---

# Events

Typical Events include:

- GEO Created
- GEO Updated
- GEO Activated
- GEO Suspended
- GEO Retired

---

# Business Rules

- A GEO shall have exactly one Owner.
- A GEO may participate in multiple Campaigns and Offers.
- A GEO may inherit characteristics from a Parent GEO.
- Business policies may differ between GEOs.

---

# Invariants

The following conditions shall always remain true:

- Every GEO shall have a unique Identifier.
- Every GEO shall belong to one governing Domain.
- Every GEO shall reference a valid Lifecycle.
- Every GEO shall have one Owner.

---

# Constraints

A GEO shall comply with applicable legal, regulatory, localization, and business governance requirements.

---

# Conformance

A GEO conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Commercial Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Germany
- Brazil
- Ontario
- European Union
- North America
- LATAM

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

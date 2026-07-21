<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Player](README.md) / Player

[↑ Up](README.md)

---
<!-- nav:end -->

# Player

**Document ID:** Entity-023

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Player Entity within the OCOM Specification.

A Player represents an individual who interacts with an organization's products or services as an active customer or user.

---

# Definition

A Player is a business Entity representing a person who has completed onboarding and is authorized to participate in business activities offered by an organization.

A Player maintains an identity throughout the entire customer lifecycle.

---

# Business Meaning

The Player Entity provides a standardized representation of customers across operational Domains.

A Player exists independently of CRM platforms, gaming systems, payment providers, or implementation technologies.

---

# Core Principles

A Player:

- shall possess a unique identity;
- shall represent a single customer;
- may own one or more Wallets;
- may participate in multiple Campaigns and Offers;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Player shall define:

- Identifier
- Registration Date
- Owner
- Lifecycle
- Status

---

# Optional Attributes

A Player may define:

- Username
- Country
- Language
- Currency
- Contact Information
- Acquisition Source
- Risk Level
- VIP Level
- Tags

---

# Ownership

The Player shall have a clearly defined Owner responsible for governance and business accountability.

---

# Domain

The governing Domain is:

**CRM**

---

# Lifecycle

This Entity shall conform to the **Commercial Lifecycle** unless otherwise specified.

---

# Relationships

A Player may be related to:

- Wallet
- Payment
- Transaction
- Bonus
- Campaign
- Offer
- GEO
- Lead
- Affiliate
- Partner

---

# Events

Typical Events include:

- Player Registered
- Player Verified
- Player Activated
- Player Suspended
- Player Deposited
- Player Withdrew Funds
- Player Closed

---

# Business Rules

- A Player shall have exactly one business identity.
- A Player may own multiple Wallets.
- A Player may participate in multiple Campaigns and Offers.
- Every Player activity shall be traceable.

---

# Invariants

The following conditions shall always remain true:

- Every Player shall have a unique Identifier.
- Every Player shall belong to one governing Domain.
- Every Player shall reference a valid Lifecycle.
- Every Player shall have one Owner.

---

# Constraints

A Player shall comply with applicable legal, regulatory, privacy, identity verification, and compliance requirements.

---

# Conformance

A Player conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Commercial Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Registered Player
- Verified Player
- VIP Player
- Suspended Player
- Self-Excluded Player

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

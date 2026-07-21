<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Vendor](README.md) / Vendor

[↑ Up](README.md)

---
<!-- nav:end -->

# Vendor

**Document ID:** Entity-024

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Vendor Entity within the OCOM Specification.

A Vendor represents an external organization that provides products, services, technology, infrastructure, or professional expertise to an organization.

---

# Definition

A Vendor is a business Entity representing a third-party supplier engaged through a commercial relationship.

A Vendor may supply one or more products or services and may participate in multiple operational Domains.

---

# Business Meaning

The Vendor Entity provides a standardized representation of external suppliers across procurement, finance, operations, technology, and compliance.

A Vendor exists independently of procurement systems, accounting software, or contract management platforms.

---

# Core Principles

A Vendor:

- shall possess a unique identity;
- shall represent one external organization;
- may provide multiple products or services;
- may support multiple business Domains;
- shall remain independent of implementation technologies.

---

# Mandatory Attributes

Every Vendor shall define:

- Identifier
- Name
- Owner
- Lifecycle
- Status
- Created Date

---

# Optional Attributes

A Vendor may define:

- Legal Name
- Vendor Type
- Country
- Contact Information
- Website
- Contract Reference
- Risk Classification
- Service Categories
- Tags

---

# Ownership

The Vendor shall have a clearly defined Owner responsible for vendor governance and relationship management.

---

# Domain

The governing Domain is:

**Procurement**

---

# Lifecycle

This Entity shall conform to the **Commercial Lifecycle** unless otherwise specified.

---

# Relationships

A Vendor may be related to:

- Department
- Team
- Payment
- Transaction
- PSP
- Task
- Ticket
- Contract

---

# Events

Typical Events include:

- Vendor Registered
- Vendor Approved
- Vendor Activated
- Vendor Suspended
- Vendor Contract Renewed
- Vendor Retired

---

# Business Rules

- A Vendor shall have exactly one Owner.
- A Vendor may provide multiple products or services.
- A Vendor may support multiple Departments.
- Every Vendor relationship shall be governed by applicable agreements.

---

# Invariants

The following conditions shall always remain true:

- Every Vendor shall have a unique Identifier.
- Every Vendor shall belong to one governing Domain.
- Every Vendor shall reference a valid Lifecycle.
- Every Vendor shall have one Owner.

---

# Constraints

A Vendor shall comply with applicable contractual obligations, regulatory requirements, procurement policies, and security standards.

---

# Conformance

A Vendor conforms to this specification if it:

- satisfies all mandatory attributes;
- references the Commercial Lifecycle;
- complies with the OCOM Core Specification;
- follows applicable Business Rules.

---

# Examples

Examples include:

- Payment Service Provider
- Cloud Infrastructure Provider
- Marketing Agency
- Software Vendor
- Identity Verification Provider
- Managed Service Provider

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

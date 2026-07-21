<!-- nav:start -->
[Docs](../../README.md) / [Entities](../README.md) / [Content](README.md) / Content

[↑ Up](README.md)

---
<!-- nav:end -->

# Content

**Document ID:** Entity-011

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative specification of the Content Entity.

The Content Entity represents information created, managed, and distributed to communicate, educate, promote, or support business objectives.

---

# Definition

Content is an operational entity representing structured or unstructured information intended for consumption by one or more audiences.

Content exists independently of its delivery channel, presentation format, or storage technology.

---

# Business Meaning

Content represents business information.

It enables communication between an organization and its stakeholders and may support commercial, operational, educational, legal, or marketing activities.

Content represents the information itself rather than the medium through which it is delivered.

---

# Core Principles

Content:

- shall have a unique identity;
- shall represent a single logical information asset;
- may exist in multiple formats;
- may be published through multiple channels;
- may participate in multiple Campaigns;
- shall remain identifiable throughout its lifecycle.

---

# Mandatory Attributes

| Attribute | Description |
|------------|-------------|
| Identifier | Globally unique identity |
| Title | Content title |
| State | Current operational state |
| Lifecycle | Governing lifecycle |
| Domain | Governing Domain |
| Owner | Responsible owner |
| Created At | Creation timestamp |

---

# Optional Attributes

| Attribute | Description |
|------------|-------------|
| Description | Content summary |
| Language | Primary language |
| Format | Text, image, video, audio, document, etc. |
| Version | Content version |
| Tags | Classification labels |
| Metadata | Additional implementation-specific information |

---

# Ownership

Every Content shall have one responsible Owner.

The Owner is accountable for governance and lifecycle integrity.

---

# Domain

Every Content shall belong to exactly one primary Domain.

---

# States

Content may include the following operational states:

- Draft
- Under Review
- Approved
- Published
- Unpublished
- Archived

Additional states may be introduced provided they remain consistent with the Lifecycle.

---

# Lifecycle

The Content Lifecycle defines all valid state transitions.

Undefined transitions are prohibited.

---

# Relationships

Content may establish relationships with:

- Brand
- Campaign
- Creative
- Landing
- Offer
- Event

Relationship definitions are specified separately.

---

# Events

Typical Events associated with Content include:

- Content Created
- Content Updated
- Content Submitted for Review
- Content Approved
- Content Published
- Content Unpublished
- Content Archived

Events represent immutable operational facts.

---

# Business Rules

Business Rules governing Content are implementation-specific.

Examples include:

- approval workflow;
- publication schedule;
- localization requirements;
- retention policies;
- editorial standards.

---

# Invariants

The following conditions shall always remain true.

- Every Content shall have exactly one Identifier.
- Every Content shall belong to exactly one primary Domain.
- Every Content shall have one current State.
- Every Content shall follow one defined Lifecycle.
- Every Content shall have one responsible Owner.

---

# Constraints

Content shall never:

- exist without an Identifier;
- exist without a Lifecycle;
- exist without a State;
- exist without an Owner;
- violate its defined Lifecycle.

---

# Conformance

Content conforms to this specification only if all mandatory requirements defined in this document are satisfied.

---

# Examples

Examples are informative and are not part of the normative specification.

Example implementations may differ while remaining conformant to this specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

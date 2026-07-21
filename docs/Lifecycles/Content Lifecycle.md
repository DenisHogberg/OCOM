<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Content Lifecycle

[← Back](Commercial%20Lifecycle.md) · [↑ Up](README.md) · [Next →](Financial%20Lifecycle.md)

---
<!-- nav:end -->

# Content Lifecycle

**Document ID:** Lifecycle-03

**Category:** Content

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This Lifecycle defines the standard progression of content-related Entities throughout their operational existence.

It provides a reusable lifecycle model for digital assets that are created, reviewed, published, maintained, and eventually retired.

---

# Applicable Entities

This Lifecycle may be used by, but is not limited to:

- Brand
- Content
- Creative
- Landing
- Banner
- Email Template
- Knowledge Base Article

---

# States

## Draft

The Entity is being created or edited.

---

## Review

The Entity is undergoing editorial, legal, compliance, or quality review.

---

## Approved

The Entity has passed all required reviews and is ready for publication.

---

## Published

The Entity is publicly available or actively used.

---

## Updated

The published Entity has been modified and awaits republication or deployment.

---

## Retired

The Entity is no longer intended for active use.

This is a terminal business state.

---

## Archived

The Entity is retained for historical or audit purposes.

This is a terminal state.

---

# State Transitions

| From | To |
|------|----|
| Draft | Review |
| Review | Draft |
| Review | Approved |
| Approved | Published |
| Published | Updated |
| Updated | Review |
| Published | Retired |
| Retired | Archived |

---

# Invalid Transitions

The following transitions are prohibited:

- Draft → Published
- Review → Published
- Approved → Retired
- Archived → Any State

---

# Entry Conditions

An Entity enters this Lifecycle upon creation.

---

# Exit Conditions

The Lifecycle ends when the Entity reaches the Archived state.

---

# Terminal States

- Retired
- Archived

---

# Conformance

A content Entity conforms to this Lifecycle if:

- it implements the defined States;
- it permits only the defined State Transitions;
- it prohibits undefined transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

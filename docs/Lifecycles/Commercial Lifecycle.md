<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Commercial Lifecycle

[↑ Up](README.md) · [Next →](Content%20Lifecycle.md)

---
<!-- nav:end -->

# Commercial Lifecycle

**Document ID:** Lifecycle-02

**Category:** Commercial

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This Lifecycle defines the standard progression of commercial Entities throughout their operational existence.

It provides a reusable lifecycle model for commercial relationships, agreements, offers, campaigns, and similar business Entities.

---

# Applicable Entities

This Lifecycle may be used by, but is not limited to:

- Partner
- Affiliate
- Offer
- Campaign
- Bonus
- Vendor Agreement

---

# States

## Draft

The Entity has been created but is still under preparation.

---

## Review

The Entity is undergoing internal validation or approval.

---

## Approved

The Entity has successfully passed validation and is ready for activation.

---

## Active

The Entity is operational and available for business use.

---

## Suspended

The Entity has been temporarily deactivated.

It may return to the Active state.

---

## Retired

The Entity has permanently ceased active operation.

This is a terminal business state.

---

## Archived

The Entity has been retained for historical purposes.

This is a terminal state.

---

# State Transitions

| From | To |
|------|----|
| Draft | Review |
| Review | Approved |
| Review | Draft |
| Approved | Active |
| Active | Suspended |
| Suspended | Active |
| Active | Retired |
| Retired | Archived |

---

# Invalid Transitions

The following transitions are prohibited:

- Draft → Active
- Review → Active
- Retired → Active
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

A commercial Entity conforms to this Lifecycle if:

- it implements the defined States;
- it permits only the defined State Transitions;
- it prohibits undefined transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

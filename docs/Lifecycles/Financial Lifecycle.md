<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Financial Lifecycle

[← Back](Content%20Lifecycle.md) · [↑ Up](README.md) · [Next →](Lifecycles.md)

---
<!-- nav:end -->

# Financial Lifecycle

**Document ID:** Lifecycle-01

**Category:** Financial

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This Lifecycle defines the standard progression of financial Entities within the OCOM Specification.

It provides a reusable state model for financial operations while ensuring consistency across different financial Entities.

---

# Applicable Entities

This Lifecycle may be used by, but is not limited to:

- Payment
- Transaction
- Wallet Operation
- Refund
- Payout
- Settlement

---

# States

## Created

The financial Entity has been created but has not yet entered processing.

---

## Pending

The Entity is awaiting validation, authorization, approval, or execution.

---

## Processing

The financial operation is currently being executed.

---

## Completed

The operation has been successfully completed.

This is a terminal state.

---

## Failed

The operation could not be completed due to an error.

This is a terminal state.

---

## Cancelled

The operation was intentionally cancelled before completion.

This is a terminal state.

---

## Archived

The Entity has been retained for historical purposes.

This is a terminal state.

---

# State Transitions

| From | To |
|------|----|
| Created | Pending |
| Pending | Processing |
| Pending | Cancelled |
| Processing | Completed |
| Processing | Failed |
| Completed | Archived |
| Failed | Archived |
| Cancelled | Archived |

---

# Invalid Transitions

The following transitions are prohibited:

- Completed → Processing
- Completed → Pending
- Failed → Processing
- Cancelled → Processing
- Archived → Any State

---

# Entry Conditions

An Entity enters this Lifecycle upon successful creation.

---

# Exit Conditions

The Lifecycle ends when the Entity reaches one of the terminal states.

---

# Terminal States

- Completed
- Failed
- Cancelled
- Archived

---

# Conformance

A financial Entity conforms to this Lifecycle if:

- it implements the defined States;
- it allows only the defined State Transitions;
- it does not permit undefined transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

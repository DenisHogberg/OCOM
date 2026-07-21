<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Operational Lifecycle

[← Back](Lifecycles.md) · [↑ Up](README.md) · [Next →](Organizational%20Lifecycle.md)

---
<!-- nav:end -->

# Operational Lifecycle

**Document ID:** Lifecycle-04

**Category:** Operational

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This Lifecycle defines the standard progression of operational Entities throughout their execution.

It provides a reusable lifecycle model for work items, operational requests, incidents, service activities, and similar operational processes.

---

# Applicable Entities

This Lifecycle may be used by, but is not limited to:

- Task
- Ticket
- Event
- Incident
- Change Request
- Service Request

---

# States

## Created

The Entity has been created but has not yet been assigned or started.

---

## Assigned

The Entity has been assigned to an Owner or responsible Team.

---

## In Progress

Work on the Entity is actively being performed.

---

## On Hold

Work has been temporarily suspended.

The Entity may return to the In Progress state.

---

## Completed

The work has been successfully finished.

This is a terminal business state.

---

## Cancelled

The work has been intentionally terminated before completion.

This is a terminal business state.

---

## Archived

The Entity is retained for historical or audit purposes.

This is a terminal state.

---

# State Transitions

| From | To |
|------|----|
| Created | Assigned |
| Assigned | In Progress |
| In Progress | On Hold |
| On Hold | In Progress |
| In Progress | Completed |
| Created | Cancelled |
| Assigned | Cancelled |
| In Progress | Cancelled |
| Completed | Archived |
| Cancelled | Archived |

---

# Invalid Transitions

The following transitions are prohibited:

- Created → Completed
- Assigned → Completed
- Completed → In Progress
- Cancelled → In Progress
- Archived → Any State

---

# Entry Conditions

An Entity enters this Lifecycle upon creation.

---

# Exit Conditions

The Lifecycle ends when the Entity reaches the Archived state.

---

# Terminal States

- Completed
- Cancelled
- Archived

---

# Conformance

An operational Entity conforms to this Lifecycle if:

- it implements the defined States;
- it permits only the defined State Transitions;
- it prohibits undefined transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

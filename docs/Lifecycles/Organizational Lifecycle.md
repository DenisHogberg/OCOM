<!-- nav:start -->
[Docs](../README.md) / [Lifecycles](README.md) / Organizational Lifecycle

[← Back](Operational%20Lifecycle.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Organizational Lifecycle

**Document ID:** Lifecycle-05

**Category:** Organizational

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This Lifecycle defines the standard progression of organizational Entities throughout their existence within an organization.

It provides a reusable lifecycle model for organizational structures, roles, teams, employees, and AI Agents.

---

# Applicable Entities

This Lifecycle may be used by, but is not limited to:

- Department
- Team
- Employee
- AI Agent
- Role
- Organizational Unit

---

# States

## Proposed

The Entity has been identified but has not yet been formally established.

---

## Active

The Entity is operational and performs its intended responsibilities.

---

## Suspended

The Entity has been temporarily deactivated while retaining the possibility of reactivation.

---

## Retired

The Entity has permanently ceased operation.

This is a terminal business state.

---

## Archived

The Entity is retained for historical, audit, or compliance purposes.

This is a terminal state.

---

# State Transitions

| From | To |
|------|----|
| Proposed | Active |
| Active | Suspended |
| Suspended | Active |
| Active | Retired |
| Retired | Archived |

---

# Invalid Transitions

The following transitions are prohibited:

- Proposed → Suspended
- Proposed → Retired
- Suspended → Retired
- Archived → Any State

---

# Entry Conditions

An Entity enters this Lifecycle upon creation or formal proposal.

---

# Exit Conditions

The Lifecycle ends when the Entity reaches the Archived state.

---

# Terminal States

- Retired
- Archived

---

# Conformance

An organizational Entity conforms to this Lifecycle if:

- it implements the defined States;
- it permits only the defined State Transitions;
- it prohibits undefined transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

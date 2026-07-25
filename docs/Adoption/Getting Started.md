# Getting Started with OCOM

**Document ID:** ADOPTION-GETTING-STARTED-01

**Status:** Informative

**Version:** 0.1

---

This is a simplified, guided path. Every claim here is backed by a normative document — look for the *(see ...)* references if you want the precise wording.

## 1. What Is OCOM

OCOM (Object-Centric Operating Model) describes an organization through the things it manages — customers, payments, campaigns, cases, whatever your business actually deals with — and the relationships between them, independently of the software used to run it *(see `docs/Specification/00 Executive Overview.md`)*.

It is not a product, a database schema, or a piece of software. It is a specification: a consistent way of describing operational reality that stays valid even as the systems underneath it change *(see `Core/Manifest.md`, Abstract)*.

## 2. What Problems It Solves

Most organizations describe themselves through whatever system happens to hold the data — an ERP here, a CRM there. When that knowledge is scattered across tools, it becomes fragmented, duplicated, and inconsistent, and nobody has one authoritative answer to "what is a customer, exactly, and what can happen to one?" *(see `Core/Manifest.md`, Motivation)*.

OCOM gives every such concept one consistent, technology-independent definition, so that people and systems reading it agree on what it means *(see `Core/Principles.md`, Principle 7 — Single Source of Truth)*.

## 3. The Minimal Set of Concepts

You do not need the whole vocabulary to start. Four ideas cover almost everything a first model needs:

- **Entity** — a real thing your business manages: identifiable, owned, with a lifecycle. This is what you model *(see `Models/Entity.md`)*.
- **Domain** — who is responsible for a given Entity. Every Entity belongs to exactly one Domain *(see `Models/Domain.md`)*.
- **State** — the condition an Entity is in right now *(see `Models/State.md`)*.
- **Lifecycle** — the complete set of States an Entity can be in, and which transitions between them are allowed *(see `Models/Lifecycle.md`)*.

Everything else — Relationship, Event, Capability, Policy, Contract — matters, but you can learn it as you need it. See `docs/Specification/03 Core Concepts.md` for the full picture when you're ready.

## 4. How to Model Your First Object

Every Entity needs, at minimum, seven things *(see `Models/Entity.md`, "Minimal Entity")*: an **Identifier**, a **Name**, a **Domain**, an **Owner**, its **Attributes**, a **State**, and a **Lifecycle**.

Walk through it with something simple — say, a support **Ticket**:

| Field | Example value |
|---|---|
| Identifier | `TCK-000123` |
| Name | Ticket |
| Domain | Support |
| Owner | Support Team |
| Attributes | subject, priority, requester |
| State | `Open` |
| Lifecycle | see step 5 below |

That's it — a conforming Entity. You do not need to model your whole business to have a valid first Object. One Entity, correctly defined, is a complete, useful starting point.

## 5. How to Define a Lifecycle

A Lifecycle is just the States your Entity can be in, and the transitions allowed between them *(see `Models/Lifecycle.md`)*. For the Ticket above, a minimal Lifecycle might be:

```text
Open
  │
  ▼
In Progress
  │
  ▼
Resolved
  │
  ▼
Closed
```

Two rules matter from the start: every Entity is in exactly one State at a time, and a transition that isn't drawn in your Lifecycle diagram is not allowed to happen *(see `Models/Lifecycle.md`, "Transitions")*. Keep your first Lifecycle small — four or five states is plenty.

## 6. How to Start Applying OCOM in a Small Team

Pick one Domain your team already owns. Model two or three Entities that Domain is responsible for, each with a minimal Lifecycle like the one above. Do not try to model the whole company, and do not wait for tooling or automation — OCOM does not require either to be useful *(see `Core/Principles.md`, Principle 6 — Separation of Model and Implementation)*.

Expect it to feel small at first. That is by design — the Core is meant to be minimal, and grows only when repeated real experience shows it needs to *(see `docs/Governance/Standard Evolution Methodology.md`, Principle of Minimal Evolution)*.

When you're ready to try this for real, continue to **[First Pilot](First%20Pilot.md)**.

---

*Source: this document restates, and does not extend, `Core/Manifest.md`, `Core/Principles.md`, `Models/Entity.md`, `Models/Domain.md`, `Models/State.md`, `Models/Lifecycle.md`, and `docs/Governance/Standard Evolution Methodology.md`. The Ticket example is illustrative only and is not part of the normative specification.*

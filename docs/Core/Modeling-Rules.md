<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Modeling Rules

[← Back](Manifest.md) · [↑ Up](README.md) · [Next →](Naming.md)

---
<!-- nav:end -->

# Modeling Rules

**Document ID:** Core-04

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the normative rules for constructing operational models using this specification.

---

# Rule 1 — Every Entity Must Have an Identifier

Every entity shall possess a unique identifier.

---

# Rule 2 — Every Entity Must Belong to a Domain

An entity shall be governed by exactly one primary domain.

---

# Rule 3 — Every Entity Must Have an Owner

Ownership shall always be explicitly defined.

---

# Rule 4 — Every Entity Must Define States

Each entity shall define one or more operational states.

---

# Rule 5 — Every Entity Must Define a Lifecycle

A lifecycle shall describe all valid state transitions.

---

# Rule 6 — Workflows Transform States

A workflow shall only perform state transitions defined by the entity lifecycle.

---

# Rule 7 — Relationships Must Be Explicit

Relationships between entities shall be explicitly modeled.

Implicit relationships are not permitted.

---

# Rule 8 — Models Must Avoid Duplication

Operational concepts shall have one authoritative definition.

Duplicate models should not exist.

---

# Rule 9 — Models Must Remain Technology Independent

Operational models shall not depend on implementation technologies.

---

# Rule 10 — Models Must Be Human and Machine Readable

Operational models shall be structured to enable consistent interpretation by both humans and software systems.

---

# Validation

A model conforms to this specification only if all mandatory rules are satisfied.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

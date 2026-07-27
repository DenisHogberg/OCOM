<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Principles

[← Back](Naming.md) · [↑ Up](README.md) · [Next →](Terminology.md)

---
<!-- nav:end -->

# Principles

**Document ID:** Core-02

**Status:** Draft

**Version:** 0.1

**Last Updated:** 23 July 2026

---

# Purpose

This document defines the fundamental principles governing the operational modeling framework.

These principles are normative and apply to every model created using this specification.

These Principles operate within, and shall not contradict, the Canonical Principles of the OCOM Constitution (`Core/Constitution.md`).

---

# Principle 1 — Organization Before Technology

Operational models describe organizations independently of software, platforms, vendors, and implementation technologies.

Technology implements the model but never defines it.

---

# Principle 2 — Entity-Centric Modeling

Object is the universal abstraction of the operational model (Constitution §1). Entity is a specialization of Object.

Every operational concept shall be represented through identifiable entities.

Entities are the primary building blocks of the operational model.

---

# Principle 3 — Explicit Ownership

Every entity shall have a clearly defined owner responsible for its lifecycle, integrity, and operational consistency.

Ownership shall never be implicit.

---

# Principle 4 — State-Based Operations

Operational activities exist to transform entity states.

Every significant operational change should be represented as a state transition.

---

# Principle 5 — Domain Responsibility

Responsibilities belong to domains.

Domains define accountability, governance, and operational boundaries.

---

# Principle 6 — Separation of Model and Implementation

Implementations adapt to the operational model; the operational model never adapts to implementation-specific constraints (Constitution §13).

The operational model shall remain independent of software architecture, databases, APIs, programming languages, and infrastructure.

Implementations may change without changing the operational model.

---

# Principle 7 — Single Source of Truth

Each operational concept shall have a single authoritative definition within the model.

Duplicate definitions should be avoided.

---

# Principle 8 — Semantic Consistency

Equivalent concepts shall be modeled consistently throughout the specification.

Naming, behavior, and relationships should remain predictable.

---

# Principle 9 — AI Interpretability

Operational models should be understandable by both humans and artificial intelligence without requiring implementation-specific knowledge.

---

# Principle 10 — Evolvability

The framework shall support organizational evolution without requiring redesign of the underlying operational model.

---

# Principle 11 — Separation of Professional Responsibility

This principle is canonically stated in Constitution §14 — Professional Responsibility (`Core/Constitution.md`).

OCOM deliberately separates the management of operational memory from professional expertise.

OCOM is responsible for Operational Memory, the Object Model, Knowledge Management, Context Preservation, Workflow Coordination, Decision Tracking, and Action Tracking.

Professional functions of the organization — including Legal, Compliance, Finance, Security, and HR — are responsible for expert judgments and decisions within their domains. OCOM shall not substitute for professional expertise; it supports that expertise through structured operational memory.

---

# Conformance

All models created using this specification shall conform to these principles.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 23 July 2026 | Added Principle 11 — Separation of Professional Responsibility (ADR CAND-003, Promoted 23 July 2026) |
| 0.1 | 27 July 2026 | Added Object-as-root sentence to Principle 2 per ARCH-003 (existing scope preserved); added Constitution §14 reference to Principle 11 (existing body preserved); added Constitution §13 cross-reference to Principle 6; added Purpose-section pointer to Constitution, per CAND-006 Step 0 integration |

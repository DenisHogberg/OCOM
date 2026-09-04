# OCOM Specification v0.2 — Design Principles

**Document ID:** SPEC-02

**Status:** Draft

**Version:** 0.2

---

These eleven principles are normative and apply to every model created using this specification.

## 1. Organization Before Technology

Operational models describe organizations independently of software, platforms, vendors, and implementation technologies. Technology implements the model but never defines it.

## 2. Entity-Centric Modeling

Object is the universal abstraction of the operational model (Constitution §1). Entity is a specialization of Object. Every operational concept **shall** be represented through identifiable entities. Entities are the primary building blocks of the operational model.

## 3. Explicit Ownership

Every entity **shall** have a clearly defined owner responsible for its lifecycle, integrity, and operational consistency. Ownership **shall** never be implicit.

## 4. State-Based Operations

Operational activities exist to transform entity states. Every significant operational change **should** be represented as a state transition.

## 5. Domain Responsibility

Responsibilities belong to domains. Domains define accountability, governance, and operational boundaries.

## 6. Separation of Model and Implementation

Implementations adapt to the operational model; the operational model never adapts to implementation-specific constraints (Constitution §13). The operational model **shall** remain independent of software architecture, databases, APIs, programming languages, and infrastructure. Implementations may change without changing the operational model.

## 7. Single Source of Truth

Each operational concept **shall** have a single authoritative definition within the model. Duplicate definitions **should** be avoided.

## 8. Semantic Consistency

Equivalent concepts **shall** be modeled consistently throughout the specification. Naming, behavior, and relationships **should** remain predictable.

## 9. AI Interpretability

Operational models **should** be understandable by both humans and artificial intelligence without requiring implementation-specific knowledge.

## 10. Evolvability

The framework **shall** support organizational evolution without requiring redesign of the underlying operational model.

## 11. Separation of Professional Responsibility

This principle is canonically stated in Constitution §14 — Professional Responsibility (`Core/Constitution.md`). OCOM deliberately separates the management of operational memory from professional expertise. OCOM is responsible for Operational Memory, the Object Model, Knowledge Management, Context Preservation, Workflow Coordination, Decision Tracking, and Action Tracking. Professional functions of the organization — including Legal, Compliance, Finance, Security, and HR — are responsible for expert judgments and decisions within their domains. OCOM **shall not** substitute for professional expertise; it supports that expertise through structured operational memory.

## Conformance

All models created using this specification **shall** conform to these principles.

---

*Source: compiled from `Core/Principles.md`, verbatim, including principle titles. (Committee Review, 22 July 2026: an earlier draft retitled Principle 9 to "Interpretability"; the Architecture Committee directed reversion to the source title, on the basis that retitling a sourced principle is an architectural judgment requiring an ADR, not an editorial choice.) (4 September 2026: resynchronised with `Core/Principles.md` after Principle 11 (ADR CAND-003, 23 July 2026) and the Constitution cross-references in Principles 2 and 6 (CAND-006) were added to the source; editorial recompilation, no content of its own.)*

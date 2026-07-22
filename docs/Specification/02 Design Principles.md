# OCOM Specification v0.2 — Design Principles

**Document ID:** SPEC-02

**Status:** Draft

**Version:** 0.2

---

These ten principles are normative and apply to every model created using this specification.

## 1. Organization Before Technology

Operational models describe organizations independently of software, platforms, vendors, and implementation technologies. Technology implements the model but never defines it.

## 2. Entity-Centric Modeling

Every operational concept **shall** be represented through identifiable entities. Entities are the primary building blocks of the operational model.

## 3. Explicit Ownership

Every entity **shall** have a clearly defined owner responsible for its lifecycle, integrity, and operational consistency. Ownership **shall** never be implicit.

## 4. State-Based Operations

Operational activities exist to transform entity states. Every significant operational change **should** be represented as a state transition.

## 5. Domain Responsibility

Responsibilities belong to domains. Domains define accountability, governance, and operational boundaries.

## 6. Separation of Model and Implementation

The operational model **shall** remain independent of software architecture, databases, APIs, programming languages, and infrastructure. Implementations may change without changing the operational model.

## 7. Single Source of Truth

Each operational concept **shall** have a single authoritative definition within the model. Duplicate definitions **should** be avoided.

## 8. Semantic Consistency

Equivalent concepts **shall** be modeled consistently throughout the specification. Naming, behavior, and relationships **should** remain predictable.

## 9. AI Interpretability

Operational models **should** be understandable by both humans and artificial intelligence without requiring implementation-specific knowledge.

## 10. Evolvability

The framework **shall** support organizational evolution without requiring redesign of the underlying operational model.

## Conformance

All models created using this specification **shall** conform to these principles.

---

*Source: compiled from `Core/Principles.md`, verbatim, including principle titles. (Committee Review, 22 July 2026: an earlier draft retitled Principle 9 to "Interpretability"; the Architecture Committee directed reversion to the source title, on the basis that retitling a sourced principle is an architectural judgment requiring an ADR, not an editorial choice.)*

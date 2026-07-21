<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Memory Record

[← Back](Layered%20Memory.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Memory Record

**Document ID:** Memory-02

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the standardized structure of a Memory Record within the OCOM Memory Specification.

A Memory Record is the fundamental unit of operational memory used by AI Agents and business systems.

The Memory Record provides a consistent representation of retained knowledge regardless of storage technology or implementation.

---

# Definition

A Memory Record represents a single retained fact, observation, inference, or decision together with its operational metadata.

A Memory Record is immutable in identity but may evolve through controlled updates.

---

# Design Principles

Every Memory Record shall be:

- uniquely identifiable;
- explainable;
- evidence-backed;
- confidence-aware;
- auditable;
- governed;
- technology independent.

---

# Mandatory Attributes

Every Memory Record shall define:

- Identifier
- Subject
- Memory Type
- Value
- Layer
- Status
- Created Date

---

# Optional Attributes

A Memory Record may define:

- Description
- Category
- Tags
- Expiration Date
- Owner
- Related Entity
- Related Workflow
- Related Event

---

# Memory Types

A Memory Record may represent:

- Fact
- Observation
- Decision
- Preference
- Rule
- Relationship
- Summary
- Inference
- Prediction
- Exception

Additional types may be introduced by future specifications.

---

# Identity

Each Memory Record shall have a globally unique identifier.

The identifier shall remain stable throughout the lifetime of the record.

---

# Subject

The Subject identifies the entity or operational context to which the memory belongs.

Examples include:

- Customer
- Partner
- Vendor
- Employee
- Contract
- Payment
- Campaign

---

# Value

The Value represents the retained operational knowledge.

The value may be:

- structured;
- semi-structured;
- unstructured.

Implementations may choose any internal representation.

---

# Layer

Every Memory Record shall belong to exactly one memory layer.

Permitted values are:

- Transient
- Stage
- Long-Term
- Persistent

Layer transitions are governed by the Layered Memory specification.

---

# Status

Typical statuses include:

- Active
- Pending Verification
- Archived
- Expired
- Rejected

Organizations may extend the status model.

---

# Relationships

A Memory Record may reference:

- Entities
- Events
- Workflows
- Lifecycles
- AI Agents
- Other Memory Records

---

# Evidence

A Memory Record may reference one or more Evidence Records.

Evidence provides the basis for explainability and confidence assessment.

The structure of Evidence is defined separately in the Evidence Overlay specification.

---

# Confidence

A Memory Record may include a confidence assessment.

Confidence expresses the estimated reliability of the retained knowledge.

The confidence model is defined in the Confidence specification.

---

# Governance

Every Memory Record shall define its governance policy.

Governance may include:

- write permissions;
- update permissions;
- approval requirements;
- write-back policy;
- retention policy.

---

# Auditability

Every Memory Record shall preserve an audit trail including:

- creator;
- creation time;
- last modification;
- modifier;
- modification reason.

Audit information shall not be removed.

---

# Independence

The Memory Record specification does not prescribe:

- storage engines;
- databases;
- vector representations;
- embedding models;
- serialization formats.

Implementations remain technology independent.

---

# Conformance

A compliant implementation shall:

- implement all mandatory attributes;
- preserve record identity;
- support evidence references;
- support confidence assessment;
- preserve audit history;
- comply with governance policies.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

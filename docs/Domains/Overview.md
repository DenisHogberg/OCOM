<!-- nav:start -->
[Docs](../README.md) / [Domains](README.md) / Domains

[↑ Up](README.md)

---
<!-- nav:end -->

# Domains

**Document ID:** DOMAINS-README-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 16 September 2026

---

# Purpose

**Status note (20 August 2026):** `Constitution-Step0-Summary.md` Decision 4 found `Domains/` to be a "genuine borderline case" for Constitution §9's Domain-Neutral Core — most domain names are universal business-function categories, but at least one (`Affiliate`) leans toward a specific business model — and explicitly declined a blanket ruling in favor of "ongoing, per-document judgment." This Status is deliberately left as `Draft`, not changed to `Informative`, pending that ongoing review — see `Governance/Publication-Model.md` and `Governance/Documentation-Standards.md`'s Status Taxonomy. This is not an oversight; changing it now would decide something Decision 4 explicitly left open.

This specification defines the domain architecture of the OCOM framework.

Domains provide a structured way to organize enterprise operational capabilities into cohesive business areas while maintaining a unified object-centric operational model.

The Domains specification establishes common principles applicable to all business domains defined by OCOM.

---

# Scope

This specification defines:

- the concept of a Domain;
- common domain architecture;
- domain boundaries;
- domain integration;
- domain communication;
- domain governance;
- domain evolution.

It does not define the internal implementation of individual domains.

Domain-specific requirements are defined in their respective specifications.

---

# Objectives

The objectives of the Domains specification are to:

- organize enterprise capabilities into coherent domains;
- establish clear ownership boundaries;
- enable interoperability between domains;
- support object-centric operations;
- promote modular enterprise architecture;
- facilitate AI-enabled enterprise operations.

---

# Design Principles

The Domains specification follows these principles:

- Object-Centric Design
- Clear Domain Ownership
- High Cohesion
- Loose Coupling
- Explicit Integration
- Event-Driven Collaboration
- Policy-Based Governance
- Technology Independence
- AI Readiness
- Incremental Evolution

---

# Domain Model

Every OCOM Domain represents a logical business capability.

A Domain manages a defined set of Objects together with their operational responsibilities.

Domains collaborate through shared Objects, Relationships, References, Events, Policies, and Contracts rather than through organizational structures or implementation technologies.

---

# Common Domain Structure

Every Domain specification should define, where applicable:

- Objects
- Relationships
- Events
- Lifecycles
- Processes
- Policies
- KPIs
- AI Responsibilities

Additional domain-specific sections may be introduced without modifying the common architecture.

---

# Domain Independence

Domains are logically independent.

Each Domain:

- owns its business responsibilities;
- governs its internal rules;
- manages its operational lifecycle;
- exposes explicit integration points.

Domain independence reduces coupling while preserving enterprise-wide consistency.

---

# Cross-Domain Collaboration

Domains collaborate through standardized mechanisms including:

- shared Objects;
- References;
- Relationships;
- Events;
- Contracts;
- Policies.

No Domain should directly depend on the internal implementation of another Domain.

---

# Relationship to Other Specifications

The Domains specification builds upon:

- Meta
- Core
- Language
- Models
- Entities
- Lifecycles
- Memory
- AI

Individual business domains specialize the principles defined by this specification.

---

# Relationship to Memory

Memory operates across all OCOM Domains, per `Memory/Overview.md`, and a Memory Record may reference Entities, Events, Workflows, Lifecycles, AI Agents and other Memory Records, per `Memory/Memory Record.md`. The Memory specification states this once for every Domain; this specification does not require each Domain to restate it.

Of the thirteen Domain AI documents, five carry a section headed AI Memory, in BI, Compliance, CRM, Finance and Payments. Each states that the Domain's AI may consume and contribute to enterprise Memory subject to Memory governance, evidence, retention and privacy requirements, with Memory Ownership unchanged; the Compliance section additionally names regulatory obligations. The five sections restate the Memory specification for their Domain and impose no requirement on Memory itself. The eight Domain AI documents that carry no such section, in AI, Affiliate, HR, Legal, Marketing, Operations, Product and Support, are not exceptions: the same relationship holds for them by virtue of the Memory specification, and their silence is closed by this section rather than by a copy of that text in each. `Domains/Common` defines no Domain of its own and carries none. A Domain that departs from this relationship states so in its own AI document; none does in this version.

This section is the explicit disposition `Governance/Master-Architecture-Backlog.md` Part 8 permits for EPIC-C in place of a uniform section, recorded 16 September 2026.

---

# Directory Structure

The Domains package consists of:

- Common
- AI
- Affiliate
- BI
- CRM
- Compliance
- Finance
- HR
- Legal
- Marketing
- Operations
- Payments
- Product
- Support

Additional Domains may be introduced in future versions without affecting existing specifications.

---

# Independence

The Domains specification does not prescribe:

- organizational structures;
- departments;
- software products;
- implementation technologies;
- deployment models.

Organizations remain free to implement Domains according to their operational requirements while preserving the principles defined by OCOM.

---

# Conformance

A conforming Domain specification shall:

- follow the common domain architecture;
- preserve object-centric principles;
- define explicit ownership;
- support standardized integration;
- remain compatible with the OCOM Core Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |
| 0.1 | 20 August 2026 | Added status note citing `Constitution-Step0-Summary.md` Decision 4's "genuine borderline case" finding; Status left unchanged (`Draft`), deliberately, pending ongoing per-document review |
| 0.1 | 16 September 2026 | Added Relationship to Memory: the Domain-level linkage to Memory is stated once by `Memory/Overview.md`; the five AI Memory sections (BI, Compliance, CRM, Finance, Payments) restate it for their Domain, the eight Domain AI documents without one are not exceptions. Explicit disposition for EPIC-C per `Master-Architecture-Backlog.md` Part 8, under `CAND-007` Section 3. |

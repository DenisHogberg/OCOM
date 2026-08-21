<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Manifest

[← Back](Governance.md) · [↑ Up](README.md) · [Next →](Modeling-Rules.md)

---
<!-- nav:end -->

# Manifest

**Document ID:** Core-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 23 July 2026

---

# Abstract

OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations, describing organizations through entities, domains, workflows, and their relationships. This document defines the modeling framework through which that operating model is expressed.

The framework provides a common operational language that enables consistent understanding by humans, software systems, and artificial intelligence while remaining independent of implementation technologies, vendors, organizational structures, and industries.

---

# Purpose

The purpose of this specification is to establish a universal operational language for describing how organizations function.

Rather than treating software systems, departments, or business processes as primary concepts, the framework models the organization itself through a consistent set of operational concepts and relationships.

The specification provides a stable foundation for documentation, analysis, governance, automation, and future operational development.

---

# Vision

Organizations should be described independently of the technologies used to operate them.

Operational knowledge should remain stable as software platforms, organizational structures, and implementation details evolve.

Humans and artificial intelligence should be able to interpret the same operational model consistently.

---

# Motivation

Operational knowledge is commonly distributed across documents, applications, teams, and software platforms.

As organizations evolve, this knowledge often becomes fragmented, duplicated, inconsistent, and difficult to maintain.

Existing approaches usually describe isolated perspectives such as business processes, organizational structures, databases, or software architecture rather than the operational system as a whole.

This specification introduces a unified operational model capable of representing an organization through consistent operational concepts and relationships.

---

# Guiding Statement

Organizations are not defined by their software.

They are defined by the operational relationships between the entities that create, transform, exchange, and preserve business value.

This specification provides a common operational language for describing those relationships independently of implementation.

---

# Core Objectives

This specification aims to:

- establish a common operational vocabulary;
- improve consistency across operational models;
- reduce ambiguity in organizational documentation;
- support interoperability between operational systems;
- enable AI-assisted analysis and automation;
- provide a stable foundation for future operational standards.

---

# Design Goals

The framework is designed to be:

- technology-independent;
- implementation-independent;
- vendor-neutral;
- extensible;
- deterministic;
- human-readable;
- machine-readable;
- AI-native.

---

# Applicability

This specification may be applied to organizations of any size and across any industry.

The framework is intended for operational modeling and may be adopted regardless of existing organizational structures, software platforms, or implementation technologies.

---

# Scope

This specification defines:

- operational concepts;
- entities;
- domains;
- workflows;
- operational relationships;
- modeling principles;
- semantic interpretation rules.

This specification does not define:

- software architecture;
- databases;
- APIs;
- programming languages;
- user interface design;
- infrastructure;
- implementation technologies;
- business strategy;
- professional or expert judgments (legal, compliance, financial, or similar);
- the responsibilities of an organization's specialized functions (Legal, Compliance, Finance, Security, HR, and others) — per Constitution §14, Professional Responsibility.

---

# Design Philosophy

The framework is based on several fundamental ideas.

Organizations are composed of interacting entities.

Domains define responsibility.

Workflows transform entity states.

Knowledge belongs to entities.

Software implements the operational model but does not define it — per Constitution §13, Adaptation Flows Toward the Model.

Operational models should remain understandable by both humans and artificial intelligence.

---

# Intended Audience

This specification is intended for:

- Enterprise Architects;
- Operations Leaders;
- Solution Architects;
- System Designers;
- Business Analysts;
- Product Organizations;
- Software Engineers;
- AI Engineers;
- Researchers.

---

# Normative Language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**, when they appear in all capitals in this document, and in every document of this specification, are to be interpreted as described in RFC 2119, as amended by RFC 8174:

- **MUST** indicates an absolute requirement.
- **MUST NOT** indicates an absolute prohibition.
- **SHOULD** indicates a recommended practice.
- **SHOULD NOT** indicates a practice that is generally discouraged.
- **MAY** indicates an optional capability or implementation choice.

This is the single authoritative definition of these key words for the entire specification. Independently of RFC 8174's own all-capitals restriction, this specification additionally extends the same defined meanings to the lowercase forms (**shall**, **shall not**, **should**, **may** — the convention already used throughout `Meta/`, `Models/`, `Core/`, and `Language/`): a document using a lowercase form intends the same normative weight as its uppercase equivalent above, by this specification's own convention, not because RFC 8174 itself extends that far. Any document restating this definition, rather than citing it, is a duplication to be corrected, not a second source.

---

# Conformance

Conformance to this specification requires compliance with the normative documents that form part of this specification.

Requirements defined in subsequent documents build upon the concepts introduced in this Manifest.

---

# Future Evolution

This specification is intended to evolve through successive versions while preserving conceptual consistency.

Future revisions may introduce new concepts, models, and extensions without changing the fundamental principles established by this specification.

---

# Related Documents

- Core-00 Constitution
- Core-02 Principles
- Core-03 Terminology
- Core-04 Naming
- Core-05 Modeling Rules
- Core-06 Governance
- Core-07 Versioning

---

# Document Status

This document represents the initial draft of the specification and is subject to revision before version 1.0.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 23 July 2026 | Scope extended to exclude professional/expert judgments and specialized organizational functions, per Principle 11 (ADR CAND-003) |
| 0.1 | 27 July 2026 | Added cross-references to Constitution §14 and §13; added Core-00 Constitution to Related Documents, per CAND-006 Step 0 integration |
| 0.1 | 20 August 2026 | Added explicit RFC 2119 / RFC 8174 citation to Normative Language, making this section the specification's single authoritative source for MUST/SHOULD/MAY — per `Governance/Publication-Model.md` |
| 0.1 | 21 August 2026 | Abstract reworded to lead with the canonical identity statement ("OCOM is an open, technology-independent operating model for organizations"), aligning with `ocom.uno` and `llms.txt`; "framework" retained as a secondary description of this document's own modeling apparatus, not as OCOM's primary identity noun — semantic positioning only, no change to normative content |

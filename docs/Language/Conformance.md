<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Conformance

[↑ Up](README.md) · [Next →](Identifier%20Syntax.md)

---
<!-- nav:end -->

# Conformance

**Document ID:** LANG-CONFORMANCE-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 16 September 2026

---

# Purpose

This document defines the conformance requirements for implementations of the OCOM Language.

Conformance establishes the criteria by which implementations may claim compliance with the OCOM Specification.

The objective is to promote interoperability, consistency, portability, and predictable behavior across independent implementations.

---

# Definition

Conformance is the degree to which an implementation satisfies the normative requirements defined by the OCOM Language Specification.

Conformance applies to implementations rather than individual models.

In this specification the adjectives conforming, compliant and conformant, when applied to an implementation, are used interchangeably and mean an implementation that satisfies the Mandatory Requirements of this document for the specification version it claims.

---

# Business Meaning

Conformance enables organizations to exchange OCOM models with confidence that independent implementations interpret language constructs consistently.

Conformance reduces integration risk and supports ecosystem interoperability.

---

# Design Principles

Conformance shall:

- be objective;
- be measurable;
- be verifiable;
- preserve interoperability;
- support extensibility;
- remain technology independent.

---

# Conformance Scope

Conformance may apply to:

- modeling tools;
- repositories;
- validation engines;
- exchange services;
- transformation tools;
- runtime platforms.

Organizations may define additional implementation categories.

---

# Mandatory Requirements

A conforming implementation shall:

- implement the required language constructs;
- preserve language semantics;
- support applicable validation;
- preserve identifier integrity;
- maintain namespace consistency.

Mandatory requirements are normative.

---

# Optional Capabilities

The OCOM Specification may define optional capabilities.

Support for optional capabilities shall not affect conformance unless explicitly declared as mandatory by a higher-level specification.

---

# Extension Conformance

Implementations may provide extensions.

Extensions shall:

- preserve compatibility with the core language;
- avoid changing normative semantics;
- remain clearly identifiable;
- be fully documented.

Extensions shall not invalidate conformance with the core specification.

---

# Version Conformance

An implementation shall identify the specification version against which conformance is claimed.

Where multiple versions are supported, each supported version shall be explicitly declared.

---

# Validation of Conformance

Conformance may be demonstrated through:

- automated validation;
- interoperability testing;
- specification review;
- implementation assessment.

The OCOM Specification does not prescribe certification procedures.

---

# Conformance Statement

A conforming implementation should provide a conformance statement including:

- implementation name;
- supported specification version;
- implemented capabilities;
- supported extensions;
- known limitations.

The format of the statement is implementation-specific.

---

# Non-Conformance

If an implementation does not satisfy one or more mandatory requirements, it shall not claim conformance with the corresponding version of the OCOM Specification.

Organizations may document partial support without claiming full conformance.

---

# Governance

Organizations shall establish governance for:

- conformance assessment;
- version management;
- compatibility management;
- extension review;
- conformance documentation.

Governance processes are organization-specific.

---

# Relationship to Other Specifications

Conformance depends upon:

- Vocabulary
- Syntax
- Schema
- Namespace
- Identifier Syntax
- Serialization
- Validation

Conformance evaluates implementation compliance with the OCOM Language Specification.

---

# Independence

The Conformance specification does not prescribe:

- certification bodies;
- compliance programs;
- testing frameworks;
- implementation technologies;
- commercial products.

Organizations remain free to establish their own conformance assessment processes.

---

# Conformance Levels

The OCOM Language defines the following conformance levels.

## Core Conformance

Supports all mandatory language requirements.

---

## Extended Conformance

Supports mandatory requirements together with documented language extensions.

---

## Profile Conformance

Supports a formally defined OCOM profile while preserving compatibility with the core specification.

A profile is formally defined when its claimant has published a Profile Declaration in the form recorded for `CAND-002` (Decided 16 September 2026) in `Governance/Concept-Paper-Profile-Conformance.md`: pinned to a Release and its commit, bounded by whole canonical source documents with their content hashes, containing every document Chapters 4 to 6 of the reading path compile, adding nothing and restating nothing. OCOM publishes no profile and reviews, registers or certifies none.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 5 September 2026 | Definition: stated that conforming, compliant and conformant are used interchangeably for an implementation; no requirement changed. |
| 0.1 | 16 September 2026 | Profile Conformance: added the pointer to the `CAND-002` Decision and its grounding paper, stating the form of a Profile Declaration; no other requirement changed. |

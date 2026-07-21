<!-- nav:start -->
[Docs](../README.md) / [Meta](README.md) / Metadata

[← Back](Identity.md) · [↑ Up](README.md) · [Next →](Object.md)

---
<!-- nav:end -->

# Metadata

**Document ID:** META-METADATA-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Metadata within the OCOM Specification.

Metadata provides descriptive information about an Object without altering its identity, behavior, or business meaning.

Metadata supports discovery, governance, interoperability, traceability, and operational management.

---

# Definition

Metadata is structured information that describes the characteristics, context, or management attributes of an Object.

Metadata supplements an Object but does not define its identity or operational state.

Metadata may evolve throughout the lifecycle of an Object.

---

# Business Meaning

Metadata enables organizations to understand, organize, discover, and govern Objects consistently across operational environments.

Metadata improves interoperability by providing common descriptive attributes independent of implementation technologies.

---

# Design Principles

Metadata shall:

- be descriptive;
- be structured;
- be extensible;
- support interoperability;
- support governance;
- remain technology independent.

---

# Core Characteristics

Metadata may describe:

- identity attributes;
- descriptive attributes;
- administrative attributes;
- governance attributes;
- operational attributes;
- technical attributes.

Organizations may define additional metadata categories.

---

# Metadata Categories

Typical metadata categories include:

## Descriptive Metadata

Provides information describing the Object.

Examples include:

- Name;
- Description;
- Version;
- Summary.

---

## Administrative Metadata

Supports operational management.

Examples include:

- Creation Date;
- Last Modified Date;
- Owner;
- Status.

---

## Governance Metadata

Supports organizational governance.

Examples include:

- Classification;
- Policy References;
- Compliance Status;
- Audit Information.

---

## Technical Metadata

Supports implementation-specific environments.

Examples include:

- Format;
- Encoding;
- Schema Version;
- External References.

Technical Metadata is implementation-specific.

---

# Metadata Lifecycle

Metadata may change throughout the lifecycle of an Object.

Metadata updates shall preserve:

- Object Identity;
- auditability;
- traceability.

Metadata history should be retained according to organizational policy.

---

# Metadata Ownership

Metadata should have defined ownership.

Organizations shall determine who may:

- create metadata;
- modify metadata;
- approve metadata;
- archive metadata.

Ownership shall remain traceable.

---

# Metadata Validation

Organizations should validate Metadata for:

- completeness;
- consistency;
- accuracy;
- required attributes;
- policy compliance.

Validation methods are organization-specific.

---

# Metadata Relationships

Metadata may reference:

- Policies;
- Classifications;
- Registries;
- External Systems;
- Related Objects.

Metadata relationships shall preserve traceability.

---

# Relationship to Other Specifications

Metadata is used throughout the OCOM Specification, including:

- Object
- Identity
- Registry
- Relationship
- Reference
- Lifecycle
- Governance
- Evaluation

All managed Objects may possess Metadata.

---

# Independence

The Metadata specification does not prescribe:

- metadata schemas;
- storage mechanisms;
- serialization formats;
- implementation technologies.

Organizations remain free to implement Metadata using any compatible approach.

---

# Conformance

A compliant implementation shall:

- support structured Metadata;
- preserve Metadata traceability;
- support Metadata governance;
- allow Metadata extension;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

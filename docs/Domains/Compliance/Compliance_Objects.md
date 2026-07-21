<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Compliance](README.md) / Compliance Objects

[← Back](Compliance_KPIs.md) · [↑ Up](README.md) · [Next →](Compliance_Policies.md)

---
<!-- nav:end -->

# Compliance Objects

**Document ID:** DOMAIN-COMPLIANCE-OBJECTS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the business Objects managed by the Compliance Domain.

Compliance Objects represent regulatory obligations, internal controls, compliance assessments, audit activities, findings, evidence, and remediation activities.

These Objects enable enterprise governance while preserving the ownership of operational business Objects within their originating Domains.

---

# Definition

A Compliance Object represents a governed business entity whose purpose is to evaluate, monitor, document, or demonstrate compliance with enterprise obligations.

Compliance Objects possess Identity, Lifecycle, Relationships, Events, Policies, and governance metadata.

Object semantics are defined by the Core specification.

---

# Business Meaning

Compliance Objects provide the enterprise with a standardized representation of governance activities.

They describe compliance status rather than operational business activities.

Operational Objects remain owned by their respective Domains.

---

# Design Principles

Compliance Objects shall:

- possess unique Identity;
- maintain explicit Ownership;
- support Lifecycle management;
- preserve auditability;
- reference operational Objects without assuming ownership;
- remain technology independent.

---

# Object Categories

Compliance Objects may be organized into the following categories.

## Obligation Objects

Objects representing compliance obligations.

Examples include:

- Regulatory Obligation;
- Internal Policy Obligation;
- Contractual Obligation;
- Licensing Obligation;
- Reporting Obligation.

---

## Control Objects

Objects representing enterprise controls.

Examples include:

- Compliance Control;
- Monitoring Control;
- Preventive Control;
- Detective Control;
- Corrective Control.

---

## Assessment Objects

Objects representing compliance evaluations.

Examples include:

- Compliance Assessment;
- Risk Assessment;
- Control Assessment;
- Policy Assessment;
- Regulatory Assessment.

---

## Audit Objects

Objects representing audit activities.

Examples include:

- Audit;
- Audit Plan;
- Audit Evidence;
- Audit Observation;
- Audit Finding.

---

## Evidence Objects

Objects representing supporting compliance information.

Examples include:

- Evidence Record;
- Evidence Collection;
- Compliance Artifact;
- Supporting Documentation.

---

## Remediation Objects

Objects representing corrective activities.

Examples include:

- Remediation Plan;
- Corrective Action;
- Preventive Action;
- Compliance Task.

---

# Object Ownership

The Compliance Domain owns Compliance Objects.

Referenced operational Objects remain owned by their originating Domains.

Ownership shall never transfer through Relationships.

---

# Object Identity

Each Compliance Object shall possess a stable Identity.

Identity remains unchanged throughout the Object Lifecycle.

---

# Object Lifecycle

Every Compliance Object shall possess a defined Lifecycle.

Lifecycle definitions are specified in:

- Lifecycles.md

---

# Object Relationships

Compliance Objects may establish Relationships with:

- other Compliance Objects;
- operational Objects;
- Policies;
- Contracts;
- Controls;
- Events.

Relationship semantics are defined separately.

---

# Object Evolution

Compliance Objects may evolve through:

- additional attributes;
- refined governance models;
- compatibility-preserving extensions.

Breaking semantic changes shall require explicit governance.

---

# Relationship to Other Specifications

Compliance Objects build upon:

- Object
- Identity
- Lifecycle
- Relationship
- Event
- Policy
- Contract
- Domain

Additional Compliance specifications define how these Objects interact.

---

# Independence

This specification does not prescribe:

- regulatory standards;
- compliance software;
- governance platforms;
- implementation technologies.

Compliance Objects remain logical enterprise entities independent of implementation.

---

# Conformance

A conforming Compliance implementation shall:

- define managed Compliance Objects;
- preserve Object Identity;
- preserve Object Ownership;
- support governed Lifecycles;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

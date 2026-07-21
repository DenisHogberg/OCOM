<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Compliance](README.md) / Compliance Relationships

[← Back](Compliance_Processes.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Compliance Relationships

**Document ID:** DOMAIN-COMPLIANCE-RELATIONSHIPS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Relationships managed by the Compliance Domain.

Compliance Relationships describe governed associations between Compliance Objects and other enterprise Objects while preserving Object Ownership, Lifecycle integrity, and interoperability across Domains.

Relationship semantics are defined independently of implementation technologies.

---

# Definition

A Compliance Relationship represents a governed business association involving one or more Compliance Objects.

Relationships establish business context without transferring Ownership or modifying the Lifecycle of participating Objects.

Relationship semantics are defined by the Core specification.

---

# Business Meaning

Compliance Relationships connect governance activities to the operational business Objects they evaluate.

They enable traceability between enterprise operations, compliance obligations, assessments, controls, evidence, audits, and remediation activities.

---

# Design Principles

Compliance Relationships shall:

- preserve Object Ownership;
- remain explicitly defined;
- support auditability;
- preserve traceability;
- remain technology independent;
- support cross-Domain interoperability.

---

# Relationship Categories

Compliance Relationships may be organized into the following categories.

## Obligation Relationships

Relationships connecting compliance obligations to governed business context.

Examples include:

- Obligation references Policy;
- Obligation references Regulation;
- Obligation applies to Contract;
- Obligation applies to Entity.

---

## Control Relationships

Relationships describing enterprise controls.

Examples include:

- Control evaluates Process;
- Control protects Capability;
- Control monitors Event;
- Control supports Policy.

---

## Assessment Relationships

Relationships connecting compliance assessments to enterprise Objects.

Examples include:

- Assessment evaluates Customer;
- Assessment evaluates Payment;
- Assessment evaluates Contract;
- Assessment evaluates Journal Entry;
- Assessment evaluates Process.

---

## Audit Relationships

Relationships supporting audit activities.

Examples include:

- Audit includes Assessment;
- Audit produces Finding;
- Audit references Evidence;
- Audit evaluates Control.

---

## Evidence Relationships

Relationships connecting evidence to governance activities.

Examples include:

- Evidence supports Assessment;
- Evidence supports Audit;
- Evidence supports Finding;
- Evidence references Event.

---

## Remediation Relationships

Relationships supporting corrective actions.

Examples include:

- Remediation resolves Finding;
- Remediation improves Control;
- Remediation addresses Assessment;
- Remediation satisfies Obligation.

---

## Cross-Domain Relationships

Compliance Objects may establish Relationships with Objects owned by other Domains.

Examples include:

- Assessment ↔ Customer
- Assessment ↔ Payment
- Assessment ↔ Account
- Assessment ↔ Contract
- Assessment ↔ Invoice
- Assessment ↔ Journal Entry
- Assessment ↔ Product
- Assessment ↔ Affiliate
- Finding ↔ Process
- Control ↔ Capability

Ownership remains with the originating Domain.

---

# Relationship Ownership

The Compliance Domain owns Relationships originating from Compliance Objects.

Ownership of referenced operational Objects shall remain unchanged.

---

# Relationship Lifecycle

Relationships may exist throughout all or part of the participating Object Lifecycles.

Relationship creation, modification, and retirement shall follow applicable Policies.

---

# Relationship Evolution

Compliance Relationships may evolve through:

- additional governed associations;
- refined business semantics;
- compatibility-preserving extensions.

Breaking semantic changes shall require explicit governance.

---

# Relationship to Other Specifications

Compliance Relationships build upon:

- Relationship
- Object
- Lifecycle
- Event
- Policy
- Contract
- Domain

Additional Compliance specifications define the Objects participating in these Relationships.

---

# Independence

This specification does not prescribe:

- database schemas;
- graph technologies;
- compliance software;
- implementation technologies.

Relationships remain logical business associations independent of implementation.

---

# Conformance

A conforming Compliance implementation shall:

- define governed Relationships;
- preserve Object Ownership;
- support Relationship traceability;
- maintain interoperability across Domains;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

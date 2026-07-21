<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Legal](README.md) / Legal Relationships

[← Back](Legal_Processes.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Legal Relationships

**Document ID:** DOMAIN-LEGAL-RELATIONSHIPS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Relationships owned by the Legal Domain.

Legal Relationships describe how legal Entities interact while preserving Object Ownership, Lifecycle integrity, governance, and enterprise interoperability.

Relationships represent governed legal associations rather than implementation-specific references.

---

# Definition

A Legal Relationship is a governed business association between two or more Entities.

Legal Relationships define contractual, regulatory, intellectual property, and legal governance connections.

Relationship semantics are defined by the Core Relationship specification.

---

# Business Meaning

Legal Relationships enable organizations to model contractual obligations, legal responsibilities, intellectual property rights, regulatory interactions, and legal governance consistently across the enterprise.

Relationships preserve legal meaning independently of legal software or document repositories.

---

# Design Principles

Legal Relationships shall:

- preserve Object Ownership;
- remain explicitly defined;
- support Lifecycle integrity;
- enable traceability;
- support enterprise interoperability;
- remain technology independent.

---

# Relationship Categories

Legal Relationships may be organized into the following categories.

---

## Contract Relationships

Relationships describing contractual structures.

Examples include:

- Contract references Agreement;
- Amendment modifies Contract;
- Statement of Work belongs to Contract;
- Contract references Counterparty;
- Contract governs Obligation.

Contracts may govern multiple Entities simultaneously.

---

## Obligation Relationships

Relationships describing legal commitments.

Examples include:

- Obligation belongs to Contract;
- Obligation references Payment;
- Obligation references Deliverable;
- Renewal Obligation extends Agreement;
- Service Obligation supports Customer Relationship.

Obligations remain independent Entities.

---

## Legal Entity Relationships

Relationships describing legal participants.

Examples include:

- Legal Entity owns Intellectual Property;
- Counterparty signs Contract;
- Subsidiary belongs to Legal Entity;
- Branch belongs to Legal Entity;
- Legal Entity participates in Litigation.

Legal Entity Relationships define legal identity rather than organizational hierarchy.

---

## Intellectual Property Relationships

Relationships describing ownership and licensing.

Examples include:

- Intellectual Property belongs to Legal Entity;
- License authorizes Product;
- Trademark protects Brand;
- Patent protects Technology;
- Copyright protects Creative Asset.

Intellectual Property Relationships preserve ownership independently of operational usage.

---

## Legal Matter Relationships

Relationships describing legal work.

Examples include:

- Legal Review evaluates Contract;
- Legal Opinion supports Legal Matter;
- Approval Record approves Agreement;
- Legal Advice references Legal Matter;
- Legal Matter references Regulatory Filing.

Legal Matters coordinate legal governance.

---

## Dispute Relationships

Relationships describing legal disputes.

Examples include:

- Claim references Contract;
- Dispute references Counterparty;
- Litigation references Legal Entity;
- Settlement resolves Claim;
- Arbitration references Agreement.

Dispute Relationships preserve legal history.

---

## Regulatory Relationships

Relationships describing regulatory governance.

Examples include:

- Regulatory Filing references Legal Entity;
- Legal Risk Assessment evaluates Contract;
- Regulatory Approval supports Product;
- Legal Notice references Obligation;
- Compliance Interpretation references Regulation.

Regulatory Relationships support enterprise governance.

---

# Cross-Domain Relationships

Legal Objects may reference Entities owned by other Domains.

Examples include:

- Contract references Customer;
- Employment Agreement references Employee;
- Partnership Agreement references Affiliate;
- License authorizes Product;
- Payment Obligation references Payment;
- Financial Obligation references Financial Record;
- Legal Review references Compliance Assessment.

Cross-Domain Relationships do not transfer Object Ownership.

---

# Relationship Ownership

Each Legal Relationship shall have one owning Domain.

The Legal Domain owns Relationships describing legal governance and contractual meaning.

Other Domains may reference Legal Relationships without assuming Ownership.

---

# Relationship Governance

Legal Relationships shall be governed through:

- Policies;
- Lifecycles;
- Constraints;
- legal governance;
- audit requirements.

Governance shall preserve legal consistency across the enterprise.

---

# Relationship Evolution

Legal Relationships may evolve through:

- additional Relationship types;
- refined legal semantics;
- expanded governance models;
- compatibility-preserving enhancements.

Historical meaning shall remain preserved.

---

# Relationship to Other Specifications

Legal Relationships build upon:

- Relationship
- Object
- Lifecycle
- Policy
- Domain Governance

Additional Legal specifications define how Relationships participate in Processes and Events.

---

# Independence

This specification does not prescribe:

- contract repositories;
- legal software;
- document management systems;
- electronic signature platforms;
- implementation technologies.

Legal Relationships remain implementation independent.

---

# Conformance

A conforming Legal implementation shall:

- define standardized Legal Relationships;
- preserve Object Ownership;
- preserve Relationship integrity;
- support enterprise interoperability;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

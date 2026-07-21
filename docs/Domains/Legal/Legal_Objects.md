<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Legal](README.md) / Legal Objects

[← Back](Legal_Lifecycles.md) · [↑ Up](README.md) · [Next →](Legal_Policies.md)

---
<!-- nav:end -->

# Legal Objects

**Document ID:** DOMAIN-LEGAL-OBJECTS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Entities owned by the Legal Domain.

Legal Objects represent the enterprise legal model, including contracts, agreements, obligations, legal entities, intellectual property, legal matters, and governance while preserving Object Ownership, Lifecycle integrity, and enterprise interoperability.

---

# Definition

A Legal Object is an Entity owned by the Legal Domain.

Legal Objects describe legal relationships and obligations independently of implementation technologies.

Object semantics are defined by the Core Object specification.

---

# Business Meaning

Legal Objects provide the authoritative representation of enterprise legal knowledge.

They enable organizations to consistently govern legal relationships, contractual commitments, intellectual property, regulatory filings, and legal risks.

---

# Design Principles

Legal Objects shall:

- possess unique business identity;
- own their Lifecycle;
- preserve semantic consistency;
- participate in governed Relationships;
- generate Legal Events;
- remain technology independent.

---

# Object Categories

Legal Objects may be organized into the following categories.

---

## Contract Objects

Objects representing contractual relationships.

Examples include:

- Contract;
- Agreement;
- Amendment;
- Master Agreement;
- Statement of Work;
- Contract Version.

Contract Objects define legal commitments independently of stored documents.

---

## Obligation Objects

Objects representing legally enforceable commitments.

Examples include:

- Obligation;
- Commitment;
- Deliverable;
- Service Obligation;
- Payment Obligation;
- Renewal Obligation.

Obligations exist independently from operational execution.

---

## Legal Entity Objects

Objects representing legal participants.

Examples include:

- Legal Entity;
- Counterparty;
- Subsidiary;
- Branch;
- Corporate Registration Reference.

Legal Entity Objects represent legal identity rather than operational organization.

---

## Intellectual Property Objects

Objects representing protected intellectual assets.

Examples include:

- Intellectual Property Asset;
- Trademark;
- Copyright;
- Patent;
- Trade Secret;
- License.

Intellectual Property Objects preserve ownership independently of Products.

---

## Legal Matter Objects

Objects representing legal activities.

Examples include:

- Legal Matter;
- Legal Review;
- Legal Opinion;
- Legal Advice Reference;
- Approval Record.

Legal Matters coordinate legal work without replacing Contracts.

---

## Dispute Objects

Objects representing legal disputes.

Examples include:

- Claim;
- Dispute;
- Litigation Case;
- Arbitration Case;
- Settlement Agreement.

Dispute Objects preserve legal history.

---

## Regulatory Objects

Objects supporting regulatory governance.

Examples include:

- Regulatory Filing Reference;
- Legal Risk Assessment;
- Regulatory Approval Reference;
- Legal Notice;
- Compliance Interpretation Reference.

Regulatory Objects support enterprise legal governance.

---

# Cross-Domain References

Legal Objects may reference Entities owned by other Domains.

Examples include:

- Contract references Product;
- Contract references Customer;
- Employment Agreement references Employee;
- Affiliate Agreement references Partner;
- Payment Obligation references Payment;
- Financial Obligation references Financial Record;
- Legal Review references Compliance Assessment.

Such references do not transfer Object Ownership.

---

# Object Ownership

Every Legal Object shall have one owning Domain.

The Legal Domain owns:

- Contracts;
- Agreements;
- Obligations;
- Legal Entities;
- Intellectual Property;
- Legal Matters;
- Disputes;
- Regulatory Legal Objects.

Other Domains may reference Legal Objects but shall not own them.

---

# Object Governance

Legal Objects shall be governed through:

- Lifecycles;
- Relationships;
- Policies;
- Constraints;
- Events.

Governance shall ensure enterprise legal consistency.

---

# Object Evolution

Legal Objects may evolve through:

- additional attributes;
- refined legal semantics;
- expanded governance models;
- compatibility-preserving enhancements.

Historical identity shall be preserved.

---

# Relationship to Other Specifications

Legal Objects build upon:

- Object
- Relationship
- Lifecycle
- Event
- Policy
- Domain

Additional Legal specifications define how these Objects interact.

---

# Independence

This specification does not prescribe:

- contract repositories;
- document management systems;
- legal software;
- electronic signature platforms;
- implementation technologies.

Legal Objects remain implementation independent.

---

# Conformance

A conforming Legal implementation shall:

- define standardized Legal Objects;
- preserve Object identity;
- preserve Object Ownership;
- support enterprise interoperability;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

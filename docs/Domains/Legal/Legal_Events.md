<!-- nav:start -->
[Docs](../../README.md) / [Domains](../README.md) / [Legal](README.md) / Legal Events

[← Back](Legal_Capabilities.md) · [↑ Up](README.md) · [Next →](Legal_KPIs.md)

---
<!-- nav:end -->

# Legal Events

**Document ID:** DOMAIN-LEGAL-EVENTS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 21 July 2026

---

# Purpose

This document defines the Events owned by the Legal Domain.

Legal Events communicate completed business facts describing changes to Legal Entities while preserving Object Ownership, Lifecycle integrity, governance, and enterprise interoperability.

Events provide an immutable record of enterprise legal activities.

---

# Definition

A Legal Event is an immutable business fact representing a completed change affecting one or more Legal Entities.

Legal Events communicate completed legal activities rather than commands, requests, or intentions.

Event semantics are defined by the Core Event specification.

---

# Business Meaning

Legal Events synchronize enterprise legal knowledge by communicating changes to Contracts, Agreements, Obligations, Legal Entities, Intellectual Property, Legal Matters, Claims, and Regulatory Objects.

They enable consistent legal governance without duplicating ownership of Legal Entities.

---

# Design Principles

Legal Events shall:

- represent completed business facts;
- remain immutable;
- preserve Object Ownership;
- support traceability;
- enable auditability;
- remain technology independent.

---

# Event Categories

Legal Events may be organized into the following categories.

---

## Contract Events

Events describing contractual lifecycle changes.

Examples include:

- Contract Created;
- Contract Reviewed;
- Contract Approved;
- Contract Executed;
- Contract Amended;
- Contract Renewed;
- Contract Terminated;
- Contract Archived.

---

## Obligation Events

Events describing legal obligations.

Examples include:

- Obligation Created;
- Obligation Assigned;
- Obligation Fulfilled;
- Obligation Violated;
- Obligation Waived;
- Obligation Closed.

---

## Legal Entity Events

Events describing legal entities.

Examples include:

- Legal Entity Registered;
- Legal Entity Updated;
- Subsidiary Established;
- Branch Registered;
- Legal Entity Dissolved.

---

## Intellectual Property Events

Events describing intellectual property.

Examples include:

- Intellectual Property Registered;
- Trademark Granted;
- Patent Granted;
- License Issued;
- License Renewed;
- License Revoked.

---

## Legal Matter Events

Events describing legal activities.

Examples include:

- Legal Review Started;
- Legal Review Completed;
- Legal Opinion Issued;
- Approval Granted;
- Legal Matter Closed.

---

## Dispute Events

Events describing disputes.

Examples include:

- Claim Filed;
- Dispute Opened;
- Arbitration Initiated;
- Litigation Started;
- Settlement Reached;
- Dispute Closed.

---

## Regulatory Events

Events describing regulatory legal activities.

Examples include:

- Regulatory Filing Submitted;
- Regulatory Approval Received;
- Legal Notice Issued;
- Legal Risk Evaluated;
- Regulatory Response Completed.

---

# Event Ownership

Every Legal Event shall have one originating Domain.

The Legal Domain owns Events describing changes to Legal Entities.

Other Domains may consume Legal Events without assuming ownership of Legal Objects.

---

# Event Characteristics

Legal Events shall:

- reference affected Entities;
- preserve Event identity;
- record occurrence time;
- remain immutable;
- support enterprise traceability.

Organizations may enrich Events with implementation-specific metadata.

---

# Event Governance

Legal Events shall be governed through:

- Ownership;
- Policies;
- Lifecycle compatibility;
- version management;
- audit requirements.

Governance shall ensure reliable enterprise legal communication.

---

# Event Evolution

Legal Events may evolve through:

- additional Event types;
- refined legal semantics;
- compatibility-preserving enhancements.

Published Events shall preserve historical meaning.

---

# Relationship to Other Specifications

Legal Events build upon:

- Event
- Object
- Lifecycle
- Relationship
- Policy
- Domain Governance

Additional Legal specifications define which Events are emitted by individual Processes and Capabilities.

---

# Independence

This specification does not prescribe:

- contract management software;
- legal workflow systems;
- document repositories;
- electronic signature platforms;
- implementation technologies.

Legal Events remain logical business facts independent of implementation.

---

# Conformance

A conforming Legal implementation shall:

- define standardized Legal Events;
- preserve Event immutability;
- preserve Object Ownership;
- support enterprise interoperability;
- remain compatible with the OCOM Specification.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 21 July 2026 | Initial draft |

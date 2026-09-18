<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Layered Memory

[← Back](Evidence%20Overlay.md) · [↑ Up](README.md) · [Next →](Memory%20Record.md)

---
<!-- nav:end -->

# Layered Memory

**Document ID:** Memory-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 18 September 2026

---

# Purpose

This document defines the layered memory architecture within the OCOM Memory Specification.

Different kinds of information have different operational value, persistence, and governance requirements.

Layered Memory classifies memory according to its operational lifetime and business significance.

---

# Definition

Layered Memory is a hierarchical memory model that separates operational knowledge into multiple persistence levels.

Each layer has distinct retention, governance, and write-back characteristics.

---

# Design Principles

Layered Memory shall:

- separate temporary and persistent knowledge;
- minimize unnecessary persistence;
- preserve organizational knowledge;
- support explainable AI;
- support governed write-back.

---

# Memory Layers

The OCOM Specification defines four standard memory layers.

## Transient Memory

Transient Memory exists only during execution.

Characteristics:

- task-scoped;
- non-persistent;
- automatically discarded;
- isolated.

Typical examples:

- prompt context;
- intermediate reasoning;
- temporary calculations;
- execution variables.

---

## Stage Memory

Stage Memory survives multiple execution steps within the same business activity.

Characteristics:

- workflow-scoped;
- temporary;
- shared between AI Agents;
- automatically expires.

Typical examples:

- onboarding process;
- fraud investigation;
- customer support conversation;
- approval workflow.

---

## Long-Term Memory

Long-Term Memory stores reusable operational knowledge.

Characteristics:

- persistent;
- versioned;
- evidence-backed;
- reusable.

Typical examples:

- customer preferences;
- supplier history;
- operational knowledge;
- business patterns.

---

## Persistent Memory

Persistent Memory represents authoritative organizational information.

Characteristics:

- governed;
- auditable;
- organization-owned;
- externally managed.

Typical examples:

- CRM
- ERP
- HR
- Finance
- Compliance

Persistent Memory is considered the system of record.

---

# Memory Flow

Typical information progression follows this path:

Transient

↓

Stage

↓

Long-Term

↓

Persistent

Promotion between layers shall follow organizational governance policies.

---

# Layer Promotion

Information shall not automatically move to a higher layer.

Promotion should consider:

- confidence;
- evidence;
- business value;
- approval requirements.

---

# Layer Demotion

Memory may move to a lower layer when:

- confidence decreases;
- evidence becomes invalid;
- retention expires;
- business rules require removal.

> **Editorial note (18 September 2026).** This section and Layer Promotion above describe a layer change as movement of an existing record, while Constitution §4 makes a Memory Entry immutable after creation. Whether a layer is an attribute of a record or a projection computed from the append-only sequence is the question `CAND-014` answered for Status and left open here. It is recorded as `AO-069`, together with the same question for `Memory/Retention.md`. This note changes no requirement.

---

# Relationship to Other Memory Components

Every memory layer may use:

- Evidence Overlay
- Confidence Model
- Write-back Governance
- Retention Policies

---

# Conformance

A compliant implementation shall:

- support all defined memory layers;
- preserve separation between layers;
- enforce promotion rules;
- preserve provenance across layers.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 18 September 2026 | Editorial note added under Layer Demotion recording that a layer change is described as movement of an existing record while Constitution §4 makes a Memory Entry immutable, per `AO-069`; no requirement changed. |

<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Retention

[← Back](Overview.md) · [↑ Up](README.md) · [Next →](Write-back%20Governance.md)

---
<!-- nav:end -->

# Retention

**Document ID:** Memory-06

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the retention model for Memory Records within the OCOM Memory Specification.

Retention determines how long Memory Records remain active, when they expire, when they are archived, and when they may be permanently removed.

---

# Definition

Retention is the set of policies governing the lifetime of Memory Records.

Retention ensures that operational memory remains relevant, accurate, and compliant with organizational and regulatory requirements.

---

# Design Principles

Retention shall:

- preserve valuable organizational knowledge;
- remove obsolete information;
- support regulatory compliance;
- support operational efficiency;
- preserve auditability;
- remain technology independent.

---

# Retention Policy

Every Memory Record shall define a retention policy.

The policy may be determined by:

- memory layer;
- memory type;
- business domain;
- regulatory requirements;
- organizational governance.

---

# Retention States

A Memory Record may exist in one of the following retention states:

## Active

The record is available for operational use.

---

## Expiring

The record is approaching the end of its retention period.

The organization may review, extend, or archive the record.

---

## Expired

The record is no longer considered operationally valid.

Expired records shall not be used for operational decision-making unless explicitly permitted.

---

## Archived

The record is retained for historical, analytical, or regulatory purposes.

Archived records remain accessible but are excluded from normal operational workflows.

---

## Deleted

The record has been permanently removed in accordance with organizational or regulatory policy.

Deletion shall be auditable.

---

# Retention Triggers

Retention actions may be triggered by:

- elapsed time;
- business events;
- lifecycle completion;
- legal requirements;
- manual review;
- governance policies.

---

# Retention Extension

Retention periods may be extended when:

- new evidence is received;
- business value increases;
- regulatory obligations require preservation;
- human reviewers approve the extension.

---

# Relationship to Memory Layers

Different memory layers may define different default retention policies.

Examples:

| Memory Layer | Typical Retention |
|---------------|------------------|
| Transient | Minutes or task duration |
| Stage | Days or workflow duration |
| Long-Term | Months or years |
| Persistent | Organization-defined |

Retention periods are implementation-specific.

---

# Relationship to Governance

Retention policies shall be compatible with:

- Write-back Governance;
- Evidence Overlay;
- Confidence Model;
- Memory Lifecycle.

---

# Auditability

Retention operations shall record:

- action;
- actor;
- timestamp;
- reason;
- affected Memory Record;
- resulting state.

Retention history shall remain auditable.

---

# Independence

The Retention specification does not prescribe:

- storage technologies;
- archive systems;
- deletion mechanisms;
- backup strategies.

Organizations remain free to implement retention using any compatible technology.

---

# Conformance

A compliant implementation shall:

- define retention policies for Memory Records;
- support retention state transitions;
- preserve audit history;
- support archival;
- support controlled deletion.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

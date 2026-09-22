<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Retention

[← Back](Overview.md) · [↑ Up](README.md) · [Next →](Write-back%20Governance.md)

---
<!-- nav:end -->

# Retention

**Document ID:** Memory-06

**Status:** Draft

**Version:** 0.1

**Last Updated:** 22 September 2026

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

A Memory Record is never altered. Where law or organizational policy requires that retained content no longer be recoverable, an implementation shall make the content of the affected record irrecoverable while preserving the record's identity, its creation time and creator, and its demonstration of integrity, and shall record the erasure as a new Memory Record naming what was erased and under which policy.

Deleted means this and nothing else. Reconstructability, Constitution Principle 6, holds for everything except the erased content, which is the purpose of the erasure.

The preserved demonstration shows what the record's content was at creation. A party holding the erased record learns from it that the content has been erased, not that it is intact; a conformance test that verifies demonstrations excludes a record named by an erasure record rather than failing it.

An erasure record shall name a Policy the organization has declared and the actor who issued it. An implementation shall refuse an erasure record that names neither, so that the exclusion an erasure record grants is granted only by a record that can itself be checked.

Deletion shall be auditable.

> **Resolution note (21 September 2026).** The editorial note of 18 September 2026 recorded that this state, and the Conformance clause "support controlled deletion", stood against Constitution Principles 4 and 6 (`AO-069`). `CAND-024` (Decided 21 September 2026) restates the state as an erasure that preserves the record and is itself recorded, so it no longer stands against either Principle. `AO-069` closes.

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
- support erasure as the Deleted state defines it, preserving the record's identity, creation time, creator and demonstration of integrity, and recording the erasure as a new Memory Record.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.1 | 18 September 2026 | Editorial note added under Deleted recording that this document's Deleted state and its controlled-deletion Conformance clause stand against Constitution §4 and §6, per `AO-069`; no requirement changed. |
| 0.1 | 21 September 2026 | Deleted restated as an erasure that makes content irrecoverable while preserving the record's identity, creation time, creator and demonstration of integrity, recorded as a new Memory Record; the Conformance item "support controlled deletion" replaced accordingly, per `CAND-024` (Decided 21 September 2026). The editorial note of 18 September is replaced by a resolution note. `AO-069` closes. |
| 0.1 | 21 September 2026 | Deleted: one sentence added stating what the preserved demonstration means after erasure (it shows the content at creation; a holder learns the record was erased), found by running the Integrity Test kind against an erased record; recorded as a postscript to `CAND-024`. |
| 0.1 | 22 September 2026 | Deleted: two sentences added requiring an erasure record to name a declared Policy and the actor who issued it, and an implementation to refuse one that names neither; the closure `AO-085` proposed, adopted as a postscript to `CAND-024` (22 September 2026). |

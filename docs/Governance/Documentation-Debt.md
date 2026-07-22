<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Documentation Debt

[← Back](Development-Readiness.md) · [↑ Up](README.md) · [Next →](Documentation-Standards.md)

---
<!-- nav:end -->

# Documentation Debt

**Document ID:** GOV-DEBT-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document is the central register of open documentation-related items across the OCOM Specification.

It is maintained by the CDKO. Entries are never deleted — only their Status changes over time, preserving history.

Entries are split into four categories to separate real problems from consciously deferred decisions:

- **Documentation Debt** — actual problems: inaccuracies, inconsistencies, outdated content.
- **Documentation Gaps** — missing coverage that has not been the subject of any decision.
- **Architecture Observations** — pointers into `Architecture-Observations.md`; not duplicated here.
- **Future Work** — consciously deferred author/architect decisions. Not debt.

---

# Documentation Debt

| ID | Description | Severity | Affected Documents | Recommendation | Status |
|---|---|---|---|---|---|
| DEBT-DOC-001 | Historical descriptive content of docs/README.md was lost during a previous automated regeneration | Medium | `docs/README.md` | Restore descriptive content in a dedicated Documentation Task | Open |

---

# Documentation Gaps

| ID | Description | Severity | Affected Documents | Recommendation | Status |
|---|---|---|---|---|---|
| GAP-001 | Four competing filename conventions coexist across the specification (Title Case With Spaces, snake_case/UPPER-suffix, PascalCase, kebab-case) | Low | ~237 content files across the specification | Agree on a single convention for a future version; do not rename files without a separate approved proposal | Open |
| GAP-002 | `Core/Terminology.md` does not define Object, Capability, Policy, Contract, Context, Knowledge, or Memory, although each has its own normative document elsewhere | Medium | `Core/Terminology.md` | Extend the glossary to cover all Meta-level concepts | Open |

---

# Architecture Observations

Summary pointers only. Full entries, Impact, and Architect Response live in `Architecture-Observations.md`.

| ID | Summary | Status | Reference |
|---|---|---|---|
| OBS-001 | `AI/Context/Overview.md` and `AI/Agents/Context.md` are content-identical | Open | Architecture-Observations.md#obs-001 |
| OBS-002 | Reference Architecture layer name retains "Business Object Architecture" while internal section headers use "Entity" | Closed | Architecture-Observations.md#obs-002 |

---

# Future Work

Consciously deferred decisions. Not documentation debt.

| ID | Description | Target Version | Affected Documents | Source of Decision | Status |
|---|---|---|---|---|---|
| FW-001 | `Evidence Overlay`: Definition, Independence, Conformance sections and the Source/Reliability attributes were intentionally removed during the v0.1 release candidate review | Undetermined | `Memory/Evidence Overlay.md` | Author RC decision, 21 July 2026 | Planned |
| FW-002 | `Campaign.md`: Business Rules section was intentionally removed during the v0.1 release candidate review, without replacement | Undetermined | `Entities/Campaign/Campaign.md` | Author RC decision, 21 July 2026 | Planned |
| FW-003 | Reference Agent does not exist anywhere in the repository — the final link of the traceability chain | Next stage of OCOM | Repository-wide | CDKO role charter, "Дополнительная задача" | Planned |
| FW-004 | Reference Implementation does not exist anywhere in the repository | Next stage of OCOM | Repository-wide | CDKO role charter, "Дополнительная задача" | Planned |
| FW-005 | Extend `Knowledge-Map.md` traceability and `docs/README.md` visibility to fully reflect Governance as a peer section of OCOM | Undetermined | `Governance/Knowledge-Map.md`, `docs/README.md` | CDKO proposal, pending Architect confirmation | Open |

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial register, populated from Documentation Health Report v0.1 |
| 0.1 | 22 July 2026 | Added DEBT-DOC-001 (docs/README.md descriptive content regression) |

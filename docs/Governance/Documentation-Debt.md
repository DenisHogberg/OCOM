<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Documentation Debt

[← Back](Development-Readiness.md) · [↑ Up](README.md) · [Next →](Documentation-Standards.md)

---
<!-- nav:end -->

# Documentation Debt

**Document ID:** GOV-DEBT-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 16 September 2026

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
| DEBT-DOC-001 | Historical descriptive content of docs/README.md was lost during a previous automated regeneration | Medium | `docs/README.md` | Restore descriptive content in a dedicated Documentation Task | Open; not required for v1.0, disposition 16 September 2026: `docs/README.md` carries a description per section and an entry paragraph naming the Constitution; the lost prose is not restored |

---

# Documentation Gaps

| ID | Description | Severity | Affected Documents | Recommendation | Status |
|---|---|---|---|---|---|
| GAP-001 | Four competing filename conventions coexist across the specification (Title Case With Spaces, snake_case/UPPER-suffix, PascalCase, kebab-case) | Low | ~237 content files across the specification | Agree on a single convention for a future version; do not rename files without a separate approved proposal | Open; not required for v1.0, disposition 16 September 2026 per `Master-Architecture-Backlog.md` Part 8 |
| GAP-002 | `Core/Terminology.md` does not define Object, Capability, Policy, Contract, Context, Knowledge, or Memory, although each has its own normative document elsewhere | Medium | `Core/Terminology.md` | Extend the glossary to cover all Meta-level concepts. Closed 16 September 2026: `Core/Terminology.md` restated as a verbatim index and extended, per `AO-066`. | Closed |
| GAP-003 | Author referenced "M020 — Public Product Release" (23 July 2026) as a prior Milestone. No definition, criteria, or scope for M020 exists anywhere in the repository, its full commit history, or any Governance document. | Low | Milestone numbering generally; `ROADMAP.md` | Author decision. | Closed |
| GAP-004 | `Core/Constitution.md` paragraph 4 names the retained-fact concept Memory Entry while the Memory tier's document is titled Memory Record; `Constitution-Step0-Summary.md` Decision 1 ruled them one concept with Memory Entry canonical, and the rename was never executed | Low | `Memory/Memory Record.md`, `Core/Constitution.md` | Execute the rename through the change process; a terminology note was added to `Memory Record.md` on 5 September 2026 | Open |
| GAP-005 | The Compliance Domain is the only profile without a Lifecycles document, although `Compliance_Objects.md` carried a shall-clause pointing at one and `Compliance/Overview.md` claims the Domain defines its Lifecycles | Medium | `Domains/Compliance/` | Either write the profile's Lifecycles document or keep the Models-tier reference added on 5 September 2026 | Open |
| GAP-006 | Process and KPI are used normatively across the Domain tier with no definition at the Core, Meta, Models or Language tiers; eleven Process pointers and seven KPI pointers named specifications that do not exist and were retargeted on 5 September 2026 | Medium | `Domains/*/*_Processes.md`, `Domains/*/*_KPIs.md`, `Domains/Common/Domain Architecture.md` | Resolve through `AO-037` and `AO-038` | Open |
| GAP-007 | Documents carrying no Revision History table, and some no Last Updated field, against this register's own standard (`Documentation-Standards.md`). Recorded 16 September 2026 as sixteen documents and corrected the same day to ten; both counts came from a check that matched English headings only, so the Russian projection of the implementation case was listed twice over as missing a table it carries under `История ревизий`. Closed 17 September 2026: the five `Adoption/` documents and `Reference Architecture/Overview.md` gained a Revision History and a Last Updated field; the Russian case carries both and its `Обновлено` field was aligned with its own last row. Three documents remain outside the rule by decision, not by omission: `Specification/Committee Review Package.md`, the record of the 22 July 2026 review, which keeps its fields as reviewed, and the two Conformance Test Suite artifacts covered by the generated and append-only convention `Documentation-Standards.md` records. A step in the publication-metadata job now checks the rule, accepting the Russian labels, and names those three. | Low | `Adoption/*.md`, `Reference Architecture/Overview.md`, `Examples/Implementation-Case/Performance-Marketing-Operator-RU.md` | Done 17 September 2026 | Closed |

---

# Architecture Observations

Summary pointers only. Full entries, Impact, and Architect Response live in `Architecture-Observations.md`.

| ID | Summary | Status | Reference |
|---|---|---|---|
| OBS-001 | `AI/Context/Overview.md` and `AI/Agents/Context.md` are content-identical. Closed 16 September 2026: `CAND-001` decided, `AI/Agents/Context.md` replaced with an Informative pointer. | Closed | Architecture-Observations.md#obs-001 |
| OBS-002 | Reference Architecture layer name retains "Business Object Architecture" while internal section headers use "Entity" | Closed | Architecture-Observations.md#obs-002 |
| OBS-003 | Reference Case: proposed Object attribute lifecycle categories (structural/type-level/evolving/derived) — not adopted, insufficient independent corroboration | Open | Architecture-Observations.md#obs-003 |

---

# Future Work

Consciously deferred decisions. Not documentation debt.

| ID | Description | Target Version | Affected Documents | Source of Decision | Status |
|---|---|---|---|---|---|
| FW-001 | `Evidence Overlay`: Definition, Independence, Conformance sections and the Source/Reliability attributes were intentionally removed during the v0.1 release candidate review | Undetermined | `Memory/Evidence Overlay.md` | Author RC decision, 21 July 2026 | Planned; not required for v1.0, disposition 16 September 2026: written only as Layer 2 of `CAND-014` needs it (`Master-Architecture-Backlog.md` EPIC-A) |
| FW-002 | `Campaign.md`: Business Rules section was intentionally removed during the v0.1 release candidate review, without replacement | Undetermined | `Entities/Campaign/Campaign.md` | Author RC decision, 21 July 2026 | Planned; not required for v1.0, disposition 16 September 2026: the author decision stands and `Campaign.md` carries no Business Rules section by decision |
| FW-003 | Reference Agent does not exist anywhere in the repository — the final link of the traceability chain | Next stage of OCOM | Repository-wide | CDKO role charter, "Дополнительная задача" | Planned |
| FW-004 | Reference Implementation does not exist anywhere in the repository | Next stage of OCOM | Repository-wide | CDKO role charter, "Дополнительная задача" | Planned |
| FW-005 | Extend `Knowledge-Map.md` traceability and `docs/README.md` visibility to fully reflect Governance as a peer section of OCOM | Undetermined | `Governance/Knowledge-Map.md`, `docs/README.md` | CDKO proposal, pending Architect confirmation | Open; not required for v1.0, disposition 16 September 2026: `docs/README.md` lists Governance among the sections and `Knowledge-Map.md` shows it as a cross-cutting layer; further extension deferred |
| FW-006 | The external Publication Engine that builds ocom.uno exposes no commit or version marker this repository can check its output against — `Publication-Model.md`'s six authoritative-version questions can be answered from inside this repository, but "does the live site match the repository" cannot be verified without cooperation from that external system | Undetermined | `Governance/Publication-Model.md`, `Governance/Release-Workflow.md` (Steps 8–9) | Publication Governance work, 20 August 2026 | Open; narrowed 18 September 2026: the Specification projection names the commit it was compiled from, and `tools/site/publication_health.py` recomputes the site's Observatory records from the published site, so the site's self-checks are reproducible; the engine still exposes no build marker of its own |
| FW-007 | A correctly-scoped next Release (containing Constitution v1.0, matching `CAND-007`'s Architecture Freeze) has not been cut — `Publication-Manifest.md`'s placeholder entry is structural only, all fields `TBD` | Next release, criteria TBD | `Governance/Publication-Manifest.md`, `Governance/Master-Architecture-Backlog.md` Part 8 (Release Readiness) | Publication Governance work, 20 August 2026 — explicitly deferred, not this plan's scope. Discharged by Release `v1.1.1` (12 September 2026: Constitution 1.0.1, Manifest entry recorded before tagging, annotated tag, Zenodo version DOI `10.5281/zenodo.22724309`). | Closed |
| FW-008 | World Model (`Core/Constitution.md` paragraphs 5, 6 and 8) and Autonomy level (paragraphs 7 and 14) are named in the Constitution and defined in no document; `Workflows/` holds ten planned workflow stubs with no content | Undetermined | `Core/Constitution.md`, `Workflows/` | Tracked as `Master-Architecture-Backlog.md` EPIC-A (Concept Paper written; an ADR Candidate is the Definition of Done) and EPIC-D; named as open exceptions in `ADR-Candidates.md` CAND-007 §1; pointer row added 5 September 2026 so that the three registers name the gap | Open |
| FW-009 | `Payment.md` carries no Business Rules section, one of the nineteen sections `Entities/Overview.md` requires, and unlike `Campaign.md` (FW-002) no decision records the omission; both documents fail the Conformance clause of their own Overview | Undetermined | `Entities/Payment/Payment.md`, `Entities/Overview.md` | Dogfooding audit of Release v1.2.0, 16 September 2026 | Open; not required for v1.0 (same class as FW-002); either write the section or record the omission as a decision |

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial register, populated from Documentation Health Report v0.1 |
| 0.1 | 22 July 2026 | Added DEBT-DOC-001 (docs/README.md descriptive content regression) |
| 0.1 | 22 July 2026 | Added pointer to OBS-003 (Reference Case: Object attribute lifecycle categories) |
| 0.1 | 23 July 2026 | Added GAP-003 (M020 does not exist; Milestone numbering begins at M021), recorded Closed per author decision |
| 0.1 | 20 August 2026 | Added FW-006 (external Publication Engine exposes no commit/version marker) and FW-007 (next correctly-scoped Release not yet cut), per `Governance/Publication-Model.md` and `Governance/Publication-Manifest.md` |
| 0.1 | 5 September 2026 | Added GAP-004 (Memory Entry / Memory Record rename pending) and FW-008 (World Model, Autonomy level and the Workflows/ stubs), so that gaps tracked only in the Backlog and CAND-007 are visible from this register. |
| 0.1 | 5 September 2026 | Added GAP-005 (no Compliance Lifecycles document) and GAP-006 (Process and KPI undefined above the Domain tier), both surfaced by a full read of the Domains, Entities, AI and Reference Architecture tiers. |
| 0.1 | 12 September 2026 | FW-007 closed: Release `v1.1.1` cut per `Governance/Release-Workflow.md` (Manifest entry before tagging, annotated tag) with Zenodo version DOI `10.5281/zenodo.22724309`; the same-day `v1.1.0` is recorded as Superseded in `Governance/Publication-Manifest.md`. |
| 0.1 | 16 September 2026 | GAP-002 closed: `Core/Terminology.md` now indexes every Meta-level concept and every Constitution term, restating each owning document's Definition verbatim; the Constitution terms no document defines are listed as Reserved (`AO-066`, `AO-067`, `AO-068`). |
| 0.1 | 16 September 2026 | OBS-001 closed per `CAND-001` (Decided 16 September 2026): `AI/Agents/Context.md` replaced with an Informative pointer to `AI/Context/Overview.md`. |
| 0.1 | 16 September 2026 | DEBT-DOC-001, GAP-001, FW-002 and FW-005 each carry a not-required-for-v1.0 disposition, per `Master-Architecture-Backlog.md` Part 8 (EPIC-F). Statuses otherwise unchanged. |
| 0.1 | 16 September 2026 | FW-001 carries a not-required-for-v1.0 disposition per the EPIC-A disposition of the same day. |
| 0.1 | 16 September 2026 | Added GAP-007 (sixteen documents without a Revision History table) and FW-009 (`Payment.md` without a Business Rules section, unrecorded until now), both from the dogfooding audit of Release v1.2.0. |
| 0.1 | 17 September 2026 | GAP-007 recounted and corrected after the v1.0 recompilation closed it for the nine chapters: ten documents, not sixteen; the Russian implementation case added, the two Conformance Test Suite artifacts listed as covered by their own convention. |
| 0.1 | 17 September 2026 | GAP-007 closed: the six documents that lacked a Revision History gained one, the Russian case was never missing anything (the check had matched English headings only), and the three documents that stay outside the rule do so by recorded decision. A CI step now enforces it. |
| 0.1 | 18 September 2026 | FW-006 narrowed: the site's Observatory records are recomputable from this repository and the Specification projection names its source commit; the gap itself stays open. |

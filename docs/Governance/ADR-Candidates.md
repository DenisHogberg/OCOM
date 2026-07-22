<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / ADR Candidates

[↑ Up](README.md) · [Next →](Architecture-Health.md)

---
<!-- nav:end -->

# ADR Candidates

**Document ID:** GOV-ADR-CANDIDATES-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document is a queue of questions that require a decision from the Chief Architect.

The CDKO does not create Architecture Decision Records. The CDKO proposes candidates. The Chief Architect reviews them and records a Decision. If the Decision is "Promote to ADR," the Chief Architect authors the actual ADR outside this document.

Every candidate uses the same template, so every candidate follows the same lifecycle regardless of where it originated:

| Field | Meaning |
|---|---|
| **ID** | Candidate identifier. |
| **Title** | Short name of the question to be decided. |
| **Status** | `Open` — queued, no decision yet. `Promoted to ADR-<ID>` / `Rejected` / `Merged` / `Closed without ADR` — per the Governance Proposal v1.1 decision set. |
| **Owner** | Who currently needs to act — the Chief Architect while `Open`. |
| **Created** | Date the candidate was queued. |
| **Related Documents** | Source Observation, specification chapters, or other documents involved. |
| **Discussion** | The question, why it cannot be resolved editorially, and the consequences of each plausible outcome. |
| **Next Action** | What has to happen for Status to change. |

---

## CAND-001

**Title:** Content duplication between `AI/Agents/Context.md` and `AI/Context/Overview.md`

**Status:** Open

**Owner:** Chief Architect

**Created:** 21 July 2026

**Related Documents:** `Architecture-Observations.md#obs-001`, `AI/Agents/Context.md`, `AI/Context/Overview.md`

**Discussion:** Should `AI/Agents/Context.md` remain a full duplicate of `AI/Context/Overview.md`, be replaced with an explicit reference, or be given distinct Agent-specific content? This cannot be resolved editorially — it requires a decision about whether the Agents section should own a description of Context distinct from the dedicated Context section, which is a question about section boundaries.

Consequences by outcome:
- *Keep as duplicate:* no immediate harm, but risk of future divergence if one copy is edited without the other.
- *Replace with reference:* removes duplication, but changes how a reader navigates the Agents section.
- *Give distinct content:* requires new normative text describing Context specifically from an Agent's perspective — new authoring work.

**Next Action:** Chief Architect to review and record a Decision.

---

## CAND-002

**Title:** Mechanics of set-scoped (profile-based) Conformance

**Status:** Open

**Owner:** Chief Architect

**Created:** 22 July 2026

**Related Documents:** `Language/Conformance.md`, `docs/Specification/08 Conformance.md`

**Discussion:** `Language/Conformance.md` already names "Profile Conformance" as a category, but does not define the mechanics of a profile — how it is declared, bounded, and validated against the Core. The author has explicitly stated this is a separate topic from the Core specification and should not be folded into it; the mechanism itself still needs to be decided.

Consequences by outcome:
- *Define now:* clarifies Conformance fully, but risks coupling the Core specification to a mechanism that may need to change independently.
- *Leave open, reference from the Conformance chapter:* keeps Core minimal, but leaves implementers without profile guidance until resolved.

**Next Action:** Chief Architect to review and record a Decision.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial queue, 1 candidate |
| 0.1 | 22 July 2026 | Added CAND-002 (set-scoped Conformance), referenced from `docs/Specification/08 Conformance.md` |
| 0.1 | 22 July 2026 | Migrated both candidates to the uniform ID/Title/Status/Owner/Created/Related Documents/Discussion/Next Action lifecycle |

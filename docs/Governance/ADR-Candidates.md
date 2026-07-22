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

---

## CAND-001

**Description:** Should `AI/Agents/Context.md` remain a full duplicate of `AI/Context/Overview.md`, be replaced with an explicit reference, or be given distinct Agent-specific content?

**Reason:** This cannot be resolved editorially — it requires a decision about whether the Agents section should own a description of Context distinct from the dedicated Context section, which is an architectural question about section boundaries.

**Consequences:**
- *Keep as duplicate:* no immediate harm, but risk of future divergence if one copy is edited without the other.
- *Replace with reference:* removes duplication, but changes how a reader navigates the Agents section.
- *Give distinct content:* requires new normative text describing Context specifically from an Agent's perspective — new authoring work.

**Recommended status for ADR:** Needs Discussion

**Source:** Architecture-Observations.md#obs-001

**Decision:** *(pending)*

**Status:** Pending Architect Review

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial queue, 1 candidate |

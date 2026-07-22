# OCOM Specification v0.2 — Committee Review Package

**Document ID:** SPEC-COMMITTEE-01

**Status:** Approved with Editorial Changes — Architecture Committee, 22 July 2026 (editorial changes completed; see Section 8)

**Version:** 0.2

**Prepared:** 22 July 2026

---

This package is self-contained. The committee should be able to reach a decision from this document alone, without reading the development history that produced it.

---

# 1. Executive Summary

`docs/Specification/` is a proposed nine-chapter reading path (`00 Executive Overview` through `08 Conformance`) that compiles and organizes the existing, already-released OCOM v0.1 normative documents into a single, sequential entry point.

It is an **editorial layer**, not a new specification. Every normative statement it contains is drawn from documents the committee has already implicitly accepted by way of the v0.1 release (`Core/`, `Meta/`, `Models/`, `Language/`, `Governance/`). No new architectural concept, no new modeling primitive, and no change to any existing definition is introduced anywhere in these nine chapters.

The granular v0.1 documents remain the normative source of truth and are unaffected by this proposal. If approved, the reading path is integrated into the repository and its own documents become Baseline Specification v0.2 — a presentation of v0.1's content, not a version bump to the architecture itself.

---

# 2. What Changed Since v0.1

| Change | Nature |
|---|---|
| `docs/Governance/` (10 documents) created and frozen as Baseline | Process infrastructure — how the specification is maintained, not what it says. Already reviewed and closed prior to this package; not part of this review. |
| `docs/Specification/` (9 chapters + this package) drafted | **This is the subject of this review.** |
| Reference Architecture layer name reverted to "Business Object Architecture" | Already decided by author during v0.1 RC; not reopened here. |
| `Memory/Evidence Overlay.md`, `Entities/Campaign/Campaign.md` | Already decided by author during v0.1 RC (sections deferred to Future Work); not reopened here. |

Nothing in the underlying architecture — Object, Entity, Domain, Relationship, Reference, Capability, Policy, Contract, Lifecycle, State, Event, Workflow — has changed since v0.1. This package proposes a way of *reading* that architecture, not a change to it.

---

# 3. Scope of Review

**In scope:**
- Whether the nine chapters accurately and faithfully compile the v0.1 normative documents they cite.
- Whether the editorial choices made (see Section 4) are acceptable.
- Whether the reading path is ready to be committed to the repository as Baseline Specification v0.2.

**Out of scope:**
- The OCOM architecture itself (Object, Entity, Domain, etc.) — unchanged, already released as v0.1, not reopened by this review.
- The Governance framework — already reviewed separately and frozen as Baseline.
- The two open ADR Candidates (Section 5) — flagged for future decision, not blocking this review, since neither requires a Core change to approve this reading path.

---

# 4. Open Issues

Issues identified during editorial preparation (Этап 1) and left unresolved by design — flagged, not corrected, per Governance policy that editorial review records tensions rather than silently resolving them.

| ID | Location | Issue | Disposition |
|---|---|---|---|
| EDIT-01 | `05 Object Model.md` | `Meta/Relationship.md` frames Relationship by the *meaning* it conveys; `Models/Relationship.md` frames it as *structural*, not behavioral. Not stated as contradictory in the source documents, but different emphasis. | Recorded as an editorial note in-chapter. No source document changed. Committee may accept as-is or request rewording. |
| EDIT-02 | `01 Introduction.md` | Chapters 2–8 use lowercase "shall/should/may," matching v0.1 source style; Chapter 1 originally defined only uppercase MUST/SHOULD/MAY without stating equivalence. | **Fixed during Этап 1** — an equivalence statement was added to Chapter 1. No longer open. |

---

# 5. ADR Candidates

Both currently **Open**, tracked in `docs/Governance/ADR-Candidates.md`. Neither blocks approval of this reading path — both concern content the reading path only references, not content it defines.

| ID | Title | Relevance to this review |
|---|---|---|
| CAND-001 | Content duplication between `AI/Agents/Context.md` and `AI/Context/Overview.md` | Not referenced by any of the 9 chapters. Unrelated to this review. |
| CAND-002 | Mechanics of set-scoped (profile-based) Conformance | Referenced in `08 Conformance.md` as an explicitly open topic, deliberately not folded into the Core Conformance chapter. |

---

# 6. Release Readiness

Per `docs/Governance/Release-Readiness.md`, v0.1 remains the only released version (Status: Released, 21 July 2026). No new release readiness entry has been created for v0.2 — that entry is created only after this committee's decision, per Governance's "review, then baseline, then commit" sequencing. At the time of this package:

- 0 broken internal links across the repository (2178 checked).
- 0 duplicate Document IDs.
- All 9 chapters carry a Document ID, Status, and Source citation.
- `docs/Specification/` is **not committed** to the repository.

---

# 7. Committee Agenda

1. Confirm scope: this review covers the reading path only, not the underlying architecture (Section 3).
2. Review each chapter's fidelity to its cited source documents (Section-by-section Source lines provided in every chapter).
3. Review EDIT-01 (Section 4) — accept the editorial note as written, or request a specific rewording.
4. Confirm CAND-001 and CAND-002 remain appropriately out of scope for this decision.
5. Record a Decision using the Decision Sheet (Section 8).

---

# 8. Decision Sheet

**Reviewed by:** Architecture Committee (Chair)

**Date:** 22 July 2026

**Outcome:**

- [ ] Approved
- [x] **Approved with Editorial Changes** — commit after the changes listed below are made.
- [ ] Returned for Revision

**Editorial changes required — all completed prior to commit:**

| # | Finding | Decision | Status |
|---|---|---|---|
| 1 | "Governance" homonym (Ch. 4 / Ch. 7) | Accepted (Editorial Clarification Required) — add disambiguating note in both chapters, no new terminology | ✅ Done |
| 2 | "Reference Material" undefined (Ch. 6) | Accepted — define inline at first use | ✅ Done |
| 3 | Principle 9 retitled (Ch. 2) | Revert to Source — restore "AI Interpretability" title and body wording; future scope changes require an ADR, not editorial discretion | ✅ Done |
| 4 | "shall never" (Ch. 5) | Editorial Normalization — align to "shall not" | ✅ Done |
| 5 | Chapter 3 Status: Draft | Keep Draft — status reflects chapter maturity as part of the normative specification, not SHALL-density | No change made |
| 6 | `docs/Governance/` cited as source (Ch. 7) | Accepted as-is — `docs/Governance/` is an approved Baseline and a legitimate citable source | No change made |
| 7 | Minor editorial items (Ch. 1) | Accepted — fix before publication | ✅ Done |

**Notes:** No finding required reconsideration of OCOM's architecture, Core, or model. All findings concerned specification quality — terminology, editorial precision, traceability, and normative-language consistency. Per the Committee's basis for decision: work now shifts from designing the model to maintaining it, documenting it, and accumulating practice through Reference Cases.

**Next step:** Commit `docs/Specification/` and mark it **Specification Baseline v0.2**, per Этап 4.

---

*This package does not itself require a Source citation — it is a review artifact, not a specification chapter. It draws its facts from `docs/Specification/00–08`, `docs/Governance/ADR-Candidates.md`, and `docs/Governance/Release-Readiness.md`, current as of 22 July 2026.*

# OCOM Specification v1.0 — Conformance

**Document ID:** SPEC-08

**Status:** Draft

**Version:** 1.0

**Last Updated:** 17 September 2026

---

## Purpose

Conformance establishes the criteria by which implementations may claim compliance with the OCOM Specification. It promotes interoperability, consistency, portability, and predictable behavior across independent implementations.

## Definition

Conformance is the degree to which an implementation satisfies the normative requirements defined by this specification. **Conformance applies to implementations, not to individual models.**

> **Editorial note (5 September 2026).** In this specification the adjectives conforming, compliant and conformant, when applied to an implementation, are used interchangeably and mean an implementation that satisfies the Mandatory Requirements of this document for the specification version it claims. (Source: `Language/Conformance.md`, Definition.)
>
> **Editorial note.** Chapters 2, 5 and 6 state conformance conditions for models and model elements ("All models created using this specification shall conform to these principles"; "An Entity, Domain, Relationship, Event, State, or Workflow conforms to this specification only if ..."), while this chapter, following `Language/Conformance.md`, scopes conformance claims to implementations. Read together: an implementation makes the conformance claim, and the models it produces are required to satisfy Chapters 2, 5 and 6 as part of that claim. This chapter records the difference in scope rather than resolving it, per the editorial policy stated in Chapter 5; it is logged as an Architecture Observation.

## Mandatory Requirements

A conforming implementation **shall**:

- implement the required language and structural constructs (Chapters 4–6);
- preserve their semantics as defined;
- support applicable validation;
- preserve identifier integrity and namespace consistency.

## Optional Capabilities

The specification may define optional capabilities. Support for an optional capability **shall not** affect conformance unless a higher-level specification explicitly declares it mandatory.

## Extension Conformance

Implementations may provide extensions. Extensions **shall** preserve compatibility with the core specification, avoid changing normative semantics, remain clearly identifiable, and be fully documented. Extensions **shall not** invalidate conformance with the core.

## Conformance Levels

- **Core Conformance** — supports all mandatory requirements defined in Chapters 4–6.
- **Extended Conformance** — supports mandatory requirements together with documented extensions.
- **Profile Conformance** — supports a formally defined OCOM profile (a bounded, named subset or specialization of the specification) while preserving compatibility with Core Conformance.

**Note on scope:** Profile Conformance is defined by the form of a claimant's Profile Declaration, decided through `CAND-002` on 16 September 2026 and grounded in `docs/Governance/Concept-Paper-Profile-Conformance.md`. A declaration names the claimant, pins a Release from `docs/Governance/Publication-Manifest.md` and that Release's commit, lists whole canonical source documents each with its content hash, contains every document Chapters 4 to 6 compile, adds nothing and restates nothing; OCOM publishes no profile and reviews, registers or certifies none. Chapters 4 to 6 remain the floor of every profile claim, consistent with the Non-Conformance clause below. The mechanics are kept in the Governance tier rather than folded into this chapter, consistent with the decision to keep set-scoped conformance a distinct discussion from the Core.

## Non-Conformance

If an implementation does not satisfy one or more mandatory requirements, it **shall not** claim conformance with the corresponding version of this specification. Partial support may be documented without a conformance claim.

## Version Conformance

An implementation **shall** identify the specification version against which conformance is claimed.

## Independence

This chapter does not prescribe certification bodies, compliance programs, testing frameworks, or commercial products. Organizations remain free to establish their own conformance assessment processes.

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.2 | 22 July 2026 | Compiled reading path, approved by the Architecture Committee with editorial changes (`Specification/Committee Review Package.md`). |
| 0.2 | 4 September 2026 | Editorial note added on the scope of conformance across Chapters 2, 5, 6 and 8; no requirement changed. |
| 0.2 | 16 September 2026 | The Note on scope now points to the `CAND-002` Decision and its grounding paper; no requirement changed. |
| 1.0 | 17 September 2026 | Purpose restated from `Language/Conformance.md` (conformance is claimed by implementations, as the Definition below already says); every other statement verified against its source as of this date. |

---

*Source: compiled from `Language/Conformance.md` and the Conformance clauses of `Core/Manifest.md` and `Core/Principles.md`. The "Note on scope" reflects the explicit decision that set-scoped conformance remains a separate discussion from this Core reading path. (4 September 2026: editorial note added on the scope of conformance across Chapters 2, 5, 6 and 8; no requirement changed.) (16 September 2026: the Note on scope now points to the `CAND-002` Decision and its grounding paper; no requirement changed) (17 September 2026: recompiled as v1.0 against the canonical documents as of this date; see Revision History)*

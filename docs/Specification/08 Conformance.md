# OCOM Specification v0.2 — Conformance

**Document ID:** SPEC-08

**Status:** Draft

**Version:** 0.2

---

## Purpose

Conformance establishes the criteria by which an implementation, model, or repository may claim compliance with OCOM. It promotes interoperability, consistency, portability, and predictable behavior across independent implementations.

## Definition

Conformance is the degree to which an implementation satisfies the normative requirements defined by this specification. **Conformance applies to implementations, not to individual models.**

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

**Note on scope:** the precise mechanics of profile definition — how a profile is declared, bounded, and validated — are intentionally not fully specified in this revision. They are tracked as a separate, open topic (see `docs/Governance/ADR-Candidates.md`) rather than folded into this chapter, consistent with the decision to keep set-scoped conformance a distinct discussion from the Core.

## Non-Conformance

If an implementation does not satisfy one or more mandatory requirements, it **shall not** claim conformance with the corresponding version of this specification. Partial support may be documented without a conformance claim.

## Version Conformance

An implementation **shall** identify the specification version against which conformance is claimed.

## Independence

This chapter does not prescribe certification bodies, compliance programs, testing frameworks, or commercial products. Organizations remain free to establish their own conformance assessment processes.

---

*Source: compiled from `Language/Conformance.md` and the Conformance clauses of `Core/Manifest.md` and `Core/Principles.md`. The "Note on scope" reflects the explicit decision that set-scoped conformance remains a separate discussion from this Core reading path.*

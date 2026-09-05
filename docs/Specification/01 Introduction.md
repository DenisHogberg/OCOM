# OCOM Specification v0.2 — Introduction

**Document ID:** SPEC-01

**Status:** Draft

**Version:** 0.2

---

## Abstract

OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations that describes an organization as a system of governed, interconnected objects with identity, ownership, lifecycle, and evidence — expressed here through entities, domains, workflows, and the relationships between them. This Specification is the compiled reading path through that model, not OCOM itself; the model's own normative terms live in the Core Vocabulary (`Meta/`).

It provides a common operational language that enables consistent understanding by humans, software systems, and artificial intelligence, while remaining independent of implementation technologies, vendors, organizational structures, and industries.

## Purpose

The purpose of this specification is to establish a universal operational language for describing how organizations function.

Rather than treating software systems, departments, or business processes as primary concepts, OCOM models the organization itself through a consistent set of operational concepts and relationships. The specification provides a stable foundation for documentation, analysis, governance, automation, and future operational development.

## Motivation

Operational knowledge is commonly distributed across documents, applications, teams, and software platforms. As organizations evolve, this knowledge becomes fragmented, duplicated, inconsistent, and difficult to maintain.

Existing approaches typically describe isolated perspectives — business processes, organizational charts, databases, or software architecture — rather than the operational system as a whole. OCOM introduces a unified operational model capable of representing an organization through one consistent set of operational concepts.

## Guiding Statement

Organizations are not defined by their software. They are defined by the operational relationships between the entities that create, transform, exchange, and preserve business value.

This specification provides a common operational language for describing those relationships independently of implementation.

## Scope

This specification defines:

- operational concepts (Object, Entity, Domain, Relationship, Event, State, Lifecycle, Workflow);
- modeling principles;
- semantic interpretation rules;
- conformance criteria.

This specification does **not** define:

- software architecture, databases, APIs, or programming languages;
- user interface design or infrastructure;
- implementation technologies;
- business strategy;
- AI system design or runtime behavior.

## Design Goals

The framework is designed to be technology-independent, implementation-independent, vendor-neutral, extensible, deterministic, human-readable, machine-readable, and interpretable by artificial intelligence without requiring implementation-specific knowledge.

## Applicability

This specification may be applied to organizations of any size and industry, regardless of existing organizational structures, software platforms, or implementation technologies.

## Intended Audience

Enterprise Architects, Operations Leaders, Solution Architects, System Designers, Business Analysts, Product Organizations, Software Engineers, Researchers, and specification maintainers and reviewers.

## Normative Language

`Core/Manifest.md`'s "Normative Language" section is the single authoritative definition of **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** for this entire specification, including this reading path. It is restated here, verbatim, for reader convenience — this chapter does not define these terms independently, and any future change to their meaning is made in `Core/Manifest.md`, not here:

> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**, when they appear in all capitals in this document, and in every document of this specification, are to be interpreted as described in RFC 2119, as amended by RFC 8174:
>
> - **MUST** indicates an absolute requirement.
> - **MUST NOT** indicates an absolute prohibition.
> - **SHOULD** indicates a recommended practice.
> - **SHOULD NOT** indicates a practice that is generally discouraged.
> - **MAY** indicates an optional capability or implementation choice.

Chapters 2–8 use the lowercase forms **shall**, **shall not**, **should**, and **may**, matching the convention already used throughout the granular OCOM documents (`Meta/`, `Models/`, `Core/`, `Language/`). Independently of RFC 8174's own all-capitals restriction, this specification extends the same defined meanings to these lowercase forms, by its own convention: they are equivalent to **MUST**, **MUST NOT**, **SHOULD**, and **MAY** respectively.

## How to Read This Specification

This document is the second of nine parts that together form the OCOM Specification v0.2 reading path:

0. Executive Overview (informative, non-technical)
1. Introduction (this document)
2. Design Principles
3. Core Concepts
4. Meta Model
5. Object Model
6. Lifecycle Model
7. Governance
8. Conformance

Each concept introduced in Chapters 3–8 is defined in full, with complete normative detail, in the granular reference documents under `docs/Meta/`, `docs/Models/`, `docs/Language/`, and related sections. This reading path is a **compilation and editorial layer over that material, not a replacement for it** — every statement here is traceable to a source document, cited at the end of each chapter. The granular documents remain the normative source of truth and continue to evolve independently of this reading path.

## Future Evolution

This specification is intended to evolve through successive versions while preserving conceptual consistency. Future revisions may introduce new concepts, models, and extensions without changing the fundamental principles established here.

---

*Source: compiled from `Core/Manifest.md`. The Normative Language section is quoted verbatim from `Core/Manifest.md`'s own "Normative Language" section, which is the specification's single authoritative source for these key words as of 20 August 2026 (see `Governance/Publication-Model.md`) — this chapter restates it, it does not independently define it. The shall/MUST equivalence note reflects the existing observation in `docs/Governance/Documentation-Standards.md` (which at the time read "consistent with RFC 2119-style usage, though not currently cited explicitly"; that sentence was corrected on 5 September 2026, since the citation has lived in `Core/Manifest.md` since 20 August 2026) — this chapter was the first to state that equivalence outright. (Committee Review, 22 July 2026: minor wording fixes to the Intended Audience list and the Chapters 3–8 cross-reference; no normative change.) (21 August 2026: Abstract reworded to lead with the canonical identity statement used consistently across `ocom.uno`, `llms.txt`, and `Core/Manifest.md`, and to state explicitly that this Specification is a compiled reading path over OCOM, not OCOM itself — semantic positioning only, no normative change.)*

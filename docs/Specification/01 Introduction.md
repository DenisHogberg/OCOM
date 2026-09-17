# OCOM Specification v1.0 — Introduction

**Document ID:** SPEC-01

**Status:** Draft

**Version:** 1.0

**Last Updated:** 17 September 2026

---

## Abstract

OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations, describing organizations through entities, domains, workflows, and their relationships. `Core/Manifest.md` defines the modeling framework through which that operating model is expressed. This reading path compiles that framework and the canonical documents built on it; it is not OCOM itself, whose normative terms live in the Core Vocabulary (`Meta/`) and the canonical documents cited at the end of each chapter.

The framework provides a common operational language that enables consistent understanding by humans, software systems, and artificial intelligence while remaining independent of implementation technologies, vendors, organizational structures, and industries.

## Purpose

The purpose of this specification is to establish a universal operational language for describing how organizations function.

Rather than treating software systems, departments, or business processes as primary concepts, the framework models the organization itself through a consistent set of operational concepts and relationships.

The specification provides a stable foundation for documentation, analysis, governance, automation, and future operational development.

## Vision

Organizations should be described independently of the technologies used to operate them. Operational knowledge should remain stable as software platforms, organizational structures, and implementation details evolve. Humans and artificial intelligence should be able to interpret the same operational model consistently.

## Motivation

Operational knowledge is commonly distributed across documents, applications, teams, and software platforms. As organizations evolve, this knowledge often becomes fragmented, duplicated, inconsistent, and difficult to maintain.

Existing approaches usually describe isolated perspectives such as business processes, organizational structures, databases, or software architecture rather than the operational system as a whole. This specification introduces a unified operational model capable of representing an organization through consistent operational concepts and relationships.

## Guiding Statement

Organizations are not defined by their software. They are defined by the operational relationships between the entities that create, transform, exchange, and preserve business value.

This specification provides a common operational language for describing those relationships independently of implementation.

## Core Objectives

This specification aims to:

- establish a common operational vocabulary;
- improve consistency across operational models;
- reduce ambiguity in organizational documentation;
- support interoperability between operational systems;
- enable AI-assisted analysis and automation;
- provide a stable foundation for future operational standards.

## Design Goals

The framework is designed to be:

- technology-independent;
- implementation-independent;
- vendor-neutral;
- extensible;
- deterministic;
- human-readable;
- machine-readable;
- AI-native.

## Applicability

This specification may be applied to organizations of any size and across any industry. The framework is intended for operational modeling and may be adopted regardless of existing organizational structures, software platforms, or implementation technologies.

## Scope

This specification defines:

- operational concepts;
- entities;
- domains;
- workflows;
- operational relationships;
- modeling principles;
- semantic interpretation rules.

This specification does not define:

- software architecture;
- databases;
- APIs;
- programming languages;
- user interface design;
- infrastructure;
- implementation technologies;
- business strategy;
- professional or expert judgments (legal, compliance, financial, or similar);
- the responsibilities of an organization's specialized functions (Legal, Compliance, Finance, Security, HR, and others), per Constitution Principle 14, Professional Responsibility.

## Design Philosophy

The framework is based on several fundamental ideas. Organizations are composed of interacting entities. Domains define responsibility. Workflows transform entity states. Knowledge belongs to entities. Software implements the operational model but does not define it, per Constitution Principle 13, Adaptation Flows Toward the Model. Operational models should remain understandable by both humans and artificial intelligence.

## Intended Audience

This specification is intended for:

- Enterprise Architects;
- Operations Leaders;
- Solution Architects;
- System Designers;
- Business Analysts;
- Product Organizations;
- Software Engineers;
- AI Engineers;
- Researchers.

## Normative Language

`Core/Manifest.md`'s "Normative Language" section is the single authoritative definition of **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** for this entire specification, including this reading path, and of the lowercase forms the canonical documents use. It is restated here, verbatim, for reader convenience; this chapter does not define these terms independently, and any future change to their meaning is made in `Core/Manifest.md`, not here:

> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**, when they appear in all capitals in this document, and in every document of this specification, are to be interpreted as described in RFC 2119, as amended by RFC 8174:
>
> - **MUST** indicates an absolute requirement.
> - **MUST NOT** indicates an absolute prohibition.
> - **SHOULD** indicates a recommended practice.
> - **SHOULD NOT** indicates a practice that is generally discouraged.
> - **MAY** indicates an optional capability or implementation choice.
>
> This is the single authoritative definition of these key words for the entire specification. Independently of RFC 8174's own all-capitals restriction, this specification additionally extends the same defined meanings to the lowercase forms (**shall**, **shall not**, **should**, **may**, and the forms **must** and **must not** as used in `Core/Constitution.md` — the convention already used throughout `Meta/`, `Models/`, `Core/`, and `Language/`): a document using a lowercase form intends the same normative weight as its uppercase equivalent above, by this specification's own convention, not because RFC 8174 itself extends that far. Any document restating this definition, rather than citing it, is a duplication to be corrected, not a second source.

Chapters 2 to 8 use the lowercase forms under that convention.

## How to Read This Specification

This document is the second of nine parts that together form the OCOM Specification v1.0 reading path:

0. Executive Overview (informative, non-technical)
1. Introduction (this document)
2. Design Principles
3. Core Concepts
4. Meta Model
5. Object Model
6. Lifecycle Model
7. Governance
8. Conformance

The v1.0 reading path is compiled from Constitution 1.0.1, the Core Vocabulary 0.1 (13 governed terms) and the canonical documents as they stand on 17 September 2026; the Release that publishes it names the exact commit in `Governance/Publication-Manifest.md`. Each concept introduced in Chapters 3 to 8 is defined in full, with complete normative detail, in the granular reference documents under `docs/Meta/`, `docs/Models/`, `docs/Language/`, and related sections. This reading path is a **compilation and editorial layer over that material, not a replacement for it**: every statement here is traceable to a source document, cited at the end of each chapter. The granular documents remain the normative source of truth and continue to evolve independently of this reading path.

## Relationship to the Constitution

Since 26 July 2026, when `CAND-006` adopted it, the specification is governed by `Core/Constitution.md` (Core-00, recorded there on 27 July 2026, version 1.0.1 since 11 September 2026). Its fourteen Canonical Principles govern every document of the specification, this reading path included. This reading path compiles the canonical source documents named at the end of each chapter and does not compile the Constitution; Chapter 2 cites the Constitution where a Design Principle is canonically stated there. Where this reading path and the Constitution differ, the Constitution and the canonical source documents govern, per `Governance/Publication-Model.md`. An Architecture Freeze (`CAND-007`, 27 July 2026) is in force; Chapter 7 states what it means for changes to the specification.

## Future Evolution

This specification is intended to evolve through successive versions while preserving conceptual consistency. Future revisions may introduce new concepts, models, and extensions without changing the fundamental principles established by this specification.

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.2 | 22 July 2026 | Compiled reading path, approved by the Architecture Committee with editorial changes (`Specification/Committee Review Package.md`). |
| 0.2 | 22 July 2026 | Minor wording fixes to the Intended Audience list and the Chapters 3–8 cross-reference; no normative change. |
| 0.2 | 21 August 2026 | Abstract reworded to lead with the canonical identity statement used consistently across `ocom.uno`, `llms.txt`, and `Core/Manifest.md`, and to state explicitly that this Specification is a compiled reading path over OCOM, not OCOM itself — semantic positioning only, no normative change. |
| 0.2 | 16 September 2026 | Added Relationship to the Constitution, per `Master-Architecture-Backlog.md` EPIC-F; no requirement changed. |
| 0.2 | 16 September 2026 | Adoption date stated as 26 July 2026 per `CAND-006`. |
| 1.0 | 17 September 2026 | Recompiled against `Core/Manifest.md` as of this date: Abstract, Purpose, Motivation, Guiding Statement, Applicability, Scope, Design Goals, Intended Audience and Future Evolution now carry the Manifest's own sentences and lists, and Vision, Core Objectives and Design Philosophy are compiled for the first time; the Normative Language quotation now carries the whole Manifest section, including its lowercase-forms convention, which this chapter had paraphrased; How to Read names the versions compiled. The 22 July 2026 compilation is preserved in the repository history. |

---

*Source: compiled from `Core/Manifest.md`, with its Abstract, Purpose, Vision, Motivation, Guiding Statement, Core Objectives, Design Goals, Applicability, Scope, Design Philosophy, Intended Audience and Future Evolution sections carried verbatim (single-sentence paragraphs joined where the chapter groups them; the two Constitution references in Scope and Design Philosophy are written as "Constitution Principle 14" and "Constitution Principle 13" where the Manifest writes the section sign). The Normative Language section is quoted verbatim from `Core/Manifest.md`'s own "Normative Language" section, which is the specification's single authoritative source for these key words (see `Governance/Publication-Model.md`); this chapter restates it, it does not independently define it. (Committee Review, 22 July 2026: minor wording fixes to the Intended Audience list and the Chapters 3–8 cross-reference; no normative change.) (21 August 2026: Abstract reworded to lead with the canonical identity statement used consistently across `ocom.uno`, `llms.txt`, and `Core/Manifest.md`, and to state explicitly that this Specification is a compiled reading path over OCOM, not OCOM itself — semantic positioning only, no normative change.) (16 September 2026: added Relationship to the Constitution, per `Master-Architecture-Backlog.md` EPIC-F; no requirement changed) (16 September 2026: adoption date stated as 26 July 2026 per `CAND-006`) (17 September 2026: recompiled as v1.0 against `Core/Manifest.md` as of this date; see Revision History)*

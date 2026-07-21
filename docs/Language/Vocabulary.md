<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Vocabulary

[← Back](Validation.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Vocabulary

**Document ID:** LANG-VOCABULARY-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the vocabulary of the OCOM Language.

The vocabulary establishes the standardized words and conceptual constructs used to describe OCOM models.

A common vocabulary promotes consistency, interoperability, readability, and machine interpretability across the OCOM ecosystem.

---

# Definition

Vocabulary is the controlled collection of standardized terms used by the OCOM Language.

Each vocabulary term represents a defined modeling concept and shall have a single unambiguous meaning within the specification.

---

# Business Meaning

A shared vocabulary enables organizations to communicate operational models consistently across business domains, technologies, and implementation environments.

Vocabulary supports collaboration between business stakeholders, architects, engineers, AI systems, and automation platforms.

---

# Design Principles

The vocabulary shall:

- be consistent;
- be unambiguous;
- be extensible;
- avoid duplication;
- support interoperability;
- remain technology independent.

---

# Vocabulary Categories

The OCOM Language organizes vocabulary into the following categories.

## Structural Terms

Describe the structure of models.

Examples include:

- Object;
- Entity;
- Relationship;
- Reference;
- Registry;
- Domain.

---

## Behavioral Terms

Describe operational behavior.

Examples include:

- Lifecycle;
- Event;
- Workflow;
- State;
- Transition.

---

## Governance Terms

Describe organizational governance.

Examples include:

- Policy;
- Constraint;
- Ownership;
- Evaluation;
- Contract.

---

## AI Terms

Describe AI operational concepts.

Examples include:

- Agent;
- Context;
- Memory;
- Knowledge;
- Prompt;
- Tool.

---

## Language Terms

Describe the language itself.

Examples include:

- Namespace;
- Identifier;
- Schema;
- Syntax;
- Notation.

---

# Vocabulary Rules

Vocabulary terms shall:

- have one primary meaning;
- avoid conflicting definitions;
- remain stable across versions;
- be reusable across specifications.

Organizations may extend the vocabulary without redefining existing terms.

---

# Naming

Vocabulary terms should:

- use singular nouns where practical;
- be concise;
- avoid abbreviations unless standardized;
- avoid implementation-specific terminology.

---

# Synonyms

Organizations may maintain synonym mappings.

However, the OCOM Specification recognizes only one canonical term for each vocabulary concept.

---

# Extensions

Organizations may introduce additional vocabulary terms.

Extensions shall:

- preserve compatibility;
- avoid semantic conflicts;
- document new definitions.

---

# Governance

Vocabulary shall be governed through:

- version management;
- review;
- approval;
- controlled extension.

Vocabulary evolution shall preserve backward compatibility whenever practical.

---

# Relationship to Other Specifications

Vocabulary provides the common language used throughout:

- Meta
- Core
- Models
- Entities
- Lifecycles
- Memory
- AI
- Domains

Vocabulary defines language constructs rather than business behavior.

---

# Independence

The Vocabulary specification does not prescribe:

- natural languages;
- implementation technologies;
- serialization formats.

Vocabulary concepts may be expressed in any human language while preserving semantic meaning.

---

# Conformance

A compliant implementation shall:

- use canonical vocabulary consistently;
- preserve vocabulary semantics;
- support vocabulary extension;
- maintain interoperability.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

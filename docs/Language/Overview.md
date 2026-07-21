<!-- nav:start -->
[Docs](../README.md) / [Language](README.md) / Language

[← Back](Notation.md) · [↑ Up](README.md) · [Next →](Schema.md)

---
<!-- nav:end -->

# Language

**Document ID:** LANG-README-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

The Language specification defines the common language used to describe OCOM models.

It establishes a consistent notation, vocabulary, syntax, and structural conventions that enable humans and systems to create, exchange, validate, and interpret OCOM models consistently.

The Language specification is independent of any implementation technology or serialization format.

---

# Scope

The Language specification defines:

- notation;
- vocabulary;
- naming conventions;
- namespaces;
- identifiers;
- schema principles;
- conformance levels.

The Language specification does not define business semantics.

Business semantics are defined by the Meta, Core, Models, and Domain specifications.

---

# Objectives

The objectives of the Language specification are to:

- establish a common modeling language;
- improve readability;
- enable interoperability;
- support automated validation;
- support serialization;
- enable future tooling.

---

# Design Principles

The Language specification shall:

- be human-readable;
- be machine-processable;
- remain implementation independent;
- support extensibility;
- preserve semantic consistency;
- minimize ambiguity.

---

# Components

The Language specification currently defines:

- Notation;
- Schema;
- Vocabulary;
- Namespace;
- Identifier Syntax;
- Conformance Levels.

Future versions may introduce additional language constructs.

---

# Relationship to Other Specifications

The Language specification provides the representation layer for:

- Meta;
- Core;
- Models;
- Entities;
- Lifecycles;
- Memory;
- Artificial Intelligence;
- Domains.

Language defines how models are expressed.

Other specifications define what those models mean.

---

# Independence

The Language specification does not prescribe:

- JSON;
- XML;
- YAML;
- RDF;
- SQL;
- Graph databases;
- programming languages.

Organizations remain free to serialize OCOM models using any compatible representation.

---

# Conformance

A conforming implementation shall:

- use Language concepts consistently;
- preserve semantic meaning;
- support interoperability;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

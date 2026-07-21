<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Prompts](README.md) / Prompt

[← Back](Prompt%20Templates.md) · [↑ Up](README.md)

---
<!-- nav:end -->

# Prompt

**Document ID:** AI-Prompt-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Prompt as an execution artifact within the OCOM Artificial Intelligence Specification.

A Prompt provides structured instructions to a reasoning engine using operational Context assembled for a specific execution.

---

# Definition

A Prompt is a structured execution instruction generated for a reasoning engine.

A Prompt communicates objectives, constraints, and relevant Context in a form consumable by an execution engine.

A Prompt is temporary and exists only for the duration of an execution.

A Prompt is neither Knowledge nor Memory.

---

# Business Meaning

Prompts enable organizations to separate business understanding from model interaction.

Business logic belongs to organizational Knowledge and operational Context.

Prompts translate that information into executable instructions for a reasoning engine.

---

# Core Principles

Every Prompt shall be:

- execution-specific;
- context-driven;
- reproducible;
- explainable;
- governed;
- technology independent.

---

# Mandatory Attributes

Every Prompt shall define:

- Identifier
- Objective
- Target Reasoning Engine
- Creation Time
- Status

---

# Optional Attributes

A Prompt may define:

- Description
- Prompt Template
- Context Reference
- Agent Reference
- Constraints
- Expected Output
- Execution Metadata

---

# Prompt Components

A Prompt may include:

- execution objective;
- operational Context;
- instructions;
- constraints;
- expected output;
- execution parameters.

Organizations may define additional components.

---

# Prompt Generation

Prompts may be generated:

- dynamically;
- from templates;
- by AI Agents;
- by workflow automation;
- by human operators.

Generation mechanisms are implementation-specific.

---

# Relationships

A Prompt may reference:

- AI Agents;
- Context;
- Knowledge;
- Memory;
- Tools;
- Workflows.

Relationships shall preserve traceability.

---

# Governance

Prompt generation and usage shall comply with:

- organizational policies;
- access permissions;
- privacy requirements;
- security classifications.

---

# Explainability

Organizations shall be able to determine:

- why the Prompt was generated;
- which Context was included;
- which Agent created the Prompt;
- which execution objective it supported.

---

# Lifecycle

Prompts are temporary execution artifacts.

Following execution, a Prompt may:

- be discarded;
- be archived;
- become part of execution history.

Prompt persistence is organization-specific.

---

# Independence

The Prompt specification does not prescribe:

- prompt syntax;
- prompt engineering methods;
- LLM providers;
- reasoning engines;
- orchestration frameworks.

Organizations remain free to implement Prompt generation using any compatible technology.

---

# Conformance

A compliant implementation shall:

- define execution-specific Prompts;
- separate Prompts from Knowledge and Memory;
- preserve explainability;
- support governed generation;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

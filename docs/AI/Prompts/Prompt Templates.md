<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Prompts](README.md) / Prompt Templates

[← Back](Prompt%20Lifecycle.md) · [↑ Up](README.md) · [Next →](Prompt.md)

---
<!-- nav:end -->

# Prompt Templates

**Document ID:** AI-Prompt-04

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Prompt Templates within the OCOM Artificial Intelligence Specification.

Prompt Templates provide reusable structures for generating consistent Prompts while separating reusable instructions from execution-specific Context.

---

# Definition

A Prompt Template is a reusable specification used to generate one or more execution-specific Prompts.

A Prompt Template defines the structure of a Prompt but does not contain execution-specific Context.

---

# Business Meaning

Prompt Templates improve consistency across AI executions.

Organizations can standardize common interaction patterns while allowing each execution to incorporate its own operational Context.

Templates reduce duplication and simplify governance.

---

# Core Principles

Every Prompt Template shall be:

- reusable;
- governed;
- versioned;
- explainable;
- maintainable;
- technology independent.

---

# Mandatory Attributes

Every Prompt Template shall define:

- Identifier
- Name
- Purpose
- Owner
- Version
- Status

---

# Optional Attributes

A Prompt Template may define:

- Description
- Supported Agent Roles
- Supported Objectives
- Input Parameters
- Output Expectations
- Constraints
- Related Workflows

---

# Template Components

A Prompt Template may define:

- instruction structure;
- reusable guidance;
- placeholders;
- execution constraints;
- expected response format;
- validation rules.

Execution-specific Context shall not be permanently embedded within a Prompt Template.

---

# Template Usage

Prompt Templates may be used by:

- AI Agents;
- Workflows;
- automation systems;
- business applications;
- human operators.

Organizations may define additional consumers.

---

# Versioning

Prompt Templates shall support version management.

Every revision should preserve:

- previous version;
- modification history;
- approval history;
- change rationale.

Organizations may maintain multiple active versions.

---

# Governance

Prompt Templates shall comply with:

- approval procedures;
- organizational policies;
- access permissions;
- security requirements.

Only approved Templates should be available for operational use.

---

# Explainability

Organizations shall be able to determine:

- which Template generated a Prompt;
- which version was used;
- who approved the Template;
- why the Template was selected.

---

# Auditability

Organizations shall preserve:

- Template Identifier;
- version history;
- approval history;
- modification history;
- usage history.

Audit records shall remain immutable.

---

# Relationship to Other Specifications

Prompt Templates interact with:

- Prompt
- Prompt Lifecycle
- Prompt Governance
- Agent
- Context
- Workflows

---

# Independence

The Prompt Templates specification does not prescribe:

- prompt syntax;
- template engines;
- programming languages;
- orchestration frameworks.

Organizations remain free to implement Prompt Templates using any compatible technology.

---

# Conformance

A compliant implementation shall:

- support reusable Prompt Templates;
- preserve version history;
- support governed reuse;
- maintain explainability;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

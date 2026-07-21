<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Prompts](README.md) / Prompts

[↑ Up](README.md) · [Next →](Prompt%20Evaluation.md)

---
<!-- nav:end -->

# Prompts

**Document ID:** AI-Prompt-00

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

The Prompts Specification defines how AI Agents communicate with language models and other reasoning engines within the OCOM Artificial Intelligence Specification.

Prompts provide a standardized interaction mechanism while remaining independent of specific model providers and prompting techniques.

---

# Definition

A Prompt is a structured instruction presented to a reasoning engine in order to accomplish a specific objective.

A Prompt is an execution artifact.

It is generated from operational Context and is not considered organizational Knowledge or Memory.

---

# Core Principles

Prompts shall be:

- objective-driven;
- contextual;
- explainable;
- reproducible;
- governed;
- technology independent.

---

# Objectives

The Prompts Specification enables organizations to:

- standardize AI interactions;
- improve execution consistency;
- reduce prompt duplication;
- support governance;
- preserve explainability;
- separate prompts from business knowledge.

---

# Architecture

The Prompts Specification consists of the following documents:

- Prompt
- Prompt Lifecycle
- Prompt Governance
- Prompt Templates
- Prompt Evaluation

Each document defines one aspect of prompt management.

---

# Relationship to Other Specifications

Prompts interact with:

- Agents
- Context
- Knowledge
- Memory
- Tools

Prompts consume Context but do not replace it.

---

# Technology Independence

The Prompts Specification does not prescribe:

- prompt engineering techniques;
- LLM providers;
- model architectures;
- prompt formats;
- orchestration frameworks.

Organizations may implement Prompts using any compatible technology.

---

# Conformance

A compliant implementation shall:

- define governed Prompts;
- separate Prompts from Knowledge and Memory;
- support explainability;
- preserve reproducibility;
- remain technology independent.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

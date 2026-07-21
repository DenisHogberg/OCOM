<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Context](README.md) / Context

[← Back](Context%20Optimization.md) · [↑ Up](README.md) · [Next →](Overview.md)

---
<!-- nav:end -->

# Context

**Document ID:** AI-Context-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines Context as the primary operational information environment used by AI Agents during task execution.

Context provides the information required for reasoning, planning, decision-making, and action while remaining independent of implementation technologies.

---

# Definition

Context is a dynamically assembled collection of information relevant to a specific execution.

Context exists only for the duration of an execution unless explicitly persisted through the OCOM Memory Specification.

Context is not a database, a prompt, or a Memory Record.

It is the operational environment in which an AI Agent performs work.

---

# Business Meaning

Context enables AI Agents to understand the current business situation.

Rather than searching every available source, an AI Agent receives a curated operational view containing only the information required for the current objective.

---

# Core Principles

Every Context shall:

- be execution-specific;
- be dynamically assembled;
- contain only relevant information;
- preserve provenance;
- remain explainable;
- comply with governance policies;
- remain technology independent.

---

# Mandatory Attributes

Every Context shall define:

- Identifier
- Objective
- Scope
- Status
- Creation Time
- Owner

---

# Optional Attributes

A Context may define:

- Description
- Priority
- Expiration Time
- Tags
- Related Workflow
- Related Entity
- Related Agent

---

# Context Sources

Context may include information from:

- Entities
- Events
- Workflows
- Memory Records
- Organizational Knowledge
- Business Rules
- Human Instructions
- External Systems

---

# Scope

A Context shall define its operational scope.

Examples include:

- Customer
- Payment
- Campaign
- Incident
- Project
- Vendor
- Employee

A Context may reference multiple entities.

---

# Lifetime

Context exists only while required for execution.

After execution:

- Context may be discarded;
- selected information may become Memory Records;
- audit information shall be preserved.

---

# Relationships

A Context may reference:

- AI Agents
- Entities
- Events
- Workflows
- Memory Records
- Knowledge
- Tools

---

# Governance

Context shall respect:

- access permissions;
- privacy policies;
- security classifications;
- retention policies;
- organizational governance.

---

# Explainability

The origin of every Context element shall be traceable.

Organizations shall be able to determine:

- where information originated;
- why it was included;
- when it was retrieved.

---

# Independence

The Context specification does not prescribe:

- context window sizes;
- prompt formats;
- vector databases;
- retrieval algorithms;
- LLM providers.

Organizations remain free to implement context management using any compatible technology.

---

# Conformance

A compliant implementation shall:

- dynamically assemble Context;
- preserve provenance;
- support governance;
- maintain explainability;
- separate Context from Memory.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

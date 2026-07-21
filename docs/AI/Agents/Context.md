<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Agents](README.md) / Context

[← Back](Agent.md) · [↑ Up](README.md) · [Next →](Multi-Agent%20Collaboration.md)

---
<!-- nav:end -->

# Context

**Document ID:** AI-Agents-05

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Context Specification within the OCOM Artificial Intelligence framework.

Context provides the operational information required by AI Agents to perform reasoning, decision-making, and execution.

The Context Specification establishes a standardized representation of operational context independent of AI models, orchestration frameworks, and implementation technologies.

---

# Definition

Context is the collection of information made available to an AI Agent during the execution of a specific task.

Context provides situational awareness by combining entities, operational knowledge, memory, workflows, events, and organizational policies.

Context exists only for the duration of an execution unless explicitly persisted through the OCOM Memory Specification.

---

# Design Principles

Context shall:

- be task-specific;
- be dynamically assembled;
- remain explainable;
- minimize irrelevant information;
- preserve provenance;
- remain technology independent.

---

# Scope

The Context Specification defines:

- context composition;
- context assembly;
- context optimization;
- context lifecycle;
- context governance.

---

# Context Architecture

The Context Specification consists of the following documents:

- Context
- Context Assembly
- Context Lifecycle
- Context Optimization

Additional documents may be introduced in future versions.

---

# Context Sources

Context may be assembled from:

- Entities;
- Domains;
- Workflows;
- Events;
- Memory Records;
- Organizational Knowledge;
- Business Rules;
- Human Input;
- External Systems.

---

# Relationship to OCOM

Context integrates information across the OCOM ecosystem.

It consumes information from:

- Entities
- Memory
- Knowledge
- Workflows
- Events
- Lifecycles

Context itself does not permanently store information.

Persistent information shall be managed through the Memory Specification.

---

# Governance

Context shall comply with organizational governance.

Governance may define:

- permitted data sources;
- access permissions;
- privacy restrictions;
- retention limits;
- execution boundaries.

---

# Operational Goals

The Context Specification aims to:

- improve reasoning quality;
- reduce irrelevant information;
- increase operational consistency;
- support explainable AI;
- optimize execution efficiency.

---

# Independence

The Context Specification does not prescribe:

- context window size;
- prompt engineering techniques;
- vector databases;
- retrieval algorithms;
- LLM providers.

Organizations remain free to implement context management using any compatible technology.

---

# Conformance

A compliant implementation shall:

- dynamically assemble operational context;
- preserve provenance;
- support governed access;
- remain explainable;
- comply with organizational governance.

---

# Documents

The Context Specification includes:

- Context
- Context Assembly
- Context Lifecycle
- Context Optimization

Additional documents may be introduced in future versions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

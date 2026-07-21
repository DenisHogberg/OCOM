<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Context](README.md) / Context Assembly

[↑ Up](README.md) · [Next →](Context%20Lifecycle.md)

---
<!-- nav:end -->

# Context Assembly

**Document ID:** AI-Context-02

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the process of assembling operational Context within the OCOM Artificial Intelligence Specification.

Context Assembly determines how relevant information is collected, filtered, and organized before being provided to an AI Agent.

---

# Definition

Context Assembly is the governed process of constructing an execution-specific Context from one or more operational information sources.

The objective is to provide sufficient information for decision-making while minimizing unnecessary complexity.

---

# Design Principles

Context Assembly shall:

- be objective-driven;
- include only relevant information;
- preserve provenance;
- respect governance policies;
- remain explainable;
- remain technology independent.

---

# Assembly Process

Context Assembly typically consists of the following stages:

1. Define Objective
2. Identify Scope
3. Discover Information Sources
4. Retrieve Relevant Information
5. Validate Access Permissions
6. Organize Context
7. Deliver Context to the AI Agent

Organizations may extend this process.

---

# Information Sources

Context may be assembled from:

- Entities;
- Events;
- Workflows;
- Memory Records;
- Organizational Knowledge;
- Business Rules;
- Human Input;
- External Systems.

Each source shall preserve provenance.

---

# Context Selection

Information shall be selected according to:

- business objective;
- operational scope;
- governance policies;
- relevance;
- confidence;
- recency.

Selection algorithms are implementation-specific.

---

# Context Composition

The assembled Context may include:

- entities;
- operational history;
- active workflows;
- recent events;
- relevant memory;
- organizational knowledge;
- applicable policies;
- supporting evidence.

---

# Governance

Context Assembly shall respect:

- access permissions;
- privacy requirements;
- security classifications;
- data ownership;
- organizational policies.

Unauthorized information shall not be included.

---

# Provenance

Every Context element shall preserve:

- originating source;
- retrieval time;
- retrieval method;
- applicable permissions.

Provenance shall remain available throughout execution.

---

# Explainability

Organizations shall be able to determine:

- why information was selected;
- why information was excluded;
- which source provided the information;
- how the Context was assembled.

---

# Relationship to Other Specifications

Context Assembly interacts with:

- Context
- Memory
- Knowledge
- Entities
- Events
- Workflows
- Tools

---

# Independence

The Context Assembly specification does not prescribe:

- retrieval algorithms;
- vector search;
- graph traversal;
- ranking models;
- prompt construction;
- orchestration frameworks.

Organizations may implement any compatible assembly mechanism.

---

# Conformance

A compliant implementation shall:

- assemble Context dynamically;
- preserve provenance;
- support governed access;
- maintain explainability;
- remain independent of implementation technologies.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

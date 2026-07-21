<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Context](README.md) / Context Lifecycle

[← Back](Context%20Assembly.md) · [↑ Up](README.md) · [Next →](Context%20Optimization.md)

---
<!-- nav:end -->

# Context Lifecycle

**Document ID:** AI-Context-03

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the lifecycle of Context within the OCOM Artificial Intelligence Specification.

The Context Lifecycle establishes the operational states through which Context progresses during execution.

---

# Definition

The Context Lifecycle represents the controlled evolution of Context from its initial creation until its disposal or persistence.

Context is inherently temporary and exists only to support a specific execution.

---

# Design Principles

The Context Lifecycle shall:

- support dynamic execution;
- minimize unnecessary persistence;
- preserve explainability;
- preserve provenance;
- support governance.

---

# Lifecycle States

The OCOM Specification defines the following lifecycle states.

## Requested

A request for operational Context has been initiated.

Characteristics:

- execution objective defined;
- scope identified;
- no information collected.

---

## Assembling

Relevant information is being collected.

Characteristics:

- sources identified;
- information retrieved;
- permissions validated.

---

## Ready

Context has been successfully assembled.

Characteristics:

- information organized;
- provenance preserved;
- available for execution.

---

## Active

The AI Agent is actively using the Context.

Characteristics:

- reasoning;
- planning;
- tool execution;
- decision support.

---

## Updated

The Context has been modified during execution.

Typical reasons include:

- new Events;
- new Memory Records;
- human input;
- workflow changes.

Updates shall preserve provenance.

---

## Completed

Execution has finished.

Context is no longer actively used.

Relevant information may be promoted to Memory.

---

## Discarded

Temporary Context has been removed.

No operational execution continues.

Audit information remains preserved.

---

# Lifecycle Transitions

Typical lifecycle progression:

Requested

↓

Assembling

↓

Ready

↓

Active

↓

Updated (optional)

↓

Completed

↓

Discarded

Organizations may introduce additional states while preserving governance.

---

# Context Refresh

Context may be refreshed when:

- new Events occur;
- Memory changes;
- workflow state changes;
- human participants provide new information;
- business policies require updates.

---

# Persistence

Context itself is temporary.

Only selected information may become:

- Memory Records;
- Events;
- Workflow updates;
- business system changes.

Persistence shall comply with the Memory Specification.

---

# Governance

Lifecycle transitions shall respect:

- access permissions;
- retention policies;
- organizational governance;
- security requirements.

---

# Auditability

Lifecycle history shall preserve:

- Context Identifier;
- previous state;
- new state;
- timestamp;
- initiating actor;
- transition reason.

Audit history shall remain immutable.

---

# Relationship to Other Specifications

The Context Lifecycle interacts with:

- Context
- Context Assembly
- Memory
- Workflows
- Events
- Agent

---

# Independence

The Context Lifecycle specification does not prescribe:

- orchestration frameworks;
- runtime engines;
- implementation technologies.

Organizations remain free to implement lifecycle management using any compatible architecture.

---

# Conformance

A compliant implementation shall:

- support lifecycle states;
- preserve lifecycle history;
- maintain provenance;
- support governed state transitions.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

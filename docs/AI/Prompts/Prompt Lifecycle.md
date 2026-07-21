<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Prompts](README.md) / Prompt Lifecycle

[← Back](Prompt%20Governance.md) · [↑ Up](README.md) · [Next →](Prompt%20Templates.md)

---
<!-- nav:end -->

# Prompt Lifecycle

**Document ID:** AI-Prompt-02

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the lifecycle of Prompts within the OCOM Artificial Intelligence Specification.

The Prompt Lifecycle establishes the operational states through which a Prompt progresses from generation to completion.

---

# Definition

The Prompt Lifecycle represents the temporary evolution of a Prompt during execution.

Unlike Knowledge and Memory, Prompts are execution artifacts with a short operational lifetime.

---

# Design Principles

The Prompt Lifecycle shall:

- support reproducibility;
- preserve explainability;
- maintain traceability;
- support governance;
- remain technology independent.

---

# Lifecycle States

The OCOM Specification defines the following lifecycle states.

## Requested

A Prompt has been requested.

Characteristics:

- execution objective identified;
- Context requested;
- Prompt not yet generated.

---

## Generated

The Prompt has been successfully created.

Characteristics:

- Context incorporated;
- instructions prepared;
- constraints applied.

---

## Validated

The Prompt has completed required validation.

Validation may include:

- policy verification;
- template validation;
- security checks;
- completeness verification.

---

## Executing

The Prompt has been submitted to a reasoning engine.

Characteristics:

- execution in progress;
- response pending.

---

## Completed

Execution has successfully finished.

A response has been received.

Execution metadata shall be preserved.

---

## Failed

Prompt execution did not complete successfully.

Typical reasons include:

- validation failure;
- execution timeout;
- unavailable reasoning engine;
- policy violation.

Failure information shall be retained.

---

## Archived

The Prompt is no longer active.

Organizations may retain archived Prompts for:

- auditing;
- reproducibility;
- troubleshooting;
- compliance.

---

# Lifecycle Transitions

Typical lifecycle progression:

Requested

↓

Generated

↓

Validated

↓

Executing

↓

Completed

↓

Archived

Failure may occur after validation or execution initiation.

Organizations may define additional lifecycle states.

---

# Ownership

Every Prompt shall have an originating actor.

The originating actor may be:

- an AI Agent;
- a Workflow;
- a human operator;
- an automated process.

Ownership shall preserve traceability.

---

# Governance

Lifecycle transitions shall comply with:

- organizational policies;
- access permissions;
- security requirements;
- retention policies.

---

# Auditability

Organizations shall preserve:

- Prompt Identifier;
- lifecycle history;
- originating actor;
- execution timestamps;
- execution outcome;
- archival status.

Audit records shall remain immutable.

---

# Relationship to Other Specifications

The Prompt Lifecycle interacts with:

- Prompt
- Agent
- Context
- Tool Execution
- Memory

---

# Independence

The Prompt Lifecycle specification does not prescribe:

- reasoning engines;
- orchestration frameworks;
- prompt formats;
- implementation technologies.

Organizations remain free to implement lifecycle management using any compatible architecture.

---

# Conformance

A compliant implementation shall:

- support lifecycle states;
- preserve execution history;
- maintain auditability;
- support governed Prompt execution.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Agents](README.md) / Agent Roles

[← Back](Agent%20Lifecycle.md) · [↑ Up](README.md) · [Next →](Agent.md)

---
<!-- nav:end -->

# Agent Roles

**Document ID:** AI-Agents-03

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the standard operational roles that AI Agents may perform within the OCOM Artificial Intelligence Specification.

Roles describe the operational responsibility of an AI Agent rather than its implementation or underlying AI model.

---

# Definition

An Agent Role defines the primary operational function performed by an AI Agent within an enterprise environment.

An AI Agent may perform one or multiple roles depending on organizational requirements.

---

# Design Principles

Agent Roles shall:

- define responsibilities rather than implementation;
- remain technology independent;
- support specialization;
- support collaboration;
- support governance.

---

# Standard Roles

The OCOM Specification defines the following standard roles.

## Coordinator

Coordinates work performed by multiple AI Agents.

Typical responsibilities include:

- task decomposition;
- work distribution;
- dependency management;
- progress monitoring;
- result aggregation.

---

## Planner

Creates execution plans to achieve defined objectives.

Typical responsibilities include:

- objective analysis;
- planning;
- sequencing activities;
- identifying dependencies.

---

## Researcher

Collects and organizes information.

Typical responsibilities include:

- information retrieval;
- document analysis;
- knowledge discovery;
- evidence collection.

---

## Analyst

Evaluates available information.

Typical responsibilities include:

- business analysis;
- comparison;
- classification;
- anomaly detection;
- recommendation generation.

---

## Executor

Performs approved operational actions.

Typical responsibilities include:

- workflow execution;
- tool invocation;
- system interaction;
- task completion.

---

## Reviewer

Evaluates outputs produced by AI Agents or humans.

Typical responsibilities include:

- validation;
- quality assessment;
- policy compliance;
- consistency checking.

---

## Monitor

Observes operational activities.

Typical responsibilities include:

- event monitoring;
- workflow supervision;
- exception detection;
- alert generation.

---

## Communicator

Interacts with people or external systems.

Typical responsibilities include:

- conversation;
- reporting;
- notifications;
- status updates.

---

# Role Composition

An AI Agent may perform multiple roles simultaneously.

Example:

Coordinator

+

Planner

+

Reviewer

Organizations may define additional composite roles.

---

# Dynamic Role Assignment

Agent roles may change during execution.

Role assignment may depend on:

- workflow;
- business domain;
- permissions;
- organizational policy;
- operational context.

---

# Governance

Organizations may restrict roles according to governance policies.

Examples include:

- only Executors may invoke production tools;
- only Reviewers may approve AI-generated outputs;
- only Coordinators may delegate work.

---

# Relationship to Other Specifications

Agent Roles interact with:

- Agent
- Agent Lifecycle
- Multi-Agent Collaboration
- Tools
- Workflows
- Memory

---

# Independence

The Agent Roles specification does not prescribe:

- agent architectures;
- orchestration frameworks;
- LLM providers;
- implementation technologies.

---

# Conformance

A compliant implementation shall:

- assign at least one operational role to every AI Agent;
- preserve role assignments;
- support governed role changes;
- maintain auditability.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

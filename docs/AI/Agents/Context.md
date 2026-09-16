<!-- nav:start -->
[Docs](../../README.md) / [AI](../README.md) / [Agents](README.md) / Context

[← Back](Agent.md) · [↑ Up](README.md) · [Next →](Multi-Agent%20Collaboration.md)

---
<!-- nav:end -->

# Context

**Document ID:** AI-Agents-05

**Status:** Informative

**Version:** 0.2

**Last Updated:** 16 September 2026

---

# Purpose

This document keeps the place of Context in the Agents reading path. Context is defined in `AI/Context/Overview.md` (`AI-Context-00`), which this document does not restate.

Until 16 September 2026 this document carried a verbatim copy of `AI/Context/Overview.md` under its own Document ID, recorded as `OBS-001` and decided through `CAND-001` in `Governance/ADR-Candidates.md`: the Agents section does not own a description of Context. This document therefore defines nothing and imposes no requirement.

---

# Where Context Is Defined

- `AI/Context/Overview.md`: the Context Specification, with its definition, design principles, sources, governance and conformance.
- `AI/Context/Context.md`: the Context concept.
- `AI/Context/Context Assembly.md`: how a Context is assembled.
- `AI/Context/Context Lifecycle.md`: the lifecycle of a Context.
- `AI/Context/Context Optimization.md`: how a Context is optimized.

An AI Agent's relation to Context is stated where the Agent is defined: `AI/Agents/Agent.md` lists Context among the things an AI Agent may interact with and Context Profile among its optional attributes, and `AI/Agents/Multi-Agent Collaboration.md` defines Shared Context.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |
| 0.2 | 16 September 2026 | Body replaced with a reference to `AI/Context/Overview.md`, per `CAND-001` (Decided 16 September 2026) and `OBS-001`; Status changed from Draft to Informative. Path, Document ID and reading-path position unchanged. |

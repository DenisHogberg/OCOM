<!-- nav:start -->
[Docs](../README.md) / [Memory](README.md) / Confidence

[↑ Up](README.md) · [Next →](Evidence%20Overlay.md)

---
<!-- nav:end -->

# Confidence

**Document ID:** Memory-04

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines the Confidence Model within the OCOM Memory Specification.

Confidence represents the estimated reliability of a Memory Record based on available evidence, provenance, and verification.

Confidence enables AI Agents and business systems to distinguish between assumptions, observations, and verified operational knowledge.

---

# Definition

Confidence is a measurable assessment of the likelihood that a Memory Record accurately represents reality.

Confidence is metadata associated with a Memory Record and shall not replace evidence or business validation.

---

# Design Principles

The Confidence Model shall:

- support explainable AI;
- remain evidence-based;
- evolve over time;
- support governance decisions;
- support write-back policies;
- remain independent of implementation technologies.

---

# Confidence Sources

Confidence may be influenced by:

- evidence quality;
- number of supporting sources;
- source reliability;
- human verification;
- historical consistency;
- business rules;
- AI reasoning.

---

# Confidence Levels

The OCOM Specification defines four standard confidence levels.

## Low

Characteristics:

- weak evidence;
- limited observations;
- AI inference only;
- requires verification.

---

## Medium

Characteristics:

- multiple observations;
- partially verified;
- reasonable reliability;
- suitable for operational use with caution.

---

## High

Characteristics:

- strong evidence;
- multiple trusted sources;
- operationally reliable;
- suitable for business decisions.

---

## Verified

Characteristics:

- explicitly confirmed;
- authoritative source;
- governed;
- considered trusted organizational knowledge.

Verified confidence does not imply absolute truth, only organizational verification.

---

# Confidence Score

Implementations may additionally represent confidence numerically.

Example:

- 0.00–1.00
- 0–100%

The numeric model is implementation-specific.

---

# Confidence Evolution

Confidence may increase when:

- additional evidence is collected;
- independent sources agree;
- humans verify the information;
- business systems confirm the record.

Confidence may decrease when:

- evidence is removed;
- contradictory evidence appears;
- information becomes outdated;
- verification expires.

---

# Relationship to Evidence

Confidence shall not exist without supporting evidence.

Evidence explains why confidence exists.

Confidence summarizes the estimated reliability of that evidence.

---

# Relationship to Governance

Organizations may define governance policies based on confidence.

Examples include:

- low confidence requires review;
- medium confidence requires confirmation;
- verified confidence may permit automatic operational use.

---

# Auditability

Changes to confidence shall record:

- previous value;
- new value;
- reason for change;
- supporting evidence;
- timestamp;
- actor.

---

# Independence

The Confidence Model does not prescribe:

- scoring algorithms;
- statistical methods;
- machine learning models;
- probability calculations.

Organizations remain free to implement their own confidence estimation methods.

---

# Conformance

A compliant implementation shall:

- associate confidence with Memory Records;
- preserve confidence history;
- support confidence evolution;
- maintain links between confidence and evidence;
- preserve auditability.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 20 July 2026 | Initial draft |

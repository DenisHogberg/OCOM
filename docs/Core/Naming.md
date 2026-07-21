<!-- nav:start -->
[Docs](../README.md) / [Core](README.md) / Naming

[← Back](Modeling-Rules.md) · [↑ Up](README.md) · [Next →](Principles.md)

---
<!-- nav:end -->

# Naming

**Document ID:** Core-05

**Status:** Draft

**Version:** 0.1

**Last Updated:** 20 July 2026

---

# Purpose

This document defines naming conventions used throughout the specification.

Consistent naming improves readability, interoperability, and semantic stability.

---

# General Rules

Names shall be:

- unique;
- descriptive;
- unambiguous;
- implementation-independent.

---

# Entity Names

Entity names shall use singular nouns.

Examples:

Customer

Invoice

Payment

Order

---

# Domain Names

Domain names shall represent operational responsibility.

Examples:

Sales

Finance

Compliance

Support

---

# Workflow Names

Workflow names shall describe operational intent.

Examples:

Register Customer

Approve Payment

Create Invoice

---

# State Names

State names shall describe observable conditions.

Examples:

Created

Pending

Approved

Completed

Archived

---

# Attribute Names

Attribute names shall be descriptive and implementation-independent.

Examples:

Registration Date

Amount

Currency

Status

---

# Prohibited Naming

The specification discourages:

- abbreviations;
- vendor-specific terminology;
- database field names;
- implementation details.

---

# Conformance

All names defined within this specification shall follow these rules.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
|0.1|20 July 2026|Initial draft|

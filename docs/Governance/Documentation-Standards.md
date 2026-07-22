<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Documentation Standards

[← Back](Documentation-Debt.md) · [↑ Up](README.md) · [Next →](Governance-Manifest.md)

---
<!-- nav:end -->

# Documentation Standards

**Document ID:** GOV-STANDARDS-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 July 2026

---

# Purpose

This document captures the formatting and structural conventions already established and consistently followed across the OCOM Specification. It is the single source of truth for how documentation is written, reviewed, and checked by the CDKO.

It describes existing, observed practice. It does not introduce new rules that existing documents would fail to meet.

---

# Normative Language

Normative documents consistently use "shall" for mandatory requirements, "may" for optional behavior, and "should" for recommendations — consistent with RFC 2119-style usage, though not currently cited explicitly in the specification text.

---

# RFC / ISO Style Elements Already in Use

- Every normative or informative document carries a metadata block: Document ID, Status, Version, Last Updated.
- Every document ends with a Revision History table.
- Documents are organized into named sections (Purpose, Definition, Design Principles, Conformance, etc.) rather than free-form prose.
- "Status: Informative" is used consistently for non-normative, illustrative material (Examples, Reference Architecture).

---

# Markdown Rules

- Headings use ATX style (`#`, `##`) only.
- Lists use `-` exclusively; no mixed bullet markers.
- Tables always include a header row and a separator row.
- Code fences use triple backticks; diagrams rendered as text use the `text` language tag.

---

# Naming Rules

Four filename conventions currently coexist across the specification (Title Case With Spaces, snake_case/UPPER-suffix, PascalCase, kebab-case). This is a tracked, open item — see `Documentation-Debt.md`, GAP-001. Two filenames are fixed by convention regardless of section: `README.md` (index) and `Overview.md` (full section content, where applicable).

---

# Cross-References

The specification favors prose references to other documents by name ("...is defined by the Identity specification") over inline Markdown hyperlinks within normative body text. Navigation-level links (breadcrumb, Up/Back/Next, README indexes) are the only consistently hyperlinked elements.

---

# Tables

Used for: Revision History (mandatory, every document), Attribute schemas (Mandatory/Optional Attributes), and structured comparisons. Column count must match between header, separator, and every row.

---

# Examples

Example documents (`Examples/iGaming/`) are marked `Status: Informative` and explicitly state they are non-normative.

---

# Diagrams

ASCII diagrams are used for layered/sequential relationships, inside ```text``` code fences. The dominant style uses `│` and `▼` connectors for vertical flows.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 July 2026 | Initial capture of existing conventions |

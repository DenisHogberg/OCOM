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

Normative documents consistently use "shall" for mandatory requirements, "may" for optional behavior, and "should" for recommendations — consistent with RFC 2119 / RFC 8174 usage, cited explicitly since 20 August 2026 in `Core/Manifest.md`'s Normative Language section, the single authoritative definition of the key words; lowercase forms are equivalent by that section's own convention.

---

# RFC / ISO Style Elements Already in Use

- Every normative or informative document carries a metadata block: Document ID, Status, Version, Last Updated.
- Every document ends with a Revision History table.
- Documents are organized into named sections (Purpose, Definition, Design Principles, Conformance, etc.) rather than free-form prose.
- "Status: Informative" is used consistently for non-normative, illustrative material (Examples, Reference Architecture).

---

# Status Taxonomy

No prior document defined these four `Status` values precisely — this section makes existing, observed usage explicit, per this document's own stated purpose. It does not change any document's Status; it only states what the values already mean in practice.

- **Draft** — normative, currently in force, subject to revision before a final version. The default status for accepted content under `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Governance/` (process documents), `Lifecycles/`, `AI/`, `Domains/`, `Entities/`, and `Specification/`. A `Draft` document's requirements apply now; "Draft" describes its maturity, not its authority.
- **Informative** — non-normative. Explanatory, illustrative, or analytical material that imposes no requirement of its own. Used for `Examples/`, `Reference Architecture/`, and every `Governance/` analysis document (Concept Papers, Architecture Discussions, Audits, this document itself). A Core-scope decision (e.g. `Constitution-Step0-Summary.md` Decision 4, on `Entities/`) does not, by itself, change a document's Status — Status tracks whether the document's own content is normative, which is a separate question from Constitution §9 Core scope.
- **Reserved** — a named section or attribute inside an otherwise-`Draft` document, explicitly deferred to a future version. A section-level marker, not a whole-document Status value: the document around it remains `Draft`/normative; only the reserved part is absent by design (example: `Memory/Evidence Overlay.md`'s "Reserved Sections," tracked as `FW-001`).
- **Planned** — content that does not yet exist, tracked in `Documentation-Debt.md`'s Future Work table or stated directly in a stub file (example: `Workflows/README.md`, "Status: Planned for future versions"). Distinguished from `Reserved`: `Reserved` names a gap inside an existing document; `Planned` may have no document at all yet.

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
| 0.1 | 20 August 2026 | Added Status Taxonomy section, defining Draft/Informative/Reserved/Planned precisely from existing observed usage — per `Governance/Publication-Model.md` |
| 0.1 | 20 August 2026 | Corrected the Draft-directory list on independent review: it omitted `Domains/`, `Entities/`, and `Specification/`, the three largest Draft populations in the repository, contradicting the section's own descriptive claim. Removed the `Entities/`-as-Informative-example clause after `Entities/Overview.md`'s Status was reverted to Draft |
| 0.1 | 5 September 2026 | Normative Language: replaced the stale statement that RFC 2119 is not cited explicitly (it has been cited in `Core/Manifest.md` since 20 August 2026). |

# OCOM Specification v0.2 — Executive Overview

**Document ID:** SPEC-00

**Status:** Informative

**Version:** 0.2

---

Most organizations describe themselves through the systems they happen to use — an ERP here, a CRM there, a spreadsheet no one remembers the origin of. When a platform changes, the description of the organization changes with it, even though the organization itself did not.

OCOM (Object-Centric Operating Model) takes a different starting point. It describes an organization through the things it manages and the relationships between them — independently of the software used to run it. A customer, a payment, a campaign, a case: each is described once, consistently, in a way that stays valid whether it lives in one system today and a different one next year.

The result is a shared operational language. The same description can be read by a person trying to understand how a business works, by a system that needs to exchange data reliably with another system, and by software that reasons about the organization's operations — without three different, drifting versions of "what a customer is" or "what happens when an order is cancelled."

This is not a product, a database schema, or a piece of software. It is a specification: a set of concepts and rules for describing operational reality, meant to remain stable while the technology underneath changes.

If that idea is useful to you — as an architect trying to bring order to a fragmented landscape, an engineer building something that needs to interoperate, or someone simply trying to understand how a business is put together — the rest of this document walks through it in order: what the specification actually requires (Chapter 1), the principles it is built on (Chapter 2), its core vocabulary (Chapter 3), and the detailed models that follow from it (Chapters 4–8).

---

*This document is informative. It introduces no terms and imposes no requirements — definitions and requirements begin in Chapter 1.*

*Source: synthesized from `Core/Manifest.md` (Abstract, Purpose, Motivation) and the root `README.md`. No new claims beyond those documents.*

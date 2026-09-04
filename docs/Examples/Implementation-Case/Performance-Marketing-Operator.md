<!-- nav:start -->
[Docs](../../README.md) / [Examples](../README.md) / [Implementation-Case](README.md) / Performance-Marketing Operator

[↑ Up](README.md)

---
<!-- nav:end -->

# OCOM Implementation Case: Adopting OCOM in a Performance-Marketing Operator

**Document ID:** EXAMPLES-CASE-PERFMKT-01

**Status:** Informative (illustrative, non-normative)

**Version:** 0.2

**Last Updated:** 12 August 2026

---

# Purpose

This document tells the story of *how* an organization adopted OCOM, in the order it actually happened. It is not a feature tour and it is not a mapping table. It follows the sequence of decisions a real rollout goes through, the problem that forced each step, and what changed once the step landed.

It is a Reference Case. It demonstrates the model, it does not extend it. Every concept named here is defined normatively in the Core Vocabulary or at the Models tier of the specification and only referenced from this document.

The organization is **fictional**. "Meridian" is a placeholder for any performance-marketing operator, used purely for illustration. No real company, brand, or person is named or implied.

Distilled from real rollouts conducted under NDA; the organization, names, and details are fictionalized.

---

# The Organization Before OCOM

Meridian is a digital performance-marketing operator. It sources offers from advertisers, resells them to traffic partners under its own terms, tracks the conversions that come back, and settles payouts on both sides.

At the start it ran on four disconnected systems, and that is the whole reason OCOM was adopted.

| System | What lived there |
|---|---|
| Messaging | partner conversations, keyed by a chat handle |
| CRM | contact names and billing emails |
| Tracker | numeric affiliate IDs, clicks, conversions |
| Finance | payouts, typed into a spreadsheet by hand |

The same partner existed as four different things, and no system was authoritative. Reconciling a single payout meant a human guessing that a chat handle, an email, an affiliate ID, and a spreadsheet row were all the same partner. Every report was a negotiation about whose copy was right.

The goal of the rollout was not "adopt a data model." It was: **one governed source that a human, the tracker, the API, and an AI assistant all read the same way.**

---

# How OCOM Was Rolled Out

The rollout followed the grain of the model's own design principles: Evidence Before Belief, and governance built in from the start. In practice that dictated the order. You cannot govern what you cannot identify, and you cannot trust what you cannot evidence, so Identity and Events came first, and the commercial layer only after them.

## Phase 1: Identity first

**Problem.** Nothing could be reconciled because nothing had a single name.

**What was applied.** The very first OCOM Object introduced was **Identity**. Every partner, advertiser, and offer was given one canonical identifier (a partner became `PRT-00417`) and the four system-specific names became aliases that resolve to it.

**The decision that mattered.** Resolution was made **deterministic and evidence-based, never automatic**. A new alias is linked to an existing Identity only on evidence. When there is no confident match, the system does not invent a merge and does not silently create a duplicate: it surfaces the ambiguity for a human. This one rule is what stopped the old chaos from re-entering through the new model.

**Outcome.** For the first time a partner was one thing. The chat history, the tracker ID, and the payout row now hung off a single Object.

## Phase 2: Events and evidence, not current state

**Problem.** The old systems stored only the latest value. Nobody could answer *why* a balance or a status was what it was.

**What was applied.** Meridian started recording **Events** as an immutable operational history: partner registered, deal signed, conversion confirmed, payout released. Communications were captured with their full envelope (who, when, which channel) as evidence attached to the Identity from Phase 1.

**The decision that mattered.** Nothing was allowed to be asserted without an Event behind it. This is Evidence Before Belief made literal: a claim about the business must resolve to recorded evidence, or it is not made.

**Outcome.** State became explainable. "This partner is approved" now resolves to the event that approved it.

## Phase 3: One computed source of truth

**Problem.** The finance spreadsheet stored balances directly, so two copies always disagreed.

**What was applied.** A single governed ledger of money events became the source of truth. **Balance was never stored, always computed** from the events.

**The decision that mattered.** A derived number is never written back as if it were a fact. It is a projection of the events, so it cannot drift from them. This is the memory-first architecture from the specification, applied to money.

**Outcome.** There was exactly one balance for a partner, and it always matched its own history.

## Phase 4: Registries

**Problem.** Two people could create two "same" partners, and often did.

**What was applied.** The collections became governed **Registries**: a Partner Registry, an Offer Catalog, an Advertiser Registry. Each has membership and uniqueness rules, not just rows.

**Outcome.** Onboarding a partner or an offer went through governed membership. Duplicates stopped at the door instead of being cleaned up later.

## Phase 5: The commercial layer (Contract, Policy, Constraint)

**Problem.** Deal terms lived in people's heads and in chat messages.

**What was applied.** Deals became **Contract** Objects binding a Partner and an Offer under explicit terms (model, rate, geo, cap, payment). The rules a deal must obey became **Policies** (KYC before first payout, confirm before pay). The hard limits it can never cross became **Constraints** (`partner_payout <= advertiser_rate`, daily cap).

**The decision that mattered.** A Deal that violates a Constraint cannot be activated. Governance is enforced at the object, not left to a reviewer's memory.

**Outcome.** Commercial terms became auditable and machine-checkable instead of tribal knowledge.

## Phase 6: Ownership by role

**Problem.** When a staff member left, the partners they handled went dark.

**What was applied.** **Ownership** of each Partner and Deal was assigned to a **role**, not a person.

**Outcome.** Responsibility survived staff changes. Every Object had a clear, current owner.

## Phase 7: Freezing the core

**Problem.** Once it worked, the temptation was to keep adding new concepts for every edge case.

**What was applied.** The Core was frozen. New concepts stopped being added directly. A candidate now has to be observed in real usage, written up as a Reference Case, and pass an Architecture Observation review before anything changes. This is governance built in from the start, applied to the model itself.

**Outcome.** The model stayed small. The whole business still fits inside the thirteen Core Vocabulary terms and the Models tier, which is exactly the point of this document.

## Phase 8: Everything else is a projection

**Problem.** The old systems each held their own copy, and copies drift.

**What was applied.** The internal admin views, the JSON API, the knowledge graph, and the AI assistant's context were all rebuilt as **projections** of the same governed Objects, never as parallel stores.

**Outcome.** A human and an AI assistant reading a partner read the same record. There is no second copy to drift.

---

# What the Sequence Teaches

The order was not arbitrary, and it is the most transferable part of this case.

1. **Identity is the keystone.** Until things have one canonical identity, nothing downstream can be trusted. It has to be first.
2. **Deterministic resolution beats clever resolution.** Refusing to auto-merge on weak evidence is what keeps the model clean over time.
3. **Evidence before state.** Record events, compute the current view. Never store a conclusion you cannot re-derive.
4. **Govern the model last, and hard.** Freeze the core once it works, so it stays small.

A team adopting OCOM can reuse this sequence directly: Identity, then Events, then a computed source of truth, then Registries, then the commercial and governance layers, then projections.

---

# Appendix: The Result at a Glance

After the rollout, every core OCOM concept has a concrete counterpart in the business.

| OCOM concept | In this operator it is | Concrete example |
|---|---|---|
| **Object** | any governable unit of the business | a Partner, an Offer, a Deal, an Invoice |
| **Identity** | the one canonical handle a thing keeps across every system | `PRT-00417` behind a chat handle, an email, and a tracker ID |
| **Metadata** | descriptive and management attributes | an Offer's geo, vertical, daily cap, status |
| **Relationship** | a governed, two-way association | "Partner promotes Offer" |
| **Reference** | a directed pointer, lighter than a Relationship | a Conversion points to the Offer that produced it |
| **Registry** | a governed collection with membership rules | the Partner Registry, the Offer Catalog |
| **Classification** | categories assigned to an Object | Offer vertical = finance; Partner tier = A |
| **Capability** | a governed ability an Object provides | a Partner delivers mobile app-install traffic in Tier-1 EU |
| **Contract** | a governed agreement between Objects | the payout deal: CPA 180, geo DE, NET-30 |
| **Policy** | governed rules applied to Objects | "KYC before first payout" |
| **Constraint** | a specific restricting condition | `partner_payout <= advertiser_rate` |
| **Ownership** | assigned responsibility | an account-management role owns the Partner |
| **Organization** | an independent participant, itself an Object | the Partner company, the Advertiser, Meridian itself |

---

# Related Specifications

- Vocabulary: Object, Identity, Metadata, Relationship, Reference, Registry, Classification, Capability, Contract, Policy, Constraint, Ownership, Organization
- Specification: Executive Overview, Normative (Chapters 1 to 8)
- Examples: Affiliate Example, Campaign Example, Payment Example

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | 12 August 2026 | Initial structural mapping. |
| 0.2 | 12 August 2026 | Reframed as a phased adoption journey. |

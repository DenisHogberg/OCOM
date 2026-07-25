<!-- nav:start -->
[Docs](../README.md) / [Adoption](README.md) / First Pilot

[← Back](Getting%20Started.md) · [↑ Up](README.md) · [Next →](FAQ.md)

---
<!-- nav:end -->

# Running a First Pilot

**Document ID:** ADOPTION-FIRST-PILOT-01

**Status:** Informative

**Version:** 0.1

---

## Purpose

A first pilot exists to answer one question — does modeling our operations as OCOM Entities actually help — without betting the whole organization on the answer. Keep it small enough to finish in weeks, not quarters.

## Suggested Shape

| Dimension | Suggested bound | Why |
|---|---|---|
| Team | 5–10 people | Small enough to agree on definitions without a formal process. |
| Domain | One | A Domain is a bounded area of responsibility by design *(see `Models/Domain.md`)* — a pilot should stay inside one. |
| Entities | 10–20 | Enough to be a real model, not so many that defining them becomes the whole project. |
| Events | A handful, only the significant ones | Events record facts, they do not need to capture everything from day one *(see `Models/Event.md`)*. |
| KPIs | A small, obvious set | Just enough to notice whether the model reflects reality. |

## What to Deliberately Leave Out

- **Governance process** — `docs/Governance/` exists to govern how the *specification itself* evolves. A pilot team modeling its own Domain does not need to run that process; it only matters if you think you've found a gap in the Core (see Common Mistakes).
- **AI or Memory** — neither is required to have a valid OCOM model. They are separate, optional layers *(see `docs/Specification/03 Core Concepts.md`, "What Is Deliberately Not Introduced Here")*.
- **Cross-Domain integration** — one Domain, one pilot. Relationships to other Domains can wait.
- **Tooling and automation** — a pilot can be a shared document. OCOM does not prescribe implementation technology *(see `Core/Principles.md`, Principle 6)*.

## Suggested Steps

1. Pick the one Domain your pilot team already owns.
2. List the things that Domain manages. Keep only the ones with a clear owner and a clear lifecycle — that shortlist is your 10–20 Entities.
3. For each Entity, write the minimal definition from `Getting Started.md` §4: Identifier, Name, Domain, Owner, Attributes, State, Lifecycle.
4. Draw each Entity's Lifecycle as a small state diagram, four or five states.
5. Name the two or three Events per Entity that actually matter to the business, not every possible occurrence.
6. Pick one or two KPIs that would tell you, honestly, whether the model is useful.
7. Run it for a few weeks against real work. See what breaks, what's missing, and what nobody actually looks at.

## What Success Looks Like

Not "we finished modeling the Domain." Success is: the team can point at the model and explain their own work more consistently than before, and they can name specific places where the model was wrong or incomplete. Both outcomes are useful — a pilot that surfaces real gaps is doing its job.

If a gap looks like it's in OCOM itself, rather than in how your pilot modeled it, that's a Reference Case — see `docs/Governance/Standard Evolution Methodology.md`, not something to solve by inventing new rules inside the pilot.

---

*Source: this document restates, and does not extend, `Models/Domain.md`, `Models/Event.md`, `Core/Principles.md`, and `docs/Governance/Standard Evolution Methodology.md`. Team size and Entity count are suggested bounds for a first attempt, not normative requirements.*

# Common Adoption Mistakes

**Document ID:** ADOPTION-MISTAKES-01

**Status:** Informative

**Version:** 0.1

---

## Modeling Processes Instead of Objects

The instinct, especially for teams used to process mapping, is to start by drawing the flow of work. OCOM starts somewhere else: "Every operational concept shall be represented through identifiable entities. Entities are the primary building blocks of the operational model" *(`Core/Principles.md`, Principle 2)*. If your first diagram has verbs as the main boxes and nouns as labels on the arrows, you've modeled a process, not an OCOM Entity. Start from the things — Entity, Domain, Lifecycle — and let Workflow describe what acts on them afterward *(`Models/Workflow.md`)*.

## Trying to Describe the Whole Company at Once

A model that tries to cover every Domain on day one tends to produce twenty shallow definitions instead of five useful ones. Nothing about OCOM requires — or rewards — starting big; Evolvability is a stated Design Principle precisely so you don't have to *(`Core/Principles.md`, Principle 10)*. See `First Pilot.md` for a deliberately bounded starting scope.

## Mixing Object and UI

An Entity is "an identifiable and governable element that exists within the operational model" *(`Meta/Object.md`)* — it is not a screen, a form, or a dashboard layout. The specification's own Scope explicitly excludes "user interface design" from what OCOM defines *(`Core/Manifest.md`, Scope)*. If an attribute only exists to control how something is displayed, it likely does not belong on the Entity.

## Adding New Concepts Without Governance

It is tempting, mid-pilot, to invent a new primitive when the existing vocabulary feels like it doesn't quite fit. Don't — that decision is not the pilot team's to make locally. `docs/Governance/Standard Evolution Methodology.md` exists for exactly this situation: a suspected gap becomes a Reference Case, then an Observation, and only after repeated, independent evidence does it become a candidate for an actual Core change. A single project's convenience is explicitly not sufficient grounds: "The existence of a single implementation problem SHALL NOT justify architectural expansion" *(`docs/Governance/Standard Evolution Methodology.md`, Principle of Minimal Evolution)*.

## Breaking the Boundaries of Core

Related to the above, but narrower: redefining an existing concept locally instead of raising a gap through Governance. If your team's definition of "Domain" or "Lifecycle" quietly diverges from `Models/Domain.md` or `Models/Lifecycle.md` to make a specific case easier, you no longer have one OCOM model — you have a private dialect that happens to reuse OCOM's words. "Each operational concept shall have a single authoritative definition within the model" *(`Core/Principles.md`, Principle 7 — Single Source of Truth)*. If the existing definition genuinely doesn't fit, that's a signal for Governance, not a license to redefine it locally.

---

*Source: this document restates, and does not extend, `Core/Manifest.md`, `Core/Principles.md`, `Meta/Object.md`, `Models/Workflow.md`, and `docs/Governance/Standard Evolution Methodology.md`.*

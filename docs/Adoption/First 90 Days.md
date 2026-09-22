<!-- nav:start -->
[Docs](../README.md) / [Adoption](README.md) / First 90 Days

[↑ Up](README.md)

---
<!-- nav:end -->

# The First 90 Days

**Document ID:** ADOPTION-FIRST-90-DAYS-01

**Status:** Draft

**Version:** 0.1

**Last Updated:** 22 September 2026

---

> **Status note.** This document is filed as `CAND-028` and stays Draft, unpublished on ocom.uno, until the Chief Architect records a Decision on it. It restates `First Pilot.md` as a plan with weeks, responsibility slots, artifacts and exit criteria; it adds no rule and no number of its own.

## Purpose

`First Pilot.md` says what a first pilot covers and what it leaves out. An operations director who says yes on a Monday needs the next question answered: who does what, by which week, producing what, and how the pilot knows it is done. This document is that plan. Every artifact it names already exists in the specification or its tooling; every rule it cites is stated elsewhere; the effort arithmetic at the end is the adopter's own numbers in a form that makes them checkable.

It is Informative. Where it says less than the documents it restates, they prevail.

## Who does what

The specification defines no job titles and says so (`Meta/Ownership.md`, Independence). It does require four responsibilities that a pilot has to place on named people, and a pilot that leaves one of them unplaced stalls at the week where it is needed.

| Responsibility | What the specification requires | Who usually holds it | Needed from |
|---|---|---|---|
| Domain owner | Every Domain has a defined owner responsible for governance and operational consistency (`Models/Domain.md`). The pilot runs inside one Domain, so this is the pilot's sponsor: the person who decides what the Domain is responsible for and signs the definitions. | The head of the function the Domain covers | Week 1 |
| Modeller | Writes the seven-field definitions, the Lifecycles and the Events with the Entity owners; produces the export and the Representation Map; runs the suite. One person for a pilot of 10 to 20 Entities. | An architect, an analyst, or the team lead | Week 1 |
| Entity owners | Every Entity has exactly one responsible owner (`Models/Entity.md`, `CAND-025`); other responsible parties are further Ownership records, not second owners. The owner confirms the definition, the States and the Events of their Entity. | The people who already answer for the things being modelled | Week 2 |
| Reviewer | Records the named judgments the suite cannot make mechanically, in a Reviewer Record (`Governance/Conformance-Test-Suite.md`, Section 3); the report carries their name. A reviewer outside the pilot team makes the Test Report more than self-validation; the suite does not check that, the publisher says it. | Internal audit, enterprise architecture, or a peer team | Week 7 |

## Weeks 1 to 2: the definitions

**Do.** Pick the one Domain the team already owns (`First Pilot.md`, step 1). List what the Domain manages and keep the 10 to 20 things with a clear owner and a clear lifecycle (step 2). For each, write the seven fields of `Getting Started.md` Section 4: Identifier, Name, Domain, Owner, Attributes, State, Lifecycle (step 3).

**Artifact.** The definitions, in whatever the team writes in: a shared document is enough (`First Pilot.md`, What to Deliberately Leave Out).

**Exit criteria.** Every Entity has an Identifier the Domain assigns and does not reuse, one responsible Owner who has confirmed the definition, and the Domain named as its primary Domain. Two things stop the week from closing: an Entity nobody will own, and an Entity two Domains claim. Both are findings, not failures; the first is dropped or reassigned, the second is decided by the Domain owner and recorded (`Domains/Common/Domain Governance.md`, Conflict Resolution).

## Weeks 3 to 6: the model that runs

**Do.** Draw each Entity's Lifecycle as four or five States with the transitions between them (step 4); name the two or three Events per Entity that matter (step 5). Then produce the export: the Reference Serialization (`Reference Serialization.md`) is one JSON file whose `entities`, `lifecycles` and `events` collections carry exactly these things, and its Representation Map can be used unchanged. Run the suite:

```text
python3 tools/conformance/validate.py \
  --model export.json \
  --map representation-map.md \
  --statement conformance-statement.md \
  --report report.md
```

**Artifact.** The export, its map, a Conformance Statement with the five fields `Language/Conformance.md` lists, and the first Test Report.

**Exit criteria.** The report shows no Fail. A Fail is the suite doing its job: an Entity without an owner, a State change its Lifecycle forbids, an identifier used twice. Fix the model, not the report. Pending rows are normal at this point; they are the Statements a reviewer decides in week 7 and the evidence a snapshot cannot carry.

## Weeks 7 to 12: the model against real work

**Do.** Use the model for the Domain's actual work for at least four weeks: record the Events as they happen, move Entities through their States, and note every place the model was wrong, incomplete, or never looked at (step 7). In week 7 the reviewer examines the evidence for the Statements the suite left pending and records a Reviewer Record; the suite reads it and the report carries the judgments under the reviewer's name. Pick the one or two KPIs the pilot chose in week 1 (step 6) and read them before and after.

**Artifact.** The final Test Report, the Reviewer Record, the readout of the KPIs, and the list of gaps.

**Exit criteria.** `First Pilot.md` says what success is: the team explains its own work more consistently than before and can name where the model was wrong. In this plan that is three things on the table at the end of week 12: a report with a named reviewer, a readout of the chosen KPIs with a before and an after, and the gap list sorted into three piles, the model was wrong (fix it), the pilot modelled it wrong (fix the pilot), the specification is missing something (a Reference Case, `Governance/Standard Evolution Methodology.md`, not a rule invented inside the pilot).

## Planning arithmetic

The specification states no effort figures, and this document does not supply any: the figures depend on how well the Domain already knows what it manages. What it supplies is the count of artifacts the plan produces, so that an adopter's own estimate per artifact turns into a plan that can be checked against what the pilot then measures.

| Artifact | Count for a pilot of N Entities | Your estimate each | Your total |
|---|---|---|---|
| Seven-field Entity definitions, confirmed by their owners | N (10 to 20) | | |
| Lifecycles of four or five States | N | | |
| Events that matter | 2N to 3N | | |
| The export and its map | 1 (the map unchanged if the Reference Serialization is used) | | |
| Suite runs and fixes until no Fail | as many as the model needs | | |
| Reviewer Record | 1, covering the pending Statements the reviewer can decide | | |
| KPI readout, before and after | 1 or 2 | | |

The first pilot's measured totals, kept next to this table, are the number the next pilot plans with. That is the whole point of writing the estimate down before starting.

## What this plan does not promise

It does not promise an operational result; the specification claims none with a number, and this document does not either. It does not name the KPI; the pilot does. It does not make the weeks a rule: a pilot that finishes the definitions in a week or takes four is not less conformant, because conformance is decided by the suite against the model and not by the calendar. It does not replace `First Pilot.md`, which it restates in a different order.

## Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 22 September 2026 | First draft, filed as `CAND-028`: `First Pilot.md` as a twelve-week plan with four responsibility slots, artifacts, exit criteria and an arithmetic for the adopter's own effort estimate. Unpublished until decided. |

---

*Source: this document restates, and does not extend, `Adoption/First Pilot.md`, `Adoption/Getting Started.md`, `Adoption/Reference Serialization.md`, `Models/Domain.md`, `Models/Entity.md`, `Domains/Common/Domain Governance.md`, `Governance/Conformance-Test-Suite.md` and `Governance/Standard Evolution Methodology.md`. It adds no requirement and no figure.*

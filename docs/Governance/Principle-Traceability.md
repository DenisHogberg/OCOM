<!-- nav:start -->
[Docs](../README.md) / [Governance](README.md) / Principle Traceability

[← Back](Knowledge-Map.md) · [↑ Up](README.md) · [Next →](Requirement-Register.md)

---
<!-- nav:end -->

# Principle Traceability

**Document ID:** GOV-TRACEABILITY-01

**Status:** Informative

**Version:** 0.1

**Last Updated:** 22 September 2026

---

# Purpose

`Core/Constitution.md` states fourteen Canonical Principles. Until this document existed, no text said which rule carries which principle, so a reader could not tell what a principle obliges an implementation to do, and an implementation could satisfy every mandatory requirement of the reading path while contradicting most of the Constitution. `AO-074` records that gap and asks for exactly one thing: a table that names, principle by principle, the rules that carry it and the Test that could fail.

This is that table. It changes no rule, adds no concept and creates no obligation. It reports what the corpus contains as of the date above.

---

# How to Read It

Each principle has one block. The block quotes the principle verbatim, records a verdict, says whether any binding carrier is inside the scope of Core Conformance, lists every occurrence found outside `Core/Constitution.md`, and names one Test that could fail, or states plainly that none could.

A **carrier** is a place in the corpus where the principle appears. Each is classified:

- **binding rule**: a sentence carrying shall, shall not or must, in a normative document, whose violation is observable in an implementation or in its exported model.
- **permission**: a may-sentence that makes something explicitly allowed. It obliges nothing, and it forecloses the opposite reading, which is what a principle about extensibility needs.
- **restatement**: the principle repeated as prose or inside a Definition. It binds nothing.
- **definition**: a term the principle uses is defined, with no obligation attached.
- **reserved**: the term is listed in `Core/Terminology.md` under Reserved Terms, which exists to record that no document defines it.
- **absent**: nothing outside the Constitution.

The **verdict** follows from the carriers, not from intent:

- **carried by rules**: at least one binding rule carries the principle.
- **partly carried**: a binding rule carries part of the principle and leaves a named part uncarried.
- **restated only**: the principle appears, and nothing binds.
- **reserved**: the principle rests on a term the specification itself records as undefined.
- **no occurrence**: the principle appears nowhere outside the Constitution.

**In conformance scope** answers a narrower question. `Language/Conformance.md` defines Core Conformance as support for all mandatory language requirements, `Specification/08 Conformance.md` names where those requirements are found, and `Governance/Requirement-Register.md` enumerates them from the twenty-two documents Chapters 4 to 6 compile, which `CAND-021` records as the reading adopted for the suite. A binding rule in `Memory/`, `Language/`, `AI/`, `Domains/` or `Entities/` binds nothing at any conformance level, which `AO-032` records. A row therefore says **yes** only when a binding carrier sits inside those twenty-two documents.

Where a carrier is a Statement of the Requirement Register, the row names its alias, so the rule, the Test and the claim share one identifier.

---

# What This Document Does Not Do

It does not decide anything. A verdict of "no occurrence" is not an instruction to write a rule: some principles may be design commitments that no implementation obligation could express, and recording which ones those are is a decision for the Chief Architect, not for this table.

It does not promote the Test column to a specification. `Governance/Conformance-Test-Suite.md` defines the five Test kinds and the register defines the Statements; the Test sentence here is what a Test would read if one were written, and no suite runs it today.

It does not touch the Constitution. `AO-074` is explicit that the map belongs beside the Knowledge Map and the Requirement Register rather than inside the constitutional text, so that the map can be corrected without amending a principle.

---

# Method

Fourteen independent passes, one per principle, each searching `Core/`, `Meta/`, `Models/`, `Memory/`, `Language/`, `Lifecycles/` and `AI/`, with `Domains/` and `Entities/` spot checked, for the principle's vocabulary, its synonyms and the mechanism it would need. Each pass was then verified adversarially by a second pass that re-read every cited line, re-checked every alias against the register, searched with different terms for occurrences the first pass missed, and challenged the verdict. Revision-history rows and editorial notes are excluded from carriers throughout: a mention added by governance work is not machinery.

`tools/governance/principle_traceability.py --check` re-verifies the mechanical half of every claim in this document against the corpus: that each cited line carries its quoted text verbatim, that each named alias exists in the Requirement Register and carries the quoted sentence, that every row classified as a binding rule quotes a sentence carrying shall or must, and that each of the fourteen principles has exactly one block quoting it verbatim. The judgment is not checkable and is not checked; the evidence under it is.

---

# The Table

Fourteen principles: 7 partly carried, 3 carried by rules, 2 restated only, 2 reserved. Binding carriers inside the scope of Core Conformance: no for 7, partly for 3, yes for 4.

---

## Principle 1: Object-Centric Reality

**Principle:** Object is the universal abstraction of OCOM. Everything represented by OCOM is expressed as an Object or as a specialization of Object.

**Verdict:** partly carried

**In conformance scope:** partly

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Meta/Organization.md:114` | binding rule | REQ-META-ORGANIZATION-002 | support Organization as a specialization of Object; |
| `docs/Meta/Object.md:224` | permission | REQ-META-OBJECT-016 | Specifications may extend Object but shall preserve its core characteristics. |
| `docs/Meta/Object.md:51` | binding rule | REQ-META-OBJECT-001 | Every Object shall: |
| `docs/Language/Syntax.md:82` | binding rule |   | contain identifiable Objects; |
| `docs/Meta/Object.md:222` | restatement |   | All managed concepts defined by the specification are specializations of Object. |
| `docs/Meta/Overview.md:105` | restatement |   | Every managed element within the specification is represented as an Object. |

**Test:** A Presence Test over the exported model and its Representation Map, reading every element the Map identifies as an Organization and failing when it is not presented as a specialization of Object carrying Object's core characteristics (REQ-META-ORGANIZATION-002), and an Invariant Test on REQ-META-OBJECT-001 failing when a managed Object exports no identity, no metadata or no way to participate in relationships.

**Note:** The obligations on things already known to be Objects are binding and in scope. The principle's own claim, that everything OCOM represents is an Object, is carried only by prose: `Meta/Object.md:222` states it and no Statement obliges an implementation to represent every operational concept as an Object, so a model that keeps half its concepts outside the Object hierarchy fails no Test. `Meta/Object.md:224` permits a derived specification to extend Object while preserving its core characteristics, and the register tiers that Statement optional rather than mandatory, so it adds nothing to a Core Conformance claim.

---

## Principle 2: Domain-Owned Identity

**Principle:** An entity becomes an OCOM Object only when its identity belongs to the operational domain rather than to the implementation. Operational role takes precedence over ontological classification. The same entity may be represented differently depending on the operational question being answered.

**Verdict:** partly carried

**In conformance scope:** yes

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Entity.md:61` | binding rule | REQ-MODELS-ENTITY-003 | Identity shall not depend on implementation technology. |
| `docs/Models/Domain.md:91` | binding rule | REQ-MODELS-DOMAIN-008 | Every Entity shall belong to exactly one primary Domain. |
| `docs/Models/Model.md:59` | binding rule | REQ-MODELS-MODEL-004 | No element shall exist without a defined operational meaning. |
| `docs/Meta/Identity.md:121` | binding rule | REQ-META-IDENTITY-010 | implementation technology. |
| `docs/Meta/Classification.md:132` | binding rule | REQ-META-CLASSIFICATION-012 | Changing a Classification shall not change Object Identity. |
| `docs/Language/Identifier Syntax.md:39` | definition |   | The same Identity may be represented by different identifiers in different implementation environments. |

**Test:** A Presence Test failing when an exported Entity carries no identity or no primary Domain (REQ-MODELS-ENTITY-001, REQ-MODELS-DOMAIN-008), and the Review Test the Test Suite itself uses as its worked example, REQ-MODELS-ENTITY-003, recording Review Fail when an Entity's identifier is the implementation's own handle, a row id, a file path or a vendor record URL.

**Note:** Sentence one is carried in both halves. Sentences two and three, that operational role takes precedence over ontological classification and that the same entity may be represented differently depending on the question asked, have no Statement anywhere, so nothing binds or tests them.

---

## Principle 3: Evidence Before Belief

**Principle:** Every operational fact must be traceable to Evidence. Evidence and Metadata are independent concepts and must never be merged.

**Verdict:** partly carried

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Memory/Memory Record.md:197` | binding rule |  | A Memory Record shall reference at least one Evidence Record. |
| `docs/Memory/Evidence Overlay.md:110` | binding rule |  | Confidence shall not exist without supporting Evidence. |
| `docs/Memory/Overview.md:48` | binding rule |   | Memory shall preserve evidence. |
| `docs/Memory/Confidence.md:35` | binding rule |   | Confidence is metadata associated with a Memory Record and shall not replace evidence or business validation. |
| `docs/Memory/Evidence Overlay.md:37` | restatement |   | A Memory Record without Evidence is a belief, and Constitution Principle 3 does not permit a retained belief without traceable Evidence. |
| `docs/Core/Terminology.md:265` | restatement |   | An Evidence Record is the retained account of why a Memory Record holds its value: what was observed or asserted, from which source, and how reliable that source was judged to be at the time. |

**Test:** A Presence Test failing on any exported Memory Record with no reference to an Evidence Record (`Memory/Memory Record.md:189`). It cannot run under Core Conformance, because no `Memory/` Statement is in the requirement set; it becomes runnable only under a Profile Declaration whose Included Set adds the two Memory documents.

**Note:** The first clause has real machinery, all of it outside the conformance scope. The second clause, that Evidence and Metadata are never merged, has no carrier at all: the Independence section of `Memory/Evidence Overlay.md` that would state it is reserved, and `Memory/Confidence.md:35` keeps confidence from standing in for evidence without saying anything about Metadata.

---

## Principle 4: Immutable Memory

**Principle:** Memory is append-only. A Memory Entry is immutable after creation. Corrections are represented as new Memory Entries, never by modifying historical records.

**Verdict:** carried by rules

**In conformance scope:** partly

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Event.md:97` | binding rule | REQ-MODELS-EVENT-010 | An Event shall never be modified after creation. |
| `docs/Models/Event.md:99` | binding rule | REQ-MODELS-EVENT-011 | Corrections shall be represented by new Events. |
| `docs/Memory/Overview.md:46` | binding rule |   | Memory shall be append-only. |
| `docs/Memory/Memory Record.md:260` | binding rule |  | never modify a Memory Record after creation, and represent corrections as new Memory Records; |
| `docs/Memory/Evidence Overlay.md:46` | binding rule |  | be append-only; |
| `docs/Memory/Retention.md:200` | binding rule |  | preserve audit history; |
| `docs/Memory/Memory Record.md:265` | binding rule |   | be able to demonstrate, to a party holding a Memory Record together with its identity and nothing else, that the record has not been altered since its creation. |

**Test:** An Invariant Test over Events: export the model, correct an already-exported Event, re-export, and fail when an identifier from the first export carries different content in the second or when the correction produced no additional Event (REQ-MODELS-EVENT-010, REQ-MODELS-EVENT-011). The same Test over Memory Records can fail only outside Core Conformance.

**Note:** This is the one principle whose full statement is carried by binding rules at two tiers. The last carrier is the contradiction `AO-069` records: the same Memory tier that requires append-only records also requires an implementation to support controlled deletion.

---

## Principle 5: Memory Precedes Knowledge

**Principle:** Knowledge is always derived from Memory. World Models are always derived from Knowledge. Memory → Knowledge → World Model.

**Verdict:** restated only

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/AI/Knowledge/Knowledge.md:35` | restatement |   | Per Constitution Principle 5, Knowledge is always derived from Memory |
| `docs/Core/Terminology.md:241` | restatement |   | Defined in `AI/Knowledge/Knowledge.md`; derived from Memory per `Core/Constitution.md` Principle 5 and `CAND-014`. |
| `docs/Entities/Overview.md:115` | restatement |   | The current state of an Entity is not a Memory Record |
| `docs/Core/Terminology.md:266` | reserved |   | **World Model** (Canonical Principles 5 and 6): its relationship to Memory and Knowledge is decided by `CAND-014` Layer 1; the document itself is Layer 2 and not yet authored. |
| `docs/AI/Knowledge/Knowledge Sources.md:129` | binding rule |   | Every Knowledge Source shall preserve: |

**Test:** No Test of any kind can fail today. The nearest candidate is an Invariant Test failing on the first Knowledge item whose provenance chain terminates anywhere other than a Memory Record, and it has no Statement to anchor to: the strongest provenance obligation in the corpus, the last carrier above, binds a Knowledge Source and never names Memory.

**Note:** The restatement in `AI/Knowledge/Knowledge.md` is the Layer 1 integration of `CAND-014`, and it fixed a contradiction rather than creating an obligation. The World Model, the chain's third stage, is a Reserved term whose document is Layer 2 and not yet authored.

---

## Principle 6: Reconstructability

**Principle:** Knowledge and World Models must always be reproducible from Memory without requiring access to the original external systems.

**Verdict:** restated only

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/AI/Knowledge/Knowledge.md:35` | restatement |   | it must be reproducible from Memory without requiring access to the original external systems |
| `docs/Core/Terminology.md:266` | reserved |   | **World Model** (Canonical Principles 5 and 6): its relationship to Memory and Knowledge is decided by `CAND-014` Layer 1; the document itself is Layer 2 and not yet authored. |
| `docs/Memory/Memory Record.md:168` | definition |  | Status is a derived projection, not a stored attribute of a Memory Record |

**Test:** No Test of any kind can fail today. An Invariant Test would read a derivation record linking each Knowledge item to the Memory Records it was computed from, and no Statement requires one to exist; a Declaration Test asking a claimant to assert reconstructability would be unfalsifiable rather than a test.

**Note:** `AO-073` records this row in full. Reproducibility language does appear elsewhere in `AI/`, for Prompts and Evaluation Criteria, but about those subjects rather than about Knowledge and Memory, so it carries nothing here.

---

## Principle 7: Separation of Dimensions

**Principle:** Architecture, Capability and Autonomy are independent dimensions. Progress in one dimension never implies progress in another.

**Verdict:** reserved

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Core/Terminology.md:267` | reserved |   | **Autonomy level** (Canonical Principles 7 and 14): no scale is defined anywhere; tracked as `AO-067`. |
| `docs/Domains/AI/AI_Policies.md:181` | binding rule |   | autonomous execution shall remain policy-controlled; |

**Test:** No Test of any kind can fail today: no Statement names the three dimensions or forbids inferring one from another. A Declaration Test could be written once a scale exists, failing when a claimant reports one combined level or derives an Autonomy claim from a Core Conformance result.

**Note:** Autonomy is Reserved in `Core/Terminology.md` and tracked by `AO-067`. The single shall-sentence in the corpus that constrains autonomous behaviour sits in a Domain profile and governs execution under policy, not the independence of the three dimensions.

---

## Principle 8: Static Before Dynamic

**Principle:** Static World Modelling precedes Dynamic World Modelling.

**Verdict:** reserved

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Core/Terminology.md:269` | reserved |   | **Static World Modelling** and **Dynamic World Modelling** (Canonical Principle 8): defined nowhere; tracked as `AO-068`. |

**Test:** No Test of any kind can fail today. `Governance/Conformance-Test-Suite.md` states that the suite does not test the World Model, and neither Static nor Dynamic World Modelling is defined anywhere, so a Declaration Test would have nothing to check a declaration against.

**Note:** Both terms the principle orders are Reserved, tracked by `AO-068`. This is the only principle whose entire vocabulary the specification records as undefined.

---

## Principle 9: Domain-Neutral Core

**Principle:** The OCOM Core must never contain domain-specific knowledge. The Core must never branch on organization-specific concepts or business entities. Domain knowledge belongs only to configuration, data and adapters. For the purposes of this principle, the Core is determined by semantic invariance across industries rather than by directory location: it is whatever would remain unchanged if OCOM were adopted by an organization in a completely different industry.

**Verdict:** partly carried

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Domains/Common/Domain Architecture.md:187` | binding rule |   | Specialization shall not modify the core architectural concepts defined by this specification. |
| `docs/Meta/Overview.md:72` | binding rule |   | remain domain independent; |
| `docs/Language/Identifier Syntax.md:70` | binding rule |   | remain independent of business meaning; |
| `docs/Meta/Overview.md:50` | restatement |   | The Meta specification does not define business-specific models or operational behavior. |
| `docs/Domains/Overview.md:23` | restatement |   | genuine borderline case |

**Test:** A Review Test reading the exported model and failing when a reviewer finds a Core-tier type, attribute or branch whose meaning would change in another industry. It cannot be built today: not one of the 335 Statements says domain independent, neutral or industry, so the Test has no Statement to bind to.

**Note:** The carriers are real and none is in the requirement set: `Meta/Overview.md` is not among the twenty-two documents Chapters 4 to 6 compile, and `Domains/` binds nothing at any conformance level. `Constitution-Step0-Summary.md` Decision 4 already called `Domains/` a borderline case for this principle and declined a blanket ruling.

---

## Principle 10: Extensibility Over Enumeration

**Principle:** Business vocabularies are extensible. Organizations extend OCOM through specialization rather than modification of the Core.

**Verdict:** partly carried

**In conformance scope:** yes

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Model.md:91` | binding rule | REQ-MODELS-MODEL-008 | Extensions shall preserve compatibility with the core model. |
| `docs/Meta/Metadata.md:229` | binding rule | REQ-META-METADATA-015 | allow Metadata extension; |
| `docs/Meta/Classification.md:53` | binding rule | REQ-META-CLASSIFICATION-001 | be extensible; |
| `docs/Language/Syntax.md:147` | permission |   | Organizations may extend the language by introducing: |
| `docs/Meta/Object.md:224` | permission | REQ-META-OBJECT-016 | Specifications may extend Object but shall preserve its core characteristics. |
| `docs/Language/Conformance.md:110` | binding rule |   | Extensions shall not invalidate conformance with the core specification. |
| `docs/Meta/Object.md:224` | binding rule | REQ-META-OBJECT-016 | Specifications may extend Object but shall preserve its core characteristics. |

**Test:** An Invariant Test on REQ-MODELS-MODEL-008 failing when an extension changes the meaning of a core model element, and a Presence Test on REQ-META-METADATA-015 failing when the Representation Map shows Metadata as a closed set that only a schema change can extend.

**Note:** Read this row against `AO-076`. Two of the in-scope carriers, `Meta/Classification.md:53` and the Metadata twin at `Meta/Metadata.md:55`, are among the twenty-five mandatory requirements that entry records as unfailable: a reviewer asked whether Classification "is extensible" has no observation that would justify a fail. The extensibility half of this principle is therefore carried in form more strongly than in substance. The second half, that organizations extend rather than modify the Core, is carried by permissions rather than obligations: `Language/Syntax.md:147` allows extension by addition, and `Meta/Object.md:224`, which the register tiers optional rather than mandatory, allows extension of Object only while its core characteristics survive.

---

## Principle 11: Structural Isolation

**Principle:** A component's actual capability must never exceed its defined responsibility. The excess capability must be verifiably absent rather than merely unused by convention. This principle states a property that must hold and can be checked; it does not prescribe an implementation architecture, and it holds regardless of the technology used to achieve it.

**Verdict:** partly carried

**In conformance scope:** yes

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Workflow.md:98` | binding rule | REQ-MODELS-WORKFLOW-008 | A Workflow shall only perform State Transitions permitted by the Lifecycle of the affected Entity. |
| `docs/Meta/Capability.md:219` | binding rule | REQ-META-CAPABILITY-018 | define Capabilities explicitly; |
| `docs/Meta/Capability.md:134` | binding rule | REQ-META-CAPABILITY-012 | Dependency relationships shall remain explicit and traceable. |
| `docs/Meta/Organization.md:55` | binding rule | REQ-META-ORGANIZATION-001 | participate in the operational model only through governed Relationships; |
| `docs/AI/Tools/Tool Governance.md:120` | binding rule |   | Access shall follow the principle of least privilege. |
| `docs/Models/Domain.md:109` | definition |   | Operational boundaries define the scope of responsibility of a Domain. |

**Test:** A Transition Test on REQ-MODELS-WORKFLOW-008 failing when a recorded State change is not one the affected Entity's Lifecycle permits, and a Presence Test on REQ-META-CAPABILITY-018 failing when the exported model declares no Capabilities for a component that exercises them.

**Note:** What is carried is bounded capability: a Workflow may do only what a Lifecycle permits, Capabilities are declared explicitly and their dependencies stay traceable, an Organization connects only through governed Relationships. What is not carried is the principle's own test, that excess capability be verifiably absent rather than merely unused. No document requires an implementation to expose its actual capability surface against its defined responsibility, so capability that is present and unused passes everything the corpus binds.

---

## Principle 12: Grounded Reasoning

**Principle:** Statements derived from Memory and Knowledge must remain distinguishable from interpretation, inference or expert opinion. The system must communicate provenance and confidence appropriately.

**Verdict:** carried by rules

**In conformance scope:** no

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Memory/Overview.md:47` | binding rule |   | Memory shall preserve provenance. |
| `docs/Memory/Confidence.md:199` | binding rule |   | associate confidence with Memory Records; |
| `docs/Memory/Confidence.md:35` | binding rule |   | Confidence is metadata associated with a Memory Record and shall not replace evidence or business validation. |
| `docs/AI/Context/Context Optimization.md:120` | binding rule |   | Optimization shall preserve provenance for every Context element. |
| `docs/AI/Knowledge/Knowledge Sources.md:95` | binding rule |   | System-generated Knowledge shall preserve system provenance. |
| `docs/Core/Terminology.md:268` | reserved |   | **Provenance** (Canonical Principle 12): three AI documents carry a Provenance section and none defines the term; tracked as `AO-068`. |

**Test:** A Presence Test failing when an exported Memory Record carries no Memory Type, a type outside the enumeration Fact, Observation and Inference, no provenance, or no confidence linked to Evidence. It can fail only under a Profile Declaration that adds the Memory documents, because no Core Conformance Test reaches any of these Statements.

**Note:** Both halves of the principle have binding rules, and not one of them is in the requirement set. Provenance, the word the principle rests on, is Reserved in `Core/Terminology.md` and tracked by `AO-068`: five documents oblige an implementation to preserve it and none defines it.

---

## Principle 13: Adaptation Flows Toward the Model

**Principle:** Implementations adapt to OCOM. OCOM never adapts to implementation-specific constraints.

**Verdict:** carried by rules

**In conformance scope:** yes

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Entity.md:61` | binding rule | REQ-MODELS-ENTITY-003 | Identity shall not depend on implementation technology. |
| `docs/Models/Model.md:103` | binding rule | REQ-MODELS-MODEL-009 | depend on implementation technologies. |
| `docs/Meta/Identity.md:121` | binding rule | REQ-META-IDENTITY-010 | implementation technology. |
| `docs/Lifecycles/Lifecycles.md:47` | binding rule | REQ-LIFECYCLES-005 | shall remain independent of implementation technologies. |
| `docs/Core/Modeling-Rules.md:81` | binding rule |   | Operational models shall not depend on implementation technologies. |
| `docs/Core/Principles.md:75` | restatement |   | Implementations adapt to the operational model; the operational model never adapts to implementation-specific constraints (Constitution §13). |

**Test:** A Review Test on REQ-MODELS-ENTITY-003, the Statement the Test Suite names as its own Review example: Review Fail when an exported Entity's identity is the implementation's technology handle, so that replacing the store would change the identity. An Invariant Test on REQ-MODELS-MODEL-009 can fail mechanically when an exported element names a storage engine, table, column or endpoint.

**Note:** Carried by real machinery at three tiers and inside the requirement set. The obligation runs in one direction only, on the model and on implementations; nothing states what happens when an implementation cannot comply, which is where the principle's second sentence would bite.

---

## Principle 14: Professional Responsibility

**Principle:** OCOM augments professional decision-making. Responsibility remains with the designated human role unless a higher Autonomy level has been explicitly delegated.

**Verdict:** partly carried

**In conformance scope:** partly

| Carrier | Kind | Alias | Quote |
|---|---|---|---|
| `docs/Models/Workflow.md:120` | binding rule | REQ-MODELS-WORKFLOW-012 | Where a Workflow's outcome depends on specialized professional judgment, the Workflow shall not reach that judgment itself. |
| `docs/Models/Entity.md:67` | binding rule | REQ-MODELS-ENTITY-004 | Every Entity shall have one responsible owner. |
| `docs/Meta/Ownership.md:122` | binding rule | REQ-META-OWNERSHIP-009 | Shared ownership shall preserve accountability. |
| `docs/AI/Overview.md:179` | binding rule |   | an AI Agent shall preserve context and route the matter to the responsible organizational function rather than reaching the professional conclusion itself |
| `docs/Core/Principles.md:119` | binding rule |   | OCOM shall not substitute for professional expertise |
| `docs/Core/Terminology.md:267` | reserved |   | **Autonomy level** (Canonical Principles 7 and 14): no scale is defined anywhere; tracked as `AO-067`. |

**Test:** A Review Test on REQ-MODELS-WORKFLOW-012 and REQ-MODELS-WORKFLOW-013: Review Fail when a Workflow whose outcome is a judgment reserved to a professional function records that judgment as its own outcome, or records it without preserving context and assigning the review to a named responsible function.

**Note:** The first half is carried, and one carrier is in scope. The second half is not: responsibility stays with the designated human role "unless a higher Autonomy level has been explicitly delegated", and no document defines an Autonomy level, a scale for it, or what a designated human role is. `Meta/Ownership.md` requires accountability to survive delegation, which is adjacent but silent about autonomy.

---

# What the Table Shows

Three principles are carried by binding rules, seven in part, two are restated and bind nothing, and two rest on terms the specification itself records as undefined.

The sharper number is the second one. Only four of the fourteen have a binding carrier inside the requirement set of Core Conformance, three more have one in part, and seven have none at all. An implementation can therefore satisfy every mandatory requirement of Chapters 4 to 6, publish a conformance claim, and contradict half the Constitution without failing anything. That is not a gap in the principles; it is a gap between where the principles live and where conformance is measured, which `AO-032` records from the other side.

The pattern is not random. The principles with the least machinery inside scope are the ones that carry the architecture's weight: Evidence Before Belief, Memory Precedes Knowledge, Reconstructability and Grounded Reasoning are carried, when they are carried at all, by `Memory/` and `AI/`, and Chapters 4 to 6 compile neither. The principles that are fully carried, Immutable Memory at the Event tier and Adaptation Flows Toward the Model, are the ones whose subject matter happens to sit in `Meta/` and `Models/`.

Three things follow, none of them decided here. A profile is the existing mechanism for the first: a claimant who wants the Memory principles to bind can add those documents to an Included Set under `CAND-002`, and the table names exactly which documents that takes. A Reference Case is the mechanism for the second: the rows whose Test column says nothing can fail are the shortest list of what a real implementation would have to demonstrate for the principle to become testable. And the Chief Architect decides the third: which principles are design commitments that no implementation obligation could express, so that the record stops presenting fourteen equally binding rules when four of them bind and two are undefined.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 0.1 | 18 September 2026 | First table, produced by fourteen independent passes over the canonical tiers, each adversarially verified, per the recommendation of `AO-074`. Checked by `tools/governance/principle_traceability.py`. |
| 0.1 | 19 September 2026 | How to Read It now cites `Language/Conformance.md` for the definition of Core Conformance and names the twenty-two-document enumeration as the suite's reading, per `CAND-021`. |
| 0.1 | 21 September 2026 | Memory-tier line references re-pointed after `CAND-023` and `CAND-024` were integrated; the Principle 3 row that recorded Evidence's Definition as reserved now carries the Definition itself; Principle 4 gains the integrity guarantee of `Memory Record.md` as a binding-rule carrier. |
| 0.1 | 22 September 2026 | Two carriers re-pointed after a paragraph was added above each (`Meta/Organization.md`, `CAND-027`; `Memory/Retention.md`, `AO-085`); no row added or removed. |

# Test Report

**Run on:** 20 September 2026

**Implementation:** OCOM reference export, library lending example

**Specification version claimed:** 1.0

**Model:** `docs/Examples/Conformance/model.json`  **Representation Map:** `docs/Examples/Conformance/representation-map.md`

**Published by:** the party that ran the suite. A report published by the claimant is self-validation; `Conformance-Test-Suite.md` Section 4 says the suite does not tell the two apart and the publisher does.

---

## Summary

| | Count |
|---|---|
| Mandatory Tests | 187 |
| Pass | 37 |
| Fail | 0 |
| Awaiting a reviewer or evidence the export does not carry | 150 |
| Not Applicable, dispositioned Descriptive | 1 |

**Core Conformance: not established.** Section 3 establishes it when every mandatory Test is Pass or Review Pass. 0 mandatory Test(s) fail and 150 await a reviewer or evidence this export does not carry.

---

## Reference Integrity

63 field value(s) were resolved against the 32 identities this export declares, and every one of them names a record it carries. Fields holding prose, and a Reference's target, which may legitimately name another system, are not resolved.

---

## Results

| Test | Document | Kind | Class | Outcome | Why |
|---|---|---|---|---|---|
| REQ-META-OBJECT-001 | `Meta/Object.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OBJECT-003 | `Meta/Object.md` | Presence | mandatory | Pass | 24 object record(s) carry identity, each distinct |
| REQ-META-OBJECT-004 | `Meta/Object.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OBJECT-008 | `Meta/Object.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OBJECT-009 | `Meta/Object.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OBJECT-018 | `Meta/Object.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-ORGANIZATION-001 | `Meta/Organization.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-ORGANIZATION-002 | `Meta/Organization.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-001 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-002 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-003 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-005 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-007 | `Meta/Identity.md` | Presence | mandatory | pending | the Statement states a condition rather than an element (when an object is created); a reviewer decides it |
| REQ-META-IDENTITY-008 | `Meta/Identity.md` | Invariant | mandatory | Pass | 32 identities, each carried by exactly one record |
| REQ-META-IDENTITY-009 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-010 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-012 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-IDENTITY-013 | `Meta/Identity.md` | Presence | mandatory | Pass | 24 object record(s) carry identity |
| REQ-META-IDENTITY-014 | `Meta/Identity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-002 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-006 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-007 | `Meta/Metadata.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-008 | `Meta/Metadata.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-009 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-010 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-011 | `Meta/Metadata.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-013 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-METADATA-015 | `Meta/Metadata.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-001 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-002 | `Meta/Classification.md` | Presence | mandatory | Pass | 3 classification record(s) carry identifier, classification name, classification type |
| REQ-META-CLASSIFICATION-007 | `Meta/Classification.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-CLASSIFICATION-008 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-011 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-012 | `Meta/Classification.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-CLASSIFICATION-013 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-014 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-015 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CLASSIFICATION-016 | `Meta/Classification.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-CLASSIFICATION-017 | `Meta/Classification.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-001 | `Meta/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-002 | `Meta/Relationship.md` | Presence | mandatory | Pass | 2 relationship record(s) carry identifier, source object, target object, relationship type |
| REQ-META-RELATIONSHIP-007 | `Meta/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-010 | `Meta/Relationship.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-RELATIONSHIP-011 | `Meta/Relationship.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-013 | `Meta/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-014 | `Meta/Relationship.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-015 | `Meta/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-RELATIONSHIP-016 | `Meta/Relationship.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-RELATIONSHIP-017 | `Meta/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-001 | `Meta/Reference.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-002 | `Meta/Reference.md` | Presence | mandatory | Pass | 1 reference record(s) carry source object, target object, direction |
| REQ-META-REFERENCE-009 | `Meta/Reference.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-010 | `Meta/Reference.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-011 | `Meta/Reference.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-013 | `Meta/Reference.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-REFERENCE-014 | `Meta/Reference.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-015 | `Meta/Reference.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-016 | `Meta/Reference.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REFERENCE-017 | `Meta/Reference.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-REFERENCE-018 | `Meta/Reference.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-002 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-003 | `Meta/Capability.md` | Presence | mandatory | Pass | 2 capability record(s) carry identifier, name, purpose |
| REQ-META-CAPABILITY-010 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-012 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-014 | `Meta/Capability.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-015 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-016 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CAPABILITY-018 | `Meta/Capability.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-002 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-003 | `Meta/Policy.md` | Presence | mandatory | Pass | 2 policy record(s) carry identifier, name, purpose, scope, effective date |
| REQ-META-POLICY-009 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-012 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-015 | `Meta/Policy.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-016 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-017 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-018 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-019 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-POLICY-020 | `Meta/Policy.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-POLICY-021 | `Meta/Policy.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-001 | `Meta/Contract.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-002 | `Meta/Contract.md` | Presence | mandatory | Pass | 1 contract record(s) carry identifier, purpose, participants, scope, effective date |
| REQ-META-CONTRACT-006 | `Meta/Contract.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-013 | `Meta/Contract.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-014 | `Meta/Contract.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-016 | `Meta/Contract.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONTRACT-017 | `Meta/Contract.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-CONTRACT-018 | `Meta/Contract.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-002 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-003 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-004 | `Meta/Constraint.md` | Presence | mandatory | Pass | 1 constraint record(s) carry identifier, name, purpose, scope |
| REQ-META-CONSTRAINT-009 | `Meta/Constraint.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-011 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-013 | `Meta/Constraint.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-015 | `Meta/Constraint.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-016 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-017 | `Meta/Constraint.md` | Presence | mandatory | pending | the Statement's subject is not a type the Representation Map declares |
| REQ-META-CONSTRAINT-018 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-019 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-CONSTRAINT-020 | `Meta/Constraint.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-CONSTRAINT-021 | `Meta/Constraint.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-001 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-002 | `Meta/Ownership.md` | Presence | mandatory | pending | the Statement's subject is not a type the Representation Map declares |
| REQ-META-OWNERSHIP-008 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-009 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-011 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-012 | `Meta/Ownership.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-014 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-015 | `Meta/Ownership.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-OWNERSHIP-016 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-017 | `Meta/Ownership.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-018 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-019 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-020 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-021 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-OWNERSHIP-022 | `Meta/Ownership.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-OWNERSHIP-023 | `Meta/Ownership.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-001 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-002 | `Meta/Registry.md` | Presence | mandatory | Pass | 1 registry record(s) carry identifier, name, purpose, registry scope, registered object types, ownership |
| REQ-META-REGISTRY-005 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-006 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-009 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-010 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-011 | `Meta/Registry.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-012 | `Meta/Registry.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-013 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-014 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-015 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-META-REGISTRY-016 | `Meta/Registry.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-META-REGISTRY-017 | `Meta/Registry.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-001 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-002 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-003 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-004 | `Models/Model.md` | Presence | mandatory | pending | the Statement's subject is not a type the Representation Map declares |
| REQ-MODELS-MODEL-005 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-006 | `Models/Model.md` | Transition | recommended | pending | 4 of this Statement's 4 parts are undecided (Workflow) |
| REQ-MODELS-MODEL-008 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-MODEL-009 | `Models/Model.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-001 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-002 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-003 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-004 | `Models/Entity.md` | Presence | mandatory | Pass | 3 entity record(s) carry responsible owner |
| REQ-MODELS-ENTITY-006 | `Models/Entity.md` | Presence | mandatory | pending | the Statement's subject is not a type the Representation Map declares |
| REQ-MODELS-ENTITY-007 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-008 | `Models/Entity.md` | Transition | mandatory | Pass | 3 Entities each occupy exactly one State defined by their Lifecycle |
| REQ-MODELS-ENTITY-009 | `Models/Entity.md` | Presence | mandatory | Pass | 3 entity record(s) carry lifecycle |
| REQ-MODELS-ENTITY-011 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-ENTITY-012 | `Models/Entity.md` | Presence | mandatory | Pass | 2 relationship record(s) carry source, target, type, cardinality |
| REQ-MODELS-ENTITY-014 | `Models/Entity.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-001 | `Models/Domain.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-002 | `Models/Domain.md` | Presence | mandatory | Pass | 1 domain record(s) carry identifier, each distinct |
| REQ-MODELS-DOMAIN-003 | `Models/Domain.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-004 | `Models/Domain.md` | Presence | mandatory | Pass | 1 domain record(s) carry operational responsibility |
| REQ-MODELS-DOMAIN-005 | `Models/Domain.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-006 | `Models/Domain.md` | Presence | mandatory | Pass | 1 domain record(s) carry owner responsible for governance and operational consistency |
| REQ-MODELS-DOMAIN-007 | `Models/Domain.md` | Invariant | mandatory | Pass | 4 governed records each name an owner |
| REQ-MODELS-DOMAIN-008 | `Models/Domain.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-010 | `Models/Domain.md` | Invariant | mandatory | Pass | 3 Entities each name one primary Domain, and no Entity type is governed twice |
| REQ-MODELS-DOMAIN-012 | `Models/Domain.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-MODELS-DOMAIN-013 | `Models/Domain.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-DOMAIN-014 | `Models/Domain.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-RELATIONSHIP-001 | `Models/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-RELATIONSHIP-002 | `Models/Relationship.md` | Presence | mandatory | pending | the Statement's list items are not separated in the source, so its elements cannot be read |
| REQ-MODELS-RELATIONSHIP-006 | `Models/Relationship.md` | Presence | mandatory | Pass | 2 relationship record(s) carry cardinality |
| REQ-MODELS-RELATIONSHIP-008 | `Models/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-RELATIONSHIP-010 | `Models/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-RELATIONSHIP-012 | `Models/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-RELATIONSHIP-013 | `Models/Relationship.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-001 | `Models/Event.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-002 | `Models/Event.md` | Presence | mandatory | Pass | 4 event record(s) carry identifier, each distinct |
| REQ-MODELS-EVENT-003 | `Models/Event.md` | Presence | mandatory | pending | the Statement states a condition rather than an element (time at which it occurred); a reviewer decides it |
| REQ-MODELS-EVENT-004 | `Models/Event.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-MODELS-EVENT-005 | `Models/Event.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-008 | `Models/Event.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-MODELS-EVENT-009 | `Models/Event.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-010 | `Models/Event.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-MODELS-EVENT-011 | `Models/Event.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-012 | `Models/Event.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-EVENT-013 | `Models/Event.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-STATE-001 | `Models/State.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-STATE-002 | `Models/State.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-STATE-003 | `Models/State.md` | Transition | mandatory | Pass | 3 Lifecycle(s) define exactly one initial State, each among their own States |
| REQ-MODELS-STATE-006 | `Models/State.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-STATE-008 | `Models/State.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-STATE-010 | `Models/State.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-WORKFLOW-001 | `Models/Workflow.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-WORKFLOW-003 | `Models/Workflow.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-WORKFLOW-004 | `Models/Workflow.md` | Presence | mandatory | Pass | 2 workflow record(s) carry required inputs |
| REQ-MODELS-WORKFLOW-006 | `Models/Workflow.md` | Presence | mandatory | Pass | 2 workflow record(s) carry expected outputs |
| REQ-MODELS-WORKFLOW-008 | `Models/Workflow.md` | Transition | mandatory | Pass | 3 recorded State change(s) compared, every one permitted by the Lifecycle |
| REQ-MODELS-WORKFLOW-009 | `Models/Workflow.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-WORKFLOW-011 | `Models/Workflow.md` | Invariant | mandatory | Pass | 2 Workflow(s) perform only Transitions their Entity's Lifecycle defines |
| REQ-MODELS-WORKFLOW-012 | `Models/Workflow.md` | Invariant | mandatory | pending | deciding this prohibition needs evidence the export does not carry (a history, or a refusal record) |
| REQ-MODELS-WORKFLOW-013 | `Models/Workflow.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-WORKFLOW-015 | `Models/Workflow.md` | Invariant | mandatory | pending | 2 of this Statement's 4 parts are undecided (modify undefined Entities) |
| REQ-MODELS-LIFECYCLE-001 | `Models/Lifecycle.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-LIFECYCLE-002 | `Models/Lifecycle.md` | Transition | mandatory | Pass | 3 Lifecycle(s) each belong to exactly one Entity; 3 Lifecycle(s) define exactly one initial State, each among their own States; 3 Lifecycle(s) define 12 States between them; 3 Life |
| REQ-MODELS-LIFECYCLE-003 | `Models/Lifecycle.md` | Transition | mandatory | Pass | 3 Lifecycle(s) define exactly one initial State, each among their own States |
| REQ-MODELS-LIFECYCLE-005 | `Models/Lifecycle.md` | Presence | mandatory | pending | the Statement states a condition rather than an element (meaning within the lifecycle); a reviewer decides it |
| REQ-MODELS-LIFECYCLE-007 | `Models/Lifecycle.md` | Transition | mandatory | Pass | 3 Lifecycle(s) define 15 Transitions, every endpoint a State they declare |
| REQ-MODELS-LIFECYCLE-009 | `Models/Lifecycle.md` | Transition | mandatory | Pass | 3 Entities each occupy exactly one State defined by their Lifecycle |
| REQ-MODELS-LIFECYCLE-010 | `Models/Lifecycle.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-LIFECYCLE-011 | `Models/Lifecycle.md` | Review | recommended | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-MODELS-LIFECYCLE-012 | `Models/Lifecycle.md` | Invariant | mandatory | pending | 1 of this Statement's 4 parts are undecided (permit ambiguous State progression) |
| REQ-LIFECYCLES-001 | `Lifecycles/Lifecycles.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| REQ-LIFECYCLES-002 | `Lifecycles/Lifecycles.md` | Transition | mandatory | Pass | 3 Lifecycle(s) define 15 Transitions, every endpoint a State they declare |
| REQ-LIFECYCLES-003 | `Lifecycles/Lifecycles.md` | Transition | mandatory | Pass | 3 recorded State change(s) compared, every one permitted by the Lifecycle |
| REQ-LIFECYCLES-004 | `Lifecycles/Lifecycles.md` | Review | mandatory | Not Applicable | dispositioned Descriptive in the Alias File |
| REQ-LIFECYCLES-005 | `Lifecycles/Lifecycles.md` | Review | mandatory | pending | awaiting a named reviewer, per the kind this Test carries |
| DECL-001 | `Language/Conformance.md` | Declaration | mandatory | pending | no procedure is bound to this clause |
| DECL-002 | `Language/Conformance.md` | Declaration | mandatory | Pass | extensions declared: none |
| DECL-003 | `Language/Conformance.md` | Declaration | mandatory | Pass | extensions declared: none |
| DECL-004 | `Language/Conformance.md` | Declaration | mandatory | Pass | the Conformance Statement names version 1.0 |
| DECL-005 | `Language/Conformance.md` | Declaration | mandatory | Pass | one version declared: 1.0 |
| DECL-006 | `Language/Conformance.md` | Declaration | mandatory | pending | decided by the outcome of every other mandatory Test, reported in the summary |

# OCOM

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21510450.svg)](https://doi.org/10.5281/zenodo.21510450)

OCOM (Object-Centric Operating Model) is an open, technology-independent operating model for organizations that describes an organization as a system of governed, interconnected objects with identity, ownership, lifecycle, and evidence.

**Website / specification:** [OCOM — the Object-Centric Operating Model specification](https://ocom.uno) · [ocom.uno](https://ocom.uno)

**Specification status:** v0.1 Core — Released · Governance & Specification v0.2 (Reading Path) — Baseline

New to OCOM? Start with [`docs/Adoption/`](docs/Adoption/README.md) — a 15–30 minute introduction. For the full normative specification, start with [`docs/Specification/`](docs/Specification/00%20Executive%20Overview.md).

## Documentation

The full specification lives in [`docs/`](docs/README.md). See [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) for a snapshot of what is stable, what is baseline, and what is still under exploration.

## Project Structure

```
docs/
├── Adoption/                — Quick Start guide, First Pilot, FAQ, Common Mistakes — start here if new
├── AI/                      — AI agents, context, evaluation, knowledge, prompts, tools
├── Core/                    — Manifest, principles, naming, versioning, modeling rules, terminology, spec governance charter
├── Domains/                 — Business domains (Affiliate, BI, CRM, Compliance, Finance, HR, Legal, Marketing, Operations, Payments, Product, Support)
├── Entities/                — Core business entities (Player, Payment, Affiliate, Wallet, Transaction, etc.)
├── Examples/                — Worked examples, including the iGaming reference scenario
├── Governance/              — How the specification itself is maintained, reviewed, and evolved (Baseline)
├── Language/                — Notation, syntax, schema, vocabulary, conformance rules
├── Lifecycles/              — Commercial, content, financial, operational, organizational lifecycles
├── Memory/                  — Layered memory, evidence overlay, retention, write-back governance
├── Meta/                    — Meta-model constructs (Object, Relationship, Capability, Policy, Contract, etc.)
├── Models/                  — Domain, entity, event, lifecycle, relationship, state, workflow models
├── Reference Architecture/  — AI, business-event, domain, enterprise, and object architecture
├── Specification/           — OCOM Specification v0.2 — sequential reading path through the normative spec (Baseline)
└── Workflows/               — Workflow specifications (planned)
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for what's completed, the current state, and future directions under exploration.

## License

Specification text (`docs/`): Creative Commons Attribution 4.0 (CC BY 4.0); see [LICENSE-docs.md](LICENSE-docs.md).
Code: Apache License 2.0; see [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

OCOM is an early-stage specification. The v0.1 Core is Released; Governance and the Specification v0.2 reading path are Baseline. "Baseline" means reviewed and frozen pending the approved change process — not that the specification is finished. Terminology, structure, and scope may still change through that process before v1.0. Content is provided as-is, without warranty.

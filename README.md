# OCOM

Object-Centric Operating Model (OCOM): A memory-first architecture for enterprise AI systems.

**Specification status:** v0.1 — Draft

## Documentation

The full specification lives in [`docs/`](docs/README.md).

## Project Structure

```
docs/
├── AI/                      — AI agents, context, evaluation, knowledge, prompts, tools
├── Core/                    — Governance, manifest, modeling rules, naming, principles, terminology, versioning
├── Domains/                 — Business domains (Affiliate, BI, CRM, Compliance, Finance, HR, Legal, Marketing, Operations, Payments, Product, Support)
├── Entities/                — Core business entities (Player, Payment, Affiliate, Wallet, Transaction, etc.)
├── Examples/                — Worked examples, including the iGaming reference scenario
├── Language/                — Notation, syntax, schema, vocabulary, conformance rules
├── Lifecycles/              — Commercial, content, financial, operational, organizational lifecycles
├── Memory/                  — Layered memory, evidence overlay, retention, write-back governance
├── Meta/                    — Meta-model constructs (Object, Relationship, Capability, Policy, Contract, etc.)
├── Models/                  — Domain, entity, event, lifecycle, relationship, state, workflow models
├── Reference Architecture/  — AI, business-event, domain, enterprise, and object architecture
└── Workflows/               — Workflow specifications (planned)
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the v0.1 → v1.0 plan.

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

OCOM is an early-stage specification (v0.1, Draft). Terminology, structure, and scope may change before v1.0. Content is provided as-is, without warranty.

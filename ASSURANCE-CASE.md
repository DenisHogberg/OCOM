# Assurance Case

Why the security claims made for this repository and for the published site are justified. Written for the OpenSSF Best Practices silver criterion `assurance_case`, and kept because the argument is useful on its own. Last reviewed 13 September 2026.

## 1. What is being protected

The project produces a specification, not software: about 400 Markdown files under `docs/`, the governance registers, and the machine-readable representations rendered from them on ocom.uno (HTML, JSON, JSON-LD, llms.txt, the knowledge API). The assets worth protecting are:

- Integrity of the canonical text: what the repository says is what the author published.
- Integrity of the published projections: what ocom.uno serves matches the canonical text and is not tampered with in transit or on the server.
- Integrity of the record about the record: versions, statuses, licences and the Publication Manifest agree with each other.
- Availability and continuity: the text survives the loss of any single account, server or person.

There is no confidential data in scope. The repository holds no credentials, no personal data and no client material, and the anonymity rule in CONTRIBUTING.md keeps it that way.

## 2. Security requirements

- C1. Only the maintainer can change the canonical text on the main branch, and every change is attributable.
- C2. Readers and machines receive the published text over an authenticated, encrypted channel, and the browser context cannot be hijacked by injected content.
- C3. Machine-readable records cannot silently disagree with the text they are derived from.
- C4. Third-party code that runs in the project's pipeline cannot change without review.
- C5. The text remains available and verifiable if GitHub, the site or the maintainer disappears.
- C6. Licensing is unambiguous for every file, so reuse carries no legal surprise.

## 3. Threat model

Threat actors: an attacker holding a stolen maintainer credential; a malicious contributor; a compromised upstream GitHub Action; a network attacker between reader and site; an attacker who finds a weakness on the site; an automated consumer (AI agent or indexer) that treats a stale or manipulated projection as truth; and plain loss of hardware, account or maintainer.

- T1. Unauthorized change to the canonical text: a push, a merged pull request, a force-push or a history rewrite.
- T2. Site compromise or impersonation: injected scripts, downgraded headers, DNS or TLS failure.
- T3. Misleading machine records: version fields, Status values or manifest commits drifting apart; projections presented as authoritative.
- T4. Supply chain: a tampered action version running in CI with write access.
- T5. Licensing ambiguity leading to withdrawal or dispute.
- T6. Loss of availability: account lockout, hosting failure, single maintainer unavailable.
- T7. Exposure of confidential or personal data through examples or records.

## 4. Trust boundaries

- B1. Maintainer workstation to GitHub: SSH keys and GitHub-enforced two-factor authentication. This is the only path that writes to main.
- B2. GitHub to CI runners: workflows run with `contents: read`. The Scorecard workflow alone holds `id-token: write`, used only to publish its result. No workflow can push.
- B3. Repository to publication engine to server: the site is rendered outside this repository by the maintainer and deployed over SSH to a server the maintainer controls. The repository cannot deploy by itself, and the server cannot change the repository.
- B4. Site to readers and machines: HTTPS only, read-only, no accounts, no forms, no stored user input.
- B5. Repository to external archives: Zenodo, Software Heritage and HAL hold independent copies with their own identifiers, and any of them can be compared against the repository at any time.

## 5. How the requirements are met

**C1 against T1.** Direct pushes require the maintainer's SSH key and a GitHub account protected by two-factor authentication. Every commit is attributable in the public history. From the first release after 13 September 2026, release tags are signed with the maintainer's SSH key and can be verified with the key published in `.github/allowed_signers` (SECURITY.md, Verifying releases). A branch ruleset that blocks force pushes and deletion on main belongs to this argument and is listed under residual risks until it is in place.

**C2 against T2.** The server sends a Content Security Policy with `default-src 'self'`, `object-src 'none'`, `base-uri 'none'`, `frame-ancestors 'self'` and `form-action 'none'`, HTTP Strict Transport Security, `X-Content-Type-Options: nosniff` and a strict Referrer-Policy. Two reflected cross-site scripting defects found in the audit of 5 September 2026 were fixed the same day, and the CSP was introduced then. The site loads no third-party scripts, fonts or analytics, so there is no external origin to compromise.

**C3 against T3.** The publication-metadata job in CI fails the build if a commit named in the Publication Manifest does not exist, if the declared Specification version disagrees with any chapter, or if a guarded Status field changes. Every projection on the site names its canonical source, and the site's observatory page compares projections with their sources after each build. The specification states that projections are never a source of truth, and the site applies that rule to itself.

**C4 against T4.** Third-party actions are pinned to full commit SHAs with the version in a comment. Each SHA is verified against the upstream tag before it is adopted. Dependabot proposes updates as reviewable pull requests, and workflow tokens are read-only. OpenSSF Scorecard's Token-Permissions and Dangerous-Workflow checks score 10 of 10 and run weekly.

**C5 against T6.** The repository is archived in Software Heritage, each release is archived in Zenodo with a DOI, and a position paper is deposited in HAL. Any one of the three survives the loss of the others. GOVERNANCE.md describes the continuity arrangement for the maintainer role.

**C6 against T5.** Every file resolves to a licence and a copyright holder under REUSE 3.3 (`REUSE.toml`, `LICENSES/`), checked in CI on every change and registered with the REUSE API.

**Against T7.** CONTRIBUTING.md and the issue templates forbid naming real organizations, clients, products or people. The Reference Case and the Implementation Case are anonymized. The site collects no personal data and sets no tracking.

## 6. Common weaknesses and how they are countered

| Weakness class | Where it could appear | Countermeasure |
|---|---|---|
| Cross-site scripting | site pages that echo a parameter | output encoding in the engine, CSP without external origins; two instances fixed on 2026-09-05 |
| Framing and object injection | site | `frame-ancestors 'self'`, `object-src 'none'`, `base-uri 'none'` |
| Downgrade to plain HTTP | site | HSTS, HTTPS-only origin |
| Tampered third-party action | CI | SHA pinning, upstream tag verification, read-only tokens, Dependabot review |
| Metadata drift | repository, machine records | publication-metadata job, revision histories, Status fields |
| Licence ambiguity | repository | REUSE compliance with per-path annotations, CI lint |
| Loss of history | repository | Git history, Zenodo, Software Heritage |
| Leaked secrets | repository | no secrets exist; no configuration or data files; pattern scan of the full tree on 2026-09-11 found nothing |

## 7. Evidence

- CI workflows: `.github/workflows/ci.yml` and `.github/workflows/scorecard.yml`; the design rationale is in CI-DESIGN.md.
- OpenSSF Scorecard: [scorecard.dev viewer](https://scorecard.dev/viewer/?uri=github.com/DenisHogberg/OCOM)
- OpenSSF Best Practices: [project 14573](https://www.bestpractices.dev/projects/14573)
- REUSE: [api.reuse.software](https://api.reuse.software/info/github.com/DenisHogberg/OCOM)
- Response headers of ocom.uno, checked on 2026-09-13: CSP with `script-src 'self'`, HSTS, nosniff, Referrer-Policy.
- Mozilla HTTP Observatory: A+ (110 of 110), scan of 2026-09-13, [observatory report](https://developer.mozilla.org/en-US/observatory/analyze?host=ocom.uno).
- Record of the 5 September 2026 fixes: [site changelog](https://ocom.uno/changelog)
- Archives: [Zenodo, DOI 10.5281/zenodo.21510450](https://doi.org/10.5281/zenodo.21510450); [Software Heritage origin](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/DenisHogberg/OCOM)

## 8. Residual risks

- `style-src` still allows `'unsafe-inline'`: 33 inline style blocks and 110 style attributes across the site would need extraction into per-page stylesheets, which is a separate job. `script-src` was reduced to `'self'` on 13 September 2026 by moving six inline scripts into files; the Mozilla Observatory grade went from B+ (80) to A+ (110).
- Releases before the signing policy (v1.0.0, v1.1.0, v1.1.1) are unsigned and are not re-tagged. Their integrity rests on the Zenodo and Software Heritage copies.
- One person holds every role. Archives and the continuity arrangement in GOVERNANCE.md mitigate this; they do not remove it.
- The publication engine lives outside this repository, so CI cannot prove that the live site matches the repository. The site's observatory page and the maintainer's post-deploy checks cover that gap.
- Branch protection on main is not yet confirmed.

## 9. Review

This case is reviewed at each release and whenever a security report is resolved.

| Version | Date | Change |
|---|---|---|
| 0.1 | 13 September 2026 | First version, written for the OpenSSF Best Practices silver criterion `assurance_case`. |
| 0.2 | 13 September 2026 | Residual risk on `script-src` closed after the inline scripts were moved to files; Observatory A+ recorded as evidence; `style-src` residual risk stated precisely. |

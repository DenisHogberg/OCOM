# Security Policy

## What this covers

This repository contains a Markdown specification and no executable code. The public surfaces that can carry a security defect are:

- the static site [ocom.uno](https://ocom.uno), which publishes this repository and serves two small client-side scripts, on `/search` and `/observatory/retrieval`;
- the machine records the site publishes: the Knowledge API under `/api/v1`, the resolver, the JSON, JSON-LD and Markdown projections;
- the continuous integration workflow in `.github/workflows/ci.yml`, whose actions are pinned by commit SHA.

Reports about the following are welcome: cross-site scripting or injection on any page of ocom.uno; regressions in the response headers (Content Security Policy, HSTS, content types); a published record that could be used to mislead a machine consumer; a weakness in the CI workflow.

A page or record that disagrees with the canonical file it names as its source is not a security issue. It is a projection defect, and it has its own [issue template](.github/ISSUE_TEMPLATE/projection-defect.md).

## How to report

Use GitHub's private vulnerability reporting: open the [Security tab](https://github.com/DenisHogberg/OCOM/security) of this repository and choose "Report a vulnerability". The report stays private until a fix is published.

If private reporting is unavailable to you, open an issue titled "Security" that describes the class of the problem without the details needed to exploit it, and the maintainer will arrange a private channel.

## What to expect

- Acknowledgement within seven days.
- A fix on the live site as soon as it is verified, with an entry in the site [changelog](https://ocom.uno/changelog) and, where the repository is affected, in [`CHANGELOG.md`](CHANGELOG.md).
- Credit in the changelog entry if you want it.

There is no bounty. The project sells nothing and has no budget for one.

## Supported versions

The `main` branch and the live site are the supported versions. Tagged releases are archived snapshots and are not patched.

## Verifying releases

Release tags created after 13 September 2026 are signed with the maintainer's SSH key. The public key is published in [`.github/allowed_signers`](.github/allowed_signers). To verify a tag locally:

```
git config gpg.ssh.allowedSignersFile .github/allowed_signers
git verify-tag <tag>
```

GitHub shows the same signature as "Verified" on the tag and release pages. The tags v1.0.0, v1.1.0 and v1.1.1 predate this policy and are unsigned; their contents can be checked against the Zenodo archives instead.

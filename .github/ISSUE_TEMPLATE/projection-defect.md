---
name: Projection defect
about: A page or machine record on ocom.uno disagrees with the canonical file it names as its source, or two representations of one record disagree with each other.
title: "[Projection] "
labels: projection-defect
assignees: ''
---

## URL

The page or record on ocom.uno, and the second representation if the defect is between two of them (HTML, JSON, JSON-LD, Markdown, the API).

## Canonical source

The file in this repository that the page names as its source, on `main`.

## Observed

Quote the text or the field as published.

## Expected

Quote the canonical text, or state the value the other representation carries.

## Reproduction

The command that shows it, for example:

```
curl -s https://ocom.uno/api/v1/term/object | python3 -c "import json,sys;print(json.load(sys.stdin)['definition'])"
```

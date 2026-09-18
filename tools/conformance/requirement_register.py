#!/usr/bin/env python3
"""Requirement Register generator for the OCOM Conformance Test Suite.

Implements Section 2 of docs/Governance/Conformance-Test-Suite.md: the requirement set
is the set of canonical source documents that Chapters 4, 5 and 6 of docs/Specification
compile, read from those chapters' Source lines; every paragraph or list item that carries
a normative keyword yields one Statement; a paragraph that carries a keyword and ends with
a colon absorbs the list that follows it; the first keyword classifies the Statement; the
identity of a Statement is the SHA-256 of its document path, its level-one section heading
and its text, joined by newlines.

Standard library only. Usage:

  requirement_register.py --write          regenerate docs/Governance/Requirement-Register.md
  requirement_register.py --check          regenerate in memory and fail if the committed
                                           register differs (the rule AO-064 recommends)
  requirement_register.py --init-aliases   first population of Requirement-Aliases.md
                                           (refuses to run if the file already exists)
  requirement_register.py --check-aliases  fail if any Statement in the register has no
                                           alias, or an alias names an identity that no
                                           longer exists without being marked superseded
  requirement_register.py --census         print the counts only
"""
import hashlib
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
DOCS = REPO / "docs"
CHAPTERS = ["04 Meta Model.md", "05 Object Model.md", "06 Lifecycle Model.md"]
REGISTER = DOCS / "Governance" / "Requirement-Register.md"
ALIASES = DOCS / "Governance" / "Requirement-Aliases.md"
KEYWORD = re.compile(r"\b(shall|must|should|may)\b", re.IGNORECASE)
CANONICAL_PREFIXES = ("Meta/", "Models/", "Lifecycles/")


def requirement_set():
    """Documents Chapters 4 to 6 compile, in the order their Source lines name them, without duplicates."""
    paths = []
    for name in CHAPTERS:
        text = (DOCS / "Specification" / name).read_text(encoding="utf-8")
        source_lines = [line for line in text.splitlines() if line.startswith("*Source")]
        if len(source_lines) != 1:
            raise SystemExit("%s: expected exactly one Source line, found %d" % (name, len(source_lines)))
        for path in re.findall(r"`([^`]+\.md)`", source_lines[0]):
            path = path[len("docs/"):] if path.startswith("docs/") else path
            if path.startswith(CANONICAL_PREFIXES) and path not in paths:
                paths.append(path)
    return paths


def classify(text):
    keyword = KEYWORD.search(text).group(1).lower()
    return {"shall": "mandatory", "must": "mandatory", "should": "recommended", "may": "optional"}[keyword]


# A metadata field line, the only thing a leading ** is allowed to mean here. A sentence that
# merely opens with a bold term ("**Ownership** shall be explicit.") is a Statement like any other,
# and skipping every line that starts with ** dropped it silently.
FIELD = re.compile(r"^\*\*[A-Z][A-Za-z ]{2,30}:\*\*")


def statements(path):
    """Statements of one document, in document order: (section, class, text, identity)."""
    text = (DOCS / path).read_text(encoding="utf-8")
    body = text.split("<!-- nav:end -->", 1)[-1]
    body = body.split("\n# Revision History", 1)[0]
    lines = body.split("\n")
    section = None
    out = []
    i = 0

    def unit_at(index):
        """Return (kind, text, next_index) for the block starting at index, or None."""
        line = lines[index]
        if line.lstrip().startswith("- "):
            return "item", line.lstrip()[2:].strip(), index + 1
        parts = []
        j = index
        while j < len(lines) and lines[j].strip() and not lines[j].lstrip().startswith("- ") \
                and not lines[j].startswith(("# ", "|")) and not FIELD.match(lines[j]) and lines[j].strip() != "---":
            parts.append(lines[j].strip())
            j += 1
        if not parts:
            return None
        return "para", " ".join(parts), j

    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            section = line[2:].strip()
            i += 1
            continue
        if section is None or not line.strip() or line.startswith(("|", "#")) or FIELD.match(line) or line.strip() == "---":
            i += 1
            continue
        unit = unit_at(i)
        if unit is None:
            i += 1
            continue
        kind, utext, nxt = unit
        if kind == "para" and KEYWORD.search(utext) and utext.endswith(":"):
            # the stem absorbs the list that follows it, blank lines allowed
            j = nxt
            while j < len(lines) and (not lines[j].strip() or lines[j].lstrip().startswith("- ")):
                if lines[j].lstrip().startswith("- "):
                    # an indented sub-bullet belongs to the same obligation; stopping at it split
                    # one Statement into two and changed the identity of both
                    utext += " " + lines[j].lstrip()[2:].strip()
                j += 1
            nxt = j
        if KEYWORD.search(utext):
            identity = hashlib.sha256(("%s\n%s\n%s" % (path, section, utext)).encode("utf-8")).hexdigest()
            out.append((section, classify(utext), utext, identity))
        i = nxt
    return out


def derive():
    paths = requirement_set()
    return paths, {path: statements(path) for path in paths}


def read_aliases(pairs=None):
    """alias file rows keyed by identity: {identity: (alias, disposition, superseded)}.

    Keying by identity loses a collision, so a caller that needs to see one passes a list in
    `pairs` and receives every (alias, identity) row in file order.
    """
    if not ALIASES.exists():
        return {}
    rows = {}
    for line in ALIASES.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| REQ-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        alias, identity = cells[0], cells[1].strip("`")
        disposition = cells[5] if len(cells) > 5 else ""
        if pairs is not None:
            pairs.append((alias, identity))
        rows[identity] = (alias, disposition, "superseded" in disposition.lower())
    return rows


def document_code(path):
    stem = pathlib.Path(path).stem.upper().replace(" ", "-")
    tier = path.split("/")[0].upper()
    return "%s-%s" % (tier, stem) if tier != "LIFECYCLES" else "LIFECYCLES"


def render_register(paths, derived, aliases):
    counts = {"mandatory": 0, "recommended": 0, "optional": 0}
    total = 0
    for path in paths:
        for _, cls, _, _ in derived[path]:
            counts[cls] += 1
            total += 1
    lines = [
        "<!-- nav:start -->",
        "[Docs](../README.md) / [Governance](README.md) / Requirement Register",
        "",
        "[← Back](Conformance-Test-Suite.md) · [↑ Up](README.md)",
        "",
        "---",
        "<!-- nav:end -->",
        "",
        "# Requirement Register",
        "",
        "**Document ID:** GOV-REQUIREMENT-REGISTER-01",
        "",
        "**Status:** Informative",
        "",
        "**Generated by:** `tools/conformance/requirement_register.py`, never edited by hand; a divergence between this file and a regeneration fails the CI check named in `CI-DESIGN.md`.",
        "",
        "**Version and history:** none, by the convention `Documentation-Standards.md` records for generated artifacts: the content of this file is its version, and its history is the history of the documents it derives from.",
        "",
        "---",
        "",
        "# Purpose",
        "",
        "This file is the Requirement Register that Section 2 of `Conformance-Test-Suite.md` specifies: every Statement derived by rule from the documents Chapters 4, 5 and 6 of the reading path compile, each with its class and its content-addressed identity. It is a derived artifact in the sense `AO-064` uses and adds nothing to the documents it reads; a Statement is what its source document says, nothing more. Aliases and Dispositions live in `Requirement-Aliases.md`, the one hand-written file of the suite.",
        "",
        "---",
        "",
        "# Census",
        "",
        "%d Statements across %d documents: %d mandatory, %d recommended, %d optional." % (total, len(paths), counts["mandatory"], counts["recommended"], counts["optional"]),
        "",
        "| Document | Statements | Mandatory | Recommended | Optional |",
        "|---|---|---|---|---|",
    ]
    for path in paths:
        c = {"mandatory": 0, "recommended": 0, "optional": 0}
        for _, cls, _, _ in derived[path]:
            c[cls] += 1
        lines.append("| `%s` | %d | %d | %d | %d |" % (path, len(derived[path]), c["mandatory"], c["recommended"], c["optional"]))
    lines += ["", "---", "", "# Statements", "", "| Alias | Document | Section | Class | Statement | Identity |", "|---|---|---|---|---|---|"]
    for path in paths:
        for section, cls, text, identity in derived[path]:
            alias = aliases.get(identity, ("unaliased", "", False))[0]
            cell = text.replace("|", "\\|")
            lines.append("| %s | `%s` | %s | %s | %s | `%s` |" % (alias, path, section.replace("|", "\\|"), cls, cell, identity))
    return "\n".join(lines) + "\n"


def render_aliases(paths, derived, today):
    lines = [
        "<!-- nav:start -->",
        "[Docs](../README.md) / [Governance](README.md) / Requirement Aliases",
        "",
        "[← Back](Requirement-Register.md) · [↑ Up](README.md)",
        "",
        "---",
        "<!-- nav:end -->",
        "",
        "# Requirement Aliases",
        "",
        "**Document ID:** GOV-REQUIREMENT-ALIASES-01",
        "",
        "**Status:** Informative",
        "",
        "**Last Updated:** " + today,
        "",
        "---",
        "",
        "# Purpose",
        "",
        "The append-only Alias File that Section 2 of `Conformance-Test-Suite.md` specifies. Each row binds a stable alias of the form `REQ-<document>-<n>` to the content-addressed identity of one Statement in `Requirement-Register.md` and carries at most one Disposition: `Descriptive` (the keyword imposes no obligation), `Review` (an obligation no mechanical procedure can decide), or empty. Rows are appended, never edited or removed; when a source sentence changes, its Statement gets a new identity, a new row is appended for it, and the old row's Disposition cell records `superseded by <alias>`. The first population was written by `tools/conformance/requirement_register.py --init-aliases`; every later row is a recorded decision with a reason and a date.",
        "",
        "---",
        "",
        "# Aliases",
        "",
        "| Alias | Identity | Document | Section | Recorded | Disposition | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    for path in paths:
        code = document_code(path)
        for n, (section, cls, text, identity) in enumerate(derived[path], start=1):
            lines.append("| REQ-%s-%03d | `%s` | `%s` | %s | %s |  | first population |" % (code, n, identity, path, section.replace("|", "\\|"), today))
    return "\n".join(lines) + "\n"


def main(argv):
    if len(argv) != 2 or argv[1] not in ("--write", "--check", "--init-aliases", "--check-aliases", "--census"):
        print(__doc__)
        return 2
    mode = argv[1]
    paths, derived = derive()
    total = sum(len(v) for v in derived.values())
    if mode == "--census":
        for path in paths:
            print("%-32s %3d" % (path, len(derived[path])))
        counts = {"mandatory": 0, "recommended": 0, "optional": 0}
        for path in paths:
            for _, cls, _, _ in derived[path]:
                counts[cls] += 1
        print("documents %d, statements %d, %s" % (len(paths), total, counts))
        return 0
    if mode == "--init-aliases":
        if ALIASES.exists():
            print("%s exists; the Alias File is append-only and is never regenerated" % ALIASES)
            return 1
        import datetime
        today = datetime.date.today().strftime("%-d %B %Y")
        ALIASES.write_text(render_aliases(paths, derived, today), encoding="utf-8")
        print("wrote %s with %d aliases" % (ALIASES, total))
        return 0
    pairs = []
    aliases = read_aliases(pairs)
    if mode == "--check-aliases":
        identities = {identity for path in paths for _, _, _, identity in derived[path]}
        missing = [(path, section, text[:80]) for path in paths for section, _, text, identity in derived[path] if identity not in aliases]
        stale = [alias for identity, (alias, _, superseded) in aliases.items() if identity not in identities and not superseded]
        # An alias names one Statement and a Statement carries one alias. Coverage in both
        # directions does not imply either: an alias edited to a name already in use binds two
        # Statements, and every consumer keyed by alias then resolves to whichever row it read last.
        from collections import Counter
        dup_alias = sorted(a for a, n in Counter(a for a, _ in pairs).items() if n > 1)
        dup_identity = sorted(i for i, n in Counter(i for _, i in pairs).items() if n > 1)
        for path, section, text in missing:
            print("no alias: %s / %s: %s" % (path, section, text))
        for alias in stale:
            print("alias %s names an identity no Statement carries and is not marked superseded" % alias)
        for alias in dup_alias:
            print("alias %s is bound to more than one Statement identity" % alias)
        for identity in dup_identity:
            print("Statement identity %s carries more than one alias" % identity[:16])
        print("aliases %d, statements %d, missing %d, stale %d, duplicate aliases %d, duplicate identities %d"
              % (len(aliases), total, len(missing), len(stale), len(dup_alias), len(dup_identity)))
        return 1 if (missing or stale or dup_alias or dup_identity) else 0
    rendered = render_register(paths, derived, aliases)
    if mode == "--write":
        REGISTER.write_text(rendered, encoding="utf-8")
        print("wrote %s: %d statements" % (REGISTER, total))
        return 0
    if not REGISTER.exists():
        print("%s missing; run --write" % REGISTER)
        return 1
    current = REGISTER.read_text(encoding="utf-8")
    if current == rendered:
        print("register up to date: %d statements" % total)
        return 0
    import difflib
    for line in difflib.unified_diff(current.splitlines(), rendered.splitlines(), "committed", "regenerated", lineterm="", n=1):
        print(line)
    print("register diverges from a regeneration; run --write and commit the result")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

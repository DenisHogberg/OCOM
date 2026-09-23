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
                                           longer exists without being marked superseded,
                                           or a committed row was edited in place rather
                                           than superseded by a new one (the append-only
                                           rule; --against <rev> picks what to compare to)
  requirement_register.py --census         print the counts only
"""
import hashlib
import os
import pathlib
import re
import subprocess
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
        rows[identity] = (alias, disposition, disposition.strip().lower().startswith("superseded by"))
    return rows


# What a Disposition cell may say. It decides whether a mandatory Test exists (Descriptive removes
# it from the measured set) and whether a stale row is forgiven (superseded), and it was free text
# compared by substring: "Review, and certainly not Descriptive" deleted a Test, and "superseded by
# <an alias that exists nowhere>" deleted one silently when a sentence was removed.
DISPOSITIONS = ("", "descriptive", "review")
SUPERSEDED = re.compile(r"^superseded by (REQ-[A-Z0-9-]+)$", re.I)


def alias_rows(text):
    """Every alias row of an Alias File, keyed by alias, as its list of cells."""
    rows = {}
    for line in text.splitlines():
        if line.startswith("| REQ-"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.setdefault(cells[0], cells)
    return rows


def file_at(rev, relative):
    """The file as of `rev`, or None when this checkout cannot answer."""
    try:
        done = subprocess.run(["git", "-C", str(REPO), "show", "%s:%s" % (rev, relative)],
                              capture_output=True, text=True)
    except OSError:
        return None
    return done.stdout if done.returncode == 0 else None


def commit_of(rev):
    """The commit `rev` resolves to, or None."""
    try:
        done = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify", "%s^{commit}" % rev],
                              capture_output=True, text=True)
    except OSError:
        return None
    return done.stdout.strip() if done.returncode == 0 else None


def base_revisions():
    """The revisions to compare the Alias File against, most meaningful first.

    HEAD was in this list, and on a push to the default branch every candidate resolved to the
    commit under test, so the comparison was the file against itself: it reported zero edits and
    the "compared against nothing" branch was unreachable in any checkout. A revision that is the
    commit under test is not a base, and `resolved_base` refuses it."""
    out = []
    base = os.environ.get("GITHUB_BASE_REF")
    if base:
        out += ["origin/" + base, base]
    # HEAD is last and is used only when no other revision resolves, which is what a shallow
    # checkout gives: the comparison then says what it could and could not see, rather than
    # reporting zero edits as though it had looked at history
    return out + ["origin/main", "main", "HEAD"]


# Only the Disposition may change after a row is committed, and only into a value the grammar
# above reads. Everything else in a row is fixed: the identity is the SHA-256 of the document
# path, the section and the text, so a changed sentence is a new identity and therefore a new row.
EDITABLE_CELL = 5


def append_only_failures(revisions):
    """Every committed alias row that was edited in place or removed, and the revision compared to.

    Section 2 makes the file append-only: rows "are appended, never edited or removed; when a
    source sentence changes, its Statement gets a new identity, a new row is appended for it, and
    the old row's Disposition cell records `superseded by <alias>`". Nothing enforced that.
    --check-aliases compares the current register against the current file, so editing a row's
    Identity cell in place to the new hash keeps the alias, the recorded date and the note, and
    every check stays green while the sentence underneath it has changed. The rule is about the
    file's history, so history is what decides it.
    """
    relative = str(ALIASES.relative_to(REPO))
    head = commit_of("HEAD")
    # a revision that is the commit under test can only show what is not committed yet: on a push
    # to the default branch every candidate resolved to it, so the file was compared against itself
    # and the check reported zero edits. It is used only when nothing else resolves, and it says so.
    ordered = [rev for rev in revisions if commit_of(rev) != head or commit_of(rev) is None] \
              + [rev for rev in revisions if commit_of(rev) is not None and commit_of(rev) == head]
    for rev in ordered:
        text = file_at(rev, relative)
        if text is None:
            continue
        if commit_of(rev) == head:
            print("comparing against %s, which is the commit under test: this can only show edits that are not "
                  "committed. Pass --against <the commit before this one> to check a push." % rev)
        before, now = alias_rows(text), alias_rows(ALIASES.read_text(encoding="utf-8"))
        failures = []
        for alias, cells in before.items():
            current = now.get(alias)
            if current is None:
                failures.append("alias %s was committed at %s and is no longer in the file; rows are appended, "
                                "never removed" % (alias, rev))
                continue
            for i, cell in enumerate(cells):
                if i == EDITABLE_CELL:
                    continue
                if i >= len(current) or current[i] != cell:
                    failures.append("alias %s was edited in place since %s: column %d read %r and now reads %r; a "
                                    "changed Statement gets a new identity and a new row, and the old row records "
                                    "`superseded by <alias>`"
                                    % (alias, rev, i + 1, cell[:60], (current[i] if i < len(current) else "")[:60]))
        return failures, rev
    return (["the Alias File could not be read at any of %s, so the append-only rule was compared against nothing"
             % ", ".join(revisions)], None)


def disposition_failures(pairs, aliases):
    """Every Disposition cell this tool cannot read, and every supersession that names nothing."""
    names = {a for a, _ in pairs}
    live = {a for identity, (a, _, _) in aliases.items()}
    out = []
    for identity, (alias, disposition, _) in aliases.items():
        value = (disposition or "").strip()
        if value.lower() in DISPOSITIONS:
            continue
        m = SUPERSEDED.match(value)
        if not m:
            out.append("alias %s carries a Disposition this tool cannot read: %r; it may be empty, Descriptive, "
                       "Review, or 'superseded by <alias>'" % (alias, value[:60]))
            continue
        if m.group(1) not in names:
            out.append("alias %s says it is superseded by %s, which this file does not carry"
                       % (alias, m.group(1)))
    return out


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
        "This file is the Requirement Register that Section 2 of `Conformance-Test-Suite.md` specifies: every Statement derived by rule from the documents "
        "Chapters 4, 5 and 6 of the reading path compile, with a stable alias, the tier its keyword sets and the identity of its text. Core Conformance "
        "itself is defined by `Language/Conformance.md`; this enumeration is the reading adopted for the suite, per `CAND-021` of 19 September 2026, and "
        "the chapters name where the requirements are found rather than originating them.",
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
    if len(argv) < 2 or argv[1] not in ("--write", "--check", "--init-aliases", "--check-aliases", "--census") \
            or (len(argv) != 2 and argv[2:3] != ["--against"]) or (argv[2:3] == ["--against"] and len(argv) != 4):
        print(__doc__)
        return 2
    mode = argv[1]
    against = None
    if "--against" in argv:
        against = argv[argv.index("--against") + 1]
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
        grammar = disposition_failures(pairs, aliases)
        for failure in grammar:
            print(failure)
        edits, compared_to = append_only_failures([against] if against else base_revisions())
        for failure in edits:
            print(failure)
        # a supersession must hand the obligation to a row that is itself live, or removing a
        # sentence removes its mandatory Test with every check green
        orphan = []
        for identity, (alias, disposition, superseded) in aliases.items():
            m = SUPERSEDED.match((disposition or "").strip())
            if superseded and m:
                successor = [i for i, (a, _, _) in aliases.items() if a == m.group(1)]
                if not successor or successor[0] not in identities:
                    orphan.append("alias %s is superseded by %s, which carries no Statement the register holds"
                                  % (alias, m.group(1)))
        for line in orphan:
            print(line)
        print("aliases %d, statements %d, missing %d, stale %d, duplicate aliases %d, duplicate identities %d, "
              "unreadable dispositions %d, orphan supersessions %d, rows edited since %s %d"
              % (len(aliases), total, len(missing), len(stale), len(dup_alias), len(dup_identity),
                 len(grammar), len(orphan), compared_to or "(no revision)", len(edits)))
        return 1 if (missing or stale or dup_alias or dup_identity or grammar or orphan or edits) else 0
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

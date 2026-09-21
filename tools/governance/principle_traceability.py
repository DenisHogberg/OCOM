#!/usr/bin/env python3
"""Check every claim `Governance/Principle-Traceability.md` makes about the corpus.

The map itself is judgment: deciding that a rule carries a principle is not something a
regular expression can do, and `AO-074` asks for the map, not for a generator. What a tool
can do is make the map falsifiable, which is the property the map is about. This checker
reads the table and verifies, for every row:

  * the cited document exists and the cited line carries the quoted text verbatim;
  * a row that names a Requirement Register alias names one that exists, and whose
    Statement text contains the quoted sentence;
  * a row classified `binding rule` quotes a sentence that actually carries shall, shall
    not or must, and is not a revision-history row or an editorial note;
  * a row classified `absent` names no document;
  * every Canonical Principle in `Core/Constitution.md` has exactly one block, and the
    block quotes the principle verbatim.

It asserts nothing about whether the classification is right. It asserts that every fact
the classification rests on is real, so a reader who disagrees with a verdict can argue
about the judgment rather than about the evidence.

  principle_traceability.py --check    verify the document against the corpus, exit 1 on any failure
  principle_traceability.py --summary  print the verdict counts the document records
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DOC = ROOT / "docs" / "Governance" / "Principle-Traceability.md"
CONSTITUTION = ROOT / "docs" / "Core" / "Constitution.md"
REGISTER = ROOT / "docs" / "Governance" / "Requirement-Register.md"

KINDS = {"binding rule", "permission", "restatement", "definition", "reserved", "absent"}
VERDICTS = {"carried by rules", "partly carried", "restated only", "reserved", "no occurrence"}
NORMATIVE = re.compile(r"\b(shall|must)\b", re.I)

BLOCK = re.compile(
    r"^## Principle (\d+): (.+?)\s*$\n+"
    r"\*\*Principle:\*\* (.+?)\s*$\n+"
    r"\*\*Verdict:\*\* (.+?)\s*$\n+"
    r"\*\*In conformance scope:\*\* (.+?)\s*$\n+"
    r"(?P<table>(?:^\|.*$\n)+)"
    r"\n\*\*Test:\*\* (.+?)\s*$",
    re.M,
)
ROW = re.compile(r"^\| `([^`]+)` \| ([^|]+?) \| ([^|]*?) \| (.+?) \|$")


def stem_of(path, lineno, window=14):
    """The modal stem a bullet belongs to.

    The corpus writes most obligations as a stem ending in a colon followed by a list, and
    the Requirement Register flattens the two into one Statement. A row may therefore cite
    the bullet, which carries the substance, as long as a stem within `window` lines above
    it carries the modal. Returns the stem line, or None.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    for i in range(lineno - 2, max(-1, lineno - 2 - window), -1):
        line = lines[i]
        if line.rstrip().endswith(":") and NORMATIVE.search(line):
            return line.strip()
        if not line.strip():
            continue
        if not line.lstrip().startswith(("-", "*")) and i < lineno - 2:
            return None
    return None

def principles():
    """The Canonical Principles as the Constitution numbers them."""
    text = CONSTITUTION.read_text(encoding="utf-8")
    section = text.split("# Canonical Principles", 1)[1].split("\n---", 1)[0]
    out = {}
    for m in re.finditer(r"^(\d+)\. \*\*(.+?)\.\*\* (.+?)\s*$", section, re.M):
        out[int(m.group(1))] = (m.group(2), m.group(3))
    return out


def aliases():
    text = REGISTER.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^\| (REQ-[A-Z0-9-]+) \| `([^`]+)` \| ([^|]*) \| (\w+) \| (.+?) \|\s*`[0-9a-f]{64}`\s*\|$", text, re.M):
        out[m.group(1)] = (m.group(2), m.group(5))
    return out


def check():
    failures = []
    if not DOC.exists():
        print("missing %s" % DOC.relative_to(ROOT))
        return 1
    doc = DOC.read_text(encoding="utf-8")
    canon = principles()
    alias_map = aliases()
    blocks = list(BLOCK.finditer(doc))
    seen = []
    rows_checked = 0

    for b in blocks:
        n = int(b.group(1))
        title, statement = canon.get(n, (None, None))
        seen.append(n)
        if title is None:
            failures.append("Principle %d is not a Canonical Principle" % n)
            continue
        if b.group(2).strip() != title:
            failures.append("Principle %d: title %r is not the Constitution's %r" % (n, b.group(2).strip(), title))
        quoted = b.group(3).strip()
        if quoted != statement.strip():
            failures.append("Principle %d: the quoted principle is not verbatim" % n)
        verdict = b.group(4).strip()
        if verdict not in VERDICTS:
            failures.append("Principle %d: verdict %r is not one of %s" % (n, verdict, sorted(VERDICTS)))
        scope = b.group(5).strip()
        if scope not in {"yes", "no", "partly"}:
            failures.append("Principle %d: conformance scope %r is not yes, no or partly" % (n, scope))

        # Every line of the table except the header and the |---| separator is a row and must be
        # checked. Selecting only lines that start with a backtick dropped malformed rows before
        # the unparsable-row failure below could see them, so a row naming a file that does not
        # exist passed by being unreadable.
        table = [l for l in b.group("table").splitlines()
                 if l.startswith("|") and not l.startswith("| Carrier") and set(l) - set("|-: ")]
        if verdict == "no occurrence" and table:
            failures.append("Principle %d: verdict is 'no occurrence' but the table names carriers" % n)
        if verdict != "no occurrence" and not table:
            failures.append("Principle %d: verdict is %r and the table is empty" % (n, verdict))

        for line in table:
            m = ROW.match(line)
            if not m:
                failures.append("Principle %d: unparsable row %s" % (n, line[:70]))
                continue
            where, kind, alias, quote = (g.strip() for g in m.groups())
            kind = kind.strip()
            rows_checked += 1
            if kind not in KINDS:
                failures.append("Principle %d: kind %r is not one of %s" % (n, kind, sorted(KINDS)))
            if ":" not in where:
                failures.append("Principle %d: carrier %r carries no line number" % (n, where))
                continue
            path, _, lineno = where.rpartition(":")
            target = ROOT / path
            if not target.exists():
                failures.append("Principle %d: %s does not exist" % (n, path))
                continue
            try:
                # split on newlines only: str.splitlines() also breaks on form feed and the
                # unicode line separators, which would shift every line number after one of them
                source = target.read_text(encoding="utf-8").split("\n")[int(lineno) - 1]
            except (ValueError, IndexError):
                failures.append("Principle %d: %s has no line %s" % (n, path, lineno))
                continue
            text = quote.strip().strip('"')
            if not text:
                failures.append("Principle %d: %s:%s carries no quote, so nothing is checked" % (n, path, lineno))
                continue
            if text not in source:
                failures.append("Principle %d: %s:%s does not carry %r" % (n, path, lineno, text[:60]))
            if kind == "absent":
                failures.append("Principle %d: a row classified 'absent' names %s; absent means no carrier exists" % (n, path))
            if kind == "binding rule":
                if not NORMATIVE.search(source) and not stem_of(target, int(lineno)):
                    failures.append("Principle %d: %s:%s is classified 'binding rule' and neither it nor a stem above it carries shall or must" % (n, path, lineno))
                if source.startswith("| 0.") or source.lstrip().startswith(">"):
                    failures.append("Principle %d: %s:%s is a revision row or an editorial note, not a rule" % (n, path, lineno))
            if alias:
                if alias not in alias_map:
                    failures.append("Principle %d: alias %s is not in the Requirement Register" % (n, alias))
                elif text and text not in alias_map[alias][1]:
                    failures.append("Principle %d: alias %s does not carry %r" % (n, alias, text[:60]))

    missing = sorted(set(canon) - set(seen))
    if missing:
        failures.append("no block for Canonical Principle(s): %s" % ", ".join(str(m) for m in missing))
    repeated = sorted({n for n in seen if seen.count(n) > 1})
    if repeated:
        failures.append("more than one block for Canonical Principle(s): %s" % ", ".join(str(r) for r in repeated))
    unparsed = len(re.findall(r"^## Principle \d+:", doc, re.M)) - len(blocks)
    if unparsed:
        failures.append("%d principle heading(s) whose block does not parse: check the field order and the table" % unparsed)

    # a carrier-shaped line that no table contains is a claim nobody checked. One sat after a
    # block's Note on 21 September 2026 and the count stayed at 71 while the file held 72.
    shaped = len([l for l in doc.splitlines() if ROW.match(l)])
    if shaped != rows_checked:
        failures.append("%d carrier-shaped row(s) sit outside a table and were not checked" % (shaped - rows_checked))

    for f in failures:
        print("FAIL %s" % f)
    print("%d principle blocks, %d carrier rows checked, %d failure(s)" % (len(blocks), rows_checked, len(failures)))
    return 1 if failures else 0


def summary():
    doc = DOC.read_text(encoding="utf-8")
    counts = {}
    for m in re.finditer(r"^\*\*Verdict:\*\* (.+?)\s*$", doc, re.M):
        counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    scope = {}
    for m in re.finditer(r"^\*\*In conformance scope:\*\* (.+?)\s*$", doc, re.M):
        scope[m.group(1)] = scope.get(m.group(1), 0) + 1
    for k in sorted(counts):
        print("%-18s %d" % (k, counts[k]))
    print("in conformance scope:", ", ".join("%s %d" % (k, v) for k, v in sorted(scope.items())))
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="verify the document against the corpus (the default)")
    g.add_argument("--summary", action="store_true", help="print the verdict counts only")
    a = p.parse_args()
    if a.summary:
        return summary()
    return check()


if __name__ == "__main__":
    sys.exit(main())

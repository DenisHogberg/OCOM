#!/usr/bin/env python3
"""How much of its sources does each compiled chapter carry, and does `verbatim` mean it?

`requirement_register.py` checks the reading path forward: every sentence a chapter carries
traces to a canonical document. `AO-077` recorded that nothing checked the other direction, and
three obligations of `Models/Entity.md` and `Models/Relationship.md` had been missing from
Chapter 5 for weeks while the forward check stayed green.

`CAND-018` says what the other direction may and may not find. A chapter's Source line declares
one of three forms, and only the third is a completeness claim:

  synthesized from          carries none of its sources' Statements as obligations
  compiled from             carries them in summary and may abridge
  compiled from ... verbatim   carries every mandatory Statement of the sections it names

So this tool measures all nine chapters and enforces the third form only. An abridged chapter is
not a defect, and a number is still worth having: it says how much of the normative text a reader
of the reading path never sees, which is the question `CAND-018` answers in principle and nobody
had answered in figures.

  compilation_survey.py --census   print the table, always exit 0
  compilation_survey.py --check    exit 1 if a chapter declaring verbatim misses a mandatory
                                   Statement, if a Source line cannot be read, or if a chapter
                                   declares no form at all

A Statement counts as carried verbatim when the chapter's text contains it once punctuation and
case are normalized away, and as paraphrase when it is at least 0.70 similar to a unit of the
chapter extracted by the same parser as the sources, so a stem-plus-list obligation is compared
against the same shape on both sides rather than against a fragment of itself.
"""
import argparse
import difflib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import requirement_register as rr  # noqa: E402  (a sibling tool, not a package)

SPEC = ROOT / "docs" / "Specification"
CHAPTER = re.compile(r"^0\d .*\.md$")
THRESHOLD = 0.70


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip()


def declaration(path):
    """(form, [source paths]) from a chapter's Source line."""
    text = path.read_text(encoding="utf-8")
    if "*Source:" not in text:
        raise SystemExit("%s carries no Source line, so what it compiles is undeclared" % path.name)
    line = text[text.rindex("*Source:"):].split("\n")[0]
    # a dated note is history and a cross-reference is not a source: neither declares anything
    body = re.sub(r"\((?:Committee Review|\d{1,2} \w+ \d{4})[^)]*\)", "", line)
    body = re.sub(r"\(see [^)]*\)", "", body)
    first = re.split(r"\.\s+(?=[A-Z])", body)[0]
    if body.startswith("*Source: synthesized"):
        form = "synthesized"
    elif "compiled from" in body:
        form = "verbatim" if "verbatim" in first else "compiled"
    else:
        raise SystemExit("%s declares no form: %s" % (path.name, line[:120]))
    sources = []
    for rel in re.findall(r"`([^`]+\.md)`", body):
        rel = rel[len("docs/"):] if rel.startswith("docs/") else rel
        if (ROOT / "docs" / rel).exists() and rel not in sources:
            sources.append(rel)
    return form, sources


def survey(path):
    """(form, sources, counts, [(source, section, text) for each Statement not carried])."""
    form, sources = declaration(path)
    body = norm(path.read_text(encoding="utf-8"))
    rel = path.relative_to(ROOT / "docs").as_posix()
    units = [norm(text) for _, _, text, _ in rr.statements(rel)]
    units += [norm(s) for s in re.split(r"(?<=[.;:])\s+|\n", path.read_text(encoding="utf-8")) if len(s) > 25]
    counts = {"verbatim": 0, "paraphrase": 0, "absent": 0}
    absent = []
    for source in sources:
        for section, kind, text, _ in rr.statements(source):
            if kind != "mandatory":
                continue
            if norm(text) in body:
                counts["verbatim"] += 1
                continue
            best = max((difflib.SequenceMatcher(None, norm(text), u).ratio() for u in units), default=0.0)
            if best >= THRESHOLD:
                counts["paraphrase"] += 1
            else:
                counts["absent"] += 1
                absent.append((source, section, text))
    return form, sources, counts, absent


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--census", action="store_true", help="print the table and exit 0")
    p.add_argument("--check", action="store_true", help="enforce the verbatim form")
    a = p.parse_args(argv)

    chapters = sorted(c for c in SPEC.glob("*.md") if CHAPTER.match(c.name))
    if not chapters:
        raise SystemExit("no chapters found under %s; a survey over nothing cannot pass" % SPEC)

    failures = []
    print("%-26s %-12s %7s %9s %11s %7s" % ("chapter", "form", "source", "verbatim", "paraphrase", "absent"))
    for chapter in chapters:
        form, sources, counts, absent = survey(chapter)
        total = sum(counts.values())
        print("%-26s %-12s %7d %9d %11d %7d"
              % (chapter.name[:26], form, total, counts["verbatim"], counts["paraphrase"], counts["absent"]))
        if form == "verbatim" and absent:
            for source, section, text in absent:
                failures.append("%s declares verbatim but does not carry `%s` (%s): %s"
                                % (chapter.name, source, section, re.sub(r"\s+", " ", text)[:110]))
        if form == "compiled" and not sources:
            failures.append("%s declares `compiled from` and names no source document" % chapter.name)

    print("\n%d chapter(s) surveyed, %d failure(s)" % (len(chapters), len(failures)))
    for f in failures:
        print("  FAIL %s" % f)
    if a.check:
        return 1 if failures else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

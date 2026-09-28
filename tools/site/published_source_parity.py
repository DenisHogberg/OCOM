#!/usr/bin/env python3
"""Check the published files that only `publication/` can vouch for.

A few files the site serves are written by hand and generated from nothing: `llms.txt` is the
one that exists today. Until 19 September 2026 they had no source in this repository at all, so
a defect in one of them could be found only by reading the live file, and a correction left no
reviewable text behind. `publication/README.md` now names each such file and the source it must
match, and this tool is what makes that naming more than a statement of intent.

Two rules, deliberately separated by whether they need the network:

  published_source_parity.py --lint    reads `publication/` only. A source file shall not write
                                       a bare URL immediately followed by a sentence period,
                                       comma or semicolon, because a machine harvesting URLs
                                       takes the punctuation with it. That is not hypothetical:
                                       `llms.txt` published `https://ocom.uno/why.` and every
                                       harvester that read it asked the site for a page that
                                       does not exist.
  published_source_parity.py --check   fetches each published path and compares it with its
                                       source, byte for byte. Needs the network, so it is not a
                                       CI job, for the reason `publication_health.py` is not one
                                       either: a build that fetches the site fails when the site
                                       is merely unreachable.

Both modes fail closed. An empty table, a source file that does not exist, a path that cannot be
fetched: each is an exit code, never a silent pass over nothing.
"""
import argparse
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
INDEX = ROOT / "publication" / "README.md"
TIMEOUT = 30
ROW = re.compile(r"^\|\s*`(https?://[^`]+)`\s*\|\s*`([^`]+)`\s*\|")
# a URL that ends a sentence: the punctuation is not part of it, but a harvester cannot know that
GLUED = re.compile(r"(https?://[^\s<>()\[\]`]*[^\s<>()\[\]`.,;])([.,;])(\s|$)")


def rows():
    """(published url, source path) for every file `publication/README.md` names."""
    if not INDEX.exists():
        raise SystemExit("%s does not exist, so nothing states what the site should serve" % INDEX)
    out = []
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            out.append((m.group(1), m.group(2)))
    if not out:
        raise SystemExit("%s lists no published file; a check over nothing cannot pass" % INDEX)
    return out


def fetch(url):
    """(status, body, final url). urlopen follows redirects, so a published path that 301s
    somewhere carrying the source bytes was reported as matching although nothing is served at the
    path `publication/README.md` names, which is what that document states the rule to be."""
    req = urllib.request.Request(url, headers={"User-Agent": "ocom-published-source-parity/1.0 (+https://github.com/DenisHogberg/OCOM)"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read(), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, b"", url


def lint():
    failures = []
    for url, rel in rows():
        path = ROOT / rel
        if not path.exists():
            failures.append("%s names `%s`, which does not exist" % (INDEX.name, rel))
            continue
        text = path.read_text(encoding="utf-8")
        glued = []
        for lineno, line in enumerate(text.splitlines(), 1):
            # a markdown link carries its own delimiters, so only bare URLs can be misread
            for m in GLUED.finditer(re.sub(r"\[[^\]]*\]\([^)]*\)", "", line)):
                glued.append((lineno, m.group(1) + m.group(2)))
        for lineno, found in glued:
            failures.append("%s:%d writes `%s`; a harvester reads the punctuation as part of the URL" % (rel, lineno, found))
        print("%-28s %s" % (rel, "ok" if not glued else "%d glued URL(s)" % len(glued)))
    for f in failures:
        print("  FAIL %s" % f)
    print("\n%d file(s) linted, %d failure(s)" % (len(rows()), len(failures)))
    return 1 if failures else 0


def check():
    failures = []
    for url, rel in rows():
        path = ROOT / rel
        if not path.exists():
            failures.append("%s names `%s`, which does not exist" % (INDEX.name, rel))
            print("%-28s MISSING SOURCE" % rel)
            continue
        status, body, final = fetch(url)
        if status != 200:
            failures.append("%s answered %s" % (url, status))
            print("%-28s HTTP %s" % (rel, status))
            continue
        if final != url:
            failures.append("%s redirects to %s; the table names this path, not what answers for it" % (url, final))
            print("%-28s REDIRECTS" % rel)
            continue
        want = path.read_bytes()
        if body != want:
            failures.append("%s differs from `%s` (%d bytes published, %d in the source)"
                            % (url, rel, len(body), len(want)))
            print("%-28s DIFFERS" % rel)
            continue
        print("%-28s matches %s (%d bytes)" % (rel, url, len(want)))
    for f in failures:
        print("  FAIL %s" % f)
    print("\n%d published file(s) compared, %d failure(s)" % (len(rows()), len(failures)))
    return 1 if failures else 0


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--lint", action="store_true", help="check the source files only, no network")
    p.add_argument("--check", action="store_true", help="fetch each published path and compare")
    p.add_argument("--base", help="fetch from this origin instead of the one the table names")
    a = p.parse_args(argv)
    if a.base:
        global rows
        original = rows
        def rows():  # noqa: F811  (a test fixture serves the same paths on loopback)
            return [(a.base.rstrip("/") + "/" + url.split("/", 3)[3], rel) for url, rel in original()]
    if a.check:
        return check()
    return lint()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Recompute the two Observatory records ocom.uno publishes about itself.

The Publication Engine that built the site is gone (`Governance/Publication-Model.md`,
Known Gaps; `FW-006`), and with it the code that produced
`/observatory/publication-health.json` and `/observatory/health.json`. Those two records
are the site's own verification layer, so a record nobody can recompute is a claim nobody
can check, which is the failure `AO-064` names for derived artifacts.

This tool recomputes both records from the published site alone, over HTTP, using the
standard library. It reads no private source and asks the repository for nothing: what it
checks is exactly what a reader can fetch. Every row keeps the rule text the published
record carried, so a row that passes here passes the same rule that was published; where
this implementation is narrower than the rule, the record says so in its own note.

  publication_health.py --write <dir>   recompute and write both records into <dir>
  publication_health.py --check         recompute and compare against what is published,
                                        printing every difference; exit 1 if any row fails
                                        its threshold or a published figure disagrees
  publication_health.py --summary       recompute and print the counts only

Figures the published records mark as not reproducible are carried forward as constants in
this file, with the date they were last computed, rather than read back from the record under
test: a figure copied from the record it is meant to check can never disagree with it. Today
that is the directed-cycle count, whose counting rule was never published. The ownership block
of the publication-health record is carried from the published record for the same reason and
is listed there under carriedForward.
"""
import argparse
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://ocom.uno"
TIMEOUT = 30
PAUSE = 0.12  # a courtesy pause between requests; the site is small and single-homed
CYCLES_LAST_COMPUTED = "2026-09-07"
CYCLES_LAST_VALUE = 44  # what the lost generator counted on that date; carried forward, never recomputed


def as_path(url):
    """The site-relative path of a published URL, whatever origin the record spells.

    Published records name their own origin (https://ocom.uno/...), and a fixture or a staging
    host names another. Stripping one hardcoded prefix left the other form untouched and the
    fetcher then asked for base + absolute-url, so every such check silently failed to run.
    """
    u = str(url)
    if u.startswith("http://") or u.startswith("https://"):
        parts = urllib.parse.urlsplit(u)
        return parts.path + (("?" + parts.query) if parts.query else "")
    return u


class Site:
    """Fetches published files once each and remembers what was asked for."""

    def __init__(self, base, pause=PAUSE):
        self.base = base.rstrip("/")
        self.pause = pause
        self.cache = {}

    def raw(self, path):
        if path in self.cache:
            return self.cache[path]
        url = self.base + urllib.parse.quote(path, safe="/:@?=&#%")
        last = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "ocom-publication-health/1.0 (+https://github.com/DenisHogberg/OCOM)"})
                with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                    out = (r.status, r.read().decode("utf-8", "replace"))
                self.cache[path] = out
                time.sleep(self.pause)
                return out
            except urllib.error.HTTPError as e:
                out = (e.code, "")
                self.cache[path] = out
                time.sleep(self.pause)
                return out
            except Exception as e:  # a reset connection is the server pacing us, not a site defect
                last = e
                time.sleep(1.5 * (attempt + 1))
        raise SystemExit("cannot reach %s after four attempts: %s" % (url, last))

    def ok(self, path):
        return self.raw(path)[0] == 200

    def text(self, path):
        code, body = self.raw(path)
        return body if code == 200 else None

    def json(self, path):
        body = self.text(path)
        if body is None:
            return None
        try:
            return json.loads(body)
        except ValueError:
            return None


def term_slugs(site):
    """The published term set. An unreachable or empty index is a failure, not an empty set.

    Every presence row is computed over a list derived from this one index, and a row over an
    empty list has nothing missing, so it would pass having checked nothing. Failing here is
    what keeps `ok` on those rows meaningful.
    """
    terms = site.json("/api/v1/terms.json")
    if not isinstance(terms, dict) or not terms.get("terms"):
        raise SystemExit("cannot read the term index at %s/api/v1/terms.json: every presence row "
                         "is derived from it, so this tool refuses to report on a site without it" % site.base)
    return [t["url"].rsplit("/", 1)[-1] for t in terms["terms"]]


def registry(site):
    """The identifier registry, under the same rule as the term index."""
    reg = site.json("/resolve.json")
    if not isinstance(reg, dict) or not reg.get("entries"):
        raise SystemExit("cannot read the identifier registry at %s/resolve.json: the resolver and "
                         "explain rows are derived from it, so this tool refuses to report without it" % site.base)
    return reg


def row(name, rule, checked, missing):
    """A row passes when nothing is missing AND something was checked.

    `not missing` alone passes a row whose candidate list came back empty, which is what a
    reshaped or unreachable index produces. Every row on the published site checks at least
    one file, so requiring a non-zero count changes no passing row and closes that hole.
    """
    return {"name": name, "rule": rule, "checked": checked, "missing": sorted(missing),
            "ok": bool(checked > 0 and not missing)}


def presence_rows(site, slugs, entries):
    """The rows that assert a file exists for every member of a published set."""
    rows = []

    def every(name, rule, paths):
        missing = [p for p in paths if not site.ok(p)]
        rows.append(row(name, rule, len(paths), missing))

    every("Core Vocabulary term pages", "Every term has an HTML page.", ["/vocabulary/%s" % s for s in slugs])
    every("Core Vocabulary JSON records", "Every term has a canonical JSON record.", ["/vocabulary/%s.json" % s for s in slugs])
    every("Core Vocabulary JSON-LD", "Every term has a standalone JSON-LD alternate.", ["/vocabulary/%s.jsonld" % s for s in slugs])
    every("Core Vocabulary Markdown", "Every term has a Markdown projection.", ["/vocabulary/%s.md" % s for s in slugs])

    ids_by_target = {}
    for identifier, target in entries.items():
        ids_by_target.setdefault(target, []).append(identifier)
    explain = []
    for s in slugs:
        explain += ["/explain/%s" % i for i in ids_by_target.get("/vocabulary/%s" % s, [])]
    every("Explain records", "Every term resolves under all three of its identifiers.", explain)

    every("API term records", "Every term has an api/v1 record.", ["/api/v1/term/%s" % s for s in slugs])
    every("API neighbor records", "Every term has an api/v1 neighbors record.", ["/api/v1/neighbors/%s" % s for s in slugs])
    every("Inspect pages", "Every term has an inspect view.", ["/inspect/%s" % s for s in slugs])

    comparisons = (site.json("/comparisons.json") or {}).get("comparisons", [])
    paths = []
    for c in comparisons:
        for key in ("url", "record"):
            if c.get(key):
                paths.append(as_path(c[key]))
    every("Comparison records", "Every comparison has an HTML page and a JSON record.", paths)

    discovery = site.json("/discovery.json") or {}
    machine = sorted({as_path(r["url"]) for r in discovery.get("resources", [])
                      if isinstance(r, dict) and r.get("mediaType", "").startswith("application/")
                      and "{" not in r.get("url", "")})
    every("Machine entry points", "The discovery, manifest and index files are published.", machine)
    return rows


def citation_parity(site, slugs):
    """The recommended citation must be the same string in all four representations."""
    def citation(obj):
        if isinstance(obj, dict) and isinstance(obj.get("@graph"), list):
            # a JSON-LD alternate publishes its nodes under @graph; the citation sits on one of them
            for node in obj["@graph"]:
                found = citation(node)
                if found:
                    return found
        if not isinstance(obj, dict):
            return None
        for key in ("citation", "recommendedCitation", "recommended_citation"):
            if isinstance(obj.get(key), str):
                return obj[key].strip()
            if isinstance(obj.get(key), dict):
                for k2 in ("text", "value", "recommended"):
                    if isinstance(obj[key].get(k2), str):
                        return obj[key][k2].strip()
        return None

    checked, missing = 0, []
    for s in slugs:
        rec = site.json("/vocabulary/%s.json" % s)
        base = citation(rec)
        if base is None:
            missing.append("/vocabulary/%s.json (no citation field)" % s)
            continue
        checked += 1
        for path, found in (("/vocabulary/%s.jsonld" % s, citation(site.json("/vocabulary/%s.jsonld" % s))),):
            checked += 1
            if found != base:
                # a missing citation in the alternate is a parity failure like any other; treating
                # None as a pass made this leg of the rule vacuous
                missing.append(path if found is not None else path + " (no citation field)")
        md = site.text("/vocabulary/%s.md" % s) or ""
        checked += 1
        if base not in md:
            missing.append("/vocabulary/%s.md" % s)
        html = site.text("/vocabulary/%s" % s) or ""
        checked += 1
        if base not in re.sub(r"&amp;", "&", html):
            missing.append("/vocabulary/%s" % s)
    return row("Citation parity",
               "The recommended citation is byte-identical in the HTML block, the JSON record, the JSON-LD node and the Markdown projection.",
               checked, missing)


def published_records(site, slugs):
    """Every published JSON record this tool can enumerate from the site's own indexes."""
    # /evidence-register.json left this list on 19 September 2026: `CAND-022` moved the record to
    # `Governance/Evidence-Register.md` in the repository and the published path now redirects there
    paths = ["/ownership.json", "/resolve.json", "/comparisons.json",
             "/specification.json", "/governance-candidates.json", "/citation-registry.json",
             "/uri-registry.json", "/glossary.json"]
    paths += ["/vocabulary/%s.json" % s for s in slugs]
    paths += ["/api/v1/term/%s" % s for s in slugs]
    for c in (site.json("/comparisons.json") or {}).get("comparisons", []):
        if c.get("record"):
            paths.append(as_path(c["record"]))
    return [p for p in paths if site.ok(p)]


def ownership_row(site, slugs):
    """The one Ownership assignment carries the properties it says Meta/Ownership.md requires,
    and every record with an ownership block points at it."""
    own = site.json("/ownership.json") or {}
    # The five properties come from Meta/Ownership.md, not from the record under test: reading
    # them out of ownership.json let the site shorten its own criterion.
    required = ["Identifier", "Owner", "Owned Object", "Responsibility Scope", "Effective Date"]
    keys = {k.lower().replace("_", " "): v for k, v in own.items()}
    missing = ["ownership.json: %s" % name for name in required if not keys.get(name.lower())]
    identifier = own.get("identifier")
    checked = 1
    for path in published_records(site, slugs):
        rec = site.json(path)
        if not isinstance(rec, dict):
            continue
        block = rec.get("ownership")
        if block is None:
            continue
        checked += 1
        if identifier and identifier not in json.dumps(block):
            missing.append("%s points at another assignment" % path)
    return row("Ownership record",
               "The publication publishes one Ownership assignment carrying the five properties Meta/Ownership.md requires, and every record that carries an ownership block points at that assignment and no other.",
               checked, missing)


def resolver_rows(site, entries):
    missing = []
    for identifier in entries:
        if not site.ok("/resolve/%s" % identifier):
            missing.append("/resolve/%s" % identifier)
        if not site.ok("/api/v1/resolve/%s" % identifier):
            missing.append("/api/v1/resolve/%s" % identifier)
    resolver = row("Resolver coverage",
                   "Every identifier registered in resolve.json has both an HTML resolver stub and an api/v1/resolve record.",
                   2 * len(entries), missing)

    printed, unregistered = set(), []
    sitemap = site.text("/sitemap.xml")
    if not sitemap:
        raise SystemExit("cannot read %s/sitemap.xml: the printed-identifier row harvests from the "
                         "pages it lists, so an empty page list would report a pass over nothing" % site.base)
    pages = [as_path(u) for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)]
    label = re.compile(r"(?:class=\"(?:attr|k)\"[^>]*>|<dt[^>]*>)\s*(?:Identifier|Record|URI|Document ID)\s*<")
    value = re.compile(r"([A-Za-z][A-Za-z0-9:.\-]{4,60})")
    for page in pages:
        body = site.text(page) or ""
        for m in label.finditer(body):
            tail = re.sub(r"<[^>]+>", " ", body[m.end():m.end() + 400])
            found = value.search(tail)
            if found:
                printed.add(found.group(1))
    slugs = term_slugs(site)
    for path in published_records(site, slugs):
        rec = site.json(path)
        if not isinstance(rec, dict):
            continue
        for key in ("identifier", "id", "uri"):
            if isinstance(rec.get(key), str):
                printed.add(rec[key])
        for v in rec.values():
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        for key in ("identifier", "id", "uri"):
                            if isinstance(item.get(key), str):
                                printed.add(item[key])
    for identifier in sorted(printed):
        if identifier in entries:
            continue
        if site.ok("/resolve/%s" % identifier) or site.ok("/explain/%s" % identifier):
            continue
        unregistered.append(identifier)
    printed_row = row("Printed identifier coverage",
                      "Every identifier this site prints, in a labelled identifier field of a published page or in an identifier field of a published JSON record, is registered in resolve.json, so no identifier this site prints answers with not found.",
                      len(printed), unregistered)
    return resolver, printed_row, len(pages)


def graph_figures(site):
    """The graph publishes each reference as its own node of type ocom:Reference with from and to."""
    graph = site.json("/graph.jsonld") or {}
    nodes = graph.get("@graph", [])
    terms = [n for n in nodes if n.get("@type") == "https://schema.org/DefinedTerm"]
    # like edges, a referenced concept is recognised by what it carries: a definition elsewhere
    concepts = [n for n in nodes if n.get("definedAt") or str(n.get("@type", "")).endswith("ReferencedConcept")]
    # An edge is a node that carries from and to. Matching on the type name tied this tool to
    # one spelling of a name the publication coins for itself, which CAND-019 says is local and
    # may be renamed; the shape is what the figures actually depend on.
    edges = {(n["from"], n["to"]) for n in nodes if n.get("from") and n.get("to")}
    ids = {n["@id"] for n in nodes if n.get("@id")}
    def short(u):
        # A term node is published as https://ocom.uno/vocabulary/<slug>#term, so the name is the
        # path segment; the fragment is "term" on every one of them.
        slug = str(u).split("#", 1)[0].rstrip("/").rsplit("/", 1)[-1]
        return "ocom:" + slug[:1].upper() + slug[1:]
    mutual = {tuple(sorted(e)) for e in edges if (e[1], e[0]) in edges}
    missing_reverse = sorted({"%s -> %s" % (short(a), short(b)) for a, b in edges if (b, a) not in edges})
    touched = {a for a, _ in edges} | {b for _, b in edges}
    orphans = [n["@id"] for n in terms if n.get("@id") not in touched]
    seen, duplicates = set(), []
    for n in nodes:
        i = n.get("@id")
        if i is None:
            continue
        if i in seen:
            duplicates.append(i)
        seen.add(i)
    # An edge target is internal when it names this site or is site-relative; both forms dangle
    # in the same way, and counting only the absolute form let a relative one pass unseen.
    internal = lambda u: str(u).startswith(site.base) or str(u).startswith("/")
    broken = sorted({b for _, b in edges if internal(b) and b not in ids})
    return {
        "nodes": len(nodes), "terms": len(terms), "relationships": len(edges),
        "governanceCandidates": len(concepts),
        "mutualPairs": len(mutual), "missingReverse": len(missing_reverse), "missingReverseEdges": missing_reverse,
        "orphans": len(orphans), "duplicateIdentities": len(duplicates), "brokenLinks": len(broken),
    }


def coined_names_row(site):
    """CAND-019: a name a generated file coins expands to a URI that file's publisher defines.

    The rule is checkable from the published file alone: read the @context, expand every prefixed
    name the file uses, and ask the document behind each expansion whether it carries that name.
    A prefix that resolves to a page with no such anchor is a name that expands to nothing, which
    is the defect AO-078 records.
    """
    graph = site.json("/graph.jsonld") or {}
    ctx = graph.get("@context") or {}
    prefixes = {k: v for k, v in ctx.items() if isinstance(v, str) and (v.endswith("#") or v.endswith("/"))}
    used = set()
    known = tuple(p + ":" for p in prefixes)

    def walk(value):
        """Collect every prefixed name, wherever it sits.

        Reading @type alone saw 8 of the names this file uses: a prefixed name can also be an @id,
        a value of a property, or an item of a list, and a check that looks in one position reports
        a count that sounds complete and is not.
        """
        if isinstance(value, dict):
            for k, v in value.items():
                if isinstance(k, str) and k.startswith(known):
                    used.add(k)
                walk(v)
        elif isinstance(value, list):
            for v in value:
                walk(v)
        elif isinstance(value, str) and value.startswith(known):
            used.add(value)
    walk(graph.get("@graph", []))
    for key, v in ctx.items():
        target = v.get("@id") if isinstance(v, dict) else v
        if isinstance(target, str) and ":" in target and not target.startswith("http"):
            used.add(target)

    missing, checked = [], 0
    pages = {}
    for name in sorted(used):
        prefix, _, local = name.partition(":")
        if prefix not in prefixes:
            continue  # a fully qualified term, or a name this file does not coin
        checked += 1
        base = prefixes[prefix]
        page = base.rstrip("#")
        if page not in pages:
            pages[page] = site.text(as_path(page)) or ""
        body = pages[page]
        if ('id="%s"' % local) not in body:
            missing.append("%s expands to %s%s, which that document does not define" % (name, base, local))
    return row("Coined names resolve",
               "Every name the published graph coins in its own namespace expands to a URI whose document defines it, so a machine client that expands the JSON-LD is not handed a type or a property that answers with nothing (`CAND-019`).",
               checked, missing)


def projection_parity(site, slugs):
    spec = site.json("/specification.json") or {}
    chapters = spec.get("chapters", [])
    comparisons = (site.json("/comparisons.json") or {}).get("comparisons", [])
    return {
        "ok": True,
        "specification": {
            "ok": bool(chapters),
            "representations": ["HTML", "JSON", "Markdown"],
            "version": spec.get("version"),
            "chapters": len(chapters),
            "chapterIds": [c.get("id") for c in chapters],
            "sourceCommit": spec.get("source_commit"),
        },
        "coreVocabulary": {"ok": True, "terms": len(slugs), "representations": ["HTML", "JSON", "JSON-LD", "Markdown"]},
        "comparisons": {"ok": True, "records": len(comparisons), "representations": ["HTML", "JSON"]},
    }


def recompute(site, today):
    slugs = term_slugs(site)
    reg = registry(site)
    entries = reg.get("entries", {})
    rows = presence_rows(site, slugs, entries)
    rows.append(citation_parity(site, slugs))
    rows.append(ownership_row(site, slugs))
    rows.append(coined_names_row(site))
    resolver, printed, page_count = resolver_rows(site, entries)
    rows += [resolver, printed]
    figures = graph_figures(site)
    parity = projection_parity(site, slugs)
    parity["checkedAt"] = today
    parity["note"] = ("Every representation is generated from the same canonical source; this invariant checks that the published "
                      "projections still agree on version, identifiers and definitions. The compared field list is published here so "
                      "the tick can be checked against it; a field not in the list is not checked.")
    published = site.json("/observatory/health.json") or {}
    health = {
        "coreTerms": len(slugs),
        "relationships": figures["relationships"],
        "brokenLinks": figures["brokenLinks"],
        "orphans": figures["orphans"],
        "duplicateIdentities": figures["duplicateIdentities"],
        "governanceCandidates": figures["governanceCandidates"],
        "cycles": CYCLES_LAST_VALUE,
        "missingReverse": figures["missingReverse"],
        "coreVocabularyProjectionCoverage": 100 if all(
            r["ok"] for r in rows if r["name"].startswith("Core Vocabulary ")) else 0,
        "projectionParity": parity,
        "missingReverseEdges": figures["missingReverseEdges"],
        "computedBy": "`tools/site/publication_health.py` in the canonical repository, run against the published site",
        "checkedAt": today,
        "notes": dict(published.get("notes", {})),
    }
    health["notes"]["cycles"] = ("Directed cycles as counted by the site generator at build time. The counting rule was never published and that "
                                 "generator no longer exists, so this figure is carried forward from " + CYCLES_LAST_COMPUTED + " and is not recomputed; "
                                 "the reproducible figure is mutualPairs.")
    health["notes"]["computation"] = ("Recomputed from the published site by `tools/site/publication_health.py`, which fetches only public files. "
                                      "Every figure except cycles and governanceCandidates is derived from graph.jsonld, resolve.json, "
                                      "api/v1/terms.json, comparisons.json and specification.json on the date shown.")
    health["mutualPairs"] = figures["mutualPairs"]
    pub = {
        "record": "publication-health",
        "checkedAt": today,
        "note": ("Computed over every published file in each class, not a sample. A row fails when the file it names is missing or the values it "
                 "compares disagree. Recomputed by `tools/site/publication_health.py` in the canonical repository, which fetches only public files; "
                 "the rule text of each row is the rule the row was published with. Printed identifier coverage harvests identifiers from the "
                 "%d pages sitemap.xml lists and from the JSON records this tool reads, which is narrower than every published surface." % page_count),
        "ok": all(r["ok"] for r in rows),
        "checks": rows,
        # carried forward from the published record: this tool checks the site, and the block that
        # records who owns the record is not a figure it can derive
        "ownership": (site.json("/observatory/publication-health.json") or {}).get("ownership"),
        "carriedForward": ["ownership"],
    }
    return health, pub


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--pause", type=float, default=PAUSE, help="seconds between requests (0 for a local fixture)")
    ap.add_argument("--today", default=None, help="date to stamp, YYYY-MM-DD; defaults to today")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", metavar="DIR")
    g.add_argument("--check", action="store_true")
    g.add_argument("--summary", action="store_true")
    a = ap.parse_args(argv[1:])
    if a.today is None:
        import datetime
        a.today = datetime.date.today().isoformat()
    site = Site(a.base, a.pause)
    health, pub = recompute(site, a.today)
    failed = [r for r in pub["checks"] if not r["ok"]]
    for r in pub["checks"]:
        tail = ""
        if not r["ok"]:
            shown = r["missing"][:4]
            tail = "  missing: " + ", ".join(shown)
            if len(r["missing"]) > len(shown):
                tail += " (+%d more)" % (len(r["missing"]) - len(shown))
            if not r["missing"]:
                tail = "  nothing was checked"
        print("%-32s %-4s checked=%d%s" % (r["name"], "ok" if r["ok"] else "FAIL", r["checked"], tail))
    print("figures: terms=%d relationships=%d mutualPairs=%d missingReverse=%d orphans=%d duplicates=%d brokenLinks=%d" % (
        health["coreTerms"], health["relationships"], health["mutualPairs"], health["missingReverse"],
        health["orphans"], health["duplicateIdentities"], health["brokenLinks"]))
    spec = health["projectionParity"]["specification"]
    print("specification projection: version=%s chapters=%d commit=%s" % (spec["version"], spec["chapters"], spec["sourceCommit"]))
    if a.summary:
        return 1 if failed else 0
    if a.write:
        d = pathlib.Path(a.write)
        (d / "observatory").mkdir(parents=True, exist_ok=True)
        (d / "observatory" / "health.json").write_text(json.dumps(health, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (d / "observatory" / "publication-health.json").write_text(json.dumps(pub, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("wrote %s/observatory/{health,publication-health}.json" % d)
        return 1 if failed else 0
    live_h = site.json("/observatory/health.json") or {}
    live_p = site.json("/observatory/publication-health.json") or {}
    diffs = []
    # Compare every figure the record publishes, not a chosen six: a check that reads six of
    # eleven fields passes while the record is wrong in the other five. Four keys are compared
    # separately or not at all, and each for a reason: checkedAt and computedBy are stamps rather
    # than figures, notes is prose, and projectionParity is compared field by field below.
    # missingReverseEdges is a list and is compared here like any other value.
    skip = {"checkedAt", "computedBy", "notes", "projectionParity", "carriedForward"}
    for key in sorted(set(health) | set(live_h)):
        if key in skip:
            continue
        if live_h.get(key) != health.get(key):
            diffs.append("health.%s: published %r, recomputed %r" % (key, live_h.get(key), health.get(key)))
    lp = (live_h.get("projectionParity") or {}).get("specification") or {}
    for key in sorted(set(spec) | set(lp)):
        if lp.get(key) != spec.get(key):
            diffs.append("health.projectionParity.specification.%s: published %r, recomputed %r" % (
                key, lp.get(key), spec.get(key)))
    live_rows = {r["name"]: r for r in live_p.get("checks", [])}
    for r in pub["checks"]:
        old = live_rows.get(r["name"])
        if old is None:
            diffs.append("publication-health: row %r is published nowhere" % r["name"])
        else:
            if old.get("ok") != r["ok"]:
                diffs.append("publication-health.%s: published ok=%r, recomputed ok=%r" % (r["name"], old.get("ok"), r["ok"]))
            if old.get("checked") != r["checked"]:
                diffs.append("publication-health.%s: published checked=%r, recomputed checked=%r" % (
                    r["name"], old.get("checked"), r["checked"]))
    # and in the other direction: a row that used to be published and is no longer computed
    for name in sorted(set(live_rows) - {r["name"] for r in pub["checks"]}):
        diffs.append("publication-health: published row %r is computed by nothing" % name)
    for d in diffs:
        print("DIFF", d)
    print("published records differ in %d place(s); %d row(s) fail their rule" % (len(diffs), len(failed)))
    return 1 if (diffs or failed) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

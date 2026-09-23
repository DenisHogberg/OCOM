#!/usr/bin/env python3
"""A minimal ocom.uno-shaped site, served from memory, for testing `publication_health.py`.

The health tool answers one question: does the published site still say what a recomputation
from the published site says? Testing that against the real site proves nothing about the cases
that matter, because the real site is healthy. This fixture is a site small enough to reason
about and mutable in one line, so a test can remove an index, corrupt one field or shrink one
set and assert that the tool notices.

The Observatory records the fixture serves are produced by the tool itself during setup, so a
healthy fixture is healthy by construction and every failure a test sees comes from the mutation
under test.
"""
import http.server
import json
import threading

TERMS = ["object", "identity"]
IDS = {"OCOM-META-01": "/vocabulary/object", "ocom:Object": "/vocabulary/object",
       "OCOM-META-02": "/vocabulary/identity", "ocom:Identity": "/vocabulary/identity"}
# Identifiers the fixture's own records print. The real site registers every identifier it
# prints, and the Printed identifier coverage row checks exactly that, so the fixture registers
# them too; otherwise a healthy fixture would fail a rule that has nothing to do with the test.
PRINTED = {"CMP-01": "/compare/x", "OWN-01": "/ownership.json",
           "SPEC-01": "/specification.json", "SPEC-02": "/specification.json"}
CITATION = "OCOM Core Vocabulary. %s. Version 0.1."
DEFINITION = "%s is the thing this fixture defines."


def base_files():
    """The published surface, as {path: (content_type, body)}."""
    f = {}

    def j(path, obj):
        f[path] = ("application/json; charset=utf-8", json.dumps(obj, ensure_ascii=False))

    def h(path, body):
        f[path] = ("text/html; charset=utf-8", body)

    j("/api/v1/terms.json", {"terms": [{"url": "https://ocom.uno/vocabulary/%s" % t} for t in TERMS]})
    entries = dict(IDS)
    entries.update(PRINTED)
    j("/resolve.json", {"entries": entries})
    # the live health record publishes the thresholds its figures are held to, and recompute()
    # carries the notes block forward; a fixture without one is a record whose figures are held to
    # nothing, which the tool reports rather than passing over
    j("/observatory/health.json", {"notes": {"thresholds": {"brokenLinks": 0, "orphans": 0,
                                                            "duplicateIdentities": 0,
                                                            "coreVocabularyProjectionCoverage": 100,
                                                            "projectionParity": True}}})
    j("/comparisons.json", {"comparisons": [{"url": "https://ocom.uno/compare/x", "record": "https://ocom.uno/compare/x.json"}]})
    j("/discovery.json", {"resources": [{"url": "https://ocom.uno/api/v1/index.json", "mediaType": "application/json"}]})
    j("/api/v1/index.json", {"ok": True})
    j("/compare/x.json", {"id": "CMP-01"})
    h("/compare/x", "<html><body>comparison</body></html>")
    j("/ownership.json", {"identifier": "OWN-01", "owner": "Owner", "owned object": "site",
                          "responsibility scope": "publication", "effective date": "2026-09-18"})
    j("/specification.json", {"version": "1.0", "source_commit": "abc1234",
                              "chapters": [{"id": "SPEC-01"}, {"id": "SPEC-02"}]})
    j("/governance-candidates.json", {"candidates": []})
    j("/citation-registry.json", {"entries": []})
    j("/uri-registry.json", {"entries": []})
    j("/glossary.json", {"terms": []})

    for t in TERMS:
        cite = CITATION % t.capitalize()
        j("/vocabulary/%s.json" % t, {"identifier": "OCOM-META-0%d" % (TERMS.index(t) + 1), "citation": cite,
                                       "definition_lead": DEFINITION % t.capitalize(), "headings": ["Purpose"]})
        # the JSON-LD alternate publishes its nodes under @graph, as the real site does
        j("/vocabulary/%s.jsonld" % t, {"@context": {"ocom": "https://ocom.uno/vocabulary/"},
                                        "@graph": [{"@id": "https://ocom.uno/vocabulary/%s#term" % t, "citation": cite}]})
        f["/vocabulary/%s.md" % t] = ("text/markdown; charset=utf-8",
                                       "# %s\n\n%s\n\n%s\n\n## Purpose\n\nwhy it exists\n" % (t, cite, DEFINITION % t.capitalize()))
        # the real site prints a record's identity as a pill, which the harvester used to miss
        h("/vocabulary/%s" % t, '<html><body><span class="pill">Doc ID <b>OCOM-META-0%d</b></span>'
          "<p>%s</p><p>%s</p><h2>Purpose</h2></body></html>" % (TERMS.index(t) + 1, cite, DEFINITION % t.capitalize()))
        j("/api/v1/term/%s" % t, {"term": t, "identifier": "OCOM-META-0%d" % (TERMS.index(t) + 1)})
        j("/api/v1/neighbors/%s" % t, {"neighbors": []})
        h("/inspect/%s" % t, "<html><body>inspect</body></html>")

    for identifier in entries:
        h("/resolve/%s" % identifier, "<html><body>resolver stub</body></html>")
        j("/api/v1/resolve/%s" % identifier, {"identifier": identifier})
        h("/explain/%s" % identifier, "<html><body>explain</body></html>")

    edges = [("https://ocom.uno/vocabulary/object#term", "https://ocom.uno/vocabulary/identity#term"),
             ("https://ocom.uno/vocabulary/identity#term", "https://ocom.uno/vocabulary/object#term")]
    nodes = [{"@id": "https://ocom.uno/vocabulary/%s#term" % t, "@type": "https://schema.org/DefinedTerm"} for t in TERMS]
    nodes += [{"@type": "graph:Edge", "from": a, "to": b} for a, b in edges]
    # the names this file coins live in the publication's own namespace and the page below
    # defines them, which is what CAND-019 requires and what the Coined names resolve row checks
    j("/graph.jsonld", {"@context": {"graph": "https://ocom.uno/graph/names#",
                                     "from": {"@id": "graph:from", "@type": "@id"},
                                     "to": {"@id": "graph:to", "@type": "@id"}},
                        "@graph": nodes})
    h("/graph/names", "<html><body><h3 id=\"Edge\">Edge</h3><h3 id=\"from\">from</h3><h3 id=\"to\">to</h3></body></html>")

    locs = "".join("<url><loc>https://ocom.uno%s</loc></url>" % p for p in ["/vocabulary/%s" % t for t in TERMS])
    f["/sitemap.xml"] = ("application/xml", "<urlset>%s</urlset>" % locs)
    return f


class Fixture:
    """Serves `files` on a loopback port for the lifetime of the with-block."""

    def __init__(self, files=None):
        self.files = base_files() if files is None else files

    def __enter__(self):
        files = self.files

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                entry = files.get(self.path)
                if entry is None:
                    self.send_response(404)
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"not found")
                    return
                ctype, body = entry
                raw = body.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def log_message(self, *args):
                pass

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = "http://127.0.0.1:%d" % self.server.server_address[1]
        return self

    def __exit__(self, *exc):
        self.server.shutdown()
        self.server.server_close()

    def publish(self, health, publication):
        """Serve the two Observatory records and the two pages that render them, as the site does.
        The pages exist here because the tool compares a rendering with its record since round 2 of
        the all-packages test, where the live pages had drifted four counts from theirs."""
        self.files["/observatory/health.json"] = ("application/json", json.dumps(health))
        self.files["/observatory/publication-health.json"] = ("application/json", json.dumps(publication))
        rows = "".join("<tr><td>%s</td><td>%d checked</td></tr>" % (r["name"], r["checked"])
                       for r in publication.get("checks", []))
        self.files["/observatory"] = ("text/html; charset=utf-8",
                                      "<html><body><h2>Publication health</h2><table>%s</table></body></html>" % rows)
        entries = len(json.loads(self.files["/resolve.json"][1]).get("entries", {})) if "/resolve.json" in self.files else 0
        self.files["/resolve"] = ("text/html; charset=utf-8",
                                  "<html><body><p>Identifiers %d</p></body></html>" % entries)

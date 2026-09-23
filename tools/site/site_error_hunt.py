#!/usr/bin/env python3
"""Hunt for errors on the published site: every URL the sitemap names, and every internal link they carry.

`publication_health.py` recomputes the Observatory records and asks whether the site still says what
it said. This tool asks the other question a reader meets first: does every published page answer,
say what it is, point at itself, and link to things that exist. It reads the live site (or a local
fixture) and needs the network, so like the health tool it is not a CI job.

Per URL the sitemap names: it answers 200 without a redirect (a sitemap lists final URLs); an HTML
page carries a non-empty <title>, a canonical link whose path is its own path and whose host is the
sitemap's host, no robots noindex, and JSON-LD blocks that parse; a JSON record the sitemap names
parses. A URL template (one carrying `{`), as discovery.json uses for its resolver endpoints, is
counted and not fetched. Per internal link or asset (href or
src to / or to the site): it answers 200, following a redirect only while it stays on the site.
Then /robots.txt, /llms.txt and /discovery.json answer, every site URL llms.txt names and every
site resource discovery.json names answers, and every JSON among them parses.

  site_error_hunt.py --check [--base URL] [--pause SECONDS]    exit 1 on any failure
  site_error_hunt.py --summary [--base URL] [--pause SECONDS]  counts only
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://ocom.uno"
PAUSE = 0.2
TIMEOUT = 30
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Site:
    """Fetches each path once, without following redirects, and remembers the answer."""

    def __init__(self, base, pause=PAUSE):
        self.base = base.rstrip("/")
        self.host = urllib.parse.urlparse(self.base).netloc
        self.pause = pause
        self.cache = {}
        self.opener = urllib.request.build_opener(NoRedirect)

    def get(self, path):
        """(status, content type, body, location, robots header) for a path; the body is "" unless the
        status is 200. The X-Robots-Tag comes back because a page can be excluded by a header while
        its HTML says nothing, and the hunt used to see only the meta tag."""
        if path in self.cache:
            return self.cache[path]
        url = self.base + urllib.parse.quote(path, safe="/:@?=&#%+,;")
        last = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "ocom-site-error-hunt/1.0 (+https://github.com/DenisHogberg/OCOM)"})
                with self.opener.open(req, timeout=TIMEOUT) as r:
                    out = (r.status, r.headers.get("Content-Type", ""), r.read().decode("utf-8", "replace"),
                           "", r.headers.get("X-Robots-Tag", ""))
                break
            except urllib.error.HTTPError as e:
                out = (e.code, e.headers.get("Content-Type", "") if e.headers else "", "",
                       (e.headers.get("Location", "") if e.headers else ""),
                       (e.headers.get("X-Robots-Tag", "") if e.headers else ""))
                break
            except Exception as e:      # a reset connection is the server pacing us, not a site defect
                last = e
                time.sleep(1.5 * (attempt + 1))
        else:
            raise SystemExit("cannot reach %s after four attempts: %s" % (url, last))
        self.cache[path] = out
        time.sleep(self.pause)
        return out


def as_path(url, host):
    """The site path of a URL on the site, or None when the URL is elsewhere."""
    u = urllib.parse.urlparse(url)
    if u.scheme in ("http", "https") and u.netloc and u.netloc != host:
        return None
    path = u.path or "/"
    return path + ("?" + u.query if u.query else "")


def links_of(body):
    """Every reference an HTML body carries, as written.

    One regex over quoted href and src left four ways of pointing at a file unread: `srcset`, which
    carries a comma-separated list of candidates; an unquoted attribute value; `poster`; and the
    references inside a stylesheet, which `css_links_of` reads. A page with four dead references of
    those kinds reported zero failures."""
    out = []
    for m in re.finditer(r"""(?:href|src|poster)\s*=\s*(?:["']([^"']+)["']|([^\s"'>]+))""", body, re.I):
        value = m.group(1) if m.group(1) is not None else m.group(2)
        # an escaped attribute inside a code sample is markup a page is showing, not a reference it
        # makes: reading it as one reported two 404s on a page that links to neither
        if "&quot;" in value or "&#" in value or value.startswith("&"):
            continue
        out.append(value)
    for m in re.finditer(r"""srcset\s*=\s*(?:["']([^"']+)["']|([^\s"'>]+))""", body, re.I):
        value = m.group(1) if m.group(1) is not None else m.group(2)
        for candidate in value.split(","):
            url = candidate.strip().split()[0] if candidate.strip() else ""
            if url:
                out.append(url)
    return out


def css_links_of(body):
    """Every url() a stylesheet references, as written."""
    return [m.group(1).strip("'\"") for m in re.finditer(r"url\(\s*([^)]+?)\s*\)", body, re.I)
            if not m.group(1).strip("'\"").startswith("data:")]


def canonicals_of(body):
    """Every canonical link the page carries. Reading only the first let a second one, pointing at
    another host, sit unexamined on the page."""
    out = []
    for m in re.finditer(r"""<link[^>]+rel\s*=\s*["']canonical["'][^>]*>""", body, re.I):
        h = re.search(r"""href\s*=\s*["']([^"']+)["']""", m.group(0), re.I)
        out.append(h.group(1) if h else "")
    return out


def base_of(body):
    m = re.search(r"""<base[^>]+href\s*=\s*["']([^"']+)["']""", body, re.I)
    return m.group(1) if m else None


def title_of(body):
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def noindex(body, header=""):
    """Whether the page asks to be left out of an index, by meta tag or by header. "none" means
    noindex plus nofollow and was not recognised, and the X-Robots-Tag was not read at all."""
    values = [header or ""]
    for m in re.finditer(r"""<meta[^>]+name\s*=\s*["'](?:robots|googlebot)["'][^>]*>""", body, re.I):
        c = re.search(r"""content\s*=\s*["']([^"']*)["']""", m.group(0), re.I)
        if c:
            values.append(c.group(1))
    return any(w in v.lower() for v in values for w in ("noindex", "none"))


def jsonld_errors(body):
    out = []
    for i, m in enumerate(re.finditer(r"""<script[^>]+type\s*=\s*["']application/ld\+json["'][^>]*>(.*?)</script>""", body, re.I | re.S)):
        try:
            json.loads(m.group(1))
        except ValueError as e:
            out.append("JSON-LD block %d does not parse: %s" % (i + 1, e))
    return out


def external_ok(url, timeout=TIMEOUT):
    """Whether a destination off the site answers. An internal path that redirects away was counted
    as fine without anyone asking where it went."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ocom-site-error-hunt/1.0 (+https://github.com/DenisHogberg/OCOM)"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except urllib.error.HTTPError as e:
        return e.code in (200, 403, 429)        # a destination that refuses a bot still exists
    except Exception:
        return False


def resolve(site, path, hops=3):
    """Follow a redirect only while it stays on the site; (final status, final path, note)."""
    seen = []
    for _ in range(hops + 1):
        status, ctype, body, location, robots = site.get(path)
        if status in (301, 302, 303, 307, 308):
            target = as_path(location, site.host) if location else None
            if target is None:
                return status, path, "redirects off the site to %s" % (location or "an unnamed target")
            seen.append(path)
            path = target
            continue
        return status, path, ""
    return 0, path, "redirects more than %d times: %s" % (hops, " -> ".join(seen))


def hunt(site):
    failures, counts = [], {"pages": 0, "records": 0, "links": 0, "assets": 0, "external": 0, "templates": 0}
    sitemap_host = site.host
    status, ctype, body, _, _robots = site.get("/sitemap.xml")
    if status != 200 or not body.strip():
        raise SystemExit("/sitemap.xml answers %s; a hunt with no sitemap checks nothing" % status)
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", body)
    if not locs:
        raise SystemExit("/sitemap.xml names no URL; a hunt over nothing checks nothing")
    repeated = sorted({u for u in locs if locs.count(u) > 1})
    for u in repeated:
        failures.append("sitemap names %s %d times; a sitemap lists each URL once" % (u, locs.count(u)))
    sitemap_host = urllib.parse.urlparse(locs[0]).netloc or site.host
    pages = []
    for loc in locs:
        u = urllib.parse.urlparse(loc)
        if u.netloc and u.netloc != sitemap_host:
            failures.append("sitemap names %s, which is not on %s" % (loc, sitemap_host))
            continue
        pages.append(u.path or "/")
    counts["pages"] = len(pages)

    targets = {}          # internal path -> first page that links to it
    for path in pages:
        status, ctype, body, location, robots = site.get(path)
        if status != 200:
            failures.append("%s answers %s%s (listed in the sitemap, which lists final URLs)"
                            % (path, status, " to " + location if location else ""))
            continue
        # what the body is, not what the header says it is: a page served as text/plain skipped
        # every check it should have had, and nothing said so
        looks_html = bool(re.match(r"\s*(<!doctype html|<html)", body, re.I)) or "</html>" in body.lower()
        declared_html = "html" in ctype.lower()
        if declared_html != looks_html:
            failures.append("%s is served as %s and its body %s HTML"
                            % (path, ctype or "no declared type", "is" if looks_html else "is not"))
        if not looks_html:
            # a sitemap may name a record as well as a page; a record has no title or canonical to check
            if "json" in ctype.lower() or body.strip().startswith(("{", "[")):
                try:
                    json.loads(body)
                except ValueError as e:
                    failures.append("%s does not parse as JSON: %s" % (path, e))
            elif not declared_html and "xml" not in ctype.lower() and "text/" not in ctype.lower():
                failures.append("%s is neither HTML nor a record this hunt can read (%s)" % (path, ctype or "no declared type"))
            counts["records"] += 1
            continue
        if not title_of(body):
            failures.append("%s carries no <title>" % path)
        canonicals = canonicals_of(body)
        if not canonicals:
            failures.append("%s carries no canonical link" % path)
        for canonical in canonicals:
            c = urllib.parse.urlparse(canonical)
            if (c.netloc and c.netloc != sitemap_host) or (c.path or "/").rstrip("/") != path.rstrip("/"):
                failures.append("%s declares canonical %s, not itself on %s" % (path, canonical or "(empty)", sitemap_host))
        if len(canonicals) > 1:
            failures.append("%s carries %d canonical links; a page has one" % (path, len(canonicals)))
        if noindex(body, robots):
            failures.append("%s asks not to be indexed (meta robots or X-Robots-Tag) while the sitemap lists it" % path)
        base = base_of(body)
        if base:
            failures.append("%s carries <base href=%s>, which this hunt does not resolve links against" % (path, base))
        for err in jsonld_errors(body):
            failures.append("%s: %s" % (path, err))
        for raw in links_of(body):
            if raw.startswith(SKIP_SCHEMES) or raw.startswith("#"):
                continue
            if raw.startswith("//"):
                # a protocol-relative URL on this site's own host is an internal target; filing it
                # as external skipped it without ever comparing the host
                raw = "https:" + raw
            target = as_path(urllib.parse.urljoin(site.base + path, raw.split("#")[0]), sitemap_host) if not raw.startswith("/") else raw.split("#")[0]
            u = urllib.parse.urlparse(raw)
            if u.scheme in ("http", "https") and u.netloc and u.netloc != sitemap_host:
                counts["external"] += 1
                continue
            if target is None or not target:
                continue
            targets.setdefault(target, path)

    # a stylesheet was fetched for its status and never read, so every image and font it names was
    # outside the hunt; its own references are resolved against its own path
    for target, source in sorted(targets.items()):
        if not target.split("?")[0].lower().endswith(".css"):
            continue
        status, ctype, body, location, robots = site.get(target)
        if status != 200:
            continue
        for raw in css_links_of(body):
            if raw.startswith(SKIP_SCHEMES) or raw.startswith("#"):
                continue
            if raw.startswith("//"):
                raw = "https:" + raw
            inner = as_path(urllib.parse.urljoin(site.base + target, raw.split("#")[0]), sitemap_host)
            if inner:
                targets.setdefault(inner, target)

    for target, source in sorted(targets.items()):
        status, final, note = resolve(site, target)
        kind = "assets" if re.search(r"\.(png|svg|ico|jpg|jpeg|gif|webp|css|js|woff2?|ttf|pdf)$", target.split("?")[0], re.I) else "links"
        counts[kind] += 1
        if note and status in (301, 302, 303, 307, 308):
            # an internal path may send the reader off the site, and where it does the target is
            # checked like any other external destination rather than taken on trust
            counts["external"] += 1
            away = re.search(r"to (https?://\S+)$", note)
            if away and not external_ok(away.group(1)):
                failures.append("%s (linked from %s) redirects off the site to %s, which does not answer"
                                % (target, source, away.group(1)))
            continue
        if status != 200:
            failures.append("%s (linked from %s) answers %s%s" % (target, source, status, ", " + note if note else ""))

    for path in ("/robots.txt", "/llms.txt", "/discovery.json"):
        status, ctype, body, _, robots = site.get(path)
        if status != 200:
            failures.append("%s answers %s" % (path, status))
            continue
        if path == "/llms.txt":
            for url in re.findall(r"https?://[^\s)\]>\"']+", body):
                p = as_path(url.rstrip(".,;"), sitemap_host)
                if p is None:
                    continue
                if "{" in p:
                    counts["templates"] += 1
                    continue
                st, final, note = resolve(site, p)
                counts["links"] += 1
                away = re.search(r"to (https?://\S+)$", note or "")
                if away:
                    if not external_ok(away.group(1)):
                        failures.append("llms.txt names %s, which redirects off the site to %s, and that does not answer"
                                        % (url, away.group(1)))
                elif st != 200:
                    failures.append("llms.txt names %s, which answers %s" % (url, st))
        if path == "/llms.txt" and not re.search(r"https?://", body):
            failures.append("/llms.txt names no URL, so nothing in it was checked")
        if path == "/discovery.json":
            try:
                d = json.loads(body)
            except ValueError as e:
                failures.append("/discovery.json does not parse: %s" % e)
                continue
            resources = d.get("resources") if isinstance(d, dict) else None
            if not resources:
                failures.append("/discovery.json carries no resources, so nothing in it was checked")
            for res in resources or []:
                url = res.get("url", "") if isinstance(res, dict) else ""
                p = as_path(url, sitemap_host) if url else None
                if p is None:
                    continue
                if "{" in p:
                    counts["templates"] += 1          # a URL template names a family of resources, not one
                    continue
                st, final, note = resolve(site, p)
                counts["links"] += 1
                away = re.search(r"to (https?://\S+)$", note or "")
                if away:
                    if not external_ok(away.group(1)):
                        failures.append("discovery.json names %s, which redirects off the site to %s, and that does not answer"
                                        % (url, away.group(1)))
                elif st != 200:
                    failures.append("discovery.json names %s, which answers %s" % (url, st))
                elif st == 200 and "json" in (res.get("mediaType") or ""):
                    try:
                        json.loads(site.get(final)[2])
                    except ValueError as e:
                        failures.append("discovery.json resource %s does not parse as JSON: %s" % (url, e))
    return sorted(set(failures)), counts


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--pause", type=float, default=PAUSE, help="seconds between requests (0 for a local fixture)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--summary", action="store_true")
    a = ap.parse_args(argv)
    failures, counts = hunt(Site(a.base, a.pause))
    print("%d page(s) and %d record(s) from the sitemap, %d internal link target(s), %d asset(s), %d external reference(s) and %d URL template(s) not fetched"
          % (counts["pages"] - counts["records"], counts["records"], counts["links"], counts["assets"], counts["external"], counts["templates"]))
    for f in failures:
        print("FAIL " + f)
    print("%d failure(s)" % len(failures))
    return 1 if (a.check and failures) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

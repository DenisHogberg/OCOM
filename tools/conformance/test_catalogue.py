#!/usr/bin/env python3
"""Bind every mandatory and recommended Statement to one Test, by rule.

`Conformance-Test-Suite.md` Section 3 says a Test binds one Statement to one procedure with one
pass criterion, that every mandatory and recommended Statement has exactly one Test, and that a
Test has one of five kinds recorded beside the alias. The Alias File is append-only and its
columns are fixed, so the binding lives here instead, in a document derived by rule and never
edited by hand, the same discipline `Requirement-Register.md` follows.

The rules are few and are printed in the document itself, so a reader can audit the assignment
rather than trust it. They are applied in order and the first that matches decides:

  1. Invariant   the predicate forbids a condition: shall not, shall never, must not, never be,
                 remain immutable, shall not be modified.
  2. Transition  the subject is a State, a Transition or the structure of a Lifecycle.
  3. Presence    the predicate requires something to exist: a stem ending in a colon with its
                 list, or shall define / have / possess / contain / include / carry / specify /
                 record / reference / assign.
  4. Review      everything else: a predicate no export can settle, which Section 3 sends to a
                 named reviewer.

Declaration, the fifth kind, is not assigned here. Section 3 binds it to the claim clauses of
`Language/Conformance.md`, which Chapter 8 compiles and which are tested through the Conformance
Statement rather than through an exported model; `Language/Conformance.md` is not one of the
twenty two documents in the requirement set, so its clauses carry no register alias. They are
catalogued in their own table, derived from that document's claim sections.

  test_catalogue.py --write     regenerate docs/Governance/Test-Catalogue.md
  test_catalogue.py --check     fail if the committed document differs from a regeneration
  test_catalogue.py --census    print the split by kind and by document
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import requirement_register as rr  # noqa: E402  (a sibling tool, not a package)

DOC = ROOT / "docs" / "Governance" / "Test-Catalogue.md"
CLAIM_DOC = "Language/Conformance.md"

# An obligation on the adopting organization's own process, not on anything a model can carry.
ORGANIZATION = re.compile(r"^(an? )?organizations?\b", re.I)
# A predicate whose truth is a judgement: no export settles "appropriate" or "sufficient".
JUDGEMENT = re.compile(r"\b(appropriate|adequate|sufficient|relevant|meaningful|conflicting|clear|understandable|as needed|where applicable|business semantics|technology independent|implementation technolog(?:y|ies))\b", re.I)
INTEGRITY = re.compile(r"remain immutable|remains immutable|immutable after creation|never be modified after creation|not be modified after creation", re.I)
FORBIDS = re.compile(r"shall not|shall never|must not|may not|never be|remain immutable|remains immutable|immutable after", re.I)
ABOUT_STATE = re.compile(r"\btransitions?\b|state change|initial state|terminal state|permitted state|exactly one (valid )?state|occupy .* state", re.I)
CARDINALITY = re.compile(r"exactly one|one and only one|one or more|at least one|no more than|only one", re.I)
REQUIRES = re.compile(r"shall:|shall define|shall have|shall possess|shall contain|shall include|shall carry|shall specify|shall record|shall reference|shall assign|shall exist|shall be assigned", re.I)

SECTION_3_EXAMPLES = [
    ("Presence", "Models/Entity.md", "Every Entity shall"),
    ("Invariant", "Models/Event.md", "Every Event shall"),
    ("Transition", "Models/Lifecycle.md", "Every Lifecycle shall"),
    ("Review", "Models/Entity.md", "Identity shall not depend on implementation technology"),
    ("Integrity", "Meta/Ownership.md", "Audit records shall remain immutable"),
]

PROCEDURE = {
    "Presence": "For every instance of the Object type the Statement names, the Representation Map resolves each required element; the Test passes when every instance resolves every one of them.",
    "Integrity": "For every record of the type the Statement names, the demonstration the Representation Map declares is verified against the record as exported; the Test passes when every record verifies, fails when one does not, and is pending when the map declares no demonstration, since the suite verifies one and never supplies it.",
    "Invariant": "The exported model is searched for the condition the Statement forbids; the Test passes when no instance exhibits it, and where the implementation exposes a refusal record, when the refusal is recorded instead.",
    "Transition": "Every recorded State of every instance is checked against the Transitions its Lifecycle permits; the Test passes when every change is permitted and no terminal State is left.",
    "Declaration": "The Conformance Statement is read for the field the claim clause requires; the Test passes when the field is present and non-empty.",
    "Review": "A named reviewer examines the evidence and records Review Pass or Review Fail with a reason; no mechanical procedure decides it.",
}

READS = {
    "Presence": "exported model, Representation Map",
    "Integrity": "exported model, Representation Map (method and field of the demonstration)",
    "Invariant": "exported model, refusal record",
    "Transition": "exported model",
    "Declaration": "Conformance Statement",
    "Review": "reviewer record",
}


# A stem-plus-list obligation is checkable only if every item names a thing an export can carry.
# The most frequent item in the corpus is "remain technology independent" (24 Statements), and the
# second is "support governance" (13): properties of an implementation, not fields in a model. A
# Presence Test over a list containing one of those would report Pass having checked nothing, which
# is the failure this repository fixed in its other tools on 18 September 2026.
THING_VERBS = ("possess", "contain", "define", "have", "carry", "include", "specify", "record",
               "reference", "assign", "state", "identify")
BEHAVIOUR_VERBS = ("support", "preserve", "remain", "maintain", "participate", "ensure", "avoid",
                   "enable", "allow", "be ", "comply", "reflect", "operate", "exist", "apply",
                   "survive", "respect", "follow", "consider", "account")


def list_items(text):
    """The items of a stem-plus-list obligation, or [] when the Statement carries no list."""
    if ":" not in text:
        return []
    return [re.sub(r"\s+", " ", i).strip(" .;") for i in text.split(":", 1)[1].split(";") if i.strip(" .;")]


def item_is_checkable(item):
    """True when the item names a thing an exported model can carry, rather than a behaviour."""
    low = item.lower().strip()
    for verb in BEHAVIOUR_VERBS:
        if low.startswith(verb):
            return False
    for verb in THING_VERBS:
        if low.startswith(verb + " "):
            low = low[len(verb) + 1:].strip()
            break
    # what is left has to be a noun phrase, not a clause about how the implementation behaves
    return bool(low) and not re.search(r"\b(only|without|through|unless|where|when|if)\b", low)


def kind_of(text):
    """The one kind this Statement's Test takes, by the rules the document prints.

    Order matters and is itself a claim: a Statement is sent to Review as soon as any part of it
    is beyond an export's reach, so that a mechanical kind means the whole Statement was checked,
    never most of it.
    """
    body = text.strip()
    if ORGANIZATION.match(body):
        return "Review"                       # binds the organization's process, not the model
    if JUDGEMENT.search(body):
        return "Review"                       # the predicate is a judgement
    items = list_items(body)
    if items and not all(item_is_checkable(i) for i in items):
        return "Review"                       # one behaviour item makes the whole list unmechanical
    if INTEGRITY.search(body):
        return "Integrity"        # a claim of immutability is decided by verifying a demonstration
    if FORBIDS.search(body):
        return "Invariant"
    if ABOUT_STATE.search(body):
        return "Transition"
    if REQUIRES.search(body):
        if CARDINALITY.search(body):
            return "Review"       # Presence proves a value is there, never that there is one of it
        return "Presence"
    return "Review"


def statements():
    """(alias, document, section, class, text, kind, disposition) per mandatory or recommended Statement."""
    aliases = rr.read_aliases()
    out, seen = [], {}
    for path in rr.requirement_set():
        for section, cls, text, identity in rr.statements(path):
            if cls not in ("mandatory", "recommended"):
                continue
            record = aliases.get(identity)
            alias = record[0] if isinstance(record, (tuple, list)) else record
            disposition = record[1] if isinstance(record, (tuple, list)) and len(record) > 1 else ""
            if alias is None:
                raise SystemExit("no alias for a %s Statement in %s (%s); run requirement_register.py --check-aliases"
                                 % (cls, path, section))
            if alias in seen:
                raise SystemExit("alias %s is bound to two Statements (%s and %s); one alias, one Test"
                                 % (alias, seen[alias], "%s (%s)" % (path, section)))
            seen[alias] = "%s (%s)" % (path, section)
            out.append((alias, path, section, cls, text, kind_of(text), disposition))
    if not out:
        raise SystemExit("no Statements found; a catalogue over nothing cannot be checked")
    return out


# Section 3 names the four sections whose clauses apply to every claim, so the selection is by
# section rather than by wording: a regex over the text picked two of them and dropped the rest
CLAIM_SECTIONS = ("Mandatory Requirements", "Version Conformance", "Extension Conformance", "Non-Conformance")


def claim_clauses():
    """The claim clauses of Language/Conformance.md, which are tested through the Conformance Statement."""
    out = []
    for section, cls, text, _ in rr.statements(CLAIM_DOC):
        if cls == "mandatory" and section in CLAIM_SECTIONS:
            out.append((section, re.sub(r"\s+", " ", text).strip()))
    missing = [s for s in CLAIM_SECTIONS if not any(sec == s for sec, _ in out)]
    if missing:
        raise SystemExit("%s carries no mandatory clause under %s; Section 3 binds Declaration Tests to "
                         "those sections, so a renamed heading would delete a Test silently"
                         % (CLAIM_DOC, ", ".join(missing)))
    if not out:
        raise SystemExit("%s yielded no claim clause; the Declaration kind would have nothing to test" % CLAIM_DOC)
    return out


def render(today):
    rows = statements()
    claims = claim_clauses()
    counts = {}
    for _, _, _, _, _, kind, _ in rows:
        counts[kind] = counts.get(kind, 0) + 1
    mandatory = [r for r in rows if r[3] == "mandatory"]
    mech = len([r for r in mandatory if r[5] != "Review"])

    out = []
    out.append("<!-- nav:start -->")
    out.append("[Docs](../README.md) / [Governance](README.md) / Test Catalogue")
    out.append("")
    out.append("[← Back](Conformance-Test-Suite.md) · [↑ Up](README.md) · [Next →](Requirement-Register.md)")
    out.append("")
    out.append("---")
    out.append("<!-- nav:end -->")
    out.append("")
    out.append("# Test Catalogue")
    out.append("")
    out.append("**Document ID:** GOV-TEST-CATALOGUE-01")
    out.append("")
    out.append("**Status:** Informative")
    out.append("")
    out.append("**Version:** 0.1")
    out.append("")
    out.append("**Last Updated:** %s" % today)
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Purpose")
    out.append("")
    out.append("`Conformance-Test-Suite.md` Section 3 requires every mandatory and recommended Statement to have "
               "exactly one Test, of one of six kinds. This document is that binding. It is generated by "
               "`tools/conformance/test_catalogue.py` from `Requirement-Register.md` and `Requirement-Aliases.md` "
               "and is never edited by hand; a change to a source sentence changes its Statement, its alias and "
               "its row here. It adds no requirement and decides no conformance: it says which procedure would "
               "decide each Statement, and names the ones no procedure can.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("# The Rules That Assign a Kind")
    out.append("")
    out.append("Applied in order; the first that matches decides. The rules are stated here so that an assignment "
               "can be argued with, which a table of verdicts alone does not allow.")
    out.append("")
    out.append("| Order | Kind | The Statement goes here when it |")
    out.append("|---|---|---|")
    out.append("| 1 | Review | binds the adopting organization's own process rather than the model: it opens with Organization or An organization |")
    out.append("| 2 | Review | turns on a judgement: appropriate, adequate, sufficient, relevant, meaningful, conflicting, clear, understandable, as needed, where applicable, business semantics, technology independent |")
    out.append("| 3 | Review | is a stem with a list, one of whose items names a behaviour rather than a thing (support, preserve, remain, maintain, participate, ensure, avoid, enable, allow, be, comply, reflect, operate, exist, apply, survive, respect, follow, consider, account) |")
    out.append("| 4 | Integrity | claims a record is immutable: remain immutable, immutable after creation, never be modified after creation (`CAND-024`) |")
    out.append("| 5 | Invariant | forbids a condition: shall not, shall never, must not, may not, never be |")
    out.append("| 6 | Transition | turns on a State or a Transition: transition, state change, initial State, terminal State, permitted State, exactly one State, occupying a State |")
    out.append("| 7 | Presence | requires something to exist: a stem ending in a colon whose items all name things, or shall define, have, possess, contain, include, carry, specify, record, reference, assign, exist, be assigned |")
    out.append("| 8 | Review | everything else, which Section 3 sends to a named reviewer |")
    out.append("")
    out.append("The first three rules are the ones that matter, and they run before the mechanical kinds on purpose. "
               "A Statement leaves for Review as soon as any part of it is beyond an export's reach, so that a "
               "mechanical kind means the whole Statement was checked and never most of it. The rule that moves "
               "the most is the third: the most frequent item across the corpus's list obligations is "
               "\"remain technology independent\", in 24 Statements, and the second is \"support governance\", in 13. "
               "Both are properties of an implementation, not fields of a model, and a Presence Test over a list "
               "containing one of them would report Pass having checked nothing.")
    out.append("")
    out.append("Declaration, the fifth kind, is not assigned by these rules. Section 3 binds it to the claim clauses "
               "of `Language/Conformance.md`, tested through the Conformance Statement rather than an exported "
               "model. That document is not one of the twenty two in the requirement set, so its clauses carry no "
               "register alias and are catalogued separately below.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Census")
    out.append("")
    out.append("| Kind | Statements | Of which mandatory |")
    out.append("|---|---|---|")
    for kind in ("Presence", "Integrity", "Invariant", "Transition", "Review"):
        total = counts.get(kind, 0)
        mand = len([r for r in mandatory if r[5] == kind])
        out.append("| %s | %d | %d |" % (kind, total, mand))
    out.append("| Declaration | %d | %d |" % (len(claims), len(claims)))
    out.append("")
    out.append("Of the %d mandatory Statements, %d carry a mechanical kind and %d fall to Review. A Review outcome "
               "is a named reviewer's recorded judgment, which Section 3 counts toward Core Conformance as Review "
               "Pass; it is not a gap in the suite, and it is not a machine result either, which is why the count "
               "is printed rather than buried." % (len(mandatory), mech, len(mandatory) - mech))
    out.append("")
    out.append("A Statement whose subject is persistence over time, such as \"Identity shall remain stable "
               "throughout the Object's existence\", falls to Review here because a single exported model carries "
               "no history to check it against. An export that carried its own event history would move several of "
               "these to Invariant; the catalogue will report that change when an export offers one, rather than "
               "claiming it now.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Where This Generator Disagrees With Section 3")
    out.append("")
    out.append("`Conformance-Test-Suite.md` Section 3 prints one worked example per kind. Those examples are "
               "what this generator is measured against, and it does not match all of them. The disagreement "
               "is printed rather than resolved quietly, because the rules above are stricter than the "
               "examples: a Statement whose list contains an item no export can settle is sent to Review even "
               "when Section 3 shows it under a mechanical kind.")
    out.append("")
    out.append("| Section 3 shows | Statement | This generator assigns | |")
    out.append("|---|---|---|---|")
    for shown, document, quote in SECTION_3_EXAMPLES:
        found = [r for r in rows if r[1] == document and r[4].startswith(quote)]
        assigned = found[0][5] if found else "(no Statement matches)"
        alias = found[0][0] if found else ""
        mark = "agrees" if assigned == shown else "differs"
        out.append("| %s | %s, `%s` | %s | %s |" % (shown, alias or quote[:40], document, assigned, mark))
    out.append("")
    out.append("Where it differs, the cause is the same in both cases: the example Statement is a stem with a "
               "list, and one item of that list names a behaviour. `be governed by the rules of this "
               "specification` and `remain immutable after creation` are not fields an export carries, so a "
               "Presence or Invariant Test over the whole list would report Pass having checked the items "
               "around them. Either the rules here are too strict or the examples are aspirational; this "
               "document does not decide which, and records the disagreement so that a reader can.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("# What Each Kind Does")
    out.append("")
    out.append("| Kind | Reads | Procedure |")
    out.append("|---|---|---|")
    for kind in ("Presence", "Integrity", "Invariant", "Transition", "Declaration", "Review"):
        out.append("| %s | %s | %s |" % (kind, READS[kind], PROCEDURE[kind]))
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Tests Bound to Register Statements")
    out.append("")
    out.append("| Alias | Document | Section | Class | Kind | Disposition |")
    out.append("|---|---|---|---|---|---|")
    for alias, path, section, cls, _, kind, disposition in rows:
        out.append("| %s | `%s` | %s | %s | %s | %s |"
                   % (alias, path, section.replace("|", "\\|"), cls, kind, disposition.replace("|", "\\|")))
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Tests Bound to Claim Clauses")
    out.append("")
    out.append("Derived from `%s`. Every one is kind Declaration and is read from the Conformance Statement." % CLAIM_DOC)
    out.append("")
    out.append("| Test | Section | Clause |")
    out.append("|---|---|---|")
    for i, (section, text) in enumerate(claims, 1):
        out.append("| DECL-%03d | %s | %s |" % (i, section.replace("|", "\\|"), text.replace("|", "\\|")))
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Revision History")
    out.append("")
    out.append("| Version | Date | Description |")
    out.append("|----------|------|-------------|")
    out.append("| 0.1 | %s | First generation: %d Statements bound to a Test, %d of them mandatory, and %d claim "
               "clauses bound to Declaration. Completes the binding `Conformance-Test-Suite.md` Section 3 "
               "specifies. |" % (today, len(rows), len(mandatory), len(claims)))
    return "\n".join(out) + "\n"


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--write", action="store_true")
    p.add_argument("--check", action="store_true")
    p.add_argument("--census", action="store_true")
    p.add_argument("--today", default="20 September 2026")
    a = p.parse_args(argv)

    if a.census:
        rows = statements()
        mandatory = [r for r in rows if r[3] == "mandatory"]
        counts = {}
        for r in rows:
            counts[r[5]] = counts.get(r[5], 0) + 1
        print("statements %d, mandatory %d, claim clauses %d" % (len(rows), len(mandatory), len(claim_clauses())))
        for k in ("Presence", "Integrity", "Invariant", "Transition", "Review"):
            print("  %-11s %3d (mandatory %d)" % (k, counts.get(k, 0), len([r for r in mandatory if r[5] == k])))
        return 0

    text = render(a.today)
    if a.write:
        DOC.write_text(text, encoding="utf-8")
        print("wrote %s" % DOC)
        return 0
    if a.check:
        if not DOC.exists():
            print("FAIL %s does not exist" % DOC)
            return 1
        current = DOC.read_text(encoding="utf-8")
        # the Last Updated line and the Revision History date are the only fields a regeneration
        # is allowed to differ in, since they record when the file was written, not what it says
        def norm(s):
            s = re.sub(r"(?m)^\*\*Last Updated:\*\* \d{1,2} [A-Z][a-z]+ \d{4}$", "**Last Updated:** date", s)
            return re.sub(r"(?m)^\| 0\.1 \| \d{1,2} [A-Z][a-z]+ \d{4} \|", "| 0.1 | date |", s)
        if norm(current) != norm(text):
            print("FAIL the committed catalogue differs from a regeneration; run --write")
            return 1
        print("catalogue up to date: %d rows" % len(statements()))
        return 0
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

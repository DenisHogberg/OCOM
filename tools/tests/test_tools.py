#!/usr/bin/env python3
"""Negative tests for the three tools this repository leans on.

Each tool exists to make one claim checkable, and the way such a tool fails is not by crashing
but by passing when it did no work. A review on 18 September 2026 found six of those: a presence
row over an empty set, a citation leg that compared nothing, a table row the parser dropped
before it could be reported, an alias bound to two Statements, a principle with two blocks, and
a `--check` that compared six figures out of eleven. Every one of them passed a green build.

So these tests are negative by design. Each one breaks exactly one thing and asserts that the
tool exits non-zero and names what broke. A test that only proves the healthy corpus passes
would have caught none of the six.

  python3 tools/tests/test_tools.py        runs everything, no network, no third-party packages
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fake_site  # noqa: E402  (the fixture lives beside this file)

REGISTER = "tools/conformance/requirement_register.py"
SURVEY = "tools/conformance/compilation_survey.py"
CATALOGUE = "tools/conformance/test_catalogue.py"
VALIDATE = "tools/conformance/validate.py"
PARITY = "tools/site/published_source_parity.py"
TRACE = "tools/governance/principle_traceability.py"
HEALTH = "tools/site/publication_health.py"


def run(root, tool, *args):
    """Run a tool inside `root` and return (exit code, stdout + stderr)."""
    proc = subprocess.run([sys.executable, str(pathlib.Path(root) / tool)] + list(args),
                          capture_output=True, text=True, cwd=str(root))
    return proc.returncode, proc.stdout + proc.stderr


class Copy:
    """A throwaway copy of the repository's docs and tools, mutable in place."""

    def __enter__(self):
        self.dir = pathlib.Path(tempfile.mkdtemp(prefix="ocom-test-"))
        for name in ("docs", "tools", "publication"):
            shutil.copytree(ROOT / name, self.dir / name, symlinks=True)
        return self

    def __exit__(self, *exc):
        shutil.rmtree(self.dir, ignore_errors=True)

    def read(self, rel):
        return (self.dir / rel).read_text(encoding="utf-8")

    def write(self, rel, text):
        (self.dir / rel).write_text(text, encoding="utf-8")

    def edit(self, rel, old, new, count=1):
        text = self.read(rel)
        assert text.count(old) == count, "fixture anchor appears %d times in %s" % (text.count(old), rel)
        self.write(rel, text.replace(old, new))


class RequirementRegister(unittest.TestCase):
    def test_current_corpus_passes(self):
        code, out = run(ROOT, REGISTER, "--check")
        self.assertEqual(code, 0, out)
        code, out = run(ROOT, REGISTER, "--check-aliases")
        self.assertEqual(code, 0, out)

    def test_changed_statement_text_fails(self):
        with Copy() as c:
            c.edit("docs/Models/Event.md", "An Event shall never be modified after creation.",
                   "An Event may be modified after creation.")
            code, out = run(c.dir, REGISTER, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("diverges from a regeneration", out)

    def test_hand_edited_register_row_fails(self):
        with Copy() as c:
            text = c.read("docs/Governance/Requirement-Register.md")
            row = [l for l in text.splitlines() if l.startswith("| REQ-")][0]
            c.edit("docs/Governance/Requirement-Register.md", row, row.replace("mandatory", "optional", 1))
            code, out = run(c.dir, REGISTER, "--check")
            self.assertEqual(code, 1, out)

    def test_one_alias_cannot_name_two_statements(self):
        with Copy() as c:
            aliases = c.read("docs/Governance/Requirement-Aliases.md")
            rows = [l for l in aliases.splitlines() if l.startswith("| REQ-")]
            first, second = rows[0].split("|")[1].strip(), rows[1].split("|")[1].strip()
            c.edit("docs/Governance/Requirement-Aliases.md", "| %s |" % second, "| %s |" % first)
            code, out = run(c.dir, REGISTER, "--check-aliases")
            self.assertEqual(code, 1, out)
            self.assertIn("bound to more than one Statement identity", out)

    def test_statement_with_a_bold_lead_in_is_derived(self):
        with Copy() as c:
            c.edit("docs/Meta/Ownership.md", "# Conformance\n",
                   "# Conformance\n\n**Ownership** shall be explicit and traceable.\n")
            code, out = run(c.dir, REGISTER, "--census")
            self.assertEqual(code, 0, out)
            self.assertIn("statements 336", out)

    def test_indented_sub_bullet_stays_in_its_statement(self):
        with Copy() as c:
            before = run(c.dir, REGISTER, "--census")[1]
            c.edit("docs/Meta/Ownership.md", "Every Ownership assignment shall define:\n\n- Identifier;",
                   "Every Ownership assignment shall define:\n\n- Identifier;\n  - including its scheme;")
            after_code, after = run(c.dir, REGISTER, "--census")
            self.assertEqual(after_code, 0, after)
            count = lambda s: int(s.split("statements ")[1].split(",")[0])
            self.assertEqual(count(after), count(before), "a sub-bullet must not split one obligation into two")


class PrincipleTraceability(unittest.TestCase):
    def test_current_document_passes(self):
        code, out = run(ROOT, TRACE, "--check")
        self.assertEqual(code, 0, out)
        self.assertIn("0 failure(s)", out)

    def test_row_without_backticks_is_still_checked(self):
        with Copy() as c:
            doc = "docs/Governance/Principle-Traceability.md"
            row = [l for l in c.read(doc).splitlines() if l.startswith("| `docs/")][0]
            c.edit(doc, row, "| docs/Nowhere/Invented.md:9999 | binding rule | REQ-NOT-REAL | nothing says this |")
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)

    def test_two_blocks_for_one_principle_fail(self):
        with Copy() as c:
            doc = "docs/Governance/Principle-Traceability.md"
            text = c.read(doc)
            start = text.index("## Principle 8:")
            end = text.index("## Principle 9:")
            c.write(doc, text[:end] + text[start:end] + text[end:])
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("more than one block", out)

    def test_quote_that_moved_fails(self):
        with Copy() as c:
            c.edit("docs/Models/Event.md", "An Event shall never be modified after creation.",
                   "An Event shall never be altered after creation.")
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("does not carry", out)

    def test_row_with_an_empty_quote_fails(self):
        with Copy() as c:
            doc = "docs/Governance/Principle-Traceability.md"
            row = [l for l in c.read(doc).splitlines() if l.startswith("| `docs/")][0]
            cells = row.split(" | ")
            # a quote cell of two quotation marks parses as a row and strips to nothing, which is
            # the fail-open: the row cites a file and a line and checks neither
            c.edit(doc, row, " | ".join(cells[:-1]) + ' | "" |')
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("carries no quote", out)

    def test_a_carrier_row_outside_its_table_is_not_silently_dropped(self):
        with Copy() as c:
            doc = "docs/Governance/Principle-Traceability.md"
            text = c.read(doc)
            i = text.index("## Principle 5:")
            stray = "| `docs/Models/Event.md:97` | binding rule | REQ-MODELS-EVENT-010 | An Event shall never be modified after creation. |\n\n"
            c.write(doc, text[:i] + stray + text[i:])
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("outside a table", out)

    def test_absent_row_naming_a_document_fails(self):
        with Copy() as c:
            doc = "docs/Governance/Principle-Traceability.md"
            row = [l for l in c.read(doc).splitlines() if "| restatement |" in l][0]
            c.edit(doc, row, row.replace("| restatement |", "| absent |"))
            code, out = run(c.dir, TRACE, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("absent", out)


class CompilationSurvey(unittest.TestCase):
    """`CAND-018` makes only the verbatim form a completeness claim, so only it is enforced."""

    def test_current_chapters_pass(self):
        code, out = run(ROOT, SURVEY, "--check")
        self.assertEqual(code, 0, out)
        self.assertIn("0 failure(s)", out)

    def test_verbatim_chapter_missing_a_statement_fails(self):
        with Copy() as c:
            # Chapter 2 declares "compiled from `Core/Principles.md`, verbatim", so a mandatory
            # Statement the source gains and the chapter does not carry is a defect of the chapter
            c.edit("docs/Core/Principles.md", "\n# Revision History",
                   "\n# Late Addition\n\nEvery Principle shall be restated in the reading path.\n\n---\n\n# Revision History")
            code, out = run(c.dir, SURVEY, "--check")
            self.assertEqual(code, 1, out)
            self.assertIn("declares verbatim but does not carry", out)

    def test_chapter_without_a_source_line_fails(self):
        with Copy() as c:
            chapter = "docs/Specification/07 Governance.md"
            text = c.read(chapter)
            c.write(chapter, text[:text.rindex("*Source:")])
            code, out = run(c.dir, SURVEY, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("carries no Source line", out)

    def test_census_reports_the_abridgement_it_permits(self):
        code, out = run(ROOT, SURVEY, "--census")
        self.assertEqual(code, 0, out)
        # a permitted abridgement still has to be visible as a number
        row = [l for l in out.splitlines() if l.startswith("04 Meta Model")][0]
        self.assertGreater(int(row.split()[-1]), 0, row)


class TestCatalogue(unittest.TestCase):
    """The binding of Statements to Tests is derived, so it has to break when a source sentence moves."""

    def test_current_catalogue_is_up_to_date(self):
        code, out = run(ROOT, CATALOGUE, "--check")
        self.assertEqual(code, 0, out)

    def test_changed_statement_breaks_the_catalogue(self):
        with Copy() as c:
            c.edit("docs/Models/Event.md", "An Event shall never be modified after creation.",
                   "An Event shall not be modified after it is created.")
            code, out = run(c.dir, CATALOGUE, "--check")
            self.assertNotEqual(code, 0, out)

    def test_a_behaviour_item_keeps_a_list_out_of_presence(self):
        with Copy() as c:
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            code, out = run(c.dir, CATALOGUE, "--census")
            self.assertEqual(code, 0, out)
            # Meta/Object.md's Design Principles list carries "remain technology independent"
            doc = run(c.dir, CATALOGUE, "--write")[0]
            self.assertEqual(doc, 0)
            text = (c.dir / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
            row = [l for l in text.splitlines() if l.startswith("| REQ-META-OBJECT-001 |")][0]
            self.assertEqual([c.strip() for c in row.strip().strip("|").split("|")][4], "Review", row)

    def test_an_organizational_obligation_is_not_mechanical(self):
        with Copy() as c:
            run(c.dir, CATALOGUE, "--write")
            text = (c.dir / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
            rows = [l for l in text.splitlines() if l.startswith("| REQ-META-IDENTITY-005 |")]
            self.assertTrue(rows, "the Statement this test names is gone from the register")
            self.assertEqual([c.strip() for c in rows[0].strip().strip("|").split("|")][4], "Review", rows[0])

    def test_a_renamed_claim_section_does_not_delete_a_test(self):
        with Copy() as c:
            c.edit("docs/Language/Conformance.md", "# Version Conformance", "# Versioning Conformance")
            code, out = run(c.dir, CATALOGUE, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Version Conformance", out)

    def test_hand_written_content_in_the_catalogue_is_caught(self):
        with Copy() as c:
            doc = "docs/Governance/Test-Catalogue.md"
            text = c.read(doc)
            c.write(doc, text.replace("| REQ-META-OBJECT-003 |", "| REQ-META-OBJECT-003-EDITED |", 1))
            code, out = run(c.dir, CATALOGUE, "--check")
            self.assertNotEqual(code, 0, out)

    def test_the_disagreement_with_section_3_is_printed(self):
        text = (ROOT / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
        self.assertIn("Where This Generator Disagrees With Section 3", text)
        block = text.split("Where This Generator Disagrees With Section 3")[1].split("# What Each Kind Does")[0]
        self.assertIn("differs", block)
        self.assertIn("agrees", block)

    def test_a_statement_without_an_alias_fails_closed(self):
        with Copy() as c:
            aliases = "docs/Governance/Requirement-Aliases.md"
            text = c.read(aliases)
            rows = [l for l in text.splitlines() if l.startswith("| REQ-")]
            c.write(aliases, text.replace(rows[0] + "\n", ""))
            code, out = run(c.dir, CATALOGUE, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("no alias", out)


class Validator(unittest.TestCase):
    """The suite has to notice a broken export, or its Pass rows mean nothing."""

    EX = "docs/Examples/Conformance"

    def run_on(self, root):
        return run(root, VALIDATE, "--model", "%s/model.json" % self.EX,
                   "--map", "%s/representation-map.md" % self.EX,
                   "--statement", "%s/conformance-statement.md" % self.EX)

    def test_the_example_passes_what_it_claims(self):
        # the exact numbers, not a substring a validator doing no work would also satisfy
        code, out = self.run_on(ROOT)
        self.assertEqual(code, 0, out)
        m = re.search(r"mandatory (\d+): Pass (\d+), Fail (\d+), pending (\d+)", out)
        self.assertIsNotNone(m, out)
        total, passed, failed, pending = (int(x) for x in m.groups())
        self.assertEqual(failed, 0, out)
        self.assertGreaterEqual(passed, 30, "the suite stopped deciding things: %s" % out)
        self.assertEqual(passed + failed + pending, total, out)
        # a model alone never establishes Core Conformance: Review Pass needs a reviewer
        self.assertIn("not established", out)

    def outcomes(self, root):
        """Every alias and its outcome, from a fresh run in `root`."""
        out = pathlib.Path(tempfile.mkdtemp()) / "r.md"
        code, printed = run(root, VALIDATE, "--model", "%s/model.json" % self.EX,
                            "--map", "%s/representation-map.md" % self.EX,
                            "--statement", "%s/conformance-statement.md" % self.EX, "--report", str(out))
        self.assertEqual(code, 0, printed)
        rows = {}
        for line in out.read_text(encoding="utf-8").splitlines():
            if line.startswith("| REQ-") or line.startswith("| DECL-"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                rows[cells[0]] = cells[4]
        shutil.rmtree(out.parent, ignore_errors=True)
        return rows

    def test_renaming_every_field_and_the_map_changes_nothing(self):
        """The suite prescribes no format, so an export that spells everything differently and
        says so in its Representation Map must score exactly the same. This is the property four
        hard-coded key reads quietly broke, each while every other test stayed green."""
        baseline = self.outcomes(ROOT)
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))

            def rename(value):
                if isinstance(value, dict):
                    return {("x_" + k if k != "export" else k): rename(v) for k, v in value.items()}
                if isinstance(value, list):
                    return [rename(v) for v in value]
                return value

            renamed = {("x_" + k if k != "export" else k): rename(v) for k, v in model.items()}
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            import importlib, validate as V
            importlib.reload(V)
            for coll in renamed.values():
                for rec in (coll if isinstance(coll, list) else []):
                    if isinstance(rec, dict) and "x_digest" in rec:
                        rec["x_digest"] = V.canonical_digest(rec, "x_digest")
            c.write("%s/model.json" % self.EX, json.dumps(renamed))

            lines = []
            for line in c.read("%s/representation-map.md" % self.EX).splitlines():
                cells = [x.strip() for x in line.strip().strip("|").split("|")] if line.startswith("| ") else []
                if len(cells) == 3 and cells[1] == "collection" and cells[2].startswith("`"):
                    paths = []
                    for path in cells[2].split(","):
                        path = path.strip().strip("`")
                        if "[]." in path:
                            parent, child = path.split("[].", 1)
                            paths.append("`x_%s[].x_%s`" % (parent, child))
                        else:
                            paths.append("`x_%s`" % path)
                    line = "| %s | collection | %s |" % (cells[0], ", ".join(paths))
                elif len(cells) == 3 and cells[1] == "field" and cells[2].startswith("`"):
                    line = "| %s | field | `x_%s` |" % (cells[0], cells[2].strip("`"))
                lines.append(line)
            c.write("%s/representation-map.md" % self.EX, "\n".join(lines) + "\n")

            after = self.outcomes(c.dir)
        differing = {a: (baseline.get(a), after.get(a)) for a in baseline if baseline[a] != after.get(a)}
        self.assertEqual(differing, {},
                         "renaming the export and its map changed %d verdict(s): %s"
                         % (len(differing), list(differing.items())[:4]))

    def test_a_repeated_value_fails_a_uniqueness_statement(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["events"][1]["id"] = model["events"][0]["id"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def integrity_rows(self, root):
        return {a: o for a, o in self.outcomes(root).items()
                if a in ("REQ-META-OWNERSHIP-022", "REQ-MODELS-EVENT-010", "REQ-MODELS-EVENT-004")}

    def test_integrity_demonstrations_verify_on_the_example(self):
        rows = self.integrity_rows(ROOT)
        self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Pass", rows)
        self.assertEqual(rows.get("REQ-MODELS-EVENT-010"), "Pass", rows)

    def test_an_altered_audit_record_fails_its_demonstration(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["audit_records"][0]["value"] = "Ownership assigned to somebody else"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.integrity_rows(c.dir).get("REQ-META-OWNERSHIP-022"), "Fail")

    def test_an_altered_event_fails_its_demonstration(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["events"][0]["occurred_at"] = "2026-08-09T10:12:00Z"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.integrity_rows(c.dir).get("REQ-MODELS-EVENT-010"), "Fail")

    def test_a_missing_demonstration_is_pending_not_passed(self):
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            c.write(path, "\n".join(l for l in c.read(path).splitlines() if not l.startswith("| Integrity.method")) + "\n")
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)

    def test_the_catalogue_binds_immutability_to_integrity(self):
        text = (ROOT / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
        row = [l for l in text.splitlines() if l.startswith("| REQ-META-OWNERSHIP-022 |")][0]
        self.assertEqual([x.strip() for x in row.strip().strip("|").split("|")][4], "Integrity", row)

    def test_a_zero_does_not_satisfy_presence(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for rel in model["relationships"]:
                rel["type"] = 0
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_list_of_absences_does_not_satisfy_presence(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            # Contract.participants is list-valued and a Presence Test does check it, unlike
            # Entity.attributes, whose Statement carries a behaviour item and goes to Review
            for contract in model["contracts"]:
                contract["parties"] = [None, ""]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_two_lifecycles_with_one_identifier_fail(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["lifecycles"][1]["id"] = model["lifecycles"][0]["id"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_dangling_references_are_found_whatever_the_identifier_looks_like(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["entities"]:
                e["owner"] = "does-not-exist"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            report = c.dir / (self.EX + "/report.md")
            run(c.dir, VALIDATE, "--model", "%s/model.json" % self.EX,
                "--map", "%s/representation-map.md" % self.EX,
                "--statement", "%s/conformance-statement.md" % self.EX, "--report", str(report))
            text = report.read_text(encoding="utf-8")
            self.assertIn("does-not-exist", text)

    def test_an_identity_reused_inside_one_collection_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][2]["id"] = model["entities"][0]["id"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_an_empty_mapped_collection_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["relationships"] = []
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_falsy_field_does_not_satisfy_presence(self):
        for empty in (False, "", "null", [], "  "):
            with Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                for rel in model["relationships"]:
                    rel["type"] = empty
                c.write("%s/model.json" % self.EX, json.dumps(model))
                code, out = self.run_on(c.dir)
                self.assertNotIn("Fail 0", out, "a field holding %r passed as present" % (empty,))

    def test_a_dangling_lifecycle_reference_is_not_silently_skipped(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["lifecycle"] = "LC-NOWHERE"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_events_no_lifecycle_resolves_for_are_not_counted_as_checked(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["events"]:
                e["subject"] = "UNKNOWN-1"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            report = c.dir / (self.EX + "/report.md")
            code2, out2 = run(c.dir, VALIDATE, "--model", "%s/model.json" % self.EX,
                              "--map", "%s/representation-map.md" % self.EX,
                              "--statement", "%s/conformance-statement.md" % self.EX,
                              "--report", str(report))
            row = [l for l in report.read_text(encoding="utf-8").splitlines()
                   if l.startswith("| REQ-LIFECYCLES-003 ")][0]
            self.assertIn("pending", row, row)

    def test_a_descriptive_disposition_is_not_applicable(self):
        code, out = run(ROOT, VALIDATE, "--model", "%s/model.json" % self.EX,
                        "--map", "%s/representation-map.md" % self.EX,
                        "--statement", "%s/conformance-statement.md" % self.EX,
                        "--report", "/tmp/ocom-disposition.md")
        self.assertEqual(code, 0, out)
        row = [l for l in open("/tmp/ocom-disposition.md") if l.startswith("| REQ-LIFECYCLES-004 ")][0]
        self.assertIn("Not Applicable", row, row)

    def test_a_missing_required_field_fails_its_test(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for r in model["relationships"]:
                del r["type"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertEqual(code, 0, out)
            self.assertNotIn("Fail 0", out)

    def test_a_state_change_the_lifecycle_forbids_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["events"].append({"id": "EVT-BAD", "type": "Invented", "occurred_at": "2026-09-09T00:00:00Z",
                                    "subject": "LIB-000198", "from_state": "Available", "to_state": "Withdrawn"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_reused_identity_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["policies"][0]["id"] = model["entities"][0]["id"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_lifecycle_with_no_transitions_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["lifecycles"][0]["transitions"] = []
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_state_outside_its_lifecycle_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["state"] = "Invented"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_an_initial_state_the_lifecycle_does_not_define_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["lifecycles"][0]["initial_state"] = "Nowhere"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_transition_out_of_a_terminal_state_is_reported(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            lc = model["lifecycles"][0]
            lc["transitions"].append({"from": lc["terminal_states"][0], "to": "Available", "trigger": "Invented"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            report = json.dumps(out)
            self.assertNotIn("Fail 0", out, report)

    def test_a_compound_statement_is_not_passed_on_one_of_its_parts(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            # REQ-MODELS-LIFECYCLE-002 requires a Lifecycle to belong to exactly one Entity and to
            # define an initial State and operational States; breaking only the first must fail it
            for lc in model["lifecycles"]:
                lc["entity"] = ""
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_an_unreachable_state_is_found(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            lc = model["lifecycles"][0]
            lc["states"].append({"name": "Orphan", "meaning": "reachable by nothing",
                                 "entity": lc["entity"], "lifecycle": lc["id"]})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_an_object_without_an_owner_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["owner"] = ""
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_an_entity_type_governed_by_two_domains_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["domains"].append({"id": "DOM-SECOND", "name": "Second", "purpose": "overlap",
                                     "owner": "OWN-DOM-LENDING", "entity_types": ["Item"]})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_workflow_outside_its_lifecycle_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["workflows"][0]["transitions"] = [{"entity": "LIB-000198", "from": "Available", "to": "Lost"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_compound_prohibition_is_pending_not_passed(self):
        # REQ-MODELS-LIFECYCLE-012 forbids four things and one of them, ambiguous State
        # progression, no export settles: the Statement must not be reported Pass on the other three
        code, out = run(ROOT, VALIDATE, "--model", "%s/model.json" % self.EX,
                        "--map", "%s/representation-map.md" % self.EX,
                        "--statement", "%s/conformance-statement.md" % self.EX, "--report", "/tmp/ocom-compound.md")
        self.assertEqual(code, 0, out)
        row = [l for l in open("/tmp/ocom-compound.md") if l.startswith("| REQ-MODELS-LIFECYCLE-012 ")][0]
        self.assertIn("pending", row)
        self.assertIn("parts", row)

    def test_a_map_that_declares_nothing_cannot_pass(self):
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            text = c.read(path)
            c.write(path, "\n".join(l for l in text.splitlines() if not l.startswith("| ") or "collection" not in l))
            code, out = self.run_on(c.dir)
            self.assertNotEqual(code, 0, out)
            self.assertIn("declares no type", out)

    def test_an_undeclared_specification_version_fails_its_declaration(self):
        with Copy() as c:
            path = "%s/conformance-statement.md" % self.EX
            text = c.read(path)
            c.write(path, text.replace("**Supported specification version:** 1.0", "**Supported specification version:**"))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)


class PublishedSourceParity(unittest.TestCase):
    """The site serves files nothing else in this repository can reproduce."""

    def test_current_sources_lint_clean(self):
        code, out = run(ROOT, PARITY, "--lint")
        self.assertEqual(code, 0, out)

    def test_url_glued_to_a_sentence_period_fails(self):
        with Copy() as c:
            c.edit("publication/llms.txt", "- Origin story and motivation: https://ocom.uno/why\n",
                   "- Origin story and motivation: https://ocom.uno/why.\n")
            code, out = run(c.dir, PARITY, "--lint")
            self.assertEqual(code, 1, out)
            self.assertIn("harvester", out)

    def test_an_index_naming_nothing_cannot_pass(self):
        with Copy() as c:
            text = c.read("publication/README.md")
            c.write("publication/README.md", "\n".join(l for l in text.splitlines() if not l.startswith("| `http")))
            code, out = run(c.dir, PARITY, "--lint")
            self.assertNotEqual(code, 0, out)
            self.assertIn("lists no published file", out)

    def test_published_copy_that_drifts_is_reported(self):
        with Copy() as c:
            served = (c.dir / "publication" / "llms.txt").read_text(encoding="utf-8")
            with fake_site.Fixture({"/llms.txt": ("text/plain; charset=utf-8", served)}) as site:
                code, out = run(c.dir, PARITY, "--check", "--base", site.base)
                self.assertEqual(code, 0, out)
            drifted = served.replace("- Origin story and motivation:", "- Origin story:", 1)
            with fake_site.Fixture({"/llms.txt": ("text/plain; charset=utf-8", drifted)}) as site:
                code, out = run(c.dir, PARITY, "--check", "--base", site.base)
                self.assertEqual(code, 1, out)
                self.assertIn("differs from", out)

    def test_a_published_path_that_disappears_fails(self):
        with Copy() as c:
            with fake_site.Fixture({}) as site:
                code, out = run(c.dir, PARITY, "--check", "--base", site.base)
                self.assertEqual(code, 1, out)
                self.assertIn("answered 404", out)


class PublicationHealth(unittest.TestCase):
    """Every case runs against the in-memory fixture; none of them touches the real site."""

    def healthy(self, site):
        """Publish the records the tool itself computes, so the fixture starts consistent."""
        out = tempfile.mkdtemp(prefix="ocom-health-")
        code, text = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--write", out)
        self.assertEqual(code, 0, text)
        health = json.loads((pathlib.Path(out) / "observatory" / "health.json").read_text(encoding="utf-8"))
        pub = json.loads((pathlib.Path(out) / "observatory" / "publication-health.json").read_text(encoding="utf-8"))
        site.publish(health, pub)
        shutil.rmtree(out, ignore_errors=True)
        return health, pub

    def test_healthy_fixture_passes(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertEqual(code, 0, out)
            self.assertIn("differ in 0 place(s)", out)

    def test_missing_identifier_registry_is_a_failure_not_an_empty_set(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            del site.files["/resolve.json"]
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("resolve.json", out)

    def test_missing_term_index_is_a_failure(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            del site.files["/api/v1/terms.json"]
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("terms.json", out)

    def test_citation_mismatch_inside_jsonld_graph_fails(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            record = json.loads(site.files["/vocabulary/object.jsonld"][1])
            record["@graph"][0]["citation"] = "A different citation."
            site.files["/vocabulary/object.jsonld"] = ("application/json", json.dumps(record))
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Citation parity", out)

    def test_a_page_that_disappears_fails_its_row(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            del site.files["/vocabulary/object.md"]
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Core Vocabulary Markdown", out)

    def test_a_coined_name_outside_type_is_still_checked(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            record = json.loads(site.files["/graph.jsonld"][1])
            # a coined name in a value position rather than in @type: the row read @type only
            record["@graph"][-1]["graph:undefinedProperty"] = "x"
            site.files["/graph.jsonld"] = ("application/json", json.dumps(record))
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Coined names resolve", out)

    def test_missing_sitemap_is_a_failure(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            del site.files["/sitemap.xml"]
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("sitemap.xml", out)

    def test_a_coined_name_that_expands_to_nothing_fails(self):
        with fake_site.Fixture() as site:
            self.healthy(site)
            record = json.loads(site.files["/graph.jsonld"][1])
            # the defect AO-078 records: a type in the publication's own namespace that the
            # document behind that namespace does not define
            record["@graph"][-1]["@type"] = "graph:Undefined"
            site.files["/graph.jsonld"] = ("application/json", json.dumps(record))
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Coined names resolve", out)

    def test_a_published_figure_that_drifts_is_reported(self):
        with fake_site.Fixture() as site:
            health, pub = self.healthy(site)
            health["mutualPairs"] = 99
            site.publish(health, pub)
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("mutualPairs", out)

    def test_a_published_row_count_that_drifts_is_reported(self):
        with fake_site.Fixture() as site:
            health, pub = self.healthy(site)
            pub["checks"][0]["checked"] = 999
            site.publish(health, pub)
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("checked=", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)

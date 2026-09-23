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
import hashlib
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
REGISTER_TOOL = REGISTER
COUNTS = "tools/governance/register_counts.py"
SURVEY = "tools/conformance/compilation_survey.py"
CATALOGUE = "tools/conformance/test_catalogue.py"
VALIDATE = "tools/conformance/validate.py"
PARITY = "tools/site/published_source_parity.py"
TRACE = "tools/governance/principle_traceability.py"
HEALTH = "tools/site/publication_health.py"
HUNT = "tools/site/site_error_hunt.py"
SCHEMA = "tools/conformance/reference_schema.py"


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
        # every repository-root file a tool reads: without README.md, register_counts.py failed on
        # its absence and every negative test around it passed without exercising anything
        for name in ("README.md", "CHANGELOG.md", "CI-DESIGN.md"):
            if (ROOT / name).exists():
                shutil.copy2(ROOT / name, self.dir / name)
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
        assert old != new, "fixture edit changes nothing in %s" % rel
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


    def commit_aliases(self, c):
        """A copy with the Alias File committed, so the append-only rule has a history to read."""
        for args in (("init", "-q"), ("add", "docs/Governance/Requirement-Aliases.md"),
                     ("-c", "user.email=t@example.com", "-c", "user.name=T", "commit", "-q", "-m", "base")):
            done = subprocess.run(["git"] + list(args), cwd=str(c.dir), capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    ALIASES = "docs/Governance/Requirement-Aliases.md"

    def test_an_alias_row_edited_in_place_is_refused(self):
        """Section 2 makes the Alias File append-only: "rows are appended, never edited or removed".
        Round 3 of the all-packages test rewrote a source sentence and edited the row's Identity cell
        to the new hash: the register regenerated cleanly, every alias was covered, and nothing
        noticed that the sentence under the row had changed. The rule is about history."""
        with Copy() as c:
            self.commit_aliases(c)
            code, out = run(c.dir, REGISTER, "--check-aliases", "--against", "HEAD")
            self.assertEqual(code, 0, out)
            self.assertIn("rows edited since HEAD 0", out)
            row = [l for l in c.read(self.ALIASES).splitlines() if l.startswith("| REQ-MODELS-DOMAIN-004 |")][0]
            c.edit(self.ALIASES, row, row.replace(row.split("|")[2].strip(), "`%s`" % ("a" * 64)))
            code, out = run(c.dir, REGISTER, "--check-aliases", "--against", "HEAD")
            self.assertNotEqual(code, 0, out)
            self.assertIn("REQ-MODELS-DOMAIN-004 was edited in place", out)

    def test_a_base_that_is_the_commit_under_test_is_no_base(self):
        """Round 4: `base_revisions` ended in HEAD, so on a push to the default branch every
        candidate resolved to the commit being checked and the file was compared against itself.
        The check reported zero edits, and the "compared against nothing" branch was unreachable."""
        with Copy() as c:
            self.commit_aliases(c)
            row = [l for l in c.read(self.ALIASES).splitlines() if l.startswith("| REQ-MODELS-DOMAIN-004 |")][0]
            c.edit(self.ALIASES, row, row.replace(row.split("|")[2].strip(), "`%s`" % ("a" * 64)))
            for args in (("-c", "user.email=t@example.com", "-c", "user.name=T", "commit", "-qam", "edit in place"),):
                subprocess.run(["git"] + list(args), cwd=str(c.dir), capture_output=True, text=True)
            # the edit is now the commit under test, which is what CI checks out: comparing the
            # file against the commit that contains it finds nothing, and the run says so
            code, out = run(c.dir, REGISTER_TOOL, "--check-aliases", "--against", "HEAD")
            self.assertIn("this can only show edits that are not committed", out)
            self.assertIn("rows edited since HEAD 0", out)
            code, out = run(c.dir, REGISTER_TOOL, "--check-aliases", "--against", "HEAD~1")
            self.assertNotEqual(code, 0, out)
            self.assertIn("was edited in place", out)

    def test_an_alias_row_that_disappears_is_refused(self):
        with Copy() as c:
            self.commit_aliases(c)
            text = c.read(self.ALIASES)
            row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-DOMAIN-004 |")][0]
            c.write(self.ALIASES, text.replace(row + "\n", ""))
            code, out = run(c.dir, REGISTER, "--check-aliases", "--against", "HEAD")
            self.assertNotEqual(code, 0, out)
            self.assertIn("is no longer in the file", out)

    def test_a_disposition_recorded_later_is_not_an_edit(self):
        """Only the Disposition cell may change after a row is committed; that is how a Statement is
        dispositioned and how a superseded row is marked."""
        with Copy() as c:
            self.commit_aliases(c)
            row = [l for l in c.read(self.ALIASES).splitlines() if l.startswith("| REQ-MODELS-DOMAIN-004 |")][0]
            cells = row.split("|")
            cells[6] = " Review "
            c.edit(self.ALIASES, row, "|".join(cells))
            code, out = run(c.dir, REGISTER, "--check-aliases", "--against", "HEAD")
            self.assertEqual(code, 0, out)

    def test_an_append_only_check_with_no_history_reports_that_it_checked_nothing(self):
        """A checker that cannot check must not report ok: outside a checkout there is no base
        revision, and the run says so and fails rather than passing over the rule."""
        with Copy() as c:
            code, out = run(c.dir, REGISTER, "--check-aliases", "--against", "HEAD")
            self.assertNotEqual(code, 0, out)
            self.assertIn("compared against nothing", out)

class RegisterCounts(unittest.TestCase):
    """The tool that compares the documents stating the register counts against the registers.

    It was an inline CI script with no test of its own, and round 4 of the all-packages test found
    it passing on a repository whose README and llms.txt both state the old counts in a wording it
    could not read."""

    def test_the_repository_agrees_with_its_registers(self):
        code, out = run(ROOT, COUNTS, "--check")
        self.assertEqual(code, 0, out)
        self.assertIn("0 disagreement(s)", out)

    def test_an_unmutated_copy_passes(self):
        """The control every negative test below depends on: the fixture must carry what the tool
        reads. It did not carry README.md, so all four tests passed on its absence."""
        with Copy() as c:
            code, out = run(c.dir, COUNTS, "--check")
            self.assertEqual(code, 0, out)
            self.assertIn("0 disagreement(s)", out)

    def stating_line(self, c, rel="publication/llms.txt"):
        return [l for l in c.read(rel).splitlines() if "AO-001 to AO-" in l][0]

    def test_a_stale_count_is_reported(self):
        with Copy() as c:
            line = self.stating_line(c)
            stale = re.sub(r"\b(\d+) recorded", lambda m: "%d recorded" % (int(m.group(1)) - 10), line, count=1)
            c.edit("publication/llms.txt", line, stale)
            code, out = run(c.dir, COUNTS, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("publication/llms.txt", out)
            self.assertIn("states no count matching", out)

    def test_a_stale_last_identifier_is_reported(self):
        with Copy() as c:
            line = self.stating_line(c)
            c.edit("publication/llms.txt", line, re.sub(r"to AO-\d+", "to AO-001", line, count=1))
            code, out = run(c.dir, COUNTS, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("names AO-001 as the last Architecture Observation", out)

    def test_a_file_stating_its_counts_in_another_wording_is_not_silently_compliant(self):
        """The defect itself: a file the check cannot read was scanned, matched nothing and passed."""
        with Copy() as c:
            line = self.stating_line(c)
            c.edit("publication/llms.txt", line, line.replace("AO-001 to AO-", "AO-001 through AO-"))
            code, out = run(c.dir, COUNTS, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("publication/llms.txt states no Architecture Observation range", out)

    def test_a_file_that_drops_one_of_the_two_ranges_is_reported(self):
        """Round 5: the readability counter was incremented by a match of either prefix, so a file
        that states the observation range and no candidate range had its candidate count compared
        against nothing while the tool reported zero disagreements."""
        with Copy() as c:
            text = c.read("docs/Governance/Evidence-Register.md")
            line = [l for l in text.splitlines() if l.startswith("| ADR Candidates |")][0]
            c.edit("docs/Governance/Evidence-Register.md", line, line.replace("CAND-001 to CAND-034", "the candidates"))
            code, out = run(c.dir, COUNTS, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("states no ADR Candidate range", out)


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
        # REQ-META-OWNERSHIP-008 opens with Organizations and stays at Review; REQ-META-IDENTITY-005 opened
        # with it too until CAND-026 bound the scope rule to a Declaration read from the map
        with Copy() as c:
            run(c.dir, CATALOGUE, "--write")
            text = (c.dir / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
            rows = [l for l in text.splitlines() if l.startswith("| REQ-META-OWNERSHIP-008 |")]
            self.assertTrue(rows, "the Statement this test names is gone from the register")
            self.assertEqual([c.strip() for c in rows[0].strip().strip("|").split("|")][4], "Review", rows[0])

    def test_the_census_columns_sum_to_the_catalogue(self):
        """The Census counted the six claim clauses as register Statements, so its columns summed to
        214 and 188 against the 208 and 182 the same document states."""
        text = (ROOT / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8")
        census = text[text.index("# Census"):text.index("Of the ")]
        rows = re.findall(r"(?m)^\| (\w+) \| (\d+) \| (\d+) \|$", census)
        self.assertEqual(len(rows), 6, rows)
        self.assertEqual(sum(int(r[1]) for r in rows), 208)
        self.assertEqual(sum(int(r[2]) for r in rows), 182)

    def test_a_census_that_does_not_add_up_stops_the_generator(self):
        with Copy() as c:
            path = "tools/conformance/test_catalogue.py"
            c.write(path, c.read(path).replace('out.append("| Declaration | %d | %d |" % (counts.get("Declaration", 0),',
                                               'out.append("| Declaration | %d | %d |" % (99 + counts.get("Declaration", 0),'))
            code, out = run(c.dir, CATALOGUE, "--write")
            self.assertNotEqual(code, 0, out)
            self.assertIn("Census that does not add up", out)

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


class ReferenceSchema(unittest.TestCase):
    """The schema is derived, and a check that could not tell a drifted schema or a broken file
    from a good one would be decoration."""

    EX = "docs/Examples/Conformance"

    def test_the_committed_schema_matches_a_regeneration_and_the_model_satisfies_it(self):
        code, out = run(ROOT, SCHEMA, "--check")
        self.assertEqual(code, 0, out)
        self.assertIn("schema up to date", out)

    def test_a_drifted_schema_fails_the_check(self):
        with Copy() as c:
            path = "%s/schema.json" % self.EX
            c.write(path, c.read(path).replace('"additionalProperties": true', '"additionalProperties": false', 1))
            code, out = run(c.dir, SCHEMA, "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("differs from a regeneration", out)

    def test_a_file_missing_a_required_key_fails_validation(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            del model["entities"][0]["id"]
            broken = c.dir / "broken.json"
            broken.write_text(json.dumps(model), encoding="utf-8")
            code, out = run(c.dir, SCHEMA, "--validate", str(broken))
            self.assertNotEqual(code, 0, out)
            self.assertIn("required key id is missing", out)

    def test_a_wrongly_typed_value_and_a_bad_digest_fail_validation(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["attributes"] = "not a list"
            model["audit_records"][0]["id"] = "not-a-digest"
            broken = c.dir / "broken.json"
            broken.write_text(json.dumps(model), encoding="utf-8")
            code, out = run(c.dir, SCHEMA, "--validate", str(broken))
            self.assertNotEqual(code, 0, out)
            self.assertIn("expected array", out)
            self.assertIn("does not match", out)

    def test_a_minimal_export_satisfies_the_schema(self):
        """Collections are optional and one example record proves nothing about optionality: an
        export carrying only its export block and its entities validates. The enterprise
        evaluation of 22 September 2026 found the first derivation demanding all eighteen keys."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            minimal = {"export": {"produced_by": "probe"}, "entities": model["entities"][:1]}
            path = c.dir / "minimal.json"
            path.write_text(json.dumps(minimal), encoding="utf-8")
            code, out = run(c.dir, SCHEMA, "--validate", str(path))
            self.assertEqual(code, 0, out)

    def test_a_model_without_records_cannot_produce_a_schema(self):
        with Copy() as c:
            c.write("%s/model.json" % self.EX, json.dumps({"export": {"produced_by": "nobody"}}))
            code, out = run(c.dir, SCHEMA, "--write")
            self.assertNotEqual(code, 0, out)
            self.assertIn("no collection of records", out)


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
        m = re.search(r"mandatory (\d+): Pass (\d+), Fail (\d+), pending (\d+), reviewed (\d+) pass and (\d+) fail", out)
        self.assertIsNotNone(m, out)
        total, passed, failed, pending, rpass, rfail = (int(x) for x in m.groups())
        self.assertEqual(failed, 0, out)
        self.assertGreaterEqual(passed, 30, "the suite stopped deciding things: %s" % out)
        self.assertEqual(passed + failed + pending + rpass + rfail, total, out)
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
            # content addresses are computed over the keys, so an implementation that spells its
            # export differently computes its own addresses; references follow the new addresses
            old_new = {}
            for coll in ("x_audit_records", "x_events"):
                for rec in renamed.get(coll, []):
                    before = rec.get("x_id")
                    rec["x_id"] = V.canonical_digest(rec, "x_id")
                    old_new[before] = rec["x_id"]
            for ev in renamed.get("x_evidence_records", []):
                ev["x_related_memory_record"] = old_new.get(ev.get("x_related_memory_record"), ev.get("x_related_memory_record"))
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

    def test_a_re_addressed_record_is_a_different_record(self):
        """Alter a record and recompute its content address: it verifies, because it is a new
        record, and every reference to the old identity dangles, which is how the holder of the
        old identity learns that the record they held is gone."""
        with Copy() as c:
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            import importlib, validate as V
            importlib.reload(V)
            model = json.loads(c.read("%s/model.json" % self.EX))
            rec = model["audit_records"][0]
            old_id = rec["id"]
            rec["value"] = "Ownership assigned to somebody else"
            rec["id"] = V.canonical_digest(rec, "id")
            c.write("%s/model.json" % self.EX, json.dumps(model))
            report = c.dir / (self.EX + "/report.md")
            run(c.dir, VALIDATE, "--model", "%s/model.json" % self.EX, "--map", "%s/representation-map.md" % self.EX,
                "--statement", "%s/conformance-statement.md" % self.EX, "--report", str(report))
            text = report.read_text(encoding="utf-8")
            self.assertIn("| REQ-META-OWNERSHIP-022 |", text)
            self.assertIn("Pass", [l for l in text.splitlines() if l.startswith("| REQ-META-OWNERSHIP-022 |")][0])
            self.assertIn(old_id, text.split("## Reference Integrity")[1].split("## Results")[0])

    def test_a_self_contained_digest_is_pending_not_passed(self):
        with Copy() as c:
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            import importlib, validate as V
            importlib.reload(V)
            model = json.loads(c.read("%s/model.json" % self.EX))
            for rec in model["audit_records"]:
                rec["id"] = rec["label"]
                rec["digest"] = V.canonical_digest(rec, "digest")
            for ev in model["evidence_records"]:
                ev["related_memory_record"] = [r["id"] for r in model["audit_records"] if r["label"] == ev["related_memory_record"] or True][0]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            text = c.read(path).replace("| Integrity.method | method | `content-addressed-identity` |", "| Integrity.method | method | `sha256-canonical-json` |")
            text = text.replace("| Audit record.integrity | field | `id` |", "| Audit record.integrity | field | `digest` |")
            c.write(path, text)
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)

    def test_a_missing_demonstration_is_pending_not_passed(self):
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            c.write(path, "\n".join(l for l in c.read(path).splitlines() if not l.startswith("| Integrity.method")) + "\n")
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)

    def test_an_erased_record_is_excluded_from_the_demonstration(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            erased = model["audit_records"][0]["id"]
            model["audit_records"][0] = self.erase(model["audit_records"][0])
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer", "created_at": "2026-09-21T00:00:00Z"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            rows = self.integrity_rows(c.dir)
            # an exclusion rests on records and map rows the claimant writes, so the Test reports
            # what it verified and leaves the exclusion to a reviewer rather than passing on it
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)
            self.assertIn("ERA-0001 names %s: well formed" % erased, self.report_text(c.dir))
            self.assertIn("2 of 3 audit record record(s) verified; 1 excluded", self.report_text(c.dir))

    def test_an_erasure_does_not_cover_a_record_that_still_carries_its_content(self):
        """Round 3 of the all-packages test: the exclusion was granted on the identity alone, so a
        record that kept every field and had its content altered was excluded from the one Test that
        would have caught the alteration. `Memory/Retention.md` grants it to a record whose content
        is irrecoverable and whose identity, creation time, creator and demonstration are preserved."""
        for label, mutate in (("tampered", lambda rec: dict(rec, value="Ownership assigned to OWN-ATTACKER")),
                              ("blanked one field", lambda rec: dict(rec, value="[erased]")),
                              ("creation time gone", lambda rec: {"id": rec["id"], "creator": rec["creator"]})):
            with self.subTest(label), Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                erased = model["audit_records"][0]["id"]
                model["audit_records"][0] = mutate(model["audit_records"][0])
                model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND",
                                      "actor": "records-officer"}]
                c.write("%s/model.json" % self.EX, json.dumps(model))
                self.map_erasures(c)
                rows = self.integrity_rows(c.dir)
                self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Fail", (label, rows))
                printed = self.run_on(c.dir)[1]
                self.assertIn("the exclusion an erasure record grants does not cover it", printed)

    def test_an_erasure_grants_nothing_where_the_map_cannot_show_the_preservation(self):
        """The map binds no creation time and no creator for the type, so nothing can say the
        Deleted state preserved them; the exclusion is refused rather than granted on the identity."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            erased = model["audit_records"][0]["id"]
            model["audit_records"][0] = self.erase(model["audit_records"][0])
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path)
                    .replace("| Registry | collection | `registries` |", "| Registry | collection | `registries` |\n| Erasure | collection | `erasures` |")
                    .replace("| Integrity.method |", "| Erasure.identifier | field | `id` |\n| Erasure.erased record | field | `record` |\n| Erasure.policy | field | `policy` |\n| Erasure.actor | field | `actor` |\n| Integrity.method |"))
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Fail", rows)
            self.assertIn("binds no field to audit record.creation time", self.run_on(c.dir)[1])

    def test_an_erasure_naming_an_identity_in_two_namespaces_grants_nothing(self):
        """Round 3: the exclusion was keyed by the namespace of the erasures collection, not of the
        record named, so an erasure stored in one scope excised a record that merely shared its key
        in another. Content addressing makes exactly that pair."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            target = model["audit_records"][0]
            erased = target["id"]
            model["audit_records"][0] = self.erase(target)
            model["capabilities"].append({"id": erased, "name": "a twin in another system", "purpose": "probe"})
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Integrity.method |",
                    "| Capability.identity scope | declaration | `External System` |\n"
                    "| Capability.identity system | declaration | `ServiceNow` |\n| Integrity.method |"))
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Fail", rows)
            self.assertIn("an identity the export declares in 2 namespaces", self.report_text(c.dir)
                          + self.run_on(c.dir)[1])


    # --- round 5 of the all-packages test -------------------------------------------------

    def test_a_record_stored_as_an_object_value_is_not_invisible(self):
        """Round 5: record_collections listed a collection of records and an object of records, and
        walked into a single record stored as an object value as though it were a container, so the
        identity it carries was compared against nothing."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["archive"] = {"id": model["entities"][0]["id"], "name": "shadow copy"}
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Fail", rows.get("REQ-META-IDENTITY-005"))
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "pending", rows.get("REQ-META-IDENTITY-008"))

    def test_a_collection_listed_under_a_type_that_binds_no_identity_is_still_compared(self):
        """Round 5: unlisted_collections skipped a listed collection and object_paths dropped one
        whose type binds no identity, so a collection listed under such a type was in neither."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["shadows"] = [{"id": model["entities"][0]["id"], "name": "shadow"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Registry | collection | `registries` |",
                                               "| Registry | collection | `registries` |\n"
                                               "| Capability | collection | `capabilities`, `shadows` |"))
            rows = self.outcomes(c.dir)
            self.assertIn(rows.get("REQ-META-IDENTITY-008"), ("Fail", "pending"), rows.get("REQ-META-IDENTITY-008"))

    def test_a_nested_collection_the_map_states_is_held_to_the_same_shape(self):
        """Round 5: the "not a list of records" refusal was applied to top-level paths only, so
        every nested collection the map states was exempt and its non-record members were filtered
        away instead of stopping the run."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["lifecycles"][0]["states"].append("not a record")
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotEqual(code, 0, out)
            self.assertIn("not a list of records", out)

    def test_an_identity_that_is_a_list_fails_rather_than_crashing(self):
        """Round 5: the uniqueness leg keyed a dict on the identity value, so an Object carrying two
        identities killed the run before any report was written. It is the input "Every Object shall
        possess a unique identity" exists to catch."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["id"] = [model["entities"][0]["id"], "P-SECOND"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertEqual(code, 0, out)      # a report is written, which is the point
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-OBJECT-003"), "Fail")

    def test_workflow_steps_that_are_not_records_are_reported_not_fatal(self):
        """Round 5: workflow_violations called .get() on every member of the steps field, so a
        Workflow recording its steps as references to Transition records killed the run."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for wf in model["workflows"]:
                wf["transitions"] = ["TR-0001", "TR-0002"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-WORKFLOW-011"), "pending", rows.get("REQ-MODELS-WORKFLOW-011"))
            self.assertIn("are not records", self.report_text(c.dir))

    def test_an_erasure_does_not_cover_content_hidden_inside_a_preserved_field(self):
        """Round 5: the content check read the record's top-level keys, so the whole tampered
        content survived inside the value of a preserved field and the exclusion was granted; and
        the creation time was prefix-matched, so a timestamp in front of the content passed."""
        cases = {
            "nested in the creator": lambda rec, i: {"id": i, "created_at": "2024-03-11T09:00:00Z",
                                                     "creator": {"name": "Branch Manager", "was": rec}},
            "a timestamp in front of the content": lambda rec, i: {
                "id": i, "creator": "Branch Manager",
                "created_at": "2024-03-11T09:00:00Z " + json.dumps(rec)},
        }
        for label, mutate in cases.items():
            with self.subTest(label), Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                original = dict(model["audit_records"][0])
                erased = original["id"]
                model["audit_records"][0] = mutate(original, erased)
                model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND",
                                      "actor": "records-officer"}]
                c.write("%s/model.json" % self.EX, json.dumps(model))
                self.map_erasures(c)
                self.assertEqual(self.integrity_rows(c.dir).get("REQ-META-OWNERSHIP-022"), "Fail", label)

    def test_an_erasure_grants_nothing_where_the_map_calls_the_content_a_creator(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            original = dict(model["audit_records"][0])
            erased = original["id"]
            model["audit_records"][0] = {"id": erased, "created_at": "2024-03-11T09:00:00Z",
                                         "value": "Ownership assigned to OWN-ATTACKER"}
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Audit record.creator | field | `creator` |",
                                               "| Audit record.creator | field | `value` |"))
            # the map can call the surviving content a creator, and no rule of grammar tells the
            # two apart; what the suite can refuse is to call the result a verified Pass
            rows = self.integrity_rows(c.dir)
            self.assertNotEqual(rows.get("REQ-META-OWNERSHIP-022"), "Pass", rows)

    def test_an_erasure_field_holding_a_list_is_reported_not_fatal(self):
        """Round 5: a list-valued Policy or erased record was compared with `in` against a set and
        raised TypeError, so one oddly shaped field produced no outcome for any of the 185
        mandatory Statements."""
        for field in ("policy", "record"):
            with self.subTest(field), Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                erased = model["audit_records"][0]["id"]
                model["audit_records"][0] = {"id": erased, "created_at": "2024-03-11T09:00:00Z",
                                             "creator": "Branch Manager"}
                erasure = {"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer"}
                erasure[field] = ["one", "two"]
                model["erasures"] = [erasure]
                c.write("%s/model.json" % self.EX, json.dumps(model))
                self.map_erasures(c)
                code, out = self.run_on(c.dir)
                self.assertEqual(code, 0, out)
                self.assertIn("several", self.report_text(c.dir))

    def test_two_spellings_of_one_declared_system_are_one_namespace(self):
        """Round 5: the declared scope was folded and the declared system was not, so SAP and sap
        were two namespaces and a reused identity passed both identity Tests."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["capabilities"].append({"id": model["entities"][0]["id"], "name": "twin", "purpose": "probe"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Integrity.method |",
                    "| Entity.identity scope | declaration | `External System` |\n"
                    "| Entity.identity system | declaration | `SAP` |\n"
                    "| Capability.identity scope | declaration | `External System` |\n"
                    "| Capability.identity system | declaration | `sap` |\n| Integrity.method |"))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Fail", rows.get("REQ-META-IDENTITY-008"))

    def test_a_second_scope_does_not_mask_a_lifecycle_violation(self):
        """Round 5: by_entity was keyed by the bare identity, so the ServiceNow twin of an SAP
        Entity overwrote it and the SAP record's State was checked against the ServiceNow record's
        Lifecycle. Two mandatory Transition Tests went from Fail to Pass through the door CAND-026
        opens for two systems' keys."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            other = [lc for lc in model["lifecycles"] if lc["id"] != model["entities"][0]["lifecycle"]][0]
            # the SAP record is in a State only the other Lifecycle defines: keyed by the bare
            # identity, the twin's Lifecycle answered for it and the violation passed
            model["entities"][0]["state"] = other["states"][0]["name"]
            twin = dict(model["entities"][0], lifecycle=other["id"])
            model["entities_snow"] = [twin]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path)
                    .replace("| Entity | collection | `entities` |", "| Entity | collection | `entities`, `entities_snow` |")
                    .replace("| Integrity.method |",
                             "| Entity.identity scope | declaration | `External System` |\n"
                             "| entities.identity system | declaration | `SAP` |\n"
                             "| entities_snow.identity system | declaration | `ServiceNow` |\n| Integrity.method |"))
            rows = self.outcomes(c.dir)
            self.assertNotEqual(rows.get("REQ-MODELS-ENTITY-008"), "Pass", rows.get("REQ-MODELS-ENTITY-008"))

    def test_a_map_row_of_the_wrong_kind_is_refused(self):
        """Round 5: `Adoption/Reference Serialization.md` called the integrity method a declaration,
        and a map written to it had every Integrity Test report that the map declares no method."""
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            row = [l for l in c.read(path).splitlines() if l.startswith("| Integrity.method |")][0]
            c.edit(path, row, row.replace("| method |", "| declaration |"))
            code, out = self.run_on(c.dir)
            self.assertNotEqual(code, 0, out)
            self.assertIn("it is kind `method`", out)

    def test_a_reviewer_record_declaring_a_binding_the_tool_cannot_verify_is_refused(self):
        """Round 5: recorded_against read three known keys, so a record naming more had the extra
        bindings dropped while the report said its inputs were verified."""
        C = ROOT / self.EX
        digests = {k: hashlib.sha256((C / f).read_bytes()).hexdigest()[:16]
                   for k, f in (("model", "model.json"), ("map", "representation-map.md"),
                                ("statement", "conformance-statement.md"))}
        digests["register"] = hashlib.sha256((ROOT / "docs/Governance/Requirement-Register.md").read_bytes()).hexdigest()[:16]
        line = "**Recorded against:** " + ", ".join("%s `%s`" % (k, v) for k, v in digests.items())
        with Copy() as c:
            path = c.dir / "reviews.md"
            path.write_text("# R\n\n%s, ledger `%s`\n\n%s%s" % (line, "f" * 16, self.HEADER, self.JUDGMENT),
                            encoding="utf-8")
            code, printed, text = self.run_with_reviews(ROOT, path)
            self.assertNotEqual(code, 0, printed)
            self.assertIn("names fewer binds its judgments", printed)

    def test_a_judgment_is_bound_to_the_register_it_was_recorded_against(self):
        """Round 5: the Statement text a reviewer judged comes from the register, whose digest the
        report printed and compared to nothing, so rewriting a Statement carried the judgment over."""
        with Copy() as c:
            register = "docs/Governance/Requirement-Register.md"
            c.write(register, c.read(register) + "\n<!-- a changed register -->\n")
            code, printed, text = self.run_with_reviews(c.dir, c.dir / self.REVIEWS)
            self.assertNotEqual(code, 0, printed)
            self.assertIn("recorded against register", printed)

    # --- round 4 of the all-packages test ------------------------------------------------

    def test_the_state_leg_reads_the_entity_identity_through_the_map(self):
        """Round 4: the "exactly one State" leg resolved its Entity with `r.value(...) or e.get("id")`,
        the last literal-key read in the engines. With the map binding the identity elsewhere, a
        stale `id` left in the record checked each Entity's State against another Entity's Lifecycle
        and two mandatory Tests passed over three violations."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["entities"]:
                e["oid"] = e["id"]
                e["id"] = model["entities"][0]["id"]      # one stale key on every record
                e["state"] = "Available"                  # a State only the Item Lifecycle defines
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path)
                    .replace("| Entity.identity | field | `id` |\n", "")
                    .replace("| Entity.identifier | field | `id` |", "| Entity.identifier | field | `oid` |"))
            rows = self.outcomes(c.dir)
            for alias in ("REQ-MODELS-ENTITY-008", "REQ-MODELS-LIFECYCLE-009"):
                self.assertNotEqual(rows.get(alias), "Pass", (alias, rows.get(alias)))

    def test_several_initial_states_fail_the_statement_rather_than_crash_the_run(self):
        """Round 4: the unreachable-State leg seeded a set with the initial State, so a Lifecycle
        declaring several died with an unhashable list and no report was written at all. The one
        input the Statement exists to catch was the one the tool could not survive."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["lifecycles"][0]["initial_state"] = [model["lifecycles"][0]["initial_state"],
                                                       model["lifecycles"][0]["states"][1]["name"]]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-LIFECYCLE-012"), "Fail", rows.get("REQ-MODELS-LIFECYCLE-012"))

    def test_a_domain_violation_is_not_discarded_when_a_later_row_is_missing(self):
        """Round 4: the leg found the violation, then returned pending because the second half of
        the Statement could not be read, and the Fail it already had was thrown away."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["domain"] = [model["domains"][0]["id"], "DOM-SECOND"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.drop_rows(c, "Domain.entity types")
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-DOMAIN-010"), "Fail")

    def test_half_an_accountable_type_declaration_decides_nothing(self):
        """Round 4: `reads_type` was the AND of the two rows, so deleting the `Ownership.type` field
        row switched CAND-025's counting leg off and the Pass reason said the map declared neither."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append({"id": "OWN-P-10432-B", "owner": "Data Governance Office",
                                       "owned_object": "P-10432", "responsibility_scope": "Second.",
                                       "effective_date": "2024-01-01"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.declare_accountable_type(c, {"OWN-P-10432": "Business", "OWN-P-10432-B": "Business"})
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")
            self.drop_rows(c, "Ownership.type")
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "pending")
            self.assertIn("binds no field to Ownership.type", self.report_text(c.dir))

    def test_an_erasure_does_not_cover_a_record_whose_creation_time_is_its_content(self):
        """Round 4: the Deleted-state check asked only that the creation time was non-empty, so
        pointing the map row at the field still holding the content made the content count as
        preserved metadata and the exclusion was granted."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            erased = model["audit_records"][0]["id"]
            model["audit_records"][0] = {"id": erased, "creator": "Branch Manager",
                                         "value": "Ownership assigned to OWN-ATTACKER"}
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-SUSPEND", "actor": "records-officer"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Audit record.creation time | field | `created_at` |",
                                               "| Audit record.creation time | field | `value` |"))
            self.assertEqual(self.integrity_rows(c.dir).get("REQ-META-OWNERSHIP-022"), "Fail")
            self.assertIn("is not a time this tool can read", self.run_on(c.dir)[1])

    def test_an_erasure_that_grants_nothing_does_not_switch_off_the_content_address_check(self):
        """Round 4: the second loop, the one that decides whether the identity addresses the
        content, skipped every record named by an erasure record whether or not the exclusion was
        granted. Eight mandatory Integrity Tests went from pending to Pass on erasing nothing."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["erasures"] = [{"id": "ERA-%d" % i, "record": rec["id"], "policy": "POL-SUSPEND",
                                  "actor": "records-officer"} for i, rec in enumerate(model["audit_records"])]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            path = "%s/representation-map.md" % self.EX
            # a readable identity with the digest in a field beside it: pending, per CAND-024
            c.write(path, c.read(path).replace("| Audit record.identity | field | `id` |",
                                               "| Audit record.identity | field | `label` |"))
            self.assertEqual(self.integrity_rows(c.dir).get("REQ-META-OWNERSHIP-022"), "pending")

    def test_a_reference_nested_under_id_is_resolved(self):
        """Round 4: a literal skip list applied at every depth, and `id` is the commonest spelling
        of a nested reference there is, so the field holding a superseded content address dangled
        while the report said every reference resolved."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["audit_records"][0]["supersedes"] = {"id": "a" * 64}
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertIn("supersedes.id names %s" % ("a" * 64), self.report_text(c.dir))

    def test_the_claim_clause_is_decided_by_the_run_and_not_by_a_reviewer(self):
        """Round 4: Chapter 8's own clause was left pending, so it blocked establishment in every
        run and a reviewer could record Review Pass on it beside a mandatory Fail."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0].pop("owner")
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("DECL-006"), "Fail", rows.get("DECL-006"))
            path = c.dir / "reviews.md"
            path.write_text("# R\n\n" + self.HEADER +
                            "| DECL-006 | Review Pass | A. Reviewer | 22 September 2026 | it is fine really |\n",
                            encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertEqual(code, 0, printed)
            self.assertIn("decided by the run's own tally rather than by a reviewer", text)
            self.assertIn("| DECL-006 | `Language/Conformance.md` | Declaration | mandatory | Fail |", text)

    def test_a_collection_the_map_does_not_list_is_found_in_every_shape(self):
        """Round 4: the walk listed a collection only when its list was non-empty and every member
        was a record, and never looked at an object of records. One string beside the records, a
        list of lists, an object keyed by identity, or a record nested under a plain object each
        hid a reused identity from both identity Tests."""
        shapes = {
            "one non-record member": lambda m, dup: m["entities"][0].__setitem__("sub", ["note", dict(dup)]),
            "a list of lists": lambda m, dup: m.__setitem__("staged", [[dict(dup)]]),
            "an object keyed by identity": lambda m, dup: m.__setitem__("by_id", {dup["id"]: dict(dup)}),
            "nested under a plain object": lambda m, dup: m.__setitem__("staging", {"shadow": [dict(dup)]}),
        }
        for label, mutate in shapes.items():
            with self.subTest(label), Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                mutate(model, {"id": model["entities"][1]["id"], "name": "Shadow"})
                c.write("%s/model.json" % self.EX, json.dumps(model))
                rows = self.outcomes(c.dir)
                self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Fail", (label, rows.get("REQ-META-IDENTITY-005")))
                self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "pending", (label, rows.get("REQ-META-IDENTITY-008")))

    def test_a_subject_the_map_lists_nowhere_fails_like_one_it_says_it_does_not_represent(self):
        """Round 4: a map row reading "not represented" Failed and deleting the row outright went
        pending, so three ways of saying the same thing about one export gave two answers and the
        claimant chose which by editing their own map."""
        with Copy() as c:
            self.drop_rows(c, "Registry")
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-REGISTRY-002"), "Fail", rows.get("REQ-META-REGISTRY-002"))
            self.assertIn("carries no row for registry", self.report_text(c.dir))

    # --- round 3 of the all-packages test: a verdict a map row can switch off ------------

    def drop_rows(self, c, *rows):
        """Delete map rows by their left-hand cell, as a claimant editing their own map would."""
        path = "%s/representation-map.md" % self.EX
        text = c.read(path)
        for row in rows:
            before = text
            text = "\n".join(l for l in text.splitlines() if not l.startswith("| %s |" % row))
            assert text != before, "no row %s in the map" % row
        c.write(path, text + "\n")

    def test_a_map_that_lists_no_ownership_collection_cannot_pass_the_owner_leg(self):
        """Round 3: the resolution leg was gated on the map declaring an Ownership collection, so an
        export whose map simply did not list one skipped it and passed. The claimant writes the map,
        so that made the verdict a one-line edit of their own artifact."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["entities"]:
                e["owner"] = "OWN-NOWHERE"
            del model["ownership"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.drop_rows(c, "Ownership", "Ownership.identifier", "Ownership.owner", "Ownership.owned object",
                           "Ownership.responsibility scope", "Ownership.effective date")
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-ENTITY-004"), "pending", rows.get("REQ-MODELS-ENTITY-004"))
            self.assertIn("lists no Ownership collection", self.report_text(c.dir))

    LIFECYCLE_TESTS = ("REQ-MODELS-LIFECYCLE-007", "REQ-MODELS-ENTITY-008", "REQ-LIFECYCLES-003",
                       "REQ-MODELS-WORKFLOW-011")

    def test_the_lifecycle_engines_read_no_literal_key(self):
        """Round 3: `state_names`, `transitions_of`, `lifecycle_index` and `workflow_violations`
        read `name`, `from`, `to`, `entity` and `id` when the map bound no row, so seven map rows
        could be deleted with every verdict unchanged: the legs compared None with None and passed."""
        with Copy() as c:
            self.drop_rows(c, "State.name", "Transition.from", "Transition.to", "Transition.entity")
            rows = self.outcomes(c.dir)
            for alias in self.LIFECYCLE_TESTS:
                self.assertEqual(rows.get(alias), "pending", (alias, rows.get(alias)))
            self.assertIn("binds no field to State.name", self.report_text(c.dir))
        with Copy() as c:
            self.drop_rows(c, "Lifecycle.identifier", "Entity.identity", "Entity.identifier",
                           "Object.identity", "Object.identifier")
            rows = self.outcomes(c.dir)
            for alias in self.LIFECYCLE_TESTS:
                self.assertNotEqual(rows.get(alias), "Pass", alias)

    def test_an_export_whose_entities_name_no_domain_cannot_pass_primary_governance(self):
        """Round 3: the leg flagged an Entity only when its Domain was a list of more than one, so
        an absent field flagged nothing and the reason asserted that every Entity names one."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["entities"]:
                e.pop("domain", None)
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-DOMAIN-010"), "pending", rows.get("REQ-MODELS-DOMAIN-010"))
        with Copy() as c:
            self.drop_rows(c, "Entity.domain")
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-DOMAIN-010"), "pending", rows.get("REQ-MODELS-DOMAIN-010"))

    def test_a_collection_of_records_nested_in_a_record_is_not_invisible(self):
        """Round 3: the unlisted-collection rule read the top level only, so a collection of records
        placed inside a record reused an identity while both identity Tests passed."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["sub_entities"] = [{"id": model["entities"][1]["id"], "name": "Shadow"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Fail", rows.get("REQ-META-IDENTITY-005"))
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "pending", rows.get("REQ-META-IDENTITY-008"))
            self.assertIn("entities[].sub_entities", self.report_text(c.dir))

    def test_a_collection_that_carries_no_identity_is_reported_and_not_failed_as_one(self):
        """The mirror of the same rule: a block of records carrying no identity the map binds is
        outside every Test, which the Pass says, but it is not an identity in no declared scope."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["export_log"] = [{"step": "extract", "at": "2026-09-23"}, {"step": "serialize", "at": "2026-09-23"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Pass", rows.get("REQ-META-IDENTITY-005"))
            printed = self.run_on(c.dir)[1]
            self.assertIn("carry no identity it binds", printed)
            self.assertIn("export_log", printed)

    def shared_ownership(self, c, second):
        model = json.loads(c.read("%s/model.json" % self.EX))
        model["ownership"].append(second)
        c.write("%s/model.json" % self.EX, json.dumps(model))
        return self.outcomes(c.dir)

    def test_a_second_ownership_record_is_seen_even_when_the_owner_names_one_by_identifier(self):
        """Round 3: the by_id branch returned before the shared-ownership leg ran, so an Entity whose
        owner named a record by its identifier passed with a second Ownership record naming it and
        the reason said "the one Ownership record that names it". CAND-025 counts one accountable."""
        with Copy() as c:
            rows = self.shared_ownership(c, {"id": "OWN-P-10432-B", "owner": "Data Governance Office",
                                             "owned_object": "P-10432", "responsibility_scope": "Second.",
                                             "effective_date": "2024-01-01"})
            self.assertEqual(rows.get("REQ-MODELS-ENTITY-004"), "Pass", rows.get("REQ-MODELS-ENTITY-004"))
            printed = self.run_on(c.dir)[1]
            self.assertIn("shared between several Ownership records", printed)
        with Copy() as c:
            # and where the owner singles out none of them, it fails rather than passing on presence
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append({"id": "OWN-P-10432-B", "owner": "Data Governance Office",
                                       "owned_object": "P-10432", "responsibility_scope": "Second.",
                                       "effective_date": "2024-01-01"})
            for e in model["entities"]:
                if e["id"] == "P-10432":
                    e["owner"] = "Somebody Else"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")
            self.assertIn("singles out 0 of them", self.report_text(c.dir))

    def declare_accountable_type(self, c, types):
        """Give every Ownership record a Type and declare which one is accountable (CAND-025)."""
        model = json.loads(c.read("%s/model.json" % self.EX))
        for rec in model["ownership"]:
            rec["ownership_type"] = types.get(rec["id"], "Business")
        c.write("%s/model.json" % self.EX, json.dumps(model))
        path = "%s/representation-map.md" % self.EX
        c.write(path, c.read(path).replace("| Integrity.method |",
                "| Ownership.type | field | `ownership_type` |\n"
                "| Ownership.accountable type | declaration | `Business` |\n| Integrity.method |"))

    def test_the_accountable_ownership_type_is_counted_where_the_map_declares_it(self):
        """CAND-025's Decision counts "exactly one Ownership record of the accountable Type per
        Entity". Nothing read an Ownership Type until round 3 found the Decision enforced by nothing."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append({"id": "OWN-P-10432-B", "owner": "Data Governance Office",
                                       "owned_object": "P-10432", "responsibility_scope": "Second.",
                                       "effective_date": "2024-01-01"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.declare_accountable_type(c, {"OWN-P-10432": "Business", "OWN-P-10432-B": "Data"})
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Pass")
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append({"id": "OWN-P-10432-B", "owner": "Data Governance Office",
                                       "owned_object": "P-10432", "responsibility_scope": "Second.",
                                       "effective_date": "2024-01-01"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            # two records of the accountable Type name the same Entity: accountability is singular
            self.declare_accountable_type(c, {"OWN-P-10432": "Business", "OWN-P-10432-B": "Business"})
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")
            self.assertIn("carry the accountable Ownership Type the map declares", self.run_on(c.dir)[1])

    def test_the_owner_leg_says_when_no_accountable_type_is_declared(self):
        """A Test that reads accountability from the owner's own pointer says so, rather than
        reporting the rule CAND-025 states."""
        code, printed = self.run_on(ROOT)
        self.assertEqual(code, 0, printed)
        self.assertIn("no accountable Ownership Type declared", printed)

    def test_an_extension_declaration_is_read_and_not_merely_present(self):
        """Round 3: both extension Declaration Tests returned Pass whenever the `Supported
        extensions` field was non-empty, including `none`, which this tool's own vocabulary calls an
        absence, and including a sentence declaring the violation they forbid. Section 5 of the
        suite binds them to the four attestations Chapter 8 imposes."""
        statement = "%s/conformance-statement.md" % self.EX
        ALL = {"compatibility": "yes", "semantics": "yes", "identifiability": "yes",
               "documentation": "yes", "conformance": "yes"}
        cases = (("none", {}, "Not Applicable", "Not Applicable"),
                 ("-", {}, "Not Applicable", "Not Applicable"),
                 ("OCOM-Finance v1, which changes the normative semantics of Ownership", {}, "Fail", "Fail"),
                 ("OCOM-Finance v1", {"compatibility": "yes", "semantics": "yes"}, "Fail", "Fail"),
                 # round 4: every marker a keyword reading looks for appears in a sentence denying it.
                 # round 5: and a qualification outside any denial list reads as an assertion, so the
                 # attestations are four fields with a closed vocabulary rather than prose
                 ("OCOM-Finance v1", dict(ALL, compatibility="preserved only in part"), "Fail", "Pass"),
                 ("OCOM-Finance v1", dict(ALL, semantics="unchanged apart from Domain governance, "
                                                         "which this extension redefines"), "Fail", "Pass"),
                 ("OCOM-Finance v1", dict(ALL, conformance="invalidated"), "Pass", "Fail"),
                 ("OCOM-Finance v1", ALL, "Pass", "Pass"))
        for extensions, attestations, decl2, decl3 in cases:
            with self.subTest(extensions=extensions, attestations=sorted(attestations.items())[:1]), Copy() as c:
                text = c.read(statement).replace("**Supported extensions:** none",
                                                 "**Supported extensions:** %s" % extensions)
                for key, value in attestations.items():
                    text += "\n**Extension attestation %s:** %s\n" % (key, value)
                c.write(statement, text)
                rows = self.outcomes(c.dir)
                self.assertEqual(rows.get("DECL-002"), decl2, (extensions, rows.get("DECL-002")))
                self.assertEqual(rows.get("DECL-003"), decl3, (extensions, rows.get("DECL-003")))

    def map_erasures(self, c):
        path = "%s/representation-map.md" % self.EX
        c.write(path, c.read(path)
                .replace("| Registry | collection | `registries` |", "| Registry | collection | `registries` |\n| Erasure | collection | `erasures` |")
                .replace("| Integrity.method |", "| Erasure.identifier | field | `id` |\n| Erasure.erased record | field | `record` |\n| Erasure.policy | field | `policy` |\n| Erasure.actor | field | `actor` |\n"
                         "| Audit record.creation time | field | `created_at` |\n| Audit record.creator | field | `creator` |\n| Integrity.method |"))

    @staticmethod
    def erase(rec):
        """What `Memory/Retention.md`'s Deleted state leaves of a record: its identity, its creation
        time, its creator and its demonstration of integrity, and nothing else. Blanking one field
        and keeping the rest is not an erasure, and the suite refuses the exclusion for it."""
        return {k: v for k, v in rec.items() if k in ("id", "created_at", "creator")}

    def report_text(self, root):
        out = pathlib.Path(tempfile.mkdtemp()) / "r.md"
        code, printed = run(root, VALIDATE, "--model", "%s/model.json" % self.EX,
                            "--map", "%s/representation-map.md" % self.EX,
                            "--statement", "%s/conformance-statement.md" % self.EX, "--report", str(out))
        self.assertEqual(code, 0, printed)
        text = out.read_text(encoding="utf-8")
        shutil.rmtree(out.parent, ignore_errors=True)
        return text

    def test_an_erasure_record_naming_no_policy_and_no_actor_grants_no_exclusion(self):
        """AO-085: the exclusion is granted only by an erasure record that can itself be checked.
        A record that names neither a Policy nor an actor leaves the erased record to be verified
        like any other, and an erased record no longer verifies."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            erased = model["audit_records"][0]["id"]
            model["audit_records"][0]["value"] = "[erased]"
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "created_at": "2026-09-21T00:00:00Z"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Fail", rows)
            text = self.report_text(c.dir)
            self.assertIn("grants no exclusion: names no Policy; names no actor", text)

    def test_an_erasure_record_naming_an_undeclared_policy_grants_no_exclusion(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            erased = model["audit_records"][0]["id"]
            model["audit_records"][0]["value"] = "[erased]"
            model["erasures"] = [{"id": "ERA-0001", "record": erased, "policy": "POL-NOWHERE", "actor": "records-officer", "created_at": "2026-09-21T00:00:00Z"}]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.map_erasures(c)
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "Fail", rows)
            self.assertIn("names Policy POL-NOWHERE, which the export does not declare", self.report_text(c.dir))

    def test_a_domain_identity_renamed_with_the_map_still_finds_the_overlap(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for dom in model["domains"]:
                dom["dom_key"] = dom.pop("id")
            model["domains"].append({"dom_key": "DOM-SECOND", "name": "Second", "purpose": "overlap", "owner": "OWN-DOM-LENDING", "entity_types": ["Item"]})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            path = "%s/representation-map.md" % self.EX
            c.write(path, c.read(path).replace("| Domain.identifier | field | `id` |", "| Domain.identifier | field | `dom_key` |\n| Domain.identity | field | `dom_key` |"))
            code, out = self.run_on(c.dir)
            self.assertNotIn("Fail 0", out)

    def test_a_collection_that_is_not_a_list_of_records_fails_closed(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["audit_records"] = {"not": "a list"}
            c.write("%s/model.json" % self.EX, json.dumps(model))
            code, out = self.run_on(c.dir)
            self.assertNotEqual(code, 0, out)
            self.assertIn("not a list of records", out)

    def test_the_catalogue_binds_the_scope_rule_to_declaration(self):
        code, out = run(ROOT, CATALOGUE, "--census")
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"Declaration\s+1 \(mandatory 1\)")
        row = [l for l in (ROOT / "docs/Governance/Test-Catalogue.md").read_text(encoding="utf-8").splitlines()
               if l.startswith("| REQ-META-IDENTITY-005 |")]
        self.assertEqual(len(row), 1)
        self.assertIn("| Declaration |", row[0])

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

    def test_an_entity_with_two_owners_fails_the_one_owner_statement(self):
        """CAND-025: `Every Entity shall have one responsible owner` is a count, not a presence."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["owner"] = ["OWN-P-10432", "OWN-LIB-000198"]
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")

    def test_an_owner_naming_another_objects_ownership_record_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["owner"] = "OWN-LIB-000198"      # names the Item's Ownership record
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")

    def test_shared_ownership_needs_the_owner_to_say_which_record_is_accountable(self):
        """Several Ownership records may name one Entity (Shared Ownership); its owner must say
        which one is accountable. A party name that matches exactly one of them passes, a name that
        matches none fails."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append({"id": "OWN-P-10432-DATA", "owner": "Data Office", "owned_object": "P-10432",
                                       "responsibility_scope": "Personal data of the record.", "effective_date": "2024-01-08"})
            model["entities"][0]["owner"] = "Membership Desk"     # the party named by OWN-P-10432, not a record id
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Pass")
            model["entities"][0]["owner"] = "Nobody In Particular"
            c.write("%s/model.json" % self.EX, json.dumps(model))
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")

    def probe_two_systems(self, c, path_keyed):
        """An SAP-shaped and a ServiceNow-shaped record carrying the same bare identifier under two
        declared systems, plus a bare reference to it. Returns the outcomes and the report text."""
        model = json.loads(c.read("%s/model.json" % self.EX))
        sap = dict(model["entities"][0], id="BP-1000001", name="SAP business partner 1000001", owner="OWN-BP-1000001")
        model["ownership"].append({"id": "OWN-BP-1000001", "owner": "Master Data Office", "owned_object": "BP-1000001",
                                   "responsibility_scope": "The partner record.", "effective_date": "2024-01-08"})
        model["relationships"].append({"id": "REL-PROBE", "source": "BP-1000001", "target": "LIB-000198",
                                       "type": "Association", "cardinality": model["relationships"][0]["cardinality"]})
        path = "%s/representation-map.md" % self.EX
        m = c.read(path)
        if path_keyed:
            model["entities"].append(sap)
            model["entities_snow"] = [dict(sap, name="ServiceNow record 1000001")]
            m = m.replace("| Entity | collection | `entities` |", "| Entity | collection | `entities`, `entities_snow` |")
            m = m.replace("| Integrity.method |", "| Entity.identity scope | declaration | `External System` |\n"
                          "| entities.identity system | declaration | `SAP S/4HANA` |\n"
                          "| entities_snow.identity system | declaration | `ServiceNow` |\n| Integrity.method |")
        else:
            model["entities"].append(sap)
            model["capabilities"].append({"id": "BP-1000001", "name": "ServiceNow asset 1000001", "purpose": "probe"})
            m = m.replace("| Integrity.method |", "| Entity.identity scope | declaration | `External System` |\n"
                          "| Entity.identity system | declaration | `SAP S/4HANA` |\n"
                          "| Capability.identity scope | declaration | `External System` |\n"
                          "| Capability.identity system | declaration | `ServiceNow` |\n| Integrity.method |")
        c.write("%s/model.json" % self.EX, json.dumps(model))
        c.write(path, m)
        return self.outcomes(c.dir), self.report_text(c.dir)

    def test_the_same_identifier_under_two_declared_systems_is_two_identities(self):
        """CAND-026: two systems' keys coexist in one export as identities of two declared scopes.
        The enterprise evaluation of 22 September 2026 ran the suite on such an export and found it
        comparing bare strings: SAP BP 1000001 and ServiceNow 1000001 failed REQ-META-OBJECT-003 and
        REQ-META-IDENTITY-008 while the page promised the opposite."""
        with Copy() as c:
            rows, text = self.probe_two_systems(c, path_keyed=False)
            self.assertEqual(rows.get("REQ-META-OBJECT-003"), "Pass", rows.get("REQ-META-OBJECT-003"))
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Pass", rows.get("REQ-META-IDENTITY-008"))
            # `Adoption/Reference Serialization.md` says a bare reference to an identity the export
            # declares in two scopes is ambiguous and is not resolved to either, so the owner leg
            # reports that it could not resolve rather than resolving by bare key. Until round 3 it
            # compared the scope and dropped the system, so every source system shared one namespace
            # and a ServiceNow record resolved to an SAP record's Ownership record.
            self.assertEqual(rows.get("REQ-MODELS-ENTITY-004"), "pending", rows.get("REQ-MODELS-ENTITY-004"))
            self.assertIn("carries an identity the export declares in 2 namespaces", text)
            # a bare reference to an identity that exists in two scopes is ambiguous, and the report says so
            self.assertIn("REL-PROBE.source names BP-1000001, an identity the export declares in 2 scopes", text)

    def test_a_declaration_keyed_by_collection_path_separates_two_sources_of_one_type(self):
        with Copy() as c:
            rows, text = self.probe_two_systems(c, path_keyed=True)
            self.assertEqual(rows.get("REQ-META-OBJECT-003"), "Pass", rows.get("REQ-META-OBJECT-003"))
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Pass", rows.get("REQ-META-IDENTITY-008"))
            self.assertIn("declares in 2 scopes", text)

    def test_the_same_identifier_within_one_scope_is_still_a_reuse(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["capabilities"].append({"id": model["entities"][0]["id"], "name": "clash", "purpose": "probe"})
            c.write("%s/model.json" % self.EX, json.dumps(model))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Fail")
            self.assertEqual(rows.get("REQ-META-OBJECT-003"), "Fail")

    REVIEWS = "docs/Examples/Conformance/reviewer-record.md"
    HEADER = "| Test | Outcome | Reviewer | Date | Reason |\n|---|---|---|---|---|\n"

    def run_with_reviews(self, root, reviews_path):
        out = pathlib.Path(tempfile.mkdtemp()) / "r.md"
        code, printed = run(root, VALIDATE, "--model", "%s/model.json" % self.EX,
                            "--map", "%s/representation-map.md" % self.EX,
                            "--statement", "%s/conformance-statement.md" % self.EX,
                            "--reviews", str(reviews_path), "--report", str(out))
        text = out.read_text(encoding="utf-8") if out.exists() else ""
        shutil.rmtree(out.parent, ignore_errors=True)
        return code, printed, text

    def test_the_reviewer_record_decides_review_tests_under_the_reviewers_name(self):
        """Section 3: a Review Pass is a named reviewer's recorded judgment; Section 4: the report
        carries the reviewer's identity. The example's illustrative record decides three Statements."""
        code, printed, text = self.run_with_reviews(ROOT, ROOT / self.REVIEWS)
        self.assertEqual(code, 0, printed)
        self.assertIn("reviewed 3 pass and 0 fail", printed)
        row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-ENTITY-003 |")][0]
        self.assertIn("| Review Pass |", row)
        self.assertIn("Example reviewer (first party), 22 September 2026:", row)
        self.assertIn("- Example reviewer (first party): 3 judgment(s)", text)
        self.assertIn("not established", printed)

    JUDGMENT = "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | A reason long enough to be read. |\n"

    def test_a_reviewer_record_that_declares_fewer_than_three_digests_is_refused(self):
        """Round 3: the run compared whatever subset of model, map and statement the line happened
        to name, so a record naming one digest was accepted against any map and any Conformance
        Statement while the report printed that all three were verified. Section 3 fixes the grammar."""
        digest = hashlib.sha256((ROOT / self.EX / "model.json").read_bytes()).hexdigest()[:16]
        for line in ("**Recorded against:** model `%s`" % digest,
                     "**Recorded against:** model `%s`, statement `nothing`" % digest,
                     "**Recorded against:** nothing in particular"):
            with self.subTest(line=line[:44]), Copy() as c:
                path = c.dir / "reviews.md"
                path.write_text("# R\n\n%s\n\n%s%s" % (line, self.HEADER, self.JUDGMENT), encoding="utf-8")
                code, printed, text = self.run_with_reviews(c.dir, path)
                self.assertNotEqual(code, 0, printed)
                self.assertIn("names fewer binds its judgments to less", printed)

    def test_a_judgment_inside_a_fence_or_a_comment_is_not_a_judgment(self):
        """Round 3: every line starting with `|` was read as a judgment, so a row written inside a
        ``` fence to illustrate the format was counted as a named reviewer's judgment and cleared a
        mandatory Test. The shipped record is full of exactly that kind of prose."""
        illustration = "| REQ-META-OBJECT-004 | Review Pass | Nobody At All | 22 September 2026 | A reason long enough to be read. |"
        for name, block in {"fence": "```\n%s\n```\n\n" % illustration,
                            "tilde fence": "~~~\n%s\n~~~\n\n" % illustration}.items():
            with self.subTest(name), Copy() as c:
                path = c.dir / "reviews.md"
                path.write_text("# R\n\n" + block + self.HEADER + self.JUDGMENT, encoding="utf-8")
                code, printed, text = self.run_with_reviews(c.dir, path)
                self.assertEqual(code, 0, printed)
                self.assertIn("reviewed 1 pass", printed, name)
                self.assertNotIn("Nobody At All", text, name)
                self.assertIn("1 judgment-shaped row(s) inside a fenced block", printed, name)

    def test_a_comment_that_hides_a_judgment_row_stops_the_run(self):
        """Round 5: the comment filter removed spans, so a comment opening inside one row's Reason
        cell and closing after a later row deleted the rows between them, Review Fails included,
        with the markers balanced and nothing printed. A filter that silently removes something
        judgment-shaped is the defect this function has had twice."""
        illustration = "| REQ-META-OBJECT-004 | Review Fail | Nobody At All | 22 September 2026 | A reason long enough to be read. |"
        for name, block in {"whole row": "<!--\n%s\n-->\n\n" % illustration,
                            "opened in a cell": "%s\n" % illustration.replace("read. |", "read. <!-- |")
                                                + "%s\n-->\n" % illustration}.items():
            with self.subTest(name), Copy() as c:
                path = c.dir / "reviews.md"
                path.write_text("# R\n\n" + self.HEADER + self.JUDGMENT + block, encoding="utf-8")
                code, printed, text = self.run_with_reviews(c.dir, path)
                self.assertNotEqual(code, 0, printed)
                self.assertIn("inside an HTML comment", printed)

    def test_a_reviewer_record_that_cannot_be_attributed_stops_the_run(self):
        """A judgment without a name, a reason, a readable date, a known Test or a permitted outcome
        is not a judgment, and two rows for one Test are a contradiction; each stops the run."""
        cases = {
            "unknown test": "| REQ-NOWHERE-001 | Review Pass | A. Reviewer | 22 September 2026 | reason |\n",
            "bad outcome": "| REQ-MODELS-ENTITY-003 | Pass | A. Reviewer | 22 September 2026 | reason |\n",
            "no reviewer": "| REQ-MODELS-ENTITY-003 | Review Pass |  | 22 September 2026 | reason |\n",
            "bad date": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | yesterday | reason |\n",
            "no reason": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 |  |\n",
            "duplicate": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | one |\n| REQ-MODELS-ENTITY-003 | Review Fail | B. Reviewer | 22 September 2026 | two |\n",
            "empty": "",
        }
        for name, rows in cases.items():
            with Copy() as c:
                path = c.dir / "reviews.md"
                path.write_text("# Reviewer Record\n\n" + self.HEADER + rows, encoding="utf-8")
                code, printed, text = self.run_with_reviews(c.dir, path)
                self.assertNotEqual(code, 0, "%s: %s" % (name, printed))
                self.assertNotIn("reviewed 1 pass", printed, name)

    def test_a_reviewer_record_the_tool_cannot_attribute_is_refused(self):
        """The gates were shape-only: 2026-13-45 was a date, "." was a reviewer, a second table of
        judgments was read by nobody, and a six-column row was accepted because the header matched
        with startswith."""
        cases = {
            "impossible date": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 2026-13-45 | examined the identifiers |\n",
            "punctuation reviewer": "| REQ-MODELS-ENTITY-003 | Review Pass | . | 22 September 2026 | examined the identifiers |\n",
            "reason too short": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | ok |\n",
            "six columns": "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | examined the identifiers | extra |\n",
        }
        for name, rows in cases.items():
            with Copy() as c:
                path = c.dir / "reviews.md"
                path.write_text("# Reviewer Record\n\n" + self.HEADER + rows, encoding="utf-8")
                code, printed, text = self.run_with_reviews(c.dir, path)
                self.assertNotEqual(code, 0, "%s: %s" % (name, printed))
        with Copy() as c:      # a second table of judgments must not sit in the file unread
            path = c.dir / "reviews.md"
            good = "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | examined the identifiers |\n"
            path.write_text("# Reviewer Record\n\n" + self.HEADER + good + "\n## Second thoughts\n\n" + self.HEADER + good, encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertNotEqual(code, 0, printed)
            self.assertIn("carries 2 headers", printed)

    def test_the_report_carries_what_section_4_says_a_report_carries(self):
        code, printed, text = self.run_with_reviews(ROOT, ROOT / self.REVIEWS)
        self.assertEqual(code, 0, printed)
        for item in ("**Read from:** the checkout at", "Release v1.4.0", "Requirement Register: 335 Statements",
                     "Alias File revision:", "**Inputs, by content:**", "**Reviewer Record:**", "## Reviewers"):
            self.assertIn(item, text, item)

    def test_a_long_reason_is_cut_with_a_marker_not_silently(self):
        with Copy() as c:
            path = c.dir / "reviews.md"
            reason = "examined the identifiers and they are technology independent, " * 6 + "but the third one is a database key"
            path.write_text("# Reviewer Record\n\n" + self.HEADER +
                            "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | %s |\n" % reason, encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertEqual(code, 0, printed)
            row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-ENTITY-003 |")][0]
            self.assertIn("... (cut here; the whole reason is in the Reviewer Record)", row)

    def test_a_disposition_cell_is_read_exactly_not_as_a_substring(self):
        """A free-text cell containing the word Descriptive removed a mandatory Test from the
        denominator; the cell is now compared exactly."""
        with Copy() as c:
            path = "docs/Governance/Test-Catalogue.md"
            text = c.read(path)
            row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-ENTITY-004 |")][0]
            c.write(path, text.replace(row, row.rstrip().rstrip("|") + " Review, and certainly not Descriptive |"))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-ENTITY-004"), "Pass", "a cell that merely mentions Descriptive must not delete the Test")

    def test_a_judgment_never_overrides_a_mechanical_outcome(self):
        with Copy() as c:
            path = c.dir / "reviews.md"
            path.write_text("# Reviewer Record\n\n" + self.HEADER +
                            "| REQ-MODELS-ENTITY-004 | Review Fail | A. Reviewer | 22 September 2026 | I disagree with the machine. |\n", encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertEqual(code, 0, printed)
            self.assertIn("reviewed 0 pass and 0 fail", printed)
            row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-ENTITY-004 |")][0]
            self.assertIn("| Pass |", row)
            self.assertIn("not applied, REQ-MODELS-ENTITY-004: A. Reviewer recorded Review Fail, but the Test decided Pass mechanically", text)

    def test_a_review_fail_blocks_core_conformance_and_a_complete_record_establishes_it(self):
        """The end-to-end path Section 3 describes: with every Test the export cannot settle judged
        Review Pass by a named reviewer, Core Conformance is established; one Review Fail among
        them and it is not."""
        with Copy() as c:
            text = self.report_text(c.dir)          # no record: everything a reviewer may decide is pending
            pending = [l.split("|")[1].strip() for l in text.splitlines()
                       if (l.startswith("| REQ-") or l.startswith("| DECL-")) and "| mandatory | pending |" in l]
            self.assertGreater(len(pending), 100, "the example stopped leaving Statements to a reviewer")
            # Chapter 8's own clause about claiming conformance is decided by the run's own tally,
            # not by a reviewer: it is pending only until the rest are decided
            self.assertIn("DECL-006", pending)
            pending.remove("DECL-006")
            rows = "".join("| %s | Review Pass | Named Reviewer | 2026-09-22 | examined, met |\n" % a for a in pending)
            path = c.dir / "complete.md"
            path.write_text("# Reviewer Record\n\n" + self.HEADER + rows, encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertEqual(code, 0, printed)
            self.assertIn("pending 0, reviewed %d pass and 0 fail. Core Conformance established" % len(pending), printed)
            self.assertIn("| DECL-006 | `Language/Conformance.md` | Declaration | mandatory | Pass |", text)
            rows = rows.replace("| %s | Review Pass |" % pending[0], "| %s | Review Fail |" % pending[0], 1)
            path.write_text("# Reviewer Record\n\n" + self.HEADER + rows, encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertIn("pending 0, reviewed %d pass and 1 fail. Core Conformance not established" % (len(pending) - 1), printed)

    def model_map(self, c, model, map_text=None):
        c.write("%s/model.json" % self.EX, json.dumps(model))
        if map_text is not None:
            c.write("%s/representation-map.md" % self.EX, map_text)

    def test_identity_is_resolved_through_the_most_specific_type_the_map_names(self):
        """The all-packages test of 22 September 2026: identity_of took the first type in map order,
        so the generic Object row answered for a collection that spells its identity otherwise and
        the reuse Invariant passed having counted those records zero times."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for d in model["domains"]:
                d["domain_key"] = d.pop("id")
            model["domains"].append({"domain_key": "DOM-LENDING", "name": "Second", "purpose": "overlap",
                                     "owner": "OWN-DOM-LENDING", "entity_types": ["Item"]})
            self.model_map(c, model, c.read("%s/representation-map.md" % self.EX)
                           .replace("| Domain.identifier | field | `id` |", "| Domain.identifier | field | `domain_key` |"))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-008"), "Fail")

    def test_a_record_whose_identity_the_map_does_not_bind_is_not_given_one(self):
        """There is no fallback to a literal `id` key: an export that binds its identity elsewhere
        must be read through the map, and an Object the map leaves unbound is pending, not passed."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for e in model["entities"]:
                e["key"] = e.pop("id")
            model["entities"].append(dict(model["entities"][0], key=model["entities"][0]["key"]))
            self.model_map(c, model)          # the map still says `id`
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "pending", rows.get("REQ-META-IDENTITY-008"))
            self.assertIn("carry no identity the Representation Map binds", self.report_text(c.dir))

    def test_a_verdict_does_not_depend_on_the_order_of_rows_in_the_map(self):
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            lines = c.read(path).splitlines()
            obj = [i for i, l in enumerate(lines) if l.startswith("| Object | collection |")][0]
            ent = [i for i, l in enumerate(lines) if l.startswith("| Entity | collection |")][0]
            lines.insert(obj, lines.pop(ent))
            c.write(path, "\n".join(lines) + "\n")
            self.assertEqual(self.outcomes(c.dir), self.outcomes(ROOT))

    def test_declaring_a_scope_for_one_type_does_not_exempt_the_others_from_the_reuse_rule(self):
        """An empty scope is not a scope: keying uniqueness by "no declaration" made it a namespace
        of its own, so one declaration row turned a real reuse from Fail into Pass."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["capabilities"].append({"id": model["entities"][0]["id"], "name": "clash", "purpose": "probe"})
            self.model_map(c, model, c.read("%s/representation-map.md" % self.EX)
                           .replace("| Identity.scope | declaration | `Organization` |",
                                    "| Entity.identity scope | declaration | `External System` |\n| Entity.identity system | declaration | `SAP` |"))
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Fail", rows.get("REQ-META-IDENTITY-008"))
            self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Fail", "a declaration that covers part of the export is not a declaration")

    def test_an_integrity_test_over_only_erased_records_is_pending_not_passed(self):
        """The exclusion is granted by records the claimant writes, so a Pass over zero verified
        records would let an export erase its way to eight Integrity Passes."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["erasures"] = []
            for i, rec in enumerate(list(model["audit_records"])):
                model["audit_records"][i] = self.erase(rec)
                model["erasures"].append({"id": "ERA-%s" % rec["id"][:6], "record": rec["id"],
                                          "policy": "POL-SUSPEND", "actor": "records-officer"})
            self.model_map(c, model)
            self.map_erasures(c)
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)
            self.assertIn("0 of 3 audit record record(s) verified", self.report_text(c.dir))

    def test_an_erasure_record_that_names_itself_or_a_record_the_export_lacks_grants_nothing(self):
        for case, named in (("itself", "SELF"), ("a record the export does not carry", "AUD-NOWHERE")):
            with Copy() as c:
                model = json.loads(c.read("%s/model.json" % self.EX))
                erased = model["audit_records"][0]["id"]
                model["audit_records"][0]["value"] = "[erased]"
                ident = erased if named == "SELF" else named
                model["erasures"] = [{"id": "ERA-0001", "record": ident, "policy": "POL-SUSPEND", "actor": "officer"}]
                if named == "SELF":
                    model["erasures"][0]["id"] = erased          # the erasure names its own identity
                self.model_map(c, model)
                self.map_erasures(c)
                self.assertEqual(self.integrity_rows(c.dir).get("REQ-META-OWNERSHIP-022"), "Fail", case)
                self.assertIn("grants no exclusion", self.report_text(c.dir), case)

    def test_a_digest_beside_a_readable_identity_is_not_a_content_address(self):
        """The guard compared two map rows, so a map could declare content-addressed identity while
        every other leg resolved a different, mutable identity for the same record."""
        with Copy() as c:
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            import importlib, validate as V
            importlib.reload(V)
            model = json.loads(c.read("%s/model.json" % self.EX))
            for i, rec in enumerate(model["audit_records"], 1):
                rec["id"] = "AUD-%04d" % i          # a readable, mutable identity
                rec["digest"] = V.canonical_digest(rec, "digest")   # and a digest beside it that verifies
            self.model_map(c, model, c.read("%s/representation-map.md" % self.EX)
                           .replace("| Audit record.integrity | field | `id` |", "| Audit record.integrity | field | `digest` |"))
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-META-OWNERSHIP-022"), "pending", rows)
            self.assertIn("the identity this export resolves for record", self.report_text(c.dir))

    def test_an_owner_that_resolves_to_no_ownership_record_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["owner"] = "OWN-NOWHERE"
            self.model_map(c, model)
            self.assertEqual(self.outcomes(c.dir).get("REQ-MODELS-ENTITY-004"), "Fail")

    def test_removing_the_terminal_states_row_does_not_turn_the_check_into_a_pass(self):
        """The terminal leg read `r.value(...) or []`, so an unbound map row made the loop body
        never run and the Test reported "no terminal State is left" having read nothing."""
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            kept = [l for l in c.read(path).splitlines() if not l.startswith("| Lifecycle.terminal states |")]
            c.write(path, "\n".join(kept) + "\n")
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-LIFECYCLE-002"), "pending", rows.get("REQ-MODELS-LIFECYCLE-002"))
            self.assertIn("terminal States", self.report_text(c.dir))

    def test_an_event_into_a_state_the_lifecycle_does_not_define_fails(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["events"].append({"id": "e" * 64, "type": "Probe", "subject": "LIB-000198",
                                    "occurred_at": "2026-08-10T10:00:00Z", "source": "probe",
                                    "from_state": None, "to_state": "Evaporated"})
            self.model_map(c, model)
            rows = self.outcomes(c.dir)
            # the Event leg decides the Lifecycles Statement; REQ-MODELS-WORKFLOW-008 is about
            # Workflow steps and is decided from the Workflow collection since round 2
            self.assertEqual(rows.get("REQ-LIFECYCLES-003"), "Fail", rows.get("REQ-LIFECYCLES-003"))
            self.assertIn("a State the Lifecycle does not define", self.report_text(c.dir))

    def test_a_reference_inside_a_nested_object_is_resolved(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["metadata"] = dict(model["entities"][0].get("metadata") or {},
                                                    provenance={"related_record": "AUD-NOWHERE"})
            self.model_map(c, model)
            self.assertIn("names AUD-NOWHERE, which the export does not declare", self.report_text(c.dir))

    def test_a_stem_with_no_list_is_not_passed(self):
        """combine([]) fell through to Pass, so a Statement that is a stem ending in a colon with no
        list reported a mandatory Test as passed having run no procedure."""
        sys.path.insert(0, str(ROOT / "tools" / "conformance"))
        import importlib, validate as V
        importlib.reload(V)
        self.assertEqual(V.combine([], lambda p: (None, "x")), (None, "the Statement is a stem with no list, so no part of it could be run"))

    def test_a_process_phrase_is_not_a_type_and_an_assignment_is(self):
        """subject_of reads both ends of the subject phrase, so 'Every Ownership assignment shall
        define:' resolves to Ownership, while 'Constraint governance shall define:' stays a process."""
        sys.path.insert(0, str(ROOT / "tools" / "conformance"))
        import importlib, validate as V
        importlib.reload(V)
        types = {"ownership": ["ownership"], "constraint": ["constraints"]}
        self.assertEqual(V.subject_of("Every Ownership assignment shall define: Identifier;", types), "ownership")
        self.assertIsNone(V.subject_of("Constraint governance shall define: ownership; approval;", types))

    def test_a_declared_system_splits_the_namespace_only_under_external_system(self):
        """One map row declaring a system under an Organization scope turned one namespace into two
        and let a reused identity pass the no-reuse Invariant."""
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["capabilities"].append({"id": model["entities"][0]["id"], "name": "clash", "purpose": "probe"})
            self.model_map(c, model, c.read("%s/representation-map.md" % self.EX)
                           .replace("| Integrity.method |", "| Entity.identity system | declaration | `SAP` |\n"
                                    "| Capability.identity system | declaration | `ServiceNow` |\n| Integrity.method |"))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-008"), "Fail")

    def test_the_reuse_invariant_compares_every_collection_that_carries_an_identity(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["ownership"].append(dict(model["ownership"][0]))      # a second record with the same id
            self.model_map(c, model)
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-008"), "Fail", rows.get("REQ-META-IDENTITY-008"))

    def test_an_erasure_record_excludes_nothing_outside_the_memory_tier(self):
        """Retention.md governs Memory Records; one erasure record used to exclude a tampered Event
        from its Integrity Test and the report credited Retention.md for it."""
        with Copy() as c:
            sys.path.insert(0, str(c.dir / "tools" / "conformance"))
            import importlib, validate as V
            importlib.reload(V)
            model = json.loads(c.read("%s/model.json" % self.EX))
            target = model["events"][0]["id"]
            model["events"][0]["source"] = "tampered, and the digest no longer matches"
            model["erasures"] = [{"id": "ERA-0001", "record": target, "policy": "POL-SUSPEND", "actor": "officer"}]
            self.model_map(c, model)
            self.map_erasures(c)
            rows = self.integrity_rows(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-EVENT-010"), "Fail", rows)
            self.assertIn("erasure record(s) naming", self.report_text(c.dir))

    def test_a_workflow_statement_is_decided_from_workflow_steps(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["workflows"][0]["transitions"] = [{"entity": "LIB-000198", "from": "Available", "to": "Vaporized"}]
            self.model_map(c, model)
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-WORKFLOW-008"), "Fail", rows.get("REQ-MODELS-WORKFLOW-008"))
            self.assertIn("is not a Transition of", self.report_text(c.dir))

    def test_a_workflow_whose_steps_the_map_cannot_find_is_pending(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            for wf in model["workflows"]:
                wf["steps"] = wf.pop("transitions")
            self.model_map(c, model)
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-WORKFLOW-008"), "pending", rows.get("REQ-MODELS-WORKFLOW-008"))
            self.assertIn("carry none under the field", self.report_text(c.dir))

    def test_an_export_carrying_a_collection_the_map_does_not_list_fails_the_scope_rule(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["sap_partners"] = [{"id": "BP-1", "name": "one"}, {"id": "BP-2", "name": "two"}]
            self.model_map(c, model)
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-META-IDENTITY-005"), "Fail", rows.get("REQ-META-IDENTITY-005"))
            self.assertIn("the Representation Map does not list", self.report_text(c.dir))

    def test_the_ownership_leg_is_pending_when_it_cannot_resolve_anything(self):
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            kept = [l for l in c.read(path).splitlines() if not l.startswith("| Ownership.owned object |")]
            c.write(path, "\n".join(kept) + "\n")
            rows = self.outcomes(c.dir)
            self.assertEqual(rows.get("REQ-MODELS-ENTITY-004"), "pending", rows.get("REQ-MODELS-ENTITY-004"))
            self.assertIn("binds no field to Ownership.owned object", self.report_text(c.dir))

    def test_a_reviewer_record_row_after_a_blank_line_is_read(self):
        """read_table stopped at the first non-row line, so every guard was disabled by one blank
        line: unknown Tests, illegal outcomes and duplicate judgments all slipped through."""
        with Copy() as c:
            path = c.dir / "reviews.md"
            good = "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | examined the identifiers |\n"
            bad = "| REQ-NOWHERE-001 | Review Pass | A. Reviewer | 22 September 2026 | a Test that does not exist |\n"
            path.write_text("# Reviewer Record\n\n" + self.HEADER + good + "\n" + bad, encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertNotEqual(code, 0, printed)
            self.assertIn("names a Test the catalogue does not carry", printed)

    def test_a_reviewer_record_recorded_against_another_export_is_refused(self):
        with Copy() as c:
            model = json.loads(c.read("%s/model.json" % self.EX))
            model["entities"][0]["name"] = "changed after the reviewer read it"
            self.model_map(c, model)
            code, printed, text = self.run_with_reviews(c.dir, c.dir / self.REVIEWS)
            self.assertNotEqual(code, 0, printed)
            self.assertIn("recorded against", printed)

    def test_a_judgment_keeps_the_mechanical_reason_it_replaced(self):
        """A judgment used to overwrite the reason the procedure gave, hiding, for instance, that
        the export models nothing the Statement is about."""
        with Copy() as c:
            path = c.dir / "reviews.md"
            path.write_text("# Reviewer Record\n\n" + self.HEADER +
                            "| REQ-MODELS-ENTITY-003 | Review Pass | A. Reviewer | 22 September 2026 | examined and met |\n",
                            encoding="utf-8")
            code, printed, text = self.run_with_reviews(c.dir, path)
            self.assertEqual(code, 0, printed)
            row = [l for l in text.splitlines() if l.startswith("| REQ-MODELS-ENTITY-003 |")][0]
            self.assertIn("the procedure returned no outcome: awaiting a named reviewer", row)

    def test_the_scope_declaration_decides_the_identity_scope_rule(self):
        """CAND-026: REQ-META-IDENTITY-005 is read from the map's Identity.scope declaration."""
        self.assertEqual(self.outcomes(ROOT).get("REQ-META-IDENTITY-005"), "Pass")
        with Copy() as c:
            path = "%s/representation-map.md" % self.EX
            row = "| Identity.scope | declaration | `Organization` |"
            self.assertIn(row, c.read(path))
            c.write(path, c.read(path).replace(row, ""))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-005"), "pending")
            c.write(path, c.read(path).replace("| Integrity.method |", "| Identity.scope | declaration | `Nowhere` |\n| Integrity.method |"))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-005"), "Fail")
            c.write(path, c.read(path).replace("| Identity.scope | declaration | `Nowhere` |", "| Identity.scope | declaration | `External System` |"))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-005"), "Fail", "External System must name its system")
            c.write(path, c.read(path).replace("| Integrity.method |", "| Identity.system | declaration | `SAP S/4HANA` |\n| Integrity.method |"))
            self.assertEqual(self.outcomes(c.dir).get("REQ-META-IDENTITY-005"), "Pass")

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


def hunt_files(**changes):
    """A two-page site for the error hunt, mutable per test: {path: (content type, body)}."""
    def page(path, title="A page", canonical=None, extra=""):
        canonical = "https://ocom.uno%s" % path if canonical is None else canonical
        return ("text/html; charset=utf-8",
                '<html><head><title>%s</title><link rel="canonical" href="%s">%s</head>'
                '<body><a href="/a">a</a> <a href="/b">b</a> <a href="/logo.png">logo</a> '
                '<a href="https://example.org/">outside</a><a href="#top">top</a></body></html>' % (title, canonical, extra))
    files = {
        "/sitemap.xml": ("application/xml", "<urlset><url><loc>https://ocom.uno/a</loc></url><url><loc>https://ocom.uno/b</loc></url></urlset>"),
        "/a": page("/a", extra='<script type="application/ld+json">{"@context": "https://schema.org"}</script>'),
        "/b": page("/b"),
        "/logo.png": ("image/png", "not really a png"),
        "/robots.txt": ("text/plain", "User-agent: *\nAllow: /\n"),
        "/llms.txt": ("text/plain", "# site\n- [a](https://ocom.uno/a): a page\n- [x](https://ocom.uno/x.json): a record\n"),
        "/discovery.json": ("application/json", json.dumps({"resources": [{"url": "https://ocom.uno/x.json", "mediaType": "application/json"}]})),
        "/x.json": ("application/json", json.dumps({"ok": True})),
    }
    for k, v in changes.items():
        if v is None:
            files.pop(k, None)
        else:
            files[k] = v
    return files


class SiteErrorHunt(unittest.TestCase):
    """The hunt has to notice a broken page, or its zero means nothing."""

    def hunt(self, files):
        with fake_site.Fixture(files) as site:
            return run(ROOT, HUNT, "--base", site.base, "--pause", "0", "--check")

    def test_a_healthy_site_passes(self):
        code, out = self.hunt(hunt_files())
        self.assertEqual(code, 0, out)
        self.assertIn("2 page(s) and 0 record(s) from the sitemap", out)
        self.assertIn("0 failure(s)", out)

    def test_a_broken_internal_link_fails(self):
        files = hunt_files()
        files["/b"] = (files["/b"][0], files["/b"][1].replace('<a href="/a">a</a>', '<a href="/nowhere">gone</a>'))
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("/nowhere (linked from /b) answers 404", out)

    def test_a_page_the_sitemap_names_that_answers_404_fails(self):
        code, out = self.hunt(hunt_files(**{"/b": None}))
        self.assertNotEqual(code, 0, out)
        self.assertIn("/b answers 404", out)

    def test_a_missing_or_wrong_canonical_fails(self):
        files = hunt_files()
        files["/b"] = (files["/b"][0], files["/b"][1].replace('<link rel="canonical" href="https://ocom.uno/b">', ""))
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("/b carries no canonical link", out)
        files = hunt_files()
        files["/b"] = (files["/b"][0], files["/b"][1].replace('href="https://ocom.uno/b"', 'href="https://ocom.uno/a"'))
        code, out = self.hunt(files)
        self.assertIn("/b declares canonical https://ocom.uno/a, not itself", out)

    def test_noindex_a_missing_title_and_bad_jsonld_fail(self):
        files = hunt_files()
        files["/b"] = (files["/b"][0], files["/b"][1].replace("<title>A page</title>", '<title></title><meta name="robots" content="noindex">'))
        files["/a"] = (files["/a"][0], files["/a"][1].replace('{"@context": "https://schema.org"}', '{"@context": '))
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("/b carries no <title>", out)
        self.assertIn("/b asks not to be indexed", out)
        self.assertIn("/a: JSON-LD block 1 does not parse", out)

    def test_a_target_llms_or_discovery_names_that_is_gone_fails(self):
        code, out = self.hunt(hunt_files(**{"/x.json": None}))
        self.assertNotEqual(code, 0, out)
        self.assertIn("llms.txt names https://ocom.uno/x.json, which answers 404", out)
        self.assertIn("discovery.json names https://ocom.uno/x.json, which answers 404", out)

    def test_a_json_record_in_the_sitemap_and_a_url_template_in_discovery_are_not_defects(self):
        files = hunt_files()
        files["/sitemap.xml"] = ("application/xml", files["/sitemap.xml"][1].replace("</urlset>", "<url><loc>https://ocom.uno/x.json</loc></url></urlset>"))
        files["/discovery.json"] = ("application/json", json.dumps({"resources": [
            {"url": "https://ocom.uno/x.json", "mediaType": "application/json"},
            {"url": "https://ocom.uno/explain/{id}", "mediaType": "text/html"}]}))
        code, out = self.hunt(files)
        self.assertEqual(code, 0, out)
        self.assertIn("2 page(s) and 1 record(s) from the sitemap", out)
        self.assertIn("1 URL template(s) not fetched", out)
        files["/x.json"] = ("application/json", "{not json")
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("/x.json does not parse as JSON", out)

    def test_a_duplicated_sitemap_url_and_an_empty_discovery_are_reported(self):
        files = hunt_files()
        files["/sitemap.xml"] = ("application/xml", files["/sitemap.xml"][1].replace("</urlset>", "<url><loc>https://ocom.uno/a</loc></url></urlset>"))
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("sitemap names https://ocom.uno/a 2 times", out)
        files = hunt_files(**{"/discovery.json": ("application/json", json.dumps({"resources": []})),
                              "/llms.txt": ("text/plain", "# nothing here\n")})
        code, out = self.hunt(files)
        self.assertNotEqual(code, 0, out)
        self.assertIn("carries no resources", out)
        self.assertIn("names no URL", out)

    def test_a_sitemap_over_nothing_cannot_pass(self):
        code, out = self.hunt(hunt_files(**{"/sitemap.xml": ("application/xml", "<urlset></urlset>")}))
        self.assertNotEqual(code, 0, out)
        self.assertIn("names no URL", out)

    def test_a_dead_reference_the_regex_used_to_miss_is_found(self):
        """Round 4: one regex over quoted href and src left srcset, unquoted attributes and
        protocol-relative URLs on this site's own host unread, so dead references of those kinds
        produced 0 failures."""
        cases = {
            "srcset": '<img srcset="/missing-a.png 1x, /missing-b.png 2x">',
            "unquoted href": '<a href=/missing-c>x</a>',
            "protocol-relative": '<a href="//HOST/missing-d">x</a>',
        }
        for label, markup in cases.items():
            with self.subTest(label):
                page = ('<html><head><title>A page</title><link rel="canonical" href="https://ocom.uno/a">'
                        '</head><body>%s</body></html>' % markup.replace("HOST", "ocom.uno"))
                code, out = self.hunt(hunt_files(**{"/a": ("text/html; charset=utf-8", page)}))
                self.assertNotEqual(code, 0, out)
                self.assertIn("missing", out)


class PublicationHealth(unittest.TestCase):
    """Every case runs against the in-memory fixture; none of them touches the real site."""

    def healthy(self, site):
        """Publish the records the tool computes, and the pages that render them, until the fixture
        is consistent with itself. One pass is not enough since the tool compares a rendering with
        its record: publishing the record changes what the next recomputation sees, exactly as a
        deploy does on the real site."""
        last = ""
        for _ in range(4):
            out = tempfile.mkdtemp(prefix="ocom-health-")
            code, last = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--write", out)
            health = json.loads((pathlib.Path(out) / "observatory" / "health.json").read_text(encoding="utf-8"))
            pub = json.loads((pathlib.Path(out) / "observatory" / "publication-health.json").read_text(encoding="utf-8"))
            site.publish(health, pub)
            shutil.rmtree(out, ignore_errors=True)
            if code == 0:
                return health, pub
        self.fail("the fixture never became self-consistent: %s" % last)
        return health, pub

    def settle(self, site, rounds=4):
        """Publish what the tool computes until the fixture stops moving, without requiring the run
        to pass: a site whose figures breach a published threshold never returns 0 and still has to
        reach the fixed point a deploy reaches."""
        health = pub = None
        for _ in range(rounds):
            out = tempfile.mkdtemp(prefix="ocom-health-")
            run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--write", out)
            health = json.loads((pathlib.Path(out) / "observatory" / "health.json").read_text(encoding="utf-8"))
            pub = json.loads((pathlib.Path(out) / "observatory" / "publication-health.json").read_text(encoding="utf-8"))
            site.publish(health, pub)
            shutil.rmtree(out, ignore_errors=True)
        return health, pub

    def test_a_projection_that_is_another_document_fails_its_row(self):
        """Round 4: the presence rows asked for a 200 and never looked at the body, so swapping a
        term's Markdown projection, JSON record or JSON-LD alternate for a different document left
        every row ok and the projection-coverage figure at 100."""
        cases = {"markdown": ("/vocabulary/object.md", "text/markdown; charset=utf-8", "<html><body>not markdown</body></html>"),
                 "json": ("/vocabulary/object.json", "application/json", "not json at all"),
                 "jsonld": ("/vocabulary/object.jsonld", "application/json", '{"no": "context"}'),
                 "html": ("/vocabulary/object", "text/html; charset=utf-8", '{"json":"where a page should be"}')}
        for label, (path, ctype, body) in cases.items():
            with self.subTest(label), fake_site.Fixture() as site:
                self.healthy(site)
                site.files[path] = (ctype, body)
                code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
                self.assertNotEqual(code, 0, out)
                self.assertIn(path, out)

    def test_a_figure_that_breaches_its_published_threshold_fails_the_check(self):
        """Round 3 of the all-packages test: the record publishes thresholds for its figures and
        nothing ever compared a figure with one. Because the same tool writes the record, a deploy
        republished the breached numbers and the next run found perfect agreement."""
        with fake_site.Fixture() as site:
            self.healthy(site)
            graph = json.loads(site.files["/graph.jsonld"][1])
            graph["@graph"].append(dict(graph["@graph"][0]))      # one @id carried by two nodes
            site.files["/graph.jsonld"] = ("application/json", json.dumps(graph))
            self.settle(site)
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("differ in 0 place(s)", out)            # the record agrees with itself
            self.assertIn("duplicateIdentities is 1", out)        # and the figure still breaches
            self.assertIn("1 figure(s) breach a published threshold", out)

    def test_a_record_that_holds_its_figures_to_nothing_is_reported(self):
        with fake_site.Fixture() as site:
            health, pub = self.healthy(site)
            for label, notes in (("no thresholds", {}), ("a threshold this tool cannot read", {"mutualPairs": 3})):
                with self.subTest(label):
                    health["notes"]["thresholds"] = notes
                    if not notes:
                        health["notes"].pop("thresholds")
                    site.publish(health, pub)
                    code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
                    self.assertNotEqual(code, 0, out)
                    self.assertIn("thresholds" if not notes else "which way it points", out)

    def test_a_resolve_page_the_tool_cannot_read_a_count_from_fails_its_row(self):
        """Round 3: the leg counted the comparison before making it, so a page printing no number in
        the shape it reads was reported ok having compared nothing; and it tested set membership, so
        a page whose headline was wrong passed whenever another number beside the word matched."""
        with fake_site.Fixture() as site:
            self.healthy(site)
            entries = len(json.loads(site.files["/resolve.json"][1])["entries"])
            pages = {"no count": "<html><body><p>Identifiers: many</p></body></html>",
                     "wrong headline": "<html><body><p>Identifiers 3</p><p>Term identifiers %d</p></body></html>" % entries}
            for label, page in pages.items():
                with self.subTest(label):
                    site.files["/resolve"] = ("text/html; charset=utf-8", page)
                    code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
                    self.assertNotEqual(code, 0, out)
                    self.assertIn("Rendered figures match their records FAIL", out)

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

    def test_an_identifier_printed_as_a_pill_is_harvested(self):
        """The harvester matched three markup shapes and the site uses a fourth, so the HTML half of
        the printed-identifier row harvested nothing while the row reported ok."""
        with fake_site.Fixture() as site:
            self.healthy(site)
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--summary")
            self.assertEqual(code, 0, out)
            row = [l for l in out.splitlines() if l.startswith("Printed identifier coverage")][0]
            self.assertIn("ok", row)
            # the same fixture with one page printing an identifier nobody registered
            site.files["/vocabulary/object"] = (site.files["/vocabulary/object"][0],
                                                site.files["/vocabulary/object"][1].replace("OCOM-META-01", "OCOM-META-99"))
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--summary")
            row = [l for l in out.splitlines() if l.startswith("Printed identifier coverage")][0]
            self.assertIn("FAIL", row, out)
            self.assertIn("OCOM-META-99", row)

    def test_a_term_whose_projections_disagree_is_reported(self):
        """projection_parity published ok as a literal for the term projections, and under that tick
        one term's JSON record fell behind its HTML and Markdown twins."""
        with fake_site.Fixture() as site:
            self.healthy(site)          # records published while the projections agree
            site.files["/vocabulary/object.md"] = (site.files["/vocabulary/object.md"][0],
                                                   site.files["/vocabulary/object.md"][1]
                                                   .replace("Object is the thing this fixture defines.", "Object is something else entirely."))
            code, out = run(ROOT, HEALTH, "--base", site.base, "--pause", "0", "--today", "2026-09-18", "--check")
            self.assertNotEqual(code, 0, out)
            self.assertIn("projectionParity", out)

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

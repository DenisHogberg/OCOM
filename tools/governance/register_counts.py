#!/usr/bin/env python3
"""Check the documents that state how many Architecture Observations and ADR Candidates exist.

Three documents carry those counts, one of them the machine-facing `publication/llms.txt` the site
serves. All three said 82 and AO-083 for two days after the registers reached 92 and AO-093, and
nothing compared them. This tool does, and it fails when a file it is asked to check states no
range it can read: the check used to scan such a file, match nothing and treat it as agreeing,
which is the failure mode every checker in this repository is written against.

Standard library only, reads only this repository.

  register_counts.py --check    compare every file below against the registers

Each file is expected to state the registers listed beside it in STATING; a range it states
is compared whether or not it is required, and a required range it does not state is a failure.
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
AO = REPO / "docs/Governance/Architecture-Observations.md"
CANDIDATES = REPO / "docs/Governance/ADR-Candidates.md"
# the files that state the counts, and which registers each one is expected to state. The guard
# counted a readable range of either prefix, so a file stating the observations and not the
# candidates had its candidate count compared against nothing and the tool reported agreement.
STATING = {"README.md": ("AO", "CAND"),
           "publication/llms.txt": ("AO",),
           "docs/Governance/Evidence-Register.md": ("AO", "CAND")}
LABELS = {"AO": "Architecture Observation", "CAND": "ADR Candidate"}


def registers():
    """(count, last identifier) per register, read from the registers themselves."""
    out = {}
    for prefix, path in (("AO", AO), ("CAND", CANDIDATES)):
        ids = sorted(re.findall(r"(?m)^## (%s-\d+)" % prefix, path.read_text(encoding="utf-8")))
        if not ids:
            raise SystemExit("%s carries no %s entry, so there is nothing to compare against" % (path, prefix))
        out[prefix] = (len(ids), ids[-1])
    return out


def failures(facts, root=REPO, stating=STATING):
    """Every disagreement between a stating document and the registers."""
    out = []
    for name, required in sorted(stating.items()):
        path = pathlib.Path(root) / name
        if not path.exists():
            out.append("%s does not exist, so its counts were compared against nothing" % name)
            continue
        read = {prefix: 0 for prefix in LABELS}
        # the body only: a count written in a revision note is what the document said it did once,
        # not what it states now, and reading one let a table lose its row while the note that
        # recorded adding the row kept the check green
        body = re.split(r"(?m)^#{1,3} (?:Revision History|История ревизий)\s*$",
                        path.read_text(encoding="utf-8"))[0]
        for lineno, line in enumerate(body.splitlines(), 1):
            for prefix, label in LABELS.items():
                m = re.search(r"%s-001 to (%s-\d+)" % (prefix, prefix), line)
                if not m:
                    continue
                read[prefix] += 1
                count, last = facts[prefix]
                numbers = [int(n) for n in re.findall(r"(?<![\w-])(\d{1,4})(?![\w-])", line)]
                if m.group(1) != last:
                    out.append("%s:%d names %s as the last %s; the register holds %s"
                               % (name, lineno, m.group(1), label, last))
                if count not in numbers:
                    out.append("%s:%d states no count matching the %d %ss the register holds"
                               % (name, lineno, count, label))
        # counted across both prefixes, one readable range made the other count unexamined: a file
        # stating the observations and not the candidates reported zero disagreements
        for prefix, label in sorted(LABELS.items()):
            if prefix in required and not read[prefix]:
                out.append("%s states no %s range this tool can read (the wording it reads is "
                           "\"%s-001 to %s-093\"), so its %s count was compared against nothing"
                           % (name, label, prefix, prefix, label))
    return out


def main(argv):
    if len(argv) != 2 or argv[1] != "--check":
        print(__doc__)
        return 2
    facts = registers()
    bad = failures(facts)
    for line in bad:
        print("::error::%s" % line)
    print("registers: %d observations to %s, %d candidates to %s; %d disagreement(s)"
          % (facts["AO"] + facts["CAND"] + (len(bad),)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

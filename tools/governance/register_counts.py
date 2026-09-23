#!/usr/bin/env python3
"""Check the documents that state how many Architecture Observations and ADR Candidates exist.

Three documents carry those counts, one of them the machine-facing `publication/llms.txt` the site
serves. All three said 82 and AO-083 for two days after the registers reached 92 and AO-093, and
nothing compared them. This tool does, and it fails when a file it is asked to check states no
range it can read: the check used to scan such a file, match nothing and treat it as agreeing,
which is the failure mode every checker in this repository is written against.

Standard library only, reads only this repository.

  register_counts.py --check    compare every file below against the registers
"""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
AO = REPO / "docs/Governance/Architecture-Observations.md"
CANDIDATES = REPO / "docs/Governance/ADR-Candidates.md"
# the files that state the counts. Each must carry at least one line this tool can read.
STATING = ("README.md", "publication/llms.txt", "docs/Governance/Evidence-Register.md")
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
    for name in stating:
        path = pathlib.Path(root) / name
        if not path.exists():
            out.append("%s does not exist, so its counts were compared against nothing" % name)
            continue
        read = 0
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for prefix, label in LABELS.items():
                m = re.search(r"%s-001 to (%s-\d+)" % (prefix, prefix), line)
                if not m:
                    continue
                read += 1
                count, last = facts[prefix]
                numbers = [int(n) for n in re.findall(r"(?<![\w-])(\d{1,4})(?![\w-])", line)]
                if m.group(1) != last:
                    out.append("%s:%d names %s as the last %s; the register holds %s"
                               % (name, lineno, m.group(1), label, last))
                if count not in numbers:
                    out.append("%s:%d states no count matching the %d %ss the register holds"
                               % (name, lineno, count, label))
        if not read:
            out.append("%s states no register range this tool can read (the wording it reads is "
                       "\"AO-001 to AO-093\"), so its counts were compared against nothing" % name)
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

#!/usr/bin/env python3
"""Run the exact regression suite under normal, -O and -OO interpreters."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SUITE = ["-B", "-m", "unittest", "discover", "-s", "tests",
         "-p", "test_wp84_source_weight_cone_audit.py", "-v"]
MODES = (("normal", []), ("O", ["-O"]), ("OO", ["-OO"]))


def main():
    failures = []
    for label, flags in MODES:
        proc = subprocess.run([sys.executable, *flags, *SUITE], cwd=ROOT,
                              text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, check=False)
        log = proc.stdout
        (ROOT / "evidence" / f"WP84_SOURCE_WEIGHT_CONE_TESTS_{label.upper()}.log").write_text(
            log, encoding="utf-8")
        print(f"MODE {label}: exit={proc.returncode}")
        print(log, end="" if log.endswith("\n") else "\n")
        if proc.returncode:
            failures.append((label, proc.returncode))
    if failures:
        raise SystemExit("test mode failures: " + repr(failures))
    print("PASS: normal, -O and -OO")


if __name__ == "__main__":
    main()

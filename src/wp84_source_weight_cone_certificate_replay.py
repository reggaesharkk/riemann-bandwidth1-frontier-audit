#!/usr/bin/env python3
"""Replay the inherited outward-rounded fourth-order kernel certificate."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "src" / "wp84_r400_filtered_connected_kernel.py"
LOG = ROOT / "evidence" / "WP84_SOURCE_WEIGHT_CONE_KERNEL_CERTIFICATE.log"


def main():
    result = subprocess.run([sys.executable, "-B", str(TARGET), "--certificate"],
                            cwd=ROOT, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False)
    LOG.write_text(result.stdout, encoding="utf-8")
    print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.returncode:
        raise SystemExit(result.returncode)
    if "RESULT: ACTUAL_ROW_CUMULANT_SIGN_COUNTEREXAMPLE_CERTIFIED; WEIGHTED_DELTA400_OPEN" not in result.stdout:
        raise RuntimeError("inherited interval certificate status changed")


if __name__ == "__main__":
    main()

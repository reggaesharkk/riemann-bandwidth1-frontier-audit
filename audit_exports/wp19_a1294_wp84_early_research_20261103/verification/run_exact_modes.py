#!/usr/bin/env python3
"""Run the exact witness checker normally, with -O and with -OO."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    checker = root / "verification" / "verify_a12994_erratum.py"
    result_dir = root / "results"
    result_dir.mkdir(exist_ok=True)
    modes = [("normal", []), ("optimized", ["-O"]), ("optimize_docstrings", ["-OO"])]
    values = {}
    for label, flags in modes:
        command = [sys.executable, *flags, str(checker), "--root", str(root)]
        done = subprocess.run(command, check=False, capture_output=True, text=True)
        need(done.returncode == 0, f"{label} replay failed: {done.stderr}")
        parsed = json.loads(done.stdout)
        need(parsed["status"] == "PASS", f"{label} replay returned non-PASS")
        (result_dir / f"a12994_{label}.json").write_text(json.dumps(parsed, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        values[label] = parsed
    need(values["normal"] == values["optimized"] == values["optimize_docstrings"], "mode outputs differ")
    summary = {"status": "PASS", "modes": [x[0] for x in modes], "output_equal": True, "A12994": values["normal"]["margins"][6]}
    (result_dir / "a12994_mode_comparison.json").write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

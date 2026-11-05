from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
env = os.environ.copy()
env["PYTHONPATH"] = str(ROOT / "reference")
commands = [
    [sys.executable, "verify_archive_inputs.py"],
    [sys.executable, "verify_catalog_source.py"],
    [sys.executable, "verify_terminal18_provenance.py"],
    [sys.executable, "verify_vrk_claim_record.py"],
]
logs: list[str] = []
for optimization, flag in (("normal", None), ("-O", "-O"), ("-OO", "-OO")):
    logs.append(f"MODE={optimization}")
    for command in commands:
        actual = command[:1] + ([flag] if flag else []) + command[1:]
        result = subprocess.run(actual, cwd=ROOT, env=env, text=True, capture_output=True)
        logs.append("$ " + " ".join(actual))
        logs.append(result.stdout.rstrip())
        if result.stderr.strip():
            logs.append("STDERR:\n" + result.stderr.rstrip())
        logs.append(f"EXIT={result.returncode}")
        if result.returncode:
            (ROOT / "verification_tests.log").write_text("\n".join(logs) + "\n", encoding="utf-8")
            raise SystemExit(result.returncode)
(ROOT / "verification_tests.log").write_text("\n".join(logs) + "\n", encoding="utf-8")
print("PASS: all three evidence scripts passed under normal Python, -O, and -OO")

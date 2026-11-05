from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
small_files = {
    "failed_drafts/terminal18/Terminal18_chunked_failed.lean",
    "reference/previous_objects/Catalog18Lookup.lean",
    "leaf_data_summary.json",
    "Terminal18Compositional.lean",
    "Catalog18AllLookups.lean",
    "verify_catalog_source.py",
}
results: list[str] = []


def fixture(tmp: Path, name: str) -> Path:
    target = tmp / name
    for rel in small_files:
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, destination)
    return target


def expect_reject(name: str, cwd: Path, command: list[str]) -> None:
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if proc.returncode == 0:
        raise RuntimeError(f"mutation was accepted: {name}")
    diagnostic = proc.stderr.strip() or proc.stdout.strip()
    final_line = next((line.strip() for line in reversed(diagnostic.splitlines()) if line.strip()), "no diagnostic")
    results.append(f"PASS rejected {name}: exit={proc.returncode}; {final_line}")


with tempfile.TemporaryDirectory(prefix="a1294-prov-mutation-", dir=ROOT / "failed_drafts") as tmp_raw:
    tmp = Path(tmp_raw)
    # Change one source catalog declaration reference.
    d = fixture(tmp, "entry")
    lookup = d / "reference/previous_objects/Catalog18Lookup.lean"
    text = lookup.read_text(encoding="utf-8")
    changed = text.replace("refinementPiece3", "refinementPiece4", 1)
    if changed == text:
        raise RuntimeError("catalog entry mutation target not found")
    lookup.write_text(changed, encoding="utf-8")
    expect_reject("single catalog entry mutation", d, [sys.executable, "verify_catalog_source.py"])

    # Reorder independent summary records.
    d = fixture(tmp, "reorder")
    summary = d / "leaf_data_summary.json"
    obj = json.loads(summary.read_text(encoding="utf-8"))
    obj["catalog_declarations"][0], obj["catalog_declarations"][1] = obj["catalog_declarations"][1], obj["catalog_declarations"][0]
    summary.write_text(json.dumps(obj), encoding="utf-8")
    expect_reject("catalog record reorder", d, [sys.executable, "verify_catalog_source.py"])

    # Duplicate one declaration record.
    d = fixture(tmp, "duplicate")
    summary = d / "leaf_data_summary.json"
    obj = json.loads(summary.read_text(encoding="utf-8"))
    obj["catalog_declarations"][1] = obj["catalog_declarations"][0]
    summary.write_text(json.dumps(obj), encoding="utf-8")
    expect_reject("duplicate catalog entry", d, [sys.executable, "verify_catalog_source.py"])

    # Truncate the catalog stream.
    d = fixture(tmp, "truncated")
    summary = d / "leaf_data_summary.json"
    obj = json.loads(summary.read_text(encoding="utf-8"))
    obj["catalog_declarations"].pop()
    summary.write_text(json.dumps(obj), encoding="utf-8")
    expect_reject("truncated catalog stream", d, [sys.executable, "verify_catalog_source.py"])

    # Shift a generated index label, testing complete ordered lookup coverage.
    d = fixture(tmp, "index")
    lookups = d / "Catalog18AllLookups.lean"
    text = lookups.read_text(encoding="utf-8")
    lookups.write_text(text.replace("theorem blocked_lookup_0 :", "theorem blocked_lookup_171 :", 1), encoding="utf-8")
    expect_reject("shifted lookup index", d, [sys.executable, "verify_catalog_source.py"])

    # Alter one byte of the frozen V2 ZIP and demand the original pinned hash.
    d = tmp / "sourcehash"
    archive = d / "reference/input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    archive.parent.mkdir(parents=True)
    raw = (ROOT / "reference/input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip").read_bytes()
    archive.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])
    shutil.copyfile(ROOT / "verify_archive_inputs.py", d / "verify_archive_inputs.py")
    expect_reject("mismatched frozen source SHA-256", d, [sys.executable, "verify_archive_inputs.py"])

print("\n".join(results))

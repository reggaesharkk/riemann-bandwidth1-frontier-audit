#!/usr/bin/env python3
"""Fresh-extract the final audit ZIP and replay its offline verification scripts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    # Keep the extraction root shallow so nested evidence paths stay below the
    # legacy Win32 MAX_PATH boundary on Windows hosts.
    parser.add_argument("--scratch", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    archive = args.archive.resolve()
    with zipfile.ZipFile(archive) as zf:
        if zf.testzip() is not None:
            raise RuntimeError("outer ZIP CRC failure")
        for name in zf.namelist():
            path = Path(name)
            if path.is_absolute() or ".." in path.parts:
                raise RuntimeError(f"unsafe outer ZIP member: {name}")
        with tempfile.TemporaryDirectory(prefix="outer-packet-", dir=args.scratch.resolve()) as temporary:
            zf.extractall(temporary)
            extracted = Path(temporary)
            for script in ("verify_manifest.py", "verify_packet.py"):
                subprocess.run([sys.executable, str(extracted / "verification" / script), "--root", str(extracted)], check=True)
            output = extracted / "verification" / "outer_witness_result.json"
            subprocess.run([sys.executable, str(extracted / "verification" / "verify_exact_witness.py"), "--root", str(extracted), "--output", str(output)], check=True, stdout=subprocess.DEVNULL)
            witness = json.loads(output.read_text(encoding="utf-8"))
            expected = "1739674247820415045342527228267900485813207074499/134217728000000000000000000000000000000000000000000"
            if witness["value_exact"] != expected:
                raise RuntimeError("fresh-extracted exact witness replay mismatch")
    print(json.dumps({"outer_zip_crc": "PASS", "fresh_extraction": "PASS", "manifest": "PASS", "v2_package_integrity": "PASS", "exact_witness_replay": "PASS", "value_exact": expected}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

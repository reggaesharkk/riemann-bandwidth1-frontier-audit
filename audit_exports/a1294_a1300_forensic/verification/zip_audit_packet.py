#!/usr/bin/env python3
"""Create the offline packet ZIP after validating its SHA256SUMS manifest."""

from __future__ import annotations

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    if root == output or root in output.parents:
        raise RuntimeError("ZIP output must be outside the packet directory")
    subprocess.run([sys.executable, str(root / "verification" / "verify_manifest.py"), "--root", str(root)], check=True)
    files = sorted(p for p in root.rglob("*") if p.is_file())
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in files:
            archive.write(path, path.relative_to(root).as_posix())
    print(f"wrote {output} with {len(files)} files")


if __name__ == "__main__":
    main()

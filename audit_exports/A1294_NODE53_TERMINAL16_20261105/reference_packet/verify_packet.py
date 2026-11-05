"""Independently extract and verify the A1294 node-55 evidence ZIP."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python verify_packet.py PACKET.zip")
    archive = Path(sys.argv[1]).resolve()
    with zipfile.ZipFile(archive) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"CRC failure: {bad}")
        names = set(zf.namelist())
        if any(PurePosixPath(n).is_absolute() or ".." in PurePosixPath(n).parts for n in names):
            raise SystemExit("unsafe archive path")
        with tempfile.TemporaryDirectory(prefix="a1294-node55-independent-extract-", dir=archive.parent) as tmp:
            root = Path(tmp)
            zf.extractall(root)
            manifest = root / "SHA256SUMS.txt"
            expected = {}
            for line in manifest.read_text(encoding="utf-8").splitlines():
                digest, rel = line.split("  ", 1)
                expected[rel] = digest
            actual_files = {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file()}
            if set(expected) != set(actual_files) - {"SHA256SUMS.txt"}:
                raise SystemExit("manifest file-set mismatch")
            for rel, p in actual_files.items():
                if rel == "SHA256SUMS.txt":
                    continue
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                if digest != expected[rel]:
                    raise SystemExit(f"SHA-256 mismatch: {rel}")
            print(f"MANIFEST_SHA256=PASS files={len(expected)}")
            proof_obj = root / "Node55Replay.olean"
            terminal_obj = root / "Terminal17Compositional.olean"
            for p in (proof_obj, terminal_obj):
                if not p.is_file() or p.stat().st_size == 0:
                    raise SystemExit(f"missing Lean object: {p.name}")
            proc = subprocess.run(
                [sys.executable, str(root / "verify_terminal17_reconstruction.py")],
                cwd=root, check=False, text=True, capture_output=True)
            print(proc.stdout, end="")
            if proc.returncode:
                print(proc.stderr, file=sys.stderr, end="")
                raise SystemExit(f"source reconstruction checker exit={proc.returncode}")
            print("INDEPENDENT_EXTRACTION=PASS")


if __name__ == "__main__":
    main()

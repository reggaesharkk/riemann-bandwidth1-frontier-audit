from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_NAME = "MANIFEST_SHA256.txt"
EXCLUDED_PARTS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".lake", "build", "dist"}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_zip", type=Path)
    args = parser.parse_args()
    output = args.output_zip.resolve()
    require_outside = output != ROOT and ROOT not in output.parents
    if not require_outside:
        raise SystemExit("output ZIP must be outside the manifested packet directory")
    manifest = ROOT / MANIFEST_NAME
    if not manifest.is_file():
        raise SystemExit("packet manifest missing")
    expected = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split(None, 1)
        key = rel.strip()
        if key in expected:
            raise SystemExit(f"duplicate manifest entry {key}")
        expected[key] = digest
    paths = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == manifest:
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS or part.endswith(".egg-info") for part in rel.parts):
            continue
        key = rel.as_posix()
        if key not in expected:
            raise SystemExit(f"unlisted packet file: {key}")
        if sha(path) != expected[key]:
            raise SystemExit(f"manifest mismatch before packing: {key}")
        paths.append((path, key))
    if set(expected) != {key for _, key in paths}:
        raise SystemExit("manifest entries do not match packet files")
    paths.append((manifest, MANIFEST_NAME))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", allowZip64=True) as archive:
        for path, rel in paths:
            compression = zipfile.ZIP_STORED if path.suffix.lower() == ".zip" else zipfile.ZIP_DEFLATED
            level = None if compression == zipfile.ZIP_STORED else 1
            archive.write(path, rel, compress_type=compression, compresslevel=level)
    print(f"PACKET_ZIP={output}")
    print(f"FILES={len(paths)}")
    print(f"BYTES={output.stat().st_size}")
    print(f"SHA256={sha(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

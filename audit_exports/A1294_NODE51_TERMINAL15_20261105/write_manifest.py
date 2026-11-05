from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST_SHA256.txt"
EXCLUDED_PARTS = {"__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".lake", "build", "dist"}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    rows = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST:
            continue
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS or part.endswith(".egg-info") for part in relative.parts):
            continue
        digest = sha(path)
        rows.append(f"{digest}  {relative.as_posix()}")
    MANIFEST.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"WROTE_MANIFEST entries={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

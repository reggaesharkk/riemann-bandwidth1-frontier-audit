from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def main() -> None:
    manifest = ROOT / "SHA256SUMS.txt"
    expected: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        path = PurePosixPath(rel)
        require(not path.is_absolute() and ".." not in path.parts, f"unsafe manifest path: {rel}")
        require(rel not in expected, f"duplicate manifest path: {rel}")
        expected[rel] = digest
    actual = {
        p.relative_to(ROOT).as_posix(): p
        for p in ROOT.rglob("*")
        if p.is_file() and p != manifest
    }
    require(set(expected) == set(actual), "manifest file-set mismatch")
    for rel, path in actual.items():
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        require(got == expected[rel], f"SHA-256 mismatch: {rel}")
    decisions = json.loads((ROOT / "DECISIONS.json").read_text(encoding="utf-8"))
    inputs = ROOT / "reference_inputs"
    node55 = inputs / "A1294_NODE55_TERMINAL17_PROOF_PACKET_20261105.zip"
    v2 = inputs / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    require(hashlib.sha256(node55.read_bytes()).hexdigest() == decisions["input_packet_sha256"], "node55 packet hash mismatch")
    require(hashlib.sha256(v2.read_bytes()).hexdigest() == decisions["frozen_v2_sha256"], "V2 archive hash mismatch")
    require((ROOT / "Node53Replay.olean").stat().st_size > 0, "missing Node53Replay.olean")
    require((ROOT / "Terminal16Compositional.olean").stat().st_size > 0, "missing Terminal16Compositional.olean")
    print(f"EVIDENCE_MANIFEST=PASS files={len(expected)}")
    print("PREDECESSOR_INPUTS=PASS; COMPILED_OBJECTS=PASS")

if __name__ == "__main__":
    main()

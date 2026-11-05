from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath


def require(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit(message)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_manifest(root: Path) -> int:
    manifest = root / "MANIFEST_SHA256.txt"
    require(manifest.is_file(), "packet manifest missing")
    entries = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split(None, 1)
        key = rel.strip()
        require(key not in entries, f"duplicate manifest entry: {key}")
        entries[key] = digest
    actual = set()
    for path in root.rglob("*"):
        if not path.is_file() or "__pycache__" in path.relative_to(root).parts:
            continue
        rel = path.relative_to(root).as_posix()
        if rel == "MANIFEST_SHA256.txt":
            continue
        actual.add(rel)
        require(rel in entries, f"unlisted extracted file: {rel}")
        require(sha(path) == entries[rel], f"manifest mismatch: {rel}")
    require(actual == set(entries), f"manifest coverage mismatch: {len(actual)} actual / {len(entries)} listed")
    return len(entries)


def safe_extract(archive: Path, destination: Path) -> None:
    require(not destination.exists(), f"fresh extraction target already exists: {destination}")
    destination.mkdir(parents=True)
    with zipfile.ZipFile(archive) as zf:
        bad = zf.testzip()
        require(bad is None, f"CRC error in {archive.name}: {bad}")
        for info in zf.infolist():
            name = PurePosixPath(info.filename)
            require(not name.is_absolute() and ".." not in name.parts,
                    f"unsafe archive path: {info.filename}")
        zf.extractall(destination)


def run(command: list[str], log: Path) -> None:
    result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(result.stdout + f"\nEXIT={result.returncode}\n", encoding="utf-8")
    require(result.returncode == 0, f"command failed ({result.returncode}): {' '.join(command)}; see {log}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("packet_zip", type=Path)
    parser.add_argument("fresh_dir", type=Path)
    args = parser.parse_args()
    archive = args.packet_zip.resolve()
    fresh = args.fresh_dir.resolve()
    require(archive.is_file(), f"packet ZIP missing: {archive}")
    safe_extract(archive, fresh)
    entries = check_manifest(fresh)
    task = fresh
    v2_zip = task / "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    v2_dir = fresh.parent / (fresh.name + "_v2_sources")
    safe_extract(v2_zip, v2_dir)
    v2_root = v2_dir / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2"
    py = sys.executable
    verifier = task / "verify15_reconstruction.py"
    for flag, name in [(None, "normal"), ("-O", "O"), ("-OO", "OO")]:
        cmd = [py] + ([flag] if flag else []) + [str(verifier), str(v2_root), str(v2_zip),
               str(task / "terminal15_authentic_input.json")]
        run(cmd, fresh.parent / f"{fresh.name}_source_replay_{name}.log")
    vrk_verifier = task / "verify_node51_vrk_record.py"
    for flag, name in [(None, "normal"), ("-O", "O"), ("-OO", "OO")]:
        cmd = [py] + ([flag] if flag else []) + [str(vrk_verifier)]
        run(cmd, fresh.parent / f"{fresh.name}_vrk_{name}.log")
    for flag, name in [(None, "normal"), ("-O", "O"), ("-OO", "OO")]:
        protocol = task / "protocol/verify_candidate_manifest.py"
        cmd = [py] + ([flag] if flag else []) + [str(protocol)]
        run(cmd, fresh.parent / f"{fresh.name}_protocol_manifest_{name}.log")
    v4_zip = task / "reference_inputs/A1294_NODE53_TERMINAL16_PROOF_PACKET_V4_20261105.zip"
    require(sha(v4_zip) == "a0b58ec6b7241f88b0bb3b223c7944fbdc0d7922fcd8f049f040d61b642d3b13",
            "V4 predecessor ZIP hash mismatch")
    require((task / "Node51Replay.generated.lean").read_bytes() == (task / "Node51Replay.lean").read_bytes(),
            "generated replay source does not equal the compiled theorem source")
    require((task / "Node51Replay.olean").is_file() and (task / "Terminal15Compositional.olean").is_file(),
            "successful Lean proof object missing")
    print(f"PASS fresh extraction, CRC, {entries} SHA-256 manifest entries, Python normal/-O/-OO replays, VRK and IntentSeal manifest checks")
    print("PASS V4 input identity, generated-source equality, and included Lean proof objects")
    print("NOTE: this integrity replay does not rebuild Lean or kernel-check an omitted theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

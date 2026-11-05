"""Build the additive A1294 node-55/terminal-17 evidence packet."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "A1294_NODE55_TERMINAL17_PROOF_PACKET_20261105.zip"
PRED_NAME = "A1294_CATALOG18_IDENTITY_TERMINAL18_NODE57_20261105.zip"
PRED = ROOT / "reference" / PRED_NAME
V2 = (ROOT / "reference" / "predecessor" / "A1294_CATALOG18_IDENTITY_20261105"
      / "reference" / "input" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip")
V2_TREE = ROOT / "reference" / "v2_source" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def copy_tree(src: Path, dst: Path) -> None:
    for p in src.rglob("*"):
        if not p.is_file() or "__pycache__" in p.parts:
            continue
        target = dst / p.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)


def main() -> None:
    expected = {
        PRED_NAME: "1b2648fc7734f63a096623350e1290bae67fa6ad8b20241147d869e672674fcb",
        V2.name: "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5",
    }
    for path, digest in ((PRED, expected[PRED_NAME]), (V2, expected[V2.name])):
        if not path.is_file() or sha(path.read_bytes()) != digest:
            raise SystemExit(f"source archive absent or hash mismatch: {path}")
    if not V2_TREE.is_dir():
        raise SystemExit(f"extracted V2 source tree absent: {V2_TREE}")

    # Stage only inside the writable audit worktree; the host temp root is sandboxed.
    with tempfile.TemporaryDirectory(prefix="a1294-node55-packet-", dir=ROOT) as tmp:
        stage = Path(tmp)
        # New audit deliverables and all retained failed drafts/logs/objects.
        for p in ROOT.iterdir():
            if p.is_file():
                shutil.copy2(p, stage / p.name)
        # Preserve the original predecessor and V2 archive bytes as inputs.
        ref = stage / "reference"
        ref.mkdir()
        shutil.copy2(PRED, ref / PRED_NAME)
        embedded = ref / "predecessor" / "A1294_CATALOG18_IDENTITY_20261105" / "reference" / "input"
        embedded.mkdir(parents=True)
        shutil.copy2(V2, embedded / V2.name)
        # The verifier consumes this extracted tree; the V2 archive is also retained above.
        copy_tree(V2_TREE, ref / "v2_source" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2")

        file_rows = []
        for p in sorted(x for x in stage.rglob("*") if x.is_file()):
            rel = p.relative_to(stage).as_posix()
            if rel == "SHA256SUMS.txt":
                continue
            raw = p.read_bytes()
            file_rows.append({"path": rel, "bytes": len(raw), "sha256": sha(raw)})
        source_inventory = {
            "format": "A1294 source and compiled-artifact hash inventory v1",
            "frozen_predecessor_archive": {"path": f"reference/{PRED_NAME}",
                "bytes": PRED.stat().st_size, "sha256": expected[PRED_NAME]},
            "frozen_v2_archive": {"path": f"reference/predecessor/A1294_CATALOG18_IDENTITY_20261105/reference/input/{V2.name}",
                "bytes": V2.stat().st_size, "sha256": expected[V2.name]},
            "source_stream_sha256": {
                "topology": "9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76",
                "terminal_kinds": "859e25cdff7379072a3928347b66dfbe762ff83c98035b0e3b591e9b533f06",
                "anchors": "32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5"
            },
            "catalog_sha256": {
                "stable": "961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b",
                "refinement_v1": "3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9",
                "refinement_v3": "7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d"
            },
            "toolchain": {
                "formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
                "lean_toolchain": "leanprover/lean4:v4.33.0-rc2",
                "lean_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
                "lake": "5.0.0-src+d8b1897",
                "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
                "lake_manifest_sha256": "1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448"
            },
            "packet_files": file_rows
        }
        (stage / "SOURCE_HASH_INVENTORY.json").write_text(
            json.dumps(source_inventory, indent=2) + "\n", encoding="utf-8")

        rows = []
        for p in sorted(x for x in stage.rglob("*") if x.is_file() and x.relative_to(stage).as_posix() != "SHA256SUMS.txt"):
            rows.append(f"{sha(p.read_bytes())}  {p.relative_to(stage).as_posix()}")
        (stage / "SHA256SUMS.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")

        OUT.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
            for p in sorted(x for x in stage.rglob("*") if x.is_file()):
                zf.write(p, p.relative_to(stage).as_posix())
    raw = OUT.read_bytes()
    print(f"PACKET={OUT}")
    print(f"PACKET_BYTES={len(raw)}")
    print(f"PACKET_SHA256={sha(raw)}")
    with zipfile.ZipFile(OUT) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC failure: {bad}")
        print(f"PACKET_FILES={len(zf.infolist())}")
        print("ZIP_CRC=PASS")


if __name__ == "__main__":
    main()

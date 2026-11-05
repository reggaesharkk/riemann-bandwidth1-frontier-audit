#!/usr/bin/env python3
"""Independent integrity and exact-data checks for the quadratic-leaf packet.

This verifier checks reproducibility artifacts. It does not replace Lean's
kernel check and does not parse or prove the full serialized certificate.
"""
from __future__ import annotations

import hashlib
import json
import bisect
import re
import sys
import zipfile
from fractions import Fraction
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("FAIL: " + message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_quadratic_leaf_evidence.py <packet-root>")
    root = Path(sys.argv[1]).resolve()

    sums_path = root / "SHA256SUMS.txt"
    require(sums_path.is_file(), "SHA256SUMS.txt exists")
    expected_hashes = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        expected_hashes[rel.replace("\\", "/")] = digest.lower()
    actual_files = {
        p.relative_to(root).as_posix(): p
        for p in root.rglob("*")
        if p.is_file() and p != sums_path
    }
    require(set(expected_hashes) == set(actual_files), "manifest file set")
    for rel, path in actual_files.items():
        require(sha(path) == expected_hashes[rel], f"manifest SHA-256: {rel}")

    v2 = root / "source" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    prior = root / "source" / "A1294_LEAN_KERNEL_PILOT_PACKET_20261104.zip"
    require(sha(v2) == "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5",
            "frozen V2 ZIP SHA-256")
    require(sha(prior) == "2e1284945636ce6de55b21ab686ae0835d4400e40b830c3226a304907311e949",
            "predecessor pilot ZIP SHA-256")

    with zipfile.ZipFile(v2) as zf:
        require(zf.testzip() is None, "V2 ZIP CRC")
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        package_manifest = json.loads(zf.read(prefix + "PACKAGE_MANIFEST.json"))
        declared_files = package_manifest["files"]
        archive_files = {
            name[len(prefix):]: info
            for name, info in ((info.filename, info) for info in zf.infolist())
            if name.startswith(prefix) and not name.endswith("/")
            and name != prefix + "PACKAGE_MANIFEST.json"
        }
        require(set(declared_files) == set(archive_files), "V2 package manifest file set")
        for rel, entry in declared_files.items():
            data = zf.read(prefix + rel)
            require(len(data) == entry["bytes"], f"V2 entry size: {rel}")
            require(hashlib.sha256(data).hexdigest() == entry["sha256"],
                    f"V2 entry SHA-256: {rel}")
        manifest = json.loads(zf.read(prefix + "certificate/manifest.json"))
        source_catalogs = [
            json.loads(zf.read(prefix + member))["pieces"]
            for member in (
                "data/macro-data-exact.json",
                "data/refinement-catalog-v1-exact.json",
                "data/refinement-catalog-v3.json",
            )
        ]
        for name, member in {
            "stable": "data/macro-data-exact.json",
            "v1": "data/refinement-catalog-v1-exact.json",
            "v3": "data/refinement-catalog-v3.json",
        }.items():
            got = hashlib.sha256(zf.read(prefix + member)).hexdigest()
            require(got == manifest["input_sha256"][name], f"V2 catalog hash: {name}")
        for name, member in {
            "topology": "certificate/topology-u8.bin",
            "kinds": "certificate/terminal-kinds-u8.bin",
            "anchors": "certificate/anchors-u16le.bin",
        }.items():
            got = hashlib.sha256(zf.read(prefix + member)).hexdigest()
            require(got == manifest["stream_sha256"][name], f"V2 stream hash: {name}")
    with zipfile.ZipFile(prior) as zf:
        require(zf.testzip() is None, "predecessor pilot ZIP CRC")

    reports = root / "reports"
    ledgers = [read_json(reports / f"ledger_{mode}.json") for mode in ("normal", "O", "OO")]
    require(ledgers[0] == ledgers[1] == ledgers[2], "ledger equality across Python modes")
    ledger = ledgers[0]
    require(ledger["status"] == "FIRST_QUADRATIC_SOURCE_LEAF_LEDGER_PASS", "ledger status")
    require(ledger["source_node_index_zero_based"] == 16, "source topology node")
    require(ledger["source_leaf_index_zero_based"] == 0, "source leaf index")
    require(ledger["source_terminal_kind"] == "quadratic", "terminal kind")
    require(len(ledger["root_path_axis_zero_based"]) == 16, "path length")
    require(ledger["root_path_sides"] == ["L"] * 16, "left-child path")
    tokens = ledger["source_topology_prefix_tokens"]
    axes = ledger["root_path_axis_zero_based"]
    require(tokens == [axis + 1 for axis in axes] + [0], "path tokens and axes")
    require(ledger["weighted_split_checks"] == 16, "weighted split count")
    require(ledger["source_box_exact"] == [["0", "15/2"], ["0", "15/2"],
            ["0", "15/4"], ["0", "15/2"], ["0", "15/2"]], "exact leaf box")
    require(ledger["anchor_codes_u16le"] == [0] * 5, "anchor codes")
    require(ledger["anchor_denominator"] == 16384, "anchor denominator")
    require(ledger["anchor_coordinates_exact"] == ["0"] * 5, "anchor coordinates")
    require(ledger["source_stream_sha256"] == manifest["stream_sha256"],
            "ledger source stream hashes")
    require(ledger["source_input_sha256"] == manifest["input_sha256"],
            "ledger source catalog hashes")
    prefix_data = read_json(reports / "source_prefix.json")
    require(prefix_data["source_node_index_zero_based"] == ledger["source_node_index_zero_based"],
            "prefix/ledger node consistency")
    require(prefix_data["source_topology_prefix_tokens"] == tokens,
            "prefix/ledger token consistency")
    require(prefix_data["root_box_exact"] == ledger["source_box_exact"],
            "prefix/ledger box consistency")

    terms = ledger["fifteen_models"]
    require(len(terms) == 15, "fifteen effective models")
    require(sum(len(t["catalog_segments"]) for t in terms) == 969, "segment ledger size")
    expected_lower = Fraction("14630385677/1000000000000")
    highs = [Fraction(piece["hi"]) for piece in source_catalogs[0]]
    raw_by_index = source_catalogs[0] + source_catalogs[1] + source_catalogs[2]
    for i, term in enumerate(terms):
        val = Fraction(term["effective_selected_constant_lower_model"])
        require(val == (expected_lower if i == 9 else 0), f"effective model value at pair {i}")
        require(term["selection_mode"] == "segmented", f"selection mode at pair {i}")
        require(len(term["catalog_segments"]) > 0, f"segment coverage at pair {i}")
        interval_lo, interval_hi = map(Fraction, term["distance_interval"])
        cursor = interval_lo
        segment_lowers = []
        for segment in term["catalog_segments"]:
            seg_lo, seg_hi = map(Fraction, segment["segment"])
            require(seg_lo == cursor and seg_hi >= seg_lo,
                    f"contiguous segment coverage at pair {i}")
            cursor = seg_hi
            idx = segment["catalog_index_zero_based"]
            require(0 <= idx < len(raw_by_index), f"catalog index at pair {i}")
            raw = raw_by_index[idx]
            require(segment["source_item"] == raw, f"catalog source item at pair {i}")
            canonical = json.dumps(raw, sort_keys=True, separators=(",", ":")).encode()
            require(hashlib.sha256(canonical).hexdigest() ==
                    segment["source_item_sha256_canonical_json"],
                    f"source item canonical hash at pair {i}")
            item_lo, item_hi = Fraction(raw["lo"]), Fraction(raw["hi"])
            require(item_lo <= seg_lo and seg_hi <= item_hi,
                    f"selected model applicable interval at pair {i}")
            owner = segment["owner_index"]
            require(isinstance(owner, int) and -1 <= owner < 56,
                    f"owner index range at pair {i}")
            expected_owner = idx if idx < 56 else int(raw["stable_piece_index"])
            require(owner == expected_owner, f"source owner field at pair {i}")
            stable_owner = min(bisect.bisect_left(highs, seg_lo), 55)
            allowed_owners = {stable_owner, max(0, stable_owner - 1), min(55, stable_owner + 1), -1}
            require(owner in allowed_owners, f"selector owner eligibility at pair {i}")
            segment_lowers.append(Fraction(segment["model_infimum_on_segment"]))
        require(cursor == interval_hi, f"segment interval endpoint at pair {i}")
        require(val == min(segment_lowers), f"segmented minimum at pair {i}")
        for segment in term["catalog_segments"]:
            active = Fraction(segment["model_infimum_on_segment"]) == val
            require(segment["active_minimizer"] is active,
                    f"active minimizer flag at pair {i}")
    require(ledger["fifteen_models"][9]["distance_interval"] == ["0", "15/4"],
            "positive term interval")
    require(Fraction(ledger["rank_tangent_lower"]) == expected_lower, "tangent lower value")
    require(Fraction(ledger["exact_positive_margin"]) ==
            Fraction("1690385677/1000000000000"), "exact positive margin")

    catalogs = [read_json(reports / f"catalog_{mode}.json") for mode in ("normal", "O", "OO")]
    require(catalogs[0] == catalogs[1] == catalogs[2], "catalog comparison equality across modes")
    for entry, expected_count in zip(catalogs[0], (56, 216, 394)):
        require(entry["json_count"] == expected_count, f"catalog JSON count: {entry['catalog']}")
        require(entry["lean_declaration_count"] == expected_count,
                f"catalog declaration count: {entry['catalog']}")
        require(entry["mismatch_count"] == 0, f"catalog field mismatch: {entry['catalog']}")

    lean = (root / "lean" / "A1294QuadraticLeaf.lean").read_text(encoding="utf-8")
    forbidden = re.search(r"\b(?:sorry|admit|native_decide|axiom)\b", lean)
    require(forbidden is None, f"forbidden proof escape in Lean source: {forbidden.group(0) if forbidden else ''}")
    build = (root / "logs" / "build_final_axioms.log").read_text(encoding="utf-8")
    require("Build completed successfully (8706 jobs)." in build, "successful final Lake build")
    require("Exit status: 0" in build, "successful build process exit")
    theorem_names = (
        "source_path_reconstructs_box", "source_anchor_is_lower_corner",
        "active_zero_source_piece_valid", "selected_pair9_model_valid",
        "selected_models_pairwise_valid", "selected_rank_tangent_lower",
        "selected_rank_tangent_check", "authentic_quadratic_leaf_box_predicate",
    )
    for name in theorem_names:
        require(name in build, f"axiom report contains {name}")
    require("[propext, Classical.choice, Quot.sound]" in build, "standard axiom transcript")
    require("sorryAx" not in build, "absence of sorryAx")

    print("QUADRATIC_LEAF_EVIDENCE=PASS")
    print("V2_ZIP_CRC_AND_SOURCE_HASHES=PASS")
    print("PYTHON_MODES=normal,-O,-OO exact ledger and catalog equality")
    print("LEAF=node16 kind=quadratic margin=1690385677/1000000000000")
    print("MODELS=15 effective; segments=969; catalog_counts=56,216,394")
    print("LEAN_BUILD=PASS; axioms=propext,Classical.choice,Quot.sound")
    print("SCOPE=single leaf; source-stream-to-Lean-path mapping remains external")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

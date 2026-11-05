#!/usr/bin/env python3
"""Independent exact checks on the bounded node-65 V2 source replay outputs."""
from __future__ import annotations
import hashlib, json, os, sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGS = Path(os.environ.get("A1294_REPLAY_LOG_DIR", str(HERE / "logs"))).resolve()
EXPECTED_ZIP = "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5"

def fail(msg: str) -> None:
    raise RuntimeError(msg)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(mode: str):
    return json.loads((LOGS / f"extract_{mode}.json").read_text(encoding="utf-8"))

def run() -> dict:
    modes = [read(x) for x in ("normal", "O", "OO")]
    if modes[0] != modes[1] or modes[1] != modes[2]:
        fail("normal/-O/-OO source replay outputs differ")
    d = modes[0]
    if d["status"] != "NODE65_QUADRATIC_QUADRATIC_SIBLING_SOURCE_REPLAY_PASS":
        fail("unexpected bounded replay status")
    if d["v2_zip_sha256"] != EXPECTED_ZIP:
        fail("V2 source ZIP hash mismatch")
    p, left, right = d["parent"], d["children"]["left"], d["children"]["right"]
    if [p["topology_node_zero_based"], left["topology_node_zero_based"],
        right["topology_node_zero_based"]] != [65, 66, 67]:
        fail("node indices differ from the requested sibling pair")
    if p["token"] != 1 or p["split_axis_zero_based"] != 0:
        fail("parent is not the source axis-0 midpoint split")
    if [left["terminal_index_zero_based"], right["terminal_index_zero_based"]] != [22, 23]:
        fail("terminal stream indices mismatch")
    if [left["terminal_kind_byte"], right["terminal_kind_byte"]] != [1, 1]:
        fail("both source terminal kinds are not quadratic")
    if left["path_axes_zero_based"] != p["path_axes_zero_based"] + [0]:
        fail("left source path is not the immediate lower child")
    if right["path_axes_zero_based"] != p["path_axes_zero_based"] + [0]:
        fail("right source path is not the immediate upper child")
    if left["path_sides"] != p["path_sides"] + ["L"]:
        fail("left source path side mismatch")
    if right["path_sides"] != p["path_sides"] + ["R"]:
        fail("right source path side mismatch")
    if len(p["path_axes_zero_based"]) != 43 or len(left["path_axes_zero_based"]) != 44:
        fail("source path depth mismatch")
    segment_count = 0
    positive_floor_count = 0
    model_counts = {}
    margins = {}
    for name, child in (("left", left), ("right", right)):
        if len(child["fifteen_models"]) != 15:
            fail(f"{name}: not exactly 15 rank models")
        A, B = F(child["A"]), F(child["B"])
        margin = F(child["rank_tangent_lower"]) - A
        if margin != F(child["exact_margin"]) or margin <= 0:
            fail(f"{name}: serialized exact tangent margin mismatch/nonpositive")
        margins[name] = str(margin)
        codes = child["anchor_codes_u16le"]
        if codes != [0] * 5 or child["anchor_denominator"] != 16384:
            fail(f"{name}: unexpected anchor encoding")
        if child["anchor_coordinates_exact"] != [row[0] for row in child["box_exact"]]:
            fail(f"{name}: source anchor not the lower corner")
        kinds = {}
        for term in child["fifteen_models"]:
            kind = term["kind"]
            kinds[kind] = kinds.get(kind, 0) + 1
            if F(term["base"]) < 0 or F(term["weight"]) < 0:
                fail(f"{name}: negative rank term coefficient")
            if kind == "segmented_constant":
                segs = term["segments"]
                if not segs:
                    if term["base"] != "0":
                        fail(f"{name}: nonzero segmented floor lacks source segments")
                    continue
                positive_floor_count += int(F(term["base"]) > 0)
                segment_count += len(segs)
                if F(segs[0]["segment"][0]) != F(term["distance_interval"][0]):
                    fail(f"{name}: first segment misses left interval endpoint")
                if F(segs[-1]["segment"][1]) != F(term["distance_interval"][1]):
                    fail(f"{name}: final segment misses right interval endpoint")
                for a, b in zip(segs, segs[1:]):
                    if F(a["segment"][1]) != F(b["segment"][0]):
                        fail(f"{name}: segment seam gap or overlap")
                for seg in segs:
                    if seg["declaration"] not in ("refinementPiece" + str(i) for i in range(1000)) and not seg["declaration"].startswith("macroPiece"):
                        fail(f"{name}: unexpected source piece declaration")
                    if F(seg["model_infimum"]) < F(term["base"]):
                        fail(f"{name}: source segment floor does not dominate the target constant")
            elif kind == "direct_piece":
                if term["direct_catalog_index"] != 11 or term["owner_index"] != 11:
                    fail(f"{name}: unexpected direct source model")
                if F(term["weight"]) <= 0:
                    fail(f"{name}: direct positive rank term has nonpositive weight")
            else:
                fail(f"{name}: unexpected model kind {kind}")
        model_counts[name] = kinds
        if child["A"] != "647/50000" or child["B"] != "1094977/5000000000":
            fail(f"{name}: threshold parameters mismatch")
    expected_hashes = {
        "topology": "9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76",
        "kinds": "859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06",
        "anchors": "32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5",
    }
    if d["source_stream_sha256"] != expected_hashes:
        fail("authenticated V2 stream hashes differ")
    if segment_count != 400 or positive_floor_count != 22:
        fail(f"segment/floor count mismatch: {segment_count}, {positive_floor_count}")
    return {
        "status": "PASS",
        "modes_equal": ["normal", "-O", "-OO"],
        "source_zip_sha256": EXPECTED_ZIP,
        "source_stream_sha256": d["source_stream_sha256"],
        "parent_and_children": [65, 66, 67],
        "terminal_indices": [22, 23],
        "terminal_kinds": ["quadratic", "quadratic"],
        "parent_path_depth": 43,
        "child_path_depth": 44,
        "parent_split_axis": 0,
        "models_each": 15,
        "segments_for_positive_floors": segment_count,
        "positive_floor_terms": positive_floor_count,
        "model_counts_by_child": model_counts,
        "exact_margins": margins,
        "extract_output_sha256": {m: sha(LOGS / f"extract_{m}.json") for m in ("normal", "O", "OO")},
        "scope": "source-authenticated bounded DFS through topology node 67; not full-tree replay",
    }

if __name__ == "__main__":
    result = run()
    target = LOGS / "verification_summary.json"
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import time
import zipfile
from fractions import Fraction
from pathlib import Path


EXPECTED_V2_SHA256 = "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5"
EXPECTED_NODE53_LEAN_SHA256 = "d3ab270499d165561d9345dac14404abcd2ad146be4051ea2a82501f9e121301"
EXPECTED_NODE53_OLEAN_SHA256 = "c047e8dfad8e1731ca814de4b61145f17adc48ebca75f3a7e224a77d6187f5e9"
EXPECTED_TOPOLOGY = [2, 0, 4, 0, 1, 0, 5, 0, 3, 0, 2, 0, 4, 0, 1, 0, 0]
EXPECTED_CODES = [0, 0, 0, 0, 0]
EXPECTED_PARENT = [
    ["195/32", "105/16"], ["195/32", "105/16"], ["195/32", "405/64"],
    ["195/32", "105/16"], ["195/32", "105/16"],
]
EXPECTED_LEAF = [
    ["195/32", "105/16"], ["195/32", "405/64"], ["195/32", "405/64"],
    ["195/32", "105/16"], ["195/32", "105/16"],
]
PAYLOAD_NAMES = [
    "payload15", "Node53.payload16", "Node55.payload17", "Node57.payload18",
    "Node59.payload19", "Node61.payload20", "Node63.payload21",
    "A1294Combined.leftPayload", "A1294Combined.rightPayload",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def q(value: str) -> Fraction:
    return Fraction(value)


def lean_token(token: int) -> str:
    require(0 <= token <= 5, f"invalid source token {token}")
    return ".terminal" if token == 0 else f".split {token - 1}"


def read_streams(v2_zip: Path) -> tuple[bytes, bytes, bytes]:
    blob = v2_zip.read_bytes()
    require(sha256(blob) == EXPECTED_V2_SHA256, "frozen V2 archive digest mismatch")
    with zipfile.ZipFile(v2_zip) as zf:
        require(zf.testzip() is None, "frozen V2 ZIP CRC failure")
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        manifest = json.loads(zf.read(prefix + "PACKAGE_MANIFEST.json"))
        paths = {
            "topology": "certificate/topology-u8.bin",
            "kinds": "certificate/terminal-kinds-u8.bin",
            "anchors": "certificate/anchors-u16le.bin",
        }
        result = {}
        for label, rel in paths.items():
            raw = zf.read(prefix + rel)
            meta = manifest["files"][rel]
            require(len(raw) == meta["bytes"] and sha256(raw) == meta["sha256"],
                    f"V2 package manifest mismatch for {label}")
            result[label] = raw
    return result["topology"], result["kinds"], result["anchors"]


def main() -> int:
    start = time.perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--v2-zip", type=Path, required=True)
    parser.add_argument("--child-lean", type=Path, required=True)
    parser.add_argument("--child-olean", type=Path, required=True)
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--compared-proof", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    record = json.loads(args.input.read_text(encoding="utf-8-sig"))
    parent = record["parent"]
    leaf = record["children"]["left"]
    require(record["v2_zip_sha256"] == EXPECTED_V2_SHA256, "input names another V2 archive")
    require(parent["topology_node_zero_based"] == 51 and parent["split_axis_zero_based"] == 1,
            "terminal-15 parent is not source node 51 / axis 1")
    require(parent["left_child_node"] == 52 and parent["right_child_node"] == 53,
            "node-51 child locations mismatch")
    require(parent["box_exact"] == EXPECTED_PARENT and leaf["box_exact"] == EXPECTED_LEAF,
            "source-derived parent/leaf box mismatch")
    require(leaf["topology_node_zero_based"] == 52 and leaf["terminal_index_zero_based"] == 15,
            "terminal-15 location mismatch")
    require(leaf["terminal_kind_byte"] == 1 and leaf["anchor_codes_u16le"] == EXPECTED_CODES,
            "terminal-15 kind or serialized anchor mismatch")
    require(len(leaf["fifteen_models"]) == 15, "expected fifteen selected models")
    require(sum(len(row["segments"]) for row in leaf["fifteen_models"]) == 369,
            "segment occurrence count mismatch")
    require(q(leaf["exact_margin"]) > 0, "exact tangent margin is not positive")

    topology, kinds, anchors = read_streams(args.v2_zip)
    require(list(topology[51:68]) == EXPECTED_TOPOLOGY, "frozen topology slice mismatch")
    require(kinds[15] == 1 and list(kinds[15:24]) == [1] * 9,
            "frozen terminal kinds 15..23 mismatch")
    anchor_offset = 10 * sum(kind == 1 for kind in kinds[:15])
    require(anchor_offset == 150, "terminal-15 anchor ordinal/byte offset mismatch")
    codes = list(struct.unpack_from("<5H", anchors, anchor_offset))
    require(codes == EXPECTED_CODES, "terminal-15 anchor bytes mismatch")

    child_text = args.child_lean.read_text(encoding="utf-8")
    require(sha256(child_text.encode("utf-8")) == EXPECTED_NODE53_LEAN_SHA256,
            "node53 Lean source does not match the preserved V4 object manifest")
    require("theorem replay53 :" in child_text and "theorem exact_exhaustion :" in child_text,
            "child source lacks checked replay/exhaustion declarations")
    child_match = re.search(
        r"def topology : CursorStream AffineTreeToken := CursorStream\.ofList\s*\[(.*?)\]\s*def payloads",
        child_text, re.S,
    )
    require(child_match is not None, "cannot parse the already proved node53 token stream")
    child_tokens = [
        ".terminal" if term == "terminal" else f".split {term}"
        for term in re.findall(r"\.split\s+(\d+)|\.terminal", child_match.group(1))
        for term in [term or "terminal"]
    ]
    source_child_tokens = [lean_token(token) for token in EXPECTED_TOPOLOGY[2:]]
    require(child_tokens == source_child_tokens, "Node53 topology differs from the frozen source suffix")
    require(args.child_olean.is_file() and args.child_olean.stat().st_size > 0,
            "compiled node53 theorem object missing")
    require(sha256(args.child_olean.read_bytes()) == EXPECTED_NODE53_OLEAN_SHA256,
            "node53 proof object does not match the preserved V4 object manifest")

    topology_tokens = [lean_token(token) for token in EXPECTED_TOPOLOGY]
    topology_def = (
        "def topology : CursorStream AffineTreeToken := CursorStream.ofList\n  ["
        + ", ".join(topology_tokens[:8]) + ",\n   "
        + ", ".join(topology_tokens[8:16]) + ",\n   "
        + topology_tokens[16] + "]"
    )
    payload_terms = [f".quadratic {name}" for name in PAYLOAD_NAMES]
    payload_def = (
        "def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList\n  ["
        + ", ".join(payload_terms[:3]) + ",\n   "
        + ", ".join(payload_terms[3:6]) + ",\n   "
        + ", ".join(payload_terms[6:8]) + ",\n   "
        + payload_terms[8] + "]"
    )
    template = args.template.read_text(encoding="utf-8")
    require(template.count("@@TOPOLOGY_DEF@@") == 1 and template.count("@@PAYLOAD_DEF@@") == 1,
            "template markers missing or duplicated")
    generated = template.replace("@@TOPOLOGY_DEF@@", topology_def).replace("@@PAYLOAD_DEF@@", payload_def)
    args.output.write_text(generated, encoding="utf-8", newline="\n")
    compared = args.compared_proof.read_text(encoding="utf-8")
    require(generated == compared, "generated replay source differs from the kernel-built proof source")
    print("PASS source-bound two-child replay generation")
    print("topology_tokens=17 payloads=9 child=Node53.replay53(15,8) plus terminal15")
    print("terminal15_rows=15 segment_occurrences=369 anchor_offset=150 exact_margin_positive=true")
    print(f"generated_sha256={sha256(generated.encode('utf-8'))}")
    print(f"node53_lean_sha256={sha256(child_text.encode('utf-8'))}")
    print(f"node53_olean_bytes={args.child_olean.stat().st_size}")
    print(f"elapsed_seconds={time.perf_counter() - start:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

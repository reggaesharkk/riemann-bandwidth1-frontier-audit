from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FAILED = ROOT / "failed_drafts"
FAILED.mkdir(exist_ok=True)
GEN = ROOT / "generate_node51_replay.py"
GOOD_INPUT = ROOT / "terminal15_authentic_input.json"
V2 = ROOT / "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
CHILD_LEAN = ROOT / "reference_dependencies/Node53Replay.lean"
CHILD_OLEAN = ROOT / "reference_dependencies/Node53Replay.olean"
TEMPLATE = ROOT / "Node51Replay.lean.template"
PROOF = ROOT / "Node51Replay.lean"


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def case(label: str, input_path: Path = GOOD_INPUT, v2_path: Path = V2,
         child_olean: Path = CHILD_OLEAN, expected: str = "") -> str:
    output = FAILED / f"mutation_{label}.lean"
    command = [sys.executable, str(GEN), "--input", str(input_path), "--v2-zip", str(v2_path),
               "--child-lean", str(CHILD_LEAN), "--child-olean", str(child_olean),
               "--template", str(TEMPLATE), "--compared-proof", str(PROOF), "--output", str(output)]
    result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    require(result.returncode != 0, f"mutated input accepted: {label}")
    require(expected in result.stdout, f"{label}: expected diagnostic {expected!r}, got {result.stdout!r}")
    require(not output.exists(), f"generator emitted source after rejecting {label}")
    return f"PASS {label}: rejected with {expected}"


def main() -> int:
    data = json.loads(GOOD_INPUT.read_text(encoding="utf-8"))
    bad_axis = json.loads(json.dumps(data))
    bad_axis["parent"]["split_axis_zero_based"] = 0
    bad_axis_path = FAILED / "terminal15_bad_axis.json"
    bad_axis_path.write_text(json.dumps(bad_axis), encoding="utf-8")

    bad_anchor = json.loads(json.dumps(data))
    bad_anchor["children"]["left"]["anchor_codes_u16le"][0] = 1
    bad_anchor_path = FAILED / "terminal15_bad_anchor.json"
    bad_anchor_path.write_text(json.dumps(bad_anchor), encoding="utf-8")

    bad_v2 = FAILED / "not_the_frozen_v2.zip"
    bad_v2.write_bytes(b"changed source archive")

    bad_olean = FAILED / "Node53Replay_mutated.olean"
    child_bytes = CHILD_OLEAN.read_bytes()
    require(len(child_bytes) > 10, "unexpectedly small predecessor olean")
    bad_olean.write_bytes(child_bytes[:-1] + bytes([child_bytes[-1] ^ 1]))

    messages = [
        case("axis", input_path=bad_axis_path, expected="source node 51 / axis 1"),
        case("anchor", input_path=bad_anchor_path, expected="kind or serialized anchor mismatch"),
        case("source_hash", v2_path=bad_v2, expected="frozen V2 archive digest mismatch"),
        case("predecessor_object", child_olean=bad_olean, expected="node53 proof object does not match"),
    ]
    print("\n".join(messages))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

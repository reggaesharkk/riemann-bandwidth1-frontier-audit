#!/usr/bin/env python3
"""Emit a bounded Lean smoke test for one complete segmented model row."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "siblings_normal.json").read_text(encoding="utf-8"))
term = next(x for x in data["children"]["left"]["fifteen_models"]
            if x["kind"] == "segmented_constant" and x["base"] != "0")
name = "smokeSegments"
floor = term["base"]
lo, hi = term["distance_interval"]
out = []
for seg in term["segments"]:
    out.append(f"  {{ lo := {seg['segment'][0]}, hi := {seg['segment'][1]}, "
               f"piece := {seg['declaration']} }}")
rows = term["segments"]
body = [
    f"def {name} : List SourceSegment := [\n" + ",\n".join(out) + "\n]",
]
checks = []
for i, seg in enumerate(rows):
    nm = f"smoke_segment_{i}_checked"
    checks.append(nm)
    body.append(
        f"theorem {nm} : sourceSegmentCheck ({floor}) "
        f"{{ lo := {seg['segment'][0]}, hi := {seg['segment'][1]}, "
        f"piece := {seg['declaration']} }} = true := by\n"
        f"  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, "
        f"{seg['declaration']}, MacroPiece.box]"
    )
body.append(
    f"theorem smokeAccepted : sourcePiecewiseCheck ({lo}) ({hi}) "
    f"({floor}) {name} = true := by\n"
    f"  have hlen : decide (0 < {name}.length) = true := by norm_num [{name}]\n"
    f"  have hcover : sourceCoverFrom ({lo}) ({hi}) {name} = true := by\n"
    f"    norm_num [sourceCoverFrom, {name}]\n"
    f"  have hall : {name}.all (sourceSegmentCheck ({floor})) = true := by\n"
    f"    simp only [{name}, List.all_cons, List.all_nil, " + ", ".join(checks) + ", Bool.true_and]\n"
    f"  simp [sourcePiecewiseCheck, hlen, hcover, hall]"
)
prefix = (HERE / "SegmentPrototype.lean").read_text(encoding="utf-8").split("def piece3Well :", 1)[0]
prefix = prefix.replace(
    "import Zeta23.ThmD.Sextuple.AffineTree\n",
    "import Zeta23.ThmD.Sextuple.AffineTree\n"
    "import Zeta23.ThmD.Sextuple.Macro.AffineAdapter\n", 1)
(HERE / "SegmentRowSmoke.lean").write_text(
    prefix + "\n" + "\n\n".join(body) +
    "\n\nend A1294TwoQuadraticParent\n", encoding="utf-8", newline="\n")
print(f"emitted {len(rows)} exact segment proofs, floor={floor}, interval=({lo},{hi})")

from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "terminal17_authentic_input.json").read_text(encoding="utf-8-sig"))["children"]["left"]
reindex = json.loads((ROOT / "terminal17_catalog_reindex.json").read_text(encoding="utf-8"))
local = {int(k): int(v) for k, v in reindex["local_index_by_global_index"].items()}
rows = data["fifteen_models"]
assert len(rows) == 15 and all(r["kind"] == "segmented_constant" for r in rows)
assert sum(len(r["segments"]) for r in rows) == 375
assert all(Fraction(r["weight"]) == 0 and Fraction(r["offset"]) == 0 for r in rows)

def q(s: str) -> str:
    x = Fraction(s)
    if x == 0:
        return "(0)"
    if x.denominator == 1:
        return f"({x.numerator})"
    return f"({x.numerator}/{x.denominator})"

def rat(s: str) -> str:
    x = Fraction(s)
    return f"⟨({x.numerator}), {x.denominator}⟩"

refs = sorted(local)
names = [f"macroPiece{i}" if i < 56 else f"refinementPiece{i-56}" if i < 272 else f"refinement2Piece{i-272}" for i in refs]
out = [
    "import Catalog17AllLookups",
    "import Zeta23.ThmD.Sextuple.CompositionalLeaf",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "noncomputable section",
    "namespace AuthenticCompact17",
    "open A1294FifteenBridge A1294Compact A1294GenericChecker",
    "def catalog : Array MacroPiece := Catalog17.catalog",
]
for i, nm in enumerate(names):
    out.append(f"theorem catalog_ref_{i} : catalog[{i}]? = some {nm} := by exact Catalog17AllLookups.catalog_lookup_{i}")

for row in rows:
    i = int(row["pair_index_zero_based"])
    segs = []
    for seg in row["segments"]:
        segs.append("{ lo := " + rat(seg["segment"][0]) + ", hi := " + rat(seg["segment"][1]) + f", pieceRef := {local[int(seg['catalog_index_zero_based'])]} }}")
    out.append(f"def row{i} : CompactRow := .floor {rat(row['base'])} [\n" + ",\n".join(segs) + "]")
out.append("def rows (p : Fin 15) : CompactRow := match p.val with " + " ".join(f"| {i} => row{i}" for i in range(14)) + " | _ => row14")
box = data["box_exact"]
out.append(
    "def box : GapBox where\n"
    + "  lo := fun i => match i.val with " + " ".join(f"| {i} => {q(interval[0])}" for i, interval in enumerate(box[:4])) + f" | _ => {q(box[4][0])}\n"
    + "  hi := fun i => match i.val with " + " ".join(f"| {i} => {q(interval[1])}" for i, interval in enumerate(box[:4])) + f" | _ => {q(box[4][1])}"
)
out.append("def anchor : Fin 5 → ℚ := box.lo")
out.append("open A1294GenericChecker")

for row in rows:
    i = int(row["pair_index_zero_based"])
    base = q(row["base"])
    lo, hi = (q(x) for x in row["distance_interval"])
    ss_name = f"segments{i}"
    segs = row["segments"]
    out.append(f"theorem canonical_{i} : compactRowCanonical row{i} = true := by decide")
    ss = ["{ lo := " + q(s["segment"][0]) + ", hi := " + q(s["segment"][1]) + ", piece := " + s["declaration"] + " }" for s in segs]
    out.append(f"def {ss_name} : List SourceSegment := [\n" + ",\n".join(ss) + "]")
    for k, seg in enumerate(segs):
        j = local[int(seg["catalog_index_zero_based"])]
        lo_seg, hi_seg = (q(x) for x in seg["segment"])
        decl = seg["declaration"]
        out += [
            f"theorem decode_segment_{i}_{k} : interpSegment catalog {{ lo := {rat(seg['segment'][0])}, hi := {rat(seg['segment'][1])}, pieceRef := {j} }} = some {{ lo := {lo_seg}, hi := {hi_seg}, piece := {decl} }} := by",
            f"  simp only [interpSegment, catalog_ref_{j}]",
            "  rfl",
            f"theorem segment_{i}_{k} : sourceSegmentCheck {base} {{ lo := {lo_seg}, hi := {hi_seg}, piece := {decl} }} = true := by",
            f"  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, {decl}, MacroPiece.box]",
        ]
    decode_names = ", ".join(f"decode_segment_{i}_{k}" for k in range(len(segs)))
    out += [
        f"theorem decode_{i} : interpCompactRow catalog row{i} = some (.floor {base} {ss_name}) := by",
        f"  simp [interpCompactRow, row{i}, {ss_name}, List.mapM_cons, {decode_names}, interpRat]",
        f"theorem coverage_{i} : sourceCoverFrom {lo} {hi} {ss_name} = true := by",
        f"  norm_num [sourceCoverFrom, {ss_name}]",
        f"theorem piecewise_{i} : certifiedPiecewiseCheck {lo} {hi} {base} {ss_name} = true := by",
        f"  have hlen : decide (0 < {ss_name}.length) = true := by norm_num [{ss_name}]",
        f"  have hall : {ss_name}.all (sourceSegmentCheck {base}) = true := by",
        f"    simp only [{ss_name}, List.all_cons, List.all_nil, {', '.join(f'segment_{i}_{k}' for k in range(len(segs)))}, Bool.true_and]",
        f"  have hp : {ss_name}.all (fun s => s.piece.check) = true := by",
        f"    simp only [{ss_name}, List.all_cons, List.all_nil, {', '.join(dict.fromkeys(s['declaration'] + '_check' for s in segs))}, Bool.true_and]",
        f"  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hlen, coverage_{i}, hall, hp]",
    ]

distances = " ".join(f"| {i} => ⟨{q(row['distance_interval'][0])}, {q(row['distance_interval'][1])}⟩" for i, row in enumerate(rows[:-1])) + f" | _ => ⟨{q(rows[-1]['distance_interval'][0])}, {q(rows[-1]['distance_interval'][1])}⟩"
out += [
    f"def distances (p : Fin 15) : RatInterval := match p.val with {distances}",
    "theorem distances_exact : ∀ p, distanceInterval box p = distances p := by\n  intro p\n  fin_cases p <;> simp [distanceInterval, distances, gapSupport, pairLeft, pairRight, box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num",
]
for row in rows:
    i = int(row["pair_index_zero_based"])
    out += [
        f"theorem row_checked_{i} : compactRowCheck catalog box (⟨{i}, by decide⟩ : Fin 15) row{i} = true := by",
        f"  simp only [compactRowCheck, canonical_{i}, decode_{i}, Bool.true_and, modelCheck]",
        "  rw [distances_exact]",
        f"  exact piecewise_{i}",
    ]
floors = " ".join(f"| {i} => {q(row['base'])}" for i, row in enumerate(rows[:-1])) + f" | _ => {q(rows[-1]['base'])}"
out += [
    f"def floors (p : Fin 15) : ℚ := match p.val with {floors}",
    "def terms (p : Fin 15) : RankOneModel := { base := floors p, weight := 0, offset := 0, coeff := fun _ => 0 }",
    "theorem interpreted_terms : (fun p => interpModel (decodedRow catalog (rows p)) p) = terms := by\n  funext p\n  fin_cases p <;> simp [rows, decodedRow, " + ", ".join(f"decode_{i}" for i in range(15)) + ", interpModel, terms, floors, interpRat]",
    f"theorem tangent_lower : rankTangentLower terms (1094977/5000000000) box anchor = {q(data['rank_tangent_lower'])} := by\n  norm_num [rankTangentLower, rankObjectiveRat, rankGradient, affineCoordinateLower, terms, floors, anchor, box, wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport, RankOneModel.valueRat, RankOneModel.dotRat, pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ, Fin.sum_univ_five]",
    "theorem tangent_checked : rankTangentCheck (647/50000) (1094977/5000000000) box anchor terms = true := by\n  have ho : box.ordered = true := by\n    rw [GapBox.ordered_iff]\n    intro i\n    fin_cases i <;> norm_num [box]\n  have ha : ∀ i, box.lo i ≤ anchor i ∧ anchor i ≤ box.hi i := by\n    intro i\n    fin_cases i <;> norm_num [anchor, box]\n  have hw : ∀ p, 0 ≤ (terms p).weight := by\n    intro p\n    fin_cases p <;> norm_num [terms, floors]\n  have hm : (647/50000 : ℚ) ≤ rankTangentLower terms (1094977/5000000000) box anchor := by\n    rw [tangent_lower]\n    norm_num\n  simp [rankTangentCheck, ho, ha, hw, hm]",
    "theorem all_rows : ∀ p, compactRowCheck catalog box p (rows p) = true := by\n  intro p\n  fin_cases p\n" + "\n".join(f"  · exact row_checked_{i}" for i in range(15)),
    "theorem accepted : compactQuadraticLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows = true := by\n  unfold compactQuadraticLeafCheck\n  rw [interpreted_terms]\n  simp [all_rows, tangent_checked]",
    "theorem accepted_original : compactQuadraticLeafCheck Catalog17.original (647/50000) (1094977/5000000000) box anchor rows = true := by\n  rw [Catalog17Identity.original_eq_catalog]\n  exact accepted",
    "theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →\n    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=\n  compactQuadraticLeafCheck_sound accepted_original",
    "#print accepted\n#print accepted_original\n#print leaf_sound\n#print axioms all_rows\n#print axioms tangent_checked\n#print axioms accepted\n#print axioms leaf_sound\nend AuthenticCompact17",
]
(ROOT / "Terminal17Compositional.lean").write_text("\n".join(out) + "\n", encoding="utf-8")
print("generated compositional terminal-17 source: 15 rows, 375 segment occurrences, 175 selected catalog refs")

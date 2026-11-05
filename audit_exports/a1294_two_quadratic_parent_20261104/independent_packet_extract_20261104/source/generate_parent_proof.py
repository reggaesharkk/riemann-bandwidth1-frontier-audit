#!/usr/bin/env python3
"""Generate source-derived Lean obligations for the authenticated node-65 sibling pair."""
from __future__ import annotations
import json
from pathlib import Path
import generate_lean_data

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "siblings_normal.json"
OUT = HERE / "A1294TwoQuadraticParent.lean"

def q(s):
    return f"({s})"

def box_def(name, rows):
    def field(k):
        clauses = " ".join(f"| {j} => {q(row[k])}" for j, row in enumerate(rows[:-1]))
        return "fun i => match i.val with " + clauses + f" | _ => {q(rows[-1][k])}"
    return f"def {name} : GapBox where\n  lo := {field(0)}\n  hi := {field(1)}\n"

def path_def(name, axes, sides):
    steps = [f"(⟨{a}, by decide⟩, {str(s == 'R').lower()})" for a, s in zip(axes, sides)]
    return f"def {name} : List (Fin 5 × Bool) := [\n  " + ",\n  ".join(steps) + "\n]\n"

def emit():
    d = json.loads(LEDGER.read_text(encoding="utf-8"))
    text = generate_lean_data.emit()
    ending = "\nend A1294TwoQuadraticParent\n"
    assert text.endswith(ending)
    text = text[:-len(ending)]
    out = ["\n-- Exact boxes, paths, anchors, segment certificates, tangent checks, and midpoint parent.\n"]
    out += ["def targetA : ℚ := 647 / 50000\ndef targetB : ℚ := 1094977 / 5000000000\n"]
    out.append(box_def("sourceParentBox", d["parent"]["box_exact"]))
    for side in ("left", "right"):
        out.append(box_def(f"source{side.title()}Box", d["children"][side]["box_exact"]))
    out.append(path_def("sourceParentPath", d["parent"]["path_axes_zero_based"], d["parent"]["path_sides"]))
    out.append("""
def descend (box : GapBox) (step : Fin 5 × Bool) : GapBox :=
  if step.2 then box.upperHalf step.1 else box.lowerHalf step.1

def sourceLeftPath : List (Fin 5 × Bool) :=
  sourceParentPath ++ [(⟨0, by decide⟩, false)]
def sourceRightPath : List (Fin 5 × Bool) :=
  sourceParentPath ++ [(⟨0, by decide⟩, true)]

theorem gapBox_ext_exact {a b : GapBox}
    (hlo : ∀ i, a.lo i = b.lo i) (hhi : ∀ i, a.hi i = b.hi i) : a = b := by
  cases a with
  | mk alo ahi =>
    cases b with
    | mk blo bhi =>
      simp only [GapBox.mk.injEq]
      constructor
      · funext i
        exact hlo i
      · funext i
        exact hhi i

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
theorem source_children_match_parent_split :
    sourceLeftBox = sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) ∧
    sourceRightBox = sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5) := by
  constructor
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def sourceAnchorCodes : Fin 5 → ℕ := fun _ => 0
def sourceAnchorLeft : Fin 5 → ℚ := fun i =>
  sourceLeftBox.lo i + (sourceAnchorCodes i : ℚ) / 16384 *
    (sourceLeftBox.hi i - sourceLeftBox.lo i)
def sourceAnchorRight : Fin 5 → ℚ := fun i =>
  sourceRightBox.lo i + (sourceAnchorCodes i : ℚ) / 16384 *
    (sourceRightBox.hi i - sourceRightBox.lo i)

theorem source_left_anchor_exact : sourceAnchorLeft = sourceLeftBox.lo := by
  funext i
  simp [sourceAnchorLeft, sourceAnchorCodes]
theorem source_right_anchor_exact : sourceAnchorRight = sourceRightBox.lo := by
  funext i
  simp [sourceAnchorRight, sourceAnchorCodes]
""")
    for side in ("left", "right"):
        title = side.title()
        child = d["children"][side]
        ds = [t["distance_interval"] for t in child["fifteen_models"]]
        floors = [t["base"] for t in child["fifteen_models"]]
        dclauses = " ".join(f"| {i} => ⟨{q(x[0])}, {q(x[1])}⟩" for i, x in enumerate(ds[:-1])) + f" | _ => ⟨{q(ds[-1][0])}, {q(ds[-1][1])}⟩"
        fclauses = " ".join(f"| {i} => {q(x)}" for i, x in enumerate(floors[:-1])) + f" | _ => {q(floors[-1])}"
        out.append(f"def sourceDistance{title} (p : Fin 15) : RatInterval := match p.val with {dclauses}\n")
        out.append(f"def sourceFloor{title} (p : Fin 15) : ℚ := match p.val with {fclauses}\n")
        out.append(f"""
def sourceRankTerms{title} (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => MacroPrototype.macroPiece11) p
  else {{ base := sourceFloor{title} p, weight := 0, offset := 0, coeff := fun _ => 0 }}

theorem source_distance_intervals_{side}_exact :
    ∀ p, distanceInterval source{title}Box p = sourceDistance{title} p := by
  intro p
  fin_cases p <;> simp [distanceInterval, sourceDistance{title}, gapSupport,
    pairLeft, pairRight, source{title}Box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num

""")
        for t in child["fifteen_models"]:
            i = t["pair_index_zero_based"]
            nm = f"source_model_{side}_{i}_valid"
            p = f"(⟨{i}, by decide⟩ : Fin 15)"
            if t["kind"] == "direct_piece":
                out.append(f"""
theorem {nm} {{g : Fin 5 → ℝ}} (hg : source{title}Box.Holds g) :
    (sourceRankTerms{title} {p}).value g ≤ 2 * mtKernel (gapDistance g {p}) ^ 2 := by
  have hfit : MacroPrototype.macroPiece11.box.lo ≤
      (distanceInterval source{title}Box {p}).lo ∧
      (distanceInterval source{title}Box {p}).hi ≤ MacroPrototype.macroPiece11.box.hi := by
    rw [source_distance_intervals_{side}_exact {p}]
    norm_num [sourceDistance{title}, MacroPrototype.macroPiece11, MacroPiece.box]
  have hd := distanceInterval_holds hg {p}
  have hpiece : RatInterval.Holds MacroPrototype.macroPiece11.box
      (gapDistance g {p}) := by
    constructor
    · have hlo : MacroPrototype.macroPiece11.box.lo ≤
        (distanceInterval source{title}Box {p}).lo := hfit.1
      have hloR : (MacroPrototype.macroPiece11.box.lo : ℝ) ≤
          ((distanceInterval source{title}Box (⟨{p}, by decide⟩ : Fin 15)).lo : ℝ) := by
        exact_mod_cast hlo
      exact hloR.trans hd.1
    · have hhi : (distanceInterval source{title}Box {p}).hi ≤
        MacroPrototype.macroPiece11.box.hi := hfit.2
      have hhiR : ((distanceInterval source{title}Box (⟨{p}, by decide⟩ : Fin 15)).hi : ℝ) ≤
          (MacroPrototype.macroPiece11.box.hi : ℝ) := by
        exact_mod_cast hhi
      exact hd.2.trans hhiR
  have hbound := MacroPiece.check_sound MacroPrototype.macroPiece11_check hpiece
  simpa [sourceRankTerms{title}] using hbound
""")
            elif t["base"] == "0":
                out.append(f"""
theorem {nm} {{g : Fin 5 → ℝ}} (hg : source{title}Box.Holds g) :
    (sourceRankTerms{title} {p}).value g ≤ 2 * mtKernel (gapDistance g {p}) ^ 2 := by
  have hnonneg : (0 : ℝ) ≤ 2 * mtKernel (gapDistance g {p}) ^ 2 := by positivity
  simpa [sourceRankTerms{title}, sourceFloor{title}, RankOneModel.value,
    RankOneModel.dot] using hnonneg
""")
            else:
                out.append(f"""
theorem {nm} {{g : Fin 5 → ℝ}} (hg : source{title}Box.Holds g) :
    (sourceRankTerms{title} {p}).value g ≤ 2 * mtKernel (gapDistance g {p}) ^ 2 := by
  have hdist := distanceInterval_holds hg {p}
  rw [source_distance_intervals_{side}_exact] at hdist
  have hbound := sourcePiecewiseCheck_sound segments_{side}_{i}_accepted
    segments_{side}_{i}_pieces_checked hdist.1 hdist.2
  simpa [sourceRankTerms{title}, sourceFloor{title}, RankOneModel.value,
    RankOneModel.dot] using hbound
""")
        out.append(f"""theorem source_models_{side}_pairwise_valid {{g : Fin 5 → ℝ}}
    (hg : source{title}Box.Holds g) : ∀ p,
      (sourceRankTerms{title} p).value g ≤ 2 * mtKernel (gapDistance g p) ^ 2 := by
  intro p
  fin_cases p
""")
        out.extend(f"  · exact source_model_{side}_{i}_valid hg\n" for i in range(15))
        tangent = q(child["rank_tangent_lower"])
        out.append(f"""
theorem source_rank_tangent_{side} :
    rankTangentLower sourceRankTerms{title} targetB source{title}Box
      sourceAnchor{title} = {tangent} := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient,
    affineCoordinateLower, sourceRankTerms{title}, sourceFloor{title},
    sourceAnchor{title}, sourceAnchorCodes, targetB, source{title}Box,
    MacroPrototype.macroPiece11, MacroPiece.box, macroPieceRankModel,
    wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport,
    RankOneModel.valueRat, RankOneModel.dotRat,
    pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ,
    Fin.sum_univ_five]

theorem source_rank_tangent_check_{side} :
    rankTangentCheck targetA targetB source{title}Box sourceAnchor{title}
      sourceRankTerms{title} = true := by
  have hordered : source{title}Box.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [source{title}Box]
  have hanchor : ∀ i, source{title}Box.lo i ≤ sourceAnchor{title} i ∧
      sourceAnchor{title} i ≤ source{title}Box.hi i := by
    intro i
    fin_cases i <;> norm_num [sourceAnchor{title}, sourceAnchorCodes, source{title}Box]
  have hweights : ∀ p, 0 ≤ (sourceRankTerms{title} p).weight := by
    intro p
    fin_cases p <;> norm_num [sourceRankTerms{title}, sourceFloor{title},
      MacroPrototype.macroPiece11, macroPieceRankModel, wellRankModel, wellSlope, wellOffset]
  have hmargin : targetA ≤ rankTangentLower sourceRankTerms{title} targetB
      source{title}Box sourceAnchor{title} := by
    rw [source_rank_tangent_{side}]
    norm_num [targetA]
  simp [rankTangentCheck, hordered, hanchor, hweights, hmargin]

theorem source_{side}_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, source{title}Box.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  exact rankTangentCheck_energy_sound source_rank_tangent_check_{side}
    (by
      intro g hg p
      exact source_models_{side}_pairwise_valid hg p)
""")
    out.append("""
theorem source_parent_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceParentBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  have hleft : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.1]
    exact source_left_box_predicate
  have hright : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.2]
    exact source_right_box_predicate
  exact boxPredicate_of_midpoint_children hleft hright

#print axioms source_children_match_parent_split
#print axioms source_left_box_predicate
#print axioms source_right_box_predicate
#print axioms source_parent_box_predicate

end A1294TwoQuadraticParent
""")
    return text + "\n".join(out)

if __name__ == "__main__":
    OUT.write_text(emit(), encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")

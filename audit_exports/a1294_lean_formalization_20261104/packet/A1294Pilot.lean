import Zeta23.ThmD.Sextuple.AffineTree

open Zeta23.ThmD.Sextuple

noncomputable section

namespace A1294Pilot

def targetA : ℚ := 647 / 50000
def targetB : ℚ := 1094977 / 5000000000

theorem exact_tail_margin :
    60 * targetB - targetA = (49931 : ℚ) / 250000000 := by
  norm_num [targetA, targetB]

theorem positive_tail_margin : 0 < 60 * targetB - targetA := by
  rw [exact_tail_margin]
  norm_num

theorem tail_span_bound {g : Fin 5 → ℝ} (hspan : (60 : ℝ) ≤ sextupleSpan g) :
    (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  have henergy : 0 ≤ sextupleEnergy g := sextupleEnergy_nonneg g
  have hB : (0 : ℝ) ≤ (targetB : ℝ) := by norm_num [targetB]
  have hscale : (60 : ℝ) * (targetB : ℝ) ≤ (targetB : ℝ) * sextupleSpan g := by
    calc
      (60 : ℝ) * (targetB : ℝ) = (targetB : ℝ) * (60 : ℝ) := by ring
      _ ≤ (targetB : ℝ) * sextupleSpan g := mul_le_mul_of_nonneg_left hspan hB
  have hbaseQ : targetA ≤ 60 * targetB := by
    nlinarith [exact_tail_margin]
  have hbase : (targetA : ℝ) ≤ (60 : ℝ) * (targetB : ℝ) := by
    exact_mod_cast hbaseQ
  nlinarith

theorem tail_covers_root_complement {g : Fin 5 → ℝ}
    (hg : ∀ i, 0 ≤ g i)
    (hout : ¬ (initialGapBox 60).Holds g) :
    (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  apply tail_span_bound
  by_contra hspan
  exact hout (initialGapBox_holds hg (le_of_lt (lt_of_not_ge hspan)))

def tailLeafBox : GapBox where
  lo := fun i => match i.val with
    | 0 => 45 / 4
    | 1 => 45 / 4
    | 2 => 45 / 8
    | 3 => 45 / 4
    | _ => 165 / 8
  hi := fun i => match i.val with
    | 0 => 105 / 8
    | 1 => 105 / 8
    | 2 => 15 / 2
    | 3 => 105 / 8
    | _ => 45 / 2

def tailLeafPath : List (Fin 5 × Bool) := [
  (2, false), (1, false), (3, false), (0, false), (4, false),
  (2, false), (1, false), (3, false), (0, false), (4, true),
  (2, false), (1, true), (3, true), (0, true), (4, false),
  (2, true), (1, true), (3, true), (0, true), (4, true),
  (2, true), (1, false), (3, false), (0, false), (4, true)
]

def descend (box : GapBox) (step : Fin 5 × Bool) : GapBox :=
  if step.2 then box.upperHalf step.1 else box.lowerHalf step.1

def reconstructedBox : GapBox := tailLeafPath.foldl descend (initialGapBox 60)
def selectedBox : GapBox := tailLeafBox

theorem extracted_path_reconstructs_box :
    ∀ i, reconstructedBox.lo i = tailLeafBox.lo i ∧
      reconstructedBox.hi i = tailLeafBox.hi i := by
  intro i
  fin_cases i <;>
    simp [tailLeafBox, tailLeafPath, descend,
      reconstructedBox, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint,
      Function.update] <;> norm_num

def tailLeafChecker : GapBox → AffineLeafPayload Unit → Bool :=
  affineLeafCheck targetA targetB (fun _ _ => false)

def tailLeafTopology : CursorStream AffineTreeToken :=
  CursorStream.ofList [.terminal]

def tailLeafPayloads : CursorStream (AffineLeafPayload Unit) :=
  CursorStream.ofList [.tail]

theorem tailLeaf_check_true : affineTailCheck targetA targetB tailLeafBox = true := by
  have hordered : tailLeafBox.ordered = true := by
    apply (GapBox.ordered_iff tailLeafBox).2
    intro i
    fin_cases i <;> norm_num [tailLeafBox]
  have hspan : tailLeafBox.lowerSpan = 60 := by
    norm_num [GapBox.lowerSpan, tailLeafBox, Fin.sum_univ_succ]
  simp [affineTailCheck, hordered, hspan]
  norm_num [targetA, targetB]

/-- The extracted source terminal is a complete one-node serialized subtree. -/
theorem source_tail_leaf_checker_true :
    checkAffineTree tailLeafChecker tailLeafTopology tailLeafPayloads 1 selectedBox = true := by
  change checkAffineTree tailLeafChecker tailLeafTopology tailLeafPayloads 1 tailLeafBox = true
  unfold checkAffineTree
  apply of_decide_eq_true
  simp [replayAffineTree, CursorStream.get?, CursorStream.ofList, tailLeafTopology,
    tailLeafPayloads, tailLeafChecker, affineLeafCheck, tailLeaf_check_true]

theorem source_tail_leaf_sound {g : Fin 5 → ℝ} (hg : tailLeafBox.Holds g) :
    (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  exact affineTailCheck_sound tailLeaf_check_true hg

theorem selected_complete_subtree_sound :
    BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g) selectedBox := by
  refine checkAffineTree_sound (P := fun g =>
    (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
    (leafCheck := tailLeafChecker) (topology := tailLeafTopology)
    (payloads := tailLeafPayloads) (fuel := 1) (root := selectedBox) ?_ ?_
  · intro box payload hc
    cases payload with
    | tail =>
        intro g hg
        exact affineTailCheck_sound (by simpa [tailLeafChecker, affineLeafCheck] using hc) hg
    | quadratic u =>
        simp [tailLeafChecker, affineLeafCheck] at hc
  · exact source_tail_leaf_checker_true

#print axioms exact_tail_margin
#print axioms sextupleEnergy_nonneg
#print axioms tail_span_bound
#print axioms tail_covers_root_complement
#print axioms extracted_path_reconstructs_box
#print axioms source_tail_leaf_checker_true
#print axioms source_tail_leaf_sound
#print axioms selected_complete_subtree_sound

end A1294Pilot

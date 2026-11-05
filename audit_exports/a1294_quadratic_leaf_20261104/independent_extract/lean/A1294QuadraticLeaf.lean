import Zeta23.ThmD.Sextuple.AffineTree
import Zeta23.ThmD.Sextuple.Macro.EnvelopeData

open Zeta23.ThmD.Sextuple
open Zeta23.ThmD.Sextuple.MacroPrototype

noncomputable section

namespace A1294QuadraticLeaf

def targetA : ℚ := 647 / 50000
def targetB : ℚ := 1094977 / 5000000000
def selectedPositiveLower : ℚ := 14630385677 / 1000000000000

/-- The exact box at the first serialized quadratic terminal, source node 16. -/
def sourceLeafBox : GapBox where
  lo := fun _ => 0
  hi := fun i => if i.val = 2 then 15 / 4 else 15 / 2

/-- Zero-based axes and sides read from the authenticated V2 root-to-leaf prefix. -/
def sourcePath : List (Fin 5 × Bool) := [
  (2, false), (1, false), (3, false), (0, false), (4, false),
  (2, false), (1, false), (3, false), (0, false), (4, false),
  (2, false), (1, false), (3, false), (0, false), (4, false),
  (2, false)
]

def descend (box : GapBox) (step : Fin 5 × Bool) : GapBox :=
  if step.2 then box.upperHalf step.1 else box.lowerHalf step.1

def reconstructedSourceBox : GapBox :=
  sourcePath.foldl descend (initialGapBox 60)

theorem source_path_reconstructs_box :
    ∀ i, reconstructedSourceBox.lo i = sourceLeafBox.lo i ∧
      reconstructedSourceBox.hi i = sourceLeafBox.hi i := by
  intro i
  fin_cases i <;>
    simp [reconstructedSourceBox, sourcePath, descend, sourceLeafBox,
      initialGapBox, GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> norm_num

/-- The five serialized anchor codes are all zero, with denominator 16384. -/
def sourceAnchorCodes : Fin 5 → ℕ := fun _ => 0
def sourceAnchor : Fin 5 → ℚ := fun i =>
  sourceLeafBox.lo i + (sourceAnchorCodes i : ℚ) / 16384 *
    (sourceLeafBox.hi i - sourceLeafBox.lo i)

theorem source_anchor_is_lower_corner : ∀ i, sourceAnchor i = 0 := by
  intro i
  fin_cases i <;> norm_num [sourceAnchor, sourceAnchorCodes, sourceLeafBox]

/-- The V2 exact replay's fifteen scalar lower models on this box.
    Fourteen outputs are zero; pair 9 has the positive segmented lower value. -/
def selectedLower (p : Fin 15) : ℚ :=
  if p.val = 9 then selectedPositiveLower else 0

def selectedRankTerms : Fin 15 → RankOneModel := fun p => {
  base := selectedLower p
  weight := 0
  offset := 0
  coeff := fun _ => 0
}

/-- The stable source zero piece which attains the segmented lower value zero. -/
theorem active_zero_source_piece_valid {x : ℝ}
    (hx : RatInterval.Holds MacroPrototype.macroPiece4.box x) :
    0 ≤ 2 * mtKernel x ^ 2 := by
  have h := MacroPiece.check_sound MacroPrototype.macroPiece4_check hx
  have hmodel : MacroPiece.model MacroPrototype.macroPiece4 x = 0 := by
    simp [MacroPiece.model, MacroPrototype.macroPiece4, LowerPiece.model]
  rw [hmodel] at h
  exact h

/-- Source macroPiece0 proves the lower bound on [0,2], and source macroPiece1
    proves the exact positive floor on [2,15/4]. Their seam is the rational 2. -/
theorem selected_pair9_model_valid {x : ℝ}
    (hxlo : 0 ≤ x) (hxhi : x ≤ (15 / 4 : ℚ)) :
    (selectedPositiveLower : ℚ) ≤ 2 * mtKernel x ^ 2 := by
  by_cases hleft : x ≤ 2
  · have hpiece : RatInterval.Holds MacroPrototype.macroPiece0.box x := by
      simpa [MacroPiece.box, MacroPrototype.macroPiece0, RatInterval.Holds] using
        And.intro hxlo hleft
    have hbound := MacroPiece.check_sound MacroPrototype.macroPiece0_check hpiece
    have hmodel : MacroPiece.model MacroPrototype.macroPiece0 x = (1 / 4 : ℝ) := by
      norm_num [MacroPiece.model, MacroPrototype.macroPiece0, LowerPiece.model]
    rw [hmodel] at hbound
    have hfloor : (selectedPositiveLower : ℝ) ≤ (1 / 4 : ℝ) := by
      norm_num [selectedPositiveLower]
    exact hfloor.trans hbound
  · have hright : (2 : ℝ) < x := lt_of_not_ge hleft
    have hpiece : RatInterval.Holds MacroPrototype.macroPiece1.box x := by
      have hseam : (15 / 4 : ℚ) ≤ 235723 / 40000 := by norm_num
      have hxright : ((2 : ℚ) : ℝ) ≤ x := le_of_lt hright
      have hxupper : x ≤ ((235723 / 40000 : ℚ) : ℝ) :=
        le_trans hxhi (by exact_mod_cast hseam)
      simpa [MacroPiece.box, MacroPrototype.macroPiece1, RatInterval.Holds] using
        And.intro hxright hxupper
    have hbound := MacroPiece.check_sound MacroPrototype.macroPiece1_check hpiece
    have hmodel : MacroPiece.model MacroPrototype.macroPiece1 x =
        (selectedPositiveLower : ℝ) := by
      norm_num [MacroPiece.model, MacroPrototype.macroPiece1,
        LowerPiece.model, selectedPositiveLower]
    rw [hmodel] at hbound
    exact hbound

theorem selected_models_pairwise_valid :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceLeafBox.Holds g → ∀ p : Fin 15,
      (selectedRankTerms p).value g ≤ 2 * mtKernel (gapDistance g p) ^ 2 := by
  intro g hg p
  by_cases hp : p.val = 9
  · have hp9 : p = (9 : Fin 15) := Fin.ext hp
    subst p
    simp [selectedRankTerms, selectedLower, RankOneModel.value,
      RankOneModel.dot, selectedPositiveLower]
    have hdist : gapDistance g (9 : Fin 15) = g 2 := by
      simp [gapDistance, gapSupport, pairLeft, pairRight,
        Finset.sum_filter, Fin.sum_univ_five]
    rw [hdist]
    have hg2 : 0 ≤ g 2 ∧ g 2 ≤ ((15 / 4 : ℚ) : ℝ) := by
      simpa [sourceLeafBox] using hg 2
    simpa [selectedPositiveLower] using
      selected_pair9_model_valid hg2.1 hg2.2
  · have hzero : selectedLower p = 0 := by simp [selectedLower, hp]
    simp [selectedRankTerms, RankOneModel.value, RankOneModel.dot, hzero]
    positivity

theorem selected_rank_tangent_lower :
    rankTangentLower selectedRankTerms targetB sourceLeafBox sourceAnchor =
      selectedPositiveLower := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient,
    affineCoordinateLower, selectedRankTerms, selectedLower,
    sourceAnchor, sourceAnchorCodes, sourceLeafBox, targetB,
    selectedPositiveLower, RankOneModel.valueRat, RankOneModel.dotRat,
    Fin.sum_univ_succ]

theorem selected_rank_tangent_check :
    rankTangentCheck targetA targetB sourceLeafBox sourceAnchor
      selectedRankTerms = true := by
  have hordered : sourceLeafBox.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [sourceLeafBox]
  have hanchor : ∀ i, sourceLeafBox.lo i ≤ sourceAnchor i ∧
      sourceAnchor i ≤ sourceLeafBox.hi i := by
    intro i
    fin_cases i <;> norm_num [sourceLeafBox, sourceAnchor,
      sourceAnchorCodes]
  have hweights : ∀ p, 0 ≤ (selectedRankTerms p).weight := by
    intro p
    simp [selectedRankTerms]
  have hmargin : targetA ≤
      rankTangentLower selectedRankTerms targetB sourceLeafBox sourceAnchor := by
    rw [selected_rank_tangent_lower]
    norm_num [targetA, selectedPositiveLower]
  simp [rankTangentCheck, hordered, hanchor, hweights, hmargin]

theorem authentic_quadratic_leaf_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceLeafBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g +
        (targetB : ℝ) * sextupleSpan g := by
  exact rankTangentCheck_energy_sound selected_rank_tangent_check
    selected_models_pairwise_valid

#print axioms source_path_reconstructs_box
#print axioms source_anchor_is_lower_corner
#print axioms active_zero_source_piece_valid
#print axioms selected_pair9_model_valid
#print axioms selected_models_pairwise_valid
#print axioms selected_rank_tangent_lower
#print axioms selected_rank_tangent_check
#print axioms authentic_quadratic_leaf_box_predicate

end A1294QuadraticLeaf

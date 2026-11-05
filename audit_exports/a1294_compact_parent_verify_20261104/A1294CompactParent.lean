import Zeta23.ThmD.Sextuple.CompositionalRight
open Zeta23.ThmD.Sextuple
namespace A1294CompactParent
def targetA : ℚ := 647/50000
def targetB : ℚ := 1094977/5000000000
def sourceParentBox : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)

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
    AuthenticCompactLeaf.box = sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) ∧
    AuthenticCompactRight.box = sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5) := by
  constructor
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [AuthenticCompactLeaf.box, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [AuthenticCompactLeaf.box, sourceParentBox,
        GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [AuthenticCompactRight.box, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [AuthenticCompactRight.box, sourceParentBox,
        GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

theorem source_parent_box_predicate :
    ∀ ⦃g : Fin 5 → ℝ⦄, sourceParentBox.Holds g →
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g := by
  have hleft : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.1]
    exact AuthenticCompactLeaf.leaf_sound
  have hright : BoxPredicate (fun g =>
      (targetA : ℝ) ≤ sextupleEnergy g + (targetB : ℝ) * sextupleSpan g)
      (sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← source_children_match_parent_split.2]
    exact AuthenticCompactRight.leaf_sound
  exact boxPredicate_of_midpoint_children hleft hright

#print axioms source_children_match_parent_split
#print axioms AuthenticCompactLeaf.accepted
#print axioms AuthenticCompactRight.accepted
#print axioms source_parent_box_predicate
#print source_parent_box_predicate
end A1294CompactParent

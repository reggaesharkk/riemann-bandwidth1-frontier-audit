import Zeta23.ThmD.Sextuple.AffineTree
open Zeta23.ThmD.Sextuple
noncomputable section
namespace A1294TwoQuadraticParent

def sourceParentBox : GapBox where
  lo := fun i => match i.val with | 0 => 405/64 | 1 => 825/128 | 2 => 795/128 | 3 => 825/128 | _ => 405/64
  hi := fun i => match i.val with | 0 => 105/16 | 1 => 105/16 | 2 => 405/64 | 3 => 105/16 | _ => 105/16

def sourceLeftBox : GapBox where
  lo := fun i => match i.val with | 0 => 405/64 | 1 => 825/128 | 2 => 795/128 | 3 => 825/128 | _ => 405/64
  hi := fun i => match i.val with | 0 => 825/128 | 1 => 105/16 | 2 => 405/64 | 3 => 105/16 | _ => 105/16

def sourceRightBox : GapBox where
  lo := fun i => match i.val with | 0 => 825/128 | 1 => 825/128 | 2 => 795/128 | 3 => 825/128 | _ => 405/64
  hi := fun i => match i.val with | 0 => 105/16 | 1 => 105/16 | 2 => 405/64 | 3 => 105/16 | _ => 105/16

lemma gapBox_ext_exact {a b : GapBox}
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

set_option maxRecDepth 5000 in
set_option maxHeartbeats 2000000 in
theorem children_match :
    sourceLeftBox = sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) ∧
    sourceRightBox = sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5) := by
  constructor
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox, GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceLeftBox, sourceParentBox, GapBox.lowerHalf, GapBox.midpoint, Function.update] <;> decide
  · apply gapBox_ext_exact
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide
    · intro i
      fin_cases i <;> norm_num [sourceRightBox, sourceParentBox, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

#print axioms children_match
end A1294TwoQuadraticParent



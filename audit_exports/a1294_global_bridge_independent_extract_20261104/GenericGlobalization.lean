import Zeta23.ThmD.Sextuple.AffineTree
noncomputable section
namespace Zeta23.ThmD.Sextuple.MacroPrototype
open Zeta23.ThmD.Sextuple
theorem affineTree_global_at {A B limit : ℚ}
    (hB : 0 ≤ B) (htail : A ≤ B * limit)
    (hroot : BoxPredicate (affineEnergyGoal A B) (initialGapBox limit))
    (g : Fin 5 → ℝ) (hg : ∀ i, 0 ≤ g i) :
    affineEnergyGoal A B g := by
  by_cases hspan : ((limit : ℚ) : ℝ) ≤ sextupleSpan g
  · have henergy := sextupleEnergy_nonneg g
    have hBR : (0 : ℝ) ≤ ((B : ℚ) : ℝ) := by exact_mod_cast hB
    have hmul : (((B * limit : ℚ) : ℚ) : ℝ) ≤
        ((B : ℚ) : ℝ) * sextupleSpan g := by
      push_cast
      exact mul_le_mul_of_nonneg_left hspan hBR
    have hAR : ((A : ℚ) : ℝ) ≤ (((B * limit : ℚ) : ℚ) : ℝ) := by
      exact_mod_cast htail
    simp only [affineEnergyGoal]
    linarith
  · exact hroot (initialGapBox_holds hg (le_of_not_ge hspan))



#print axioms affineTree_global_at
end Zeta23.ThmD.Sextuple.MacroPrototype

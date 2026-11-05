import GenericGlobalization
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace A1294GlobalBridge
theorem exact_tail_margin :
    (60 : ℚ) * (1094977/5000000000) - (647/50000) = 49931/250000000 := by
  norm_num
theorem A1294_global_of_root_predicate
    (root : BoxPredicate (affineEnergyGoal (647/50000) (1094977/5000000000))
      (initialGapBox 60)) (g : Fin 5 → ℝ) (hg : ∀ i, 0 ≤ g i) :
    (647/50000 : ℝ) ≤ sextupleEnergy g + (1094977/5000000000 : ℝ) * sextupleSpan g := by
  have h := affineTree_global_at (A := 647/50000) (B := 1094977/5000000000)
    (limit := 60) (by norm_num) (by norm_num) root g hg
  simpa [affineEnergyGoal] using h
#print axioms exact_tail_margin
#print axioms A1294_global_of_root_predicate
end A1294GlobalBridge

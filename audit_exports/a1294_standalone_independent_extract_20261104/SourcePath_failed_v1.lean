import StandaloneTerminal22
open Zeta23.ThmD.Sextuple
namespace StandaloneSourcePath
set_option maxRecDepth 6000
set_option maxHeartbeats 1000000
def root : GapBox where
  lo := fun _ => 0
  hi := fun _ => 60
def steps : List (Fin 5 × Bool) := [
(⟨2,by decide⟩,false),
(⟨1,by decide⟩,false),
(⟨3,by decide⟩,false),
(⟨0,by decide⟩,false),
(⟨4,by decide⟩,false),
(⟨2,by decide⟩,false),
(⟨1,by decide⟩,false),
(⟨3,by decide⟩,false),
(⟨0,by decide⟩,false),
(⟨4,by decide⟩,false),
(⟨2,by decide⟩,false),
(⟨1,by decide⟩,false),
(⟨3,by decide⟩,false),
(⟨0,by decide⟩,false),
(⟨4,by decide⟩,false),
(⟨2,by decide⟩,true),
(⟨1,by decide⟩,true),
(⟨3,by decide⟩,true),
(⟨0,by decide⟩,true),
(⟨4,by decide⟩,true),
(⟨2,by decide⟩,true),
(⟨1,by decide⟩,true),
(⟨3,by decide⟩,true),
(⟨0,by decide⟩,true),
(⟨4,by decide⟩,true),
(⟨2,by decide⟩,false),
(⟨1,by decide⟩,false),
(⟨3,by decide⟩,false),
(⟨0,by decide⟩,false),
(⟨4,by decide⟩,false),
(⟨2,by decide⟩,true),
(⟨1,by decide⟩,true),
(⟨3,by decide⟩,true),
(⟨0,by decide⟩,true),
(⟨4,by decide⟩,true),
(⟨2,by decide⟩,false),
(⟨1,by decide⟩,true),
(⟨3,by decide⟩,true),
(⟨0,by decide⟩,true),
(⟨4,by decide⟩,true),
(⟨2,by decide⟩,true),
(⟨1,by decide⟩,true),
(⟨3,by decide⟩,true),
(⟨0,by decide⟩,false)]
def descend : GapBox → List (Fin 5 × Bool) → GapBox
  | box, [] => box
  | box, (axis,upper)::rest => descend (if upper then box.upperHalf axis else box.lowerHalf axis) rest
theorem path_box : descend root steps = IndependentTerminal22.box := by
  have hlo : ∀ i, (descend root steps).lo i = IndependentTerminal22.box.lo i := by
    intro i
    fin_cases i <;> norm_num [descend, root, steps, IndependentTerminal22.box, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update]
  have hhi : ∀ i, (descend root steps).hi i = IndependentTerminal22.box.hi i := by
    intro i
    fin_cases i <;> norm_num [descend, root, steps, IndependentTerminal22.box, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update]
  cases h : descend root steps with
  | mk lo hi =>
    have hl : lo = IndependentTerminal22.box.lo := by funext i; simpa [h] using hlo i
    have hh : hi = IndependentTerminal22.box.hi := by funext i; simpa [h] using hhi i
    rw [hl,hh]
#print axioms path_box
end StandaloneSourcePath

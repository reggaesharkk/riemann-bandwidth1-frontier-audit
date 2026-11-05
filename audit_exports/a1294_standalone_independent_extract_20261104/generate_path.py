from pathlib import Path
import json
D=Path(__file__).resolve().parent
j=json.loads((D/'authentic_input.json').read_text())['children']['left']
path=',\n'.join(f'(⟨{a},by decide⟩,{"true" if s=="R" else "false"})' for a,s in zip(j['path_axes_zero_based'],j['path_sides']))
s='''import StandaloneTerminal22
open Zeta23.ThmD.Sextuple
namespace StandaloneSourcePath
set_option maxRecDepth 6000
set_option maxHeartbeats 1000000
def root : GapBox where
  lo := fun _ => 0
  hi := fun _ => 60
def steps : List (Fin 5 × Bool) := [
'''+path+''']
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
'''
(D/'SourcePath.lean').write_text(s,encoding='utf-8');print('typed source midpoint path steps',len(j['path_sides']))

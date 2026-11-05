import CombinedHelpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace A1294Combined
set_option maxHeartbeats 400000
theorem threeNodeReplay {α : Type} (check : GapBox → α → Bool) (box : GapBox)
    (l r : α) (hl : check (box.lowerHalf 0) l = true)
    (hr : check (box.upperHalf 0) r = true) :
    replayAffineTree check (CursorStream.ofList [.split 0,.terminal,.terminal])
      (CursorStream.ofList [l,r]) 2 0 0 box = some (3,2) := by
  simp [replayAffineTree, hl, hr]

theorem replay65 : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox = some (3,2) := by
  exact threeNodeReplay leafCheck A1294Source.parentBox (.quadratic leftPayload) (.quadratic rightPayload) left_check right_check

theorem accepted_tree : checkAffineTree leafCheck topology payloads 2 A1294Source.parentBox = true := by
  unfold checkAffineTree
  rw [replay65]
  rfl
#print axioms replay65
#print axioms accepted_tree
end A1294Combined

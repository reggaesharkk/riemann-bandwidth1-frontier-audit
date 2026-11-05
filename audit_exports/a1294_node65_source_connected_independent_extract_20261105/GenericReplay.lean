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

#print axioms threeNodeReplay
end A1294Combined

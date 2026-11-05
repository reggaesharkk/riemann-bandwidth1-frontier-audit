import CombinedTree
open Zeta23.ThmD.Sextuple
namespace A1294ReplayControls
 theorem extra {α : Type} (check : GapBox → α → Bool) (box : GapBox) (l r : α)
    (hl : check (box.lowerHalf 0) l = true) (hr : check (box.upperHalf 0) r = true) :
    checkAffineTree check (CursorStream.ofList [.split 0,.terminal,.terminal,.terminal])
      (CursorStream.ofList [l,r]) 2 box = false := by
  simp [checkAffineTree, replayAffineTree, hl, hr, CursorStream.ofList]
 theorem truncated {α : Type} (check : GapBox → α → Bool) (box : GapBox) (l r : α)
    (hl : check (box.lowerHalf 0) l = true) :
    checkAffineTree check (CursorStream.ofList [.split 0,.terminal])
      (CursorStream.ofList [l,r]) 2 box = false := by
  simp [checkAffineTree, replayAffineTree, hl, CursorStream.ofList]
 theorem missingPayload {α : Type} (check : GapBox → α → Bool) (box : GapBox) (l : α)
    (hl : check (box.lowerHalf 0) l = true) :
    checkAffineTree check (CursorStream.ofList [.split 0,.terminal,.terminal])
      (CursorStream.ofList [l]) 2 box = false := by
  simp [checkAffineTree, replayAffineTree, hl, CursorStream.ofList]
 theorem reject_extra := extra A1294Combined.leafCheck A1294Source.parentBox
   (.quadratic A1294Combined.leftPayload) (.quadratic A1294Combined.rightPayload)
   A1294Combined.left_check A1294Combined.right_check
 theorem reject_truncated := truncated A1294Combined.leafCheck A1294Source.parentBox
   (.quadratic A1294Combined.leftPayload) (.quadratic A1294Combined.rightPayload) A1294Combined.left_check
 theorem reject_missing := missingPayload A1294Combined.leafCheck A1294Source.parentBox
   (.quadratic A1294Combined.leftPayload) A1294Combined.left_check
 theorem invalid_topology : decodeAffineTreeToken 6 = none := by rfl
 theorem invalid_prefix_kind : A1294Source.locate 1 [0] [2] = none := by rfl
 #print axioms reject_extra
 #print axioms reject_truncated
 #print axioms reject_missing
 #print axioms invalid_prefix_kind
 #print axioms A1294Combined.exact_exhaustion
 #check A1294Combined.source_connected_parent
end A1294ReplayControls

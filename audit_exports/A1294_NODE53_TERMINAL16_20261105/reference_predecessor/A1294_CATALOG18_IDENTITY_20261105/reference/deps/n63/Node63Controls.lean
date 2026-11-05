import Node63Replay
open Zeta23.ThmD.Sextuple
namespace Node63Controls
theorem extra {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b c : α)
    (ha : check (box.lowerHalf 3) a = true)
    (hb : check ((box.upperHalf 3).lowerHalf 0) b = true)
    (hc : check ((box.upperHalf 3).upperHalf 0) c = true) :
    checkAffineTree check (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal,.terminal])
      (CursorStream.ofList [a,b,c]) 3 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb,hc]
  change 5 = 6 → ¬ 3 = 3
  decide
theorem truncated {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b c : α)
    (ha : check (box.lowerHalf 3) a = true)
    (hb : check ((box.upperHalf 3).lowerHalf 0) b = true) :
    checkAffineTree check (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal])
      (CursorStream.ofList [a,b,c]) 3 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb]
theorem missing {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b : α)
    (ha : check (box.lowerHalf 3) a = true)
    (hb : check ((box.upperHalf 3).lowerHalf 0) b = true) :
    checkAffineTree check (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList [a,b]) 3 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb]
-- Source-order rejection is exact literal disagreement, not universal semantic
-- rejection of arbitrary permuted mathematical witnesses by replayAffineTree.
theorem misordered_source : ([4,1,0,0,0] : List Nat) ≠ A1294Source.topologyBytes.drop 63 := by decide
theorem missing_source : ([4,0,1,0] : List Nat) ≠ A1294Source.topologyBytes.drop 63 := by decide
theorem extra_source : ([4,0,1,0,0,0] : List Nat) ≠ A1294Source.topologyBytes.drop 63 := by decide
theorem invalid_topology : decodeAffineTreeToken 6 = none := by rfl
theorem invalid_kind : A1294Source.locate 1 [0] [2] = none := by rfl
theorem right_left_check : A1294Combined.leafCheck ((Source63.parentBox.upperHalf 3).lowerHalf 0)
    (.quadratic A1294Combined.leftPayload) = true := by
  change A1294Combined.leafCheck ((Source63.parentBox.upperHalf (⟨3,by decide⟩ : Fin 5)).lowerHalf 0) _ = true
  rw [Source63.right_box]
  exact A1294Combined.left_check
theorem right_right_check : A1294Combined.leafCheck ((Source63.parentBox.upperHalf 3).upperHalf 0)
    (.quadratic A1294Combined.rightPayload) = true := by
  change A1294Combined.leafCheck ((Source63.parentBox.upperHalf (⟨3,by decide⟩ : Fin 5)).upperHalf 0) _ = true
  rw [Source63.right_box]
  exact A1294Combined.right_check
theorem reject_extra : checkAffineTree A1294Combined.leafCheck
    (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal,.terminal])
    Node63.payloads 3 Source63.parentBox = false :=
  extra _ _ _ _ _ Node63.left_check right_left_check right_right_check
theorem reject_truncated : checkAffineTree A1294Combined.leafCheck
    (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal])
    Node63.payloads 3 Source63.parentBox = false :=
  truncated _ _ _ _ _ Node63.left_check right_left_check
theorem reject_missing : checkAffineTree A1294Combined.leafCheck Node63.topology
    (CursorStream.ofList [.quadratic Node63.payload21,.quadratic A1294Combined.leftPayload])
    3 Source63.parentBox = false :=
  missing _ _ _ _ Node63.left_check right_left_check
#print axioms reject_extra
#print axioms reject_truncated
#print axioms reject_missing
#print axioms misordered_source
#print axioms invalid_kind
end Node63Controls

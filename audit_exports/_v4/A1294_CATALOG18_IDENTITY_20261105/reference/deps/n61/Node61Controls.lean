import Node61Replay
import Node63Controls
open Zeta23.ThmD.Sextuple
namespace Node61Controls
theorem extra {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b c d : α)
    (ha : check (box.lowerHalf 1) a = true)
    (hb : check ((box.upperHalf 1).lowerHalf 3) b = true)
    (hc : check (((box.upperHalf 1).upperHalf 3).lowerHalf 0) c = true)
    (hd : check (((box.upperHalf 1).upperHalf 3).upperHalf 0) d = true) :
    checkAffineTree check (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal,.terminal])
      (CursorStream.ofList [a,b,c,d]) 4 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb,hc,hd]
  change 7 = 8 → ¬ 4 = 4
  decide
theorem truncated {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b c d : α)
    (ha : check (box.lowerHalf 1) a = true)
    (hb : check ((box.upperHalf 1).lowerHalf 3) b = true)
    (hc : check (((box.upperHalf 1).upperHalf 3).lowerHalf 0) c = true) :
    checkAffineTree check (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal])
      (CursorStream.ofList [a,b,c,d]) 4 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb,hc]
theorem missing {α : Type} (check : GapBox → α → Bool) (box : GapBox) (a b c : α)
    (ha : check (box.lowerHalf 1) a = true)
    (hb : check ((box.upperHalf 1).lowerHalf 3) b = true)
    (hc : check (((box.upperHalf 1).upperHalf 3).lowerHalf 0) c = true) :
    checkAffineTree check (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList [a,b,c]) 4 box = false := by
  simp [checkAffineTree,replayAffineTree,ha,hb,hc]
-- Source-order rejection is exact literal disagreement, not universal semantic
-- rejection of arbitrary permuted mathematical witnesses by replayAffineTree.
theorem misordered_source : ([2,4,0,0,1,0,0] : List Nat) ≠ A1294Source.topologyBytes.drop 61 := by decide
theorem missing_source : ([2,0,4,0,1,0] : List Nat) ≠ A1294Source.topologyBytes.drop 61 := by decide
theorem extra_source : ([2,0,4,0,1,0,0,0] : List Nat) ≠ A1294Source.topologyBytes.drop 61 := by decide
theorem invalid_topology : decodeAffineTreeToken 6 = none := by rfl
theorem invalid_kind : A1294Source.locate 1 [0] [2] = none := by rfl
theorem h21 : A1294Combined.leafCheck ((Source61.parentBox.upperHalf 1).lowerHalf 3)
    (.quadratic Node63.payload21) = true := by
  change A1294Combined.leafCheck ((Source61.parentBox.upperHalf (⟨1,by decide⟩ : Fin 5)).lowerHalf 3) _ = true
  rw [Source61.right_box]
  exact Node63.left_check
theorem h22 : A1294Combined.leafCheck (((Source61.parentBox.upperHalf 1).upperHalf 3).lowerHalf 0)
    (.quadratic A1294Combined.leftPayload) = true := by
  change A1294Combined.leafCheck (((Source61.parentBox.upperHalf (⟨1,by decide⟩ : Fin 5)).upperHalf 3).lowerHalf 0) _ = true
  rw [Source61.right_box]
  exact Node63Controls.right_left_check
theorem h23 : A1294Combined.leafCheck (((Source61.parentBox.upperHalf 1).upperHalf 3).upperHalf 0)
    (.quadratic A1294Combined.rightPayload) = true := by
  change A1294Combined.leafCheck (((Source61.parentBox.upperHalf (⟨1,by decide⟩ : Fin 5)).upperHalf 3).upperHalf 0) _ = true
  rw [Source61.right_box]
  exact Node63Controls.right_right_check
theorem reject_extra : checkAffineTree A1294Combined.leafCheck
    (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal,.terminal])
    Node61.payloads 4 Source61.parentBox = false :=
  extra _ _ _ _ _ _ Node61.left_check h21 h22 h23
theorem reject_truncated : checkAffineTree A1294Combined.leafCheck
    (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal])
    Node61.payloads 4 Source61.parentBox = false :=
  truncated _ _ _ _ _ _ Node61.left_check h21 h22
theorem reject_missing : checkAffineTree A1294Combined.leafCheck Node61.topology
    (CursorStream.ofList [.quadratic Node61.payload20,.quadratic Node63.payload21,.quadratic A1294Combined.leftPayload])
    4 Source61.parentBox = false :=
  missing _ _ _ _ _ Node61.left_check h21 h22
#print axioms reject_extra
#print axioms reject_truncated
#print axioms reject_missing
#print axioms misordered_source
#print axioms invalid_kind
end Node61Controls

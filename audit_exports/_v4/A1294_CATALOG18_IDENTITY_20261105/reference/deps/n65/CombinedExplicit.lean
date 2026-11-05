import CombinedHelpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace A1294Combined
set_option maxHeartbeats 400000
theorem replay65 : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox = some (3,2) := by
  change (if leafCheck (A1294Source.parentBox.lowerHalf 0) (.quadratic leftPayload) then
    (if leafCheck (A1294Source.parentBox.upperHalf 0) (.quadratic rightPayload) then some (3,2) else none)
    else none) = some (3,2)
  rw [left_check, right_check]
  rfl
theorem accepted_tree : checkAffineTree leafCheck topology payloads 2 A1294Source.parentBox = true := by
  unfold checkAffineTree
  rw [replay65]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [A1294Source.node65_box, source_topology]
  change (match sourcePayloads 22 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList [.split 0,.terminal,.terminal]) (CursorStream.ofList ps) 2 A1294Source.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
theorem source_connected_parent : BoxPredicate (affineEnergyGoal A B) A1294Source.parentBox := by
  exact tree_sound accepted_tree
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
theorem split_chunk_replay {α : Type} (check : GapBox → α → Bool)
    (ts : CursorStream AffineTreeToken) (ps : CursorStream α) (box : GapBox)
    (axis : Fin 5) (fuel tc pc : Nat) (mid final : Nat × Nat)
    (ht : ts.get? tc = some (.split axis))
    (hl : replayAffineTree check ts ps fuel (tc+1) pc (box.lowerHalf axis) = some mid)
    (hr : replayAffineTree check ts ps fuel mid.1 mid.2 (box.upperHalf axis) = some final) :
    replayAffineTree check ts ps (fuel+1) tc pc box = some final := by
  simp only [replayAffineTree,ht,hl]
  exact hr
#print axioms quadratic_sound
#print axioms combined_sound
#print axioms tree_sound
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_parent
#print axioms split_chunk_replay
#print source_connected_parent
end A1294Combined

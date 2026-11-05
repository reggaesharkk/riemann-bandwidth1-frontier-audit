import Node63Helpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node63
open A1294Combined
theorem left_run : replayAffineTree leafCheck topology payloads 2 1 0
    (Source63.parentBox.lowerHalf 3) = some (2,1) := by
  simp only [replayAffineTree,top1,pay0,left_check,ite_true]
theorem reused_node65_run : replayAffineTree leafCheck topology payloads 2 2 1
    A1294Source.parentBox = some (5,3) := by
  exact ReplayTransport.transport leafCheck A1294Combined.topology topology
    A1294Combined.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 2) (tc := 0) (pc := 0) (a := 3) (b := 2) (box := A1294Source.parentBox) A1294Combined.replay65
theorem right_run : replayAffineTree leafCheck topology payloads 2 2 1
    (Source63.parentBox.upperHalf 3) = some (5,3) := by
  change replayAffineTree leafCheck topology payloads 2 2 1
    (Source63.parentBox.upperHalf (⟨3,by decide⟩ : Fin 5)) = some (5,3)
  rw [Source63.right_box]
  exact reused_node65_run
theorem replay63 : replayAffineTree leafCheck topology payloads 3 0 0 Source63.parentBox = some (5,3) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads Source63.parentBox
    3 2 0 0 (2,1) (5,3) top0 left_run right_run
theorem accepted_tree : checkAffineTree leafCheck topology payloads 3 Source63.parentBox = true := by
  unfold checkAffineTree
  rw [replay63]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [Source63.node63_box,Source63.source_topology]
  change (match sourcePayloads 21 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 3 Source63.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) Source63.parentBox := by
  have h := source_check_accepted
  unfold sourceCheck at h
  rw [Source63.node63_box,Source63.source_topology] at h
  change (match sourcePayloads 21 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 3 Source63.parentBox
    | none => false) = true at h
  rw [source_payloads] at h
  exact A1294Combined.tree_sound h
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 3 0 0 Source63.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
#print axioms reused_node65_run
#print axioms replay63
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_predicate
#print axioms exact_exhaustion
#check source_connected_predicate
#check exact_exhaustion
end Node63

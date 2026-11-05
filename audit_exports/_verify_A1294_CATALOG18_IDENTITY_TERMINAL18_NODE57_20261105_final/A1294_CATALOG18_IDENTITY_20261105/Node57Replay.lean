import Node57Helpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node57
open A1294Combined
theorem left_run : replayAffineTree leafCheck topology payloads 5 1 0
    (Source57.parentBox.lowerHalf 4) = some (2,1) := by
  simp only [replayAffineTree,top1,pay0,left_check,ite_true]
theorem reused_node59_run : replayAffineTree leafCheck topology payloads 5 2 1
    Source59.parentBox = some (11,6) := by
  exact ReplayTransport.transport leafCheck Node59.topology topology
    Node59.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 5) (tc := 0) (pc := 0) (a := 9) (b := 5) (box := Source59.parentBox) Node59.replay59
theorem right_run : replayAffineTree leafCheck topology payloads 5 2 1
    (Source57.parentBox.upperHalf 4) = some (11,6) := by
  change replayAffineTree leafCheck topology payloads 5 2 1
    (Source57.parentBox.upperHalf (⟨4,by decide⟩ : Fin 5)) = some (11,6)
  rw [Source57.right_box]
  exact reused_node59_run
theorem replay57 : replayAffineTree leafCheck topology payloads 6 0 0 Source57.parentBox = some (11,6) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads Source57.parentBox
    4 5 0 0 (2,1) (11,6) top0 left_run right_run
theorem accepted_tree : checkAffineTree leafCheck topology payloads 6 Source57.parentBox = true := by
  unfold checkAffineTree
  rw [replay57]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [Source57.node57_box,Source57.source_topology]
  change (match sourcePayloads 18 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 6 Source57.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) Source57.parentBox := by
  have h := source_check_accepted
  unfold sourceCheck at h
  rw [Source57.node57_box,Source57.source_topology] at h
  change (match sourcePayloads 18 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 6 Source57.parentBox
    | none => false) = true at h
  rw [source_payloads] at h
  exact A1294Combined.tree_sound h
theorem right_predicate : BoxPredicate (affineEnergyGoal A B) (Source57.parentBox.upperHalf (⟨4,by decide⟩ : Fin 5)) := by
  rw [Source57.right_box]
  exact Node59.source_connected_predicate
#print axioms right_predicate
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 6 0 0 Source57.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
#print axioms reused_node59_run
#print axioms replay57
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_predicate
#print axioms exact_exhaustion
#check source_connected_predicate
#check exact_exhaustion
end Node57

import Node59Helpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node59
open A1294Combined
theorem left_run : replayAffineTree leafCheck topology payloads 4 1 0
    (Source59.parentBox.lowerHalf 2) = some (2,1) := by
  simp only [replayAffineTree,top1,pay0,left_check,ite_true]
theorem reused_node61_run : replayAffineTree leafCheck topology payloads 4 2 1
    Source61.parentBox = some (9,5) := by
  exact ReplayTransport.transport leafCheck Node61.topology topology
    Node61.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 4) (tc := 0) (pc := 0) (a := 7) (b := 4) (box := Source61.parentBox) Node61.replay61
theorem right_run : replayAffineTree leafCheck topology payloads 4 2 1
    (Source59.parentBox.upperHalf 2) = some (9,5) := by
  change replayAffineTree leafCheck topology payloads 4 2 1
    (Source59.parentBox.upperHalf (⟨2,by decide⟩ : Fin 5)) = some (9,5)
  rw [Source59.right_box]
  exact reused_node61_run
theorem replay59 : replayAffineTree leafCheck topology payloads 5 0 0 Source59.parentBox = some (9,5) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads Source59.parentBox
    2 4 0 0 (2,1) (9,5) top0 left_run right_run
theorem accepted_tree : checkAffineTree leafCheck topology payloads 5 Source59.parentBox = true := by
  unfold checkAffineTree
  rw [replay59]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [Source59.node59_box,Source59.source_topology]
  change (match sourcePayloads 19 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 5 Source59.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) Source59.parentBox := by
  have h := source_check_accepted
  unfold sourceCheck at h
  rw [Source59.node59_box,Source59.source_topology] at h
  change (match sourcePayloads 19 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 5 Source59.parentBox
    | none => false) = true at h
  rw [source_payloads] at h
  exact A1294Combined.tree_sound h
theorem right_predicate : BoxPredicate (affineEnergyGoal A B) (Source59.parentBox.upperHalf (⟨2,by decide⟩ : Fin 5)) := by
  rw [Source59.right_box]
  exact Node61.source_connected_predicate
#print axioms right_predicate
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 5 0 0 Source59.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
#print axioms reused_node61_run
#print axioms replay59
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_predicate
#print axioms exact_exhaustion
#check source_connected_predicate
#check exact_exhaustion
end Node59

import Node61Helpers
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node61
open A1294Combined
theorem left_run : replayAffineTree leafCheck topology payloads 3 1 0
    (Source61.parentBox.lowerHalf 1) = some (2,1) := by
  simp only [replayAffineTree,top1,pay0,left_check,ite_true]
theorem reused_node63_run : replayAffineTree leafCheck topology payloads 3 2 1
    Source63.parentBox = some (7,4) := by
  exact ReplayTransport.transport leafCheck Node63.topology topology
    Node63.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 3) (tc := 0) (pc := 0) (a := 5) (b := 3) (box := Source63.parentBox) Node63.replay63
theorem right_run : replayAffineTree leafCheck topology payloads 3 2 1
    (Source61.parentBox.upperHalf 1) = some (7,4) := by
  change replayAffineTree leafCheck topology payloads 3 2 1
    (Source61.parentBox.upperHalf (⟨1,by decide⟩ : Fin 5)) = some (7,4)
  rw [Source61.right_box]
  exact reused_node63_run
theorem replay61 : replayAffineTree leafCheck topology payloads 4 0 0 Source61.parentBox = some (7,4) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads Source61.parentBox
    1 3 0 0 (2,1) (7,4) top0 left_run right_run
theorem accepted_tree : checkAffineTree leafCheck topology payloads 4 Source61.parentBox = true := by
  unfold checkAffineTree
  rw [replay61]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [Source61.node61_box,Source61.source_topology]
  change (match sourcePayloads 20 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 4 Source61.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) Source61.parentBox := by
  have h := source_check_accepted
  unfold sourceCheck at h
  rw [Source61.node61_box,Source61.source_topology] at h
  change (match sourcePayloads 20 with
    | some ps => checkAffineTree leafCheck
      (CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
      (CursorStream.ofList ps) 4 Source61.parentBox
    | none => false) = true at h
  rw [source_payloads] at h
  exact A1294Combined.tree_sound h
theorem right_predicate : BoxPredicate (affineEnergyGoal A B) (Source61.parentBox.upperHalf (⟨1,by decide⟩ : Fin 5)) := by
  rw [Source61.right_box]
  exact Node63.source_connected_predicate
#print axioms right_predicate
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 4 0 0 Source61.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
#print axioms reused_node63_run
#print axioms replay61
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_predicate
#print axioms exact_exhaustion
#check source_connected_predicate
#check exact_exhaustion
end Node61

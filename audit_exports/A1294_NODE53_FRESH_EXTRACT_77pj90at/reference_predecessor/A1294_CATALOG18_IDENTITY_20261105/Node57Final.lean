import Node57Replay
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact A1294Combined
namespace Node57Final

theorem cursor_counts : Node57.topology.length = 11 ∧ Node57.payloads.length = 6 := by
  have h : (11, 6) = (Node57.topology.length, Node57.payloads.length) :=
    Option.some.inj (Node57.replay57.symm.trans Node57.exact_exhaustion)
  constructor
  · exact (congrArg Prod.fst h).symm
  · exact (congrArg Prod.snd h).symm

theorem numeric_replay : replayAffineTree leafCheck Node57.topology Node57.payloads 6 0 0 Source57.parentBox = some (11, 6) := Node57.replay57

theorem exact_replay_exhaustion : replayAffineTree leafCheck Node57.topology Node57.payloads 6 0 0 Source57.parentBox = some (Node57.topology.length, Node57.payloads.length) := Node57.exact_exhaustion

#check Node57.source_connected_predicate
#check Node57.replay57
#check Node57.exact_exhaustion
#print axioms cursor_counts
#print axioms numeric_replay
#print axioms exact_replay_exhaustion
#print axioms Node57.source_connected_predicate
end Node57Final


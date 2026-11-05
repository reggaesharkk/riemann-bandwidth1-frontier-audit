import Terminal17Compositional
import Node57Replay
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node55
open A1294Source A1294Combined

def payload17 : Payload := ⟨AuthenticCompact17.catalog, [0,0,0,0,0], List.ofFn AuthenticCompact17.rows⟩
def parentBox : GapBox := A1294Source.box38

theorem left_box : parentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) = AuthenticCompact17.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, parentBox, A1294Source.box38,
        AuthenticCompact17.box, Function.update_apply] <;> norm_num <;> decide

theorem right_box : parentBox.upperHalf (⟨0, by decide⟩ : Fin 5) = Source57.parentBox := by
  exact A1294Source.checkpoint38

theorem left_check : leafCheck (parentBox.lowerHalf 0) (.quadratic payload17) = true := by
  change leafCheck (parentBox.lowerHalf (⟨0, by decide⟩ : Fin 5)) (.quadratic payload17) = true
  rw [left_box]
  simp only [leafCheck, affineLeafCheck, quadraticCheck, payload17, decodeRows_ofFn, decodeAnchor_zero]
  exact AuthenticCompact17.accepted

def topology : CursorStream AffineTreeToken := CursorStream.ofList
  [.split 0, .terminal, .split 4, .terminal, .split 2, .terminal, .split 1, .terminal,
   .split 3, .terminal, .split 0, .terminal, .terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload17, .quadratic Node57.payload18, .quadratic Node59.payload19,
   .quadratic Node61.payload20, .quadratic Node63.payload21,
   .quadratic A1294Combined.leftPayload, .quadratic A1294Combined.rightPayload]

theorem top0 : topology.get? 0 = some (.split 0) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload17) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = Node57.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology, Node57.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = Node57.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads, Node57.payloads]

theorem left_run : replayAffineTree leafCheck topology payloads 6 1 0
    (parentBox.lowerHalf 0) = some (2,1) := by
  simp only [replayAffineTree, top1, pay0, left_check, ite_true]

theorem reused_node57_run : replayAffineTree leafCheck topology payloads 6 2 1
    Source57.parentBox = some (13,7) := by
  exact ReplayTransport.transport leafCheck Node57.topology topology
    Node57.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 6) (tc := 0) (pc := 0) (a := 11) (b := 6) (box := Source57.parentBox) Node57.replay57

theorem right_run : replayAffineTree leafCheck topology payloads 6 2 1
    (parentBox.upperHalf (⟨0, by decide⟩ : Fin 5)) = some (13,7) := by
  rw [right_box]
  exact reused_node57_run

theorem replay55 : replayAffineTree leafCheck topology payloads 7 0 0 parentBox = some (13,7) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads parentBox
    0 6 0 0 (2,1) (13,7) top0 left_run right_run

theorem accepted_tree : checkAffineTree leafCheck topology payloads 7 parentBox = true := by
  unfold checkAffineTree
  rw [replay55]
  rfl

theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 7 0 0 parentBox =
    some (topology.length, payloads.length) := checkAffineTree_exact_exhaustion accepted_tree

def sourcePath55 : Path := Source57.path.take 38
def typedPath55 : List (Fin 5 × Bool) := Source57.typedPath.take 38
theorem locate55 : locate 55 topologyBytes kindBytes = some (sourcePath55,17) := by decide
theorem typed_path55 : decodePath sourcePath55 = some typedPath55 := by rfl
theorem source_path55 : walk (initialGapBox 60) typedPath55 = A1294Source.box38 := by
  change walk A1294Source.box0 typedPath55 = A1294Source.box38
  simp only [typedPath55, Source57.typedPath, List.take, walk]
  rw [A1294Source.checkpoint0, A1294Source.checkpoint1, A1294Source.checkpoint2,
    A1294Source.checkpoint3, A1294Source.checkpoint4, A1294Source.checkpoint5,
    A1294Source.checkpoint6, A1294Source.checkpoint7, A1294Source.checkpoint8,
    A1294Source.checkpoint9, A1294Source.checkpoint10, A1294Source.checkpoint11,
    A1294Source.checkpoint12, A1294Source.checkpoint13, A1294Source.checkpoint14,
    A1294Source.checkpoint15, A1294Source.checkpoint16, A1294Source.checkpoint17,
    A1294Source.checkpoint18, A1294Source.checkpoint19, A1294Source.checkpoint20,
    A1294Source.checkpoint21, A1294Source.checkpoint22, A1294Source.checkpoint23,
    A1294Source.checkpoint24, A1294Source.checkpoint25, A1294Source.checkpoint26,
    A1294Source.checkpoint27, A1294Source.checkpoint28, A1294Source.checkpoint29,
    A1294Source.checkpoint30, A1294Source.checkpoint31, A1294Source.checkpoint32,
    A1294Source.checkpoint33, A1294Source.checkpoint34, A1294Source.checkpoint35,
    A1294Source.checkpoint36, A1294Source.checkpoint37]
theorem source_node55_box : sourceBoxAt 55 = some (A1294Source.box38,17) := by
  unfold sourceBoxAt
  rw [locate55]
  change (decodePath sourcePath55).bind (fun typed => some (walk (initialGapBox 60) typed,17)) = _
  rw [typed_path55]
  change some (walk (initialGapBox 60) typedPath55,17) = _
  rw [source_path55]

theorem source_topology55 : (topologyBytes.drop 55).mapM decodeAffineTreeToken =
    some [.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,
      .split 3,.terminal,.split 0,.terminal,.terminal] := by rfl
theorem source_kind_anchor17 : (kindBytes[17]?, (List.range 5).mapM (anchorCode 17)) =
    (some 1, some [0,0,0,0,0]) := by rfl

def witness55 : Nat → Option Payload
  | 17 => some payload17
  | 18 => some Node57.payload18
  | 19 => some Node59.payload19
  | 20 => some Node61.payload20
  | 21 => some Node63.payload21
  | 22 => some A1294Combined.leftPayload
  | 23 => some A1294Combined.rightPayload
  | _ => none
def sourcePayloads55 (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 7).mapM fun offset => do
    let p ← witness55 (cursor+offset)
    let kind ← kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads55 : sourcePayloads55 17 = some
    [.quadratic payload17, .quadratic Node57.payload18, .quadratic Node59.payload19,
     .quadratic Node61.payload20, .quadratic Node63.payload21,
     .quadratic A1294Combined.leftPayload, .quadratic A1294Combined.rightPayload] := by rfl

def sourceCheck : Bool :=
  match sourceBoxAt 55, (topologyBytes.drop 55).mapM decodeAffineTreeToken with
  | some (box,cursor), some tokens =>
    match sourcePayloads55 cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 7 box
    | none => false
  | _,_ => false
theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [source_node55_box, source_topology55]
  change (match sourcePayloads55 17 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList
        [.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,
         .split 3,.terminal,.split 0,.terminal,.terminal]) (CursorStream.ofList ps) 7 parentBox
    | none => false) = true
  rw [source_payloads55]
  exact accepted_tree
theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) parentBox := by
  have h := source_check_accepted
  unfold sourceCheck at h
  rw [source_node55_box, source_topology55] at h
  change (match sourcePayloads55 17 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList
        [.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,
         .split 3,.terminal,.split 0,.terminal,.terminal]) (CursorStream.ofList ps) 7 parentBox
    | none => false) = true at h
  rw [source_payloads55] at h
  exact A1294Combined.tree_sound h

#print left_box
#print replay55
#print exact_exhaustion
#print source_check_accepted
#print source_connected_predicate
#print axioms left_check
#print axioms replay55
#print axioms exact_exhaustion
#print axioms source_node55_box
#print axioms source_connected_predicate
end Node55

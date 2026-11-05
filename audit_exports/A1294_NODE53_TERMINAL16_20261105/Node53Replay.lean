import Terminal16Compositional
import Node55Replay

open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section

namespace Node53
open A1294Source A1294Combined

def payload16 : Payload :=
  ⟨AuthenticCompact16.catalog, [0,0,0,0,0], List.ofFn AuthenticCompact16.rows⟩
def parentBox : GapBox := A1294Source.box37

theorem left_box : parentBox.lowerHalf (⟨3, by decide⟩ : Fin 5) = AuthenticCompact16.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, parentBox, A1294Source.box37,
        AuthenticCompact16.box, Function.update_apply] <;> norm_num <;> decide

theorem right_box : parentBox.upperHalf (⟨3, by decide⟩ : Fin 5) = Node55.parentBox := by
  exact A1294Source.checkpoint37

theorem left_check : leafCheck (parentBox.lowerHalf 3) (.quadratic payload16) = true := by
  change leafCheck (parentBox.lowerHalf (⟨3, by decide⟩ : Fin 5)) (.quadratic payload16) = true
  rw [left_box]
  simp only [leafCheck, affineLeafCheck, quadraticCheck, payload16,
    decodeRows_ofFn, decodeAnchor_zero]
  exact AuthenticCompact16.accepted

def topology : CursorStream AffineTreeToken := CursorStream.ofList
  [.split 3, .terminal, .split 0, .terminal, .split 4, .terminal, .split 2, .terminal,
   .split 1, .terminal, .split 3, .terminal, .split 0, .terminal, .terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload16, .quadratic Node55.payload17, .quadratic Node57.payload18,
   .quadratic Node59.payload19, .quadratic Node61.payload20, .quadratic Node63.payload21,
   .quadratic A1294Combined.leftPayload, .quadratic A1294Combined.rightPayload]

theorem top0 : topology.get? 0 = some (.split 3) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload16) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = Node55.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology, Node55.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = Node55.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads, Node55.payloads]

theorem left_run : replayAffineTree leafCheck topology payloads 7 1 0
    (parentBox.lowerHalf 3) = some (2,1) := by
  simp only [replayAffineTree, top1, pay0, left_check, ite_true]

theorem reused_node55_run : replayAffineTree leafCheck topology payloads 7 2 1
    Node55.parentBox = some (15,8) := by
  exact ReplayTransport.transport leafCheck Node55.topology topology
    Node55.payloads payloads 2 1 topology_offset payload_offset
    (fuel := 7) (tc := 0) (pc := 0) (a := 13) (b := 7) (box := Node55.parentBox)
    Node55.replay55

theorem right_run : replayAffineTree leafCheck topology payloads 7 2 1
    (parentBox.upperHalf (⟨3, by decide⟩ : Fin 5)) = some (15,8) := by
  rw [right_box]
  exact reused_node55_run

theorem replay53 : replayAffineTree leafCheck topology payloads 8 0 0 parentBox = some (15,8) := by
  exact A1294Combined.split_chunk_replay leafCheck topology payloads parentBox
    3 7 0 0 (2,1) (15,8) top0 left_run right_run

theorem accepted_tree : checkAffineTree leafCheck topology payloads 8 parentBox = true := by
  unfold checkAffineTree
  rw [replay53]
  rfl

theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 8 0 0 parentBox =
    some (topology.length, payloads.length) := checkAffineTree_exact_exhaustion accepted_tree

theorem exact_lengths : topology.length = 15 ∧ payloads.length = 8 := by
  constructor <;> rfl

def sourcePath53 : Path := Source57.path.take 37
def typedPath53 : List (Fin 5 × Bool) := Source57.typedPath.take 37
theorem locate53 : locate 53 topologyBytes kindBytes = some (sourcePath53,16) := by decide
theorem typed_path53 : decodePath sourcePath53 = some typedPath53 := by rfl
theorem source_path53 : walk (initialGapBox 60) typedPath53 = A1294Source.box37 := by
  change walk A1294Source.box0 typedPath53 = A1294Source.box37
  simp only [typedPath53, Source57.typedPath, List.take, walk]
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
    A1294Source.checkpoint36]

theorem source_node53_box : sourceBoxAt 53 = some (A1294Source.box37,16) := by
  unfold sourceBoxAt
  rw [locate53]
  change (decodePath sourcePath53).bind
    (fun typed => some (walk (initialGapBox 60) typed,16)) = _
  rw [typed_path53]
  change some (walk (initialGapBox 60) typedPath53,16) = _
  rw [source_path53]

theorem source_topology_bytes53 : topologyBytes.drop 53 =
    [4,0,1,0,5,0,3,0,2,0,4,0,1,0,0] := by rfl

theorem source_topology53 : (topologyBytes.drop 53).mapM decodeAffineTreeToken =
    some [.split 3,.terminal,.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,
      .split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal] := by rfl

theorem source_kind_anchor16 : (kindBytes[16]?, (List.range 5).mapM (anchorCode 16)) =
    (some 1, some [0,0,0,0,0]) := by rfl

def witness53 : Nat → Option Payload
  | 16 => some payload16
  | 17 => some Node55.payload17
  | 18 => some Node57.payload18
  | 19 => some Node59.payload19
  | 20 => some Node61.payload20
  | 21 => some Node63.payload21
  | 22 => some A1294Combined.leftPayload
  | 23 => some A1294Combined.rightPayload
  | _ => none

def sourcePayloads53 (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 8).mapM fun offset => do
    let p ← witness53 (cursor+offset)
    let kind ← kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none

theorem source_payloads53 : sourcePayloads53 16 = some
    [.quadratic payload16, .quadratic Node55.payload17, .quadratic Node57.payload18,
     .quadratic Node59.payload19, .quadratic Node61.payload20, .quadratic Node63.payload21,
     .quadratic A1294Combined.leftPayload, .quadratic A1294Combined.rightPayload] := by rfl

def sourceCheck53 : Bool :=
  match sourceBoxAt 53, (topologyBytes.drop 53).mapM decodeAffineTreeToken with
  | some (box,cursor), some tokens =>
    match sourcePayloads53 cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens)
      (CursorStream.ofList ps) 8 box
    | none => false
  | _,_ => false

theorem source_check_accepted : sourceCheck53 = true := by
  unfold sourceCheck53
  rw [source_node53_box, source_topology53]
  change (match sourcePayloads53 16 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList
        [.split 3,.terminal,.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,
         .split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
        (CursorStream.ofList ps) 8 parentBox
    | none => false) = true
  rw [source_payloads53]
  exact accepted_tree

theorem source_connected_predicate : BoxPredicate (affineEnergyGoal A B) parentBox := by
  have h := source_check_accepted
  unfold sourceCheck53 at h
  rw [source_node53_box, source_topology53] at h
  change (match sourcePayloads53 16 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList
        [.split 3,.terminal,.split 0,.terminal,.split 4,.terminal,.split 2,.terminal,
         .split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal])
        (CursorStream.ofList ps) 8 parentBox
    | none => false) = true at h
  rw [source_payloads53] at h
  exact A1294Combined.tree_sound h

#print left_box
#print replay53
#print exact_exhaustion
#print source_node53_box
#print source_check_accepted
#print source_connected_predicate
#print axioms left_check
#print axioms replay53
#print axioms exact_exhaustion
#print axioms source_node53_box
#print axioms source_connected_predicate

end Node53

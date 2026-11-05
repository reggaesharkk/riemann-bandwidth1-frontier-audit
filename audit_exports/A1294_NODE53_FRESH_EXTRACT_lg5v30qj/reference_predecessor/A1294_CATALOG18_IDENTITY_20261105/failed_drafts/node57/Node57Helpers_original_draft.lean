import Terminal18
import Source57
import Node59Replay
import ReplayTransport
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node57
open A1294Combined
def payload18 : Payload := ⟨AuthenticCompact18.catalog,[0,0,0,0,0],List.ofFn AuthenticCompact18.rows⟩
theorem left_box : Source57.parentBox.lowerHalf (⟨4,by decide⟩ : Fin 5) = AuthenticCompact18.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, Source57.parentBox,
        A1294Source.box39, AuthenticCompact18.box, Function.update_apply] <;> norm_num <;> decide
theorem left_check : leafCheck (Source57.parentBox.lowerHalf 4) (.quadratic payload18) = true := by
  change leafCheck (Source57.parentBox.lowerHalf (⟨4,by decide⟩ : Fin 5)) (.quadratic payload18) = true
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,payload18,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompact18.accepted
def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 4,.terminal,.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload18,.quadratic Node59.payload19,.quadratic Node61.payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload]
theorem top0 : topology.get? 0 = some (.split 4) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload18) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = Node59.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology,Node59.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = Node59.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads,Node59.payloads]
def witness : Nat → Option Payload
  | 0 => some payload18
  | 1 => some Node59.payload19
  | 2 => some Node61.payload20
  | 3 => some Node63.payload21
  | 4 => some leftPayload
  | 5 => some rightPayload
  | _ => none
def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 6).mapM fun offset => do
    let p ← witness offset
    let kind ← A1294Source.kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads : sourcePayloads 18 = some
    [.quadratic payload18,.quadratic Node59.payload19,.quadratic Node61.payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload] := by rfl
def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 57,
      (A1294Source.topologyBytes.drop 57).mapM decodeAffineTreeToken with
  | some (box,cursor),some tokens =>
    match sourcePayloads cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 6 box
    | none => false
  | _,_ => false
#print axioms left_check
#print axioms topology_offset
#print axioms payload_offset
end Node57

import Terminal20
import Source61
import Node63Replay
import ReplayTransport
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node61
open A1294Combined
def payload20 : Payload := ⟨AuthenticCompact20.catalog,[0,0,0,0,0],List.ofFn AuthenticCompact20.rows⟩
theorem left_box : Source61.parentBox.lowerHalf (⟨1,by decide⟩ : Fin 5) = AuthenticCompact20.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, Source61.parentBox,
        A1294Source.box41, AuthenticCompact20.box, Function.update_apply] <;> norm_num <;> decide
theorem left_check : leafCheck (Source61.parentBox.lowerHalf 1) (.quadratic payload20) = true := by
  change leafCheck (Source61.parentBox.lowerHalf (⟨1,by decide⟩ : Fin 5)) (.quadratic payload20) = true
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,payload20,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompact20.accepted
def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload]
theorem top0 : topology.get? 0 = some (.split 1) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload20) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = Node63.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology,Node63.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = Node63.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads,Node63.payloads]
def witness : Nat → Option Payload
  | 0 => some payload20
  | 1 => some Node63.payload21
  | 2 => some leftPayload
  | 3 => some rightPayload
  | _ => none
def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 4).mapM fun offset => do
    let p ← witness offset
    let kind ← A1294Source.kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads : sourcePayloads 20 = some
    [.quadratic payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload] := by rfl
def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 61,
      (A1294Source.topologyBytes.drop 61).mapM decodeAffineTreeToken with
  | some (box,cursor),some tokens =>
    match sourcePayloads cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 4 box
    | none => false
  | _,_ => false
#print axioms left_check
#print axioms topology_offset
#print axioms payload_offset
end Node61

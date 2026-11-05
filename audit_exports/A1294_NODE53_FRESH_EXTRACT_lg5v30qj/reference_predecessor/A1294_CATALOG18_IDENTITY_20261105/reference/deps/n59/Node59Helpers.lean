import Terminal19
import Source59
import Node61Replay
import ReplayTransport
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node59
open A1294Combined
theorem decode_anchor : decodeAnchor AuthenticCompact19.box [0,0,16384,0,0] = some AuthenticCompact19.anchor := by
  simp only [decodeAnchor]
  norm_num
  congr 1
  funext i
  fin_cases i <;> norm_num [AuthenticCompact19.anchor, AuthenticCompact19.box]
def payload19 : Payload := ⟨AuthenticCompact19.catalog,[0,0,16384,0,0],List.ofFn AuthenticCompact19.rows⟩
theorem left_box : Source59.parentBox.lowerHalf (⟨2,by decide⟩ : Fin 5) = AuthenticCompact19.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, Source59.parentBox,
        A1294Source.box40, AuthenticCompact19.box, Function.update_apply] <;> norm_num <;> decide
theorem left_check : leafCheck (Source59.parentBox.lowerHalf 2) (.quadratic payload19) = true := by
  change leafCheck (Source59.parentBox.lowerHalf (⟨2,by decide⟩ : Fin 5)) (.quadratic payload19) = true
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,payload19,decodeRows_ofFn,decode_anchor]
  exact AuthenticCompact19.accepted
def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 2,.terminal,.split 1,.terminal,.split 3,.terminal,.split 0,.terminal,.terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload19,.quadratic Node61.payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload]
theorem top0 : topology.get? 0 = some (.split 2) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload19) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = Node61.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology,Node61.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = Node61.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads,Node61.payloads]
def witness : Nat → Option Payload
  | 0 => some payload19
  | 1 => some Node61.payload20
  | 2 => some Node63.payload21
  | 3 => some leftPayload
  | 4 => some rightPayload
  | _ => none
def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 5).mapM fun offset => do
    let p ← witness offset
    let kind ← A1294Source.kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads : sourcePayloads 19 = some
    [.quadratic payload19,.quadratic Node61.payload20,.quadratic Node63.payload21,.quadratic leftPayload,.quadratic rightPayload] := by rfl
def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 59,
      (A1294Source.topologyBytes.drop 59).mapM decodeAffineTreeToken with
  | some (box,cursor),some tokens =>
    match sourcePayloads cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 5 box
    | none => false
  | _,_ => false
#print axioms left_check
#print axioms topology_offset
#print axioms payload_offset
end Node59

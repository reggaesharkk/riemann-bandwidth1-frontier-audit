import Terminal21
import Source63
import CombinedTree
import ReplayTransport
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace Node63
open A1294Combined
def payload21 : Payload := ⟨AuthenticCompact21.catalog,[0,0,0,0,0],List.ofFn AuthenticCompact21.rows⟩
theorem left_box : Source63.parentBox.lowerHalf (⟨3,by decide⟩ : Fin 5) = AuthenticCompact21.box := by
  apply A1294Source.box_ext
  all_goals
    intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, GapBox.midpoint, Source63.parentBox,
        A1294Source.box42, AuthenticCompact21.box, Function.update_apply] <;> norm_num <;> decide
theorem left_check : leafCheck (Source63.parentBox.lowerHalf 3) (.quadratic payload21) = true := by
  change leafCheck (Source63.parentBox.lowerHalf (⟨3,by decide⟩ : Fin 5)) (.quadratic payload21) = true
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,payload21,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompact21.accepted
def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 3,.terminal,.split 0,.terminal,.terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList
  [.quadratic payload21,.quadratic leftPayload,.quadratic rightPayload]
theorem top0 : topology.get? 0 = some (.split 3) := by rfl
theorem top1 : topology.get? 1 = some .terminal := by rfl
theorem pay0 : payloads.get? 0 = some (.quadratic payload21) := by rfl
theorem topology_offset : ∀ i, topology.get? (2+i) = A1294Combined.topology.get? i := by
  intro i
  rw [show 2+i=i+2 by omega]
  simp [topology,A1294Combined.topology]
theorem payload_offset : ∀ i, payloads.get? (1+i) = A1294Combined.payloads.get? i := by
  intro i
  rw [show 1+i=i+1 by omega]
  simp [payloads,A1294Combined.payloads]
def witness : Nat → Option Payload
  | 0 => some payload21
  | 1 => some leftPayload
  | 2 => some rightPayload
  | _ => none
def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 3).mapM fun offset => do
    let p ← witness offset
    let kind ← A1294Source.kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads : sourcePayloads 21 = some
    [.quadratic payload21,.quadratic leftPayload,.quadratic rightPayload] := by rfl
def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 63,
      (A1294Source.topologyBytes.drop 63).mapM decodeAffineTreeToken with
  | some (box,cursor),some tokens =>
    match sourcePayloads cursor with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 3 box
    | none => false
  | _,_ => false
#print axioms left_check
#print axioms topology_offset
#print axioms payload_offset
end Node63

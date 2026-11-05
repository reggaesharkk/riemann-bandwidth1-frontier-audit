import SourceNode65
import Zeta23.ThmD.Sextuple.CompositionalRight
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
noncomputable section
namespace A1294Combined
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
structure Payload where
  catalog : Array Zeta23.ThmD.Sextuple.MacroPrototype.MacroPiece
  codes : List Nat
  rows : List CompactRow
def decodeRows (xs : List CompactRow) : Option (Fin 15 → CompactRow) :=
  if h : xs.length = 15 then some (fun p => xs[p.val]'(by omega)) else none
def decodeAnchor (box : GapBox) (codes : List Nat) : Option (Fin 5 → ℚ) :=
  if h : codes.length = 5 then
    if codes.all (fun k => decide (k ≤ 16384)) then
      some (fun i => box.lo i + (codes[i.val]'(by omega) : ℚ) / 16384 * (box.hi i-box.lo i))
    else none
  else none
def quadraticCheck (A B : ℚ) (box : GapBox) (payload : Payload) : Bool :=
  match decodeRows payload.rows, decodeAnchor box payload.codes with
  | some rows, some anchor => compactQuadraticLeafCheck payload.catalog A B box anchor rows
  | _, _ => false
theorem quadratic_sound {A B : ℚ} : ∀ box payload,
    quadraticCheck A B box payload = true → BoxPredicate (affineEnergyGoal A B) box := by
  intro box payload hc
  cases hr : decodeRows payload.rows with
  | none => simp [quadraticCheck,hr] at hc
  | some rows =>
    cases ha : decodeAnchor box payload.codes with
    | none => simp [quadraticCheck,hr,ha] at hc
    | some anchor =>
      have h : compactQuadraticLeafCheck payload.catalog A B box anchor rows = true := by
        simpa [quadraticCheck,hr,ha] using hc
      exact compactQuadraticLeafCheck_sound h
theorem combined_sound {A B : ℚ} : ∀ box payload,
    affineLeafCheck A B (quadraticCheck A B) box payload = true →
      BoxPredicate (affineEnergyGoal A B) box :=
  affineLeafCheck_sound quadratic_sound
theorem tree_sound {A B : ℚ} {topology : CursorStream AffineTreeToken}
    {payloads : CursorStream (AffineLeafPayload Payload)} {fuel : Nat} {box : GapBox}
    (h : checkAffineTree (affineLeafCheck A B (quadraticCheck A B)) topology payloads fuel box = true) :
    BoxPredicate (affineEnergyGoal A B) box := checkAffineTree_sound combined_sound h
theorem decodeRows_ofFn (rows : Fin 15 → CompactRow) :
    decodeRows (List.ofFn rows) = some rows := by
  simp only [decodeRows, List.length_ofFn, dite_true]
  congr 1
  funext p
  simp
theorem decodeAnchor_zero (box : GapBox) : decodeAnchor box [0,0,0,0,0] = some box.lo := by
  simp only [decodeAnchor]
  norm_num
  congr 1
  funext i
  fin_cases i <;> simp
theorem reject_bad_row_length (xs : List CompactRow) (h : xs.length ≠ 15) :
    decodeRows xs = none := by simp [decodeRows,h]
theorem reject_bad_anchor_length (xs : List Nat) (box : GapBox) (h : xs.length ≠ 5) :
    decodeAnchor box xs = none := by simp [decodeAnchor,h]
def leftPayload : Payload := ⟨AuthenticCompactLeaf.catalog,[0,0,0,0,0],List.ofFn AuthenticCompactLeaf.rows⟩
def rightPayload : Payload := ⟨AuthenticCompactRight.catalog,[0,0,0,0,0],List.ofFn AuthenticCompactRight.rows⟩
abbrev A : ℚ := 647/50000
abbrev B : ℚ := 1094977/5000000000
abbrev leafCheck := affineLeafCheck A B (quadraticCheck A B)
theorem left_box : A1294Source.parentBox.lowerHalf (⟨0,by decide⟩ : Fin 5) = AuthenticCompactLeaf.box := by
  apply A1294Source.box_ext
  all_goals intro i; fin_cases i <;> norm_num [A1294Source.parentBox,A1294Source.box43,AuthenticCompactLeaf.box,GapBox.lowerHalf,GapBox.midpoint,Function.update] <;> decide
theorem right_box : A1294Source.parentBox.upperHalf (⟨0,by decide⟩ : Fin 5) = AuthenticCompactRight.box := by
  apply A1294Source.box_ext
  all_goals intro i; fin_cases i <;> norm_num [A1294Source.parentBox,A1294Source.box43,AuthenticCompactRight.box,GapBox.upperHalf,GapBox.midpoint,Function.update] <;> decide
theorem left_check : leafCheck (A1294Source.parentBox.lowerHalf 0) (.quadratic leftPayload) = true := by
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,leftPayload,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompactLeaf.accepted
theorem right_check : leafCheck (A1294Source.parentBox.upperHalf 0) (.quadratic rightPayload) = true := by
  rw [right_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,rightPayload,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompactRight.accepted
def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 0,.terminal,.terminal]
def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList [.quadratic leftPayload,.quadratic rightPayload]
theorem source_topology : (A1294Source.topologyBytes.drop 65).mapM decodeAffineTreeToken =
    some [.split 0,.terminal,.terminal] := by rw [A1294Source.subtree_bytes]; rfl
def witness : Nat → Option Payload
  | 0 => some leftPayload
  | 1 => some rightPayload
  | _ => none
def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 2).mapM fun local => do
    let p ← witness local
    let kind ← A1294Source.kindBytes[cursor+local]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+local))
      return .quadratic {p with codes := codes}
    else none
theorem source_payloads : sourcePayloads 22 = some [.quadratic leftPayload,.quadratic rightPayload] := by rfl
def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 65,
        (A1294Source.topologyBytes.drop 65).mapM decodeAffineTreeToken with
  | some (box,cursor), some tokens =>
      match sourcePayloads cursor with
      | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 2 box
      | none => false
  | _,_ => false
theorem replay65 : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox = some (3,2) := by
  simp [replayAffineTree,topology,payloads,left_check,right_check]
theorem accepted_tree : checkAffineTree leafCheck topology payloads 2 A1294Source.parentBox = true := by
  unfold checkAffineTree
  rw [replay65]
  rfl
theorem source_check_accepted : sourceCheck = true := by
  simpa only [sourceCheck,A1294Source.node65_box,source_topology,source_payloads,topology,payloads] using accepted_tree
theorem source_connected_parent : BoxPredicate (affineEnergyGoal A B) A1294Source.parentBox := by
  have h := source_check_accepted
  simp only [sourceCheck,A1294Source.node65_box,source_topology,source_payloads] at h
  exact tree_sound h
theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
theorem reject_extra_topology : checkAffineTree leafCheck
    (CursorStream.ofList [.split 0,.terminal,.terminal,.terminal]) payloads 2 A1294Source.parentBox = false := by
  simp [checkAffineTree,replayAffineTree,payloads,left_check,right_check]
theorem reject_truncated_topology : checkAffineTree leafCheck
    (CursorStream.ofList [.split 0,.terminal]) payloads 2 A1294Source.parentBox = false := by
  simp [checkAffineTree,replayAffineTree,payloads,left_check,right_check]
theorem reject_invalid_token : decodeAffineTreeToken 6 = none := by rfl
theorem split_chunk_replay {α : Type} (check : GapBox → α → Bool)
    (ts : CursorStream AffineTreeToken) (ps : CursorStream α) (box : GapBox)
    (axis : Fin 5) (fuel tc pc : Nat) (mid final : Nat × Nat)
    (ht : ts.get? tc = some (.split axis))
    (hl : replayAffineTree check ts ps fuel (tc+1) pc (box.lowerHalf axis) = some mid)
    (hr : replayAffineTree check ts ps fuel mid.1 mid.2 (box.upperHalf axis) = some final) :
    replayAffineTree check ts ps (fuel+1) tc pc box = some final := by
  simp only [replayAffineTree,ht,hl]
  exact hr
#print axioms quadratic_sound
#print axioms combined_sound
#print axioms tree_sound
#print axioms accepted_tree
#print axioms source_check_accepted
#print axioms source_connected_parent
#print axioms split_chunk_replay
#print source_connected_parent
end A1294Combined

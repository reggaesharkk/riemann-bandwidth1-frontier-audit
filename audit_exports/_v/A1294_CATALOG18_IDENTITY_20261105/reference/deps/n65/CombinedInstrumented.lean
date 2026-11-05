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
#check decodeRows

def decodeAnchor (box : GapBox) (codes : List Nat) : Option (Fin 5 → ℚ) :=
  if h : codes.length = 5 then
    if codes.all (fun k => decide (k ≤ 16384)) then
      some (fun i => box.lo i + (codes[i.val]'(by omega) : ℚ) / 16384 * (box.hi i-box.lo i))
    else none
  else none
#check decodeAnchor

def quadraticCheck (A B : ℚ) (box : GapBox) (payload : Payload) : Bool :=
  match decodeRows payload.rows, decodeAnchor box payload.codes with
  | some rows, some anchor => compactQuadraticLeafCheck payload.catalog A B box anchor rows
  | _, _ => false
#check quadraticCheck

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
#check quadratic_sound

theorem combined_sound {A B : ℚ} : ∀ box payload,
    affineLeafCheck A B (quadraticCheck A B) box payload = true →
      BoxPredicate (affineEnergyGoal A B) box :=
  affineLeafCheck_sound quadratic_sound
#check combined_sound

theorem tree_sound {A B : ℚ} {topology : CursorStream AffineTreeToken}
    {payloads : CursorStream (AffineLeafPayload Payload)} {fuel : Nat} {box : GapBox}
    (h : checkAffineTree (affineLeafCheck A B (quadraticCheck A B)) topology payloads fuel box = true) :
    BoxPredicate (affineEnergyGoal A B) box := checkAffineTree_sound combined_sound h
#check tree_sound

theorem decodeRows_ofFn (rows : Fin 15 → CompactRow) :
    decodeRows (List.ofFn rows) = some rows := by
  simp only [decodeRows, List.length_ofFn, dite_true]
  congr 1
  funext p
  fin_cases p <;> rfl
#check decodeRows_ofFn

theorem decodeAnchor_zero (box : GapBox) : decodeAnchor box [0,0,0,0,0] = some box.lo := by
  simp only [decodeAnchor]
  norm_num
  congr 1
  funext i
  fin_cases i <;> simp
#check decodeAnchor_zero

theorem reject_bad_row_length (xs : List CompactRow) (h : xs.length ≠ 15) :
    decodeRows xs = none := by simp [decodeRows,h]
#check reject_bad_row_length

theorem reject_bad_anchor_length (xs : List Nat) (box : GapBox) (h : xs.length ≠ 5) :
    decodeAnchor box xs = none := by simp [decodeAnchor,h]
#check reject_bad_anchor_length

def leftPayload : Payload := ⟨AuthenticCompactLeaf.catalog,[0,0,0,0,0],List.ofFn AuthenticCompactLeaf.rows⟩
#check leftPayload

def rightPayload : Payload := ⟨AuthenticCompactRight.catalog,[0,0,0,0,0],List.ofFn AuthenticCompactRight.rows⟩
#check rightPayload

abbrev A : ℚ := 647/50000
#check A

abbrev B : ℚ := 1094977/5000000000
#check B

abbrev leafCheck := affineLeafCheck A B (quadraticCheck A B)
#check leafCheck

theorem left_box : A1294Source.parentBox.lowerHalf (⟨0,by decide⟩ : Fin 5) = AuthenticCompactLeaf.box := by
  apply A1294Source.box_ext
  all_goals intro i; fin_cases i <;> norm_num [A1294Source.parentBox,A1294Source.box43,AuthenticCompactLeaf.box,GapBox.lowerHalf,GapBox.midpoint,Function.update] <;> decide
#check left_box

theorem right_box : A1294Source.parentBox.upperHalf (⟨0,by decide⟩ : Fin 5) = AuthenticCompactRight.box := by
  apply A1294Source.box_ext
  all_goals intro i; fin_cases i <;> norm_num [A1294Source.parentBox,A1294Source.box43,AuthenticCompactRight.box,GapBox.upperHalf,GapBox.midpoint,Function.update] <;> decide
#check right_box

theorem left_check : leafCheck (A1294Source.parentBox.lowerHalf 0) (.quadratic leftPayload) = true := by
  change leafCheck (A1294Source.parentBox.lowerHalf (⟨0,by decide⟩ : Fin 5)) (.quadratic leftPayload) = true
  rw [left_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,leftPayload,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompactLeaf.accepted
#check left_check

theorem right_check : leafCheck (A1294Source.parentBox.upperHalf 0) (.quadratic rightPayload) = true := by
  change leafCheck (A1294Source.parentBox.upperHalf (⟨0,by decide⟩ : Fin 5)) (.quadratic rightPayload) = true
  rw [right_box]
  simp only [leafCheck,affineLeafCheck,quadraticCheck,rightPayload,decodeRows_ofFn,decodeAnchor_zero]
  exact AuthenticCompactRight.accepted
#check right_check

def topology : CursorStream AffineTreeToken := CursorStream.ofList [.split 0,.terminal,.terminal]
#check topology

def payloads : CursorStream (AffineLeafPayload Payload) := CursorStream.ofList [.quadratic leftPayload,.quadratic rightPayload]
#check payloads

theorem source_topology : (A1294Source.topologyBytes.drop 65).mapM decodeAffineTreeToken =
    some [.split 0,.terminal,.terminal] := by rw [A1294Source.subtree_bytes]; rfl
#check source_topology

def witness : Nat → Option Payload
  | 0 => some leftPayload
  | 1 => some rightPayload
  | _ => none
#check witness

def sourcePayloads (cursor : Nat) : Option (List (AffineLeafPayload Payload)) :=
  (List.range 2).mapM fun offset => do
    let p ← witness offset
    let kind ← A1294Source.kindBytes[cursor+offset]?
    if kind = 0 then return .tail
    else if kind = 1 then
      let codes ← (List.range 5).mapM (A1294Source.anchorCode (cursor+offset))
      return .quadratic {p with codes := codes}
    else none
#check sourcePayloads

theorem source_payloads : sourcePayloads 22 = some [.quadratic leftPayload,.quadratic rightPayload] := by rfl
#check source_payloads

def sourceCheck : Bool :=
  match A1294Source.sourceBoxAt 65,
        (A1294Source.topologyBytes.drop 65).mapM decodeAffineTreeToken with
  | some (box,cursor), some tokens =>
      match sourcePayloads cursor with
      | some ps => checkAffineTree leafCheck (CursorStream.ofList tokens) (CursorStream.ofList ps) 2 box
      | none => false
  | _,_ => false
#check sourceCheck

theorem top0 : topology.get? 0 = some (.split 0) := by rfl
#check top0

theorem top1 : topology.get? 1 = some .terminal := by rfl
#check top1

theorem top2 : topology.get? 2 = some .terminal := by rfl
#check top2

theorem pay0 : payloads.get? 0 = some (.quadratic leftPayload) := by rfl
#check pay0

theorem pay1 : payloads.get? 1 = some (.quadratic rightPayload) := by rfl

#check pay1

theorem replay65 : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox = some (3,2) := by
  simp only [replayAffineTree, top0, top1, top2, pay0, pay1, Nat.reduceAdd, left_check, right_check, Bool.true_eq, ite_true]
#check replay65

theorem accepted_tree : checkAffineTree leafCheck topology payloads 2 A1294Source.parentBox = true := by
  unfold checkAffineTree
  rw [replay65]
  rfl
#check accepted_tree

theorem source_check_accepted : sourceCheck = true := by
  unfold sourceCheck
  rw [A1294Source.node65_box, source_topology]
  change (match sourcePayloads 22 with
    | some ps => checkAffineTree leafCheck (CursorStream.ofList [.split 0,.terminal,.terminal]) (CursorStream.ofList ps) 2 A1294Source.parentBox
    | none => false) = true
  rw [source_payloads]
  exact accepted_tree
#check source_check_accepted

theorem source_connected_parent : BoxPredicate (affineEnergyGoal A B) A1294Source.parentBox := by
  exact tree_sound accepted_tree
#check source_connected_parent

theorem exact_exhaustion : replayAffineTree leafCheck topology payloads 2 0 0 A1294Source.parentBox =
    some (topology.length,payloads.length) := checkAffineTree_exact_exhaustion accepted_tree
#check exact_exhaustion

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

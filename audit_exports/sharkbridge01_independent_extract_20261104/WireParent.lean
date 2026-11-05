import Zeta23.ThmD.Sextuple.A1294CompactParent
open Zeta23.ThmD.Sextuple A1294Compact A1294FifteenBridge
noncomputable section
namespace SharkBridge01
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
structure WireSegment where
  lo : Nat
  hi : Nat
  cat : Nat
inductive WireRow where
  | direct (cat : Nat)
  | floor (q : Nat) (segments : List Nat)
def decodeSeg (qs : Array CompactRat) (ss : Array WireSegment)
    (localRefs : Array (Option Nat)) (i : Nat) : Option CompactSegment := do
  let s ← ss[i]?
  let lo ← qs[s.lo]?
  let hi ← qs[s.hi]?
  let c ← localRefs[s.cat]?
  let c ← c
  return {lo := lo, hi := hi, pieceRef := c}
def decodeRow (qs : Array CompactRat) (ss : Array WireSegment)
    (localRefs : Array (Option Nat)) : WireRow → Option CompactRow
  | .direct i => do
      let c ← localRefs[i]?
      let c ← c
      return .direct c
  | .floor q ids => do
      let v ← qs[q]?
      let segs ← ids.mapM (decodeSeg qs ss localRefs)
      return .floor v segs
def rowOrDefault (r : Option CompactRow) : CompactRow := r.getD (.direct 0)
def qs : Array CompactRat := #[
⟨(0),1⟩,
⟨(105),16⟩,
⟨(255),8⟩,
⟨(405),32⟩,
⟨(405),64⟩,
⟨(647),50000⟩,
⟨(795),128⟩,
⟨(825),64⟩,
⟨(825),128⟩,
⟨(1215),64⟩,
⟨(1245),64⟩,
⟨(1635),64⟩,
⟨(1665),64⟩,
⟨(2085),64⟩,
⟨(2445),128⟩,
⟨(2475),128⟩,
⟨(3255),128⟩,
⟨(3315),128⟩,
⟨(4065),128⟩,
⟨(4155),128⟩,
⟨(8089),1250⟩,
⟨(31731),5000⟩,
⟨(62837),10000⟩,
⟨(64087),10000⟩,
⟨(65337),10000⟩,
⟨(126299),20000⟩,
⟨(127549),20000⟩,
⟨(128799),20000⟩,
⟨(130049),20000⟩,
⟨(160217),6250⟩,
⟨(250723),40000⟩,
⟨(251973),40000⟩,
⟨(253223),40000⟩,
⟨(254473),40000⟩,
⟨(255723),40000⟩,
⟨(256973),40000⟩,
⟨(258223),40000⟩,
⟨(259473),40000⟩,
⟨(260723),40000⟩,
⟨(261973),40000⟩,
⟨(318101),25000⟩,
⟨(323559),12500⟩,
⟨(599371),31250⟩,
⟨(633077),50000⟩,
⟨(637743),25000⟩,
⟨(643993),25000⟩,
⟨(795519),25000⟩,
⟨(1094977),5000000000⟩,
⟨(1269279),100000⟩,
⟨(1272361),50000⟩,
⟨(1275529),100000⟩,
⟨(1278611),50000⟩,
⟨(1284861),50000⟩,
⟨(1291111),50000⟩,
⟨(1297361),50000⟩,
⟨(1587913),50000⟩,
⟨(2381859),125000⟩,
⟨(2413109),125000⟩,
⟨(2535433),200000⟩,
⟨(2541683),200000⟩,
⟨(2547847),100000⟩,
⟨(2547933),200000⟩,
⟨(2554097),100000⟩,
⟨(2560347),100000⟩,
⟨(2566597),100000⟩,
⟨(2572847),100000⟩,
⟨(2579097),100000⟩,
⟨(2585347),100000⟩,
⟨(2591597),100000⟩,
⟨(2597847),100000⟩,
⟨(3178951),100000⟩,
⟨(3185201),100000⟩,
⟨(4748093),250000⟩,
⟨(4779343),250000⟩,
⟨(4810593),250000⟩,
⟨(5086319),200000⟩,
⟨(5092569),200000⟩,
⟨(5098819),200000⟩,
⟨(5105069),200000⟩,
⟨(5111319),200000⟩,
⟨(5117569),200000⟩,
⟨(5123819),200000⟩,
⟨(5130069),200000⟩,
⟨(5136319),200000⟩,
⟨(5142569),200000⟩,
⟨(5148819),200000⟩,
⟨(5155069),200000⟩,
⟨(5161319),200000⟩,
⟨(5167569),200000⟩,
⟨(5173819),200000⟩,
⟨(5180069),200000⟩,
⟨(5186319),200000⟩,
⟨(5192569),200000⟩,
⟨(6354777),200000⟩,
⟨(6361027),200000⟩,
⟨(6367277),200000⟩,
⟨(6373527),200000⟩,
⟨(6448527),200000⟩,
⟨(9511811),500000⟩,
⟨(9543061),500000⟩,
⟨(9574311),500000⟩,
⟨(9605561),500000⟩,
⟨(9636811),500000⟩,
⟨(9668061),500000⟩,
⟨(12755291),1000000⟩,
⟨(19007997),1000000⟩,
⟨(19039247),1000000⟩,
⟨(19070497),1000000⟩,
⟨(19101747),1000000⟩,
⟨(19132997),1000000⟩,
⟨(19164247),1000000⟩,
⟨(19195497),1000000⟩,
⟨(19226747),1000000⟩,
⟨(19257997),1000000⟩,
⟨(19289247),1000000⟩,
⟨(19320497),1000000⟩,
⟨(19351747),1000000⟩,
⟨(245028537159250067459167806169),1250000000000000000000000000000000⟩,
⟨(21287960894909617826490440080249),5000000000000000000000000000000000⟩,
⟨(1755263779336959657910023102330969),7812500000000000000000000000000000000000⟩,
⟨(12892869620170946020955818564495929),50000000000000000000000000000000000000⟩,
⟨(1060756076606974029304872234228987649),5000000000000000000000000000000000000000⟩,
⟨(5170581624709583018970186520240204081),3200000000000000000000000000000000000000⟩,
⟨(6876046637736468087644507155946023489),80000000000000000000000000000000000000000⟩,
⟨(7594713117315031921983662976367761841),80000000000000000000000000000000000000000⟩,
⟨(29727308394007168144031841183195847081),500000000000000000000000000000000000000000⟩]
def segs : Array WireSegment := #[
⟨2,97,6⟩,
⟨3,43,51⟩,
⟨4,32,49⟩,
⟨6,30,3⟩,
⟨8,36,22⟩,
⟨9,72,57⟩,
⟨11,79,94⟩,
⟨14,108,65⟩,
⟨16,75,85⟩,
⟨18,55,38⟩,
⟨20,37,34⟩,
⟨21,33,59⟩,
⟨22,31,10⟩,
⟨23,35,91⟩,
⟨24,39,46⟩,
⟨25,4,49⟩,
⟨26,34,81⟩,
⟨27,8,22⟩,
⟨27,36,22⟩,
⟨28,38,36⟩,
⟨29,82,98⟩,
⟨30,22,9⟩,
⟨31,25,48⟩,
⟨32,21,50⟩,
⟨33,26,70⟩,
⟨34,23,84⟩,
⟨35,27,11⟩,
⟨36,20,33⟩,
⟨37,28,35⟩,
⟨38,24,37⟩,
⟨39,1,47⟩,
⟨40,61,56⟩,
⟨41,17,27⟩,
⟨41,90,27⟩,
⟨42,111,72⟩,
⟨43,58,52⟩,
⟨44,78,92⟩,
⟨45,86,18⟩,
⟨46,95,43⟩,
⟨48,59,54⟩,
⟨49,76,87⟩,
⟨50,104,0⟩,
⟨51,80,96⟩,
⟨52,84,14⟩,
⟨53,88,23⟩,
⟨54,92,31⟩,
⟨55,93,39⟩,
⟨56,107,63⟩,
⟨57,115,80⟩,
⟨58,48,53⟩,
⟨59,40,55⟩,
⟨60,77,89⟩,
⟨61,50,8⟩,
⟨62,79,94⟩,
⟨63,81,4⟩,
⟨64,83,12⟩,
⟨65,85,16⟩,
⟨66,87,20⟩,
⟨67,89,25⟩,
⟨68,91,29⟩,
⟨69,12,5⟩,
⟨70,94,41⟩,
⟨71,96,45⟩,
⟨72,105,58⟩,
⟨73,109,67⟩,
⟨74,113,76⟩,
⟨75,49,86⟩,
⟨76,60,88⟩,
⟨77,44,90⟩,
⟨78,62,93⟩,
⟨79,51,95⟩,
⟨80,63,97⟩,
⟨81,29,4⟩,
⟨82,64,99⟩,
⟨83,52,13⟩,
⟨84,65,15⟩,
⟨85,45,17⟩,
⟨86,66,19⟩,
⟨87,53,21⟩,
⟨88,67,24⟩,
⟨89,41,26⟩,
⟨90,68,28⟩,
⟨91,54,30⟩,
⟨92,69,32⟩,
⟨93,70,40⟩,
⟨94,46,42⟩,
⟨95,71,44⟩,
⟨96,97,6⟩,
⟨97,13,7⟩,
⟨97,19,7⟩,
⟨98,106,61⟩,
⟨99,108,65⟩,
⟨100,110,69⟩,
⟨101,112,74⟩,
⟨102,114,78⟩,
⟨103,116,83⟩,
⟨104,7,1⟩,
⟨105,98,60⟩,
⟨106,56,62⟩,
⟨107,99,64⟩,
⟨108,73,66⟩,
⟨109,100,68⟩,
⟨110,42,71⟩,
⟨111,101,73⟩,
⟨112,74,75⟩,
⟨113,102,77⟩,
⟨114,57,79⟩,
⟨115,15,82⟩,
⟨115,103,82⟩,
⟨116,10,2⟩]
def qAt (i : Nat) : ℚ := interpRat ((qs[i]?).getD ⟨0,1⟩)
def parentBox : GapBox where
  lo := fun i => match i.val with | 0 => qAt 4 | 1 => qAt 8 | 2 => qAt 6 | 3 => qAt 8 | _ => qAt 4
  hi := fun i => match i.val with | 0 => qAt 1 | 1 => qAt 1 | 2 => qAt 4 | 3 => qAt 1 | _ => qAt 1
theorem parentBox_exact : parentBox = A1294CompactParent.sourceParentBox := by
  apply A1294CompactParent.gapBox_ext_exact
  all_goals intro i; fin_cases i <;> norm_num [parentBox, A1294CompactParent.sourceParentBox, qAt, qs, interpRat]

def refs_left : Array (Option Nat) := #[some 87, some 9, some 89, some 96, some 45, some 95, some 71, some 72, some 86, some 97, some 98, some 7, some 48, some 49, some 50, some 51, some 52, some 53, some 54, some 55, some 56, some 57, some 8, some 58, some 59, some 60, some 61, some 62, some 90, some 91, some 92, some 93, some 94, some 73, some 74, some 75, some 76, some 77, some 63, some 64, some 65, some 66, some 67, some 68, some 69, some 70, some 78, some 79, some 99, some 0, some 1, some 80, some 81, some 82, some 83, some 84, some 85, some 10, some 11, some 2, some 12, some 13, some 14, some 15, some 16, some 17, some 18, some 19, some 20, some 21, some 3, some 22, some 23, some 24, some 25, some 26, some 27, some 28, some 29, some 30, some 31, some 4, some 32, some 88, some 5, some 33, some 34, some 35, some 36, some 37, some 38, some 6, some 39, some 40, some 41, some 42, some 43, some 44, some 46, some 47]
def wire_left : Fin 15 → WireRow := fun p => match p.val with | 0 => .floor 122 [2,23,11,24,16,25,13,26,17] | 1 => .direct 1 | 2 => .floor 119 [5,63,97,90,98,47,99,91,100,64,101,92,102,34,103,93,104,65,105,94,106,48,107] | 3 => .floor 123 [8,66,40,67,51,68,36,69,53,70,42,71,54,72,20,73,55,74,43,75,56,76,37,77,57,78,44,79,58,80,32] | 4 => .floor 124 [9,46,84,61,85,38,86,62,87,89] | 5 => .floor 120 [4,27,10,28,19,29,14,30] | 6 => .floor 0 [1,35,49,39,50,31,52,41,96] | 7 => .floor 125 [7,100,64,101,92,102,34,103,93,104,65,105,94,106,48,108,95,109] | 8 => .floor 123 [8,66,40,67,51,68,36,69,53,70,42,71,54,72,20,73,55,74,43,75,56,76,37,77,57,78,44,79,58,80,33,81,59,82,45,83,60] | 9 => .floor 118 [3,21,12,22,15] | 10 => .floor 0 [1,35,49,39,50,31,52,41,96] | 11 => .floor 119 [5,63,97,90,98,47,99,91,100,64,101,92,102,34,103,93,104,65,105,94,106,48,108,95,109] | 12 => .floor 120 [4,27,10,28,19,29,14,30] | 13 => .direct 1 | _ => .floor 120 [2,23,11,24,16,25,13,26,18,27,10,28,19,29,14,30]
def box_left : GapBox where
  lo := fun i => match i.val with | 0 => qAt 4 | 1 => qAt 8 | 2 => qAt 6 | 3 => qAt 8 | _ => qAt 4
  hi := fun i => match i.val with | 0 => qAt 8 | 1 => qAt 1 | 2 => qAt 4 | 3 => qAt 1 | _ => qAt 1
def anchor_left : Fin 5 → ℚ := fun i => match i.val with | 0 => qAt 4 | 1 => qAt 8 | 2 => qAt 6 | 3 => qAt 8 | _ => qAt 4
theorem box_left_exact : box_left = AuthenticCompactLeaf.box := by
  apply A1294CompactParent.gapBox_ext_exact
  all_goals intro i; fin_cases i <;> norm_num [box_left, AuthenticCompactLeaf.box, qAt, qs, interpRat]
theorem anchor_left_exact : anchor_left = AuthenticCompactLeaf.anchor := by
  funext i
  fin_cases i <;> norm_num [anchor_left, AuthenticCompactLeaf.anchor, AuthenticCompactLeaf.box, qAt, qs, interpRat]

theorem decoded_left : ∀ p, decodeRow qs segs refs_left (wire_left p) = some (AuthenticCompactLeaf.rows p) := by
  intro p
  fin_cases p <;> rfl
def rows_left (p : Fin 15) : CompactRow := rowOrDefault (decodeRow qs segs refs_left (wire_left p))
theorem rows_left_exact : rows_left = AuthenticCompactLeaf.rows := by
  funext p
  simp [rows_left, decoded_left, rowOrDefault]
theorem accepted_left : compactQuadraticLeafCheck AuthenticCompactLeaf.catalog (647/50000) (1094977/5000000000) box_left anchor_left rows_left = true := by
  rw [rows_left_exact, box_left_exact, anchor_left_exact]
  exact AuthenticCompactLeaf.accepted
theorem leaf_left : ∀ ⦃g : Fin 5 → ℝ⦄, AuthenticCompactLeaf.box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  compactQuadraticLeafCheck_sound (by simpa only [box_left_exact, anchor_left_exact] using accepted_left)
#print axioms decoded_left
#print axioms accepted_left
#print axioms leaf_left

def refs_right : Array (Option Nat) := #[some 64, some 8, some 26, some 73, some 31, some 54, some 55, some 56, some 63, some 74, some 75, some 91, some 34, some 35, some 36, some 37, some 38, some 39, some 40, some 41, some 42, some 43, some 0, some 44, some 45, some 46, some 47, some 48, some 49, some 50, some 51, some 52, some 53, some 1, some 2, some 3, some 4, some 5, none, none, none, none, none, none, none, none, some 6, some 7, some 76, some 77, some 85, some 57, some 58, some 59, some 60, some 61, some 62, some 78, some 79, some 86, some 80, some 81, some 82, some 83, some 84, some 9, some 10, some 11, some 12, some 13, some 87, some 14, some 15, some 16, some 17, some 18, some 19, some 20, some 21, some 22, some 23, some 88, some 24, some 25, some 89, some 65, some 66, some 67, some 68, some 69, some 70, some 90, some 71, some 72, some 27, some 28, some 29, some 30, some 32, some 33]
def wire_right : Fin 15 → WireRow := fun p => match p.val with | 0 => .floor 120 [4,27,10,28,19,29,14,30] | 1 => .direct 1 | 2 => .floor 125 [7,100,64,101,92,102,34,103,93,104,65,105,94,106,48,108,95,109] | 3 => .floor 121 [6,70,42,71,54,72,20,73,55,74,43,75,56,76,37,77,57,78,44,79,58,80,33,81,59,82,45,83,60] | 4 => .floor 117 [0,88] | 5 => .floor 120 [4,27,10,28,19,29,14,30] | 6 => .floor 0 [1,35,49,39,50,31,52,41,96] | 7 => .floor 125 [7,100,64,101,92,102,34,103,93,104,65,105,94,106,48,108,95,109] | 8 => .floor 123 [8,66,40,67,51,68,36,69,53,70,42,71,54,72,20,73,55,74,43,75,56,76,37,77,57,78,44,79,58,80,33,81,59,82,45,83,60] | 9 => .floor 118 [3,21,12,22,15] | 10 => .floor 0 [1,35,49,39,50,31,52,41,96] | 11 => .floor 119 [5,63,97,90,98,47,99,91,100,64,101,92,102,34,103,93,104,65,105,94,106,48,108,95,109] | 12 => .floor 120 [4,27,10,28,19,29,14,30] | 13 => .direct 1 | _ => .floor 120 [2,23,11,24,16,25,13,26,18,27,10,28,19,29,14,30]
def box_right : GapBox where
  lo := fun i => match i.val with | 0 => qAt 8 | 1 => qAt 8 | 2 => qAt 6 | 3 => qAt 8 | _ => qAt 4
  hi := fun i => match i.val with | 0 => qAt 1 | 1 => qAt 1 | 2 => qAt 4 | 3 => qAt 1 | _ => qAt 1
def anchor_right : Fin 5 → ℚ := fun i => match i.val with | 0 => qAt 8 | 1 => qAt 8 | 2 => qAt 6 | 3 => qAt 8 | _ => qAt 4
theorem box_right_exact : box_right = AuthenticCompactRight.box := by
  apply A1294CompactParent.gapBox_ext_exact
  all_goals intro i; fin_cases i <;> norm_num [box_right, AuthenticCompactRight.box, qAt, qs, interpRat]
theorem anchor_right_exact : anchor_right = AuthenticCompactRight.anchor := by
  funext i
  fin_cases i <;> norm_num [anchor_right, AuthenticCompactRight.anchor, AuthenticCompactRight.box, qAt, qs, interpRat]

theorem decoded_right : ∀ p, decodeRow qs segs refs_right (wire_right p) = some (AuthenticCompactRight.rows p) := by
  intro p
  fin_cases p <;> rfl
def rows_right (p : Fin 15) : CompactRow := rowOrDefault (decodeRow qs segs refs_right (wire_right p))
theorem rows_right_exact : rows_right = AuthenticCompactRight.rows := by
  funext p
  simp [rows_right, decoded_right, rowOrDefault]
theorem accepted_right : compactQuadraticLeafCheck AuthenticCompactRight.catalog (647/50000) (1094977/5000000000) box_right anchor_right rows_right = true := by
  rw [rows_right_exact, box_right_exact, anchor_right_exact]
  exact AuthenticCompactRight.accepted
theorem leaf_right : ∀ ⦃g : Fin 5 → ℝ⦄, AuthenticCompactRight.box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  compactQuadraticLeafCheck_sound (by simpa only [box_right_exact, anchor_right_exact] using accepted_right)
#print axioms decoded_right
#print axioms accepted_right
#print axioms leaf_right

theorem decoded_children :
    box_left = parentBox.lowerHalf (⟨0, by decide⟩ : Fin 5) ∧
    box_right = parentBox.upperHalf (⟨0, by decide⟩ : Fin 5) := by
  rw [box_left_exact, box_right_exact, parentBox_exact]
  exact A1294CompactParent.source_children_match_parent_split
theorem parent : ∀ ⦃g : Fin 5 → ℝ⦄, parentBox.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g := by
  rw [parentBox_exact]
  have hl : BoxPredicate (fun g => ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g)
      (A1294CompactParent.sourceParentBox.lowerHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← A1294CompactParent.source_children_match_parent_split.1]
    exact leaf_left
  have hr : BoxPredicate (fun g => ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g)
      (A1294CompactParent.sourceParentBox.upperHalf (⟨0, by decide⟩ : Fin 5)) := by
    rw [← A1294CompactParent.source_children_match_parent_split.2]
    exact leaf_right
  exact boxPredicate_of_midpoint_children hl hr
#print axioms parent
#print parent
end SharkBridge01

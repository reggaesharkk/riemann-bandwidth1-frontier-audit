import Zeta23.ThmD.Sextuple.AffineTree
open Zeta23.ThmD.Sextuple
noncomputable section
namespace A1294Source
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000
abbrev Path := List (Nat × Bool)
def scan : Nat → List Nat → List Nat → List Path → Nat → Option (List Path × Nat)
  | 0, _, _, pending, cursor => some (pending,cursor)
  | _+1, [], _, _, _ => none
  | _+1, _, _, [], _ => none
  | n+1, token::rest, kinds, path::pending, cursor =>
      if token = 0 then
        match kinds[cursor]? with
        | none => none
        | some k => if k ≤ 1 then scan n rest kinds pending (cursor+1) else none
      else if 1 ≤ token ∧ token ≤ 5 then
        scan n rest kinds ((path ++ [(token-1,false)])::(path ++ [(token-1,true)])::pending) cursor
      else none
def locate (n : Nat) (bytes kinds : List Nat) : Option (Path × Nat) := do
  let (pending,cursor) ← scan n bytes kinds [[]] 0
  let path ← pending.head?
  return (path,cursor)
def topologyBytes : List Nat := [3, 2, 4, 1, 5, 3, 2, 4, 1, 5, 3, 2, 4, 1, 5, 3, 0, 2, 0, 4, 0, 1, 0, 5, 0, 3, 0, 2, 0, 4, 0, 1, 0, 5, 0, 3, 2, 4, 1, 5, 3, 0, 2, 0, 4, 0, 1, 0, 5, 0, 3, 2, 0, 4, 0, 1, 0, 5, 0, 3, 0, 2, 0, 4, 0, 1, 0, 0]
def kindBytes : List Nat := [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def anchorBytes : List Nat := [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def parentPath : Path := [(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,false),(3,false),(0,false),(4,false),(2,true),(1,true),(3,true),(0,true),(4,true),(2,false),(1,true),(3,true),(0,true),(4,true),(2,true),(1,true),(3,true)]
def typedParentPath : List (Fin 5 × Bool) := [(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,false),(⟨3,by decide⟩,false),(⟨0,by decide⟩,false),(⟨4,by decide⟩,false),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,false),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true),(⟨0,by decide⟩,true),(⟨4,by decide⟩,true),(⟨2,by decide⟩,true),(⟨1,by decide⟩,true),(⟨3,by decide⟩,true)]
def decodePath (p : Path) : Option (List (Fin 5 × Bool)) := p.mapM fun (a,b) =>
  if h : a < 5 then some (⟨a,h⟩,b) else none
theorem node65 : locate 65 topologyBytes kindBytes = some (parentPath,22) := by decide
theorem node66 : locate 66 topologyBytes kindBytes = some (parentPath ++ [(0,false)],22) := by decide
theorem node67 : locate 67 topologyBytes kindBytes = some (parentPath ++ [(0,true)],23) := by decide
theorem typed_path : decodePath parentPath = some typedParentPath := by rfl
theorem subtree_bytes : topologyBytes.drop 65 = [1,0,0] := by rfl
theorem kinds22_23 : (kindBytes[22]?,kindBytes[23]?) = (some 1,some 1) := by rfl
theorem prefix_all_quadratic : kindBytes.all (fun k => k == 1) = true := by decide
def quadraticIndex (terminal : Nat) : Nat := ((kindBytes.take terminal).filter (fun k => k == 1)).length
def anchorCode (terminal coordinate : Nat) : Option Nat := do
  let lo ← anchorBytes[quadraticIndex terminal*10+coordinate*2]?
  let hi ← anchorBytes[quadraticIndex terminal*10+coordinate*2+1]?
  return lo+256*hi
theorem anchors22 : (List.range 5).mapM (anchorCode 22) = some [0,0,0,0,0] := by rfl
theorem anchors23 : (List.range 5).mapM (anchorCode 23) = some [0,0,0,0,0] := by rfl
theorem quadratic_cursors : (quadraticIndex 22,quadraticIndex 23) = (22,23) := by rfl
def walk : GapBox → List (Fin 5 × Bool) → GapBox
  | box, [] => box
  | box, (a,false)::rest => walk (box.lowerHalf a) rest
  | box, (a,true)::rest => walk (box.upperHalf a) rest
theorem box_ext {a b : GapBox} (hl : ∀ i, a.lo i = b.lo i)
    (hh : ∀ i, a.hi i = b.hi i) : a = b := by
  cases a; cases b
  simp only [GapBox.mk.injEq]
  exact ⟨funext hl,funext hh⟩
def box0 : GapBox := initialGapBox 60

def box1 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (60) | 1 => (60) | 2 => (30) | 3 => (60) | _ => (60)
theorem checkpoint0 : box0.lowerHalf (⟨2,by decide⟩ : Fin 5) = box1 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box0, box1, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box2 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (60) | 1 => (30) | 2 => (30) | 3 => (60) | _ => (60)
theorem checkpoint1 : box1.lowerHalf (⟨1,by decide⟩ : Fin 5) = box2 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box1, box2, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box3 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (60) | 1 => (30) | 2 => (30) | 3 => (30) | _ => (60)
theorem checkpoint2 : box2.lowerHalf (⟨3,by decide⟩ : Fin 5) = box3 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box2, box3, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box4 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (30) | 1 => (30) | 2 => (30) | 3 => (30) | _ => (60)
theorem checkpoint3 : box3.lowerHalf (⟨0,by decide⟩ : Fin 5) = box4 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box3, box4, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box5 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (30) | 1 => (30) | 2 => (30) | 3 => (30) | _ => (30)
theorem checkpoint4 : box4.lowerHalf (⟨4,by decide⟩ : Fin 5) = box5 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box4, box5, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box6 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (30) | 1 => (30) | 2 => (15) | 3 => (30) | _ => (30)
theorem checkpoint5 : box5.lowerHalf (⟨2,by decide⟩ : Fin 5) = box6 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box5, box6, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box7 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (30) | 1 => (15) | 2 => (15) | 3 => (30) | _ => (30)
theorem checkpoint6 : box6.lowerHalf (⟨1,by decide⟩ : Fin 5) = box7 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box6, box7, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box8 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (30) | 1 => (15) | 2 => (15) | 3 => (15) | _ => (30)
theorem checkpoint7 : box7.lowerHalf (⟨3,by decide⟩ : Fin 5) = box8 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box7, box8, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box9 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15) | 1 => (15) | 2 => (15) | 3 => (15) | _ => (30)
theorem checkpoint8 : box8.lowerHalf (⟨0,by decide⟩ : Fin 5) = box9 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box8, box9, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box10 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15) | 1 => (15) | 2 => (15) | 3 => (15) | _ => (15)
theorem checkpoint9 : box9.lowerHalf (⟨4,by decide⟩ : Fin 5) = box10 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box9, box10, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box11 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15) | 1 => (15) | 2 => (15/2) | 3 => (15) | _ => (15)
theorem checkpoint10 : box10.lowerHalf (⟨2,by decide⟩ : Fin 5) = box11 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box10, box11, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box12 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15) | 1 => (15/2) | 2 => (15/2) | 3 => (15) | _ => (15)
theorem checkpoint11 : box11.lowerHalf (⟨1,by decide⟩ : Fin 5) = box12 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box11, box12, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box13 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15)
theorem checkpoint12 : box12.lowerHalf (⟨3,by decide⟩ : Fin 5) = box13 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box12, box13, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box14 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15)
theorem checkpoint13 : box13.lowerHalf (⟨0,by decide⟩ : Fin 5) = box14 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box13, box14, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box15 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (0) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint14 : box14.lowerHalf (⟨4,by decide⟩ : Fin 5) = box15 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box14, box15, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box16 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (0) | 2 => (15/4) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint15 : box15.upperHalf (⟨2,by decide⟩ : Fin 5) = box16 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box15, box16, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box17 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (15/4) | 2 => (15/4) | 3 => (0) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint16 : box16.upperHalf (⟨1,by decide⟩ : Fin 5) = box17 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box16, box17, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box18 : GapBox where
  lo := fun i => match i.val with | 0 => (0) | 1 => (15/4) | 2 => (15/4) | 3 => (15/4) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint17 : box17.upperHalf (⟨3,by decide⟩ : Fin 5) = box18 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box17, box18, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box19 : GapBox where
  lo := fun i => match i.val with | 0 => (15/4) | 1 => (15/4) | 2 => (15/4) | 3 => (15/4) | _ => (0)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint18 : box18.upperHalf (⟨0,by decide⟩ : Fin 5) = box19 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box18, box19, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box20 : GapBox where
  lo := fun i => match i.val with | 0 => (15/4) | 1 => (15/4) | 2 => (15/4) | 3 => (15/4) | _ => (15/4)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint19 : box19.upperHalf (⟨4,by decide⟩ : Fin 5) = box20 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box19, box20, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box21 : GapBox where
  lo := fun i => match i.val with | 0 => (15/4) | 1 => (15/4) | 2 => (45/8) | 3 => (15/4) | _ => (15/4)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint20 : box20.upperHalf (⟨2,by decide⟩ : Fin 5) = box21 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box20, box21, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box22 : GapBox where
  lo := fun i => match i.val with | 0 => (15/4) | 1 => (45/8) | 2 => (45/8) | 3 => (15/4) | _ => (15/4)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint21 : box21.upperHalf (⟨1,by decide⟩ : Fin 5) = box22 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box21, box22, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box23 : GapBox where
  lo := fun i => match i.val with | 0 => (15/4) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (15/4)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint22 : box22.upperHalf (⟨3,by decide⟩ : Fin 5) = box23 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box22, box23, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box24 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (15/4)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint23 : box23.upperHalf (⟨0,by decide⟩ : Fin 5) = box24 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box23, box24, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box25 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (15/2) | 3 => (15/2) | _ => (15/2)
theorem checkpoint24 : box24.upperHalf (⟨4,by decide⟩ : Fin 5) = box25 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box24, box25, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box26 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (15/2) | 2 => (105/16) | 3 => (15/2) | _ => (15/2)
theorem checkpoint25 : box25.lowerHalf (⟨2,by decide⟩ : Fin 5) = box26 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box25, box26, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box27 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (105/16) | 2 => (105/16) | 3 => (15/2) | _ => (15/2)
theorem checkpoint26 : box26.lowerHalf (⟨1,by decide⟩ : Fin 5) = box27 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box26, box27, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box28 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (15/2) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (15/2)
theorem checkpoint27 : box27.lowerHalf (⟨3,by decide⟩ : Fin 5) = box28 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box27, box28, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box29 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (15/2)
theorem checkpoint28 : box28.lowerHalf (⟨0,by decide⟩ : Fin 5) = box29 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box28, box29, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box30 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (45/8) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint29 : box29.lowerHalf (⟨4,by decide⟩ : Fin 5) = box30 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box29, box30, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box31 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (45/8) | 2 => (195/32) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint30 : box30.upperHalf (⟨2,by decide⟩ : Fin 5) = box31 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box30, box31, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box32 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (195/32) | 2 => (195/32) | 3 => (45/8) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint31 : box31.upperHalf (⟨1,by decide⟩ : Fin 5) = box32 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box31, box32, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box33 : GapBox where
  lo := fun i => match i.val with | 0 => (45/8) | 1 => (195/32) | 2 => (195/32) | 3 => (195/32) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint32 : box32.upperHalf (⟨3,by decide⟩ : Fin 5) = box33 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box32, box33, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box34 : GapBox where
  lo := fun i => match i.val with | 0 => (195/32) | 1 => (195/32) | 2 => (195/32) | 3 => (195/32) | _ => (45/8)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint33 : box33.upperHalf (⟨0,by decide⟩ : Fin 5) = box34 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box33, box34, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box35 : GapBox where
  lo := fun i => match i.val with | 0 => (195/32) | 1 => (195/32) | 2 => (195/32) | 3 => (195/32) | _ => (195/32)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (105/16) | 3 => (105/16) | _ => (105/16)
theorem checkpoint34 : box34.upperHalf (⟨4,by decide⟩ : Fin 5) = box35 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box34, box35, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box36 : GapBox where
  lo := fun i => match i.val with | 0 => (195/32) | 1 => (195/32) | 2 => (195/32) | 3 => (195/32) | _ => (195/32)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint35 : box35.lowerHalf (⟨2,by decide⟩ : Fin 5) = box36 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box35, box36, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box37 : GapBox where
  lo := fun i => match i.val with | 0 => (195/32) | 1 => (405/64) | 2 => (195/32) | 3 => (195/32) | _ => (195/32)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint36 : box36.upperHalf (⟨1,by decide⟩ : Fin 5) = box37 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box36, box37, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box38 : GapBox where
  lo := fun i => match i.val with | 0 => (195/32) | 1 => (405/64) | 2 => (195/32) | 3 => (405/64) | _ => (195/32)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint37 : box37.upperHalf (⟨3,by decide⟩ : Fin 5) = box38 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box37, box38, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box39 : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (405/64) | 2 => (195/32) | 3 => (405/64) | _ => (195/32)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint38 : box38.upperHalf (⟨0,by decide⟩ : Fin 5) = box39 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box38, box39, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box40 : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (405/64) | 2 => (195/32) | 3 => (405/64) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint39 : box39.upperHalf (⟨4,by decide⟩ : Fin 5) = box40 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box39, box40, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box41 : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (405/64) | 2 => (795/128) | 3 => (405/64) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint40 : box40.upperHalf (⟨2,by decide⟩ : Fin 5) = box41 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box40, box41, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box42 : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (405/64) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint41 : box41.upperHalf (⟨1,by decide⟩ : Fin 5) = box42 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box41, box42, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def box43 : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (105/16) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
theorem checkpoint42 : box42.upperHalf (⟨3,by decide⟩ : Fin 5) = box43 := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box42, box43, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide

def parentBox : GapBox := box43
theorem source_path_box : walk (initialGapBox 60) typedParentPath = parentBox := by
  change walk box0 typedParentPath = box43
  simp only [typedParentPath, walk]
  rw [checkpoint0, checkpoint1, checkpoint2, checkpoint3, checkpoint4, checkpoint5, checkpoint6, checkpoint7, checkpoint8, checkpoint9, checkpoint10, checkpoint11, checkpoint12, checkpoint13, checkpoint14, checkpoint15, checkpoint16, checkpoint17, checkpoint18, checkpoint19, checkpoint20, checkpoint21, checkpoint22, checkpoint23, checkpoint24, checkpoint25, checkpoint26, checkpoint27, checkpoint28, checkpoint29, checkpoint30, checkpoint31, checkpoint32, checkpoint33, checkpoint34, checkpoint35, checkpoint36, checkpoint37, checkpoint38, checkpoint39, checkpoint40, checkpoint41, checkpoint42]
def sourceBoxAt (n : Nat) : Option (GapBox × Nat) := do
  let (p,c) ← locate n topologyBytes kindBytes
  let typed ← decodePath p
  return (walk (initialGapBox 60) typed,c)
theorem node65_box : sourceBoxAt 65 = some (parentBox,22) := by
  simp only [sourceBoxAt, node65, Option.bind_some, typed_path]
  rw [source_path_box]
#print axioms node65
#print axioms node66
#print axioms node67
#print axioms source_path_box
#print axioms node65_box
end A1294Source

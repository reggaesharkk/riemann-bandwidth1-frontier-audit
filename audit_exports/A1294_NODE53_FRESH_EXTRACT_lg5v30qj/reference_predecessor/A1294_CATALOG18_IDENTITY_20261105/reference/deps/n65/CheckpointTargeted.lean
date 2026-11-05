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
  · intro i
    fin_cases i <;> rfl
  · intro i
    fin_cases i <;>
      simp only [GapBox.lowerHalf, box0, initialGapBox, GapBox.midpoint,
        Function.update_apply, box1] <;> norm_num <;> decide



#print axioms checkpoint0
end A1294Source

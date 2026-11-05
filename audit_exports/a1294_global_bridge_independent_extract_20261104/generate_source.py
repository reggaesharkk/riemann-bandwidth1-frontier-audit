from pathlib import Path
from fractions import Fraction as F
import hashlib,json,zipfile
D=Path(__file__).resolve().parent
archive=D/'frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
if not archive.exists():archive=D.parent.parent/'a1294_quadratic_leaf_20261104/delivery/source/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
j=json.loads((D/'authentic_input.json').read_text());p=j['parent']
if hashlib.sha256(archive.read_bytes()).hexdigest()!=j['v2_zip_sha256']:raise RuntimeError('frozen archive')
with zipfile.ZipFile(archive) as z:
    prefix='A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/'
    top=list(z.open(prefix+'topology-u8.bin').read(68));kinds=list(z.open(prefix+'terminal-kinds-u8.bin').read(24));anchors=list(z.open(prefix+'anchors-u16le.bin').read(240))
(D/'source_prefix.json').write_text(json.dumps({'archive_sha256':j['v2_zip_sha256'],'topology':top,'kinds':kinds,'anchors':anchors},indent=2))
path=list(zip(p['path_axes_zero_based'],p['path_sides']))
natpath=lambda xs:'['+','.join(f'({a},{"true" if b=="R" else "false"})' for a,b in xs)+']'
typed=lambda xs:'['+','.join(f'(⟨{a},by decide⟩,{"true" if b=="R" else "false"})' for a,b in xs)+']'
S=['''import Zeta23.ThmD.Sextuple.AffineTree
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
def topologyBytes : List Nat := '''+str(top)+'''
def kindBytes : List Nat := '''+str(kinds)+'''
def anchorBytes : List Nat := '''+str(anchors)+'''
def parentPath : Path := '''+natpath(path)+'''
def typedParentPath : List (Fin 5 × Bool) := '''+typed(path)+'''
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
''']
box=[(F(0),F(60)) for _ in range(5)]
for k,(axis,side) in enumerate(path):
    lo,hi=box[axis];mid=(lo+hi)/2;box[axis]=(mid,hi) if side=='R' else (lo,mid)
    S += [f'def box{k+1} : GapBox where\n  lo := fun i => match i.val with '+' '.join(f'| {i} => ({b[0]})' for i,b in enumerate(box[:-1]))+' | _ => ('+str(box[-1][0])+')\n  hi := fun i => match i.val with '+' '.join(f'| {i} => ({b[1]})' for i,b in enumerate(box[:-1]))+' | _ => ('+str(box[-1][1])+')']
    op='upperHalf' if side=='R' else 'lowerHalf'
    S += [f'''theorem checkpoint{k} : box{k}.{op} (⟨{axis},by decide⟩ : Fin 5) = box{k+1} := by
  apply box_ext
  all_goals intro i; fin_cases i <;> norm_num [box{k}, box{k+1}, initialGapBox, GapBox.lowerHalf, GapBox.upperHalf, GapBox.midpoint, Function.update] <;> decide
''']
if box!=[tuple(map(F,b)) for b in p['box_exact']]:raise RuntimeError('parent checkpoint differs')
S += ['def parentBox : GapBox := box'+str(len(path)),'''theorem source_path_box : walk (initialGapBox 60) typedParentPath = parentBox := by
  change walk box0 typedParentPath = '''+'box'+str(len(path))+'''
  simp only [typedParentPath, walk]
  rw ['''+', '.join('checkpoint'+str(k) for k in range(len(path)))+''']
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
''']
(D/'SourceNode65.lean').write_text('\n'.join(S),encoding='utf-8');print('Generated bounded 68-byte topology interpretation and',len(path),'individually normalized midpoint checkpoints.')

from pathlib import Path
import json
from codec import decode,strict
D=Path(__file__).resolve().parent
w=strict((D/'payload.sb01').read_text());decode((D/'payload.sb01').read_bytes())
S=['''import Zeta23.ThmD.Sextuple.A1294CompactParent
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
'''+',\n'.join(f'⟨({n}),{d}⟩' for n,d in w['q'])+']',
'def segs : Array WireSegment := #[\n'+',\n'.join(f'⟨{a},{b},{c}⟩' for a,b,c in w['segments'])+']']
j=json.loads((D/'frozen/authentic_input.json').read_text())
S+=['def qAt (i : Nat) : ℚ := interpRat ((qs[i]?).getD ⟨0,1⟩)']
def boxdef(name,b):
    return 'def '+name+' : GapBox where\n  lo := fun i => match i.val with '+ ' '.join(f'| {i} => qAt {a}' for i,(a,_) in enumerate(b[:-1]))+' | _ => qAt '+str(b[-1][0])+'\n  hi := fun i => match i.val with '+' '.join(f'| {i} => qAt {h}' for i,(_,h) in enumerate(b[:-1]))+' | _ => qAt '+str(b[-1][1])
S+=[boxdef('parentBox',w['parent'][2]),'''theorem parentBox_exact : parentBox = A1294CompactParent.sourceParentBox := by
  apply A1294CompactParent.gapBox_ext_exact
  all_goals intro i; fin_cases i <;> norm_num [parentBox, A1294CompactParent.sourceParentBox, qAt, qs, interpRat]
''']
for side,l,ns in zip(['left','right'],w['leaves'],['AuthenticCompactLeaf','AuthenticCompactRight']):
    catalog=[]
    for t in j['children'][side]['fifteen_models']:
        for name in (['macroPiece'+str(t['direct_catalog_index'])] if t['kind']=='direct_piece' else [x['declaration'] for x in t['segments']]):
            if name not in catalog:catalog.append(name)
    S+=['def refs_'+side+' : Array (Option Nat) := #['+', '.join('some '+str(catalog.index(c)) if c in catalog else 'none' for c in w['catalog'])+']']
    def row(r):return '.direct '+str(r[1]) if r[0]==0 else '.floor '+str(r[1])+' ['+','.join(map(str,r[2]))+']'
    S+=['def wire_'+side+' : Fin 15 → WireRow := fun p => match p.val with '+' '.join(f'| {i} => {row(r)}' for i,r in enumerate(l[4][:-1]))+' | _ => '+row(l[4][-1])]
    S+=[boxdef('box_'+side,l[2]),'def anchor_'+side+' : Fin 5 → ℚ := fun i => match i.val with '+' '.join(f'| {i} => qAt {a}' for i,a in enumerate(l[3][:-1]))+' | _ => qAt '+str(l[3][-1])]
    S+=[f'''theorem box_{side}_exact : box_{side} = {ns}.box := by
  apply A1294CompactParent.gapBox_ext_exact
  all_goals intro i; fin_cases i <;> norm_num [box_{side}, {ns}.box, qAt, qs, interpRat]
theorem anchor_{side}_exact : anchor_{side} = {ns}.anchor := by
  funext i
  fin_cases i <;> norm_num [anchor_{side}, {ns}.anchor, {ns}.box, qAt, qs, interpRat]
''']
    S+=[f'''theorem decoded_{side} : ∀ p, decodeRow qs segs refs_{side} (wire_{side} p) = some ({ns}.rows p) := by
  intro p
  fin_cases p <;> rfl
def rows_{side} (p : Fin 15) : CompactRow := rowOrDefault (decodeRow qs segs refs_{side} (wire_{side} p))
theorem rows_{side}_exact : rows_{side} = {ns}.rows := by
  funext p
  simp [rows_{side}, decoded_{side}, rowOrDefault]
theorem accepted_{side} : compactQuadraticLeafCheck {ns}.catalog (647/50000) (1094977/5000000000) box_{side} anchor_{side} rows_{side} = true := by
  rw [rows_{side}_exact, box_{side}_exact, anchor_{side}_exact]
  exact {ns}.accepted
theorem leaf_{side} : ∀ ⦃g : Fin 5 → ℝ⦄, {ns}.box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  compactQuadraticLeafCheck_sound (by simpa only [box_{side}_exact, anchor_{side}_exact] using accepted_{side})
#print axioms decoded_{side}
#print axioms accepted_{side}
#print axioms leaf_{side}
''']
S+=['''theorem decoded_children :
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
''']
(D/'WireParent.lean').write_text('\n'.join(S),encoding='utf-8')
print('Generated typed interned-data decoder and semantic correspondence; acceptance reuses frozen proofs. This is not a standalone lower-cost acceptance engine.')

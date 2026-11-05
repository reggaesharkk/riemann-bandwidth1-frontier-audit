import json
from pathlib import Path
from fractions import Fraction
D=Path(__file__).resolve().parent
j=json.loads((D/'authentic_input.json').read_text())['children']['left']
def q(x):
 x=Fraction(x);return f'⟨({x.numerator}), {x.denominator}⟩'
cat=[]
for t in j['fifteen_models']:
 for name in ([f"macroPiece{t['direct_catalog_index']}"] if t['kind']=='direct_piece' else [s['declaration'] for s in t['segments']]):
  if name not in cat:cat.append(name)
lines=['namespace AuthenticCompact19','open A1294FifteenBridge A1294Compact', 'def catalog : Array MacroPiece := #['+', '.join(cat)+']']
for t in j['fifteen_models']:
 i=t['pair_index_zero_based']
 if t['kind']=='direct_piece':v=f".direct {cat.index('macroPiece'+str(t['direct_catalog_index']))}"
 else:
  ss=[f'{{ lo := {q(s["segment"][0])}, hi := {q(s["segment"][1])}, pieceRef := {cat.index(s["declaration"])} }}' for s in t['segments']]
  v=f'.floor {q(t["base"])} [\n'+',\n'.join(ss)+']'
 lines.append(f'def row{i} : CompactRow := {v}')
lines.append('def rows (p : Fin 15) : CompactRow := match p.val with '+ ' '.join(f'| {i} => row{i}' for i in range(14))+' | _ => row14')
box=j['box_exact']
lines.append('def box : GapBox where\n  lo := fun i => match i.val with '+ ' '.join(f'| {i} => ({box[i][0]})' for i in range(4))+f' | _ => ({box[4][0]})'+'\n  hi := fun i => match i.val with '+ ' '.join(f'| {i} => ({box[i][1]})' for i in range(4))+f' | _ => ({box[4][1]})')
lines+=['def anchor : Fin 5 → ℚ := fun i => if i.val = 2 then box.hi i else box.lo i', 'set_option maxRecDepth 4000 in\nset_option maxHeartbeats 1000000 in\ntheorem accepted : compactQuadraticLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows = true := by\n  decide', 'theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →\n    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=\n  compactQuadraticLeafCheck_sound accepted', '#print axioms leaf_sound','end AuthenticCompact19']
(D/'AuthenticCompact19.lean').write_text('import Zeta23.ThmD.Sextuple.CompositionalLeaf\nopen Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype\nnoncomputable section\n'+'\n'+'\n'.join(lines),encoding='utf-8')
(D/'leaf_data_summary.json').write_text(json.dumps({'side':'left','terminal':19,'topology_node':60,'catalog_declarations':cat,'segments':sum(len(t['segments']) for t in j['fifteen_models']),'external_source_bridge':True},indent=2))
print('generated authentic left leaf; catalog',len(cat))


from pathlib import Path
import json
D=Path(__file__).resolve().parent
leaf=(D/'generator_sources/generate_leaf.py').read_text(encoding='utf-8')
leaf=leaf.replace("['children']['left']", "['children']['right']")
leaf=leaf.replace("(D/'A1294FifteenBridge.lean').read_text(encoding='utf-8-sig')", "'import Zeta23.ThmD.Sextuple.CompositionalLeaf\\nopen Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype\\nnoncomputable section\\n'")
leaf=leaf.replace('AuthenticCompactLeaf', 'AuthenticCompactRight')
leaf=leaf.replace('generated authentic left leaf', 'generated authentic right leaf')
leaf=leaf.replace("'side':'left','terminal':22,'topology_node':66", "'side':'right','terminal':23,'topology_node':67")
(D/'generate_right_literals.py').write_text(leaf,encoding='utf-8')
exec(compile(leaf,str(D/'generate_right_literals.py'),'exec'), {'__file__':str(D/'generate_right_literals.py')})
comp=(D/'generator_sources/generate_compositional.py').read_text(encoding='utf-8')
comp=comp.replace("['children']['left']", "['children']['right']")
comp=comp.replace("D.parent/'a1294_fifteen_bridge_20261104/AuthenticCompactLeaf.lean'", "D/'AuthenticCompactRight.lean'")
comp=comp.replace('end AuthenticCompactLeaf','end AuthenticCompactRight')
comp=comp.replace("D/'CompositionalLeaf.lean'", "D/'CompositionalRight.lean'")
(D/'generate_right_proofs.py').write_text(comp,encoding='utf-8')
exec(compile(comp,str(D/'generate_right_proofs.py'),'exec'), {'__file__':str(D/'generate_right_proofs.py')})
j=json.loads((D/'authentic_input.json').read_text())['children']['right']
print('right exact margin:',j['exact_margin'])
print('direct rows:',[(t['pair_index_zero_based'],t.get('direct_catalog_index')) for t in j['fifteen_models'] if t['kind']=='direct_piece'])

"""Reconstruct the external compositional decoder conversion, without writing.

Run after retaining the original generated draft. This checks byte equality with
the final Lean file; the Lean compiler, not this script, proves acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib
D=Path(__file__).resolve().parent
s=(D/'Terminal20_failed_v1.lean').read_text(encoding='utf-8')
j=json.loads((D/'authentic_input.json').read_text())['children']['left']
cats=json.loads((D/'leaf_data_summary.json').read_text())['catalog_declarations']
def qr(v):
    q=F(v);return f'⟨({q.numerator}), {q.denominator}⟩'
for row in j['fifteen_models']:
    i=row['pair_index_zero_based'];defs=[];names=[]
    for k,t in enumerate(row['segments']):
        name=f'decode_segment_{i}_{k}';names.append(name)
        lo,hi=t['segment'];ref=cats.index(t['declaration'])
        literal=f'{{lo := {qr(lo)}, hi := {qr(hi)}, pieceRef := {ref}}}'
        val=f'{{lo := ({lo}), hi := ({hi}), piece := {t["declaration"]}}}'
        defs.append(f'theorem {name} : interpSegment catalog {literal} = some {val} := by rfl')
    a=s.index(f'theorem decode_{i} :');b=s.index(f'\ntheorem segment_{i}_0',a)
    statement=s[a:s.index(':= by',a)]
    proof=':= by\n  simp [interpCompactRow, row'+str(i)+', segments'+str(i)+', List.mapM_cons, '+', '.join(names)+', interpRat]\n'
    s=s[:a]+'\n'.join(defs)+'\n'+statement+proof+s[b:]
pos=s.index('theorem canonical_0')
s=s[:pos]+'\n'.join(f'theorem catalog_ref_{i} : catalog[{i}]? = some {decl} := by simp [catalog]' for i,decl in enumerate(cats))+'\n'+s[pos:]
s=re.sub(r'(theorem decode_segment_\d+_\d+ : interpSegment catalog .*?pieceRef := (\d+)\}.*? := by) rfl',lambda m:m[1]+'\n  simp only [interpSegment, catalog_ref_'+m[2]+']\n  rfl',s)
if s != (D/'Terminal20.lean').read_text(encoding='utf-8'):
    raise RuntimeError('decoder conversion mismatch')
print('PASS: exact final decoder conversion; SHA256 '+hashlib.sha256(s.encode()).hexdigest())

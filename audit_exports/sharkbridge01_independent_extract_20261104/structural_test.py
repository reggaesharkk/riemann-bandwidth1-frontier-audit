"""Exact reflection/template residual experiment; not LRSC K11 projection."""
from pathlib import Path
import json,zlib
from codec import strict,canonical
D=Path(__file__).resolve().parent
w=strict((D/'payload.sb01').read_text());rows=[r for l in w['leaves'] for r in l[4]]
# Ordinary row interning comparison.
table=[];refs=[]
for r in rows:
    if r not in table:table.append(r)
    refs.append(table.index(r))
ordinary=canonical({'table':table,'refs':refs})
# Reflection/structural template relation, with complete signed integer residual.
templates=[];encoded=[];recovered=[]
for row in rows:
    if row[0]==0:encoded.append(['direct',row[1]]);recovered.append(row);continue
    floor,ids=row[1:];candidates=[]
    for k,t in enumerate(templates):
        if len(t)!=len(ids):continue
        for flip in [False,True]:
            base=t[::-1] if flip else t
            residual=[[i,a-b] for i,(a,b) in enumerate(zip(ids,base)) if a!=b]
            v=['delta',floor,k,int(flip),residual]
            candidates.append(v)
    literal=['literal',floor,ids]
    v=min(candidates+[literal],key=lambda v:(len(canonical(v)),canonical(v)))
    encoded.append(v)
    if v[0]=='literal':templates.append(ids);out=ids
    else:
        out=list(templates[v[2]][::-1] if v[3] else templates[v[2]])
        for i,delta in v[4]:out[i]+=delta
    if out!=ids:raise RuntimeError('inverse residual failure')
    recovered.append([1,floor,out])
if recovered!=rows:raise RuntimeError('row stream changed')
transform=canonical({'templates':templates,'rows':encoded})
result={'lossless_inverse':'PASS','row_occurrences':len(rows),'unique_rows':len(table),'reflection_delta_rows':sum(r[0]=='delta' for r in encoded),'raw_rows_bytes':len(canonical(rows)),'ordinary_row_intern_bytes':len(ordinary),'ordinary_row_intern_zlib':len(zlib.compress(ordinary,9)),'reflection_residual_bytes':len(transform),'reflection_residual_zlib':len(zlib.compress(transform,9)),'scope':'row substream only; not a full-payload compression comparison','K11':'not used; no injective exact reconstruction of arbitrary 99-vector from 11 coordinates without residual'}
(D/'structural_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

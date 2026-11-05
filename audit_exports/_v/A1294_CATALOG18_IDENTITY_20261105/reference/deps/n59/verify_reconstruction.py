from pathlib import Path
from fractions import Fraction as F
import json,zipfile,hashlib,struct
p=Path(__file__).resolve().parent;l=json.loads((p/'authentic_input.json').read_text())['children']['left'];zpath=Path('audit_exports/a1294_quadratic_leaf_20261104/delivery/source/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip')
with zipfile.ZipFile(zpath) as z:
 pre='A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/';m=json.loads(z.read(pre+'certificate/manifest.json'));cats=[]
 streams={}
 for key,name in [('topology','topology-u8.bin'),('kinds','terminal-kinds-u8.bin'),('anchors','anchors-u16le.bin')]:
  b=z.read(pre+'certificate/'+name)
  if hashlib.sha256(b).hexdigest()!=m['stream_sha256'][key]:raise RuntimeError(key+' source hash')
  streams[key]=b
 if list(streams['topology'][59:68])!=[3,0,2,0,4,0,1,0,0] or streams['kinds'][19]!=1:raise RuntimeError('source topology/kind')
 q=sum(k==1 for k in streams['kinds'][:19])
 if q!=19 or struct.unpack_from('<5H',streams['anchors'],q*10)!=(0,0,16384,0,0):raise RuntimeError('source anchor bytes')
 for key,name in [('stable','macro-data-exact.json'),('v1','refinement-catalog-v1-exact.json'),('v3','refinement-catalog-v3.json')]:
  b=z.read(pre+'data/'+name)
  if hashlib.sha256(b).hexdigest()!=m['input_sha256'][key]:raise RuntimeError(key)
  cats+=json.loads(b)['pieces']
a=list(map(F,l['anchor_coordinates_exact']));box=[[F(x),F(y)] for x,y in l['box_exact']];codes=l['anchor_codes_u16le']
if codes!=[0,0,16384,0,0] or a!=[F(405,64),F(405,64),F(795,128),F(405,64),F(405,64)]:raise RuntimeError('anchor')
if a!=[lo+F(c,16384)*(hi-lo) for (lo,hi),c in zip(box,codes)]:raise RuntimeError('anchor decode')
B=F(l['B']);value=B*sum(a);gradient=[B]*5
for row in l['fifteen_models']:
 i,j=row['gap_index_range_inclusive'];lo=sum((box[k][0] for k in range(i,j+1)),F(0));hi=sum((box[k][1] for k in range(i,j+1)),F(0))
 if [lo,hi]!=list(map(F,row['distance_interval'])):raise RuntimeError('distance')
 w=F(row['weight']);dot=sum(a[i:j+1])+F(row['offset']);value+=F(row['base'])+w*dot*dot
 for k in range(i,j+1):gradient[k]+=2*w*dot
 if row['kind']=='direct_piece':
  piece=cats[row['direct_catalog_index']];plo,phi=map(F,row['piece_interval'])
  if [plo,phi]!=[F(piece['lo']),F(piece['hi'])] or not (plo<=lo<=hi<=phi) or F(row['base'])!=F(row['piece_floor']) or F(row['weight'])!=F(row['piece_curvature']) or F(row['offset'])!=-F(row['piece_center']):raise RuntimeError('direct catalog')
 if row['kind']=='segmented_constant':
  end=lo
  for seg in row['segments']:
   if F(seg['segment'][0])!=end or seg['source_item']!=cats[seg['catalog_index_zero_based']]:raise RuntimeError('segment')
   end=F(seg['segment'][1])
  if end!=hi:raise RuntimeError('coverage')
tangent=value+sum(g*(box[i][0 if g>=0 else 1]-a[i]) for i,g in enumerate(gradient))
if tangent!=F(l['rank_tangent_lower']) or tangent-F(l['A'])!=F(l['exact_margin']) or tangent<=F(l['A']):raise RuntimeError('tangent')
print('PASS exact anchor, 15 distance supports, segmented seams/catalog records, tangent',tangent,'margin',tangent-F(l['A']))

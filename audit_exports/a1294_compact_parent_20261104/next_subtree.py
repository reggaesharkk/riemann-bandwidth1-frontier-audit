from pathlib import Path
import json,hashlib,zipfile
D=Path(__file__).resolve().parent
z=zipfile.ZipFile(D/'frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip')
data=z.read('A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/topology-u8.bin')
if hashlib.sha256(data).hexdigest()!='9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76':raise RuntimeError('topology hash')
kinds=z.read('A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/terminal-kinds-u8.bin')
stack=[]; completed=[]; terminal=0
# Bounded topology inspection only. No model selection or proof search.
for node,t in enumerate(data[:4096]):
    if t:
        stack.append({'node':node,'children':[]}); continue
    item={'node':node,'end':node,'leaves':[terminal],'kinds':[kinds[terminal]]};terminal+=1
    while stack:
        stack[-1]['children'].append(item)
        if len(stack[-1]['children'])<2:break
        p=stack.pop();a,b=p['children']
        item={'node':p['node'],'end':item['end'],'children':[a['node'],b['node']], 'leaves':a['leaves']+b['leaves'],'kinds':a['kinds']+b['kinds']}
        if item['node']<65 and item['end']>=67:completed.append(item)
    if completed:break
if not completed:raise RuntimeError('no enclosing subtree completed within bounded prefix')
item=completed[0]
item['nodes']=item['end']-item['node']+1
item['scope']='bounded topology inspection; future leaf mathematics not checked'
(D/'next_subtree.json').write_text(json.dumps(item,indent=2))
print(json.dumps(item,indent=2))

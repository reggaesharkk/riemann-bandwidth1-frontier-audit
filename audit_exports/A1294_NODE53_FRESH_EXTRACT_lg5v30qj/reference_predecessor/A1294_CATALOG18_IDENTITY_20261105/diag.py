import json,re,pathlib
D=pathlib.Path('.')
old=(D/'failed_drafts/terminal18/Terminal18_chunked_failed.lean').read_text(encoding='utf-8-sig')
lookup=(D/'reference/previous_objects/Catalog18Lookup.lean').read_text()
def arr(src,name):
 m=re.search(r'^def '+name+r' : Array MacroPiece := #\[([^\n]*)\]$',src,re.M)
 return [x.strip() for x in m.group(1).split(',')] if m else []
a=arr(old,'catalog'); b=arr(lookup,'original'); print(len(a),len(b))
for i,(x,y) in enumerate(zip(a,b)):
 if x!=y: print('first diff',i,repr(x),repr(y));break
else: print('prefix matches',min(len(a),len(b)))
print('terminal tail',a[-8:]); print('lookup tail',b[-8:])
print('terminal token counts',[(x,a.count(x)) for x in ['macroPiece30','macroPiece31','refinementPiece26','macroPiece14']])

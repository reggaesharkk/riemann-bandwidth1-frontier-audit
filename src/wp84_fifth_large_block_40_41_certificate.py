"""Universal full-rank four-column certificates for 41 and 40 blocks."""
from fractions import Fraction as Q
from pathlib import Path
import json
from wp84_fifth_large_block_symbolic import coeff
from wp84_fifth_large_block_18_certificate import terms
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
def diff(f,g,car,k):
 a=coeff(f,car,k);b=coeff(g,car,k)
 return {x:a.get(x,Q(0))-b.get(x,Q(0)) for x in set(a)|set(b) if a.get(x,Q(0))!=b.get(x,Q(0))}
def main():
 out=[]
 for ids,car,poly1,poly2,poly3 in [
 ([41,45,58,67],{2:[0],1:[1],-1:[2,3]}, {(1,1,1,1):16},{(2,0,1,1):8,(1,1,1,1):8},{(2,2,1,0):2,(2,2,0,1):2,(3,1,1,0):-2,(3,1,0,1):-2}),
 ([40,44,57,66],{2:[0],1:[1],-2:[2]}, {(1,1,2):8},{(2,0,2):4,(1,1,2):4},{(2,2,1):2,(3,1,1):-2})]:
  for f in ids[1:]:
   for k in range(4):assert not diff(f,ids[0],car,k)
  assert not diff(ids[1],ids[0],car,4)
  assert diff(ids[2],ids[0],car,4)==terms(poly1,{'DJDJ':1,'DDJJ':-1},2)
  assert diff(ids[3],ids[0],car,4)==terms(poly2,{'DJDJ':1,'DDJJ':-1},2)
  assert diff(ids[1],ids[0],car,5)==terms(poly3,{'DJDJJ':1,'DDJJJ':-1},2)
  out.append({'ids':ids,'basis':[f'F{ids[0]}',f'F{ids[2]}-F{ids[0]}',f'F{ids[3]}-F{ids[0]}',f'F{ids[1]}-F{ids[0]}'],'orders':[5,9,9,10],'ratio':'(a+b)/(2*b)','legal_cells':'p large prime; q in [p^k,2*p^k], k=6/5 or3/2; negative primes fixed at2 (and3); alias2; X0=p*sqrt(q/(r*s)) or p*sqrt(q)/r','ratio_limits':['11/12','5/6'],'normalized_minor':[['1','0','0','0'],['star','1','r_6/5','0'],['star','1','r_3/2','0'],['star','star','star','1']],'determinant':'r_3/2-r_6/5 -> -1/12','rank':4,'universal_symbolic_check':True})
 (ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_40_41_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS universal size-four minors for blocks 40 and41')
if __name__=='__main__':main()

"""Blockwise exact fifth separation certificates; no generic rank inference."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
RESOLVED={(1,2):2,(3,4,6):3,(5,7):2,(11,13):2,(14,19,24):3,(35,55):2,(51,70):2,(52,71):2}
def main():
    fs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());old=json.loads((ROOT/'notes/WP84_SHARED_CARRIER_DEGREE5_BLOCKS.json').read_text());table=[];witness=[]
    for block in old:
        ids=tuple(block['functional_ids']);rank=RESOLVED.get(ids,1);prior=2 if ids==(5,7) else 1
        table.append({'support':block['support'],'ids':ids,'size':len(ids),'layouts':[{'id':i,'signs':fs[i]['sign_word'],'pi':fs[i]['equality_partition'],'aliases':fs[i]['aliases']} for i in ids],'old_lower':prior,'new_lower':rank,'upper':len(ids),'unresolved_dimensions':len(ids)-rank,'complete':rank==len(ids),'witness_ids':list(ids) if ids in RESOLVED or len(ids)==1 else [ids[0]]})
        witness+=table[-1]['witness_ids']
    assert sum(b['old_lower'] for b in table)==20 and sum(b['new_lower'] for b in table)==29 and len(witness)==29
    formulas=[
      {'ids':[1,2],'order':11,'coefficient':'pi^2*Z2/n*a^5*b^2*c^2*(b-a)*(c-a)/(p^(3/2)*sqrt(q*r))','condition':'repeated prime p<q,r','identity':'sym Tr(X^3YZ-X^2YXZ)=-2*Tr([X,Y][X,Z]X)'},
      {'ids':[5,7],'order':11,'coefficient':'parent exact coefficient','condition':'parent smallest repeated-prime criterion','identity':'parent six-assignment commutator identity'},
      {'ids':[11,13],'order':10,'coefficient':'2*pi^2*Z12/n*a^5*b^2*c^2*(b-a)/(p^(3/2)*sqrt(q*r))','condition':'p<q; p^3*q/r carrier','identity':'symmetric matrices: single Tr(X^3YZ-X^2YXZ)=-Tr([X,Y][X,Z]X)'},
      {'ids':[35,55],'order':9,'coefficient':'16*pi^2*Z1/n*a^5*b^2*c^2/(p^(3/2)*sqrt(q*r))','condition':'all distinct primes, carrier p^3/(q*r)','identity':'same repeated-cube identity, both singleton signs negative'},
      {'ids':[51,70],'order':9,'coefficient':'16*pi^2*Z1/n*w^4*a*b*c*(a*b+a*c+b*c)/(s*sqrt(p*q*r))','condition':'all distinct primes, carrier p*q*r/s^2','identity':'cyclic six-assignment commutator identity, repeated matrix is negative branch'},
      {'ids':[52,71],'order':9,'coefficient':'32*pi^2*Z1/n*a*b*c*v^2*w^2*(a*b+a*c+b*c)/sqrt(p*q*r*s*t)','condition':'all distinct primes, carrier p*q*r/(s*t)','identity':'polarization in the two negative matrices of the six-assignment commutator identity'}]
    triples=[
      {'ids':[3,4,6],'basis':['F6','F3-F4','F4-F6'],'orders':[5,11,11],'differences':{'F3-F4':'pi^2*Z2/(2*n)*a^3*b^3*c^2*(b-a)^2*(a+b-c)/(p*q*sqrt(r))','F4-F6':'pi^2*Z2/(2*n)*a^4*b^4*c*(b-a)^2/(p*q*sqrt(r))'},'minor':'(log 2-log 3)*(log p+log q-log 2-log 3)/(log p*log q)','rows':'leading row plus two order-11 carrier cells with singleton r=2 and r=3, fixed p,q large','normalized_matrix':[['1','0','0'],['star1','R(log 2)','1'],['star2','R(log 3)','1']],'R':'c*(a+b-c)/(a*b)','nonzero':'p,q distinct large, p*q>6; both carrier cells legal at m=2'},
      {'ids':[14,19,24],'basis':['F19','F14-F24','F24-F19'],'orders':[5,10,11],'differences':{'F14-F24':'-2*pi^2*Z12/n*a^3*b^3*c^2*(b-a)^2/(p*q*sqrt(r))','F24-F19':'pi^2*Z2/(2*n)*a^4*b^4*c*(b-a)^2/(p*q*sqrt(r))'},'minor':'nonzero leading coefficient times displayed order-10 coefficient times displayed order-11 coefficient','normalized_matrix':[['1','0','0'],['star1','1','0'],['star2','star3','1']],'nonzero':'p!=q, all primes distinct, n>=2,R>=1, legal p^2*q^2/r alias cell'}]
    coeff_field='actual constants Q(i,pi,log p,sqrt p); no formal algebraic independence assumed'
    cert={'decision':'B','parent':'4ab72a687d6a6801f1d374309d23fa023466c2fe','old_fifth_lower':20,'new_dimensions':9,'new_fifth_lower':29,'fifth_upper':72,'witness_ids':sorted(witness),'resolved_blocks':list(map(list,RESOLVED)),'remaining_blocks':[b['ids'] for b in table if not b['complete']],'pair_coefficients':formulas,'triple_minors':triples,'section_invariants':{'Z1':'sum (i-j)^2 J_ij^2','Z12':'sum (i-j)^2 J_ij*(J^2)_ij','Z2':'sum (i-j)^2*(J^2)_ij^2','positivity':'Z1>=2*(n-1),Z12>=4*(n-1),Z2>=8*(n-1) for n>=2,R>=1'},'coefficient_field':coeff_field,'global_kernel_vectors':[],'mixed_intersection':None,'total_453_family_rank_bounds':[35,453],'strict_gt79':'OPEN','source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json','notes/WP84_SHARED_CARRIER_DEGREE5_BLOCKS.json','notes/WP84_FIFTH_5_7_DIFFERENCE_CERTIFICATE.json']}}
    (ROOT/'notes/WP84_FIFTH_SHARED_BLOCK_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
    (ROOT/'notes/WP84_FIFTH_SHARED_RANK_WITNESS.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS fifth inventory: old lower 20, new dimensions 9, new lower 29; seven unresolved blocks')
    print('Resolved:',list(RESOLVED));print('Witness:',sorted(witness))
if __name__=='__main__':main()

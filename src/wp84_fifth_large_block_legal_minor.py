"""Machine-checkable rational enclosure of legal prime-log ratio minors."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def first(k,e):
 lo=2*k*k-2*(k+e);hi=2*(k+e)**2-2*k
 denlo=k*k*(2*k-2);denhi=(k+e)**2*(2*(k+e)-2)
 assert lo>0 and denlo>0
 return [-hi/denlo,-lo/denhi]
def second(k,e):return [(1+1/(k+e))/2,(1+1/k)/2]
def main():
 e=Q(1,100);r2=first(Q(2),e);r3=first(Q(3),e);det18=[r3[0]-r2[1],r3[1]-r2[0]];assert det18[0]>0
 r6=second(Q(6,5),e);r32=second(Q(3,2),e);det40=[r32[0]-r6[1],r32[1]-r6[0]];assert det40[1]<0
 out={'log_error_bound':str(e),'condition':'p>=2^100; q,r in [p^k,2p^k]; existence for sufficiently large p by PNT','block18_ratio_intervals':[[str(x) for x in r] for r in [r2,r3]],'block18_normalized_determinant_interval':list(map(str,det18)),'blocks40_41_ratio_intervals':[[str(x) for x in r] for r in [r6,r32]],'blocks40_41_normalized_determinant_interval':list(map(str,det40)),'exact_nonzero':True}
 (ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_LEGAL_MINOR_INTERVALS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()

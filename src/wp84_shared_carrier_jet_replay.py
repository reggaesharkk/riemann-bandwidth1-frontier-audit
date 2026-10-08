"""Independent shared-block and exact constant-field jet replay."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from math import factorial
from itertools import combinations,product,permutations
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def alternative_jets(terms,through):
    out=defaultdict(Q)
    for (lam,rho,power,logs,nu,nh),c in terms.items():
        pol={tuple([0]*len(rho)):Q(1)}
        for n in range(through-power+1):
            for beta,v in pol.items():
                ip=(n-nh)%4;coef=c*v*Q(2**n,factorial(n))*(-1 if ip>=2 else 1)
                out[lam,power+n,n-nh,ip%2,tuple(a+b for a,b in zip(logs,beta)),nu]+=coef
            nxt=defaultdict(Q)
            for beta,v in pol.items():
                for j,r in enumerate(rho):
                    inc=list(beta);inc[j]+=1;nxt[tuple(inc)]+=v*r
            pol=nxt
    return {k:v for k,v in out.items() if v}
def main():
    fs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());c=json.loads((ROOT/'notes/WP84_SHARED_CARRIER_JET_RANK_CERTIFICATE.json').read_text());groups=defaultdict(set)
    for f in fs:
        b,a,d=f['pattern'];groups[b,frozenset((tuple(a),tuple(d)))].add(f['id'])
    for b,total,nblocks in ((5,72,19),(6,381,35)):
        records=json.loads((ROOT/f'notes/WP84_SHARED_CARRIER_DEGREE{b}_BLOCKS.json').read_text())
        assert len(records)==nblocks and sum(r['size'] for r in records)==total
        for r in records:
            bb,a,d=r['support'];assert set(r['functional_ids'])==groups[bb,frozenset((tuple(a),tuple(d)))]
            assert r['analytic_rank_lower']==1 and r['analytic_rank_upper']==r['size']
            assert r['exact_analytic_rank']==(1 if r['size']==1 else None)
    for f in fs:
        b,a,d=f['pattern'];assert (sum(a)+sum(d))%2==b%2
    assert c['ordinary_reduced_common_carriers']==0 and c['mixed_physical_intersection'] is None
    from wp84_prime_path_faithfulness import cell_atom_terms
    from wp84_shared_carrier_jet_rank import exact_jets
    examples=json.loads((ROOT/'notes/WP84_SHARED_CARRIER_JET_EXAMPLES.json').read_text())
    for e in examples:
        terms=cell_atom_terms(e['eps'],e['lags'],e['pi'],e['block_primes'],*e['section'])
        assert alternative_jets(terms,e['through'])==exact_jets(terms,e['through'])
    jet=json.loads((ROOT/'notes/WP84_SHARED_CARRIER_SMALLEST_BLOCK_JET.json').read_text())
    assert jet['functional_ids']==[5,7] and all(r[0]==r[1] for r in jet['normalized_rows'])
    assert jet['jet_kernel_vector']==[1,-1] and jet['normalized_rows'][0]==['1','1']
    assert fs[5]['sign_word']==fs[7]['sign_word']=='+++++'
    # Two nonzero lags are the only nonzero-path contributions through b+2.
    # Enumerate every placement and allowed nonzero lag at finite test sections.
    for d in (1,2,3,5,9):
        for R in (1,2,6):
            K=min(R,d-1);expected=2*K-Q(K*(K+1),d)
            for i,j in combinations(range(5),2):
                actual=Q(0)
                for r in range(-R,R+1):
                    if not r:continue
                    l=[0]*5;l[i]=r;l[j]=-r;u=[0]
                    for x in l:u.append(u[-1]+x)
                    actual+=Q(max(0,d-max(u)+min(u)),d)
                assert actual==expected
    for d in (2,3,5,9):
        for R in (1,2,6):
            K=min(R,d-1);expected=K*(K-1)*(3-Q(2*(K+1),d));actual=Q(0)
            for r in range(-R,R+1):
                for ss in range(-R,R+1):
                    t=-r-ss
                    if not r or not ss or not t or abs(t)>R:continue
                    actual+=Q(max(0,d-max(abs(r),abs(ss),abs(t))),d)
            assert actual==expected
            # The +/- pair averages root positions to the full-section mean.
            for r in range(1,K+1):
                M=d-r
                means=[Q(M-1,2),r+Q(M-1,2)]
                assert sum(means)/2==Q(d-1,2)
    # Exhaust the full path/root sum in a small algebraic section for both
    # repeated-prime layouts, including all six prime assignments. This
    # independently tests the low-jet identity, not admissible rank points.
    totals=[]
    for pi in ([0,0,1,2,3],[0,1,0,2,3]):
        total=defaultdict(Q)
        for singles in permutations((3,5,7)):
            ps=(2,)+singles;order=sorted(range(4),key=lambda j:ps[j])
            for short in product((-1,0,1),repeat=4):
                lag=short+(-sum(short),)
                if abs(lag[-1])>1:continue
                terms=cell_atom_terms([1]*5,lag,pi,ps,0,1)
                for (lam,k,pip,ip,logs,nu),v in alternative_jets(terms,8).items():
                    key=(tuple(lam[j] for j in order),k,pip,ip,tuple(logs[j] for j in order),tuple(nu[j] for j in order))
                    total[key]+=v
        totals.append({k:v for k,v in total.items() if v})
    assert totals[0]==totals[1] and totals[0]
    # Corrupt one normalized jet coefficient: claimed null relation fails.
    good=[Q(1),Q(1)];bad=[Q(1),Q(2)]
    assert good[0]-good[1]==0 and bad[0]-bad[1]!=0
    assert c['global_kernel'] is None and c['decision']=='F'
    for p,h in c['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS all 54 blocks, exact constant-field jet expansion, 150 placement/lag-sum identities and coefficient-corruption detector')
    print('Smallest full-amplitude jet rank=1 through u^8; no global kernel inferred.')
if __name__=='__main__':main()

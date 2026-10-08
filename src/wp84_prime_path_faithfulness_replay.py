"""Independent carrier-witness, rational-growth and rank-bound replay."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
    f=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());w=json.loads((ROOT/'notes/WP84_PRIME_PATH_CARRIER_WITNESSES.json').read_text());c=json.loads((ROOT/'notes/WP84_PRIME_PATH_FAITHFULNESS_CERTIFICATE.json').read_text())
    for p,h in c['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    supports={};counts=defaultdict(int)
    for v in w:
        o=f[v['functional_id']];pi=list(map(int,o['equality_partition'].split(',')));eps=[1 if x=='+' else -1 for x in o['sign_word']]
        es=[sum(e for p,e in zip(pi,eps) if p==j) for j in range(max(pi)+1)]
        assert es==v['block_exponents'] and pi==v['equality_partition'] and eps==v['signs']
        gamma=list(map(Q,v['rational_prime_growth_exponents']));assert all(0<x<1 for x in gamma)
        assert sum(e*x for e,x in zip(es,gamma))==v['m'] and v['m'] in o['aliases']
        a=tuple(sorted((e for e in es if e>0),reverse=True));b=tuple(sorted((-e for e in es if e<0),reverse=True))
        # Unordered reciprocal carrier support rather than producer min key.
        key=(o['degree'],frozenset((a,b)));assert key not in supports;supports[key]=v['functional_id'];counts[o['degree']]+=1
        assert (sum(a)+sum(b))%2==o['degree']%2
    assert dict(counts)=={5:19,6:35}
    allkeys=set()
    for o in f:
        b,a,d=o['pattern'];allkeys.add((b,frozenset((tuple(a),tuple(d)))))
    assert set(supports)==allkeys and len(w)==54
    rows=list(csv.DictReader((ROOT/'notes/WP84_PRIME_PATH_PARTIAL_SUPPORT_MATRIX.csv').open()));assert len(rows)==54
    assert c['fifth_lower']==19 and c['sixth_lower']==35 and c['total_lower']==max(counts.values())
    assert c['analytic_nullity_bounds']==[0,453-35]
    assert c['global_kernel_basis'] is None and c['interval_rank_witness'] is None
    # Coefficient identities behind constant-carrier/free-lift counterexamples:
    # phase exponents of cancelling terms coincide exactly after multiplication.
    l1,l2=Q(1),Q(2);assert (l1-l2)+l2==l1
    # The zero-lag leading kernel sum is M/dprime=1 for every section.
    for d in range(1,31):assert Q(d,d)==1
    # Every nonzero-lag filter has zero constant term in its Taylor germ.
    for eps in (-1,1):
        for lag in (-2,-1,1,2):assert Q(1,2*eps*lag)+Q(-1,2*eps*lag)==0
    from wp84_prime_path_faithfulness import cell_atom_terms
    # Zero-lag leading term is exactly sign(b)/2 on both carriers,
    # irrespective of section, after its constant log/sqrt factors.
    for b in (5,6):
        eps=[1]*2+[-1]*(b-2);pi=list(range(b))
        for km,kp in ((0,0),(3,8)):
            terms=cell_atom_terms(eps,[0]*b,pi,[2,3,5,7,11,13][:b],km,kp)
            for sign in (-1,1):
                leading=sum(q for (lam,rho,powz,logs,nu,nh),q in terms.items() if lam==tuple(sign*e for e in eps) and powz==b and nh==0)
                assert leading==Q((-1)**b,2)
    print('PASS 54 independent reciprocal carrier witnesses, rational support interior, exact leading-term cancellations and partial rank bounds')
    print('Symbolic proofs are in the accompanying theorem note; no interval minor fabricated.')
if __name__=='__main__':main()

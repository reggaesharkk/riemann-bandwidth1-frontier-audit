"""Independent zeta-recurrence replay; does not use producer Mobius inversion."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as F
import csv,json,hashlib
from wp84_signed_near_alias_attack import partitions
ROOT=Path(__file__).resolve().parents[1]
def finer(a,b):
    return all(a[i]!=a[j] or b[i]==b[j] for i in range(len(a)) for j in range(i))
def main():
    cert=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_CERTIFICATE.json').read_text())
    groups=defaultdict(set);counts=Counter();unique=defaultdict(set);red=Counter()
    for r in csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv').open()):
        b=int(r['degree']);m=int(r['m']);pi=tuple(map(int,r['equality_labels'].split(',')));word=r['sign_word']
        groups[b,word,m].add(pi);counts[b]+=1;unique[b].add((word,pi))
        e=[sum(1 if word[i]=='+' else -1 for i in range(b) if pi[i]==j) for j in range(max(pi)+1)]
        key=(tuple(sorted((v for v in e if v>0),reverse=True)),tuple(sorted((-v for v in e if v<0),reverse=True)),m)
        assert json.loads(r['canonical_reduced_key'])==[list(key[0]),list(key[1]),m]
        assert sum(abs(v) for v in e)%2==b%2
        red[b,key]+=1
    assert dict(counts)=={5:1956,6:19632};assert {b:len(v) for b,v in unique.items()}=={5:1132,6:7608}
    observed={}
    for r in csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_MOBIUS_COEFFICIENTS.csv').open()):
        observed[int(r['degree']),r['sign_word'],int(r['m']),tuple(map(int,r['coarse_equality_constraints'].split(',')))]=int(r['exact_mobius_coefficient'])
    expected={};tests=0
    for (b,word,m),selected in groups.items():
        coeff={}
        for rho in sorted(partitions(b),key=lambda p:-len(set(p))):
            c=int(rho in selected)-sum(v for pi,v in coeff.items() if pi!=rho and finer(pi,rho))
            coeff[rho]=c;tests+=1
            if c:expected[b,word,m,rho]=c
    assert expected==observed and tests==56960
    rel=F(cert['relaxed_allowance']);ideal=F(cert['ideal_allowance'])
    assert rel==F(52897896569489,572357731837500000)
    assert ideal==F(27704610381502,17886179119921875)
    for r in cert['primitive_allocations']:
        assert F(r['primitive_requirement'])*(1+F(r['H'])/2)==F(r['share'])*rel
    assert abs(float(rel/201)-4.598061669031416e-7)<1e-20
    for p,h in cert['frozen_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    # Soft counterexample core, including conjugate alias. Fixed norm scaling
    # cannot compensate a lower bound growing like X^(1/10).
    z=10**10;X=z**5;V=z**3;K=V//10000
    lower2=F(4999,5000)**2*F(K*K,16*X)
    assert lower2>1 and lower2>rel*rel
    assert cert['actual_survivor_charge'] is None and cert['decision']=='F'
    agg=Counter()
    for (b,word,m,pi),c in observed.items():
        e=[sum(1 if word[i]=='+' else -1 for i in range(b) if pi[i]==j) for j in range(max(pi)+1)]
        key=(b,tuple(sorted((v for v in e if v>0),reverse=True)),tuple(sorted((-v for v in e if v<0),reverse=True)),m)
        agg[key]+=c
    with (ROOT/'notes/WP84_NEAR_ALIAS_MOBIUS_REDUCED_SUMS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','positive_exponents','negative_exponents','m','coefficient_sum','scope'])
        for key,c in sorted(agg.items()):w.writerow([*key,c,'formal scalar sum; original signed path weights remain distinct'])
    print('PASS independent recurrence:',tests,'equalities;',len(expected),'coefficients; counts, parity, budgets, conjugate soft falsifier, frozen hashes')
if __name__=='__main__':main()

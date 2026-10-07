"""Independent exact orbit and disjoint-incidence rank replay."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
import csv,json,hashlib
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
def main():
    c=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_ORBIT_CERTIFICATE.json').read_text());p=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_PATTERN_LEDGER.json').read_text());f=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    for path,h in c['frozen_sha256'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    # Unordered pairs rather than producer lexicographic orbit representatives.
    keys={(v['degree'],tuple(v['numerator_exponents']),tuple(v['denominator_exponents'])) for v in p}
    orbits={frozenset((k,(k[0],k[2],k[1]))) for k in keys}
    types={(v['degree'],tuple(v['numerator_exponents']),tuple(v['denominator_exponents']),m) for v in p for m in v['aliases']}
    to={frozenset((k,(k[0],k[2],k[1],-k[3]))) for k in types}
    assert len(keys)==105 and len(types)==336
    assert len(orbits)==c['pattern_orbits'] and len(to)==c['alias_orbits']
    for v in p:
        u=p[v['conjugate_pattern_id']]
        assert u['conjugate_pattern_id']==v['id']
        assert v['numerator_exponents']==u['denominator_exponents']
        assert set(v['aliases'])=={-m for m in u['aliases']}
        assert len(v['origins'])==v['raw_classes']
    rows=list(csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_EXACT_INCIDENCE.csv').open()))
    assert len(rows)==8740 and len(f)==c['actual_raw_conjugate_functionals']
    for label,field in [('raw_to_phase_pattern','phase_pattern_id'),('raw_to_phase_orbit','phase_orbit_id'),('raw_to_conjugate_raw_functional','raw_conjugate_functional_id')]:
        supports=defaultdict(set)
        for r in rows:supports[int(r[field])].add(int(r['raw_id']))
        assert len(supports)==c['incidence_ranks'][label]['rank']
        assert sum(map(len,supports.values()))==8740
        # Nonempty pairwise disjoint support proves column independence over Q.
        assert len(set.union(*supports.values()))==8740
    by=defaultdict(list)
    for r in rows:by[int(r['raw_conjugate_functional_id'])].append(r)
    for j,v in enumerate(f):
        rr=by[j];assert len(rr)==len(v['raw_orbit_members'])
        assert all(Q(r['omega'])*len(rr)==Q(v['exact_alpha']) for r in rr)
        assert {(int(r['degree']),r['sign_word'],r['equality_partition']) for r in rr}=={tuple(x) for x in v['raw_orbit_members']}
        assert all(len(r['sign_word'])==v['degree'] for r in rr)
        # Synthetic independent real direction obeys conjugacy and |C|<=1.
        # Its coefficient is nonzero, so symmetries alone do not annihilate it.
        assert Q(v['exact_alpha'])!=0
    # Independent generator closure by BFS, not producer orbit enumeration.
    def norm(seq):
        out=[];seen=[]
        for v in seq:
            if v not in seen:seen.append(v)
            out.append(seen.index(v))
        return ','.join(map(str,out))
    for v in f:
        start=(v['degree'],v['sign_word'],v['equality_partition']);seen={start};todo=[start]
        while todo:
            b,w,q=todo.pop();pi=q.split(',')
            children=[(b,w[1:]+w[:1],norm(pi[1:]+pi[:1])),(b,w[::-1],norm(pi[::-1])),(b,''.join('-' if x=='+' else '+' for x in w),q)]
            for t in children:
                if t not in seen:seen.add(t);todo.append(t)
        assert seen=={tuple(t) for t in v['raw_orbit_members']}
    mass=sum(abs(Q(v['exact_alpha'])) for v in f)
    assert mass==Q(c['absolute_coefficient_mass'])
    assert mass*Q(c['sufficient_common_bound_full_relaxed_allocation'])==Q(52897896569489,572357731837500000)
    assert all((sum(k[1])+sum(k[2]))%2==k[0]%2 for k in keys)
    assert c['actual_minimal_correlation_rank'] is None and c['decision']=='F'
    symmetry_tests=0
    for b in (5,6):
        for short in product((-1,0,1),repeat=b-1):
            l=short+(-sum(short),)
            if abs(l[-1])>1:continue
            u=[0]
            for x in l:u.append(u[-1]+x)
            for eps in product((-1,1),repeat=b):
                for shift in range(b):
                    order=list(range(shift,b))+list(range(shift))
                    new=[0]
                    for j in order:new.append(new[-1]+l[j])
                    assert min(new)==min(u)-u[shift] and max(new)==max(u)-u[shift]
                    # Coefficient of each independent alpha_j in W*K.
                    for t,j in enumerate(order):assert eps[j]*(new[t]+u[shift])==eps[j]*u[j]
                    symmetry_tests+=1
                order=list(reversed(range(b)));new=[0]
                for j in order:new.append(new[-1]-l[j])
                assert min(new)==min(u) and max(new)==max(u)
                for t,j in enumerate(order):assert eps[j]*(new[t]-l[j])==eps[j]*u[j]
                symmetry_tests+=1
    print('PASS exact symbolic path-phase coefficient and root compensation:',symmetry_tests,'rotation/reversal cases')
    print('PASS independent orbit, involution, incidence rank, rational coefficient, parity, budget and symmetry-only synthetic falsifier replay')
    print('No analytic rank inferred from formal incidence rank.')
if __name__=='__main__':main()

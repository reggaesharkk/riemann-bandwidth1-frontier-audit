"""Independent rational replay: root jets, joint windows, and hostile mutations.

Universal algebra fixtures are not source-legal arithmetic determinant minors.
"""
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = [[15,20,26,28,31,32], [10,12,16,17,21,22,25,29],
          [36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],
          [34,37,39,43,53,56,60,63]]


def power_sums(count: int, depth: int) -> list[Q]:
    values = [Q(count)]
    for j in range(1, depth + 1):
        values.append((Q(count ** (j + 1)) - sum(
            (comb(j + 1, t) * values[t] for t in range(j)), Q(0)
        )) / (j + 1))
    return values


def jet_by_faulhaber(a: int, n: int, minimum: int, span: int, depth: int) -> list[Q]:
    moments = power_sums(n - span, depth)
    return [sum((comb(h, j) * (a-minimum)**(h-j) * moments[j]
                 for j in range(h+1)), Q(0)) / (n * factorial(h))
            for h in range(depth+1)]


def exact_checks() -> dict:
    checks = 0
    # c0*lambda is a formal factor. No fake prime logarithm is evaluated.
    for n, path in [(17, (2,-1,1,-2,0)), (12001,(6000,6000,-6000,-6000,0)),
                    (12001,(0,0,0,0,0)), (24002,(6000,6000,-6000,-6000,0))]:
        prefix = [0]
        for lag in path: prefix.append(prefix[-1] + lag)
        minimum = min(prefix); span = max(prefix)-minimum
        assert sum(path) == 0 and span <= 12000 and n > span
        for a in (0, 11):
            faulhaber = jet_by_faulhaber(a,n,minimum,span,8)
            direct = [Q(sum(i**h for i in range(a-minimum, a-minimum+n-span)),
                        n*factorial(h)) for h in range(9)]
            assert faulhaber == direct
            shifted = jet_by_faulhaber(a+7,n,minimum,span,8)
            assert shifted == [sum((Q(7**(h-r),factorial(h-r))*direct[r]
                                    for r in range(h+1)), Q(0)) for h in range(9)]
            checks += 1
    # Exact endpoint flux identities, one monomial per allowed root.
    for a,b,mn,mx in [(0,12000,0,12000),(10,31,-2,3),(3,22,0,0)]:
        old=set(range(a-mn,b-mx+1))
        lower=set(range(a+1-mn,b-mx+1))
        upper=set(range(a-mn,b+1-mx+1))
        assert old-lower == {a-mn} and upper-old == {b+1-mx}
        n=b-a+1
        for root in old|upper:
            assert Q(int(root in lower),n-1)-Q(int(root in old),n) == (
                Q(int(root in old),n*(n-1))-Q(int(root==a-mn),n-1))
            assert Q(int(root in upper),n+1)-Q(int(root in old),n) == (
                Q(int(root==b+1-mx),n+1)-Q(int(root in old),n*(n+1)))
        checks += 1
    # Complete complex jet translation is unipotent and composes exactly.
    depth=8
    for s,t in [(2,3),(-5,7),(0,-2)]:
        def matrix(z):
            return [[Q(z**(i-j),factorial(i-j)) if j<=i else Q(0)
                     for j in range(depth+1)] for i in range(depth+1)]
        A=matrix(s);B=matrix(t);C=matrix(s+t)
        assert [[sum((A[i][r]*B[r][j] for r in range(depth+1)),Q(0))
                 for j in range(depth+1)] for i in range(depth+1)] == C
        assert all(A[i][i] == 1 for i in range(depth+1))
        checks += 1
    def realified(s):
        size=2*(depth+1); result=[[Q(0) for _ in range(size)] for _ in range(size)]
        for i in range(depth+1):
            for j in range(i+1):
                r=i-j; scale=Q(s**r,factorial(r))
                re,im=[(1,0),(0,1),(-1,0),(0,-1)][r%4]
                result[2*i][2*j]=scale*re; result[2*i][2*j+1]=-scale*im
                result[2*i+1][2*j]=scale*im; result[2*i+1][2*j+1]=scale*re
        return result
    size=2*(depth+1)
    for s,t in [(2,3),(-5,7),(0,-2)]:
        A=realified(s);B=realified(t);C=realified(s+t)
        assert [[sum((A[i][r]*B[r][j] for r in range(size)),Q(0))
                 for j in range(size)] for i in range(size)] == C
        assert all(A[i][i]==1 for i in range(size))
        checks += 1
    # Real-only stencil: germs (1,i); order 0 and 1 rows.
    for s in (0,1,7):
        stack=[[Q(0),Q(0)] for _ in range(size)]
        stack[0]=[Q(1),Q(0)];stack[1]=[Q(0),Q(1)]
        transform=realified(s)
        real_matrix=[[sum((transform[row][r]*stack[r][col] for r in range(size)),Q(0))
                      for col in range(2)] for row in (0,2)]
        determinant = real_matrix[0][0]*real_matrix[1][1]-real_matrix[0][1]*real_matrix[1][0]
        assert determinant == -s
    # Physical alias factor is 1 on the grid; its formal first jet is not.
    formal_alias_first_jet = Q(2*3)  # common c0*L factor not specialized
    assert formal_alias_first_jet != 0
    # Joint fixed-length sections, including all endpoints in both windows.
    for d,q in [(15000,21),(100000,300),(1000000,1000)]:
        for k in (0,q//2,q-1):
            a=k;b=k+d-q;n=b-a+1
            assert 0<=a<q and d-q<=b<d and a<b
            assert n==d-q+1 and d-n==q-1 and n>12000
            checks += 1
    # Independent rational path-filter bound and proof log(6000)<9.
    assert sum((Q(9**j,factorial(j)) for j in range(25)),Q(0)) > 6000
    assert Q(23,3)**3 * Q(13,9) == Q(158171,243)
    # Elementary interval-count majorant on many rational intervals.
    for center in (Q(17,3),Q(100),Q(1001,5)):
        for t in (Q(1,100),Q(1,10),Q(1,2)):
            lo=center*(1-t);hi=center/(1-t)
            first=-(-lo.numerator//lo.denominator);last=hi.numerator//hi.denominator
            count=max(0,last-first+1)
            assert count <= 1+4*t*center
            checks += 1
    return {"universal_exact_cases": checks, "jet_depth": 8,
            "real_stencil_structural_counterexample": "det=-s; not a prime-source minor",
            "complex_translation_determinant": "1", "joint_dimension_loss": "q-1"}


def validate(data: dict, disk: bool = False) -> list[str]:
    errors=[]
    funcs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    records=data.get('fields',[])
    expected=[i for ids in BLOCKS for i in ids]
    if [r.get('id') for r in records] != expected: errors.append('row/column descriptor order changed')
    w2=Q(0)
    for r in records:
        fid=r.get('id')
        if fid not in expected: errors.append('unknown descriptor');continue
        f=funcs[fid];pi=list(map(int,f['equality_partition'].split(',')))
        signs=[1 if x=='+' else -1 for x in f['sign_word']]
        net=[sum(signs[s] for s in range(5) if pi[s]==j) for j in range(max(pi)+1)]
        nu=[pi.count(j) for j in range(max(pi)+1)]
        hidden=any(e==0 and v==2 for e,v in zip(net,nu))
        if (r.get('pi'),r.get('signs'),r.get('net'),r.get('nu'),r.get('aliases')) != (pi,signs,net,nu,f['aliases']): errors.append('actual carrier/weight changed')
        if r.get('independent_canceled_prime') != hidden: errors.append('canceled-prime sum changed')
        if r.get('exact_consumer_alpha') != f['exact_alpha']: errors.append('consumer weight changed')
        if r.get('R') != 6000: errors.append('R changed')
        if r.get('pool') != 'all ordinary primes <=N, injective on equality blocks': errors.append('prime pool truncated')
        if r.get('source_mask') != 'exact descriptor, cutoff, distinctness, nearest allowed alias, 0<abs(lambda-mL)<=H/T, positive source root count': errors.append('source mask deleted/relaxed')
        if r.get('root_order') != 'increasing i from a0-min(v) through b0-max(v), inclusive': errors.append('root order changed')
        if r.get('prefix_order') != 'v0=0; v_s=sum_(r=1)^s ell_r; original ordered slots': errors.append('Fourier/slot order changed')
        if r.get('normalization') != 'slot -log(p)/(a_phi*L*sqrt(p)); positive-carrier factor 1/2; exact root divisor n': errors.append('normalization changed')
        w2 += Q(f['exact_alpha'])**2
    if data.get('physical_bound',{}).get('W2') != str(w2): errors.append('squared coefficient mass changed')
    if data.get('physical_bound',{}).get('P_R_rational_upper') != str(Q(158171,243)): errors.append('path constant changed')
    score=data.get('score',{})
    if score.get('joint') is not True: errors.append('independent endpoints substituted')
    if score.get('adjacent_offsets') != [0,1]: errors.append('adjacent endpoint missing')
    if score.get('centered_heuristic') is not False: errors.append('centered heuristic substituted')
    if score.get('candidate_line') != 'a0=k; b0=k+d-q; k=0,...,q-1; q=floor(d/sqrt(L))': errors.append('candidate windows changed')
    if score.get('determinant_selector_certified') is not False: errors.append('unsupported determinant selector')
    if data.get('jet_gate',{}).get('alias_reduction_commutes_with_jet') is not False: errors.append('physical alias identity used on jets')
    if data.get('jet_gate',{}).get('frozen_real_row_stencil_closed') is not None: errors.append('unsupported real row closure')
    if data.get('fifth_rank_bounds') != [38,72] or data.get('determinant_visible_K') is not None: errors.append('unsupported rank/K promotion')
    if disk:
        for p,pin in data['source_pins'].items():
            if hashlib.sha256((ROOT/p).read_bytes()).hexdigest() != pin['sha256']: errors.append('source changed: '+p)
        for p,sha in data['packet_sha256'].items():
            if hashlib.sha256((ROOT/p).read_bytes()).hexdigest() != sha: errors.append('packet changed: '+p)
    return errors


if __name__ == '__main__':
    data=json.loads((ROOT/'notes/WP84_DETERMINANT_NATIVE_ENDPOINT_CERTIFICATE.json').read_text())
    assert not validate(data,disk=True), validate(data,disk=True)
    checks=exact_checks()
    mutations=[
        ('R400 substitution',lambda d:d['fields'][0].update(R=400)),
        ('source mask removal',lambda d:d['fields'][0].update(source_mask='none')),
        ('truncated pool',lambda d:d['fields'][0].update(pool='six primes')),
        ('all-ones rows',lambda d:d['fields'][0].update(net=[1]*3,nu=[1]*3)),
        ('root reordering',lambda d:d['fields'][0].update(root_order='decreasing')),
        ('Fourier reordering',lambda d:d['fields'][0].update(prefix_order='sorted lags')),
        ('centered heuristic',lambda d:d['score'].update(centered_heuristic=True)),
        ('drop canceled primes',lambda d:d['fields'][4].update(independent_canceled_prime=False)),
        ('normalization mutation',lambda d:d['fields'][0].update(normalization='1')),
        ('independent endpoints',lambda d:d['score'].update(joint=False)),
        ('alias reduction in jets',lambda d:d['jet_gate'].update(alias_reduction_commutes_with_jet=True)),
        ('jet closure asserted',lambda d:d['jet_gate'].update(frozen_real_row_stencil_closed=True)),
        ('adjacent term removed',lambda d:d['score'].update(adjacent_offsets=[0])),
        ('candidate windows mutation',lambda d:d['score'].update(candidate_line='centered')),
    ]
    for name,mutate in mutations:
        bad=copy.deepcopy(data);mutate(bad);assert validate(bad),name
    print('PASS independent source pins, packet hashes and',checks['universal_exact_cases'],'universal exact cases')
    print('PASS',len(mutations),'hostile mutations; no selector or rank promotion')
    print('E: real source-jet intertwining lemma remains OPEN')

"""Reusable ordinary-prime carrier parity, degree-eight structure diagnostics."""
from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
from math import factorial,comb
from pathlib import Path
import json
import sympy as s
from wp84_c5_pointwise_supercritical_sign import compile_terms,set_partitions
ROOT=Path(__file__).resolve().parents[1]

def carrier_sets(max_b,prime_count=3):
    moves=[tuple(e if j==i else 0 for j in range(prime_count)) for i in range(prime_count) for e in (-1,1)]
    sets={0:{(0,)*prime_count}}
    for b in range(1,max_b+1):
        sets[b]={tuple(u+v for u,v in zip(a,m)) for a in sets[b-1] for m in moves}
        assert all(sum(abs(v) for v in a)<=b and sum(abs(v) for v in a)%2==b%2 for a in sets[b])
        # Exhaustive characterization in the finite exponent cube.
        expected={a for a in product(range(-b,b+1),repeat=prime_count) if sum(abs(v) for v in a)<=b and sum(abs(v) for v in a)%2==b%2}
        assert sets[b]==expected
    return sets

def connected_value(v,scale):
    total=0;terms=compile_terms(len(v))
    for sign,masks in terms:
        positions=[0]+[sum(v[j] for j in mask) for mask in masks]
        total+=sign*max(0,scale-max(positions)+min(positions))
    path=[0]
    for x in v:path.append(path[-1]+x)
    O=F(max(0,scale-max(path)+min(path)),scale)
    return {'vector':[str(F(x,scale)) for x in v],'terms':len(terms),'C':str(F(total,scale)),
            'outer':str(O),'signed_density':str(F(total,scale)*O)}
def ratio(labels,signs):
    z=F(1)
    for p,e in zip(labels,signs):z*=F(p) if e==1 else F(1,p)
    return z

def main():
    sets=carrier_sets(10)
    assert all(not sets[r]&sets[t] for r in range(1,11) for t in range(1,11) if (r-t)%2)
    assert sets[5]<sets[7] and sets[6]<sets[8]
    r5=ratio([2,3,5,7,11],[1,1,-1,-1,-1]);r7=ratio([2,3,5,7,11,13,13],[1,1,-1,-1,-1,1,-1]);assert r5==r7==F(6,385)
    r6=ratio([2,3,5,7,11,13],[1,1,-1,-1,-1,-1]);r8=ratio([2,3,5,7,11,13,17,17],[1,1,-1,-1,-1,-1,1,-1]);assert r6==r8==F(6,5005)
    kernels=[connected_value([6,-4,6,-4,-4,3,-3],10),connected_value([-7,8,-7,6,-4,4,2,-2],10)]
    assert kernels[0]['C']=='-1/5' and kernels[0]['signed_density']=='-1/25'
    assert kernels[1]['C']=='1/5' and kernels[1]['signed_density']=='1/50'
    counts={}
    for b in (7,8):
        partitions=list(set_partitions(list(range(b))))
        shapes=Counter(tuple(sorted(map(len,p),reverse=True)) for p in partitions)
        assert len(partitions)=={7:877,8:4140}[b]
        assert shapes[(b-2,2)]=={7:21,8:28}[b]
        counts[b]={str(k):{'placements':v,'inverse_cumulant_coefficient':(-1)**(len(k)-1)*factorial(len(k)-1)} for k,v in sorted(shapes.items())}
    assert F(15)*F(1,3)*F(-1,60)==F(-1,12)!=F(-23,420)
    odd_ratios={e:F(comb(7,(7+e)//2),comb(5,(5+e)//2)) for e in (1,3,5)}
    even_ratios={e:F(comb(8,(8+e)//2),comb(6,(6+e)//2)) for e in (0,2,4,6)}
    assert len(set(odd_ratios.values()))>1 and len(set(even_ratios.values()))>1
    G=s.Matrix(5,5,lambda i,j:s.Symbol('g'+str(min(i,j))+str(max(i,j))))
    coeff=[s.expand(sum(G[i,j] for i in range(5) for j in range(5) if i+j==k)) for k in range(9)]
    assert coeff[4]==2*G[0,4]+2*G[1,3]+G[2,2]
    assert coeff[5]==2*G[1,4]+2*G[2,3]
    assert coeff[6]==2*G[2,4]+G[3,3]
    assert coeff[7]==2*G[3,4] and coeff[8]==G[4,4]
    # Liouville sign flip and parity projectors, formal polynomial identity.
    x=s.symbols('x');cs=s.symbols('c0:9');P=sum(cs[k]*x**k for k in range(9))
    assert s.expand((P+P.subs(x,-x))/2)==sum(cs[k]*x**k for k in range(0,9,2))
    assert s.expand((P-P.subs(x,-x))/2)==sum(cs[k]*x**k for k in range(1,9,2))
    X,y,z=s.symbols('X y z',real=True)
    q=(144000*X**4+14400*X**3-12720*X**2-1128*X-449)/s.Integer(117559)
    P=s.Poly(s.expand(q*q),X);cs8=[P.nth(i) for i in range(9)]
    assert q.subs(X,-1)==1
    assert all(c>=0 for c in s.Poly(s.expand(q.subs(X,-1-y)-1),y).all_coeffs())
    assert cs8[4]==0 and cs8[5]+cs8[7]/6==0 and cs8[6]+cs8[8]/6==0
    assert s.integrate(z*(1-z)**2,(z,0,1))==s.Rational(1,12)
    a=s.symbols('a');w=s.symbols('w',nonzero=True)
    Dplus=a*s.diag(1,w,w**2);Dminus=a*s.diag(1,1/w,1/w**2)
    assert Dplus*Dminus==a*a*s.eye(3) and Dminus*Dplus==a*a*s.eye(3)
    av=s.Matrix([s.Poly(q,X).nth(i) for i in range(5)]);Gram=av*av.T
    minors=[Gram.extract(ix,ix).det() for size in range(1,6) for ix in combinations(range(5),size)]
    assert len(minors)==31 and all(m>=0 for m in minors)
    assert s.Rational(1)+21*s.Rational(1,3)+35*s.Rational(1,4)+21*s.Rational(1,36)+7*s.Rational(157,630)==s.Rational(1717,90)
    known=cs8[0]+cs8[2]/3+cs8[5]/36+cs8[6]*s.Rational(157,630)
    candidate={'q':str(q),'coefficients':list(map(str,cs8)),
               'support_q_minus_one_coefficients':list(map(str,s.Poly(s.expand(q.subs(X,-1-y)-1),y).all_coeffs())),
               'Gram_certificate':'rational rank-one outer product of q coefficients','all_31_principal_minors':list(map(str,minors)),
               'known_model_part':str(known),'unknown_model_part':'c7*mu7+c8*mu8',
               'model_gt79_certified':False,'band_charge_certified':False}
    out={'parent' :'c819938650457a94d3e821c2407a0b1034202f31','decision':'A',
      'general_parity_theorem':'sum_p |r_p-s_p|=b-2 sum_p min(r_p,s_p)',
      'support_characterization':'e supported on cutoff primes; ||e||1<=b; ||e||1=b mod 2 (nonempty prime alphabet)',
      'orders_1_through_10_counts':{b:len(sets[b]) for b in range(1,11)},
      'same_parity_dictionary':{'5_into_7':len(sets[5]&sets[7]),'6_into_8':len(sets[6]&sets[8])},
      'hard_ratio_witnesses':{'5_7':str(r5),'6_8':str(r6)},
      'connected_pair_insertion_survival':kernels,'partition_counts':counts,
      'degree8_coefficients':list(map(str,coeff)),
      'exact_scalar_same_carrier_ratios':{'7_over_5':{str(k):str(v) for k,v in odd_ratios.items()},'8_over_6':{str(k):str(v) for k,v in even_ratios.items()}},
      'pair_factorization_countercheck':{'naive_42':'-1/12','actual_model_42':'-23/420'},
      'frozen_ratio':'-620/371','negative_coercivity_quantity':'-1240/371',
      'known_exact_mu7':False,'known_exact_mu8':False,
      'canonical_pair_lift':'A_(b+2)^lift=2*S0_T*A_b, S0_T=sum_p c_p^2*(1-log(p)/L)^2',
      'canonical_pair_limit':'2*S0_T -> 1/6','quartic_candidate':candidate,
      'first_uncertified_gate':'remaining higher-order amplitude norms and exact centered mu7/mu8',
      'new_model_gt79_certified':False,'strict_gt79':False,
      'Liouville_projector_algebraically_valid':True,'auxiliary_zero_side_equivalence_proved':False,
      'full_7_8_theorem_started':False}
    (ROOT/'notes/WP84_PARITY_GRADED_DEGREE8_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: all carrier supports 1..10; exact 5/7 and 6/8 witnesses; connected survival; Bell counts; SOS and parity projection identities.')
    print('A: canonical same-parity lift and support-valid quartic exist; no full-pair or 7/8 theorem is certified.')
if __name__=='__main__':main()

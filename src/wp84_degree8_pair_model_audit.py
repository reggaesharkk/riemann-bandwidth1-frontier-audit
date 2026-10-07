"""Exact pair-sector, Bell/Mobius and moment-completion audit; no guessed moments."""
from fractions import Fraction as F
from collections import Counter
from math import factorial,comb
from pathlib import Path
import json, subprocess, hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
def partitions(n):
    def rec(a):
        if len(a)==n:
            yield tuple(tuple(i for i,x in enumerate(a) if x==j) for j in range(max(a)+1));return
        for x in range(max(a)+2): yield from rec(a+[x])
    yield from rec([0])
def table(n):
    d=Counter(tuple(sorted(map(len,p),reverse=True)) for p in partitions(n))
    assert sum(d.values())=={7:877,8:4140}[n]
    for typ,count in d.items():
        den=1
        for t in typ:den*=factorial(t)
        for m in Counter(typ).values():den*=factorial(m)
        assert count==factorial(n)//den
    return {','.join(map(str,t)):{'count':v,'inverse_mobius':(-1)**(len(t)-1)*factorial(len(t)-1)} for t,v in sorted(d.items())}
def moment_certificate():
    m=list(map(s.Rational,['1','0','1/3','0','1/4','1/36','157/630']))
    H=s.Matrix(4,4,lambda i,j:m[i+j]);z=s.symbols('mu7');h=s.Matrix(m[4:]+[z])
    a=s.Matrix([-449,-1128,-12720,14400])/117559;t=s.Rational(144000,117559)
    f=s.expand((a.T*H*a)[0]+2*t*(a.T*h)[0]+t*t*(h.T*H.inv()*h)[0])
    opt=s.solve(s.diff(f,z),z)[0];lo=s.factor(f.subs(z,opt));curv=s.expand(f).coeff(z,2)
    assert all(H[:i,:i].det()>0 for i in range(1,5))
    assert s.expand(f-lo-curv*(z-opt)**2)==0
    assert lo>s.Rational(21,200)
    return {'lower_bound':str(lo),'completion_mu7_minimizer':str(opt),'square_coefficient':str(curv),'percentage_upper_bound':str(100*(1-2*lo)),'excess_over_21_200':str(lo-s.Rational(21,200)),'H_leading_minors':[str(H[:i,:i].det()) for i in range(1,5)],'mu7':'UNCERTIFIED','mu8':'UNCERTIFIED'}
def pairs():
    # Scalar Laurent special case disproves a universal full-sector scalar.
    out={}
    for b in (5,6):
        out[str(b)]={str(e):str(F(comb(b+2,(b+2+e)//2),comb(b,(b+e)//2))) for e in range(b%2,b+1,2)}
        assert len(set(out[str(b)].values()))>1
    # Admissible closed higher path whose only opposite pair cannot be deleted.
    lag=[1,1,-1,0,-1,0,0];assert sum(lag)==0 and all(abs(x)<=1 for x in lag)
    assert lag[0]+lag[1]!=0
    c=list(map(s.Rational,[201601,1012944,12694944,15765120,0,-691200000,-3456000000,4147200000,20736000000]))
    assert c[5]+c[7]/6==0 and c[6]+c[8]/6==0
    E5,E6,N7,N8,A5,A6=s.symbols('E5 E6 N7 N8 A5 A6')
    assert s.expand(c[5]*A5+c[6]*A6+c[7]*(A5/6+E5+N7)+c[8]*(A6/6+E6+N8)-c[7]*(E5+N7)-c[8]*(E6+N8))==0
    return {'scalar_laurent_ratios':out,'nondeletable_closed_path':lag,'canonical_multiplier':'2*S0_T -> 1/6','full_scalarization':False}
def inventory():
    files=['src/wp81_spec52_exact.py','src/wp81_spec52_verify.py','src/wp80_c7_full_orbit_batch.py','src/wp80_c7_full_orbit_aggregate.py','src/wp80_c7_symmetry_reduce.py','src/wp84_c5_pointwise_supercritical_sign.py','src/wp84_parity_graded_degree8_verify.py','src/wp84_parity_graded_degree8_recon.py']
    return {p:{'commit':'855a47a80f962c7d068ab5db233c36bc6f0e6852','git_blob':subprocess.check_output(['git','rev-parse','855a47a:'+p],cwd=ROOT,text=True).strip(),'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in files}
def main():
    result={'pair':pairs(),'partitions':{str(n):table(n) for n in (7,8)},'moment_certificate':moment_certificate(),'sources':inventory(),'integration_workload':{'C7_ordered_terms':9366,'C7_symmetry_orbits':397,'SPEC52_terms':450,'C8_ordered_terms':94586,'mu7_dimension':6,'mu8_dimension':7},'decision':'C'}
    path=ROOT/'notes/WP84_DEGREE8_PAIR_INSERTION_AND_MODEL_CERTIFICATE.json';path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['moment_certificate'],indent=2));print('Decision C; exact certificate:',path)
if __name__=='__main__':main()

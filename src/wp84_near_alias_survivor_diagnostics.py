"""Discovery-only actual-prime survivor diagnostics for the original zero-lag path.
Full natural section, a_phi=1. NOT full R6000 or selected-good-section data.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import defaultdict
from math import log,sqrt,exp,floor,factorial,prod,pi,sin
from fractions import Fraction as F
import cmath,json
from wp84_signed_near_alias_attack import alias_status
from wp84_near_alias_long_tail_discharge import log_interval
ROOT=Path(__file__).resolve().parents[1]
def diagnostic(X,H=100):
    L=log(X);T=2*pi*X;N=floor(exp(L-sqrt(L)));d=floor(X*L)
    lb=log_interval(X);g=lb[0]-log_interval(N)[1];gp=lb[1]-log_interval(N+1)[0]
    assert g>0 and g*g>=lb[1] and gp>0 and gp*gp<lb[0]
    ps=[p for p in range(2,N+1) if all(p%q for q in range(2,int(sqrt(p))+1))];k=len(ps)
    leaf=[-log(p)/(L*sqrt(p))*(1-log(p)/L) for p in ps]
    atoms=defaultdict(complex);byclass=defaultdict(complex);uncertain=0;selected=0;abs_raw=0.
    for b in (5,6):
        omega=-11501/12500 if b==5 else 137641/250000
        for row in combinations_with_replacement(range(2*k),b):
            pos=[0]*k;neg=[0]*k
            for v in row:
                (pos if v<k else neg)[v%k]+=1
            nu=[a+c for a,c in zip(pos,neg) if a+c];e=[a-c for a,c in zip(pos,neg) if a+c]
            ur=prod(p**max(a-c,0) for p,a,c in zip(ps,pos,neg));vr=prod(p**max(c-a,0) for p,a,c in zip(ps,pos,neg));ratio=F(ur,vr)
            lam=log(ur)-log(vr);m=floor(lam/L+.5)
            if not m or ratio==F(X)**m:continue
            delta=lam-m*L
            if abs(abs(delta)-H/T)<1e-10:uncertain+=1;continue
            if abs(delta)>H/T or alias_status(e,m,nu)!='remaining_signed_dilated_product':continue
            mult=factorial(b)//prod(factorial(v) for v in pos+neg)
            weight=omega*mult*prod(c**(a+bb) for c,a,bb in zip(leaf,pos,neg))
            sig=1 if delta>0 else -1;z=weight*cmath.exp(1j*T*lam)
            atoms[(m,sig,ratio)]+=z;selected+=1;abs_raw+=abs(weight)
            key=(b,tuple(sorted((v for v in e if v>0),reverse=True)),tuple(sorted((-v for v in e if v<0),reverse=True)),m)
            gk=cmath.exp(1j*pi*(d-1)*delta/L)*sin(pi*d*delta/L)/(d*sin(pi*delta/L))
            byclass[key]+=z*gk
    groups=defaultdict(list);trace=0j;kernel_abs=0.
    for (m,sig,ratio),z in atoms.items():
        lam=log(ratio.numerator)-log(ratio.denominator);delta=lam-m*L;x=abs(delta)
        groups[(m,sig)].append((x,z));gk=cmath.exp(1j*pi*(d-1)*delta/L)*sin(pi*d*delta/L)/(d*sin(pi*delta/L))
        trace+=z*gk;kernel_abs+=abs(z*gk)
    primitive_norm=0.;endpoints=[]
    for key,values in groups.items():
        cur=0j;best=0.
        for x,z in sorted(values,key=lambda t:t[0]):cur+=z;best=max(best,abs(cur))
        primitive_norm+=best;endpoints.append({'m_sigma':key,'sup_abs_primitive':best,'endpoint_real':cur.real,'endpoint_imag':cur.imag})
    return {'X':X,'T':T,'L':L,'N':N,'H':H,'dprime':d,'section':[0,d-1],'a_phi_diagnostic':1,'primes':ps,'selected_signed_multisets':selected,'unique_ratio_atoms':len(atoms),'classification_boundary_skips':uncertain,'joint_kernel_real':trace.real,'joint_kernel_imag':trace.imag,'joint_primitive_sum_sup':primitive_norm,'absolute_raw_weight_mass':abs_raw,'absolute_kernel_atom_sum':kernel_abs,'kernel_cancellation_ratio':abs(trace)/kernel_abs if kernel_abs else None,'primitive_endpoints':endpoints,'largest_zero_lag_reduced_classes':[{'key':str(q),'real':z.real,'imag':z.imag,'abs':abs(z)} for q,z in sorted(byclass.items(),key=lambda t:abs(t[1]),reverse=True)[:8]]}
def main():
    rows=[diagnostic(x) for x in (63,100,215,405)]
    exponents=[]
    for a,b in zip(rows,rows[1:]):
        aa=a['joint_primitive_sum_sup'];bb=b['joint_primitive_sum_sup']
        exponents.append({'X_pair':[a['X'],b['X']],'exploratory_local_log_slope':log(bb/aa)/log(b['T']/a['T']) if aa>0 and bb>0 else None})
    result={'scope':'ACTUAL ordinary primes, zero-lag subset of original fixed-R sum only; natural full section, a_phi=1; selected-good-section status NOT certified; floating point discovery, NOT interval proof','degree_rescaling':'replace each degree-b primitive/kernel component by a_phi(T)^(-b) before combining if the finite taper differs','diagnostics':rows,'local_slopes':exponents,'empirical_decay_promoted':False}
    (ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_DIAGNOSTICS.json').write_text(json.dumps(result,indent=2)+'\n')
    for r in rows:print(r['X'],'prime count',len(r['primes']),'atoms',r['unique_ratio_atoms'],'P norm',r['joint_primitive_sum_sup'],'signed charge',r['joint_kernel_real'])
    print('Discovery only; no full-R or asymptotic bound')
if __name__=='__main__':main()

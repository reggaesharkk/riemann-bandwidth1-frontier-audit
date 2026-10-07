"""Complete marked-pair channels, hard masks, and exact SOS completion witness.
Channel coefficients remain symbolic finite-T expressions; no arithmetic saving.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[1]
def carrier(word):
    c=Counter()
    for p,e,l in word:c[p]+=e
    return tuple(sorted((p,e) for p,e in c.items() if e))
def offsets(word):
    u=[0]
    for p,e,l in word:u.append(u[-1]+l)
    return u
def admissible(word,root,section,R):
    u=offsets(word)
    return u[-1]==0 and all(abs(l)<=R for p,e,l in word) and all(section[0]<=root+t<=section[1] for t in u)
def marked_deletions(word):
    for i,j in combinations(range(len(word)),2):
        if word[i][0]==word[j][0] and word[i][1]==-word[j][1]:
            lower=tuple(t for k,t in enumerate(word) if k not in (i,j))
            assert carrier(lower)==carrier(word)
            yield (i,j,lower)
def insertion_channels(lower,primes,R,root,section):
    # Domain includes open skeletons. Every output is closed and section-admissible.
    n=len(lower)+2
    for i,j in combinations(range(n),2):
        for p,e,v,w in product(primes,(-1,1),range(-R,R+1),range(-R,R+1)):
            it=iter(lower);word=tuple((p,e,v) if k==i else (p,-e,w) if k==j else next(it) for k in range(n))
            if admissible(word,root,section,R):yield (i,j,word)
def hard_mask(word,logp,L,T,H,pwindows,product_window=None):
    # User-specified actual finite-T windows, not fabricated numerical primes.
    if not all(pwindows[j][0]<=logp[p]/L<=pwindows[j][1] for j,(p,e,l) in enumerate(word)):return False
    lam=sum(e*logp[p] for p,e,l in word)
    if abs(lam)>H/T:return False
    if product_window:
        lp=sum(logp[p] for p,e,l in word if e>0)
        if not product_window[0]<=lp/L<=product_window[1]:return False
    return True

def channel_factor(higher,slots,root,L,a_phi,section,R,logp):
    """Exact symbolic entry on unprojected rooted skeleton weights, unmarked convention."""
    i,j=slots;assert higher[i][0]==higher[j][0] and higher[i][1]==-higher[j][1]
    if not admissible(higher,root,section,R):return s.Integer(0)
    lower=tuple(t for k,t in enumerate(higher) if k not in slots)
    p,e,v=higher[i];w=higher[j][2];alpha=logp[p]/L
    def filt(l,eps):
        f=1-alpha if l==0 else (1-s.exp(2*s.pi*s.I*l*alpha))/(2*s.pi*s.I*l)
        return f if eps==1 else s.conjugate(f)
    def phase(word):
        u=offsets(word)
        return sum(e*(root+u[k])*logp[p]/L for k,(p,e,l) in enumerate(word))
    D=len(list(marked_deletions(higher)))
    return (logp[p]/(a_phi*L*s.sqrt(p)))**2*filt(v,e)*filt(w,-e)*s.exp(2*s.pi*s.I*(phase(higher)-phase(lower)))/D

def completion_optimizer(coefficients):
    """Exact fixed-consumer optimum in the extended Hankel-positivity relaxation."""
    m=list(map(s.Rational,['1','0','1/3','0','1/4','1/36','157/630']))
    H=s.Matrix(4,4,lambda i,j:m[i+j]);z=s.symbols('mu7',real=True);h=s.Matrix(m[4:]+[z])
    t=s.expand((h.T*H.inv()*h)[0]);c=list(map(s.Rational,coefficients));base=sum(c[i]*m[i] for i in range(7))
    if c[8]==0:
        assert c[7]==0
        return {'infimum':str(base),'mu7':'free','mu8':'Schur lower bound'}
    assert c[8]>0
    f=s.expand(base+c[7]*z+c[8]*t);opt=s.solve(s.diff(f,z),z)[0]
    return {'infimum':str(s.factor(f.subs(z,opt))),'mu7_relaxed_optimizer':str(opt),'mu8_relaxed_optimizer':str(s.factor(t.subs(z,opt)))}

def spectral_gate(domain_order,codomain_order,identification=None):
    if domain_order!=codomain_order and identification is None:
        raise ValueError('Rectangular cross-order operator: no endomorphism eigenvalue without certified identification')

def certificate():
    x,y=s.symbols('x y');a=list(map(s.Rational,['-19101/185500','961/3710','31/50','-371/500','1/100000']))
    a[1]=-(a[2]**2+2*a[0]*a[4])/(2*a[3]);q=sum(a[i]*x**i for i in range(5));q=s.expand(q/q.subs(x,-1));p=s.Poly(q*q,x)
    assert p.nth(4)==0
    support=s.Poly(q.subs(x,-1-y),y);assert support.nth(0)==1 and all(t>=0 for t in support.all_coeffs())
    m=list(map(s.Rational,['1','0','1/3','0','1/4','1/36','157/630']));H=s.Matrix(4,4,lambda i,j:m[i+j]);h=s.Matrix(m[4:]+[0]);m += [s.Integer(0),(h.T*H.inv()*h)[0]+1]
    H8=s.Matrix(5,5,lambda i,j:m[i+j]);assert all(H8[:i,:i].det()>0 for i in range(1,6))
    E=sum(p.nth(i)*m[i] for i in range(9));assert E<s.Rational(21,200)
    word=((2,1,1),(2,-1,1),(3,1,-1),(5,1,0),(7,-1,-1),(11,-1,0),(13,-1,0))
    assert admissible(word,0,(0,2),1)
    dels=list(marked_deletions(word));assert len(dels)==1
    lower=dels[0][2];assert offsets(lower)[-1]==-2
    assert any(w==word for i,j,w in insertion_channels(lower,[2],1,0,(0,2)))
    return {'decision':'F','SOS_witness':{'q_coefficients':[str(s.Poly(q,x).nth(i)) for i in range(5)],'p_coefficients':[str(p.nth(i)) for i in range(9)],'support_q_minus1_minusy':[str(support.nth(i)) for i in range(5)],'relaxed_completion_moments':[str(t) for t in m],'H8_leading_minors':[str(H8[:i,:i].det()) for i in range(1,6)],'expectation':str(E),'uncharged_coefficient':str(1-2*E),'c7_over_c5':str(p.nth(7)/p.nth(5)),'c8_over_c6':str(p.nth(8)/p.nth(6))},'operator_counterexample':{'higher_word':word,'deleted_skeleton':lower,'lower_total_displacement':-2,'complete_on_augmented_open_skeletons':True,'complete_on_closed_lower_space':False},'fixed_consumer_completion_optimum':completion_optimizer([p.nth(i) for i in range(9)]),'actual_mu7_mu8':'NOT COMPUTED','arithmetic_ratio_region':'UNCERTIFIED','intersection':'UNRESOLVED'}
if __name__=='__main__':

    try:spectral_gate(5,7)
    except ValueError:pass
    else:raise AssertionError('invalid spectrum accepted')
    try:spectral_gate(6,8)
    except ValueError:pass
    else:raise AssertionError('invalid spectrum accepted')
    c=certificate();(ROOT/'notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json').write_text(json.dumps(c,indent=2)+'\n');print(json.dumps(c['SOS_witness'],indent=2))

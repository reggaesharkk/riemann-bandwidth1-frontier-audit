"""Independent rational differentiation and Sturm-chain validation; no producer import."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'notes/WP84_REFEREE_FOUNDATIONS_CERTIFICATE.json'
def clean(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def plus(a,b):return clean([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def times(a,b):
    d=[F(0)]*(len(a)+len(b)-1)
    for i in range(len(a)):
        for j in range(len(b)):d[i+j]+=a[i]*b[j]
    return clean(d)
def neg(a):return [-x for x in a]
def derivative(a):return clean([i*a[i] for i in range(1,len(a))] or [F(0)])
def quotient_derivative(n,d):return plus(times(derivative(n),d),neg(times(n,derivative(d)))),times(d,d)
def residual(a,b):
    a=a[:]
    while len(a)>=len(b) and any(a):
        n=len(a)-len(b);factor=a[-1]/b[-1]
        a=plus(a,neg([F(0)]*n+[factor*v for v in b]))
    return a
def proportional_positive(a,b):
    assert len(a)==len(b)
    ratio=next(x/y for x,y in zip(a,b) if y)
    assert ratio>0 and all(x==ratio*y for x,y in zip(a,b))
def variations(seq,side):
    signs=[(1 if p[-1]>0 else -1)*((-1)**(len(p)-1) if side<0 else 1) for p in seq]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def integral(p):return sum(c*F(2,2**(i+1)*(i+1)) for i,c in enumerate(p) if i%2==0)
def verify(data):
    assert data['R']==6000 and data['input_head']=='8a36b35d103850c4a8b37e2e1334364483b0b500'
    c=data['curvature'];a=F(c['a']);M=F(c['bound'])
    assert a==F(221,200) and M==F(137721,5000)
    P=list(map(F,c['P']));assert P==[F(1),-F(594893,185500),F(1423,500),-F(371,500)]
    N=[a**6*x for x in times(P,P)];D=[a*a,F(0),F(1)];G=times(times(D,D),D)
    n1,d1=quotient_derivative(N,G);n2,d2=quotient_derivative(n1,d1)
    H=list(map(F,c['numerator']));den=list(map(F,c['denominator']))
    assert den==times(times(G,D),D) and times(n2,den)==times(H,d2)
    for sign,record in zip((1,-1),c['sturm_gates']):
        seq=[list(map(F,p)) for p in record]
        gate=plus([M*x for x in den],[sign*x for x in H])
        proportional_positive(seq[0],gate);proportional_positive(seq[1],derivative(seq[0]))
        for j in range(2,len(seq)):proportional_positive(seq[j],neg(residual(seq[j-2],seq[j-1])))
        assert len(seq[-1])==1 and variations(seq,-1)==variations(seq,1)==5 and seq[0][0]>0
    b=data['budget'];band=3*M*F(106,333)**2/6000;var=2*F(26060119,430128125)*F(106,333)**2/6000
    cap=F(21,200)-F(364848201,34410250000)+F(26060119,430128125)/3-band-var
    margin=cap+F(11501,12500)/36-F(137641,250000)*F(34,135)
    assert F(b['band'])==band and F(b['variance'])==var and F(b['Jstar'])==cap
    assert F(b['reference_margin'])==margin==F(52897896569489,572357731837500000)
    assert F(b['curvature_error_allowance'])==margin/(3*F(106,333)**2/6000)
    assert F(b['third_moment_adverse_allowance'])==margin/F(21981971,46375000)
    assert F(b['third_coefficient'])==F(21981971,46375000) and F(b['sixth_ceiling_slack'])==F(1,378)
    old=json.loads((ROOT/'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json').read_text())
    assert b['required_saving_lower']==old['gaussian_pinching']['required_negative_residual_at_least']
    assert not data['finite_R_multiplicativity'] and not data['GUE_fifth_sixth_computed'] and not data['strict_gt79_proved']
    assert data['foundation_status']['same_section_centered_mu3']=='not proved by cited source; keep original third coefficient'
    assert data['foundation_status']['C_ab_replacement']=='proved bounded-gate implication; not unconditional sixth control'
    expected=[]
    for p in subprocess.check_output(['git','ls-tree','-r','--name-only',data['input_head']],cwd=ROOT,text=True).splitlines():
        if p.endswith(('.md','.py')):
            for n,line in enumerate((ROOT/p).read_text(encoding='utf-8-sig').splitlines(),1):
                if re.search(r'mu3|mu_3|mu_\{3\}|[μµ].?3|third[- ]moment|third.*cumulant|third.*PRIME|P_R\^3',line,re.I):
                    expected.append({'path':p,'line':n,'text':line})
    assert data['third_claim_search_inventory']==expected
    for p,pin in data['source_pins'].items():
        assert sha256((ROOT/p).read_bytes()).hexdigest()==pin['sha256']
        assert subprocess.check_output(['git','rev-parse',data['input_head']+':'+p],cwd=ROOT,text=True).strip()==pin['git_blob']
    for p,h in data['packet_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    # Nonmultiplicativity gap for the half interval at the ORIGINAL R.
    assert F(7,22)**2/6001>0 and F(7,22)**2/6001<F(106,333)**2/5999
    # Missing derivative term in point sampling can fail, already for a polynomial.
    poly=[F(1)]
    for _ in range(4):poly=times(poly,[F(1),F(0),-F(4)])
    sq=times(poly,poly);ds=times(derivative(poly),derivative(poly))
    assert 2*integral(sq)<1<=2*integral(sq)+2*integral(ds)
    # Exact Holder exponents for the distinct visible 3/4-slot PNT test.
    assert 3*F(1,6)==F(1,2) and 4*F(1,6)==F(2,3)
if __name__=='__main__':
    d=json.loads(PATH.read_text());verify(d)
    mutations=[('R',400),('finite_R_multiplicativity',True),('GUE_fifth_sixth_computed',True),('strict_gt79_proved',True)]
    for k,v in mutations:
        bad=json.loads(json.dumps(d));bad[k]=v
        try:verify(bad)
        except AssertionError:pass
        else:raise AssertionError('accepted '+k)
    for kind in ('curvature','third_status','PNT_status','third_inventory'):
        bad=json.loads(json.dumps(d))
        if kind=='curvature':bad['curvature']['sturm_gates'][0][-1][0]='0'
        elif kind=='third_status':bad['foundation_status']['same_section_centered_mu3']='unconditional'
        elif kind=='PNT_status':bad['foundation_status']['C_ab_replacement']='unconditional sixth bound'
        else:bad['third_claim_search_inventory']=[]
        try:verify(bad)
        except (AssertionError,ZeroDivisionError,StopIteration):pass
        else:raise AssertionError('accepted '+kind)
    print('PASS independent quotient differentiation; two rational Sturm chains, V(-infinity)=V(+infinity)=5; exact budget/sensitivity')
    print('PASS sampling derivative falsifier, finite-R positive multiplicativity gap, third-claim inventory, pins and 8 hostile mutations')
    print('GUE dictionary STOP; same-section third arithmetic gate and strict >79 OPEN.')

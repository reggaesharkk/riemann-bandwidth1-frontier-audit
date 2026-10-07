"""Exact circularity and scalar prime-field reconstruction audit.
Stops at the user's first characteristic circularity gate; no CLT claim.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import wp84_mehler_weak_dual_certificate as dual
ROOT=Path(__file__).resolve().parents[1]

def zero(x,label):
    if s.simplify(s.expand_complex(x))!=0:raise ValueError(label)

def reconstruction():
    # Actual prime powers 2 and 4, L=4log2, T=2pi/log2, a_phi=1.
    # This is an exact representation regression, not the asymptotic cutoff.
    d=3
    terms=[(s.Rational(1,4),-1/(4*s.sqrt(2))),
           (s.Rational(1,2),-s.Rational(1,8))]
    q=[];qp=[];A=s.zeros(d)
    for k in range(d):
        q.append(sum(c*s.exp(2*s.pi*s.I*k*v) for v,c in terms))
        qp.append(s.I*sum(c*v*s.exp(2*s.pi*s.I*k*v) for v,c in terms))
    for v,c in terms:
        phases=[s.exp(2*s.pi*s.I*k*v) for k in range(d)]
        for i in range(d):
            for j in range(d):
                A[i,j]+=c*((1-v)*phases[i] if i==j else
                           (phases[i]-phases[j])/(2*s.pi*s.I*(j-i)))
    a=[s.im(z).simplify() for z in q]
    b=[(2*s.re(q[k])-2*s.im(qp[k])).simplify() for k in range(d)]
    J=s.Matrix(d,d,lambda i,j:0 if i==j else 1/(s.pi*(j-i)))
    Loewner=s.diag(*b)+s.diag(*a)*J-J*s.diag(*a)
    for entry in A+A.conjugate().T-Loewner:zero(entry,'exact prime scalar reconstruction')
    D=s.diag(*range(d));one=s.ones(d,1);av=s.Matrix(a)
    for entry in D*Loewner-Loewner*D-(one*av.T-av*one.T)/s.pi:
        zero(entry,'exact rank-two source')
    return {'prime_powers':['2','4'],'L':'4 log 2','T':'2pi/log2',
            'Q_samples':list(map(str,q)),'Qprime_over_L_samples':list(map(str,qp)),
            'matrix_reconstruction':'PASS','rank_two_source':'PASS',
            'scope':'finite exact algebra only'}

def characteristic():
    r=s.symbols('r',positive=True);t,v1,v2,c=s.symbols('t v1 v2 c',positive=True)
    z=s.Rational(3142,2415)+s.I*s.Rational(131,200);s0=s.Integer(1)
    H=s.Matrix([[s.Rational(4,3),s.Rational(2,7)],[s.Rational(2,7),s.Rational(4,5)]])
    I=s.eye(2);R=(H-z*I).inv();zr=s0+r*(z-s0);Hr=s0*I+r*(H-s0*I)
    Rr=(Hr-zr*I).inv()
    for k in (1,2,3):
        for entry in r**k*Rr**k-R**k:zero(entry,'consumer factor unchanged on characteristic')
    # Exact invariant differentiation under logarithmic characteristic time.
    ell=s.symbols('ell',real=True)
    fields={'v1/t^2':(v1*s.exp(2*ell))/(t*s.exp(ell))**2,
            'v2/t^2':(v2*s.exp(2*ell))/(t*s.exp(ell))**2,
            'c/t^2':(c*s.exp(2*ell))/(t*s.exp(ell))**2}
    for expr in fields.values():zero(s.diff(expr,ell),'covariance invariant')
    for k in (1,2,3):
        q=s.symbols('q'+str(k));zero(s.diff(q*s.exp(k*ell)/(t*s.exp(ell))**k,ell),'coefficient invariant')
    zeta=s.symbols('zeta');zero(s.diff(zeta*s.exp(ell)/(t*s.exp(ell)),ell),'pole invariant')
    dual.reject(lambda:zero(r**2*Rr[0,0]-R[0,0],'wrong resolvent scaling'))
    return {'invariants':['v1/t^2','v2/t^2','c/t^2','Re(zeta)/t','Im(zeta)/t',
      'Re(q0)','Im(q0)','Re(q1)/t','Im(q1)/t','Re(q2)/t^2','Im(q2)/t^2',
      'Re(q3)/t^3','Im(q3)/t^3'],
      'independent_invariant_count_real':13,'consumer_scaling':'PASS',
      'incorrect_scaling':'REJECTED','pointwise_boundary_equals_terminal':True}

def main():
    original=json.loads((ROOT/'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json').read_text())
    ws=[w for w in original['witnesses'] if w['K']==32]
    for w in ws:dual.verify(w)
    previous=json.loads((ROOT/'notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG_CERTIFICATE.json').read_text())
    out={'parent':'00f5f8f67b9c03d399c90650d0811cf01e6c7464','witnesses':ws,
      'characteristic':characteristic(),'prime_field_reconstruction':reconstruction(),
      'boundary_classification':'A: literally the original compiled signed target under reparameterization',
      'stop_condition':'16.A: equivalent original target; no simplification from master characteristic',
      'decision':'D: master route provably circular at the first requested stop gate',
      'finite_lag_localization':'not pursued after stop gate; not established',
      'finite_prime_field_CLT':'not pursued after stop gate; neither proved nor falsified',
      'literature_and_public_candidate_audit':'not reached under explicit stop condition',
      'Gaussian_smoothing':'already present and unchanged by the characteristic identity',
      'lag_tail_error':None,'reconstructed_boundary_value':None,'actual_margin':None,
      'required_grouped_lower_threshold':previous['exact_required_grouped_limit_lower_threshold'],
      'epsilon':'8711/2778200','initial_payment_upper':'53503/66000000',
      'synthetic_regression_margin':next(row['synthetic_margin_lower'] for row in original['benchmark_rows'] if row['K']==32),
      'consumer_certified':False}
    names=['WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md','WP84_JOINT_GAUSSIAN_MEHLER_MASTER_LAW.md',
      'WP84_COMPILED_MEHLER_PRIME_LINDEBERG.md','WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF.md']
    out['source_coverage']=[{'path':'notes/'+name,'sha256':hashlib.sha256((ROOT/'notes'/name).read_bytes()).hexdigest()} for name in names]
    (ROOT/'notes/WP84_PRIME_CHARACTERISTIC_BOUNDARY_LAW_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:out[key] for key in ('decision','characteristic','prime_field_reconstruction','stop_condition')},indent=2))
if __name__=='__main__':main()

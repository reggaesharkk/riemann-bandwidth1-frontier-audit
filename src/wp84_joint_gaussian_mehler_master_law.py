"""Two-copy Gaussian master-law exact algebra and labeled quadrature regressions.
The Euler master equation does not certify a prime-state response value.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import numpy as np
import wp84_mehler_weak_dual_certificate as dual
ROOT=Path(__file__).resolve().parents[1]

def check(x,label):
    if s.simplify(x)!=0:raise ValueError(label)

def exact():
    t,u,rho=s.symbols('t u rho',real=True);v=t*(1-t)
    Sigma=s.Matrix([[v+u,v+u*rho],[v+u*rho,v+u]])
    U=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    modes=(U.T*Sigma*U).applyfunc(s.simplify)
    check(modes[0,0]-2*v-u*(1+rho),'common mode')
    check(modes[1,1]-u*(1-rho),'difference mode')
    check(modes[0,1],'mode off diagonal')
    check(s.diff(v,t)-2*(v+u)/t+1+2*u/t,'diagonal path coefficient')
    check(s.diff(v,t)-2*(v+u*rho)/t+1+2*u*rho/t,'cross path coefficient')
    # Bounded Fourier Gaussian probe independently checks Price and drift factors.
    tt,pp,v1,v2,c,alpha,beta=s.symbols('tt pp v1 v2 c alpha beta',real=True)
    M=s.exp(s.I*(alpha-beta)*tt*pp-(alpha*alpha*v1+beta*beta*v2-2*alpha*beta*c)/2)
    check(s.diff(M,v1)+alpha*alpha*M/2,'Price variance 1/2')
    check(s.diff(M,c)-alpha*beta*M,'Price cross coefficient 1')
    radial=alpha*s.diff(M,alpha)+beta*s.diff(M,beta)
    check(radial-tt*s.diff(M,tt)-2*(v1*s.diff(M,v1)+v2*s.diff(M,v2)+c*s.diff(M,c)),
          'two-copy radial IBP')
    dual.reject(lambda:check(radial-tt*s.diff(M,tt)-2*(v1*s.diff(M,v1)+v2*s.diff(M,v2))-c*s.diff(M,c),'missing second cross block'))
    # Fundamental rational consumer dilation: rho is unrelated to dilation r.
    rr=s.symbols('r',positive=True)
    H=s.Matrix([[2,s.Rational(1,3)],[s.Rational(1,3),-1]])
    z=s.Rational(1,5)+s.I*s.Rational(7,9);I=s.eye(2)
    R=(H-I-z*I).inv()
    shifted=(I+rr*(H-I)-(1+rr*z)*I).inv()
    for k in (1,2,3):
        for value in (rr**k*shifted**k-R**k):check(value,'finite rational dilation')
    # Actual consumer scalar counterexample to uniqueness of the master PDE.
    x=s.symbols('x',real=True);a=s.Rational(131,200);cc=s.Rational(3142,2415)
    P=1-s.Rational(43428,13891)*x+s.Rational(37704,13891)*x*x-s.Rational(9660,13891)*x**3
    energy=(cc*cc+a*a)**3*P*P/((x-cc)**2+a*a)**3
    vals=[s.cancel(energy.subs(x,k)) for k in (1,2)]
    trace_zero=[s.cancel((energy.subs(x,1+h)+energy.subs(x,1-h))/2) for h in (1,2)]
    if trace_zero[0]==trace_zero[1]:raise ValueError('Trace-zero boundary counterexample failed')
    if vals[0]==vals[1] or s.diff(energy,x).subs(x,1)==0:raise ValueError('No boundary counterexample')
    curvature={str(k):str(s.cancel(s.diff(energy,x,2).subs(x,k))) for k in (0,1,2,3,10)}
    if not any(s.Rational(x)>0 for x in curvature.values()) or not any(s.Rational(x)<0 for x in curvature.values()):
        raise ValueError('Variance sign test missing both signs')
    return {'copy_modes':list(map(str,(modes[0,0],modes[1,1]))),
      'Price_and_radial_IBP':'PASS','missing_cross_block':'REJECTED','rational_degree_three_dilation':'PASS',
      'same_scalar_boundary_two_different_prime_directions':{'s0':'1','P':['0','1'],
       'Sigma':'0','energies_at_t1':list(map(str,vals)),'same_t0_energy':str(vals[0]),
       'scope':'synthetic Loewner states; nonuniqueness of PDE data, not prime-theorem counterexamples'},
      'trace_zero_two_by_two_P_counterexample':{'P_diagonals':['(1,-1)','(2,-2)'],'terminal_energies':list(map(str,trace_zero)),'same_t0_all_Sigma_boundary':True},
      'finite_map_mismatch':{'B_covariance_scalar_branch_real_one':'4','circular_covariance_same_branch':'2','exactly_equal_at_finite_T':False},
      'energy_second_derivatives':curvature}

def numerical(order,matrix):
    # Direct correlated Gaussian quadrature for actual bounded rational Q.
    d=2 if matrix else 1
    I=np.eye(d);s0=1.;t=.6
    P=np.array([[1/3,2/7],[2/7,-1/5]]) if matrix else np.array([[1/3]])
    E=np.array([[1/4,1/8],[1/8,-1/6]]) if matrix else np.array([[1/np.sqrt(6)]])
    Sigma=np.array([[.2,.07],[.07,.3]])
    z=3142/2415+1j*131/200;eta=(abs(z)**2)**1.5
    p=[1,-43428/13891,37704/13891,-9660/13891]
    b=[p[3],p[2]+3*z*p[3],p[1]+2*z*p[2]+3*z*z*p[3],sum(p[j]*z**j for j in range(4))]
    nodes,weights=np.polynomial.hermite.hermgauss(order)
    n=np.sqrt(2)*nodes
    grid=np.array(np.meshgrid(n,n,indexing='ij')).reshape(2,-1).T
    w=(weights[:,None]*weights[None,:]/np.pi).ravel()
    def build(tt,SS):
        noise=grid@np.linalg.cholesky(SS).T
        return [s0*I+tt*P+noise[:,i,None,None]*E for i in range(2)]
    H1,H2=build(t,Sigma)
    def values(H,scale=1.):
        zz=s0+scale*(z-s0)
        R=np.linalg.inv(H-zz*I);powers=[np.broadcast_to(I,R.shape),R]
        for k in range(2,6):powers.append(powers[-1]@R)
        q=sum(eta*b[k]*scale**k*powers[k] for k in range(4))
        return q,powers
    Q1,R1=values(H1);Q2,R2=values(H2)
    def inner(A,B):
        return float(np.sum(w*np.einsum('nij,nij->n',A.conj(),B).real/d))
    def first(R,B):
        return -sum(eta*b[k]*(R[pp]@B@R[k+1-pp]) for k in range(1,4) for pp in range(1,k+1))
    def second(R):
        return 2*sum(eta*b[k]*(R[pp]@E@R[qq]@E@R[k+2-pp-qq])
                     for k in range(1,4) for pp in range(1,k+1)
                     for qq in range(1,k+2-pp) if k+2-pp-qq>=1)
    derivatives=[inner(first(R1,P),Q2)+inner(Q1,first(R2,P)),
                 inner(second(R1),Q2)/2,inner(Q1,second(R2))/2,
                 inner(first(R1,E),first(R2,E))]
    radial=inner(first(R1,H1-s0*I),Q2)+inner(Q1,first(R2,H2-s0*I))
    residual=radial-t*derivatives[0]-2*(Sigma[0,0]*derivatives[1]+Sigma[1,1]*derivatives[2]+Sigma[0,1]*derivatives[3])
    step=1e-5
    def observed(tt,SS):
        H=build(tt,SS);return inner(values(H[0])[0],values(H[1])[0])
    fds=[(observed(t+step,Sigma)-observed(t-step,Sigma))/(2*step)]
    for i,j in ((0,0),(1,1),(0,1)):
        delta=np.zeros((2,2));delta[i,j]=1;delta[j,i]=1
        fds.append((observed(t,Sigma+step*delta)-observed(t,Sigma-step*delta))/(2*step))
    dilation=(inner(values(H1,np.exp(step))[0],values(H2,np.exp(step))[0])
              -inner(values(H1,np.exp(-step))[0],values(H2,np.exp(-step))[0]))/(2*step)
    error=max(abs(x-y) for x,y in zip(derivatives,fds))
    if abs(residual)>2e-7 or error>2e-7 or abs(dilation+radial)>2e-7:
        raise ValueError('Master quadrature regression failed')
    return {'order':order,'matrix_dimension':d,'M':inner(Q1,Q2),
      'radial_IBP_residual':residual,'Price_finite_difference_error':error,
      'finite_parameter_dilation_error':abs(dilation+radial),
      'scope':'numerical regression only, not interval-certified theorem data'}

def main():
    original=json.loads((ROOT/'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json').read_text())
    ws=[w for w in original['witnesses'] if w['K']==32]
    for w in ws:dual.verify(w)
    coeff=list(map(F,ws[0]['coefficients']));rho=list(map(F,ws[0]['rhos']))
    q=[dual.evaluate(coeff,rho,k) for k in range(3)]
    out={'parent':'25694f1db77b95e2f47060dda48e806b70b36815','witnesses':ws,
      'exact':exact(),'numerical_regressions':[numerical(n,m) for m in (False,True) for n in (48,96)],
      'dual_multiplier_0_1_2':list(map(str,q)),'q0_minus_q1':str(q[0]-q[1]),
      'q0_minus_one':str(q[0]-1),
      'synthetic_margin_regression':next(r['synthetic_margin_lower'] for r in original['benchmark_rows'] if r['K']==32),
      'synthetic_master_embedding_proved':False,
      'scalar_boundary_determines_master':False,'consumer_certified':False,
      'decision':'D: degenerate drift-free master transport does not determine the prime-dependent characteristic boundary'}
    sources=[]
    for path in sorted((ROOT/'notes').glob('*.md')):
        if any(k in path.name for k in ('GAUSSIAN','MEHLER','COMPILED','D2_CURRENT','D2_UNIFORM','D2_FAST','FULL_DRIFT','COMMON_STATE','CHARACTERISTIC')):
            sources.append({'path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    for path in sorted((ROOT/'src').glob('wp84_*.py')):
        if any(k in path.name for k in ('gaussian','mehler','compiled','characteristic','common_state','d2_','d1_','rank3','drift_elimination')):
            sources.append({'path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    previous=json.loads((ROOT/'notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG_CERTIFICATE.json').read_text())
    CF=F(previous['uniform_Taylor_cubic_constant'])
    out['exact_ledger']={'epsilon':'8711/2778200','initial_payment_upper':'53503/66000000',
      'invariance_cube_constant':str(F(5,4)*CF),
      'required_grouped_lower_threshold':previous['exact_required_grouped_limit_lower_threshold'],
      'actual_margin':None,'vanishing_errors_do_not_pay_characteristic_boundary':True}
    out['source_coverage']=sources
    (ROOT/'notes/WP84_JOINT_GAUSSIAN_MEHLER_MASTER_LAW_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'decision':out['decision'],'exact':out['exact'],'numerical_regressions':out['numerical_regressions']},indent=2))
if __name__=='__main__':main()

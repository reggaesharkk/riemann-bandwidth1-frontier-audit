"""Exact scalar falsifier and structured direct-energy Hessian reconnaissance."""
import argparse
import sympy as S
import numpy as np


def setup():
    x=S.symbols('x',real=True)
    c=S.Rational(3142,2415);a=S.Rational(131,200);z=c+S.I*a
    P=1-S.Rational(43428,13891)*x+S.Rational(37704,13891)*x**2-S.Rational(9660,13891)*x**3
    r6=(c*c+a*a)**3
    f=r6*P**2/((x-c)**2+a*a)**3
    Q=S.sqrt(r6)*P/(x-z)**3
    delta=2*S.I*a;p=P.subs(x,z);p1=S.diff(P,x).subs(x,z);p2=S.diff(P,x,2).subs(x,z)
    co=[r6*((p1*p1+p*p2)/delta**3-6*p*p1/delta**4+6*p*p/delta**5),
        r6*(2*p*p1/delta**3-3*p*p/delta**4),r6*p*p/(2*delta**3)]
    u=S.symbols('u');v=z*u-S.conjugate(z)
    q=S.Poly(S.expand(S.sqrt(r6)/delta**3*((u-1)**3-S.Rational(43428,13891)*v*(u-1)**2+S.Rational(37704,13891)*v*v*(u-1)-S.Rational(9660,13891)*v**3)),u)
    return x,c,a,z,P,f,Q,co,[complex(S.N(q.nth(j),18)) for j in range(4)]


def curvature(H,directions,z,q,co):
    d=len(H);R=np.linalg.inv(H-z*np.eye(d));delta=z-z.conjugate()
    U=np.eye(d)+delta*R
    powers=[np.linalg.matrix_power(U,j) for j in range(4)]
    Q=sum(q[j]*powers[j] for j in range(4))
    g1=g2=0.
    for B in directions:
        X=-delta*R@B@R;Y=2*delta*R@B@R@B@R
        DQ=np.zeros_like(R);D2=np.zeros_like(R)
        for n in range(1,4):
            for i in range(n):
                DQ+=q[n]*powers[i]@X@powers[n-1-i]
                D2+=q[n]*powers[i]@Y@powers[n-1-i]
            for i in range(n):
                for j in range(i+1,n):
                    D2+=2*q[n]*powers[i]@X@powers[j-i-1]@X@powers[n-1-j]
        g1+=np.trace(DQ.conj().T@DQ).real/d
        g2+=np.trace(Q.conj().T@D2).real/d
    rp=[np.linalg.matrix_power(R,j) for j in range(5)]
    Xi=[]
    import math
    for order in (1,2,3):
        Xi.append(math.factorial(order)*sum(np.trace(B@rp[k+1]@B@rp[order-k+1]) for B in directions for k in range(order+1))/d)
    analytic=sum(co[j]*Xi[j] for j in range(3)).real
    assert abs(g1+g2-analytic)<1e-9*max(1.,abs(analytic))
    assert np.linalg.norm(R.conj().T@R-(R-R.conj().T)/(2j*z.imag))<1e-9
    return g1,g2


def main():
    if not __debug__:
        raise RuntimeError('Checks require Python without -O.')
    parser=argparse.ArgumentParser();parser.add_argument('--recon',action='store_true');args=parser.parse_args()
    x,c,a,z,P,f,Q,co,q=setup()
    for h in (0,1):
        Qh=Q.subs(x,h);Qp=S.diff(Q,x).subs(x,h);Qpp=S.diff(Q,x,2).subs(x,h)
        g1=S.simplify(S.expand_complex(Qp*S.conjugate(Qp)))/6
        g2=S.simplify(S.re(S.expand_complex(S.conjugate(Qh)*Qpp)))/6
        exact=S.factor(S.diff(f,x,2).subs(x,h))
        assert exact<0 and g1>0 and g2<0 and -g2>g1
        assert S.simplify(g1+g2-exact/12)==0
        xi=[S.factor(S.diff((x-z)**-2,x,j)*(-1)**j/6).subs(x,h) for j in (1,2,3)]
        assert S.simplify(S.re(sum(co[j]*xi[j] for j in range(3)))-exact/12)==0
        print('EXACT scalar H=',h,'p_second=',exact)
        print('Gamma1/Gamma2/total/error-ratio:',*[S.N(v,20) for v in (g1,g2,g1+g2,-g2/g1)])
    Uf=S.Poly(S.Rational(9660,13891)**2*((x-c)**2+a*a)**3-P*P,x)
    roots=S.nroots(Uf,maxsteps=200)
    print('DIAGNOSTIC gap roots:',roots)
    zf=complex(z);cf=[complex(S.N(v,18)) for v in co]
    upper=[complex(v) for v in roots if S.im(v)>0]
    delta=zf-zf.conjugate()
    gap_poly=np.poly1d([1.,-1.])
    for root in upper:
        gap_poly*=np.poly1d([zf-root,root-zf.conjugate()])
    gap_poly*=float(S.sqrt((c*c+a*a)**3*Uf.LC()))/delta**3
    qg=list(reversed(gap_poly.c))
    for label,coeff in [('p',q),('gap',qg)]:
        nd=2/float(a)*sum(j*abs(coeff[j]) for j in range(1,4))
        nd2=4/float(a)**2*sum(j*j*abs(coeff[j]) for j in range(1,4))
        print('DIAGNOSTIC Cayley conditioning',label,'DQ bound',nd,'D2Q bound',nd2)
    rng=np.random.default_rng(8467)
    # Exact sharp translation construction, finite surrogate L and carrier.
    d=4;L=5.;carrier=1.;k=np.arange(d);directions=[];mean=np.eye(d)
    for p in (2,3,5,7):
        s=np.log(p)/L;phase=np.exp(2j*np.pi*k*s)
        A=np.empty((d,d),complex)
        for i in range(d):
            for j in range(d):
                A[i,j]=(1-s)*phase[i] if i==j else (phase[i]-phase[j])/(2j*np.pi*(j-i))
        A*= -np.log(p)/(L*np.sqrt(p))*np.exp(1j*carrier*np.log(p))
        C=A+A.conj().T;T=1j*(A-A.conj().T)
        assert np.max(abs(C.imag))<1e-14 and np.max(abs(T.imag))<1e-14
        directions.extend([C.real/np.sqrt(2),T.real/np.sqrt(2)])
        mean+=C.real
    states=[np.eye(d),np.zeros((d,d)),mean]
    for _ in range(20):
        aa=rng.normal(size=d);hh=rng.normal(size=d)
        H=np.diag(hh)
        for i in range(d):
            for j in range(d):
                if i!=j:H[i,j]=(aa[i]-aa[j])/(np.pi*(j-i))
        states.append(H)
    bridge_rng=np.random.default_rng(8468)
    for utest in (1.,4.,16.):
        for _ in range(3):
            fresh=sum(v*B for v,B in zip(bridge_rng.normal(size=len(directions)),directions))
            states.append(mean+np.sqrt(utest)*fresh)
    minimum=(1e99,None)
    for idx,H in enumerate(states):
        g1,g2=curvature(H,directions,zf,q,cf)
        h1,h2=curvature(H,directions,zf,qg,[-v for v in cf])
        assert abs(g1+g2+h1+h2)<1e-8
        if g1+g2<minimum[0]:minimum=(g1+g2,idx)
    print('DIAGNOSTIC sharp/quadrature regression minimum curvature:',minimum)
    if args.recon:
        ff=S.lambdify(x,f,'numpy');Einf=float((c*c+a*a)**3*S.Rational(9660,13891)**2)
        # Gaussian quadrature samples are diagnostics only, never theorem bounds.
        samples=4096
        W=np.einsum('sj,jkl->skl',rng.normal(size=(samples,len(directions))),np.asarray(directions))
        initial=float(np.mean(ff(np.linalg.eigvalsh(mean))))
        target=Einf-.105
        print('FINITE-PRIME SURROGATE, L=5,d=4; NOT asymptotic WP84: E0=',initial,'target=',target)
        for u in (1,2,4,8,16,32,64,128,256):
            eu=float(np.mean(ff(np.linalg.eigvalsh(mean+np.sqrt(u)*W))))
            print('U',u,'sample E_U',eu,'integral diagnostic E_U-E0',eu-initial,'shortfall',target-(eu-initial))
    print('RESULT: DIRECT_HESSIAN_STENCIL_AGREEMENT; POINTWISE_SIGN_FALSE; INTEGRATED_ERROR_OPEN')


if __name__=='__main__':
    main()

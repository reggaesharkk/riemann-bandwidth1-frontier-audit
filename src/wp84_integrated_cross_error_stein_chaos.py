"""Stein/chaos algebra checks and finite sharp-prime diagnostics; no theorem promotion."""
import argparse
import math
import numpy as np
import sympy as S
from wp84_tail_capped_finite_u_curvature import setup


def exact_gates():
    g=S.symbols('g',real=True)
    # Normalized probabilists' Hermite derivative/lowering and radial laws.
    for n in range(2,9):
        hn=S.hermite_prob(n,g)/S.sqrt(S.factorial(n))
        h2=S.hermite_prob(n-2,g)/S.sqrt(S.factorial(n-2))
        assert S.simplify(S.diff(hn,g,2)-S.sqrt(n*(n-1))*h2)==0
        assert S.simplify(g*S.diff(hn,g)-n*hn-S.diff(hn,g,2))==0
    # Sharp oscillator-form constants, witnessed by exp(t |g|^2).
    t,m=S.symbols('t m',positive=True)
    number=4*t*t*m/(1-4*t)
    cross=2*t*m+number
    assert S.limit(cross-number,t,S.Rational(1,4),dir='-')==m/2
    assert S.limit(cross/number,t,S.Rational(1,4),dir='-')==1
    radius=S.symbols('radius',real=True)
    phi2=(radius-m)/S.sqrt(2*m)
    phi4=(radius**2-2*(m+2)*radius+m*(m+2))/S.sqrt(8*m*(m+2))
    radial_lap=lambda f:4*radius*S.diff(f,radius,2)+2*m*S.diff(f,radius)
    assert S.simplify(radial_lap(phi4)-2*S.sqrt(m+2)*phi2)==0
    assert S.simplify(radial_lap(phi2)-S.sqrt(2*m))==0
    # Mean-free radial level-2/4 chain obstruction grows with dimension.
    print('mean-free two-level lower relative constant sqrt((m+2)/8):')
    for mm in (2,8,32,128):
        print(mm,S.sqrt(S.Rational(mm+2,8)),float(S.sqrt(S.Rational(mm+2,8))))
    x,c,a,z,P,f,Q,co,q=setup()
    qp=S.diff(Q,x);qpp=S.diff(Q,x,2)
    g1=S.simplify(S.expand_complex((qp*S.conjugate(qp)).subs(x,1)))/6
    g2=S.simplify(S.re(S.expand_complex((S.conjugate(Q)*qpp).subs(x,1))))/6
    assert g1>0 and g2<0 and 2*g1+g2<0
    print('H=1 corrector endpoint derivatives:')
    print('Eprime',S.N(g1+g2,18),'Vprime=(uG)prime',S.N(g1,18),'meanprime',S.N(g2,18))
    print('(E+V)prime and (E+uG)prime:',S.N(2*g1+g2,18))
    # Scalar deterministic Gaussian quadrature, independent radial regression.
    nodes,weights=np.polynomial.hermite.hermgauss(160)
    normals=np.sqrt(2)*nodes;weights=weights/np.sqrt(np.pi)
    Qfn=S.lambdify(x,Q,'numpy');Qpfn=S.lambdify(x,qp,'numpy');Qppfn=S.lambdify(x,qpp,'numpy')
    for uu in (.01,.1,.5):
        h=1+np.sqrt(uu/6)*normals
        v=Qfn(h);vp=Qpfn(h);vpp=Qppfn(h)
        hessian=np.sum(weights*(abs(vp)**2+np.real(v.conj()*vpp)))/6
        radial=np.sum(weights*np.real(v.conj()*vp)*normals)/np.sqrt(6*uu)
        step=1e-5*uu
        energy=lambda u:np.sum(weights*abs(Qfn(1+np.sqrt(u/6)*normals))**2)
        diff=(energy(uu+step)-energy(uu-step))/(2*step)
        print('NUMERICAL scalar u / Hessian / radial / difference',uu,hessian,radial,diff)
        if uu==.1:
            hermites=[np.ones_like(normals),normals]
            for n in range(1,16):
                hermites.append((normals*hermites[-1]-np.sqrt(n)*hermites[-2])/np.sqrt(n+1))
            coeff=np.array([np.sum(weights*v*hn) for hn in hermites])
            dn=sum(n*abs(coeff[n])**2 for n in range(len(coeff)))
            cn=sum(np.sqrt((n+1)*(n+2))*np.real(coeff[n].conjugate()*coeff[n+2]) for n in range(len(coeff)-2))
            print('NUMERICAL Hermite orders <=16: Gamma1, Gamma2, sum',dn/uu,cn/uu,(dn+cn)/uu)
    return x,c,a,z,P,f,Q,co,q


def prime_state(T):
    L=np.log(T/(2*np.pi));N=int(np.floor(np.exp(L-np.sqrt(L))))
    d=int(np.floor(T*L/(2*np.pi)))
    primes=[p for p in range(2,N+1) if all(p%q for q in range(2,int(np.sqrt(p))+1))]
    k=np.arange(d);H=np.eye(d);directions=[]
    for p in primes:
        power=p
        while power<=N:
            v=np.log(power)/L;phase=np.exp(2j*np.pi*k*v)
            gap=k[None,:]-k[:,None]
            A=np.zeros((d,d),complex)
            nz=gap!=0
            numerator=phase[:,None]-phase[None,:]
            A[nz]=numerator[nz]/(2j*np.pi*gap[nz])
            np.fill_diagonal(A,(1-v)*phase)
            A*= -np.log(p)/(L*np.sqrt(power))*np.exp(1j*T*np.log(power))
            C=(A+A.conj().T).real
            H+=C
            if power==p:
                directions.extend([C/np.sqrt(2),(1j*(A-A.conj().T)).real/np.sqrt(2)])
            power*=p
    return H,np.asarray(directions),L,N


def recon(data,samples,quadrature):
    x,c,a,z,P,f,Q,co,q=data
    ff=S.lambdify(x,f,'numpy');pf=S.lambdify(x,S.diff(f,x),'numpy')
    pp=S.lambdify(x,S.diff(f,x,2),'numpy');qf=S.lambdify(x,Q,'numpy');qpf=S.lambdify(x,S.diff(Q,x),'numpy')
    Einf=float((c*c+a*a)**3*S.Rational(9660,13891)**2)
    nodes,weights=np.polynomial.legendre.leggauss(quadrature)
    rng=np.random.default_rng(846353)
    for T in (128,256):
        H,B,L,N=prime_state(T);d=len(H)
        W=np.einsum('sj,jkl->skl',rng.normal(size=(samples,len(B))),B)
        def evaluate(u,endpoints=False):
            means=np.zeros((d,d),complex);energy=g1=derivative=0.
            for noise in W:
                lam,O=np.linalg.eigh(H+np.sqrt(u)*noise)
                val=qf(lam);der=qpf(lam)
                diff=lam[:,None]-lam[None,:]
                close=abs(diff)<1e-10
                div=np.empty((d,d),complex);pdiv=np.empty((d,d))
                nd=val[:,None]-val[None,:];pd=pf(lam)[:,None]-pf(lam)[None,:]
                div[~close]=nd[~close]/diff[~close]
                pdiv[~close]=pd[~close]/diff[~close]
                div[close]=np.broadcast_to(der[:,None],(d,d))[close]
                pdiv[close]=np.broadcast_to(pp(lam)[:,None],(d,d))[close]
                covariance=sum(abs(O.T@direction@O)**2 for direction in B)
                g1+=np.sum(covariance*abs(div)**2)/d
                derivative+=np.sum(covariance*pdiv)/(2*d)
                energy+=np.mean(abs(val)**2)
                if endpoints:means+=(O*val)@O.T
            energy/=samples;g1/=samples;derivative/=samples
            mu=np.sum(abs(means/samples)**2)/d if endpoints else None
            return g1,derivative-g1,energy,mu
        initial=float(np.mean(ff(np.linalg.eigvalsh(H))))
        print('FINITE SHARP PRIME DIAGNOSTIC T,d,L,N,m,samples,E0:',T,d,L,N,len(B),samples,initial)
        print('U P Err P-Err max-node-error-ratio integrated-ratio V_U mean_U uG_U endpoint-integral target-shortfall')
        for U in (1,2,4,8,16):
            ps=er=0.;ratios=[]
            for node,weight in zip(nodes,weights):
                uu=U*(node+1)/2
                pos,cross,_,_=evaluate(uu)
                ps+=weight*U/2*pos;er-=weight*U/2*cross
                ratios.append(-cross/pos if pos>0 else float('nan'))
            gp,_,eu,mu=evaluate(U,True)
            print(U,ps,er,ps-er,max(ratios),er/ps,eu-mu,mu,U*gp,eu-initial,Einf-.105-(ps-er))
        print('Quadrature and Monte Carlo errors are NOT certified; full sharp section, s0=a_phi=1; no adaptive endpoint or taper promotion.')


def main():
    if not __debug__:
        raise RuntimeError('Checks require Python without -O.')
    parser=argparse.ArgumentParser();parser.add_argument('--recon',action='store_true');parser.add_argument('--samples',type=int,default=64);parser.add_argument('--nodes',type=int,default=12)
    args=parser.parse_args()
    data=exact_gates()
    if args.recon:
        if args.samples<2:raise ValueError('Use at least two diagnostic samples.')
        recon(data,args.samples,args.nodes)
    print('RESULT: RADIAL_STEIN_CHAOS_IDENTITIES_PASS; UNIVERSAL_HARDY_BOUND_INSUFFICIENT; ACTUAL_CHAIN_INEQUALITY_OPEN')


if __name__=='__main__':
    main()

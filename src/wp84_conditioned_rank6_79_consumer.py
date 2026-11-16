#!/usr/bin/env python3
"""Exact + finite-matrix regression gate for the conditioned rank-six >79 consumer."""

from fractions import Fraction as F
import numpy as np

QINT=[
    (44,2205),
    (-5695,169),
    (-192,-5495),
    (1936,0),
]
DEN=5000

EXPECTED_DEFECT=F(
    1272283602671916206561064875108101,
    12442212289373925054228673142500000,
)
EXPECTED_SIMPLE=F(
    4948822542015046320553271696141899,
    6221106144686962527114336571250000,
)

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    c=[F(0)]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def sub(a,b):
    return add(a,[-v for v in b])

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return trim(c)

def scale(a,s):
    return trim([s*x for x in a])

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and not (len(a)==1 and a[0]==0):
        d=len(a)-len(b)
        z=a[-1]/b[-1]
        q[d]+=z
        for j in range(len(b)):
            a[d+j]-=z*b[j]
        a=trim(a)
    return trim(q),trim(a)

def egcd(a,b):
    r0,r1=trim(a),trim(b)
    s0,s1=[F(1)],[F(0)]
    t0,t1=[F(0)],[F(1)]
    while not (len(r1)==1 and r1[0]==0):
        q,r=divmod_poly(r0,r1)
        r0,r1=r1,r
        s0,s1=s1,sub(s0,mul(q,s1))
        t0,t1=t1,sub(t0,mul(q,t1))
    lead=r0[-1]
    return scale(r0,1/lead),scale(s0,1/lead),scale(t0,1/lead)

def mod_poly(a,m):
    return divmod_poly(a,m)[1]

def inv_mod(a,m):
    g,s,_=egcd(a,m)
    assert g==[F(1)]
    return mod_poly(s,m)

def exact_scalar_gate():
    # Directly frozen support numerator:
    # p(x)-1=S(x)/[12500000(1+x^2)^3].
    S=[
        2001,
        -84028544,
        186573135,
        -303496416,
        183847891,
        -82863712,
        2645,
    ]
    # x=-y makes every coefficient positive.
    Sy=[F(S[k])*(-1)**k for k in range(7)]
    assert all(v>0 for v in Sy),Sy

    den=scale(mul(mul([F(1),F(0),F(1)],[F(1),F(0),F(1)]),[F(1),F(0),F(1)]),F(12500000))
    num=add(den,[F(v) for v in S])

    # Christoffel cubic.
    P=[F(1),F(-43428,13891),F(37704,13891),F(-9660,13891)]

    R=mod_poly(mul(num,inv_mod(den,P)),P)
    R += [F(0)]*(3-len(R))

    w0=F(1415,13891)
    p0=F(12502001,12500000)
    Efull=R[0]+R[1]+F(4,3)*R[2]
    E=Efull-w0*R[0]+w0*p0
    simple=1-2*E

    assert E==EXPECTED_DEFECT,(E,EXPECTED_DEFECT)
    assert simple==EXPECTED_SIMPLE,(simple,EXPECTED_SIMPLE)
    assert E<F(105,1000)
    assert simple>F(79,100)

    print("support coefficients at x=-y:",Sy)
    print("model defect =",E,"~",float(E))
    print("model simple =",simple,"~",float(simple))
    print(">79 defect cushion =",float(F(105,1000)-E))

def build_sharp(d,L,T,ys,cs):
    tau=T+2*np.pi*np.arange(d)/L
    q=sum(c*np.exp(1j*tau*y) for y,c in zip(ys,cs))
    qp=sum(1j*c*y*np.exp(1j*tau*y) for y,c in zip(ys,cs))
    a=q.imag
    b=q.real
    ap=qp.imag

    H=np.empty((d,d),dtype=float)
    for k in range(d):
        for l in range(d):
            if k==l:
                H[k,l]=1+2*b[k]-2*ap[k]/L
            else:
                H[k,l]=(a[k]-a[l])/(np.pi*(l-k))
    return H,a

def q_of_U(U):
    I=np.eye(U.shape[0],dtype=complex)
    return (
        (44+2205j)*I
        +(-5695+169j)*U
        +(-192-5495j)*(U@U)
        +1936*(U@U@U)
    )/5000.0

def finite_matrix_gate():
    d=61
    L=13.75
    T=19.125
    ys=np.array([0.31,0.83,1.9,3.2,5.7,8.4])
    cs=np.array([0.4,-0.17,0.09,0.055,-0.021,0.013])

    H,a=build_sharp(d,L,T,ys,cs)
    I=np.eye(d,dtype=complex)
    D=np.diag(np.arange(d,dtype=float))
    R=np.linalg.inv(H-1j*I)
    U=(H+1j*I)@R
    Q=q_of_U(U)

    CU=D@U-U@D
    CQ=D@Q-Q@D

    assert np.linalg.norm(U.conj().T@U-I,2)<3e-12
    assert np.linalg.norm(Q.T-Q,'fro')<3e-12
    assert np.linalg.norm(CQ.T+CQ,'fro')<3e-11

    q1=(-5695+169j)/5000
    q2=(-192-5495j)/5000
    q3=1936/5000
    B0=q1*I+q2*U+q3*(U@U)
    B1=q2*I+q3*U

    pred=CU@B0+U@CU@B1+(U@U)@CU*q3
    assert np.linalg.norm(CQ-pred,'fro')<2e-10

    # Exact two-column sharp source.
    one=np.ones(d)
    Ra=R@a
    R1=R@one
    G2=np.column_stack([(2j/np.pi)*Ra,(-2j/np.pi)*R1])
    H2=np.column_stack([R1,Ra])
    assert np.linalg.norm(CU-G2@H2.T,'fro')<2e-10

    # Explicit six-column polynomial source.
    G6=np.column_stack([G2,U@G2,(U@U)@G2])
    H6T=np.vstack([H2.T@B0,H2.T@B1,q3*H2.T])
    assert np.linalg.norm(CQ-G6@H6T,'fro')<3e-10

    sv=np.linalg.svd(CQ,compute_uv=False)
    rank=int(np.sum(sv>1e-9*max(1.0,sv[0])))
    assert rank<=6,(rank,sv[:10])

    # Skew-symmetric matrices have paired nonzero singular values.
    assert abs(sv[0]-sv[1])<2e-10
    assert abs(sv[2]-sv[3])<2e-10
    assert abs(sv[4]-sv[5])<2e-10

    total=np.trace(Q.conj().T@Q).real/d
    diag=np.sum(np.abs(np.diag(Q))**2)/d
    off=sum(
        abs(CQ[i,j])**2/((i-j)**2)
        for i in range(d)
        for j in range(d)
        if i!=j
    )/d
    assert abs(total-diag-off)<2e-11

    # The nonzero singular spectrum is already encoded by 6x6 Gram data.
    H6=H6T.T
    gramG=G6.conj().T@G6
    gramH=H6.T@np.conj(H6)
    small=np.linalg.eigvals(gramH@gramG)
    small=np.sort(np.maximum(np.real_if_close(small).real,0))[::-1]
    small_sv=np.sqrt(small)
    assert np.max(np.abs(sv[:6]-small_sv[:6]))<3e-9

    print("rank[D,Q] =",rank)
    print("paired singular values =",sv[:6])
    print("six-by-six recovered =",small_sv[:6])
    print("energy total/diag/off =",total,diag,off)
    print("RESULT: WP84_CONDITIONED_RANK6_79_CONSUMER_PASS")

def main():
    exact_scalar_gate()
    finite_matrix_gate()

if __name__=="__main__":
    main()

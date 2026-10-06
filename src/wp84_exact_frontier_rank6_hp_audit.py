#!/usr/bin/env python3
"""80-digit deterministic algebra audit for the exact-frontier rank-six consumer."""

import mpmath as mp

mp.mp.dps=80

A=mp.mpf(43428)/13891
B=mp.mpf(37704)/13891
C=mp.mpf(9660)/13891
a=(mp.mpf(13891)/9660)**(mp.mpf(1)/3)

q=[
    (A*a-C*a**3 + 1j*(-1+B*a*a))/8,
    (-A*a-3*C*a**3 + 1j*(3+B*a*a))/8,
    (-A*a-3*C*a**3 + 1j*(-3-B*a*a))/8,
    (A*a-C*a**3 + 1j*(1-B*a*a))/8,
]

def fro(M):
    return mp.sqrt(sum(abs(M[i,j])**2 for i in range(M.rows) for j in range(M.cols)))

def build_state():
    d=11
    L=mp.mpf('13.75')
    T=mp.mpf('19.125')
    ys=[mp.mpf(x) for x in ('0.31','0.83','1.9','3.2','5.7','8.4')]
    cs=[mp.mpf(x) for x in ('0.4','-0.17','0.09','0.055','-0.021','0.013')]

    tau=[T+2*mp.pi*k/L for k in range(d)]
    z=[]
    zp=[]
    for t in tau:
        z.append(sum(c*mp.e**(1j*t*y) for y,c in zip(ys,cs)))
        zp.append(sum(1j*c*y*mp.e**(1j*t*y) for y,c in zip(ys,cs)))

    alpha=[mp.im(x) for x in z]
    beta=[mp.re(x) for x in z]
    ap=[mp.im(x) for x in zp]

    H=mp.matrix(d)
    for i in range(d):
        for j in range(d):
            if i==j:
                H[i,j]=1+2*beta[i]-2*ap[i]/L
            else:
                H[i,j]=(alpha[i]-alpha[j])/(mp.pi*(j-i))
    return H,mp.matrix(alpha)

def main():
    H,alpha=build_state()
    d=H.rows
    I=mp.eye(d)
    D=mp.diag([mp.mpf(i) for i in range(d)])

    R=(H-1j*a*I)**-1
    U=(H+1j*a*I)*R

    Q=mp.zeros(d)
    Uk=mp.eye(d)
    for k in range(4):
        Q += q[k]*Uk
        Uk=Uk*U

    CU=D*U-U*D
    CQ=D*Q-Q*D

    unit=fro(U.conjugate().transpose()*U-I)
    sym=fro(Q.transpose()-Q)
    skew=fro(CQ.transpose()+CQ)

    q1,q2,q3=q[1],q[2],q[3]
    B0=q1*I+q2*U+q3*(U*U)
    B1=q2*I+q3*U

    pred=CU*B0+U*CU*B1+(U*U)*CU*q3
    poly=fro(CQ-pred)

    one=mp.matrix([1]*d)
    Ra=R*alpha
    R1=R*one

    G2=mp.matrix(d,2)
    H2=mp.matrix(d,2)
    for i in range(d):
        G2[i,0]=(2j*a/mp.pi)*Ra[i]
        G2[i,1]=(-2j*a/mp.pi)*R1[i]
        H2[i,0]=R1[i]
        H2[i,1]=Ra[i]

    source=fro(CU-G2*H2.transpose())

    UG2=U*G2
    U2G2=U*UG2
    G6=mp.matrix(d,6)
    for i in range(d):
        for j in range(2):
            G6[i,j]=G2[i,j]
            G6[i,j+2]=UG2[i,j]
            G6[i,j+4]=U2G2[i,j]

    H6T=mp.matrix(6,d)
    blocks=[
        H2.transpose()*B0,
        H2.transpose()*B1,
        q3*H2.transpose(),
    ]
    for b,blk in enumerate(blocks):
        for i in range(2):
            for j in range(d):
                H6T[2*b+i,j]=blk[i,j]

    factor=fro(CQ-G6*H6T)

    total=sum(abs(Q[i,j])**2 for i in range(d) for j in range(d))/d
    diag=sum(abs(Q[i,i])**2 for i in range(d))/d
    off=sum(
        abs(CQ[i,j])**2/((i-j)**2)
        for i in range(d)
        for j in range(d)
        if i!=j
    )/d
    energy=abs(total-diag-off)

    vals={
        "unitarity":unit,
        "Q_symmetry":sym,
        "CQ_skew":skew,
        "polynomial_commutator":poly,
        "rank2_source":source,
        "six_column_factor":factor,
        "energy_identity":energy,
    }

    for k,v in vals.items():
        print(k,mp.nstr(v,12))
        assert v < mp.mpf('1e-70'),(k,v)

    print("a_star",mp.nstr(a,30))
    print("RESULT: WP84_EXACT_FRONTIER_RANK6_HP_AUDIT_PASS")

if __name__=="__main__":
    main()

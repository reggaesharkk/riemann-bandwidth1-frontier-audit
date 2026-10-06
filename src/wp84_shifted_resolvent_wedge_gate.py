#!/usr/bin/env python3
"""Finite-dimensional regression for the shifted consumer's 3x3 wedge factorization.

Exact Fraction checks cover the coefficient matrix M and its invariants.
Floating matrix checks cover only finite algebra, not a large-T zeta estimate.
"""
from fractions import Fraction as F
import math, random

def zadd(x,y): return (x[0]+y[0], x[1]+y[1])
def zsub(x,y): return (x[0]-y[0], x[1]-y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zscale(c,x): return (c*x[0],c*x[1])
def zpow(x,n):
    out=(F(1),F(0))
    for _ in range(n): out=zmul(out,x)
    return out
def as_complex(x): return complex(float(x[0]),float(x[1]))

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(c,A): return [[c*x for x in row] for row in A]
def eye(n): return [[complex(i==j) for j in range(n)] for i in range(n)]
def tr(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def inv(A):
    n=len(A); X=[list(map(complex,row))+eye(n)[i] for i,row in enumerate(A)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(X[i][k])); X[k],X[p]=X[p],X[k]
        v=X[k][k]; X[k]=[x/v for x in X[k]]
        for i in range(n):
            if i!=k:
                v=X[i][k]; X[i]=[x-v*y for x,y in zip(X[i],X[k])]
    return [row[n:] for row in X]
def err(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def exact_coefficients():
    A,B,C=F(43428,13891),F(37704,13891),F(9660,13891)
    z=(F(4,5),F(4,5))
    p0,p1,p2,p3=F(1),-A,B,-C
    b1=zadd(zscale(F(3),zmul(z,(p3,F(0)))),(p2,F(0)))
    b2=zadd(zadd(zscale(F(3),zmul(zpow(z,2),(p3,F(0)))),
                 zscale(F(2),zmul(z,(p2,F(0))))),(p1,F(0)))
    b3=zadd(zadd(zadd(zmul(zpow(z,3),(p3,F(0))),
                         zmul(zpow(z,2),(p2,F(0)))),
                 zmul(z,(p1,F(0)))),(p0,F(0)))
    expected=[
        (F(14520,13891),F(-23184,13891)),
        (F(84492,69455),F(23232,13891)),
        (F(-273989,347275),F(90672,347275)),
    ]
    assert [b1,b2,b3]==expected
    trace=zadd(b1,b3)
    second=zsub(zsub(zmul(b1,b3),zmul(b2,b2)),zmul(b3,b3))
    det=zscale(F(-1),zpow(b3,3))
    assert trace==(F(89011,347275),F(-488928,347275))
    assert second==(F(45103112063,120599925625),F(-249325314384,120599925625))
    assert det==(F(13810617575994941,41881339171421875),
                 F(-19674781705321488,41881339171421875))
    assert b3!=(F(0),F(0))
    return A,B,C,b1,b2,b3

def main():
    A,B,C,b1q,b2q,b3q=exact_coefficients()
    b1,b2,b3=map(as_complex,(b1q,b2q,b3q))
    z=.8+.8j
    r3=(math.sqrt(32/25))**3
    d=9; rng=random.Random(8406); alpha=[rng.uniform(-1,1) for _ in range(d)]
    H=[[0.0 for _ in range(d)] for _ in range(d)]
    for i in range(d):
        H[i][i]=rng.uniform(-.7,.7)
        for j in range(i):
            H[i][j]=H[j][i]=(alpha[j]-alpha[i])/(math.pi*(i-j))
    Hc=[[complex(x) for x in row] for row in H]
    R=inv([[Hc[i][j]-(z if i==j else 0) for j in range(d)] for i in range(d)])
    R2=mm(R,R); R3=mm(R2,R)
    H2=mm(Hc,Hc); H3=mm(H2,Hc)
    PH=add(add(add(eye(d),scale(-float(A),Hc)),scale(float(B),H2)),scale(-float(C),H3))
    Q=scale(r3,mm(PH,R3))
    D=[[complex(i if i==j else 0) for j in range(d)] for i in range(d)]
    comm=add(mm(D,Q),scale(-1,mm(Q,D)))
    one=[[1.0] for _ in range(d)]; al=[[x] for x in alpha]
    Us=[]; Vs=[]
    for power in (R,R2,R3):
        Us.append(mm(power,one)); Vs.append(mm(power,al))
    U=[[Us[k][i][0] for k in range(3)] for i in range(d)]
    V=[[Vs[k][i][0] for k in range(3)] for i in range(d)]
    M=[[b1,b2,b3],[b2,b3,0j],[b3,0j,0j]]
    wedge=add(mm(mm(U,M),tr(V)),scale(-1,mm(mm(V,M),tr(U))))
    pred=scale(-r3/math.pi,wedge)
    comm_res=err(comm,pred)
    assert comm_res<2e-10,comm_res
    lhs=sum(abs(Q[i][j])**2 for i in range(d) for j in range(d))/d
    rhs=sum(abs(Q[i][i])**2 for i in range(d))/d
    rhs+=sum(abs(comm[i][j])**2/(i-j)**2 for i in range(d) for j in range(d) if i!=j)/d
    energy_res=abs(lhs-rhs)
    assert energy_res<1e-12,(lhs,rhs)
    print('exact M coefficients and invariants: PASS')
    print('max_commutator_factorization_residual =',comm_res)
    print('positive_energy_identity_residual =',energy_res)
    print('RESULT: SHIFTED_RESOLVENT_WEDGE_FACTOR_PASS (finite algebra only)')
if __name__=='__main__': main()

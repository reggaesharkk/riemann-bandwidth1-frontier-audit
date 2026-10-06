#!/usr/bin/env python3
"""Finite-dimensional regression for the shifted consumer's 3x3 wedge factorization.

Checks algebra only; this is not a large-T zeta-side estimate.
"""
from fractions import Fraction as F
import math, random

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
def err(A,B): return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def main():
    A=F(43428,13891); B=F(37704,13891); C=F(9660,13891)
    z=.8+.8j
    p0,p1,p2,p3=1,-A,B,-C
    b1=3*z*float(p3)+float(p2)
    b2=3*z*z*float(p3)+2*z*float(p2)+float(p1)
    b3=z**3*float(p3)+z*z*float(p2)+z*float(p1)+float(p0)
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
    print('max_commutator_factorization_residual =',comm_res)
    print('positive_energy_identity_residual =',energy_res)
    print('RESULT: SHIFTED_RESOLVENT_WEDGE_FACTOR_PASS (finite algebra only)')
if __name__=='__main__': main()

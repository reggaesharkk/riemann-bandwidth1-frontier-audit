#!/usr/bin/env python3
"""Exact finite-matrix falsifier for automatic V_sum cancellation.

Take the non-cyclic shift S on N=5 and the exact carrier-free sharp operator

    H = S + S^*.

At z=i let R=(H-iI)^(-1).  All arithmetic below is exact over Q(i).

The multiplication/diagonal surrogate would kill first-order shifted traces
and same-sign variance traces.  The true resolvent of H does not:

    first shifted trace = 7 i / 20,
    V_sum               = 17 i / 80,
    V_diff              =  3 i / 80.

Thus V_sum is not removed by an algebraic phase cancellation; here it is more
than five times the mixed branch.

No asymptotic conclusion is inferred from this finite example.  Its purpose is
to falsify any proof step that drops V_sum solely from carrier/transpose
symmetry once the intermediate resolvent has left the multiplication algebra.
"""
from fractions import Fraction as F

# Gaussian rational z = a + i b represented by (a,b).
Z=(F(0),F(0)); O=(F(1),F(0)); I=(F(0),F(1))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    return (x[0]*y[0]-x[1]*y[1],
            x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    assert d
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def iszero(x): return x==Z

def mm(A,B):
    n=len(A); p=len(B); m=len(B[0])
    assert len(A[0])==p
    C=[[Z for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if iszero(A[i][k]): continue
            for j in range(m):
                if not iszero(B[k][j]):
                    C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
    return C

def madd(A,B):
    return [[add(x,y) for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]

def trans(A):
    return [list(row) for row in zip(*A)]

def eye(n):
    return [[O if i==j else Z for j in range(n)] for i in range(n)]

def minv(A):
    n=len(A)
    M=[A[i][:]+eye(n)[i][:] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if not iszero(M[i][c]))
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[div(x,q) for x in M[c]]
        for i in range(n):
            if i==c or iszero(M[i][c]): continue
            q=M[i][c]
            M[i]=[sub(x,mul(q,y)) for x,y in zip(M[i],M[c])]
    return [row[n:] for row in M]

def scale(A,q):
    return [[mul(q,x) for x in row] for row in A]

def trace_n(A):
    n=len(A)
    s=Z
    for i in range(n): s=add(s,A[i][i])
    return (s[0]/n,s[1]/n)

def prod(*As):
    out=As[0]
    for A in As[1:]:
        out=mm(out,A)
    return out

def fmt(z):
    a,b=z
    if a==0: return f"{b}*i"
    if b==0: return str(a)
    return f"({a})+({b})*i"

def main():
    N=5
    S=[[Z for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        S[i][i+1]=O
    Sm=trans(S)
    H=madd(S,Sm)

    # R=(H-iI)^-1.
    A=[row[:] for row in H]
    for i in range(N):
        A[i][i]=sub(A[i][i],I)
    R=minv(A)

    first=add(trace_n(prod(R,S,R)),
              trace_n(prod(R,Sm,R)))

    vsum=add(trace_n(prod(R,S,R,S,R)),
             trace_n(prod(R,Sm,R,Sm,R)))

    vdiff=add(trace_n(prod(R,S,R,Sm,R)),
              trace_n(prod(R,Sm,R,S,R)))

    assert first==(F(0),F(7,20))
    assert vsum==(F(0),F(17,80))
    assert vdiff==(F(0),F(3,80))

    # Diagonal surrogate R=I kills same-sign/first-order shifted traces.
    Rd=eye(N)
    first_diag=add(trace_n(prod(Rd,S,Rd)),
                   trace_n(prod(Rd,Sm,Rd)))
    vsum_diag=add(trace_n(prod(Rd,S,Rd,S,Rd)),
                  trace_n(prod(Rd,Sm,Rd,Sm,Rd)))
    assert first_diag==Z
    assert vsum_diag==Z

    print("first true =",fmt(first))
    print("V_sum true =",fmt(vsum))
    print("V_diff true =",fmt(vdiff))
    print("V_sum / V_diff =",F(17,3))
    print("first diagonal surrogate =",fmt(first_diag))
    print("V_sum diagonal surrogate =",fmt(vsum_diag))
    print("RESULT: WP84_VSUM_AUTOMATIC_CANCELLATION_FALSIFIED")

if __name__=="__main__":
    main()

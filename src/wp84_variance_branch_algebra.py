#!/usr/bin/env python3
"""WP84 exact algebra gate for the real modulated-Toeplitz variance map."""
P=257
N=8
OMEGA=pow(3,(P-1)//N,P)
assert pow(OMEGA,N,P)==1

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%P for j in range(n)] for i in range(n)]

def add(*Ms):
    n=len(Ms[0])
    return [[sum(M[i][j] for M in Ms)%P for j in range(n)] for i in range(n)]

def smul(c,A):
    return [[c*x%P for x in row] for row in A]

def diag(v):
    n=len(v)
    return [[v[i] if i==j else 0 for j in range(n)] for i in range(n)]

def main():
    coeff={r:((11*r*r+7*r+19)%P) for r in range(-(N-1),N)}
    T=[[coeff[i-j] for j in range(N)] for i in range(N)]
    A=[[((17*i+23*j+5*i*j+31)%P) for j in range(N)] for i in range(N)]
    D=diag([pow(OMEGA,i,P) for i in range(N)])
    Ds=diag([pow(OMEGA,-i,P) for i in range(N)])

    Cp=mm(mm(D,T),D)
    Cm=mm(mm(Ds,T),Ds)
    C=smul(pow(2,P-2,P),add(Cp,Cm))
    lhs=mm(mm(C,A),C)

    bpp=mm(mm(mm(mm(mm(D,T),D),A),D),mm(T,D))
    bpm=mm(mm(mm(mm(mm(D,T),D),A),Ds),mm(T,Ds))
    bmp=mm(mm(mm(mm(mm(Ds,T),Ds),A),D),mm(T,D))
    bmm=mm(mm(mm(mm(mm(Ds,T),Ds),A),Ds),mm(T,Ds))
    rhs=smul(pow(4,P-2,P),add(bpp,bpm,bmp,bmm))

    assert lhs==rhs
    print("dimension",N)
    print("RESULT: WP84_VARIANCE_BRANCH_ALGEBRA_PASS")

if __name__=="__main__":
    main()

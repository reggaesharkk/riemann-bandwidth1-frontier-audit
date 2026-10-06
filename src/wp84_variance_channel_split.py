#!/usr/bin/env python3
"""WP84 exact finite-field gate for the variance-channel multiplication rule."""
P=23
N=11
W=2
INV2N=pow(2,-1,N)
INV2P=pow(2,-1,P)

assert pow(W,N,P)==1

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%P
             for j in range(n)] for i in range(n)]

def madd(A,B):
    n=len(A)
    return [[(A[i][j]+B[i][j])%P for j in range(n)] for i in range(n)]

def smul(c,A):
    return [[c*x%P for x in row] for row in A]

def diag(v):
    n=len(v)
    return [[v[i] if i==j else 0 for j in range(n)] for i in range(n)]

def D(A0,y,sgn):
    vals=[]
    for k in range(N):
        e=((A0+k)*y*INV2N)%N
        if sgn<0:
            e=(-e)%N
        vals.append(pow(W,e,P))
    return diag(vals)

def toeplitz(y):
    coeff=[(7+3*r+5*r*r+2*y*r)%P for r in range(N)]
    return [[coeff[(i-j)%N] for j in range(N)] for i in range(N)]

def Rmat():
    return [[(3+5*i+7*j+2*i*j)%P for j in range(N)] for i in range(N)]

def channel(A0,y,sgn,tau):
    T=toeplitz(y); R=Rmat()
    Ds=D(A0,y,sgn); Dt=D(A0,y,tau)
    return mm(mm(mm(mm(Ds,T),Ds),R),mm(mm(Dt,T),Dt))

def C(A0,y):
    T=toeplitz(y)
    Cp=mm(mm(D(A0,y,+1),T),D(A0,y,+1))
    Cm=mm(mm(D(A0,y,-1),T),D(A0,y,-1))
    return smul(INV2P,madd(Cp,Cm))

def main():
    checks=0
    for A0 in (0,1,3,7):
        for y in (1,2,4,8,10):
            R=Rmat()
            lhs=mm(mm(C(A0,y),R),C(A0,y))
            rhs=[[0]*N for _ in range(N)]
            for sgn in (+1,-1):
                for tau in (+1,-1):
                    rhs=madd(rhs,channel(A0,y,sgn,tau))
            rhs=smul(pow(4,-1,P),rhs)
            assert lhs==rhs

            for sgn in (+1,-1):
                for tau in (+1,-1):
                    got=channel(A0,y,sgn,tau)
                    base=channel(0,y,sgn,tau)
                    carr=pow(W,(A0*y*(sgn+tau))%N,P)
                    assert got==smul(carr,base)
                    if sgn==-tau:
                        assert carr==1
                    checks+=1
    print("exact channel checks =",checks)
    print("RESULT: WP84_VARIANCE_CHANNEL_SPLIT_PASS")

if __name__=="__main__":
    main()

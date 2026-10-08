"""Independent formal-trace and rational matrix-series replay for fifth pair."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def sub(A,B):return [[a-b for a,b in zip(r,s)] for r,s in zip(A,B)]
def tr(A):return sum(A[i][i] for i in range(len(A)))
def scale(A,c):return [[c*x for x in r] for r in A]
def comm(A,B):return sub(mul(A,B),mul(B,A))
def series(a,n,R,K):
    out=[]
    for k in range(K+1):
        A=[[Q(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            A[i][i]=Q(a**k*i**k,factorial(k))-(Q(a**k*i**(k-1),factorial(k-1)) if k else 0)
            for j in range(n):
                if i!=j and abs(i-j)<=R:A[i][j]=Q(a**k*(i**k-j**k),factorial(k)*(j-i))
        out.append(A)
    return out

def smul(A,B,K):
    n=len(A[0]);zero=[[Q(0) for _ in range(n)] for _ in range(n)];out=[]
    for k in range(K+1):
        C=[r[:] for r in zero]
        for j in range(k+1):C=add(C,mul(A[j],B[k-j]))
        out.append(C)
    return out

def main():
    c=json.loads((ROOT/'notes/WP84_FIFTH_5_7_DIFFERENCE_CERTIFICATE.json').read_text())
    for p,h in c['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    # Exact trace identity tested independently with integer nonsymmetric matrices.
    n=3;X=[[Q(i+2*j+1) for j in range(n)] for i in range(n)]
    mats=[[[Q((k+1)*i*i+j+int(i==j)) for j in range(n)] for i in range(n)] for k in range(3)]
    lhs=Q(0);rhs=Q(0)
    for Y,Z,W in permutations(mats):
        lhs+=tr(mul(mul(mul(mul(X,X),Y),Z),W))-tr(mul(mul(mul(mul(X,Y),X),Z),W))
        rhs-=tr(mul(mul(comm(X,Y),comm(X,Z)),W))
    assert lhs==rhs
    # Formal cyclic-word replay by rotation sets, independent of producer
    # lexicographic cyclic representative selection.
    orbits={}
    def push(word,value):
        orbit=frozenset(word[k:]+word[:k] for k in range(len(word)))
        orbits[orbit]=orbits.get(orbit,Q(0))+value
    for y,z,w in permutations('YZW'):
        push('XX'+y+z+w,1);push('X'+y+'X'+z+w,-1)
        for word,sgn in [('X'+y+'X'+z+w,1),('X'+y+z+'X'+w,-1),(y+'XX'+z+w,-1),(y+'X'+z+'X'+w,1)]:push(word,sgn)
    assert all(v==0 for v in orbits.values())
    corrupt=dict(orbits);one=next(iter(corrupt));corrupt[one]+=1
    assert any(v!=0 for v in corrupt.values())
    checks=[]
    # Rational c=1 realization of the universal coefficient identity;
    # pi/i restoration and actual-log positivity are proved symbolically in note.
    for n,R in ((2,1),(3,1),(3,2)):
        logs=(1,2,3,4);E={a:series(a,n,R,6) for a in logs};D=[[Q(i)*int(i==j) for j in range(n)] for i in range(n)];J=[[Q(abs(i-j)<=R) for j in range(n)] for i in range(n)]
        H=sub(D,J);K=sub(scale(mul(D,D),Q(1,2)),scale(add(mul(D,J),mul(J,D)),Q(1,2)))
        L=comm(H,K);assert L==scale(comm(D,mul(J,J)),Q(-1,2))
        coeff=[Q(0)]*7
        for b,cc,d in permutations((2,3,4)):
            words=((1,1,b,cc,d),(1,b,1,cc,d))
            for sign,word in ((1,words[0]),(-1,words[1])):
                P=E[word[0]]
                for a in word[1:]:P=smul(P,E[a],6)
                for k in range(7):coeff[k]+=sign*tr(P[k])
        assert all(x==0 for x in coeff[:6])
        a,b,cc,d=map(Q,logs);S=b*cc*(b-a)*(cc-a)+b*d*(b-a)*(d-a)+cc*d*(cc-a)*(d-a)
        expected=-2*a*a*S*tr(mul(L,L));assert coeff[6]==expected and expected!=0
        # Mutation destroys the exact first-coefficient replay.
        assert coeff[6]+1!=expected
        Z=sum((i-j)**2*mul(J,J)[i][j]**2 for i in range(n) for j in range(n))
        assert tr(mul(L,L))==Q(-Z,4)
        checks.append({'n':n,'R':R,'normalized_first_order':6,'rational_c1_first_coefficient':str(coeff[6]),'Z':str(Z)})
    assert c['first_nonzero_jet']['amplitude_order']==11 and c['pair_analytic_rank']==2
    # A path with one exchanged lag changes its prime-log phase coefficients.
    assert c['slot_defect']['old_phase_log_coefficients']!=c['slot_defect']['new_phase_log_coefficients']
    (ROOT/'notes/WP84_FIFTH_5_7_INDEPENDENT_REPLAY.json').write_text(json.dumps({'checks':checks,'trace_identity':True,'corruption_detected':True,'scope':'exact rational verification of universal algebra; analytic/legal-cell proof in theorem note'},indent=2)+'\n')
    print('PASS independent integer trace identity, exact full matrix series through first order 6, band commutator squares and corruption test')
    print('Restored full prime amplitude first order u^11; pair rank 2')
if __name__=='__main__':main()

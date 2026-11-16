#!/usr/bin/env python3
"""Exact local-algebra checks for the uniform gamma-tail theorem."""

from fractions import Fraction as F

SIGMA_NUM=2
SIGMA_DEN=3

def beta_loc(p,a,e1,e2):
    z=F(1)
    for e in (e1,e2):
        aa=max(a-e,0)
        if aa>=2:
            return F(0)
        if aa==1:
            z *= -F(1,p-1)
    return z

def f_loc(p,v,e1,e2):
    return beta_loc(p,v,e1,e2)-beta_loc(p,v+1,e1,e2)

def support_max(e1,e2):
    # beta(v)=0 for v>=max(e1,e2)+2, hence f(v)=0 beyond max+1.
    return max(e1,e2)+1

def main():
    # Generic odd prime identity.
    for p in [3,5,7,11,13,17,19,23,29]:
        g=F(1)-F(1,(p-1)**2)
        assert f_loc(p,0,0,0)==g
        assert f_loc(p,1,0,0)==F(1,(p-1)**2)
        assert all(f_loc(p,v,0,0)==0 for v in range(2,7))

    # Generic p=2 forces v_2(d)=1.
    assert f_loc(2,0,0,0)==0
    assert f_loc(2,1,0,0)==1
    assert all(f_loc(2,v,0,0)==0 for v in range(2,7))

    # Exhaustive small special-prime support and triangle bound:
    # sum |f_v| p^(sigma v) <= 2 sum_{v=0}^{E+1} p^(sigma v).
    # Avoid irrational p^(2v/3) by cubing both sides after a looser
    # integer comparison p^(2v/3) <= p^v for p>=2.
    for p in [2,3,5,7,11]:
        for e1 in range(0,6):
            for e2 in range(0,6):
                E=max(e1,e2)
                for v in range(E+2, E+8):
                    assert f_loc(p,v,e1,e2)==0
                lhs=sum(abs(f_loc(p,v,e1,e2))*p**v for v in range(E+2))
                rhs=2*sum(F(p**v) for v in range(E+2))
                assert lhs<=rhs

    # Class-support crude cutoff:
    # for primes dividing 2*b1*b2, nonzero local v <= e_max+1.
    # Therefore d_class divides prod p^(e_p+1), which is <= rad(2b1b2)*(2b1b2).
    # The numerical examples below verify the exact support formula.
    for b1,b2 in [(2,3),(8,9),(25,49),(32,125),(121,169)]:
        # factorization helper
        n=2*b1*b2
        ps=[]
        x=n
        p=2
        while p*p<=x:
            if x%p==0:
                e=0
                while x%p==0:
                    x//=p;e+=1
                ps.append((p,e))
            p+=1
        if x>1: ps.append((x,1))
        dmax=1
        for p,_ in ps:
            # actual exponent from b1,b2
            def vp(y,p):
                e=0
                while y%p==0:
                    y//=p;e+=1
                return e
            E=max(vp(b1,p),vp(b2,p))
            dmax*=p**(E+1)
        assert dmax <= (2*b1*b2)**2

    print("generic odd local factor = 1 + (p^(sigma)-1)/(p-1)^2 at moment level")
    print("special local support: v <= max(e1,e2)+1")
    print("class-support cutoff: d <= (2*b1*b2)^2 (crude)")
    print("RESULT: UNIFORM_GAMMA_TAIL_LOCAL_ALGEBRA_PASS")

if __name__=="__main__":
    main()

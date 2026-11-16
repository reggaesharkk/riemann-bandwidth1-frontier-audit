#!/usr/bin/env python3
"""Exact rational Gram + numerical Fejer factor gate for conditioned p3."""
import sympy as sp
import numpy as np

def main():
    I=sp.I

    a0=sp.Rational(3379,2000)
    c1=sp.Rational(2101,20000)+sp.Rational(284,250)*I
    c2=-sp.Rational(789,2500)+sp.Rational(1653,10000)*I
    c3=-sp.Rational(61,800)-sp.Rational(439,20000)*I

    G=sp.Matrix([
      [sp.Rational(33,100),
       sp.Rational(7,500)+sp.Rational(509,1000)*I,
       -sp.Rational(229,1000)+sp.Rational(91,1000)*I,
       -sp.Rational(61,800)-sp.Rational(439,20000)*I],

      [sp.Rational(7,500)-sp.Rational(509,1000)*I,
       sp.Rational(859,1000),
       sp.Rational(41,500)+sp.Rational(239,500)*I,
       -sp.Rational(433,5000)+sp.Rational(743,10000)*I],

      [-sp.Rational(229,1000)-sp.Rational(91,1000)*I,
       sp.Rational(41,500)-sp.Rational(239,500)*I,
       sp.Rational(421,1000),
       sp.Rational(181,20000)+sp.Rational(149,1000)*I],

      [-sp.Rational(61,800)+sp.Rational(439,20000)*I,
       -sp.Rational(433,5000)-sp.Rational(743,10000)*I,
       sp.Rational(181,20000)-sp.Rational(149,1000)*I,
       sp.Rational(159,2000)]
    ])

    assert sp.simplify(sum(G[i,i] for i in range(4))-a0)==0
    assert sp.simplify(sum(G[i,i+1] for i in range(3))-c1)==0
    assert sp.simplify(sum(G[i,i+2] for i in range(2))-c2)==0
    assert sp.simplify(G[0,3]-c3)==0

    minors=[sp.factor(G[:k,:k].det()) for k in range(1,5)]
    expected=[
      sp.Rational(33,100),
      sp.Rational(24193,1000000),
      sp.Rational(127207,1000000000),
      sp.Rational(36360049,400000000000000)
    ]
    assert minors==expected
    assert all(m>0 for m in minors)

    # Numerical Fejer factor from the inside-unit-disk roots.
    coeff_pos={1:complex(c1),2:complex(c2),3:complex(c3)}
    poly=[]
    for exponent in range(6,-1,-1):
        k=exponent-3
        if k==0:
            z=complex(a0)
        elif k>0:
            z=coeff_pos[k]
        else:
            z=np.conj(coeff_pos[-k])
        poly.append(z)

    roots=np.roots(poly)
    inside=[z for z in roots if abs(z)<1]
    assert len(inside)==3

    prod=np.prod(inside)
    q3sq=(-coeff_pos[3]/np.conj(prod)).real
    assert q3sq>0
    q3=np.sqrt(q3sq)
    desc=q3*np.poly(inside)
    q=np.array([desc[-1],desc[-2],desc[-3],desc[-4]])

    recon=[sum(abs(z)**2 for z in q)]
    for k in range(1,4):
        recon.append(sum(np.conj(q[j])*q[j+k] for j in range(4-k)))

    assert abs(recon[0]-float(a0))<2e-12
    for k in range(1,4):
        assert abs(recon[k]-coeff_pos[k])<2e-12

    print("leading principal minors:")
    for m in minors:
        print(" ",m)
    print("Fejer factor q0..q3:")
    for z in q:
        print(" ",repr(complex(z)))
    print("RESULT: WP84_DEGREE3_POSITIVE_RANK6_GRAM_PASS")

if __name__=="__main__":
    main()

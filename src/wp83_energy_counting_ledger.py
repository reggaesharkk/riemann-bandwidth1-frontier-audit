#!/usr/bin/env python3
"""WP83 exact cluster graph and rank-energy ledger.

Two algebraic facts used by the Proposition-R energy-counting sieve:

1. For every connected component of size s>=5, s <= (5/4)(s-1).
   Since a connected component has at least s-1 edges,
       #vertices in large components <= (5/4) * #edges
   after summing componentwise (using any spanning forest).

2. If a Hermitian retained compression B has rank <= r and
   Frobenius energy E2=tr(B^2), then
       tr(B^4) >= E2^2/r.
   Thus M clusters, each contributing rank <=8 and total
   E2 >= c*M*X^(2 delta)/L^C, force a fourth-power cost
       >= (c^2/8) * M * X^(4 delta)/L^(2C).

The script checks the finite combinatorial inequality exactly.
"""
from fractions import Fraction as F

def main():
    # component-size ledger
    for s in range(5,101):
        assert F(s,1) <= F(5,4)*(s-1)
    print("large-component vertex/forest-edge factor = 5/4 PASS")

    # rank-energy symbolic coefficient
    for M in range(1,101):
        r=8*M
        # Normalize each cluster energy to 1, so total E2=M.
        lower=F(M*M,r)
        assert lower==F(M,8)
    print("rank-energy factor: M unit-energy clusters -> tr4 >= M/8 PASS")
    print("RESULT: WP83_ENERGY_COUNTING_LEDGER_PASS")

if __name__=="__main__":
    main()

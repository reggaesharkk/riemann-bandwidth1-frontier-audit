#!/usr/bin/env python3
"""Prime-base grouping algebra gate for WP84.

Checks the exact valuation selection rules for bounded exponent ranges.
The proof is unique factorization; enumeration is only a regression guard.
"""
from itertools import product

def first_order_solutions(a_max=8, q_exp_max=8):
    # Model the p-adic coordinate only.  Previous prime-base groups have
    # p-adic exponent exactly zero, so closure would require +/-a=0.
    out=[]
    for a in range(1,a_max+1):
        for s in (-1,1):
            if s*a==0:
                out.append((a,s))
    return out

def second_order_solutions(a_max=12):
    same=[]
    mixed=[]
    for a,b in product(range(1,a_max+1),repeat=2):
        for s1,s2 in product((-1,1),repeat=2):
            v=s1*a+s2*b
            if v==0:
                if s1==s2:
                    same.append((a,b,s1,s2))
                else:
                    mixed.append((a,b,s1,s2))
    return same,mixed

def main():
    assert first_order_solutions()==[]

    same,mixed=second_order_solutions()
    assert same==[]
    assert mixed
    assert all(a==b and s1==-s2 for a,b,s1,s2 in mixed)

    print("first-order exact current-base closures: 0")
    print("same-sign second-order exact current-base closures: 0")
    print("mixed closures:",len(mixed),
          "(all equal-power opposite-sign)")
    print("RESULT: WP84_PRIME_BASE_GROUPING_GATE_PASS")

if __name__=="__main__":
    main()

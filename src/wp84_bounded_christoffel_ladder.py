#!/usr/bin/env python3
"""WP84 bounded Christoffel consumer ladder.

For
    F_delta(x)=(delta+1) g(x)/(g(x)+delta),
    g=P(x)^2,
the exact simple-zero ledger floor is

    S(delta)
      = 1 - 2(1+1/delta) * 1415/13891
      = 11061/13891 - 2830/(13891 delta).

This approaches 11061/13891 monotonically from below.
"""
from fractions import Fraction as F

w0=F(1415,13891)
limit=F(11061,13891)

def simple_floor(delta:int):
    return F(1)-F(2)*(F(delta+1,delta))*w0

def main():
    assert simple_floor(61)==F(671891,847351)
    assert limit-simple_floor(61)==F(2830,13891*61)

    ladder=[
        (161,F(795,1000)),
        (752,F(796,1000)),
        (2871,F(7962,10000)),
        (9717,F(79625,100000)),
        (18577,F(79626,100000)),
        (1000000,F(0)), # display only
    ]
    for d,target in ladder:
        s=simple_floor(d)
        if target:
            assert s>target,(d,s,target)
        print(d,s,float(s),100*float(s))

    assert all(simple_floor(d+1)>simple_floor(d) for d in range(61,500))
    print("limit",limit,float(limit),100*float(limit))
    print("RESULT: WP84_BOUNDED_CHRISTOFFEL_LADDER_PASS")

if __name__=="__main__":
    main()

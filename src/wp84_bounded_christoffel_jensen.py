#!/usr/bin/env python3
"""Exact Jensen ledger for the bounded Christoffel family."""
from fractions import Fraction as F

w=F(1415,13891)
frontier=F(11061,13891)

def cap(delta):
    d=F(delta)
    return (d+1)*w/(d+w)

def simple(delta):
    return 1-2*cap(delta)

def main():
    assert w<1
    for d in (61,752,2871,9717,18577):
        s=simple(d)
        print(d,s,float(s),100*float(s))
        assert s<frontier
    assert all(simple(d+1)>simple(d) for d in range(1,1000))
    print("bounded optimum/frontier =",frontier,float(frontier),100*float(frontier))
    print("RESULT: WP84_BOUNDED_CHRISTOFFEL_JENSEN_PASS")

if __name__=="__main__":
    main()

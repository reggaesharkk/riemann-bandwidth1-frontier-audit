#!/usr/bin/env python3
"""Exact certificate for the preferred a=1 r2 record rung."""
from fractions import Fraction as F

Q = F(
    2575059657047327248,
    2914998924731524849,
)
SIMPLE = 2*Q-1

PUBLIC = F(
    722547711262091300265625000000000,
    1072825050442925667061714615173641,
)
RETUNED_HEADLINE = F(6735000520898147,10**16)

def main():
    qpub=(1+PUBLIC)/2
    qret=(1+RETUNED_HEADLINE)/2

    assert SIMPLE == F(
        2235120389363129647,
        2914998924731524849,
    )
    assert SIMPLE > PUBLIC
    assert SIMPLE > RETUNED_HEADLINE
    assert Q > qpub
    assert Q > qret

    print("q exact =",Q)
    print("q decimal =",float(Q))
    print("simple exact =",SIMPLE)
    print("simple decimal =",float(SIMPLE))
    print("public q threshold =",float(qpub))
    print("margin over public q threshold =",float(Q-qpub))
    print("retuned q threshold =",float(qret))
    print("margin over retuned q threshold =",float(Q-qret))
    print("RESULT: WP84_R2_A1_RECORD_RUNG_PASS")

if __name__=="__main__":
    main()

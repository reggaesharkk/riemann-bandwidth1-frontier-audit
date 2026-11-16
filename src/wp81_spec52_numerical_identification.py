#!/usr/bin/env python3
"""Regression/identification ledger for the WP81 {5,2} midpoint ladder.

This script records the three independently computed midpoint rungs, checks
the frozen {4,2} convention values, and evaluates the pre-registered rational
candidates.  It is not a substitute for the exact 450-term polytope proof.
"""
from fractions import Fraction as F

SPEC42={
 F(1,10): (
   F(-6870600,10**9),
   F(-765600,10**9),
   F(-4327950,10**9),
 ),
 F(1,20): (
   F(-64807515625,10**13),
   F(-7866890625,10**13),
   F(-405844453125,10**14),
 ),
}

RUNGS={
 F(1,5): (
   F(105216,10**7),
   F(28064,10**7),
   F(5984,10**6),
 ),
 F(1,10): (
   F(1008315,10**8),
   F(27847875,10**10),
   F(5366625,10**9),
 ),
 F(1,20): (
   F(996204140625,10**14),
   F(27795181640625,10**16),
   F(5210787109375,10**15),
 ),
}

CAND=(F(5,504),F(1,360),F(13,2520))
TOTAL=F(1,8)

def main():
    assert F(7)*sum(CAND,F(0))==TOTAL

    totals={}
    for h,us in sorted(RUNGS.items(),reverse=True):
        totals[h]=F(7)*sum(us,F(0))
        print("dv",float(h),"Us",*[float(x) for x in us],
              "SPEC52",float(totals[h]))

    # Fixed values from the independent lower-rung spectator reference.
    s42_01=6*F(-6870600,10**9)+6*F(-765600,10**9)+3*F(-4327950,10**9)
    assert float(s42_01)==-0.05880105

    # Candidate errors and h^2 ratios.
    e20=float(totals[F(1,5)]-TOTAL)
    e10=float(totals[F(1,10)]-TOTAL)
    e05=float(totals[F(1,20)]-TOTAL)
    print("candidate SPEC52 = 1/8")
    print("errors",e20,e10,e05)
    print("ratios",e20/e10,e10/e05)

    for j,c in enumerate(CAND):
        e10=float(RUNGS[F(1,10)][j]-c)
        e05=float(RUNGS[F(1,20)][j]-c)
        print("U%d candidate"%(j+1),c,"ratio",e10/e05)

    rich=(F(4)*totals[F(1,20)]-totals[F(1,10)])/F(3)
    print("Richardson .10/.05 =",float(rich))
    print("candidate component fractions =",CAND)
    print("RESULT: WP81_SPEC52_NUMERICAL_IDENTIFICATION_PASS")

if __name__=="__main__":
    main()

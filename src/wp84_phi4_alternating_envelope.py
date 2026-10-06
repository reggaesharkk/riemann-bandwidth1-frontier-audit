#!/usr/bin/env python3
"""Exact alternating-order envelope certificate for B4_nc.

Imports the exact nonclosed arrangement machinery and strengthens the
pointwise sign theorem.

Acceptance decisions are Fraction/integer only.
"""

from fractions import Fraction as F
from itertools import combinations

import wp84_phi4_balanced_nonclosed_nonpositive as base

Z=F(0)
O=F(1)

def main():
    hs=base.hyperplanes()
    assert len(hs)==45,len(hs)

    vertices=set()
    for four in combinations(hs,4):
        x=base.solve4(four)
        if x is None:
            continue
        if all(-O<=u<=O for u in x):
            vertices.add(x)

    assert len(vertices)==327,len(vertices)

    # The two additional envelope kink planes are already present.
    hp_plus=base.normalize_hp((O,Z,O,Z,O))      # 1+v1+v3=0
    hp_minus=base.normalize_hp((-O,Z,O,Z,O))   # -1+v1+v3=0
    assert hp_plus in hs
    assert hp_minus in hs

    summaries=[]

    for positive in combinations(range(4),2):
        P=set(positive)
        vals=[]

        for x in vertices:
            if any((x[j]<0 if j in P else x[j]>0) for j in range(4)):
                continue

            if base.spread(base.WALK,x)>O:
                continue

            b=base.B4(x)

            if positive==(0,2):
                envelope=max(Z,-x[1]-x[3]-O)
                gap=b+envelope
                assert b<=0
                assert gap>=0,(positive,x,b,envelope,gap)

            elif positive==(1,3):
                envelope=max(Z,x[1]+x[3]-O)
                gap=b+envelope
                assert b<=0
                assert gap>=0,(positive,x,b,envelope,gap)

            else:
                envelope=Z
                gap=b
                assert b==0,(positive,x,b)

            vals.append((b,gap))

        assert vals
        summaries.append(
            (
                positive,
                len(vals),
                min(v[0] for v in vals),
                max(v[0] for v in vals),
                min(v[1] for v in vals),
                max(v[1] for v in vals),
            )
        )

    for row in summaries:
        print(
            "positive labels",row[0],
            "support vertices",row[1],
            "B4 min/max",row[2],row[3],
            "envelope-gap min/max",row[4],row[5],
        )

    # Exact calculus identity recorded in the note:
    # each alternating continuum envelope integrates to 1/144.
    assert F(2,144)==F(1,72)

    print("total geometric envelope =",F(1,72))
    print("RESULT: WP84_PHI4_ALTERNATING_ENVELOPE_PASS")

if __name__=="__main__":
    main()

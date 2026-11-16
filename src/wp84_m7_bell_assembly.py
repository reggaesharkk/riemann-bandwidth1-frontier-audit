#!/usr/bin/env python3
"""Exact Bell(7) assembly identity for the model seventh moment.

Using the already-established frozen-singleton rule and vanishing of classes
containing a 3-block, Bell(7) reduces to known lower-order classes plus only
two genuinely new no-singleton pieces: {5,2} and {7}=C7.

The exact identity is

    m7 = 1717/90 + {5,2} + C7.

No value for {5,2} or C7 is assumed here.
"""
from fractions import Fraction as F
from collections import Counter

def parts(items):
    if not items:
        yield []
        return
    first,rest=items[0],items[1:]
    for p in parts(rest):
        for i in range(len(p)):
            yield p[:i]+[[first]+p[i]]+p[i+1:]
        yield [[first]]+p

def sig(p):
    return tuple(sorted((len(b) for b in p),reverse=True))

def crossing(a,b):
    a1,a2=sorted(a); b1,b2=sorted(b)
    return (a1<b1<a2<b2) or (b1<a1<b2<a2)

def main():
    P=list(parts(list(range(7))))
    C=Counter(sig(p) for p in P)
    assert len(P)==877

    expected={
      (1,1,1,1,1,1,1):1,
      (2,1,1,1,1,1):21,
      (2,2,1,1,1):105,
      (2,2,2,1):105,
      (3,1,1,1,1):35,
      (3,2,1,1):210,
      (3,2,2):105,
      (3,3,1):70,
      (4,1,1,1):35,
      (4,2,1):105,
      (4,3):35,
      (5,1,1):21,
      (5,2):21,
      (6,1):7,
      (7,):1,
    }
    assert C==expected,(C,expected)

    # Chord split inside {2,2,1,1,1}: for every chosen 4-set there
    # are two noncrossing and one crossing matching.
    adj=opp=0
    for p in P:
        if sig(p)!=(2,2,1,1,1):
            continue
        pairs=[b for b in p if len(b)==2]
        if crossing(pairs[0],pairs[1]): opp+=1
        else: adj+=1
    assert (adj,opp)==(70,35)

    ta=F(7,60)
    to=F(1,30)
    phi4=F(-1,60)
    t222=F(131,420)
    c5=F(1,36)
    c42=F(-23,420)
    c6=F(-1,126)

    # Frozen-singleton assembly:
    # 1^7; 2,1^5; 2^2,1^3; 4,1^3;
    # seven copies of the no-singleton 6-cycle {2,2,2}, {4,2}, {6};
    # 21 frozen copies of C5.
    base=(
        F(1)
        +F(21,3)
        +F(70)*ta+F(35)*to
        +F(35)*phi4
        +F(7)*t222
        +F(7)*c42
        +F(21)*c5
        +F(7)*c6
    )
    assert base==F(1717,90)

    # Same identity seen via centered raw moments:
    # m7 - 1717/90 is exactly the genuinely new seventh-order sector.
    print("Bell(7) =",len(P))
    print("{2,2,1,1,1} chord split =",adj,opp)
    print("known frozen/lower-order base =",base,"=",float(base))
    print("m7 = 1717/90 + SPEC52 + C7")
    print("If C7=-17/360 then m7 =",
          base-F(17,360),"+ SPEC52 =",
          F(6851,360),"+ SPEC52")
    print("RESULT: WP84_M7_BELL_ASSEMBLY_PASS")

if __name__=="__main__":
    main()

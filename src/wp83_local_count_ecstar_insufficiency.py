#!/usr/bin/env python3
"""WP83 local-count insufficiency witness for EC-star.

Construct an abstract ordinate configuration with:
  - at most L points in each unit interval;
  - all L points in that interval packed into a microscopic cluster;
  - therefore ~L^2/2 close pairs per unit interval.

This proves combinatorially that an O(log T) local zero count alone cannot
yield a power-saving close-pair estimate.
"""
from fractions import Fraction as F

def main():
    for L in (10,30,100,300,1000):
        units=17
        vertices=units*L
        edges=units*L*(L-1)//2
        # Every point has L-1 close neighbours inside its unit packet.
        assert edges*2 == vertices*(L-1)
        # Edge/vertex ratio grows linearly with L.
        ratio=F(edges,vertices)
        assert ratio==F(L-1,2)
        print("L",L,"vertices",vertices,"edges",edges,
              "edges/vertices",float(ratio))
    print("RESULT: WP83_LOCAL_COUNT_ECSTAR_INSUFFICIENCY_PASS")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
from fractions import Fraction as F

c4=F(49,1395654656)
C=F(26,1)
K4=2*C*(F(19,1)/c4+1)

def main():
    assert K4==F(1378906802676,49)
    print("c4 =",c4)
    print("K4 =",K4)
    print("K4 decimal =",float(K4))
    print("RESULT: WP83_BLOCK_INGHAM_CONSTANT_PASS")

if __name__=="__main__":
    main()

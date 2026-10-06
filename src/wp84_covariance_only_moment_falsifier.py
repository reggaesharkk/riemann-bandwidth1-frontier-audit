#!/usr/bin/env python3
"""WP84 exact moment falsifier for the covariance-only multiplication closure."""
from fractions import Fraction as F

# Target/model raw moments currently used by the conditional six-moment consumer.
target={
    0:F(1), 1:F(1), 2:F(4,3), 3:F(2),
    4:F(13,4), 5:F(101,18), 6:F(12809,1260),
}

# In the sharp covariance-only multiplication model:
# centered variance = int_0^1 K1(x) dx = 1/3,
# centered fourth moment = 2*int_0^1 K1(x)^2 dx = 7/30,
# odd centered moments vanish for the centered operator-valued semicircle.
c2=F(1,3)
c3=F(0)
c4=F(7,30)
c5=F(0)

def raw4():
    return F(1)+6*c2+4*c3+c4

def target_centered(k):
    import math
    s=F(0)
    for j in range(k+1):
        s += F(math.comb(k,j))*((-1)**(k-j))*target[j]
    return s

def main():
    assert raw4()==F(97,30)
    assert target[2]==F(4,3)
    assert target[3]==F(2)
    assert target[4]-raw4()==F(1,60)
    assert target_centered(4)==F(1,4)
    assert target_centered(4)-c4==F(1,60)
    assert target_centered(5)==F(1,36)
    assert c5==0

    print("covariance-only raw m4 =",raw4())
    print("target/model raw m4 =",target[4])
    print("m4 deficit =",target[4]-raw4())
    print("covariance-only centered m5 =",c5)
    print("target/model centered m5 =",target_centered(5))
    print("RESULT: WP84_COVARIANCE_ONLY_MOMENT_FALSIFIER_PASS")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""WP83 shell-sum algebra for far-field decoupling.

If each unit ordinate shell contains at most A*logT zeros and a cross-kernel
is bounded by C/Delta^2, then

  sum_{|Delta|>=R} |K(Delta)|
    <= 2*A*logT*C * sum_{n>=floor(R)} 1/n^2
    <= 2*A*logT*C * (1/(R-1) + 1/(R-1)^2)

and the squared/Frobenius shell sum has the stronger R^-3 tail.

This is an exponent ledger only; A and C stay symbolic.
"""
from fractions import Fraction as F

def tail2(N):
    # elementary upper bound sum_{n>=N} n^-2 <= 1/N^2 + integral_N^inf x^-2 dx
    return F(1,N*N)+F(1,N)

def tail4(N):
    # sum n^-4 <= N^-4 + integral_N^inf x^-4 dx
    return F(1,N**4)+F(1,3*N**3)

def main():
    for N in (2,4,8,16,32,64,128):
        t2=tail2(N)
        t4=tail4(N)
        assert t2 <= F(2,N)
        assert t4 <= F(2,N**3)
        print(N,"tail2<=",t2,"tail4<=",t4)
    print("RESULT: WP83_FAR_FIELD_SHELL_LEDGER_PASS")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""WP84 exact integer ledger: simple zeros from a positive-index lower bound.

If
  nplus <= s1+s2+p
and
  s1+2*s2+2*p <= Nprime,
then
  2*nplus-Nprime <= s1.

This is the zero-side consumer needed by the bounded spectral route.
"""
def main():
    checked=0
    for s1 in range(15):
      for s2 in range(15):
        for p in range(15):
          base=s1+2*s2+2*p
          for slack in range(5):
            N=base+slack
            for nplus in range(s1+s2+p+1):
              assert 2*nplus-N <= s1
              checked+=1
    print("states checked =",checked)
    print("RESULT: WP84_SIMPLE_FROM_POSINDEX_LEDGER_PASS")

if __name__=="__main__":
    main()

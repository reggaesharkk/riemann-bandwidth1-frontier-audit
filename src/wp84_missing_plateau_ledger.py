#!/usr/bin/env python3
"""WP84 exact missing-plateau ledger.

The covariance-only sharp closure predicts centered mu4=7/30.
The target/model centered fourth moment is 1/4.

The public sine-model bookkeeping has
  pairings = 4/15,
  plateau  = +1/60,
  R_model  = -1/30.

Thus
  covariance-only = pairings + R_model = 7/30,
  target          = pairings + plateau + R_model = 1/4.

So the exact covariance-only deficit is precisely the +1/60 plateau term.
This is an exact ledger identity, not yet an operator derivation.
"""
from fractions import Fraction as F

def main():
    pairings=F(4,15)
    plateau=F(1,60)
    R_model=-F(1,30)

    mu4_cov=F(7,30)
    mu4_target=F(1,4)

    assert pairings + R_model == mu4_cov
    assert pairings + plateau + R_model == mu4_target
    assert mu4_target-mu4_cov == plateau

    raw_cov=F(1)+F(2)+mu4_cov
    raw_target=F(1)+F(2)+mu4_target
    assert raw_cov==F(97,30)
    assert raw_target==F(13,4)
    assert raw_target-raw_cov==plateau

    print("pairings =",pairings)
    print("R_model =",R_model)
    print("plateau =",plateau)
    print("centered covariance-only m4 =",mu4_cov)
    print("centered target m4 =",mu4_target)
    print("raw covariance-only m4 =",raw_cov)
    print("raw target m4 =",raw_target)
    print("RESULT: WP84_MISSING_PLATEAU_LEDGER_PASS")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""WP84 order-four same-sign prime resonance gate.

Current block is the prime p (exponent 1), inserted twice with the same shift
sign.  At theta^4 there are exactly two previous block occurrences.

Trace closure requires exponent balance at every prime.  If the previous
occurrences are p^b and p^c, with b,c>=2 because the current p block is not in
the previous subset, the resonance equation is

    2 + eps1*b + eps2*c = 0, eps1,eps2 in {+1,-1}.

Every solution has |b-c|=2 and b+c>=6.  Thus it necessarily uses proper prime
powers and its absolute block weight is O(log(p)^4/(L^4 p^4)).

If previous blocks use any other prime base, unique factorization forces that
base to cancel separately; with only two previous occurrences this cannot
repair the p-exponent without the same proper-power pattern.
"""
from itertools import product

def resonances(B=20):
    out=[]
    for b in range(2,B+1):
        for c in range(2,B+1):
            for e1,e2 in product((-1,1),repeat=2):
                if 2+e1*b+e2*c==0:
                    out.append((b,c,e1,e2))
    return out

def main():
    rr=resonances(30)
    assert rr
    for b,c,e1,e2 in rr:
        assert abs(b-c)==2
        assert b+c>=6
        assert b>=2 and c>=2

    # No resonance if the two prior p-exponents are both absent.
    # Minimal p-decay:
    # current B_p^2 contributes p^-1,
    # prior B_{p^b} B_{p^c} contributes p^{-(b+c)/2} <= p^-3.
    min_total_decay=min(1+(b+c)/2 for b,c,_,_ in rr)
    assert min_total_decay==4

    print("first resonances:",rr[:12])
    print("minimum total p-decay exponent =",min_total_decay)
    print("RESULT: WP84_ORDER4_VSUM_PRIME_RESONANCE_PASS")

if __name__=="__main__":
    main()

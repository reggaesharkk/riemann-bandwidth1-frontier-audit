#!/usr/bin/env python3
"""WP84 exact order-4 Lindeberg word ledger.

Purpose
-------
Audit what the *quadratic per-block* resolvent update can still carry at
global order four.  The update is represented as a formal noncommutative
polynomial

    R -> R - R B R + R B R B R,

truncated only by total word degree for this finite algebra check.

Results
-------
1. With two block labels A,B, every word containing A twice and B twice
   occurs with coefficient +1.  Under cyclic trace equivalence these six
   words split into:
       four adjacent/nested words,
       two alternating/crossing words.
   Therefore the exact geometry is weighted in the ratio 2:1, giving
       2*t_adj + t_opp.

2. With four distinct block labels A,B,C,D, all 4! words occur with
   coefficient +1.  Hence killing single-block cubic remainders does NOT
   remove the global four-distinct word sector.  It survives through repeated
   first-order history.

3. Exact sharp overlap integrals give
       t_adj = 7/60,
       t_opp = 1/30,
   so the complete pair layer is 4/15.

The pinned centered fourth moment is 1/4.  The frozen connected-core constant
Phi4=-1/60 supplies
       4/15 - 1/60 = 1/4.

This checker does not prove the arithmetic connected-core limit.  It identifies
the exact sector the theorem must preserve.
"""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import permutations

MAXDEG=4

def addp(*ps):
    out=defaultdict(F)
    for p in ps:
        for w,c in p.items():
            out[w]+=c
    return {w:c for w,c in out.items() if c}

def scal(c,p):
    return {w:c*v for w,v in p.items() if c*v}

def mulp(p,q):
    out=defaultdict(F)
    for w,c in p.items():
        for v,d in q.items():
            if len(w)+len(v)<=MAXDEG:
                out[w+v]+=c*d
    return {w:c for w,c in out.items() if c}

I={():F(1)}

def quadratic_update(R,label):
    B={(label,):F(1)}
    RBR=mulp(mulp(R,B),R)
    RBRBR=mulp(mulp(mulp(mulp(R,B),R),B),R)
    return addp(R,scal(F(-1),RBR),RBRBR)

def sequential(labels):
    R=I
    for lab in labels:
        R=quadratic_update(R,lab)
    return R

def cyclic_rep(word):
    rots=[word[k:]+word[:k] for k in range(len(word))]
    return min(rots)

def pair_word_gate():
    R=sequential(("A","B"))
    pair={
        w:c for w,c in R.items()
        if len(w)==4 and Counter(w)==Counter({"A":2,"B":2})
    }
    expected=set(permutations(("A","A","B","B")))
    assert set(pair)==expected
    assert set(pair.values())=={F(1)}

    cls=defaultdict(list)
    for w in pair:
        cls[cyclic_rep(w)].append(w)
    sizes=sorted(len(v) for v in cls.values())
    assert sizes==[2,4],sizes
    return cls

def distinct_word_gate():
    R=sequential(("A","B","C","D"))
    words={
        w:c for w,c in R.items()
        if len(w)==4 and len(set(w))==4
    }
    expected=set(permutations(("A","B","C","D")))
    assert set(words)==expected
    assert set(words.values())=={F(1)}
    return words

def exact_overlap_constants():
    # Adjacent walk [0,v,0,w,0].
    # Same-sign quadrant:
    #   2 * int_0^1 int_0^a (1-a) a b db da = 1/20.
    same_quad = F(1,20)

    # Opposite-sign quadrant:
    #   int_0^1 int_0^(1-a) (1-a-b) a b db da = 1/120.
    opposite_quad = F(1,120)

    t_adj=2*same_quad+2*opposite_quad

    # Crossing walk [0,v,v+w,w,0] has spread |v|+|w|;
    # all four sign quadrants are the same triangle.
    t_opp=4*opposite_quad

    assert t_adj==F(7,60)
    assert t_opp==F(1,30)
    return t_adj,t_opp

def main():
    cls=pair_word_gate()
    distinct=distinct_word_gate()
    t_adj,t_opp=exact_overlap_constants()

    pair_layer=2*t_adj+t_opp
    phi4=-F(1,60)
    target=pair_layer+phi4
    scalar_cov=2*t_adj

    assert pair_layer==F(4,15)
    assert target==F(1,4)
    assert scalar_cov==F(7,30)
    assert target-scalar_cov==F(1,60)

    print("pair cyclic classes:")
    for rep,words in sorted(cls.items()):
        print(" ", "".join(rep), "size",len(words),
              ["".join(w) for w in sorted(words)])
    print("all-distinct words retained =",len(distinct))
    print("t_adj =",t_adj)
    print("t_opp =",t_opp)
    print("pair layer =",pair_layer)
    print("connected Phi4 =",phi4)
    print("centered m4 target =",target)
    print("scalar covariance =",scalar_cov)
    print("net scalar defect =",target-scalar_cov)
    print("RESULT: WP84_LINDEBERG_M4_WORD_LEDGER_PASS")

if __name__=="__main__":
    main()

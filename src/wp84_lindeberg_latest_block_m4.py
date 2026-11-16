#!/usr/bin/env python3
"""WP84 exact latest-block classification at order four.

For a fixed permutation of block labels, expand the quadratic one-block
resolvent update around a scalar background.  At theta^4, every word is
classified by the multiplicity of the *latest inserted label* appearing in
that word:

    latest multiplicity 1 -> first-order Lindeberg term A1,
    latest multiplicity 2 -> second-order Lindeberg term A2,
    latest multiplicity >=3 -> cubic remainder sector.

This is a purely combinatorial identity.  It explains exactly where the
order-four word classes live before any arithmetic estimate.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from fractions import Fraction as F

def latest_label(word,order):
    rank={lab:i for i,lab in enumerate(order)}
    return max(set(word), key=lambda x: rank[x])

def sector(word,order):
    lab=latest_label(word,order)
    mult=word.count(lab)
    return "A1" if mult==1 else ("A2" if mult==2 else "R3+")

def pattern(word):
    return tuple(sorted(Counter(word).values(),reverse=True))

def all_words_for_labels(labels):
    return list(product(labels,repeat=4))

def exact_pattern_fractions(labels):
    orders=list(permutations(labels))
    totals=defaultdict(lambda:defaultdict(int))
    for word in all_words_for_labels(labels):
        pat=pattern(word)
        # Only record words using every supplied label at least once, so the
        # permutation averaging is over the actual distinct labels in word.
        used=tuple(sorted(set(word)))
        if tuple(sorted(labels))!=used:
            continue
        for order in orders:
            totals[pat][sector(word,order)]+=1
    out={}
    for pat,d in totals.items():
        n=sum(d.values())
        out[pat]={k:F(v,n) for k,v in d.items()}
    return out

def pair_pair_gate():
    labels=("A","B")
    words=set(permutations(("A","A","B","B")))
    for order in permutations(labels):
        assert all(sector(w,order)=="A2" for w in words)
    return len(words)

def four_distinct_gate():
    labels=("A","B","C","D")
    words=set(permutations(labels))
    for order in permutations(labels):
        assert all(sector(w,order)=="A1" for w in words)
    return len(words)

def pattern_211_gate():
    # For any word with multiplicities 2,1,1, the latest distinct label is
    # the doubled label with probability 1/3 over permutations of the three
    # distinct labels, and a singleton with probability 2/3.
    labels=("A","B","C")
    orders=list(permutations(labels))
    words=set(permutations(("A","A","B","C")))
    counts=Counter()
    for w in words:
        for order in orders:
            counts[sector(w,order)]+=1
    n=sum(counts.values())
    frac={k:F(v,n) for k,v in counts.items()}
    assert frac=={"A1":F(2,3),"A2":F(1,3)},frac
    return frac

def pattern_31_gate():
    labels=("A","B")
    orders=list(permutations(labels))
    words=set(permutations(("A","A","A","B")))
    counts=Counter()
    for w in words:
        for order in orders:
            counts[sector(w,order)]+=1
    n=sum(counts.values())
    frac={k:F(v,n) for k,v in counts.items()}
    assert frac=={"A1":F(1,2),"R3+":F(1,2)},frac
    return frac

def main():
    pp=pair_pair_gate()
    fd=four_distinct_gate()
    f211=pattern_211_gate()
    f31=pattern_31_gate()

    print("2+2 words:",pp,"-> A2 with probability 1")
    print("1+1+1+1 words:",fd,"-> A1 with probability 1")
    print("2+1+1 permutation split:",f211)
    print("3+1 permutation split:",f31)
    print("4 sector -> R3+ with probability 1")
    print("RESULT: WP84_LATEST_BLOCK_M4_CLASSIFICATION_PASS")

if __name__=="__main__":
    main()

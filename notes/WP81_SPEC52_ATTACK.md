# WP81 — exact {5,2} attack

Date: 2026-10-04  
Status: **LAUNCHED; private/local/Colab first; no theorem claim**

## Why {5,2} now

The public k=8 outlook identifies the remaining analytic work as the mixed
`{5,2}` transport plus the m8 mixed classes.  After the exact post-79
consumer gate, the fastest useful next model-side object is therefore the
missing `{5,2}` joint constant.

This is deliberately separate from the Stage-A theorem bridge.  A model-side
exact fraction does not promote any zeta theorem without the arithmetic
transport.

## Exact specification

The public `{4,2}` spectator-pair specification uses a connected b-block
cumulant, a `C2(v)=min(|v|,1)` spectator pair, and the full-cycle overlap.

For `{5,2}`, use free variables

[
(v,c_1,c_2,c_3,c_4),qquad
c_5=-(c_1+c_2+c_3+c_4).
]

There are three cyclic-distance classes for the pair in a 7-cycle:

- d=1: ((+v,-v,c_1,c_2,c_3,c_4,c_5));
- d=2: ((+v,c_1,-v,c_2,c_3,c_4,c_5));
- d=3: ((+v,c_1,c_2,-v,c_3,c_4,c_5)).

Because 7 is odd, each distance class has multiplicity 7, exhausting all
(inom72=21) unordered pair placements.  Hence

[
oxed{
{5,2}=7(U_1+U_2+U_3).
}
]

Each (U_d) is a five-dimensional exact rational polytope integral of

[
O_7,C_5,C_2.
]

The connected (C_5) factor has 150 partition-cyclic terms, so the full
certificate has exactly 450 exact term integrals.

## Trust boundary

The driver imports only the exact-polytope engine from the pinned public
checkout

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

It refuses a different git HEAD unless `--allow-unpinned` is supplied
explicitly.  Production evidence must never use that override.

The first complete aggregate has **no hard-coded target**.  This prevents us
from tuning the computation toward a desired rational.

## Fastest compute plan

Do not spend private GitHub Actions minutes.

Use the laptop and/or free Colab as interchangeable workers.  Split each class
into term shards.  For example, 10-term shards:

```
python src/wp81_spec52_exact.py --upstream /path/to/zeta-0.7947-reproduction \
  --d 1 --terms 0:10 --out work/spec52_d1_000_010.txt
```

Run different non-overlapping shards on laptop and Colab.  Every term is an
independent exact Fraction computation.

After all 450 terms are present:

```
python src/wp81_spec52_aggregate.py work/spec52_*.txt \
  --json-out work/wp81_spec52_exact_certificate.json
```

The aggregator fails closed on a missing or duplicate term.

## Promotion rule

A completed exact `{5,2}` fraction is **model-side exact evidence only**.
Next steps are:

1. independent replay of the aggregate;
2. insert it into an explicit m7 assembly ledger;
3. prove the corresponding arithmetic transport;
4. only then consume m7 in the exact k=8 Christoffel gate.

The repository remains private while this attack is active.  Public GitHub
Actions may be used later only by an explicit decision to trade secrecy for
speed; publication is not required for mathematical validity.

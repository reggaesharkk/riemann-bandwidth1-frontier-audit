# WP84 — exact delta-144 margin and arithmetic gate (2026-10-06)

Status: **EXACT MODEL THRESHOLD VERIFIED; ARITHMETIC RESOLVENT GATE OPEN**

This record audits the proposed first strict 79.5% rung against the live
bounded Christoffel family at PR #5 head
`d3ff55114f39d361cb1a2c4dd6b1335b8b4db064`.

## Exact consumer calculation

Set
```
w0 = 1415/13891,
g(x) = P(x)^2,
F_delta(x) = (delta+1) g(x)/(g(x)+delta),
h_delta(w) = (delta+1)w/(delta+w).
```

The existing support-free consumer argument gives, for every pinned-moment
model measure,
```
integral F_delta dnu <= h_delta(w0),
nu((-infinity,0]) <= integral F_delta dnu.
```
The corresponding simple-zero coefficient is
```
S_delta = 1 - 2 h_delta(w0).
```

For the strict target (S_delta>0.795=159/200), the exact real threshold is
```
delta > 507985/3531 = 143.864344...
```
so the first integer is (delta=144). At that rung,
```
h_144(w0) = 205175/2001719
          = 0.102499401764183684...,

S_144     = 1591369/2001719
          = 0.795001196471632632... .
```

A simple-zero coefficient above 79.5% requires the actual trace cap to be
strictly less than
```
(1 - 0.795)/2 = 41/400 = 0.1025.
```
The entire model-side headroom is therefore
```
41/400 - h_144(w0) = 479/800687600
                   = 5.98235816316...e-7.
```
This is the exact consumer margin, not an error estimate for the arithmetic
trace.

The exact rational regression is
`src/wp84_delta144_margin_gate.py`. It checks the threshold, first integer,
consumer value, score, and strict-target headroom using `Fraction` arithmetic.

## What the analytic theorem must still prove

The needed arithmetic statement is
```
limsup_{T->infinity} tau(F_144(H_T)) <= 205175/2001719.
```
The fixed-(delta) six-pole representation reduces this to one weighted
combination of normalized resolvents. The conditional zero-counting transfer
then gives (S_{144}>79.5\%).

A weaker target sufficient merely for (>79.5\%) is
```
limsup tau(F_144(H_T)) < 41/400.
```
That still requires a theorem for the actual arithmetic matrices. The
(5.98\times10^{-7}) difference above is not supplied by a variance estimate.

## Variance versus expectation

The repository's Gaussian frame/Poincare note proves concentration of the
normalized resolvent trace around its Gaussian-bridge expectation at its stated
fixed poles. That note explicitly leaves the deterministic expectation and
arithmetic drift open. Concentration alone cannot bound that expectation.
The bridge identity contains both the expected drift
`E tau(R_t P_full R_t)` and a covariance term; evaluating their integrated
contribution at the (F_{144}) poles remains part of the open arithmetic
gate.

Therefore the optional description of this as a closed “scalar variance loop”
is not established by the current files. No unconditional 79.5% theorem is
claimed.

## Reproduction

Run:
```
python src/wp84_delta144_margin_gate.py
```

Expected terminal marker:
```
RESULT: DELTA144_EXACT_MODEL_MARGIN_PASS
ARITHMETIC_GATE: OPEN
```

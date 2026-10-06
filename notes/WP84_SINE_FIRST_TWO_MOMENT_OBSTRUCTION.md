# WP84 — first-two-moment obstruction for the full-sharp sine variance route

Date: 2026-10-06

Status: **EXACT OBSTRUCTION — THE FIRST TWO SHARP MOMENTS ALONE CANNOT CLOSE THE 76.99% SINE-SQUARE VARIANCE GATE**

No unconditional zero-density percentage is claimed here.

At a=23/20 and t=113/100 the full-sharp sine-square route reduces the comparison crossing to

    Var_tau(S_a) < 0.1069812171909...,

where

    S_a(x)=2ax/(x^2+a^2).

The first two moments

    tau(H)=1+o(1),
    tau(H^2)=4/3+o(1)

are useful for the mean term, but they do not by themselves control the remaining variance strongly enough.

## 1. Universal two-moment positive-index ceiling

The probability measure

    nu_0=(1/4) delta_0 +(3/4) delta_{4/3}

has

    int x dnu_0=1,
    int x^2 dnu_0=4/3,

but only

    nu_0((0,infinity))=3/4.

Therefore no argument using only the first two raw moments can prove a universal positive-index lower bound above 3/4.

## 2. Exact counterexample to the variance gate

Take

    p=3/25,
    x_- = 1-sqrt(22)/3,
    x_+ = 1+sqrt(22)/22,

and

    nu_1=(3/25) delta_{x_-} +(22/25) delta_{x_+}.

Then exactly

    int x dnu_1=1,
    int x^2 dnu_1=4/3.

For a=23/20 and s(x)=2ax/(x^2+a^2),

    Var_{nu_1}(s)=0.3379014531555588... .

The companion exact checker proves

    Var_{nu_1}(s)>1/3,

whereas the required theorem ceiling is below 1/9.

Thus the current variance gate cannot follow from the first two moments alone.

## 3. Consequence

The mean/variance decomposition remains exact, but the final variance estimate must use additional operator/arithmetic structure. The active options are:

- the full-sharp rank-two displacement law;
- the two-vector resolvent wedge and scalar K2 decomposition;
- the Gaussian covariance / heat-flow representation;
- the separate fixed-band fourth-moment arithmetic route.

Do not spend further effort trying to derive the variance ceiling from mu1 and mu2 alone.

No unconditional record theorem is claimed.

See:

    notes/WP84_SINE_FULL_SHARP_RETUNED.md
    notes/WP84_SINE_SCALAR_K2_WEDGE.md
    notes/WP84_SINE_WEDGE_CANONICAL_FRAME.md

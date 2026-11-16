# WP84 — hostile-audit corrections: pole strip, endpoint dimension, and connected-state provenance

Date: 2026-10-05

Status: **THREE POTENTIAL OBJECTIONS RESOLVED; CONNECTED-STATE ARITHMETIC LIMIT STILL OPEN**

This note records only mathematical corrections and surviving theorem debt.

## 1. The delta=61 pole-strip claim is correct

For

    F_delta(x)
      = (delta+1) P(x)^2/(P(x)^2+delta),

the poles solve

    P(z)^2+delta=0.

At delta=61, direct high-precision roots are

    -0.713719271864919 +/- 1.076039256240280 i,
     1.301484231306875 +/- 2.152798294007430 i,
     3.315340630620156 +/- 1.076759037767149 i.

Therefore

    min |Im z_j|
      = 1.076039256240280... > 1.

The independent exact elimination/Sturm gate also proves that no pole at
delta=61 lies in |Im z|<=1.

The uniform-family proof then shows that for every delta>=61,

    boxed:
    |Im z_j(delta)|>1.

So no repair from delta>=61 to delta>=62 is needed.

## 2. Why DPSS is genuinely needed for the ramp endpoint

In the sharp coordinate model, a translation by at least L-W connects only
the two boundary strips of physical width W.

However, after compression to the d Fourier/Gabor modes, the restriction map

    T_I=M_I P_d

to a nonzero interval I has full algebraic rank d.

Therefore the exact physical support statement does **not** imply an exact
finite-dimensional rank bound 2W.

What is small is the **effective concentration dimension**, which is exactly
the DPSS/prolate problem.

Thus the prolate step is not optional for the actual finite Fourier
compression.

## 3. DPSS precision budget is asymptotically safe

The present matrix dimension satisfies

    d asymp T L/(2*pi).

Choose the endpoint strip width

    W=K log L

and DPSS bandwidth

    W_DPS=W/(2L).

Then the DPSS time-bandwidth product is

    d W_DPS
      asymp T W
      asymp T log L.

Hence

    log(d W_DPS)=O(log T)=O(L).

Choose concentration threshold

    epsilon=T^(-A)

with fixed A>2. Then

    log(1/epsilon)=A log T=O(L).

The published nonasymptotic DPSS transition-width bound therefore gives

    transition count
      = O(log(d W_DPS) log(1/epsilon))
      = O(L^2).

But

    d asymp T L,

so

    transition count / d
      = O(L/T)
      = o(1).

The Shannon part has rank fraction

    W/L
      = K log L/L
      = o(1).

Therefore the complete concentrated boundary subspace has rank fraction o(1)
even at the polynomially small epsilon needed to beat the crude
T^(1/2+o(1)) middle-operator norm.

This closes the precision/rank compatibility check.

## 4. The operator-norm cubic budget is already stronger than a rank-weighted budget

The exact one-block normalized-trace remainder satisfies

    |E_j(z)| <= ||B_j||^3 / |Im z|^4.

Therefore

    sum_j |E_j(z)|
      <= |Im z|^(-4) sum_j ||B_j||^3
      = O(L^-3).

No rank factor is needed.

A rank-weighted refinement could improve constants, but it is not necessary
for vanishing of the fixed-nonreal cubic remainder.

## 5. Vanishing single-block cubic remainder does not force a Gaussian fourth moment

The exact telescoping identity evaluates the first- and second-order
increments at the **exact evolving intermediate resolvent**.

Consequently the accumulated first/second-order history already contains
arbitrary global word degrees in previously inserted block labels.

At order four:

- all 2+2 words are visible in the second-order insertion sector;
- all four-distinct words are visible in the first-order history sector;
- 2+1+1 words are split between the two.

Thus a nonzero global connected fourth contribution is logically compatible
with a vanishing cubic remainder for each newly inserted block.

The implication

    sum ||B_j||^3=o(1)
      => centered m4 is pair/Wick determined

is false unless an additional independence/static-covariance closure is
proved.  That additional closure has already failed.

## 6. What remains open about Phi4

The known model calibration is

    pair layer
      = 2*t_adj+t_opp
      = 4/15,

    connected core
      = Phi4
      = -1/60,

    centered m4
      = 1/4.

The exact latest-block algebra proves that the full first/second-order
Lindeberg state has room to carry Phi4.

It does **not** yet prove that the arithmetic retained-range state converges
to the model connected value -1/60.

That is the genuine provenance theorem still required.

The next attack should therefore identify the permutation-averaged
finite-population state law explicitly rather than add third/fourth
single-block Taylor terms.

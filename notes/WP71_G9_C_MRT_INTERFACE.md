# WP71 G9-C — exact MRT interface audit

Date: 2026-10-04  
Status: **SOURCE INTERFACE PINNED; reduction from welding remainder still open**

Source independently checked:

K. Matomäki, M. Radziwiłł, T. Tao,
*Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges*, Proc. London Math. Soc. 118 (2019), 284--350,
DOI 10.1112/plms.12181.

## 1. Exact Proposition 5.4 hypotheses

MRT Proposition 5.4 is a Dirichlet-series mean-value estimate.

With

[
sigma=8/33,qquad
H=X^{sigma+arepsilon},qquad
Q=(log X)^B,
]

it assumes

[
1le qle Q,qquad q=q_0q_1,
]

and

[
oxed{
X^{-1/6-arepsilon}lelambdalerac1{qQ}.
}
]

The arithmetic function is either

[
f=Lambda,1_{(X,2X]}
]

or

[
f=d_k,1_{(X,2X]}.
]

The proposition gives the required log-power saving for a character-summed
Dirichlet-series mean value in the (t)-window associated with
(lambda H).

## 2. Exact Proposition 3.4 interface

The additive-frequency minor-arc statement that is ultimately used in the
correlation theorem is Proposition 3.4.

For (qle Q), ((a,q)=1), it supplies:

- a range down to additive frequency (X^{-1/6-arepsilon});
- and, in the long-shift regime (sigmage8/33), a localized bound around
  (eta) when

[
X^{-1/6-arepsilon}le |eta|lerac1{qQ}.
]

This is the clean additive-frequency interface against which the Stage-A
welding remainder should be matched.

## 3. Important citation correction

The public candidate sentence

> "... divisor-bounded envelopes of Proposition 5.4, Appendix A of MRT ..."

is too compressed and conflates two different pieces of the published paper.

- Proposition 5.4 is proved in the main argument, through the
  combinatorial/Dirichlet-polynomial work of Sections 6--7.
- Appendix A is explicitly the proof of Proposition 5.5, a different
  mean-value estimate.

Therefore **G9-C is not closed by citing "Prop. 5.4, App. A"**.

The final proof must say exactly which of Proposition 3.4, Proposition 5.4,
or Proposition 5.5 is being invoked at each step and verify its own
hypotheses.

## 4. Fail-closed substitution table for G9-C

Before any MRT estimate is consumed, the welding reduction must provide a
table with the following rows.

| MRT symbol | Stage-A object | Required check |
|---|---|---|
| (X) | dyadic prime scale of the relevant (m) or (n) block | support lies in one dyadic interval after partition |
| (H) | allowed shift-window length | (Hge X^{8/33+arepsilon}) and (Hle X^{1-arepsilon}) |
| (q) | structured modulus from (b_1,b_2) gcd reduction | (qle(log X)^B) after truncation |
| (q_0,q_1) | factorization used in character decomposition | explicitly stated and within the proposition's range |
| (lambda) | additive-frequency / smoothing scale | (X^{-1/6-arepsilon}lelambdale1/(qQ)) |
| (f) | prime block being transformed | exactly (Lambda 1_{(X,2X]}), or a stated dyadic decomposition into such blocks |
| weight | slow Stage-A geometry | removed by Abel/partial summation with a proved variation bound |

If one row is missing, G9-C remains open.

## 5. Current strategic consequence

There are two legitimate routes:

### Route C1 — use Proposition 3.4 directly

After dyadic partition and Abel summation, rewrite the welding remainder as a
weighted additive-frequency prime exponential-sum error and invoke the minor
arc estimate directly.

This is preferable if the Stage-A geometry naturally lives in additive
frequency.

### Route C2 — descend to Proposition 5.4

Perform the same Fourier transformations used by MRT and identify the exact
Dirichlet-series family and its ((q,q_0,q_1,lambda)) parameters.

This route is longer but exposes every analytic interface.

We should choose the shorter route only after the Stage-A weight is written
explicitly enough to verify the range inequalities.

## 6. Gate state

- G9-A exact welding reindexing: **CLOSED**.
- G9-B signed main factorization/Abel transport: **OPEN**.
- G9-C MRT analytic remainder reduction: **OPEN, source hypotheses now pinned**.
- G9-D conversion to exact (R)-units and (o(1)): **OPEN**.

No theorem percentage is promoted by this source audit.

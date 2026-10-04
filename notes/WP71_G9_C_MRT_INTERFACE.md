# WP71 G9-C — exact MRT interface and constant ledger

Date: 2026-10-04
Status: **SOURCE INTERFACE PINNED; notation corrected; two-modulus dilation audit is the next analytic gate**

Source:
K. Matomaki, M. Radziwill, T. Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. LMS 118 (2019), 284--350.

## 1. Do not identify the two q's

Stage A has a welding multiplier

    q_w=b2/gcd(b1,b2),

appearing in the physical shift h=q_w*k.

MRT has an arc denominator q_arc in alpha=a/q_arc+beta, with q_arc<=Q=(log X)^B.

They are unrelated. See `notes/WP71_WELDING_VS_ARC_MODULUS.md`.

G2 controls the structured h=q_w*k family through divisor-bounded multiplicity and does not require q_w to be polylogarithmic.

## 2. Proposition 5.4 source hypotheses

MRT Proposition 5.4 fixes sufficiently small epsilon>0, A>0, fixed k>=2, and B sufficiently large depending on k,A. It sets

    H = X^(sigma+epsilon),
    Q = (log X)^B,

with sigma>=8/33 for the long-shift application. It assumes

    1 <= q_arc <= Q,
    q_arc=q0*q1,

and

    X^(-1/6-epsilon) <= lambda <= 1/(q_arc*Q).

The arithmetic function is Lambda*1_(X,2X] or d_k*1_(X,2X]. The resulting mean-value estimate has arbitrary requested logarithmic saving, with an implied constant depending on k,epsilon,A,B.

## 3. Proposition 3.4 additive-frequency interface

For alpha=a/q_arc+beta, q_arc<=Q, Proposition 3.4 gives the minor-arc L2 estimate. In the localized long-shift form (sigma>=8/33), the center beta satisfies

    X^(-1/6-epsilon) <= |beta| <= 1/(q_arc*Q).

Part (i) handles the complementary larger-frequency region down to the major-arc boundary.

## 4. Exact dilation denominator reduction

For the Stage-A sums

    S_m(alpha)=sum Lambda(m)e(b2*m*alpha),
    S_n(alpha)=sum Lambda(n)e(b1*n*alpha),

write alpha=a/q_arc+beta with (a,q_arc)=1. Then the rational parts reduce exactly to denominators

    q_m = q_arc/gcd(q_arc,b2),
    q_n = q_arc/gcd(q_arc,b1).

Hence q_m,q_n<=q_arc<=Q. This is the arithmetic core of the claimed b-uniformity.

What is not automatic is the width: the residual frequencies are b2*beta and b1*beta modulo 1. The proof must classify when both are major and, outside that finite family, show that at least one dilated side satisfies the minor-arc estimate in its own approximation quality.

## 5. Lemma 2.2 exact maximal constant

MRT's maximal summation-by-parts inequality is

    |sum f(n)g(n)|*
      <= |sum g(n)|*
         * (sup|f| + interval_length*sup|f'|).

The displayed operator coefficient is exactly 1. Thus the Stage-A slow-weight cost is the explicit variation norm

    V(f)=sup|f|+length*sup|f'|.

## 6. Corollary 2.5 endpoint truncation

For f supported on [X/C,CX], Corollary 2.5 bounds every interval-truncated Dirichlet polynomial by an endpoint-independent integral of the untruncated polynomial plus a truncation error.

The kernel mass is exactly

    integral_{-T}^{T} du/(1+|u|)=2*log(1+T).

So maximalizing over endpoints introduces logarithmic losses, not a count of endpoint choices.

The corollary still carries an implicit C-dependent constant, and Proposition 5.4 carries further implicit constants. These are not numerical finite-height certification constants. The correct target is an exponent-level o(1), not a fabricated rational decimal bound.

## 7. Correct fail-closed substitution table

| object | Stage-A meaning | required check | status |
|---|---|---|---|
| X_m,X_n | dyadic scales of the prime variables after block partition | each support lies in a fixed-ratio dyadic interval | OPEN write-out |
| H_shift | long physical-shift averaging scale used before structured extraction | H_shift>=X^(8/33+epsilon) where MRT is consumed | OPEN |
| q_w | b2/g welding multiplier | handled only through divisor multiplicity | G2 DERIVED |
| q_arc | rational-approximation denominator for alpha | q_arc<=Q=(log X)^B | source condition |
| q_m,q_n | reduced denominators after dilation | exact q_arc/gcd(q_arc,b_i) | ALGEBRA CLOSED |
| beta/lambda | residual frequency scale | verify the Proposition 3.4/5.4 ranges after dilation | OPEN / HIGH PRIORITY |
| interval truncation | moving/block endpoints | Cor. 2.5 endpoint-independent maximalization | MECHANISM CLOSED |
| slow geometry | kernel/overlap amplitude | Lemma 2.2 variation bound | FORMULA CLOSED; Stage-A bound OPEN |

## 8. Citation map

- Lemma 2.2: maximal summation by parts.
- Corollary 2.5: arbitrary interval truncation.
- Proposition 3.4: additive-frequency minor-arc estimate.
- Proposition 5.4: Dirichlet-series mean-value estimate, proved through Sections 6--7.
- Proposition 5.5: complementary mean-value estimate, proved in Appendix A.

The shorthand 'Prop. 5.4, Appendix A' is incorrect.

## 9. Current analytic target

Because the n-first moving window is O(1), G9 no longer seeks pointwise control of w_k(n). The preferred route is the j-first centered four-point object in `WP71_G9_C_JFIRST_PIVOT.md`.

The MRT interface is therefore used inside a long averaged/spectral proof, where q_arc is a frequency denominator and q_w remains a structured physical shift.

No percentage claim is promoted here.

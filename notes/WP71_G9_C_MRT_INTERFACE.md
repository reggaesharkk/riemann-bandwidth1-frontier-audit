# WP71 G9-C — exact MRT interface and constant ledger

Date: 2026-10-04
Status: **SOURCE INTERFACE PINNED; endpoint maximalization quantified at exponent level; Stage-A substitution still open**

Source:
K. Matomäki, M. Radziwill, T. Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. LMS 118 (2019), 284--350.

## 1. Proposition 5.4: exact hypothesis ledger

MRT Proposition 5.4 fixes a sufficiently small epsilon>0, A>0, fixed k>=2, and B sufficiently large depending on k and A. It sets

    H = X^(sigma+epsilon),
    Q = (log X)^B,

with the long-shift regime sigma>=8/33 inherited from Proposition 3.4(ii). It assumes

    1 <= q <= Q,
    q = q0*q1,

and

    X^(-1/6-epsilon) <= lambda <= 1/(q*Q).

The arithmetic function is either Lambda*1_(X,2X] or d_k*1_(X,2X].

The conclusion is a squared Dirichlet-series mean-value bound of size

    <<_{k,epsilon,A,B} q * lambda^2 * H^2 * X * (log X)^(-A).

The implied constant is not numerical in the paper.

## 2. Proposition 3.4: additive-frequency interface

For q<=Q and (a,q)=1, Proposition 3.4(ii) gives, for sigma>=8/33,

    integral_{|theta-beta| <= X^(-sigma-epsilon)}
      |S_f(a/q+theta)|^2 dtheta
        <<_{k,epsilon,A,B} X (log X)^(-A),

provided

    X^(-1/6-epsilon) <= |beta| <= 1/(qQ).

Part (i) treats the complementary larger-frequency region.

Important: MRT's H is a **shift-window scale**. It is not the same object as the length of our moving m-interval I_k(n). A bulk lower bound on |I_k(n)| does not by itself verify H>=X^(8/33+epsilon). These checks must remain separate in the substitution table.

## 3. Lemma 2.2 has an explicit operator constant

MRT defines the maximal interval sum

    |sum_{X<=n<=X0} g(n)|*
      = sup_{X<=X1<=X2<=X0} |sum_{X1<=n<=X2} g(n)|.

Lemma 2.2 gives the exact inequality

    |sum f(n)g(n)|*
      <= |sum g(n)|*
         * ( sup|f| + (X0-X)*sup|f'| ).

There is no hidden multiplicative constant in this displayed summation-by-parts step. For a slow Stage-A weight f, the only price is its explicit variation norm

    V(f) := sup|f| + length*sup|f'|.

This is the correct quantity to put in the G9 weight ledger.

## 4. Corollary 2.5: endpoint-independent, but not numerically constant-explicit

For f supported on [X/C,CX], Corollary 2.5 gives uniformly for every interval I=[X1,X2]

    |D[f 1_I](1/2+it)|
      <=_C
      integral_{-T}^{T} |D[f](1/2+i(t+u))| du/(1+|u|)
      + ||f||_infty * X^(1/2) * log(2+T)/T.

The endpoint dependence is completely absent from the right-hand side.

The kernel mass is explicit:

    integral_{-T}^{T} du/(1+|u|) = 2 log(1+T).

So one application costs at most one logarithmic power at amplitude level, hence two logarithmic powers after squaring, before any additional outer integrations.

However the symbol <=_C carries an implicit constant depending on C. The paper does not supply a numerical value for this constant. Therefore it is invalid to turn Corollary 2.5 into a finite exact rational R-unit number unless that constant is reconstructed from the proof and all imported Perron constants.

For our asymptotic purpose this is unnecessary: the constant is fixed while Proposition 5.4 supplies arbitrary log-power saving.

## 5. Proposition 5.4 itself is not an effective numerical constant source

The bound in Proposition 5.4 is stated with an implied constant depending on k, epsilon, A and B, with B only required to be sufficiently large. The proof also uses standard asymptotic estimates. Hence the correct certification target is

    fixed constant * (log X)^(-eta) = o(1),

not a finite decimal upper bound at a particular X.

This distinction is essential. The local exact checker should certify algebraic identities and exponent inequalities; it must not invent numerical values for hidden big-O constants.

## 6. Maximalization inheritance

Because Corollary 2.5 is pointwise and endpoint-independent, define

    Dstar_f(t) = sup_I |D[f 1_I](1/2+it)|.

Taking the supremum over I preserves the same right-hand side. Minkowski then passes this through the Proposition-5.4 type character/t0 functional with only powers of log X coming from the kernel mass 2 log(1+T).

Thus no endpoint union bound is needed.

This closes the **maximalization mechanism**, not the full Stage-A theorem.

## 7. Fail-closed Stage-A substitution table

| MRT symbol | Stage-A object | Required check | Status |
|---|---|---|---|
| X | dyadic prime scale of m or n block | exact support after dyadic partition | OPEN |
| H=X^(sigma+eps) | shift-window length in h | identify h=qk range and prove sigma>=8/33 | OPEN |
| q | structured shift modulus | q<=Q=(log X)^B | PARTIAL: polylog truncation available |
| q0,q1 | character factorization | specify factorization used by MRT transform | OPEN |
| lambda | additive/multiplicative frequency scale | X^(-1/6-eps)<=lambda<=1/(qQ) | OPEN |
| f | prime sequence | exactly Lambda*1_(X,2X] after dyadic split | OPEN |
| interval I | moving m-window | handled by Cor. 2.5 maximalization | MECHANISM CLOSED |
| slow weight | Stage-A geometry/kernel | Lemma 2.2 variation norm V(f) | FORMULA CLOSED; bound OPEN |
| collar | small n/k endpoint family | exact consumed R-unit charge | OPEN |

If any OPEN row survives, G9-C remains open.

## 8. Citation correction

The shorthand 'Proposition 5.4, Appendix A' is incorrect.

- Proposition 5.4 is proved through the main Sections 6--7 argument.
- Appendix A proves Proposition 5.5.
- Lemma 2.2 supplies maximal summation by parts.
- Corollary 2.5 supplies endpoint-independent interval truncation.

All four roles must be cited separately.

## 9. Gate state

- G9-A exact welding reindexing: CLOSED.
- G9-B signed main local factorization and rectangular calibration: CLOSED.
- G9-B moving-interval combinatorics: CLOSED.
- G9-C maximal endpoint mechanism: CLOSED AT REDUCTION LEVEL.
- G9-C full Stage-A parameter substitution: OPEN.
- G9-D exact R-unit collar/outer-budget normalization: OPEN.

No theorem percentage is promoted by this source audit.

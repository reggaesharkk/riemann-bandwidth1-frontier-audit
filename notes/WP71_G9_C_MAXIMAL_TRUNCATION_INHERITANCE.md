# WP71 G9-C — maximal-truncation inheritance from MRT Corollary 2.5

Date: 2026-10-04
Status: **DIRICHLET-SERIES MAXIMALIZATION DERIVED; Stage-A parameter substitution still open**

This note removes one conceptual obstruction from the moving-endpoint problem: no union bound over all endpoint pairs is needed.

## 1. Published pointwise truncation inequality

For f supported on a fixed dyadic-scale interval, MRT Corollary 2.5 states, uniformly for every subinterval I=[X1,X2] and every t, that

    |D[f 1_I](1/2+it)|
      <= C * integral_{|u|<=T} |D[f](1/2+i(t+u))| du/(1+|u|)
         + ||f||_infty X^(1/2) log(2+T)/T.

The right side is independent of the endpoints X1,X2.

Therefore taking the supremum over **all** subintervals is immediate:

    Dstar_f(t)
      := sup_I |D[f 1_I](1/2+it)|

satisfies the same right-hand side.

This is stronger than controlling a finite endpoint family by a union bound.

## 2. Passage through the Proposition 5.4 functional

The Proposition 5.4 quantity is monotone in |D|: for each outer t it sums over characters and integrates |D| over a t0-window, then squares and integrates in t.

Insert the pointwise maximal bound above. Minkowski moves the u-integral outside the character/t0 functional. Since

    integral_{|u|<=T} du/(1+|u|) = O(log(2+T)),

maximalizing the interval truncation costs only fixed powers of log X.

The additive truncation error is also endpoint-independent. For f=Lambda 1_(X,2X],

    ||f||_infty <= log(2X).

In the actual proof of Proposition 5.4, MRT chooses a truncation parameter of the form

    T = lambda * X^(1-epsilon/10)

when removing a support truncation. With the proposition's lower bound

    lambda >= X^(-1/6-epsilon),

the pointwise additive error is power-saving in X, up to logarithms, and is negligible against any requested logarithmic saving after the surrounding integration.

Thus Proposition 5.4 admits the following maximal-truncation variant with the same parameter range and with only an arbitrarily absorbable logarithmic loss:

    replace |D[f](s)| by sup_I |D[f 1_I](s)|.

Because the source proposition already permits arbitrary requested log-power saving A (by choosing its internal B sufficiently large), this extra log loss can be absorbed by asking for a stronger source exponent.

## 3. Why this matters for G9

The G9-B moving interval produces prime-pair errors on intervals I_k(n) whose endpoints vary with n. We do not have to enumerate or union-bound those endpoints inside the Dirichlet-polynomial argument.

Instead, the endpoint family is dominated pointwise by MRT's endpoint-independent maximal Dirichlet-series majorant.

This turns the G9-C question into two remaining checks:

1. **circle-method inheritance:** carry the maximalized Proposition 5.4 bound through the same Proposition 3.4 / correlation reduction used by MRT;
2. **Stage-A scale substitution:** verify every middle-band cell satisfies the actual q, lambda, H and dyadic-scale inequalities, and account for the logarithmic bulk threshold.

## 4. Bulk/collar interface

On the logarithmic bulk from WP71_G9_BULK_COLLAR_REDUCTION, the moving interval length is at least

    delta*M,  delta=(log X)^(-D).

Therefore an ambient-scale maximal correlation error of size

    M*(log X)^(-A')

is at most

    |I|*(log X)^(-(A'-D)).

For squared L2 estimates the loss is at most 2D logarithmic powers. Choosing A' larger absorbs it.

The genuinely tiny endpoint intervals are removed into the deterministic collar and must be charged separately in R-units.

## 5. Evidence boundary

This derivation is an analytic reduction, not yet the final G9-C theorem. It does not claim that Proposition 5.4 alone is the moving-correlation statement.

The remaining work is to re-run the published Proposition 3.4/circle-method interface with Dstar_f in place of D[f], verify the Stage-A parameter table, and then combine with the collar charge.

Source basis: MRT Lemma 2.2, Corollary 2.5, Proposition 5.4, and the proof step where Corollary 2.5 is already used to remove a truncation.

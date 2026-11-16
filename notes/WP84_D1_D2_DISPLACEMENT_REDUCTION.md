# WP84 — exact D1/D2 reduction to rank-four displacement generators

Date: 2026-10-05

Status: **BIVARIATE TRANSITION-MEASURE FORMULATION ELIMINATED ALGEBRAICALLY FOR THE SHARP MODEL; PERMUTATION-AVERAGED GENERATOR LIMIT OPEN**

The LRSC-inspired displacement-rank closure gives a sharper route to the
Lindeberg drift and Hessian terms.

For one current sharp block B and one intermediate fixed-pole resolvent R,
put

    X = B R.

Then both required Taylor coefficients are z-derivatives of the first two
normalized traces of X, and X has displacement rank at most four.

## 1. First derivative identity

Let

    R(z)=(H-zI)^(-1).

Since

    dR/dz = R^2,

we have

    d/dz tau(BR)
      = tau(BR^2)
      = tau(RBR).

Therefore the first-order Lindeberg scalar is exactly

    boxed:
    D1(H;B,z)
      = d/dz tau(BR).

No bivariate spectral measure is required to state it.

## 2. Second derivative identity

Likewise

    d/dz tr(BRBR)
      = tr(BR^2BR)+tr(BRBR^2).

By cyclicity the two terms are equal and each is

    tr(RBRBR).

Hence

    boxed:
    D2(H;B,z)
      = tau(RBRBR)
      = (1/2) d/dz tau((BR)^2).

So the second-order term is determined by the first two trace moments of the
single matrix

    X=BR.

## 3. Displacement rank of X

Let

    D=diag(0,1,...,d-1).

The sharp current block satisfies

    rank[D,B] <= 2,

and the exact resolvent closure gives

    rank[D,R] <= 2.

Using Leibniz,

    [D,BR]
      = [D,B]R + B[D,R].

Therefore

    boxed:
    rank[D,X] <= 4.

Choose any factorization

    [D,X]=G H^T,

with at most four columns in G and H.

## 4. Exact reconstruction from diagonal plus generators

For i!=j,

    [D,X]_{ij}
      = (i-j)X_{ij}.

Hence

    boxed:
    X_{ij}
      = (G H^T)_{ij}/(i-j),
      i!=j.

Thus X is completely determined by:

- its d diagonal entries x_i=X_ii;
- at most four right generator columns;
- at most four left generator columns.

Again the state is O(d), not d^2.

## 5. Exact trace-square formula

Because

    tr(X^2)
      = sum_i X_ii^2
        + sum_{i!=j} X_ij X_ji,

the reconstruction above gives

    boxed:
    tr(X^2)
      = sum_i x_i^2
        - sum_{i!=j}
            C_ij C_ji/(i-j)^2,

where

    C=G H^T=[D,X].

This is an exact finite identity.

Equivalently, expanding the rank-four generators,

    C_ij
      = sum_{alpha<=4} G_{i alpha} H_{j alpha},

turns the second term into a finite sum of scalar discrete
1/(i-j)^2 transforms of generator products.

There is no need to carry a generic two-variable transition measure Gamma.

## 6. Lindeberg closure target after this reduction

For every current block B_j and subset state S define

    X_{S,j}(z)
      = B_j R_S(z).

Then the exact first two terms are

    D1
      = d/dz [
          d^(-1) sum_i (X_{S,j})_ii
        ],

and

    D2
      = (1/2) d/dz [
          d^(-1) {
            sum_i (X_{S,j})_ii^2
            - sum_{i!=j}
                C_ij C_ji/(i-j)^2
          }
        ],

with

    C=[D,X_{S,j}],
    rank C<=4.

Therefore the analytic debt is now a finite list of one-dimensional grid
statistics:

1. diagonal of B_j R_S;
2. four displacement-generator columns for B_j R_S;
3. their discrete squared-Cauchy transforms;
4. permutation averages of those quantities.

This is strictly smaller than proving a full bivariate local law.

## 7. Relation to connected fourth-order memory

Nothing in this reduction scalarizes the state.

The generator term

    -sum_{i!=j} C_ij C_ji/(i-j)^2

retains noncommutative off-diagonal information.

Therefore the order-four crossing and connected sectors are not discarded.
The exact -1/60 calibration can, in principle, live in the generator part.

This is precisely the feature missing from the falsified multiplication-only
closure.

## 8. New kill gate

The next theorem-grade attack is:

    prove the permutation-averaged limits of the diagonal and rank-four
    generator statistics above for the retained prime range.

If those limits close using only the scalar Dirichlet-polynomial
representation Q_S and classical bounded harmonic-analysis estimates, WP84
would no longer require an operator-valued Gamma-law.

No unconditional >79 theorem is claimed.

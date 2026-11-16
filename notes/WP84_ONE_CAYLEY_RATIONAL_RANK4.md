# WP84 — exact one-Cayley rational rank-four first strike

Date: 2026-10-05

Status: **EXACT FINITE-d REDUCTION; THE MATCHED TWO-POLE POSITIVE ENERGY IS A SINGLE-CAYLEY RATIONAL FUNCTION WITH DISPLACEMENT RANK AT MOST FOUR**

No unconditional zero-density percentage is claimed here.

The recent degree-3 Cayley majorant reduced the conditioned two-pole route to one polynomial in U=(H+iI)(H-iI)^(-1), with displacement rank at most six. That is minimal only inside the polynomial-majorant architecture. The matched two-pole filter gives a smaller exact bounded rational state.

Let b=9/4 and q=(b-1)/(b+1)=5/13. Put

    U=(H+iI)(H-iI)^(-1),
    A=(I-qU)^(-1).

Then

    U_b=(H+ibI)(H-ibI)^(-1)
       =(U-qI)(I-qU)^(-1).

Since U is unitary,

    ||A|| <= 1/(1-q)=13/8.

For every c>0,

    L_c=(H-cI)(H-icI)^(-1)
       =aI+gamma U_c,

with

    a=(1-i)/2,
    gamma=(1+i)/2.

The matched defect factor is

    K_match=L_1 L_b,

and

    I-f_match(H)=K_match^*K_match.

Thus the record problem is the positive energy tau(K_match^*K_match).

## Exact Möbius commutator

Let C=[D,U]. Since

    [D,A]=q A C A,

we get

    [D,U_b]=(1-q^2) A C A.

Hence rank[D,U_b]<=rank C. In the sharp Loewner state rank C<=2, so rank[D,U_b]<=2.

Also

    [D,L_1]=gamma C,
    [D,L_b]=gamma(1-q^2)ACA.

Therefore

    boxed:
    [D,K_match]
      =gamma C L_b
       +gamma(1-q^2)L_1 A C A.

Each term has rank at most two, so

    boxed:
    rank[D,K_match]<=4.

This uses only the single Cayley unitary U and the safe rational factor A.

## Explicit four-column factorization

If C=G H^* is any rank-two factorization, then

    [D,K_match]=G_4 H_4^*,

with

    G_4=[ gamma G, gamma(1-q^2)L_1 A G ],

and block rows

    H_4^*=[ H^*L_b ; H^*A ].

At q=5/13,

    1-q^2=144/169.

Thus the off-diagonal defect energy has a one-dimensional Fourier representation with matrices of size at most 4 x 4.

## Positive displacement energy

For i!=j,

    (K_match)_ij=[D,K_match]_ij/(i-j).

Hence exactly

    tau(K_match^*K_match)
      =d^(-1) sum_i |K_ii|^2
       +d^(-1) sum_{i!=j}|[D,K_match]_ij|^2/(i-j)^2.

Both terms are nonnegative.

The model matched-filter simple-zero ledger is 73.0318273584...%, with positive-index record margin 0.0284091182481592....

## Strategic correction

The degree-2 dual obstruction proves only that no degree-2 trigonometric polynomial majorant can cross the conservative record. It does not imply a universal rank-four obstruction.

The matched rational route shows:

    rank six is minimal only inside the current polynomial-majorant route,
    not inside the full bounded rational route.

For proof development maintain both routes:

1. matched rational route: one U, one well-conditioned inverse A, rank <=4, larger model margin;
2. integer degree-3 route: one polynomial q(U), no rational inverse, rank <=6, slightly smaller margin.

The matched rational rank-four route should be tested first analytically. Do not expand A geometrically unless the exact rational channel stalls.

See:

    notes/WP84_TWO_POLE_MATCHED_CAYLEY_FILTER.md
    notes/WP84_TWO_POLE_POSITIVE_DISPLACEMENT_ENERGY.md
    notes/WP84_DEGREE2_CAYLEY_OBSTRUCTION.md
    notes/WP84_INTEGER_RANK6_CAYLEY_SQUARE.md

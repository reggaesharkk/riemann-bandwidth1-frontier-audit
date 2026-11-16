# WP84 — conditioned exact rank-six bounded consumer at 79.5489%

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE BOUNDED >79.5 MODEL CONSUMER; ONE CAYLEY POINT; POSITIVE ENERGY; DISPLACEMENT RANK AT MOST SIX; SUPERSEDES THE PREVIOUS 79.5197% CUBIC**

No unconditional zero-density percentage is claimed here.

The previous optimized cubic consumer had model simple-zero value
79.5197401511...% and a full-sharp rank-six positive-energy formulation.

A second optimization pass targeted the same rank-six class while also
penalizing the exposed Gaussian heat-curvature coefficients.  A simple exact
rational point improves both the model value and the curvature conditioning.

Let

    U=(H+iI)(H-iI)^(-1)

and define

    boxed:

    q(u)
      =
      1/5000
      [
        1936 u^3
        +(-192-5495 i)u^2
        +(-5695+169 i)u
        +(44+2205 i)
      ].

Put

    Q=q(U),

    p(x)=|q((x+i)/(x-i))|^2,

    h(x)=1-p(x).

Then

    tau h(H)
      =
      1-tau(Q^*Q).

## 1. Exact support certificate

Direct exact simplification gives

    p(x)-1

      =
      S(x)
      /
      [
        12500000 (x^2+1)^3
      ],

where

    S(x)
      =
        2645 x^6
       -82863712 x^5
       +183847891 x^4
       -303496416 x^3
       +186573135 x^2
       -84028544 x
       +2001.

For x=-y<=0,

    boxed:

    S(-y)
      =
        2645 y^6
       +82863712 y^5
       +183847891 y^4
       +303496416 y^3
       +186573135 y^2
       +84028544 y
       +2001
      >
      0.

Therefore

    p(x)>=1
    for every x<=0.

For x>0, p(x)>=0 because it is a modulus square.  Hence globally

    boxed:

    h(x)<=1_{x>0}.

Thus every Hermitian H satisfies

    boxed:

    n_+(H)/d
      >=
      1-tau(Q^*Q).

No spectral support assumption or raw moment bound is used.

## 2. Exact Christoffel-model value

Against the frozen four-node Christoffel extremal model,

    boxed:

    E_model[p]
      =
      1272283602671916206561064875108101
      /
      12442212289373925054228673142500000

      =
      0.1022554167283008....

Therefore the induced model simple-zero coefficient is

    boxed:

    1-2E_model[p]

      =
      4948822542015046320553271696141899
      /
      6221106144686962527114336571250000

      =
      0.7954891665433984....

That is

    boxed:

    79.5489166543...%.

The direct >79 theorem threshold remains

    tau(Q^*Q)<0.105.

The exact model cushion is

    boxed:

    0.105-E_model[p]

      =
      34148687712345924132945804854399
      /
      12442212289373925054228673142500000

      =
      0.0027445832716992....

This is larger than the previous optimized cubic cushion
0.002598700755693....

## 3. Positive rank-six displacement energy

Because q has degree three and the full sharp Loewner matrix satisfies

    rank[D,U]<=2,

the polynomial commutator identity gives

    boxed:

    rank[D,Q]<=6.

More explicitly, with

    C=[D,U],

    B0=q1 I+q2 U+q3 U^2,

    B1=q2 I+q3 U,

one has exactly

    boxed:

    [D,Q]
      =
      C B0
      +U C B1
      +U^2 C q3.

If

    C=G2 H2^T

is the exact two-column sharp source factorization, then

    boxed:

    [D,Q]=G6 H6^T,

where

    G6=[G2, U G2, U^2 G2],

and the three two-row blocks of H6^T are

    H2^T B0,
    H2^T B1,
    q3 H2^T.

Thus the six-column state is explicit rather than an abstract rank bound.

## 4. Extra symmetry: three canonical wedge pairs

For the sharp real-symmetric H,

    U^T=U,

hence

    Q^T=Q.

Therefore

    boxed:

    [D,Q]^T=-[D,Q].

The rank-six commutator is a complex skew-symmetric matrix.

Consequently its nonzero singular values occur in equal pairs.  The generic
rank-six state therefore consists of at most three canonical skew/wedge
channels, not six unrelated singular directions.

This pairing was verified numerically on the exact sharp-Loewner regression
state to machine precision; the algebraic skew-symmetry above is the proof.

## 5. Exact positive energy decomposition

For i!=j,

    Q_ij
      =
      [D,Q]_ij/(i-j).

Hence

    boxed:

    tau(Q^*Q)

      =
      d^(-1) sum_i |Q_ii|^2

      +
      d^(-1) sum_{i!=j}
        |[D,Q]_ij|^2/(i-j)^2.

Both pieces are nonnegative.

The off-diagonal term may be represented by the usual one-dimensional S2
Fourier kernel acting only on the six-column factor G6,H6.

## 6. Heat-flow conditioning also improves

Write on the unit circle

    |q(u)|^2
      =
      c0
      +sum_{k=1}^3[
         c_k u^k+conjugate(c_k)u^(-k)
       ].

The exact coefficients are

    c0=17826383/6250000,

    c1=-42431/12500000
       +(6816213/3125000)i,

    c2=-23150443/25000000
       -(36401/6250000)i,

    c3=1331/390625
       -(53361/312500)i.

Using U=I+2iR at z=i gives

    boxed:

    tau(Q^*Q)
      =
      E_infinity
      +2 Re[
          A m(i)
          +B m'(i)
          +C m''(i)
        ],

where

    boxed:

    E_infinity
      =
      |q(1)|^2
      =
      2500529/2500000
      =
      1.0002116,

    A
      =
      -2589491/781250
      -(11532549/3125000)i,

    B
      =
      22894891/6250000
      +(3238061/1562500)i,

    C
      =
      -53361/78125
      -(5324/390625)i.

Numerically,

    |A|+|B|+|C|
      ~=9.85229.

For the superseded 79.51974015...% cubic the same exposed coefficient norm is

    ~=10.04602.

Thus the new exact point improves:

- the model defect;
- the >79 cushion;
- the large-noise boundary constant;
- the first scalar heat-curvature coefficient proxy;

while keeping the same rank-six displacement width.

## 7. High-precision structural verification

An 80-decimal sharp-Loewner check on a deterministic 11x11 regression state
gave residuals:

    Cayley unitarity               1.49e-81
    Q symmetry                     5.27e-83
    [D,Q] skew symmetry            1.35e-82
    polynomial commutator          8.85e-82
    rank-two source factor         6.72e-82
    six-column factor              1.01e-81
    positive-energy decomposition  1.16e-84.

These are verification values for the finite algebra, not evidence for the
large-T arithmetic inequality.

## 8. New preferred direct >79 target

The preferred single-shot direct theorem target is now

    boxed:

    limsup_T
      tau[
        q(U_T)^*q(U_T)
      ]
      <
      0.105,

with q fixed exactly above.

If proved, this yields an unconditional simple-zero proportion above 79%.

The current model benchmark is

    79.5489166543...%,

not a theorem claim.

## Evidence boundary

Closed:

- exact rational q;
- exact global half-line support certificate;
- exact model evaluation;
- exact positive-energy representation;
- exact rank-six commutator factorization;
- exact skew-symmetry and paired-singular-value structure;
- exact one-point resolvent/heat-flow coefficient map.

Open:

- the large-T one-sided energy inequality for the actual sharp zeta matrix.

See:

    notes/WP84_OPTIMIZED_RANK6_79_CONSUMER.md
    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md
    notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md

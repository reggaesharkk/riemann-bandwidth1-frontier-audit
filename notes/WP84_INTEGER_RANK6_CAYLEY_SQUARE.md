# WP84 — exact integer-coefficient rank-six Cayley square

Date: 2026-10-05

Status: **EXACT GLOBAL ONE-POINT MINORANT; SINGLE POSITIVE DEGREE-3 CAYLEY ENERGY WITH SMALL INTEGER COEFFICIENTS**

No unconditional zero-density percentage is claimed here.

The previous conditioned degree-3 majorant proved that the post-band theorem
can be reduced to one positive degree-3 Cayley energy at z=i.

The Fejer factor supplied by the exact trigonometric polynomial is algebraic.

For arithmetic transport it is cleaner to have a single factor with exact
small rational coefficients from the beginning.

Such a factor exists.

## 1. One exact polynomial

Let

    U
      =
      (H+iI)(H-iI)^(-1).

Define

    boxed:

    q(u)
      =
      1/105
      [
        72 u^3
        -(6+106 i)u^2
        -(44+8 i)u
        -(12-3 i)
      ].

Equivalently

    q_0
      =
      -4/35 + i/35,

    q_1
      =
      -44/105 - 8i/105,

    q_2
      =
      -2/35 - 106i/105,

    q_3
      =
      24/35.

Put

    boxed:
    p_q(u)=|q(u)|^2

for |u|=1.

Then the candidate support-free minorant is

    boxed:
    h_q(x)
      =
      1-p_q(
        (x+i)/(x-i)
      ).

## 2. Exact domination of the conditioned two-pole defect

Recall the theorem-conditioned two-pole defect

    g_*(x)
      =
      [x^2-(82/25)x+9/4]^2
      /
      [(x^2+1)(x^2+81/16)].

A direct exact simplification gives

    boxed:

    p_q(u(x))-g_*(x)

      =
      N_q(x)
      /
      [
        275625
        (x^2+1)^3
        (16x^2+81)
      ],

where

    N_q(x)
      =
      558400 x^8
      +4033600 x^7
      -3655019 x^6
      -46464400 x^5
      +102823262 x^4
      -73448000 x^3
      +17415581 x^2
      -486000 x
      +234900.

The exact Sturm count is

    boxed:
    N_q has zero real roots.

Also

    N_q(0)=234900>0,

and the leading coefficient is positive.

Therefore

    boxed:
    p_q(u(x))>g_*(x)

for every real x.

Since

    f_*(x)=1-g_*(x)
      <= 1_{x>0},

we obtain the global support-free one-point minorant

    boxed:

    h_q(x)
      =
      1-|q(u(x))|^2

      <=
      f_*(x)

      <=
      1_{x>0}.

So the theorem may be expressed entirely at the single point z=i.

## 3. Positive-energy form

For Hermitian H,

    Q=q(U).

Then exactly

    boxed:

    h_q(H)
      =
      I-Q^*Q.

Therefore

    boxed:

    tau h_q(H)
      =
      1-tau(Q^*Q).

The first-record theorem becomes one upper bound on the positive energy

    boxed:
    tau(Q^*Q).

No cancellation between separate Cayley moments is required.

## 4. Exact pinned-model value

Against the pinned Christoffel model,

    boxed:

    E_model[
      Q^*Q
    ]

      =
      7587045874174614507624172997869
      /
      54870156196139009489148448558425

      =
      0.13827272237122745....

Hence the induced model positive-index lower bound is

    boxed:

    q_model
      =
      47283110321964394981524275560556
      /
      54870156196139009489148448558425

      =
      0.8617272776287726....

The corresponding model simple-zero ledger is

    boxed:

    39696064447789780473900102562687
    /
    54870156196139009489148448558425

      =
      0.7234545552575451....

So this exact integer-coefficient one-point rung has model simple-zero value

    boxed:
    72.3454555258...%.

This remains a model/consumer value only.

## 5. Record margin

The conservative positive-index record ceiling for the defect energy is

    E_rec
      =
      0.163249981456072....

Therefore the exact integer Cayley square retains pre-band margin

    boxed:

    Delta_q
      =
      E_rec
      -
      E_model[Q^*Q]

      ~= 0.0249772590848446.

That is only modestly below the optimized real-coefficient p_3 margin.

The simplification is substantial:

- one exact polynomial q;
- common denominator 105;
- small integer coefficients;
- automatic positivity;
- one spectral point z=i;
- degree three.

## 6. Exact displacement rank

Let

    C=[D,U].

The sharp Loewner resolvent law gives

    rank C<=2.

Write

    q(U)
      =
      q_0 I+q_1U+q_2U^2+q_3U^3.

Then

    boxed:

    [D,Q]

      =
      C(
        q_1 I+q_2U+q_3U^2
      )

      + U C(
          q_2 I+q_3U
        )

      + U^2 C q_3.

Therefore

    boxed:
    rank[D,Q]<=6.

This bound is exact and requires no sum of the separate
rank[D,U^k] estimates.

## 7. Positive displacement-energy decomposition

For i!=j,

    Q_ij
      =
      [D,Q]_ij/(i-j).

Hence

    boxed:

    tau(Q^*Q)

      =
      (1/d)
      sum_i |Q_ii|^2

      +
      (1/d)
      sum_{i!=j}
        |[D,Q]_ij|^2/(i-j)^2.

Both pieces are nonnegative.

Thus the post-band first-strike theorem is a positive diagonal energy plus a
positive rank-six squared-Cauchy energy.

## 8. Hybrid full-to-band architecture

The simple integer Cayley square is ideal for the finite-band arithmetic
step.

For the long-displacement comparison, keep using the conditioned two-pole
wrapper f_* because its explicit O(1/R) constant is much better conditioned:

    C_{2,*}
      =
      2.2079400595....

Since

    h_q<=f_*,

for the fixed-band H_R,

    f_*(H_R)
      >=
      h_q(H_R)
      =
      I-Q_R^*Q_R.

Hence

    boxed:

    tau f_*(H)

      >=
      1
      -
      tau(Q_R^*Q_R)
      -
      C_{2,*}/R
      +o(1).

For R=256,

    C_{2,*}/R
      ~=0.00862476586.

So the finite-band integer-energy target is

    boxed:

    limsup_T
      tau(Q_{T,R}^*Q_{T,R})

      <
      0.15462521560...

while the exact model benchmark is

    0.13827272237....

This leaves about

    boxed:
    0.01635249323

for the finite-band arithmetic/local-law step.

## 9. Why this is preferable to the algebraic Fejer factor

The previous exact p_3 was already positive and therefore admitted a
Fejer--Riesz factor.

But that factor had algebraic coefficients.

The present q:

    - is exact over Q(i);
    - has denominator only 105;
    - is already a single square;
    - retains a substantial record margin;
    - has the same rank-six displacement ceiling.

So this should replace the algebraic spectral factor as the implementation
target for the next arithmetic proof.

## 10. Evidence boundary

Closed here:

- exact global one-point minorant;
- exact Sturm positivity;
- exact small-integer factor;
- exact pinned-model certificate;
- exact positive-energy identity;
- exact rank-six displacement law.

Still open:

- the zeta-side finite-band estimate

      tau(Q_R^*Q_R)
        <
      0.15462521560...

  for one convenient fixed R such as 256.

No unconditional record theorem is claimed.

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md
    notes/WP84_CONDITIONED_DEGREE3_CAYLEY_MAJORANT.md
    notes/WP84_DEGREE3_POSITIVE_RANK6_ENERGY.md

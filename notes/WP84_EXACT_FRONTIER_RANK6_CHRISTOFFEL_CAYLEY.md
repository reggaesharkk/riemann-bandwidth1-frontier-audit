# WP84 — exact-frontier bounded Christoffel–Cayley consumer with rank six

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE BOUNDED CONSUMER HITTING THE FULL 79.62709668... CHRISTOFFEL MODEL FRONTIER; ONE FIXED CAYLEY POINT; POSITIVE ENERGY; DISPLACEMENT RANK AT MOST SIX**

No unconditional zero-density percentage is claimed here.

The bounded Christoffel ladder showed that the full 79.62709668... model
frontier can be approached by a family of bounded fixed-pole consumers.

There is a simpler direct construction.

It uses the Christoffel cubic itself, but divides its square by exactly the
third power of one fixed quadratic denominator.  With a canonical choice of
pole height, the resulting bounded consumer:

- is support-free;
- vanishes at the zero atom;
- equals one at all three positive Christoffel nodes;
- tends to zero at both spectral infinities after taking the minorant;
- has a single repeated nonreal pole pair;
- has a positive rank-six displacement factor.

So the full model frontier is already represented by one fixed bounded
rank-six consumer.

## 1. Christoffel cubic

Write

    P(x)
      =
      1-Ax+Bx^2-Cx^3,

with

    A=43428/13891,

    B=37704/13891,

    C=9660/13891.

The frozen Christoffel quadrature has:

- zero atom
      w0=1415/13891;

- three positive nodes
      x_1,x_2,x_3,
  which are exactly the positive roots of P.

Define the canonical pole height a_* by

    boxed:

    a_*^3
      =
      1/C
      =
      13891/9660.

Thus

    a_*
      =
      (13891/9660)^(1/3)

      ~=1.1287180278353677.

In particular a_*>1.

## 2. Bounded rational defect

Define

    boxed:

    p_*(x)
      =
      a_*^6 P(x)^2
      /
      (x^2+a_*^2)^3,

and

    boxed:

    h_*(x)
      =
      1-p_*(x).

Clearly p_*(x)>=0 for all real x, so

    h_*(x)<=1

for x>0.

It remains to prove h_*(x)<=0 for x<=0.

## 3. Exact negative-half-line support certificate

Put x=-y with y>=0.

Then

    P(-y)
      =
      1+Ay+By^2+Cy^3.

Expand

    N(y)
      =
      a_*^6 P(-y)^2
      -(y^2+a_*^2)^3.

The constant coefficient cancels.

The y^6 coefficient also cancels exactly because

    C^2 a_*^6=1.

The remaining coefficients are

    y:
      2A a_*^6,

    y^2:
      a_*^4[
        a_*^2(A^2+2B)-3
      ],

    y^3:
      a_*^6[
        2C+2AB
      ],

    y^4:
      a_*^2[
        a_*^4(B^2+2AC)-3
      ],

    y^5:
      2BC a_*^6.

Every odd coefficient is strictly positive.

For the two even coefficients, exact rational arithmetic gives

    boxed:

    A^2+2B-3
      =
      2354604069/192959881
      >
      0,

and

    boxed:

    B^2+2AC-3
      =
      1681740933/192959881
      >
      0.

Since a_*>1, both even coefficients are also strictly positive.

Therefore

    boxed:

    N(y)>=0
    for every y>=0,

with equality only at y=0.

Hence

    boxed:

    p_*(x)>=1
    for every x<=0,

and globally

    boxed:

    h_*(x)
      <=
      1_{x>0}.

This is a finite exact coefficient-sign proof.  No numerical minimization or
Sturm scan is needed.

## 4. Boundedness and endpoint normalization

At x=0,

    P(0)=1,

so

    boxed:

    p_*(0)=1,
    h_*(0)=0.

At |x|->infinity,

    p_*(x)
      ->
      a_*^6 C^2
      =
      1,

so

    boxed:

    h_*(x)->0.

Thus h_* is bounded and Proposition-R safe.

## 5. The Christoffel model is hit exactly

At every positive Christoffel node x_j,

    P(x_j)=0,

so

    p_*(x_j)=0,
    h_*(x_j)=1.

At the zero atom,

    h_*(0)=0.

Therefore the frozen four-node model gives exactly

    boxed:

    E_model[p_*]
      =
      w0
      =
      1415/13891
      =
      0.1018645165934778...,

and

    boxed:

    E_model[h_*]
      =
      1-w0.

The induced model simple-zero coefficient is exactly

    boxed:

    1-2w0

      =
      11061/13891

      =
      0.7962709668130444...

      =
      79.6270966813...%.

Unlike the previous r_m hierarchy, there is no approximation gap to the
Christoffel model frontier.

This remains a model/consumer statement until the zeta-side energy estimate
is proved.

## 6. One fixed positive operator energy

For Hermitian H define

    boxed:

    Q_*
      =
      a_*^3
      P(H)
      (H-i a_* I)^(-3).

All factors are functions of H and commute.

Therefore

    boxed:

    Q_*^* Q_*
      =
      a_*^6
      P(H)^2
      (H^2+a_*^2 I)^(-3)

      =
      p_*(H).

Thus

    boxed:

    tau h_*(H)
      =
      1-tau(Q_*^*Q_*).

The theorem is one positive-energy problem.

## 7. Exact degree-three Cayley factor

Let

    U_*
      =
      (H+i a_* I)
      (H-i a_* I)^(-1).

For a scalar u set

    x
      =
      i a_*
      (u+1)/(u-1).

Then

    x-i a_*
      =
      2 i a_*/(u-1).

Hence

    boxed:

    Q_*
      =
      q_*(U_*),

where

    q_*(u)
      =
      (i/8)
      (u-1)^3
      P(
        i a_*(u+1)/(u-1)
      ).

This is a polynomial of degree three.

Explicitly,

    8 q_*(u)

      =
      [
        i+A a_*-iB a_*^2-C a_*^3
      ] u^3

      +[
        -3i-A a_*-iB a_*^2-3C a_*^3
      ] u^2

      +[
        3i-A a_*+iB a_*^2-3C a_*^3
      ] u

      +[
        -i+A a_*+iB a_*^2-C a_*^3
      ].

Since C a_*^3=1, these coefficients simplify further.

Numerically,

    q_*(u)
      ~=

      (0.31609465+0.30724985 i)

      +(-0.81609465+0.80724985 i) u

      +(-0.81609465-0.80724985 i) u^2

      +(0.31609465-0.30724985 i) u^3.

## 8. Displacement rank is at most six

The sharp Loewner matrix satisfies

    rank[D,U_*]<=2.

Since q_* has degree three,

    boxed:

    rank[D,Q_*]
      <=
      6.

The explicit polynomial commutator factorization is the same 2x3 Krylov
factorization used by the other degree-three Cayley consumers.

Because H is real symmetric,

    U_*^T=U_*,

and hence

    Q_*^T=Q_*.

Therefore

    boxed:

    [D,Q_*]^T
      =
      -[D,Q_*].

So the nonzero singular values again occur in equal pairs: the generic
rank-six state consists of at most three canonical wedge channels.

## 9. Positive diagonal plus K2 energy

Exactly,

    boxed:

    tau(Q_*^*Q_*)

      =
      d^(-1)
      sum_i |(Q_*)_ii|^2

      +
      d^(-1)
      sum_{i!=j}
        |[D,Q_*]_ij|^2/(i-j)^2.

This is the same finite six-column positive-energy interface already prepared
for the direct >79 attack.

## 10. First >79 theorem cushion

To prove a simple-zero proportion above 79 percent, it is enough to prove

    tau h_*(H)>0.895+o(1),

equivalently

    boxed:

    limsup_T
      tau(Q_{*,T}^*Q_{*,T})
      <
      0.105.

The exact model energy is w0, so the available model cushion is

    boxed:

    0.105-w0

      =
      8711/2778200

      =
      0.00313548340652221....

This exceeds the m=10 repeated-pole cushion while using rank at most six
instead of rank at most twenty.

## 11. Full 79.627 theorem target

The exact headline would follow from the sharper asymptotic inequality

    boxed:

    limsup_T
      tau(Q_{*,T}^*Q_{*,T})
      <=
      1415/13891.

If that holds with the already-closed zero-side/rank/background transfers,
then

    boxed:

    liminf
      N_0^s(T)/N(T)

      >=
      11061/13891

      =
      79.6270966813...%.

No delta ladder is required for this direct route.

The bounded Christoffel ladder remains independently useful because its
upper bound is moment-forced for every pinned six-moment law; the present
consumer instead gives a sharper single actual-zeta target.

## Evidence boundary

Closed:

- canonical fixed pole a_*;
- exact global half-line support certificate;
- boundedness and endpoint normalization;
- exact saturation of the frozen Christoffel quadrature;
- exact positive-energy factor;
- exact degree-three Cayley representation;
- displacement rank at most six;
- skew-symmetric three-wedge structure;
- exact >79 model cushion.

Open:

- the large-T zeta-side positive-energy inequality.

See:

    notes/WP84_CHRISTOFFEL_RANK6_POSITIVE_ENERGY.md
    notes/WP84_CONDITIONED_RANK6_79_CONSUMER.md
    notes/WP84_BOUNDED_CHRISTOFFEL_LADDER.md
    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md

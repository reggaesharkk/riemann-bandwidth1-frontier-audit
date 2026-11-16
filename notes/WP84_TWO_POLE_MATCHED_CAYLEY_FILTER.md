# WP84 — matched two-pole Cayley filter

Date: 2026-10-05

Status: **EXACT GLOBAL MINORANT; TWO SIMPLE POLES; DEFECT FACTORS INTO TWO AFFINE CAYLEY CONTRACTIONS**

No unconditional zero-density percentage is claimed here.

The theorem-conditioned two-pole member with A=82/25 is nearly optimal for
the explicit band-tail ratio.

A structurally cleaner member loses only about 0.2% in that conditioning
metric and factorizes exactly into two matched Cayley factors.

Take

    a=1,
    b=9/4,

and set

    boxed:
    Q(x)
      =
      (x-1)(x-9/4).

Define

    boxed:
    f_match(x)
      =
      1
      -
      [
        (x-1)^2/(x^2+1)
      ]
      [
        (x-9/4)^2/(x^2+81/16)
      ].

## 1. Global minorant is immediate factor by factor

For x<=0 and every c>0,

    (x-c)^2
      >=
      x^2+c^2

because

    (x-c)^2-(x^2+c^2)
      =
      -2cx
      >=0.

Hence each factor in the defect is at least one on x<=0, so

    f_match(x)<=0.

For x>0 the defect is nonnegative, so

    f_match(x)<=1.

Therefore

    boxed:
    1_{x>0}
      >=
      f_match(x)

globally.

No auxiliary polynomial inequality is needed.

## 2. Exact simple-pole decomposition

The rational function is

    f_match(x)

      =
      2x(
        52x^2-72x+117
      )
      /
      [
        (x^2+1)(16x^2+81)
      ].

Its exact partial fractions are

    boxed:

    f_match(x)

      =
      2(65x+72)/
        [65(x^2+1)]

      +
      72(65x-162)/
        [65(16x^2+81)].

Equivalently,

    f_match(H)
      =
      2 Re[
        c_1 R(i)
        +
        c_b R(9i/4)
      ],

with the unusually simple residues

    boxed:
    c_1
      =
      1-(72/65)i,

    c_b
      =
      9/4+(162/65)i.

Again there are only two simple poles and no derivatives.

## 3. Exact model certificate

Against the pinned Christoffel model,

    boxed:

    q_match
      =
      11902275928166268139448
      /
      13757325585554779750729

      =
      0.8651591367920871....

The corresponding model simple-zero ledger is

    boxed:

    2q_match-1

      =
      10047226270777756528167
      /
      13757325585554779750729

      =
      0.7303182735841743....

So the model rung is

    73.0318273584...%.

The positive-index margin over the conservative record threshold is

    boxed:
    Delta_match
      =
      0.0284091182481592....

## 4. Tail conditioning remains essentially optimal

The O(1/R) simple-resolvent constant is

    C_match
      =
      2.1728342265....

Thus

    boxed:

    Delta_match/C_match
      =
      0.01307468278....

The fully conditioned A=82/25 member gives

    0.01310366017....

So the matched factorization sacrifices only about 0.22% in this metric.

That is a very small price for the extra algebraic structure below.

## 5. Exact Cayley factorization

For any c>0 define the Cayley unitary

    U_c
      =
      (H+icI)(H-icI)^(-1).

Then

    boxed:

    (H-cI)(H-icI)^(-1)

      =
      (1-i)/2 I
      +
      (1+i)/2 U_c.

Call this affine unitary factor

    L_c.

The defect filter is exactly

    boxed:
    K_match
      =
      L_1 L_{9/4},

and

    boxed:
    I-f_match(H)
      =
      K_match^* K_match.

Thus the first-record theorem becomes

    tau(K_match^*K_match)
      <
      0.163249981456072....

The model energy is

    1-q_match
      =
      0.1348408632079129...,

leaving the margin Delta_match above.

## 6. Both Cayley unitaries are functions of one unitary

Let

    U=U_1.

For b>1,

    U_b
      =
      (U-qI)(I-qU)^(-1),

where

    q
      =
      (b-1)/(b+1).

At b=9/4,

    boxed:
    q=5/13.

So

    K_match

is a fixed rational inner function of the **single** unitary U=U_1.

The only denominator is

    I-(5/13)U,

whose inverse has the operator-norm geometric expansion

    sum_{n>=0}
      (5/13)^n U^n.

This gives the same rapidly convergent finite bounded-unitary hierarchy as
the general two-pole note, but now the defect itself is a product of two
transparent Cayley factors.

## 7. Displacement rank

Each U_c satisfies

    rank[D,U_c]<=2.

Therefore

    rank[D,L_c]<=2,

and the product identity

    [D,L_1L_b]
      =
      [D,L_1]L_b
      +
      L_1[D,L_b]

gives

    boxed:
    rank[D,K_match]<=4.

Hence its positive energy again has the exact form

    tau(K_match^*K_match)

      =
      diagonal energy
      +
      rank-four K2 displacement energy.

## 8. Recommendation

For proof development maintain both two-pole members:

A. conditioned numerical optimum:
       A=82/25;
       model simple 73.13642...%;
       best explicit tail ratio;

B. matched Cayley filter:
       A=13/4=a+b;
       model simple 73.03183...%;
       only 0.22% worse tail ratio;
       much cleaner factorization.

The matched member should be preferred whenever the next analytic estimate
uses positivity, Cayley products, or displacement generators.

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md
    notes/WP84_TWO_POLE_POSITIVE_DISPLACEMENT_ENERGY.md
    notes/WP84_TWO_POLE_CAYLEY_FINITE_REDUCTION.md

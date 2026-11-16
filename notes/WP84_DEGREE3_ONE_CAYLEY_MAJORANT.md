# WP84 — exact degree-3 one-Cayley majorant for the matched two-pole defect

Date: 2026-10-05

Status: **EXACT GLOBAL MAJORANT; AFTER TWO-POLE BAND TRUNCATION THE FIRST-STRIKE CONSUMER REDUCES TO U,U^2,U^3 AT z=i**

No unconditional zero-density percentage is claimed here.

The matched two-pole minorant is

    f_match(x)
      =
      1
      -
      g_match(x),

with

    g_match(x)
      =
      [(x-1)^2/(x^2+1)]
      [(x-9/4)^2/(x^2+81/16)].

Its direct two-simple-pole formulation is useful for the sharp O(1/R)
displacement-tail comparison.

Once that tail has been removed, the remaining fixed-band theorem can be
compressed further to a **single Cayley unitary at z=i and only three
powers**.

## 1. Cayley variable

For real x define

    u(x)
      =
      (x+i)/(x-i).

Then |u|=1.

For a Hermitian matrix H set

    U
      =
      (H+iI)(H-iI)^(-1).

Thus U is unitary.

## 2. Explicit degree-3 trigonometric polynomial

Define, for |u|=1 with u=e^{i theta},

    boxed:

    p_3(u)
      =
      1.679
      +0.206 cos(theta)
      -2.251 sin(theta)
      -0.621 cos(2theta)
      -0.329 sin(2theta)
      -0.150 cos(3theta)
      +0.043 sin(3theta).

Equivalently

    p_3(U)

      =
      1.679 I
      + 2 Re[
          c_1 U
          + c_2 U^2
          + c_3 U^3
        ],

with exact rational coefficients

    boxed:

    c_1
      =
      103/1000
      + (2251/2000)i,

    c_2
      =
      -621/2000
      + (329/2000)i,

    c_3
      =
      -3/40
      - (43/2000)i.

## 3. Exact global majorant

Substitute

    u=(x+i)/(x-i).

A direct exact simplification gives

    boxed:

    p_3(u(x))
      -
      g_match(x)

      =
      N(x)
      /
      [
        500
        (x^2+1)^3
        (16x^2+81)
      ],

where

    N(x)
      =
      912 x^8
      +7520 x^7
      -6599 x^6
      -83092 x^5
      +185207 x^4
      -136916 x^3
      +36799 x^2
      -1584 x
      +81.

The denominator is strictly positive for every real x.

The exact Sturm count of N on the real line is

    boxed:
    0 real roots.

Since

    N(0)=81>0

and the leading coefficient is positive,

    boxed:
    N(x)>0

for every real x.

Therefore

    boxed:
    g_match(x)
      <=
      p_3(u(x))

globally.

Equivalently

    boxed:
    1-p_3(u(x))
      <=
      f_match(x)
      <=
      1_{x>0}.

Thus

    h_3(x)
      :=
      1-p_3(u(x))

is itself a global support-free bounded minorant.

## 4. Exact pinned-model benchmark

Evaluate p_3 against the pinned four-node Christoffel model.

Exact polynomial reduction modulo the Christoffel cubic gives

    boxed:

    E_model[p_3(U)]

      =
      69125495024210721523306745833
      /
      497688491574957002169146925700

      =
      0.1388930951677425....

Therefore the induced positive-index lower bound is

    boxed:

    q_{3,Cayley}
      =
      1-E_model[p_3(U)]

      =
      428562996550746280645840179867
      /
      497688491574957002169146925700

      =
      0.8611069048322575....

The corresponding model simple-zero ledger is

    boxed:

    2q_{3,Cayley}-1
      =
      0.7222138096645150....

So even after replacing the exact matched two-pole defect by this coarse
degree-3 Cayley majorant, the model rung remains

    72.2213809664...%.

This is still a model/consumer statement only.

## 5. Record margin after the majorant loss

Against the conservative positive-index threshold

    q_rec
      =
      0.8367500185439279...,

the majorized one-Cayley rung retains

    boxed:

    Delta_3C
      =
      0.0243568862883296....

Equivalently its model simple-zero ledger sits about

    4.871377 percentage points

above the 67.3500037 comparison line.

Thus the majorant spends only part of the original matched-filter model
margin and still leaves a substantial theorem budget.

## 6. Why this is stronger than the geometric N=8 reduction

The previous exact Cayley-geometric reduction of the second pole produced a
finite polynomial in U of degree roughly 8 before the approximation error
became comfortably small.

The present construction removes the second pole by a **one-sided global
majorant** instead.

There is:

- no geometric truncation error;
- no second spectral point;
- no z derivative;
- only U, U^2, U^3.

The price is a controlled loss in the model margin.

## 7. Use the two-pole wrapper only where it is strongest

Do **not** discard the matched two-pole consumer.

Its simple-pole representation has the good O(1/R) long-displacement
constant

    C_match
      ~= 2.1728342265.

So the recommended proof order is:

1. compare the full matrix H with the fixed-band H_R using f_match itself:

       tau f_match(H)
         >=
         tau f_match(H_R)
         - C_match/R
         + o(R^-1);

2. on H_R, use the pointwise inequality

       f_match(H_R)
         >=
         I-p_3(U_R);

3. prove

       tau p_3(U_R)

   stays below the remaining record threshold.

This preserves the excellent two-simple-pole tail conditioning while making
the **arithmetic/local theorem consume only three powers of one Cayley
unitary**.

## 8. Exact theorem target after band truncation

For fixed R,

    boxed:

    tau f_match(H)

      >=
      1
      -
      tau p_3(U_R)
      -
      C_match/R
      + o(1).

Therefore a sufficient condition for the record crossing is

    boxed:

    limsup_T
      tau p_3(U_{T,R})

      <
      0.163249981456072...
      -
      C_match/R,

for some fixed sufficiently large R.

At the model benchmark,

    E p_3
      =
      0.1388930951677425...,

so before allocating band error the available budget is

    0.0243568862883296....

For example, taking R large enough that C_match/R uses only part of this
budget leaves a positive arithmetic/local-law margin.

## 9. Displacement rank of the consumed observables

At z=i,

    rank[D,U]
      <=2.

Therefore

    rank[D,U^k]
      <=2k,

so the entire degree-3 consumer has displacement rank at most six at the
highest power.

The local theorem now needs only the bounded quantities

    tau(U),
    tau(U^2),
    tau(U^3)

or, preferably, their one combined positive/majorant functional p_3(U).

No global limiting spectral law is required.

## 10. Evidence boundary

Closed here:

- exact global degree-3 Cayley majorant;
- exact Sturm positivity certificate;
- exact pinned-model expectation;
- exact residual record margin;
- reduction of the post-band theorem to U,U^2,U^3.

Still open:

- theorem-grade transport/local arithmetic for the degree-3 bounded Cayley
  observable on the actual fixed-band sharp zeta matrix.

This is now a smaller target than the previous degree-8 bounded-unitary
hierarchy.

See:

    notes/WP84_TWO_POLE_MATCHED_CAYLEY_FILTER.md
    notes/WP84_TWO_POLE_CAYLEY_FINITE_REDUCTION.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md

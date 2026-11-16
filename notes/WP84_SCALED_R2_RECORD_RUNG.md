# WP84 — scaled r2 one-point alternative first record rung

Date: 2026-10-05

Status: **MODEL/CONSUMER CERTIFICATE — ONE UPPER-HALF-PLANE POINT PLUS ONE z-DERIVATIVE; COMPETITIVE WITH F9 FOR THE FIRST RECORD CROSSING**

No unconditional zero-density percentage is claimed here.

The active F9 rung uses four simple poles and has model simple-zero ledger

    69.60486322...%

with minimum pole distance about 1.46336.

There is a second bounded route that is algebraically smaller.

## 1. A scaled support-free minorant

For a>0 define

    boxed:
    r_{2,a}(x)
      =
      1
      -
      [
        (x-a)^2/(x^2+a^2)
      ]^2.

For x<=0,

    (x-a)^2-(x^2+a^2)
      = -2ax >=0,

so

    r_{2,a}(x)<=0.

For x>0 the ratio lies in [0,1), so

    0<r_{2,a}(x)<=1.

Therefore

    boxed:
    1_{x>0} >= r_{2,a}(x)

for every real x and every a>0.

Also the ratio

    (x-a)^2/(x^2+a^2)

lies in [0,2], hence

    boxed:
    -3 <= r_{2,a}(x) <= 1.

Thus the consumer is globally bounded and Proposition-R safe.

## 2. Exact two-double-pole formula

Scaling the a=1 partial fraction identity gives

    boxed:

    r_{2,a}(x)
      =
      a(2+i)/(x-ia)
      - a^2/(x-ia)^2

      + a(2-i)/(x+ia)
      - a^2/(x+ia)^2.

For a Hermitian H and

    m_H(z)=tau((H-zI)^(-1)),

we obtain

    boxed:

    tau r_{2,a}(H)

      =
      2 Re[
        a(2+i)m_H(ia)
        - a^2 m_H'(ia)
      ].

So the whole bounded consumer is determined by:

- one upper-half-plane point z=ia;
- its first z-derivative.

No continuum of spectral parameters is required.

## 3. Exact model value at a=3/2

Against the current four-node extremal quadrature determined by the pinned
six-moment model, exact polynomial reduction modulo the Christoffel cubic
gives

    boxed:

    q_{3/2}
      =
      506616611216431521048
      /
      593746460699485818169

      =
      0.8532541156027985... .

The corresponding model simple-zero ledger is

    boxed:

    2 q_{3/2}-1

      =
      419486761733377223927
      /
      593746460699485818169

      =
      0.706508231205597... .

Thus this model rung is about

    70.65082312%.

Again: this is a model/consumer value, not an unconditional theorem.

## 4. Record threshold and margin

To beat the audited comparison

    C_rec=0.673500037,

the positive-index consumer only needs

    tau r_{2,3/2}(H_T)
      >
      (1+C_rec)/2

      =
      0.8367500185.

The model margin is therefore

    boxed:
    0.8532541156027985
      - 0.8367500185

      =
      0.0165040971027985....

This is larger than the F9 bounded-consumer margin

    0.011274297609422....

The pole distance is also slightly larger:

    r2,a=3/2:
        |Im z|=1.5;

    F9:
        min |Im z_j|
          ~=1.46336065.

## 5. Tradeoff versus F9

Advantages of r_{2,3/2}:

- one upper-half-plane spectral point instead of two conjugate pairs;
- pole distance 1.5;
- larger model consumer margin than F9;
- globally bounded in [-3,1];
- direct support-free minorant of 1_{x>0};
- only m(z) and m'(z).

Disadvantage:

- the poles are double, so a z-derivative is consumed.

This is not a serious new state variable in the current architecture because:

- all resolvent state formulas are analytic in z;
- the Bernoulli drift-elimination equation can be differentiated once;
- alternatively m'(ia) can be controlled by a fixed small Cauchy circle
  around ia.

Thus r_{2,3/2} should be kept as a serious parallel first theorem rung.

## 6. Tail/background transfer

Write

    t_a(x)=2ax/(x^2+a^2).

Then

    r_{2,a}(x)
      = 2 t_a(x)-t_a(x)^2,

with

    |t_a(x)|<=1.

Since

    |d(2t-t^2)/dt|<=4

for t in [-1,1], and

    |t_a'(x)|<=2/a,

we have the global Lipschitz bound

    boxed:
    Lip(r_{2,a}) <= 8/a.

At a=3/2,

    Lip(r_{2,3/2}) <= 16/3.

Therefore the existing trace-norm background/tail quarantine transfers
directly to this consumer.

## 7. Relation to the new drift-elimination equation

The Bernoulli self-consistency identity now gives

    t partial_t m
      + m
      + (z-s_0)m_z
      =
      -t B_t
      +o(1).

Differentiating once in z closes the pair

    m(3i/2),
    m'(3i/2)

against the same already-explicit D2 state functional and its z-derivative.

So this rung does not require reopening the first-order prime drift.

## 8. Decision rule

Do not discard F9.

Instead run the remaining analytic state estimate against both:

A. F9:
   four simple poles,
   no pole derivatives,
   model simple ledger 69.6049%.

B. r_{2,3/2}:
   one upper-half-plane double pole,
   one derivative,
   model simple ledger 70.6508%.

Whichever gives the cleaner theorem-grade state bound should become the first
record crossing.

The six-pole 79.62709668% rung remains the stronger second-stage target.

Companion exact checker:

    src/wp84_scaled_r2_record_rung.py

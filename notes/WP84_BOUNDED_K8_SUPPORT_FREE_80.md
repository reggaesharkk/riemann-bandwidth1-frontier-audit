# WP84 — bounded support-free k=8 consumer beyond 80%

Date: 2026-10-05

Status: **CONSUMER-SIDE >80 BOUNDED ROUTE CLOSED; ARITHMETIC ONE-SIDED m7/m8 TRANSPORT OPEN**

The degree-4 Christoffel gate previously gave a conditional >80 route under
one-sided information

    m7 >= L,
    m8 <= U,

with

    L>L0,
    U<T80(L).

That result was originally phrased for a measure supported on [0,infinity).
The sign structure of the exact minimizer actually gives a stronger
support-free statement and admits a bounded rational consumer.

## 1. Feasible parametrization

Write

    L = L0+t,
    t>=0,

and

    U = F8(L)+eta,
    eta>=0.

Let

    Q(x)=1+q1 x+q2 x^2+q3 x^3+q4 x^4

be the exact degree-4 Christoffel minimizer built from the surrogate moments
(L,U).

In the positive-definite feasible region D(L,U)>0, exact elimination gives
the coefficient numerators

    N1
      = -(11025/283)
          [12290124 eta
           +129018960 t^2
           +3931153 t],

    B2
      = -(15120/283)
          [889186 eta
           +12983040 t^2
           +1024177 t],

    N3
      = -(1080/283)
          [227815 eta
           +4057200 t^2
           +889186 t],

    N4
      = 1352400 t.

Because

    q1 = 12 N1/D,
    q2 = -105 B2/D,
    q3 = 1470 N3/D,
    q4 = 945 N4/D,

we obtain throughout the one-sided feasible region

    boxed:
    q1<=0,
    q2>=0,
    q3<=0,
    q4>=0.

For every u>=0,

    Q(-u)
      = 1 - q1 u + q2 u^2 - q3 u^3 + q4 u^4
      >= 1.

Hence

    boxed:
    Q(x)^2>=1
      for every x<=0.

No support restriction on the spectral measure is needed.

## 2. One-sided moment consumption remains sign-safe

Let

    G(x)=Q(x)^2
      = sum_{k=0}^8 y_k x^k.

The exact coefficient signs are

    y7=2 q3 q4 <=0,
    y8=q4^2 >0

away from the flat point.

Therefore if the actual law has the pinned moments through m6 and satisfies

    m7_actual >= L,
    m8_actual <= U,

then

    integral G dnu_actual
      <= integral G dnu_surrogate
      = lambda4(L,U).

Thus

    nu_actual((-infinity,0])
      <= lambda4(L,U).

Whenever

    U<T80(L),

we have

    lambda4(L,U)<1/10,

so

    positive spectral mass > 0.9

and the exact zero-side counting ledger gives

    boxed:
    simple-zero coefficient > 0.8.

This is now a support-free spectral statement.

## 3. Bounded rationalization

For any fixed delta>0 define

    F_{delta;L,U}(x)
      = (delta+1) G(x)/(G(x)+delta).

Since G(x)>=1 on x<=0,

    F_{delta;L,U}(x)>=1
      on the whole nonpositive half-line.

Let

    h_delta(t)
      = (delta+1)t/(t+delta).

This function is increasing and concave for t>=0.  Jensen therefore gives

    integral F_{delta;L,U} dnu_actual
      <= h_delta(
           integral G dnu_actual
         )
      <= h_delta(lambda4(L,U)).

Thus the bounded consumer yields >80 whenever

    h_delta(lambda4)<1/10.

Solving exactly,

    boxed:
    delta
      > 9 lambda4/(1-10 lambda4).

So every strict unbounded >80 certificate automatically admits a **finite
fixed bounded rational >80 consumer**.

No delta(T) limit is required.

## 4. Exact midpoint example

At

    L=19.136,

and

    U=(F8(L)+T80(L))/2,

the exact surrogate Christoffel value simplifies to

    lambda4
      = 1415/14409
      = 0.0982025123....

The bounded >80 threshold is

    delta
      > 49.169884....

Therefore delta=50 already works.

Its Jensen cap is

    14433/144373
      = 0.0999702160...,

and the exact simple-zero ledger is

    boxed:
    115507/144373
      = 0.8000595679...
      > 80%.

Larger fixed delta recovers more of the conditional unbounded margin.

## 5. Eight fixed nonreal poles

For fixed (L,U,delta), the denominator

    Q(z)^2+delta

has degree eight and no real roots because Q(x)^2>=0 on R.

For generic fixed delta the roots are simple.  At the exact midpoint example
with delta=50, numerical diagnostics give eight simple poles with

    min |Im z_j|
      ~= 0.6878068.

Thus the conditional >80 theorem can also be posed entirely as a fixed
bounded resolvent problem.

## 6. Strategic consequence

The bounded-resolvent architecture is not intrinsically capped at 79.627%.

There are now two bounded consumer rungs:

1. **k<=6 unconditional model rung**
       -> frontier 79.62709668...%;

2. **k=8 one-sided rung**
       -> strictly above 79.627% whenever m7 moves above its flat floor,
       -> above 80% when U<T80(L).

The second rung requires new arithmetic information: a transported lower
bound for m7 and upper bound for m8 in the limiting/model state.

No >80 zeta theorem is claimed until those analytic inequalities are proved.

Companion exact checker:

    src/wp84_bounded_k8_support_free_80_gate.py

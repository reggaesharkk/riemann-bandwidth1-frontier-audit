# WP84 — Jensen sharpening and the optimal bounded Christoffel consumer

Date: 2026-10-05

Status: **FULL 79.627 CHRISTOFFEL COEFFICIENT HAS A BOUNDED CONTINUOUS CONSUMER; RATIONAL FAMILY CONVERGES TO IT**

Let

    g(x)=P(x)^2,

with

    integral g dnu
      = w0
      = 1415/13891
      < 1,

and

    g(x)>=1 for x<=0.

The previously introduced rational family

    F_delta(x)
      = (delta+1) g(x)/(g(x)+delta)

is one bounded approximation to a stronger canonical consumer.

## 1. Exact bounded optimum

Define

    F_star(x)
      = min(g(x),1).

Then

    0<=F_star<=1

on the whole real line.

Because g(x)>=1 for x<=0,

    boxed:
    F_star(x)=1
      for x<=0.

Therefore

    nu((-infinity,0])
      <= integral F_star dnu.

Even more directly,

    F_star(x)<=g(x)

pointwise.  Therefore

    integral F_star dnu
      <= integral g dnu
      = w0.

Concavity of h(t)=min(t,1) gives the same inequality by Jensen, but is not needed for this clipped optimum.

Hence

    boxed:
    nu((-infinity,0])
      <= 1415/13891

using a **bounded continuous consumer**.

The exact zero-side ledger therefore yields immediately

    boxed:
    simple-zero coefficient
      >= 11061/13891
      = 79.62709668... percent

at the model-consumption level.

No unbounded observable is intrinsically required by the consumption step.

## 2. Optimality and the Markov--Krein interpretation

The clipped bound equals the degree-6 Markov--Krein extremal mass at the nonpositive half-line: the Christoffel measure attains the same cap w0.  So the bounded clipping loses no certificate strength.\n\nLet h:[0,infinity)->[0,1] be concave with

    h(t)>=1 for t>=1

and h(t)>=0.

Then h(1)=1 and concavity between 0 and 1 implies

    h(t)>=t

for 0<=t<=1.

Therefore at w0,

    h(w0)>=w0.

So F_star=min(g,1) attains the smallest possible Jensen cap among bounded
concave scalarizations of the exact Christoffel square.

This explains why the full 79.627 coefficient is the natural bounded
frontier of this degree-6 certificate.

## 3. Rational family Jensen sharpening

For

    h_delta(t)
      = (delta+1)t/(t+delta),

h_delta is increasing and concave on t>=0.

Therefore the universal model bound is sharper than the earlier pointwise
comparison:

    integral F_delta dnu
      <= h_delta(w0)

      = (delta+1)w0/(delta+w0).

The corresponding simple-zero ledger is

    S_J(delta)
      = 1 - 2 (delta+1)w0/(delta+w0).

Examples:

    delta=61
      -> 79.32763565... percent,

    delta=752
      -> 79.60276803... percent,

    delta=2871
      -> 79.62072365... percent,

    delta=9717
      -> 79.62521365... percent.

Again

    S_J(delta)
      increases to
        11061/13891.

## 4. Relation to the theorem interface

F_star is bounded and continuous but not analytic at the six real points
where

    P(x)^2=1.

It is therefore not as convenient as F_delta for a one-shot finite resolvent
identity.

The rational family remains the preferred theorem interface because each
fixed delta has only six simple poles away from the real axis.

But the target bound should use the sharper Jensen cap

    h_delta(w0),

not merely

    (1+1/delta)w0,

once comparison to the pinned-moment model law is established.

## 5. Approximation route to F_star

Since F_star is bounded and continuous, it may also be approached uniformly
by bounded rational functions with poles a fixed positive distance from the
real axis.

Thus a sufficiently general fixed-resolvent convergence theorem would imply
convergence of tau(F_star(H_T)) directly by approximation, and recover the
full 79.627 coefficient without taking an unbounded observable limit.

This is a secondary route; the six-pole F_delta family remains the simpler
current analytic target.

No unconditional >79 theorem is claimed.

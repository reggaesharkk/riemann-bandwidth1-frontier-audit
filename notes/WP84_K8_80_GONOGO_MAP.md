# WP84 — k=8 >80 go/no-go map

Date: 2026-10-05

Status: **EXACT CONSUMER GEOMETRY; MODEL m7/m8 LOCATION STILL UNKNOWN**

The order-4 one-sided gate is narrow.  It is therefore worth isolating the
required model location before spending analytic effort on transport.

## 1. Exact corridor coordinates

Write

    L = L0+t,

and parameterize the eighth moment by its exact feasibility floor:

    m8 = F8(L)+eta,
    eta>=0.

The >80 condition is exactly

    boxed:
    eta
      < C t^2,

where

    C = 2666160/10471
      = 254.62324515328....

Thus the entire geometry is summarized by one quadratic cone.

Equivalently,

    boxed:
    t
      > sqrt(eta/C).

Selected tolerances:

    eta=0.001
      -> t>0.0019816...,

    eta=0.005
      -> t>0.004431...,

    eta=0.010
      -> t>0.006266...,

    eta=0.020
      -> t>0.008862...,

    eta=0.023
      -> t>0.009502....

Since

    19.136-L0
      = 0.00965498...,

the diagnostic upper-endpoint lift permits at most about

    eta=0.02373565....

This quantifies how close the model eighth moment must lie to the Schur
feasibility floor.

## 2. Cheap model-side go/no-go

Before any theorem-grade k=8 transport, obtain the **model-side** pair

    (m7_model,m8_model)

with sufficient numerical or exact confidence to evaluate

    lambda4(m7_model,m8_model).

Then:

    lambda4 >= 1/10
      -> this degree-4 consumer cannot prove >80,
         regardless of transport quality;

    lambda4 < 1/10
      -> bounded fixed-resolvent >80 consumers exist.

The latter case still requires arithmetic transport, but it justifies the
investment.

## 3. Bounded-margin ladder at the midpoint diagnostic

At

    L=19.136,
    U=(F8(L)+T80(L))/2,

we have exactly

    lambda4=1415/14409.

The bounded rational consumer gives:

    delta=50
      -> 80.00595679...%,

    delta=60
      -> 80.06478397...%,

    delta=100
      -> 80.18255374...%,

    delta=200
      -> 80.27098222...%,

    delta=500
      -> 80.32408098...%,

    delta=1000
      -> 80.34178752...%,

    delta=5000
      -> 80.35595525...%.

Thus delta=50 is only a proof-of-principle crossing with a tiny margin.
A practical theorem should choose a larger fixed delta after the model point
is known.

## 4. Current evidence status

The public higher-rung record only places the model reconnaissance in a narrow
m7 band and does not supply an exact closed m8 value.

The exact C7 and {5,2} programs therefore remain useful not because the
consumer is missing, but because they can decide whether the true model point
actually lies inside the >80 cone.

No >80 zeta theorem is claimed.

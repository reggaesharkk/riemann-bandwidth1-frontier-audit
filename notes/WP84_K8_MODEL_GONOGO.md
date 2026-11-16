# WP84 — k=8 exact model go/no-go gate

Date: 2026-10-05

Status: **CONSUMER GATE READY; EXACT MODEL m7/m8 NOT YET AVAILABLE IN THE WORKING RECORD**

The bounded support-free k=8 architecture can exceed 80%, but only if the
actual limiting/model pair lies inside the exact one-sided corridor.

Before spending analytic effort on transport, the cheapest decisive test is:

    compute the exact model m7 and m8,
    then evaluate lambda4(m7,m8).

Companion evaluator:

    src/wp84_k8_model_gonogo.py

## 1. Exact decision rule

Given exact model values M7,M8, compute

    F8(M7)
      = moment-matrix feasibility floor,

    T80(M7)
      = exact >80 upper threshold.

Then:

    if M8 >= T80(M7):
        this degree-4 Christoffel consumer cannot reach 80%;

    if F8(M7) <= M8 < T80(M7):
        lambda4(M7,M8)<1/10
        and the consumer clears 80%.

For a bounded rational consumer, if lambda4<1/10 it is enough to choose fixed

    delta
      > 9 lambda4/(1-10 lambda4).

## 2. The corridor is genuinely narrow

The exact width is

    T80(L)-F8(L)
      = (2666160/10471)(L-L0)^2,

where

    L0=25866469/1352400
      = 19.126345016267....

Representative widths are:

    L=19.127  -> 0.0001092343
    L=19.128  -> 0.0006974057
    L=19.130  -> 0.0034014880
    L=19.132  -> 0.0081425563
    L=19.134  -> 0.0149206105
    L=19.136  -> 0.0237356507.

Thus the exact model value of m7 matters strongly.  Near the flat floor, even
a tiny m8 excess above F8 can kill the >80 rung.

Equivalently, if

    eta=M8-F8(M7),

then >80 requires

    eta
      < (2666160/10471)(M7-L0)^2.

For planning:

    eta=0.001
      requires
        M7-L0 > 0.00198176...;

    eta=0.005
      requires
        M7-L0 > 0.00443135...;

    eta=0.010
      requires
        M7-L0 > 0.00626687....

## 3. Why the go/no-go cannot yet be executed honestly

The currently pinned public/model record contains:

- exact moments through m6;
- an identification-grade C7 value;
- a reconnaissance m7 interval reaching about 19.136;
- a reported k=8 payoff range roughly 0.797--0.802.

It does **not** supply an exact model pair (m7,m8) at proof grade.

In the private attack tree, the missing model-side objects are exactly the
ones already isolated:

- exact C7 completion;
- exact mixed {5,2} contribution;
- exact m8 mixed classes {2^4}, {4,2,2}, {4,4}, {6,2}.

Therefore no exact >80 model verdict is recorded yet.

## 4. Promotion rule

As soon as the exact model pair is assembled, run

    python src/wp84_k8_model_gonogo.py --m7 NUM/DEN --m8 NUM/DEN

before starting any new k=8 arithmetic transport.

PASS:
    the model itself lies below T80 and transport is worth attacking.

FAIL:
    the model lies at or above T80; abandon this consumer and redesign the
    k=8 bounded test function before spending transport effort.

This is deliberately a model-first falsifier.

No >80 arithmetic theorem is claimed.

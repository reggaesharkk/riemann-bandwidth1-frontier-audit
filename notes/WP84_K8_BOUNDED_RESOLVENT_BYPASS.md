# WP84 — bounded k=8 resolvent route does not require arithmetic raw-moment transport

Date: 2026-10-05

Status: **STRATEGIC REDUCTION CLOSED; MODEL m7/m8 STILL NEEDED TO CHOOSE THE CONSUMER; ARITHMETIC SIDE CAN STAY BOUNDED**

The one-sided k=8 moment gate was originally formulated as an arithmetic task:

    prove m7_arith >= L,
    prove m8_arith <= U<T80(L).

That route is sufficient, but it is not necessary once the bounded resolvent
architecture is available.

## 1. Model side and arithmetic side can be separated

Suppose the exact limiting/model law has exact moments

    M7, M8

and these satisfy

    M8<T80(M7).

Then the degree-4 Christoffel minimizer

    Q_model

built from the exact model pair has

    lambda4_model
      = integral Q_model(x)^2 dnu_model
      < 1/10.

The exact alternating coefficient signs give

    Q_model(x)^2>=1
      for x<=0.

Now fix any delta satisfying

    delta
      > 9 lambda4_model/(1-10 lambda4_model),

and define the bounded rational consumer

    F_model,delta(x)
      = (delta+1) Q_model(x)^2
          /(Q_model(x)^2+delta).

Then

    F_model,delta(x)>=1
      for x<=0,

and, by concavity,

    integral F_model,delta dnu_model
      <= h_delta(lambda4_model)
      < 1/10.

This consumer has eight fixed nonreal poles.

## 2. Arithmetic theorem target

The arithmetic side need not prove finite-T raw seventh or eighth moments.

It is enough to prove the bounded comparison

    boxed:
    tau_d F_model,delta(H_T)
      <= integral F_model,delta dnu_model
         + o(1).

Equivalently, using the partial-fraction decomposition of F_model,delta, it
suffices to prove convergence/comparison at its eight fixed nonreal poles.

The exact simple-zero ledger then gives

    liminf simple-zero proportion
      > 0.8.

Thus the Proposition-R raw-moment firewall remains intact.

## 3. What exact model m7/m8 are still needed for

The exact model pair remains valuable because it decides the consumer before
the arithmetic proof begins.

It answers the cheap go/no-go question:

    is lambda4_model < 1/10?

If NO, the degree-4 k=8 consumer is dead.

If YES, freeze Q_model and one finite delta, then forget arithmetic raw m7/m8
and attack only the bounded resolvent law.

## 4. Why this is stronger than one-sided arithmetic moment transport

The one-sided moment route must control an extremely narrow m8 corridor.

The bounded-resolvent route only needs the **model** to lie in that corridor.
Once the model consumer is frozen, the arithmetic theorem compares one bounded
functional directly.

Rare rank-o(d) arithmetic outliers can therefore be deleted without
contaminating raw seventh/eighth moments.

## 5. Current sequencing

The correct >80 sequence is now:

1. finish the exact model C7 / {5,2} / m8 ledgers;
2. run the exact model go/no-go gate;
3. if PASS, freeze the eight-pole bounded consumer;
4. reuse the retained-range rank-robust resolvent machinery directly;
5. do not open a separate finite-T raw m7/m8 transport branch unless the
   bounded route itself fails.

This is the preferred >80 architecture.

No >80 arithmetic theorem is claimed.

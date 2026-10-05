# WP84 — bounded four-pole record-beating rung

Date: 2026-10-05

Status: **MODEL/CONSUMER CERTIFICATE CLOSED; FOUR-POLE ARITHMETIC TRANSPORT OPEN; PRIORITY RECORD-BEATING RUNG**

No unconditional zeta percentage is claimed in this note.

The six-pole degree-6 Christoffel consumer remains the route to the
79.62709668... model coefficient.  But the hostile audit suggests that the
best first theorem target is a lower-degree bounded consumer with fewer poles,
larger pole distance, and a much larger margin over the currently audited
67.28--67.35% frontier.

That rung already exists using only the first four model moments.

## 1. Degree-2 half-line certificate

Use

    m0=1,
    m1=1,
    m2=4/3,
    m3=2,
    m4=13/4.

The degree-2 Christoffel minimizer at zero is

    boxed:
    P2(x)
      = 1 -(7/4)x +(2/3)x^2.

Direct exact arithmetic gives

    boxed:
    integral P2(x)^2 dnu = 5/36.

For x=-u<=0,

    P2(-u)=1+(7/4)u+(2/3)u^2 >= 1.

Therefore the certificate is support-free:

    nu((-infinity,0]) <= 5/36,

so the model positive-index floor is

    31/36 = 86.111111...%.

The corresponding simple-zero ledger in the unbounded limit is

    1 - 2*(5/36)
      = 13/18
      = 72.222222...%.

This is a consumer/model statement only.

## 2. Bounded four-pole family

For every fixed delta>0 define

    boxed:
    F_delta^(4)(x)
      = (delta+1) P2(x)^2
          / (P2(x)^2+delta).

Because P2(x)^2>=1 for x<=0,

    F_delta^(4)(x)>=1
    on the nonpositive half-line.

Put

    h_delta(t)=(delta+1)t/(t+delta).

This function is increasing and concave for t>=0.  Jensen therefore gives

    integral F_delta^(4) dnu
      <= h_delta(5/36)
      = 5(delta+1)/(36 delta+5).

The exact simple-zero model ledger is

    boxed:
    S4(delta)
      = 1 - 10(delta+1)/(36 delta+5)
      = (26 delta-5)/(36 delta+5).

Examples:

    delta=5   -> 25/37   = 67.567567...%
    delta=6   -> 151/221 = 68.325791855...%
    delta=7   -> 177/257 = 68.871595...%
    delta=10  -> 51/73   = 69.863013...%
    delta=20  -> 103/145 = 71.034482...%
    delta=30  -> 5/7     = 71.428571...%

and

    sup_delta S4(delta)=13/18.

Thus one bounded theorem schema would recover the old 72.222... fourth-order
headline without ever asserting a finite-T raw fourth moment.

## 3. Delta=6 is a clean first record target

At delta=6,

    model simple ledger
      = 151/221
      = 68.325791855...%.

This lies above both audited comparison levels:

    67.28005676...%  (A1290/A1294-class public/formalized level),
    67.3500037...%   (later audited bandwidth-one certificate level).

The model margins are about

    +1.045735 percentage points over 67.28005676...,
    +0.975788 percentage points over 67.3500037....

The point is not the decimal itself.  It is that the bounded theorem has
almost a full percentage point of simple-zero budget while using only four
fixed poles.

## 4. Exact pole geometry at delta=6

The poles solve

    P2(z)^2+6=0.

Equivalently

    P2(z)= +/- i sqrt(6).

After multiplying by 12,

    8 z^2 -21 z +12(1 -/+ i sqrt(6))=0,

so the quadratic discriminants are

    57 +/- 384 i sqrt(6).

If

    sqrt(57+384 i sqrt(6))=u+i v,

then

    v^2
      = [sqrt(57^2+384^2*6)-57]/2
      = [sqrt(887985)-57]/2.

Every pole has

    |Im z|=v/16.

To prove |Im z|>1 it is enough to show

    sqrt(887985)>569,

which is immediate from

    887985 > 569^2.

Numerically the minimum pole distance is

    min |Im z_j|
      ~= 1.3149750177.

There are exactly four simple poles.  The derivative P2' vanishes only at
the real point 21/16, which cannot solve P2(z)=+/- i sqrt(6).

So the delta=6 rung is better conditioned off the real axis than the
six-pole delta=61 baseline.

## 5. Proposition-R firewall

This rung must **not** be proved by extracting the finite-T theta^4
coefficient or by proving a raw fourth-moment upper bound.

The theorem target is the fixed bounded rational functional

    tau F_6^(4)(H_T),

equivalently one weighted combination of four fixed nonreal resolvents.

That remains rank-robust to an o(d)-rank family of arbitrarily large
off-line outliers.

Order four is used only as a limiting-generator consistency gate:

    pair layer      = 4/15,
    connected core  = -1/60,
    centered m4     = 1/4.

## 6. Why this should be attacked before the six-pole 79.627 rung

The four-pole target has:

- fewer consumed resolvents: 4 instead of 6;
- a clean exact parameter delta=6;
- minimum pole gap about 1.315 rather than just above 1;
- an approximately one-percentage-point margin over the audited
  67.28--67.35 frontier;
- the same rank-robust bounded-functional architecture;
- the same prime-base grouping, LRSC displacement-rank, boundary quarantine,
  and product-correlation machinery already built for WP84.

It does **not** remove the connected-state arithmetic problem.  It makes the
first theorem-grade crossing substantially more forgiving.

## 7. Attack order

The recommended order is now:

    bounded four-pole delta=6
      -> close arithmetic D1/D2 comparison
      -> obtain the first genuinely record-beating bounded-rung theorem
         if the comparison passes
      -> generalize in fixed delta toward 13/18
      -> transfer the same machinery to the six-pole degree-6 family
      -> target 79.62709668...%.

The project should not spend scarce compute on higher model rungs until this
lower-pole theorem interface has been exhausted.

Companion exact checker:

    src/wp84_four_pole_record_rung.py

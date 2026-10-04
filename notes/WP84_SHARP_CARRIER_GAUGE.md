# WP84 — sharp carrier gauge: the T-phase is not arithmetic randomness

Date: 2026-10-05

Status: **EXACT SHARP-MODEL UNITARY GAUGE IDENTIFIED; FAST/RESONANT PHASE LANGUAGE IS REPRESENTATION-DEPENDENT**

The four-channel algebra in WP84_VARIANCE_TOEPLITZ_RULES is correct.  But the interpretation of the exp(+/- i T y) carriers needs a crucial correction in the sharp physical model.

## 1. Sharp complex block

With s=y/L in [0,1], the sharp physical block is

    Cplus_T(s) = 2*pi * exp(i T y) * U_s^+,
    Cminus_T(s)= 2*pi * exp(-i T y) * U_s^-,

where U_s^+ is the partial translation f(x)->1_{x<=1-s}f(x+s), and U_s^- is its adjoint.

## 2. One unitary removes every carrier simultaneously

Define on L2[0,1]

    (Q_T f)(x)=exp(i T L x) f(x).

Then

    Q_T^* U_s^+ Q_T = exp(i T L s) U_s^+ = exp(i T y) U_s^+,

and

    Q_T^* U_s^- Q_T = exp(-i T y) U_s^-.

Therefore

    boxed:
    Cplus_T(s)=2*pi Q_T^* U_s^+ Q_T,
    Cminus_T(s)=2*pi Q_T^* U_s^- Q_T.

The same Q_T works for every prime power because y=L s.

Consequently the entire sharp prime operator is unitarily equivalent to a carrier-free sum of partial shifts.

Companion exact finite partial-shift gate:

    src/wp84_sharp_carrier_gauge.py

## 3. Consequence for the variance split

The labels 'fast carrier' and 'resonant carrier' are algebraically useful in the original Gabor basis, but the macroscopic T phase is not an invariant source of cancellation.  In the sharp model it is a gauge.

Therefore no theorem may close V-sum or drift merely by appealing to exp(+/-2iTy) or exp(+/-iTy) oscillation.

The invariant reason those branches vanish in WP84_SHARP_RESOLVENT_TRACE is different: when the resolvent belongs to the multiplication algebra, same-sign products are nonzero partial translations with zero normalized diagonal trace.

That geometric statement survives the gauge change.

## 4. Carrier-free sharp prime operator

Up to the common unitary conjugation and the already recorded normalization, the sharp prime part has the form

    P_sharp = - sum_{n<=X} Lambda(n)/(a L sqrt(n))
                * (U_{s_n}^+ + U_{s_n}^-),

    s_n=log n/L.

This is a deterministic truncated-translation / Wiener-Hopf type operator, not a random-phase matrix.

Thus the remaining ALG-star problem should be formulated as a spectral-distribution theorem for this structured translation operator (plus scalar background), rather than as a high-frequency prime cancellation theorem.

## 5. Strategic correction

This removes one misleading possible shortcut and points to the correct operator algebra:

    sharp partial translations
      -> truncated convolution / Wiener-Hopf calculus
      -> normalized trace of bounded resolvents
      -> fixed-pole r_m consumer.

The ramp-transfer note already shows that the second-order consumed variance trace may be moved to the sharp model at o(1) cost.  The next audit should test whether a classical Wiener-Hopf/Szego trace theorem can be adapted to the T-dependent prime translation measure.

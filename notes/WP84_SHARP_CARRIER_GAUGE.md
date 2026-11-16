# WP84 — carrier gauge audit: infinite-space identity does not preserve the finite compression

Date: 2026-10-05

Status: **FINITE-COMPRESSION GAUGE SHORTCUT RETRACTED; INFINITE-SPACE IDENTITY RETAINED ONLY AS A DIAGNOSTIC**

The earlier note observed a correct identity on the full physical Hilbert
space but promoted it too far.

The finite Gabor matrix is a compression to a d-dimensional Fourier band.
The gauge multiplication that removes the carrier does **not** preserve that
band.  Therefore the carrier cannot simply be erased from the theorem-side
finite matrix.

## 1. Exact sharp complex block

With s=y/L, the sharp physical shift is

    U_s^+ f(x)
      = 1_{x in overlap(s)} f(x+s).

The finite complex block is the compression

    Cplus_T(s)
      = 2*pi e^(iTy)
          P_d U_s^+ P_d

in the physical Fourier representation, up to the frozen normalization and
coordinate convention.

The negative branch is the adjoint.

## 2. The full-space gauge identity is correct

On the full L2 interval define

    (Q_T f)(x)=e^(iTLx)f(x).

Then

    Q_T^* U_s^+ Q_T
      = e^(iTy) U_s^+.

So on the **uncompressed full space** the carrier may indeed be absorbed into
a modulation.

## 3. Why this is not a finite-matrix unitary equivalence

The Gabor compression uses

    P_d
      = projection onto d consecutive Fourier modes.

But Q_T shifts Fourier frequency by approximately

    TL/(2*pi)
      asymp d.

Consequently

    Q_T P_d Q_T^*
      != P_d.

In fact it moves the selected Fourier band to a different band.

Therefore

    P_d Q_T^* U_s Q_T P_d

is not obtained from

    P_d U_s P_d

by unitary conjugation **inside the same d-dimensional compressed space**.

The previous statement that one fixed unitary removes all prime carriers from
the finite theorem operator is invalid.

## 4. Correct finite theorem operator

The sharp finite prime operator must retain the scalar carriers:

    boxed:
    P_sharp
      = - sum_{n<=X}
          Lambda(n)/(a L sqrt(n))
          [
            e^(iT log n) P_d U_{s_n}^+ P_d
            + e^(-iT log n) P_d U_{s_n}^- P_d
          ],

    s_n=log n/L,

again up to the already frozen harmless constants.

Equivalently,

    e^(iT log n)=n^(iT).

These phases are part of the finite-compression arithmetic state.

## 5. What survives from the old note

Several later results do **not** depend on deleting the carriers:

1. boundary support/factorization:
   scalar unit-modulus carriers can be absorbed into the middle operator K;

2. crude operator norms:
   |e^(iTy)|=1, so every absolute norm bound is unchanged;

3. endpoint low-rank quarantine:
   unchanged;

4. global ramp-to-sharp boundary quarantine:
   unchanged after defining
       K_+=sum c_n e^(iTy_n)U_{y_n};

5. closed translation-word traces:
   when a signed displacement word closes,
       sum eps_j y_j=0,
   the total carrier is
       exp(iT sum eps_j y_j)=1.

Thus the fixed-degree resonance/overlap calculations remain valid.

## 6. What must be corrected strategically

The active theorem is **not** a carrier-free Wiener--Hopf problem.

It is a finite-band compressed, carrier-bearing truncated-translation problem.

Carrier oscillation may therefore be used if proved through the compressed
trace; it may not be dismissed as a pure gauge.

Likewise no same-sign branch may be killed by citing the full-space gauge.

## 7. Evidence boundary

This correction does not reopen the LRSC-inspired boundary quarantine.

It retracts only the stronger and unjustified finite-compression unitary
equivalence.

No unconditional >79 theorem is claimed.

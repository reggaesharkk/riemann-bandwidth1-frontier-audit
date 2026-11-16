# WP84 — four-pole inequality-only record kill gate

Date: 2026-10-05

Status: **ONE SCALAR BOUNDED INEQUALITY IS SUFFICIENT TO BEAT THE AUDITED 67.3500037 LEVEL; EXACT MODEL IDENTIFICATION IS NOT REQUIRED**

No new unconditional simple-zero percentage is claimed here.

The degree-2 bounded consumer at delta=9 is

    F9(x)
      = 10 P2(x)^2/(P2(x)^2+9),

with

    P2(x)=1-(7/4)x+(2/3)x^2.

It has four fixed simple nonreal poles and the support-free property

    F9(x)>=1 for x<=0.

## 1. Zero-side record threshold

If

    E_T = tau_d F9(H_T),

then the positive-index/simple-zero ledger gives asymptotically

    simple proportion >= 1-2 E_T

once the already-closed rank/tail transfers are inserted.

To beat the audited comparison level

    C_rec = 0.673500037,

it is enough to prove

    boxed:
    limsup E_T
      < U_rec
      := (1-C_rec)/2
      = 0.1632499815.

This is the theorem target.

It is weaker than proving convergence to the full model law.

## 2. Model/Jensen benchmark and available slack

The pinned first four model moments give

    integral P2^2 dnu = 5/36.

Because

    h_9(t)=10t/(t+9)

is increasing and concave,

    integral F9 dnu
      <= h_9(5/36)
      = 50/329
      = 0.1519756838905775....

Therefore the record-safe consumer budget is

    boxed:
    Delta_rec
      = U_rec - 50/329
      = 0.011274297609422... .

Equivalently the proof may lose more than one full percentage point in the
bounded consumer expectation relative to the Jensen model cap and still beat
67.3500037.

Against the 67.28005676 public/formalized comparison, the budget is slightly
larger.

## 3. Four fixed resolvents

The poles are

    z = [21 +/- sqrt(57 +/- 1152 i)]/16.

For

    F9(x)
      = 10 + sum_j c_j/(x-z_j),

the residues are

    c_j
      = -90/[2 P2(z_j) P2'(z_j)].

Numerically,

    min_j |Im z_j|
      ~= 1.4633606537,

and

    sum_j |c_j|
      ~= 21.20024.

Thus the exact theorem may be written as one scalar weighted-resolvent
inequality

    boxed:
    limsup_T [
      10 + sum_j c_j m_T(z_j)
    ]
      < 0.1632499815,

where

    m_T(z)=d^(-1) tr(H_T-zI)^(-1).

There is no requirement to prove each m_T(z_j) converges separately if the
weighted combination can be controlled directly.

## 4. Crude equal-error interpretation

Suppose, only for budgeting purposes, that a comparison law provides

    |m_T(z_j)-m_ref(z_j)| <= epsilon

at all four poles and that its F9 expectation is bounded by 50/329.

Then

    |Delta E|
      <= epsilon sum_j |c_j|.

The record budget allows roughly

    epsilon < 5.318e-4

before charging the already-vanishing boundary/background/cubic errors.

This is a crude sufficient condition, not the preferred theorem statement.
The preferred statement is the single weighted inequality in Section 3,
because conjugate-pole and generator cancellations can be kept intact.

## 5. What no longer has to be proved

For the first record crossing we do **not** need:

- a full limiting spectral distribution;
- all six pinned moments as arithmetic finite-T moments;
- C7 or the k=8 model program;
- pointwise convergence of four separate resolvents;
- a raw fourth-moment theorem;
- exact recovery of every connected constant if a one-sided weighted bound
  closes inside the available Delta_rec budget.

The exact order-four values remain fail-closed diagnostics for any proposed
generator, not mandatory intermediate theorem statements.

## 6. Active analytic object

Using the exact prime-base permutation-Lindeberg expansion,

    E_T - E_background
      = bounded D1
        + bounded D2
        + o(1),

with the current-block cubic mass already o(1).

The LRSC-derived displacement reduction expresses D1/D2 through:

- diagonal entries of B R;
- at most four displacement generators;
- the summable discrete kernel 1/(i-j)^2.

The next proof should therefore target the **weighted F9 combination**
directly and spend no effort proving a stronger law than the
0.0112742976 consumer budget requires.

## 7. Escalation rule

PASS at this rung means an actual unconditional record-beating theorem only
after every zero-side, rank, background, taper, and arithmetic hypothesis in
the repository has been source-closed.

If the four-pole inequality closes, the same generator theorem can then be
tightened in delta toward 13/18 and transferred to the six-pole
79.62709668... family.

See:

    notes/WP84_FOUR_POLE_RECORD_BEATING_RUNG.md
    notes/WP84_D1_D2_DISPLACEMENT_REDUCTION.md
    notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md

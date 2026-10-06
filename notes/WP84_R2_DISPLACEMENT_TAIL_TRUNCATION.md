# WP84 — bounded-consumer displacement-tail truncation

Date: 2026-10-05

Status: **EXACT MATRIX TAIL IDENTITY + SOURCE-CLOSED L2 CONTROL REDUCE THE PREFERRED r2 THEOREM TO FIXED DISPLACEMENT BANDWIDTH BEFORE ANY WORD EXPANSION**

No unconditional zero-density percentage is claimed here.

The preferred first record consumer is

    r2(x)
      = 1 - [ (x-1)^2/(x^2+1) ]^2,

with target

    liminf tau r2(H_T)
      > 0.8367500185439279....

The current Loewner representation is

    H
      = M_beta + [M_alpha,J],

up to the already-closed scalar background / boundary / taper errors, with

    J_ij=1/[pi(j-i)], i!=j.

This note shows that the long displacement tail |i-j|>R may be removed
*before* attacking the remaining state law.

The error tends to zero like R^(-1/2) for every globally Lipschitz bounded
consumer, uniformly after T->infinity.

This gives a theorem-grade route from the infinite displacement Loewner
matrix to a fixed-band matrix.

## 1. Fixed-band truncation

For an integer R>=1 define

    J^(R)_ij
      = J_ij  if 0<|i-j|<=R,
      = 0     otherwise,

and

    H^(R)
      = M_beta + [M_alpha,J^(R)].

The difference is purely off diagonal:

    Delta_R
      := H-H^(R)
      = [M_alpha, J-J^(R)].

Entrywise,

    (Delta_R)_ij
      =
      (alpha_i-alpha_j)/
      [pi(j-i)]

for |i-j|>R, and zero otherwise.

## 2. Exact normalized Hilbert--Schmidt tail bound

Because alpha is real,

    tau_d(Delta_R^2)
      =
      ||Delta_R||_F^2/d

      =
      1/(pi^2 d)
      sum_{|i-j|>R}
        |alpha_i-alpha_j|^2/(i-j)^2.

For each displacement r,

    sum_i
      |alpha_{i+r}-alpha_i|^2

      <=
      4 ||alpha||_2^2.

Hence

    tau_d(Delta_R^2)

      <=
      8/(pi^2)
      [ ||alpha||_2^2/d ]
      sum_{r>R} 1/r^2

      <=
      boxed:
      8/(pi^2 R)
      [ ||alpha||_2^2/d ].

This is deterministic and finite-d.

## 3. The full retained prime field has bounded normalized L2 mass

The full field is

    alpha_i
      = Im Q_*(tau_i).

After adaptive endpoint quarantine the retained integer range satisfies

    N/T=o(1).

The degree-two nonclosed leakage is therefore o(1) by the already-closed
m=1 sign-balance gate.

The same-sign carrier piece is o(1) by the already-closed high-frequency
prime-polynomial estimate.

The surviving diagonal prime-square contribution is

    1/2
    sum_p
      (log p)^2/(L^2 p)

      -> 1/4

in the sharp normalization a_phi->1.

Thus

    boxed:
    ||alpha||_2^2/d
      = 1/4 + o(1).

A weaker uniform O(1) bound also follows directly from the
Montgomery--Vaughan large sieve and is enough for the qualitative theorem.

Consequently

    boxed:
    limsup_T
      tau_d(Delta_R^2)
      <=
      2/(pi^2 R).

The exact 1/4 constant is useful for the error budget but is not needed for
the structural reduction.

## 4. Lipschitz spectral transfer

For Hermitian A,B, Hoffman--Wielandt gives ordered eigenvalues satisfying

    1/d
    sum_j
      |lambda_j(A)-lambda_j(B)|^2

      <=
      tau_d((A-B)^2).

Therefore every globally Lipschitz real f obeys

    |
      tau_d f(A)-tau_d f(B)
    |

      <=
      Lip(f)
      sqrt(
        tau_d((A-B)^2)
      ).

For r2,

    r2'(x)
      =
      -4 (x-1)^3 (x+1)/(x^2+1)^3.

The already-closed scaled-r2 derivative bound gives the fully elementary
global estimate

    Lip(r2)<=8.

(The exact optimum is smaller, but no optimization is needed here.)

Combining with Section 3 gives

    boxed:

    limsup_T
    |
      tau r2(H_T)
      - tau r2(H_T^(R))
    |

      <=
      (8 sqrt(2))/(pi sqrt(R)).

Thus

    lim_{R->infinity}
    limsup_{T->infinity}
    |
      tau r2(H_T)
      - tau r2(H_T^(R))
    |
      =0.

Long Loewner displacements are not part of the essential r2 theorem.

## 5. Rank quarantine of large alpha sites

The same reduction can make the fixed band uniformly bounded.

For M>0 define the bad set

    I_M
      = { i : |alpha_i|>M }.

By Section 3,

    |I_M|/d
      <=
      [||alpha||_2^2/d]/M^2
      =
      O(M^-2).

Let alpha^(M) be alpha clipped to [-M,M].

Then

    [M_alpha,J^(R)]
      -
    [M_alpha^(M),J^(R)]

is the sum of

    M_{alpha-alpha^(M)} J^(R)

and

    -J^(R) M_{alpha-alpha^(M)}.

The first matrix has nonzero rows only on I_M and the second has nonzero
columns only on I_M.  Therefore

    boxed:
    rank(
      [M_alpha,J^(R)]
      -
      [M_alpha^(M),J^(R)]
    )
      <= 2 |I_M|.

The preferred consumer r2 has total variation exactly 8:

    r2(-infinity)=0,
    r2(-1)=-3,
    r2(1)=1,
    r2(+infinity)=0.

The rank inequality for empirical spectral distributions therefore gives

    boxed:
    |
      tau r2(H^(R))
      -
      tau r2(H^(R,M))
    |
      <=
      16 |I_M|/d
      =
      O(M^-2),

where H^(R,M) uses the clipped alpha field.

An identical diagonal rank quarantine may be applied to beta if a later
locality argument requires a uniform diagonal bound.

## 6. Consequence: fixed-band, bounded-amplitude reduction

Take the limits in the order

    T -> infinity,
    then M -> infinity,
    then R -> infinity

(or choose large fixed R,M against the explicit record margin).

The preferred record theorem is equivalent, up to arbitrarily small bounded
consumer error, to the same theorem for a matrix with:

- fixed displacement bandwidth R;
- clipped alpha amplitude |alpha_i|<=M;
- optionally clipped beta amplitude;
- the same one-point r2 consumer.

This step is performed **before** any polynomial/word expansion, so it does
not revive the Proposition-R raw-moment problem.

## 7. Why this opens a finite-degree route if needed

For fixed R and bounded amplitudes, the truncated operator has bounded
off-diagonal row sum

    <=
    (4M/pi)
    sum_{r=1}^R 1/r.

After an optional beta clip, its full spectrum lies in a fixed compact
interval depending only on R and M.

Since r2 is analytic off the fixed poles +/-i, it may then be uniformly
approximated on that compact interval by a polynomial of finite degree n.

For a bandwidth-R matrix,

    tau p_n(H^(R,M))

depends only on closed walks of length <=n and displacement <=nR.

Therefore the all-degree bounded-resolvent theorem can, if necessary, be
reduced with explicit error accounting to a **finite-degree,
finite-displacement arithmetic problem**.

This is now a legitimate fallback route because:

1. bounded-consumer stability removed the long displacement tail first;
2. rank quarantine removed large amplitudes;
3. the polynomial degree is fixed only after the analytic error budget is
   chosen;
4. no finite-T unbounded raw moment is asserted.

## 8. Record-margin budgeting

The preferred a=1 model rung has positive-index margin

    0.0466326939503807...

above the audited record threshold.

A possible fail-closed allocation is:

    long displacement tail       < epsilon_band,
    amplitude rank quarantine    < epsilon_clip,
    compact polynomial/locality  < epsilon_poly,
    finite arithmetic transport  < epsilon_arith,

with

    epsilon_band
    + epsilon_clip
    + epsilon_poly
    + epsilon_arith

      < 0.04663269395.

No specific numerical R,M,n is frozen in this note because the next step
should optimize those constants before launching any heavy computation.

## 9. New frontier

The previous formulation asked for a limiting law of the full long-range
Gaussian/Loewner state.

That is stronger than necessary for the first record crossing.

The bounded r2 statistic only needs:

    fixed displacement band
      + bounded-amplitude state
      + finite local/finite-degree arithmetic control

after the theorem-grade limits above.

This is the preferred direction to test before attempting a global
matrix-Dyson theorem.

See:

    notes/WP84_R2_CAYLEY_DEFECT_GATE.md
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
    notes/WP84_TAPER_UNIVERSALITY_ADAPTIVE_ENDPOINT.md

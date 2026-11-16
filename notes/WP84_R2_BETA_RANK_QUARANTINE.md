# WP84 — beta-field rank quarantine and compact local reduction

Date: 2026-10-05

Status: **THE DIAGONAL FIELD MAY ALSO BE CLIPPED AT ARBITRARILY SMALL BOUNDED-CONSUMER COST; AFTER FIXED R,M,B THE LOCAL OPERATOR HAS A COMPACT SPECTRAL WINDOW**

No unconditional zero-density percentage is claimed here.

The preferred first-record consumer is

    r2(x)
      = 1 - [ (x-1)^2/(x^2+1) ]^2.

The previous two notes established:

1. long Loewner displacements may be discarded with vanishing r2-trace error;
2. large alpha sites may be removed by an o(d)-rank perturbation;
3. the remaining z=i resolvent is exponentially local even without bounding beta.

This note records a second option that is useful if we want to invoke a
finite polynomial/local-word theorem:

> the diagonal field beta also has bounded normalized L2 mass and can be
> clipped by rank.

So, at arbitrarily small r2 cost, the fixed-band matrix can be made uniformly
bounded in operator norm.

## 1. Full beta field

For an ordinary retained prime p write

    s_p = log p/L,

    c_p = -log p/(a_phi L sqrt p),

and

    beta_p(tau)
      = 2 c_p (1-s_p) cos(tau log p).

The full diagonal field is

    beta = sum_p beta_p

plus the already-negligible proper-prime-power correction.

## 2. Normalized beta square mass

Average beta_i^2 over the Fourier grid.

The p=q diagonal part contributes

    2
    sum_p
      c_p^2 (1-s_p)^2

because cos^2=(1+cos(2 theta))/2.

The same-sign cos(2 tau log p) part is a carrier-2T term and is o(1) by the
already-closed VK fast-channel estimate.

For p!=q, the difference-frequency term is a nonclosed degree-two word.
The m=1 finite-compression gate and N/T=o(1) kill it.  The sum-frequency
term is again in the already-closed fast channel.

Therefore

    (1/d)||beta||_2^2

      =
      2
      sum_p
        (log p)^2/(a_phi^2 L^2 p)
        (1-log p/L)^2

      + o(1).

The square-prime Mertens measure tends to s ds, so

    boxed:

    (1/d)||beta||_2^2
      ->
      (2/a_phi^2)
      int_0^1
        s(1-s)^2 ds
      =
      1/(6a_phi^2).

Since a_phi->1 in the sharp normalization,

    boxed:
    (1/d)||beta||_2^2
      =
      1/6 + o(1).

This matches independently the previously derived resonant covariance value

    C_bb(0)=1/6.

## 3. Clip beta by a diagonal rank perturbation

For B>0 define

    J_B
      = { i : |beta_i|>B }.

Chebyshev gives

    |J_B|/d
      <=
      [||beta||_2^2/d]/B^2
      =
      1/(6B^2)+o(1).

Let beta^(B) be beta clipped to [-B,B].

Then

    M_beta - M_beta^(B)

is diagonal and supported on J_B, hence

    rank(
      M_beta - M_beta^(B)
    )
      <= |J_B|.

The scalar r2 has total variation exactly 8:

    0 -> -3 -> 1 -> 0.

The standard finite-rank spectral-distribution inequality therefore gives

    boxed:

    |
      tau r2(H)
      -
      tau r2(H with beta clipped)
    |

      <=
      8 |J_B|/d

      <=
      4/(3B^2)+o(1).

So beta may be clipped after T->infinity at an arbitrarily small
bounded-consumer cost.

## 4. Combine with the alpha quarantine

From the previous displacement-tail note,

    ||alpha||_2^2/d
      =
      1/4+o(1).

If alpha is clipped to [-M,M], the commutator perturbation has rank at most

    2 |{i:|alpha_i|>M}|,

so

    boxed:

    r2 alpha-clip error
      <=
      4/M^2 + o(1).

Thus, after first choosing large fixed R,M,B, the theorem may be reduced to

    H_{R,M,B}

with:

    |i-j|<=R off diagonal,
    |alpha_i|<=M,
    |beta_i|<=B.

## 5. Compact spectral window

The off-diagonal row sum satisfies

    sup_i
    sum_{j!=i}
      |H_ij|

      <=
      (4M/pi) H_R,

where

    H_R=sum_{r=1}^R 1/r.

Therefore Gershgorin / the Schur bound gives

    boxed:

    ||H_{R,M,B}||op
      <=
      K(R,M,B)

      :=
      B
      + (4M/pi) H_R.

This constant is independent of T and d.

Hence every eigenvalue of the clipped finite-band matrix lies in the fixed
compact interval

    [-K,K].

## 6. Finite polynomial reduction is now legitimate

Fix R,M,B and epsilon>0.

Since r2 is continuous on [-K,K], there exists a real polynomial P_n with
finite degree n=n(R,M,B,epsilon) such that

    sup_{|x|<=K}
      |r2(x)-P_n(x)|
      <= epsilon.

Consequently

    boxed:

    |
      tau r2(H_{R,M,B})
      -
      tau P_n(H_{R,M,B})
    |
      <= epsilon.

Because H_{R,M,B} has bandwidth R,

    tau P_n(H_{R,M,B})

depends only on closed index walks of:

    length <= n,
    displacement per step <=R.

So after R,M,B,n are frozen, the first-record theorem becomes a finite
collection of finite-degree local translation-word averages.

This is a bounded-consumer reduction.  It does not assert a finite-T raw
moment theorem for the original unbounded matrix.

## 7. Evidence boundary

Closed here:

- beta normalized L2 constant 1/6;
- beta rank quarantine;
- compact spectral support after alpha+beta clipping and fixed band;
- existence of a finite polynomial/local-word reduction.

Not closed here:

- a useful small numerical degree n;
- the finite arithmetic transport for all words required by that n.

The crude R,M,B error constants are not yet optimized and should not be used
to launch a huge finite computation.

The correct next question is whether the local r2 observable admits a much
smaller rational/positive approximation than a generic compact-interval
polynomial approximation, so that only the already-accessible degree-four
or degree-six arithmetic gates are needed.

See:

    notes/WP84_R2_DISPLACEMENT_TAIL_TRUNCATION.md
    notes/WP84_R2_FINITE_BAND_LOCALITY.md
    notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md
    notes/WP84_RESONANT_SCALAR_COVARIANCE.md

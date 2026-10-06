# WP84 — balanced product coefficient second-mass bound

Date: 2026-10-06

Status: **THEOREM-SIDE NORMALIZATION — THE ORDINARY-PRIME BALANCED PRODUCT COEFFICIENT HAS UNIFORMLY BOUNDED L2 MASS; PROPER PRIME-POWER CORRECTIONS ARE LOWER ORDER**

No unconditional zero-density percentage is claimed here.

The fixed-scale Schur-product argument and the large-sieve perturbation route
need an L2 bound for the balanced product coefficient.

That bound follows from the prime-square measure already established on the
branch.

## 1. One-prime squared mass

For an ordinary prime p, write the normalized sharp coefficient in the form

    kappa_p
      =
      c0
      *
      log p/(L sqrt p),

where c0 is the fixed normalization constant of the sharp block.

The strengthened prime-square measure theorem gives

    sum_{p<=exp L}
      (log p)^2/p

      =
      (1/2)L^2
      +O(1).

Therefore

    boxed:

    sum_p |kappa_p|^2
      =
      c0^2/2
      +O(L^-2)

      =
      O(1).

The precise fixed constant is not needed below; uniform boundedness is
enough.

## 2. Ordered two-prime coefficient

For an ordered ordinary-prime pair define

    z_{p,q}
      =
      kappa_p kappa_q w_{p,q},

where w_{p,q} is any overlap/taper weight satisfying

    |w_{p,q}|<=1.

Then

    boxed:

    sum_{p,q}
      |z_{p,q}|^2

      <=
      (
        sum_p |kappa_p|^2
      )^2

      =
      O(1).

This is exactly the normalization needed for the six-sign-pattern ledger:
the ordered pair sum already contains the two internal permutations of each
same-sign factor pair.

## 3. Product collapse

Collapse ordered pairs by their product:

    c(m)
      =
      sum_{pq=m}
        z_{p,q}.

For distinct ordinary primes, an integer m=pq has at most the two ordered
representations

    (p,q),
    (q,p).

Hence

    |c(m)|^2
      <=
      2
      sum_{pq=m}
        |z_{p,q}|^2.

Summing m gives

    boxed:

    sum_m |c(m)|^2
      =
      O(1).

Thus the balanced ordinary-prime product vector has uniformly bounded L2
mass in the exact normalization consumed by the finite-trace quadratic form.

## 4. Proper prime powers

For k>=2,

    sum_p
      (log p)^2/p^k

converges absolutely.

After the L^-2 sharp normalization, the total squared mass of proper prime
powers is therefore

    boxed:

    O(L^-2).

Any balanced term containing at least one proper-prime-power coefficient is
lower order after Cauchy--Schwarz against the O(1) ordinary-prime block.

So the load-bearing second-mass theorem may be proved on the ordinary-prime
sector and the proper-prime-power sector added as o(1).

## 5. Consequence

The coefficient-side hypothesis needed by the fixed-scale connected-kernel
route is now source-closed:

    boxed:

    ||c||_2^2
      =
      O(1).

No divisor-count or pointwise semiprime estimate is required.

This bound is compatible with the exact orientation normalization in

    notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md.

## 6. Evidence boundary

Closed:

- one-prime sharp squared mass is O(1);
- ordered two-prime squared mass is O(1);
- collapsed ordinary-semiprime coefficient has O(1) L2 mass;
- proper-prime-power squared mass is o(1).

Still open:

- combine this bounded coefficient mass with the unequal-scale detuning
  kernel strongly enough to obtain an o(1) connected error.

See:

    notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md
    notes/WP84_PRIME_FRAME_GAUSSIAN_CONCENTRATION.md
    notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md

# WP84 — strengthened prime-square measure discrepancy from the PNT

Date: 2026-10-05

Status: **CUMULATIVE PRIME-SQUARE MEASURE ERROR IMPROVED FROM O(L^-1) TO O(L^-2); K2-WEIGHTED GROWING-SECTION TESTS NOW HAVE O(L^-1) ERROR**

No percentage theorem is claimed here.

Several WP84 notes use only the coarse source-closed estimate

    sum_{n<=x} Lambda(n)^2/n
      = (1/2)(log x)^2 + O(log x).

For the ordinary-prime D2 sector we can do better using only the classical
prime number theorem with its standard unconditional zero-free-region error.

The stronger error is important because it is exactly what is needed to pass
from fixed lattice displacement to K2-weighted growing sections.

## 1. Prime number theorem input

The classical PNT supplies, for some c>0,

    pi(x)
      = li(x)
        + O(
            x exp(-c sqrt(log x))
          ).

The Vinogradov--Korobov version is stronger, but the displayed
de la Vallee Poussin scale is already sufficient.

By partial summation,

    A(x)
      := sum_{p<=x} (log p)^2

      = x log x - x
        + O(
            x (log x)^2
            exp(-c sqrt(log x))
          ).

## 2. One more partial summation

Put

    B(x)
      := sum_{p<=x} (log p)^2/p.

Then

    B(x)
      = A(x)/x
        + int_2^x A(t)/t^2 dt.

Insert the asymptotic for A.

The main terms give

    (1/2)(log x)^2 + C0

for an absolute constant C0.

The error integral converges because

    int_2^infinity
      (log t)^2
      exp(-c sqrt(log t))
      dt/t

is finite.

Hence

    boxed:
    sum_{p<=x}
      (log p)^2/p

      =
      (1/2)(log x)^2
      + C0
      + O(
          (log x)^C
          exp(-c' sqrt(log x))
        )

for suitable absolute C,c'>0.

In particular the remainder after subtracting the quadratic main and the
constant is uniformly bounded.

## 3. Normalized measure discrepancy

Let X=e^L and define the ordinary-prime measure on [0,1]

    nu_L
      =
      L^(-2)
      sum_{p<=X}
        (log p)^2/p
        delta_{log p/L}.

Let

    nu(ds)=s ds.

Then

    nu([0,s])=s^2/2.

The asymptotic above gives uniformly for 0<=s<=1

    boxed:
    sup_s
      |
        nu_L([0,s])
        - s^2/2
        - C0/L^2
      |
      = O(L^-2),

where the harmless constant atom correction C0/L^2 may be absorbed into the
same O(L^-2) discrepancy for bounded-variation testing.

Therefore, for every complex function g of bounded variation,

    boxed:
    |
      int g dnu_L
      - int_0^1 s g(s) ds
    |

      <=
      C/L^2
      [
        ||g||_infinity
        + Var(g)
      ].

This is one full power of L stronger than the coarse ledger previously used.

## 4. Fourier-mode consequence

For

    g_r(s)=exp(2*pi*i*r*s),

we have

    Var(g_r)=2*pi|r|.

Hence

    boxed:
    |
      int g_r dnu_L
      - int_0^1
          s exp(2*pi*i*r*s) ds
    |

      <=
      C(1+|r|)/L^2.

This remains useful for lattice displacements growing with L once an
additional 1/r^2 kernel is present.

## 5. K2-weighted bilinear consequence

Let x,y in C^d and define

    G_{x,y}(s)
      =
      (1/d)
      sum_{i!=j}
        x_i y_j
        exp(2*pi*i(i-j)s)
        /(i-j)^2.

By Cauchy--Schwarz on each displacement diagonal,

    |
      sum_i x_i y_{i-r}
    |
      <= ||x||_2 ||y||_2.

Therefore

    ||G_{x,y}||_infinity
      <= C
          ||x||_2||y||_2/d,

while differentiation loses one power of |r|:

    Var(G_{x,y})
      <=
      C log d
      * ||x||_2||y||_2/d.

Thus if

    ||x||_2,
    ||y||_2
      = O(sqrt d),

then

    boxed:
    |
      int G_{x,y} dnu_L
      - int_0^1 s G_{x,y}(s) ds
    |

      =
      O(
        log d / L^2
      ).

In the WP84 scaling

    log d = L+O(log L),

so

    boxed:
    K2-weighted prime-square substitution error
      = O(L^-1)
      = o(1).

This is uniform over every pair of state vectors with bounded normalized
l2 norms.

## 6. Why this matters for the LRSC/displacement closure

The exact D1/D2 reductions repeatedly produce the squared-Cauchy kernel

    1/(i-j)^2.

The resonant beta covariance independently produced the same kernel.

Section 5 shows that, for every occurrence that can be organized as a
K2-weighted bilinear of bounded normalized state vectors, the passage from
the discrete prime-square measure to the continuum s ds law is now
theorem-grade even though d grows exponentially in L.

The old fixed-r objection disappears for this class.

## 7. What remains open

This note does not automatically close every resonant D2 term.

Some alpha/commutator pieces contain discrete Hilbert operators J before the
outer K2 reconstruction.  Those terms must be rearranged so that the bounded
l2 operator norm of J is used instead of an absolute 1/|r| summation.

Likewise the carrier-2T sum-frequency/Hankel channel is untouched.

The next gate is therefore precise:

> rewrite every resonant rank-three D2 contribution as a finite sum of
> K2-weighted bilinears with J used only through its l2 operator norm.

If this succeeds, V_res closes at o(1) directly from the strengthened PNT
measure discrepancy.

Public source used for the PNT input:
NIST DLMF §27.12, equations 27.12.5--27.12.6.

See:

    notes/WP84_RESONANT_SCALAR_COVARIANCE.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md

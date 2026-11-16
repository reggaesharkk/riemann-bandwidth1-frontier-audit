# WP84 — uniform block large-sieve bound for the finite-trace Gram matrix

Date: 2026-10-06

Status: **THEOREM-SIDE OPERATOR BOUND — THE PRODUCT-BLOCK FINITE-TRACE GRAM MATRIX HAS NORM O(1+M/T) WITH AN EXPLICIT ABSOLUTE CONSTANT**

No unconditional zero-density percentage is claimed here.

Let

    K_{mn}
      =
      d^(-1)
      sum_{k=0}^{d-1}
        exp(
          i tau_k log(m/n)
        ),

with

    tau_k
      =
      T+2pi k/L,

and

    d=floor(TL/(2pi)).

Restrict m,n to one dyadic product block

    M<m,n<=2M.

The carrier exp(iT log(m/n)) is a diagonal unitary conjugation and therefore
does not affect the operator norm.

## 1. Frequency separation

Put

    x_m
      =
      log m/L
      mod 1.

For distinct m,n in one dyadic block and L sufficiently large, there is no
mod-one wrap inside the block because

    |log(m/n)|/L
      <=
      log 2/L
      <1/2.

If n=m+1 at the closest spacing,

    log(n/m)
      =
      log(1+1/m)
      >=
      1/(2m)

for m>=1.

Since m<=2M,

    boxed:

    ||x_m-x_n||
      >=
      1/(4ML).

Thus the frequency set is delta-separated with

    delta
      >=
      1/(4ML).

## 2. Large sieve

The Montgomery--Vaughan/Selberg large-sieve inequality gives, for
delta-separated frequencies x_j and a trigonometric polynomial of length d,

    sum_j
      |
        sum_{k=0}^{d-1}
          a_k e(k x_j)
      |^2

      <=
      (
        d+delta^(-1)
      )
      sum_k |a_k|^2.

By duality, the Gram matrix

    G_{mn}
      =
      d^(-1)
      sum_{k=0}^{d-1}
        e(
          k(x_m-x_n)
        )

satisfies

    ||G||_op
      <=
      1
      +
      delta^(-1)/d.

Therefore

    boxed:

    ||K||_op
      <=
      1
      +
      4ML/d.

For TL>=4pi,

    d
      =
      floor(TL/(2pi))
      >=
      TL/(4pi),

so

    boxed:

    ||K||_op
      <=
      1
      +
      16pi M/T.

Thus on the product scale H=M/T,

    boxed:

    ||K||_op
      <=
      1+16pi H.

The constant is deliberately coarse but completely uniform.

## 3. Quadratic-form consequence

For every product coefficient vector c,

    boxed:

    |
      c^* K c
    |

      <=
      (
        1+16pi M/T
      )
      ||c||_2^2.

The balanced coefficient normalization already gives

    ||c||_2^2=O(1).

Hence the only way a scale-detuning perturbation can fail to be o(1) is if
its operator multiplier loses more than the reciprocal H scale.

## 4. Why this matters

A perturbation carrying an additional factor

    O(
      1/(TL)
    )

on a product block has quadratic-form size at most

    O(
      (1+M/T)/(TL)
    )

      =
      O(
        1/(TL)
        +
        M/(T^2 L)
      ).

For the consumed product range

    M<=T^2,

this is

    boxed:

    O(1/L).

Therefore a theorem-grade detuning representation with an explicit
1/(TL) factor closes at o(1).

What remains is to derive that factor at the exact connected-kernel level;
it must not be inferred merely from a cell-center freezing of width
L^(-1/2).

## 5. Source

The large-sieve input is the classical theorem of Montgomery and Vaughan,
*The large sieve*, Mathematika 20 (1973), 119--134,
DOI 10.1112/S0025579300004708.

The slightly sharper Selberg constant is unnecessary here.

## 6. Evidence boundary

Closed:

- exact logarithmic frequency separation on a dyadic product block;
- explicit uniform operator bound
      ||K||<=1+16pi M/T;
- compatibility with the O(1) product-coefficient L2 mass.

Open:

- expose the unequal-scale connected residual with an explicit
  O(1/(TL)) operator factor.

See:

    notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md
    notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md
    notes/WP84_CONNECTED_SCALE_FREEZING_BRIDGE.md

# WP84 — exact resonant scalar-field covariance fingerprint

Date: 2026-10-05

Status: **FIXED-DISPLACEMENT RESONANT COVARIANCES CLOSED IN EXACT FORM; GROWING-SECTION UNIFORMITY / FAST HANKEL CHANNEL STILL OPEN**

No percentage theorem is claimed here.

After the D2 proper-power reduction, one current ordinary-prime block is
encoded by one exponential.

For

    y=log p,
    s=y/L,

the sharp normalized scalar polynomial is

    Q_p(tau)
      = c_p exp(i tau y),

with

    c_p
      = - log p/(a L sqrt p),

where a is the taper-mass normalization and a->1 in the sharp flat model.

Hence

    alpha_p(tau)
      = c_p sin(tau y),

    beta_p(tau)
      = 2 c_p (1-s) cos(tau y).

The prime block is

    B_p
      = M_{beta_p}
        + [M_{alpha_p},J].

## 1. Prime-square continuum measure

For every fixed smooth g on [0,1], the square-prime Mertens law gives

    sum_{p<=X}
      c_p^2 g(log p/L)

      =
      a^(-2)
      int_0^1 s g(s) ds
      + O_g(L^-1).

Proper prime powers contribute only O(L^-2) at the D2 scale and have already
been removed.

## 2. Difference-frequency covariance

On the Fourier grid

    tau_i=T+2*pi*i/L,

the difference phase is

    (tau_i-tau_j)y
      = 2*pi(i-j)s.

Put

    r=i-j.

Using product-to-sum,

    alpha_i alpha_j

has resonant part

    (c_p^2/2) cos(2*pi*r*s),

while

    alpha_i beta_j

has resonant part

    c_p^2(1-s) sin(2*pi*r*s),

and

    beta_i beta_j

has resonant part

    2 c_p^2(1-s)^2 cos(2*pi*r*s).

Therefore, for every fixed integer r, the limiting resonant covariances are
exactly the following.

## 3. alpha-alpha: purely diagonal

Define

    C_aa(r)
      =
      (1/(2a^2))
      int_0^1
        s cos(2*pi*r*s) ds.

Then

    boxed:
    C_aa(0)=1/(4a^2),

and for every nonzero integer r,

    boxed:
    C_aa(r)=0.

So the resonant alpha field is white on the integer Fourier lattice at the
level of its second covariance.

## 4. alpha-beta: identically zero

Define

    C_ab(r)
      =
      a^(-2)
      int_0^1
        s(1-s) sin(2*pi*r*s) ds.

Because s(1-s) is symmetric around 1/2 while the integer-frequency sine is
antisymmetric,

    boxed:
    C_ab(r)=0

for every integer r, including r=0.

Thus the resonant diagonal field beta is orthogonal to the resonant
commutator field alpha at second order.

## 5. beta-beta: one squared-Cauchy kernel

Define

    C_bb(r)
      =
      (2/a^2)
      int_0^1
        s(1-s)^2 cos(2*pi*r*s) ds.

At r=0,

    boxed:
    C_bb(0)=1/(6a^2).

For r!=0, direct integration gives

    int_0^1
      s(1-s)^2 cos(k s) ds

      =
      [-k^2-2k sin k-6 cos k+6]/k^4.

At

    k=2*pi*r,

this becomes

    -1/k^2.

Hence

    boxed:
    C_bb(r)
      = -1/(2 a^2 pi^2 r^2),
      r!=0.

Let K2 be the zero-diagonal squared-Cauchy matrix

    (K2)_{ij}
      = 1/(i-j)^2,
      i!=j.

Then the resonant beta covariance is the explicit Toeplitz kernel

    boxed:
    C_bb
      =
      (1/(6a^2)) I
      - (1/(2a^2 pi^2)) K2.

This is the same K2 that appeared independently in the LRSC/displacement
reconstruction of D1/D2.

## 6. Structural coincidence

Two routes have now produced the same one-dimensional Green kernel:

1. displacement rank:
       off-diagonal BR reconstruction uses 1/(i-j)^2;

2. arithmetic resonant covariance:
       beta-beta covariance uses
       -1/(2a^2 pi^2(i-j)^2).

This is a nontrivial consistency check.

The squared-Cauchy kernel is not an arbitrary convenience introduced by the
linear algebra.  It is already present in the prime-square continuum
covariance.

## 7. Formal resonant variance map

If one may pass the fixed-r covariance limits through the growing finite
section, expansion of

    B_p
      = M_beta+[M_alpha,J]

would give, for an arbitrary matrix A,

    V_res(A)
      =
      C_bb hadamard A
      + E_alpha[
          [M_alpha,J]
          A
          [M_alpha,J]
        ],

with all alpha-beta cross terms zero.

Using

    C_aa=(4a^2)^(-1) I

formally reduces the alpha part to diagonal extractions and J:

    (1/(4a^2)) [
        diag(diag(JA)) J
        - diag(diag(JAJ))
        - J diag(diag(A)) J
        + J diag(diag(AJ))
    ].

And

    C_bb hadamard A
      =
      (1/(6a^2)) diag(diag A)
      - (1/(2a^2 pi^2))(K2 hadamard A).

This is the candidate exact resonant operator map.

## 8. Evidence boundary

Section 7 is **not yet promoted as a growing-d theorem**.

The square-prime Mertens substitution above is source-closed for each fixed
lattice displacement r.  The actual matrix section has

    |r| up to d~T L,

so a uniform tail/interchange theorem is still required.

The important advance is that the target of that theorem is now explicit:
there are no unknown resonant covariance constants.

The remaining D2 analytic debt separates cleanly into:

1. justify the fixed-r-to-growing-section interchange for the explicit
   C_aa/C_ab/C_bb kernels;
2. treat the sum-frequency / carrier-2T Hankel channel.

See:

    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md
    notes/WP84_D1_AGGREGATE_D2_PRIME_ONLY.md
    notes/WP84_BR_RANK3_SCALAR_D1.md

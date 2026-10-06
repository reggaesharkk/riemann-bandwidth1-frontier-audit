# WP84 — bounded rational recovery of limiting moments

Date: 2026-10-05

Status: **RAW-MOMENT FIREWALL CLOSED AT THE LIMIT-LAW INTERFACE**

The limiting-law route needs the moments of the **limit law** through degree
six, but it must not prove finite-T raw fourth/sixth moments of the full
arithmetic matrices.  This note records an exact bounded-resolvent bridge.

## 1. Bounded rational probes

Fix R>0 and k=0,...,6.  Define

    f_{k,R}(x)
      = x^k / (1+(x/R)^8)
      = R^8 x^k/(x^8+R^8).

For every fixed R this is a bounded continuous function on R.

Its eight poles are

    z_j = R exp(i(2j+1)pi/8),
    j=0,...,7,

all strictly off the real axis.

Since k<8, the rational function is proper and has the exact partial-fraction
representation

    f_{k,R}(x)
      = sum_{j=0}^7 c_{j,k,R}/(x-z_j),

with residues

    c_{j,k,R}
      = R^8 z_j^(k-7)/8.

Therefore

    integral f_{k,R}(x) dnu_T(x)

is a finite linear combination of normalized Stieltjes transforms evaluated
at eight fixed nonreal points.

## 2. Consequence of bounded resolvent convergence

Suppose

    m_T(z) -> m_*(z)

at the eight poles for a fixed R.  Then

    integral f_{k,R} dnu_T
      -> integral f_{k,R} dnu_*.

No raw finite-T kth moment enters this statement.

Huge o(d)-rank outliers are harmless because every f_{k,R} is bounded and the
rank-Stieltjes inequality already shows that such sectors disappear from the
weak limit.

## 3. Recover moments only after taking the spectral limit

Assume the identified model law nu_* has finite kth moment.  Then

    f_{k,R}(x) -> x^k

pointwise as R->infinity and

    |f_{k,R}(x)| <= |x|^k.

Dominated convergence on **nu_*** gives

    lim_{R->infinity}
      integral f_{k,R} dnu_*
        = integral x^k dnu_*.

The order of limits is essential:

    first T->infinity at fixed R,
    then R->infinity in the already-identified model law.

This never requires uniform integrability of the full finite-T arithmetic
spectra.

## 4. Why this avoids Proposition-R

The dangerous raw-moment statement would be

    integral x^k dnu_T -> m_k

for the full arithmetic matrices.

WP84 does not need that.

It needs only:

1. bounded-resolvent convergence at fixed nonreal points;
2. a model law nu_* whose finite moments can be computed internally;
3. bounded rational probes to connect the two.

Rare power-law outliers may make

    integral |x|^k dnu_T

huge while changing every fixed-R rational probe by o(1).  This is precisely
the separation the rank-robust route requires.

## 5. Minimal point set

For each R the moment probe consumes only eight nonreal resolvent values.

To identify the weak limiting law uniquely, add any countable set with an
accumulation point in C_+, for example

    i(1+1/n), n=1,2,...

Normalized Stieltjes transforms form a normal family on C_+.  Agreement on
that set determines every subsequential analytic limit by the identity
theorem.

Thus the theorem target can be reduced from a continuum of contour values to
a countable collection of fixed safe points.

## 6. The resulting theorem architecture

A sufficient route is:

    arithmetic matrix
      -> resolvent convergence at a countable fixed set
      -> unique weak law nu_*
      -> compute m0..m6 inside the model law
      -> degree-6 half-line certificate
      -> positive-index liminf.

The order-4 word gate remains a consistency check on the candidate model
generator.  It must not be promoted into a proof of finite-T raw m4.

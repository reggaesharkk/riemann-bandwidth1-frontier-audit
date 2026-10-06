# WP71 G9-B — the j=0 puncture is a lower-order same-prime family

Date: 2026-10-04
Status: **ZERO-HOLE OBSTRUCTION CLOSED IN SUPPORT/OUTER-MASS SHAPE**

The moving-interval audit isolated one puncture:

q divides n, with

n=q t,
m=r t,

where

g=(b1,b2), r=b1/g, q=b2/g, and (r,q)=1.

For the welded partner,

n'=q(t-k),
m'=r(t-k).

The actual four-von-Mangoldt weight at the forbidden j=0 point is therefore

Lambda(qt) Lambda(q(t-k)) Lambda(rt) Lambda(r(t-k)).

We consider k nonzero.

## 1. If q>1 and r>1, the hole weight vanishes identically

Suppose Lambda(qt)Lambda(rt) is nonzero.

If t>1, any prime dividing t divides both qt and rt. Since each of qt and rt
must be a prime power, they must be powers of the same prime. Then both q and
r are powers of that prime, contradicting (q,r)=1 with q,r>1.

Hence t=1.

Applying the same argument to t-k shows t-k=1. Therefore k=0, contrary to the
off-diagonal condition.

Thus

boxed:
  q>1, r>1, k!=0
  implies
  Lambda(qt)Lambda(q(t-k))Lambda(rt)Lambda(r(t-k)) = 0.

So the j=0 puncture contributes no actual four-prime mass in every genuinely
two-sided coprime cell.

## 2. Nonzero holes require q=1 or r=1

If q=1, then b2 divides b1.
If r=1, then b1 divides b2.

But b1 and b2 are prime powers in the Stage-A outer sum. Therefore a
divisibility relation between them implies that they are powers of the same
prime.

So every potentially nonzero puncture lies in the same-prime outer-cell
family.

The diagonal q=r=1 case is simply b1=b2 and is included in the same family.

## 3. Same-prime outer mass is bounded

The outer prime-power weight is

Lambda(b1)Lambda(b2)/(b1 b2).

Summed over all ordered powers of the same prime,

sum_p sum_{a,b>=1}
  (log p)^2 / p^(a+b)

=
boxed:
sum_p (log p)^2/(p-1)^2
< infinity.

This converges absolutely.

By contrast, the full two-dimensional prime-power Mertens mass grows like
(log X)^2. Hence the entire same-prime/divisibility family is lower
dimensional and lower order in the normalized continuum limit.

This is the same structural reason diagonal prime-power pairs were already
classified as lower order in the prime-power measure gate.

## 4. Consequence for the moving-window remainder

The exact prefix decomposition contained a hole deviation

1_hole * (Lambda(m0)Lambda(m0-rk)-S(rk)).

When multiplied by the outer pair factor, the actual four-Lambda hole is
identically zero away from the same-prime outer family.

Therefore G9-C does not need a new general four-prime theorem for the
puncture. The only surviving cells are the bounded same-prime family, to be
charged with the already-used lower-dimensional outer-mass argument.

The companion checker

src/wp71_g9_b_zero_hole_support.py

exhaustively verifies the q>1,r>1 support impossibility over a finite integer
grid. The mathematical proof is the prime-factor argument above.

## Remaining G9-B/C boundary

After removing the lower-order puncture family, the moving-window remainder
has only the two monotone endpoint pullbacks

E_k(U_k(n)) - E_k(L_k(n)-1).

Those are now the sole general-purpose objects that must be mapped into the
MRT estimate.

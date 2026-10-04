# WP71 G9-B — moving interval and boundary-transition audit

Date: 2026-10-04
Status: **MOVING-INTERVAL COMBINATORICS CLOSED; analytic endpoint errors remain**

This resolves the structural question left after the rectangular calibration:
what exactly is the moving interval I(n), where can its boundaries change,
and what must a signed Abel argument track?

Fix b1,b2,J, an outer window

m in [ell,h] intersect Z,

and put

g=(b1,b2), r=b1/g, q=b2/g.

After the exact welding substitution

m'=m-rk, n'=n-qk,

the simultaneous outer-window constraint is

m in [A_k,B_k],

where

A_k=max(ell,ell+rk),
B_k=min(h,h+rk).

The j-strip condition 0<|b1 n-b2 m|<=J gives the full, unpunctured interval

L_k(n)=max(A_k, ceil((b1 n-J)/b2)),

U_k(n)=min(B_k, floor((b1 n+J)/b2)).

## 1. The only puncture is j=0

Because b1=gr, b2=gq and (r,q)=1, the equation b1 n=b2 m has an integer
solution exactly when q divides n. Then

m0=r*(n/q).

Hence I_k(n) is the integer interval [L_k(n),U_k(n)] with at most the one
point m0 removed, when q|n and m0 lies in [A_k,B_k].

The punctures themselves form the exact progression

(n,m0) -> (n+q,m0+r).

They must be tracked explicitly; they may not be silently absorbed into o(1).

## 2. Same-j invariance is exact

For the welded partner,

b1(n-qk)-b2(m-rk)=b1 n-b2 m

because b1 q=b2 r.

Therefore one j-strip test controls both members of the welded pair.

## 3. Boundary transitions are monotone

For fixed k, L_k(n) is nondecreasing and its active source can switch only once:

static A_k -> moving j-lower endpoint.

Likewise U_k(n) is nondecreasing and its active source can switch only once:

moving j-upper endpoint -> static B_k.

Moreover

0 <= L_k(n+1)-L_k(n) <= ceil(b1/b2),

and the same bound holds for U_k.

Thus the endpoint variation does not oscillate. On every n-block, total
variation telescopes to the endpoint difference.

This is the structural fact required for the Abel step.

## 4. Exact prefix decomposition

For fixed lag rk put

x_k(m)=Lambda(m)Lambda(m-rk)

and

P_k(t)=sum_{m<=t} x_k(m).

Then exactly,

w_k(n)
 =
P_k(U_k(n))-P_k(L_k(n)-1)
-1_hole*x_k(m0).

If a prime-pair prefix law is written as

P_k(t)=S(rk) N_k(t)+E_k(t),

then

w_k(n)=S(rk)|I_k(n)|+e_k(n)

with exact remainder

e_k(n)
 =
E_k(U_k(n))-E_k(L_k(n)-1)
-1_hole*(Lambda(m0)Lambda(m0-rk)-S(rk)).

So the opaque moving-window error reduces to only three components:

1. upper-endpoint prime-pair error;
2. lower-endpoint prime-pair error;
3. explicit q-spaced zero-hole deviation.

These are the precise objects G9-C must map into MRT-compatible estimates.

## 5. Required signed boundary ledger

Every implementation of the moving-geometry Abel step must record:

- A_k and B_k;
- current L_k and U_k;
- active lower source: static or jlower;
- active upper source: jupper or static;
- each source-switch n;
- every q-spaced zero-hole point;
- every sign change of the external slow geometric/kernel weight.

The arithmetic endpoints themselves have no hidden sign ambiguity because
they are monotone. Sign partitioning is needed only for the external signed
geometry.

The signed main must be Abel-summed separately on those sign cells. No
absolute value is permitted before that partition.

## 6. Machine gate

src/wp71_g9_b_moving_interval.py checks on unrelated exact integer families:

- the closed endpoint formulas against direct enumeration;
- same-j invariance;
- the prefix-sum identity;
- exact main/remainder decomposition for an arbitrary surrogate constant;
- endpoint monotonicity and increment bounds;
- at most one active-source switch per endpoint;
- the exact puncture progression.

The checker uses arbitrary deterministic integer weights because this gate is
combinatorial.

## Gate consequence

G9-B is now reduced to a weighted Abel / analytic endpoint-error problem.

No new prime-correlation main constant remains to be discovered in the moving
interval. The next task is to map the two endpoint-error pullbacks and the
sparse hole term into the pinned MRT hypotheses and then charge them in exact
R-units.

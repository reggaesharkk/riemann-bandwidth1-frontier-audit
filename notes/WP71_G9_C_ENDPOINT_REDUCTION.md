# WP71 G9-C — endpoint reduction and the single analytic target

Date: 2026-10-04
Status: **EXACT REDUCTION CLOSED; maximal shifted-prime input still to be proved**

The moving-interval audit reduced the general welding error, outside the
lower-dimensional j=0 puncture family, to

e_k(n)
 =
E_{rk}(U_k(n))
-
E_{rk}(L_k(n)-1),

where E_h(t) is the cumulative prime-pair error at shift h.

This note isolates one sufficient analytic statement which would close the
general middle-band remainder.

## 1. Maximal pair-error norm

On a dyadic prime scale M define

D_h(u,v)
 =
sum_{u<m<=v} Lambda(m)Lambda(m-h)
-
S(h)(v-u),

and

Emax(h;M)
 =
sup_{M<=u<v<=2M} |D_h(u,v)|.

The moving interval I_k(n) is always a subinterval of the corresponding
outer m-block, up to the already isolated j=0 puncture. Therefore

|e_k(n)| <= 2 Emax(rk;M)

for every admissible n in that dyadic block.

No smoothness or number theory is used here; this is a direct consequence of
the two-endpoint representation.

## 2. Exact shift-only Cauchy--Schwarz

Let G_{k,n} be the signed slow geometry/kernel coefficient after all fixed
cell prefactors are extracted, and put

A_{k,n}=Lambda(n)Lambda(n-qk).

The general endpoint remainder is

R_end
 =
sum_k sum_n G_{k,n} A_{k,n} e_k(n).

Define the nonnegative outer weight budget

W_k
 =
sum_n |G_{k,n}| A_{k,n}.

Then, without applying Cauchy--Schwarz in n or across the cell family,

|R_end|
 <=
2 sum_k Emax(rk;M) W_k

and hence

boxed:
|R_end|
 <=
2
( sum_k Emax(rk;M)^2 )^(1/2)
( sum_k W_k^2 )^(1/2).

This is exactly the allowed use of Cauchy--Schwarz: **in the shift variable
only**.

The signed main has already been removed before this inequality is invoked.

## 3. Sufficient analytic input

A sufficient prime-correlation theorem for G9-C is:

For every A and every polylogarithmic structured multiplier r,

boxed:
sum_{k<=K}
Emax(rk;M)^2
 <<_A
K M^2 (log M)^(-A),

uniformly in the Stage-A range K r <= M^(1-epsilon).

Call this the **maximal structured-shift L2 input**.

Once it is available, any fixed logarithmic losses in the deterministic
outer budget W_k can be beaten by choosing A larger.

This is stronger than the already-derived fixed-window G2 statement because
of the supremum over interval endpoints.  Therefore G2 by itself does not
close G9-C.

## 4. Why the target is plausible but not yet claimed

MRT supplies the underlying long-shift correlation theorem and, deeper in the
proof, the minor-arc mean-value estimates.  The public candidate also invokes
a smoothing collar and Abel summation.

There are two legitimate ways to prove the maximal structured-shift input:

### Route M1 — smooth maximal family

Replace sharp interval endpoints by a fixed finite family of smooth monotone
cutoffs at the Gallagher scale, prove the corresponding structured-shift
L2 estimate from MRT Proposition 3.4 / Proposition 5.4, and pay the hard/smooth
difference through G7.

### Route M2 — direct endpoint decomposition

Decompose every moving interval into a logarithmic family of canonical
subintervals or smooth blocks and union the exceptional-shift estimates with
an arbitrarily stronger logarithmic saving.

This route must be written carefully: Theorem 1.3 as printed is not itself a
black-box maximal-prefix theorem.

Until one of M1/M2 is fully written with all parameter inequalities checked,
G9-C remains open.

## 5. Deterministic outer-budget obligation

The second factor

( sum_k W_k^2 )^(1/2)

contains no inner prime-pair uncertainty. It is a geometry/outer-pair budget.
G9-D must place it in the exact public normalization

1/(pi*l*X*ell1^4)

and prove that its growth costs only a fixed power of log M (and the already
charged cell-mass factors).

This is now a separate deterministic calculation.

## 6. Gate map after the reduction

- G9-A exact welding reindexing: CLOSED.
- G9-B local Euler factorization: CLOSED.
- G9-B rectangular main calibration: CLOSED.
- G9-B moving-interval combinatorics: CLOSED.
- G9-B j=0 support isolation: CLOSED IN SHAPE / lower-dimensional charge.
- G9-C endpoint reduction: CLOSED.
- G9-C maximal structured-shift L2 theorem: OPEN.
- G9-D exact R-unit outer-budget normalization: OPEN.

This is the smallest honest analytic target currently visible for the
middle-band glue.

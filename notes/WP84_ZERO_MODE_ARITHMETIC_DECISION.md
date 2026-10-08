# WP84 zero completion mode: arithmetic decision

Input HEAD: `0ff4b44d2f7a8eb6b4c700dac7991cd7e102225f`.
**NO-GO for extending the tested Fourier-completion/rectangular Type-II route.**
No magnitude power saving, o(1) removal, or signed constant is earned.
This does not disprove the WP84 arithmetic inequality.

## Exact completion, without linearizing any source phase

Keep R=6000, X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)), and
every original path, prefix, root, prime restriction, hidden-prime sum,
normalization and carrier from equations (1)--(3) of
`WP84_CUBIC_FIRST_ALIAS_TYPEII_FEASIBILITY.md`. Write u=pq, r the
negative visible prime, delta=log(u/(Xr)), tau_j=T+h(i_min+j).
Let W_ell(p,q,r) be exactly the three c_p F factors and all original
non-alias masks; for a fifth-order path it also includes the original
B_ab,T(p,q,r), with its hidden exclusions and masks. Do not replace B_ab,T
by a covariance or replace the five-slot path by a three-slot path.

For one original alias interval E in delta, partition by
k=floor(u/r). Define the exact finite residue set

    J_(r,k)={s in {0,...,r-1}: log((kr+s)/(Xr)) in E}.

Only positive kr+s are considered. Keep the original endpoint conventions.
Dyadic product endpoints can also be intersected into J; other masks stay
in W. A union of alias intervals is partitioned into disjoint pieces.
No new half-core is substituted for E. This definition works for real X,
not only integer X. With M_(r,k)(u)=1_(u mod r in J_(r,k)), set

    h_(r,k)(a)=1/r sum_(s in J_(r,k)) exp(-2pi i a s/r).
    H_j(u,r)=exp(i tau_j log(u/(Xr))-2pi i u/r).

The exact original contribution S_E is Z_E+NZ_E, where

    Z_E = exp(iT L)/n sum_ell sum_r sum_k sum_(j<rho)
        h_(r,k)(r-1)
        sum_(p,q: floor(pq/r)=k) W_ell(p,q,r) H_j(pq,r),       (1)

    NZ_E = exp(iT L)/n sum_ell sum_r sum_k sum_(j<rho)
        sum_(a mod r, a!=r-1) h_(r,k)(a)
        sum_(p,q: floor(pq/r)=k) W_ell(p,q,r) H_j(pq,r)
                              exp(2pi i (a+1)pq/r).           (2)

All primes in these formulas remain <=N. The identity is pointwise:

    exp(2pi i u/r) M_(r,k)(u)
      = sum_(a mod r) h_(r,k)(a) exp(2pi i (a+1)u/r).         (3)

Multiply (3) by H_j, the original W and carrier, then sum. Completion
has EXACTLY ZERO error; no root linearization is used. Conjugate words
use exp(-2pi i u/r), with zero index a=1 mod r and conjugate H/carrier.
The replayer checks both signs, prime and composite moduli, empty/full
and interval masks in exact cyclotomic arithmetic, and quotient cells with
rational noninteger X. These are identities, not sampled prime estimates.

Crucial interpretation: zero in (1) means zero in the COMPLETION basis.
H_j remains oscillatory. More generally factoring exp(2pi i c u/r)
would place the zero index at -c mod r. There is no invariant arithmetic
main term merely because a completion coefficient is nonzero.

In fact its remaining phase has the exact factorization

    H_j(pq,r)=(Xr)^(-i tau_j) p^(i tau_j) q^(i tau_j)
                                      exp(-2pi i pq/r).       (3a)

Thus the completion-zero term still has a coprime numerator -1 for a
prime r, together with separable multiplicative phases. In the ORIGINAL
logarithmic-phase basis it is not zero additive frequency at all: that
index would be a=0, not a=r-1. This corrects any interpretation of the
previous linearized special-root example as an intrinsic constant phase
for the full source. Identity (3a) permits a rectangular DFT bound if the
quotient and other coupled masks could be removed legally; they cannot
be removed here. No saving follows simply by changing the Fourier basis.

## Arithmetic structure and unconditional estimates

In the previous integer-X half-core J={1,...,floor(r/1000)},

    h_(r,X)(r-1)=1/r sum_(s in J) exp(2pi i s/r),
    Re h >= (4999/5000)|J|/r.

The bound follows from cos t>=1-t^2/2 and pi<22/7, since
0<=t<=2pi/1000. It proves a nonzero coefficient, not the sign of (1).
For r=1009,J={1}, the coefficient is exactly exp(2pi i/1009)/1009.

For general J, |h|<=|J|/r<=1. The inner zero-mode object counts weighted
ordered prime products in [kr,(k+1)r), with the complete source filters
and residual phases. In the tested core k~X, r~X^(3/5), its length is
r~u^(3/8). In the balanced p,q~X^(4/5) cell, fixing p leaves a q interval
of length r/p~X^(-1/5). This is a genuine thin prime-product correlation,
not a long individual prime sum. PNT for marginal prime measures does not
evaluate it, nor does Fourier orthogonality provide a signed identity.
No applicable uniform prime-correlation asymptotic is proved or imported.

An unconditional bound follows directly. In |delta|<=H/X with fixed H,
at most 6H+2 quotient cells meet E for each r, because the full u interval
has length <=6Hr. Each complete quotient cell contains r integers; each
integer has at most two ordered distinct-prime factorizations. Eventually
|c_p|<=2/sqrt(p), |F|<=1 and u>=Xr/2, so a cubic coefficient has magnitude
<=8sqrt(2)/(sqrt(X) r). Thus each zero-mode cell has total coefficient mass
<=16sqrt(2)/sqrt(X). For r in [V,2V), at most 2V integer denominators,
rho/n<=1, the per-path bound is

    |Z_E| <=32sqrt(2)(6H+2) V/sqrt(X)=O_H(X^(1/10)).          (4)

Original masks can only reduce this absolute bound. Fifth-order hidden
mass contributes the inherited eventual factor <=2, conditional on the
same source-normalization hypothesis as the previous report. Finite path
and word counts depend on fixed R. Equation (4) supplies no small bound.
For the complete gate and arbitrary good-section transfers retain all
inherited hypotheses; no new masked transfer or proper-power disposal is
claimed. Non-core shells and tails are not removed by (4).

For a contiguous J, its geometric-series coefficients satisfy

    sum_(a mod r)|h(a)| <= 2+log r.                           (5)

Indeed |h(0)|<=1 and |h(a)|<=1/(2 min(a,r-a)); pairing opposite
indices bounds the remainder by a harmonic sum <=1+log r.
Multiple disjoint intervals pay their interval count. Applying the cell
count before summing completion modes gives only
O_H(X^(1/10)(1+log X)) for their aggregate absolute majorant. This is
weaker than the unsplit mask bound. A large completion coefficient need
not be large after summation; cancellation between Z and NZ is retained.

## Sign, consumer and nonzero modes

The full carrier, complex filters and H_j prevent a sign conclusion from
Re h>0. Even the zero-displacement cubic path has c_p c_q c_r<0 and
positive f_0 factors, but a complex root/carrier multiplier; neither
negativity of that coefficient nor positivity of h proves a real saving.
Rotating any nonzero complex term by 1 versus -1 reverses its real part
without changing its norm. This falsifies a coefficient/norm-only sign
inference, NOT the actual source arithmetic inequality. The actual carrier
is fixed and is not freely chosen in a proof.

The source-exact shared contribution is

    Re[ c3 (Z3+NZ3) - A sum_(original paired fifth paths)(Z5+NZ5) ],
    c3=21981971/46375000, A=11501/12500.                       (6)

Different physical path prefixes, root ranges and B_ab,T remain in (6).
There is no termwise scalar relation between Z3 and Z5 that licenses
Gaussian contraction, covariance substitution or a favorable sign.
All remaining sixth-order populations retain coefficient B=137641/250000.
They are not removed or assigned this cubic completion frequency.

For a prime denominator every nonzero integer completion numerator is
coprime to r, but this refers to a+1 BEFORE H_j is multiplied back in.
By (3a), the exact resulting additive numerator is a. In particular the
completion-nonzero mode a=0 has no additive oscillation in the original
basis. For a!=0 the remaining multiplicative p/q phases are separable and
are permitted by the rectangular DFT theorem; they are not by themselves
a failed hypothesis. The quotient condition and hidden exclusions still
prevent its rectangular application. Most original roots have noninteger
theta_j=tau_j/(2pi X), so treating H_j as constant, as in a special
linearized theta=1 calculation, would also be invalid. Vaughan integer
leaves have composite denominators; nonzero numerators can then also be
non-coprime. No source-matched dispersion or bilinear improvement is
established for (2). A hypothetical bound only for (2) would leave (1).

The frozen conditional reference margin is unchanged:
8558084052085891/91584868530424500000=0.00009344430132847649... .
The entire joint residual still must satisfy Jcap-B Pair6_6000-kappa-eta,
where Jcap=51835308978310574561/457924342652122500000 and eta>0 is a
strict gap. Its necessary negative saving exceeds
15909857470864664470267332031322977/
7733161315109907280429056000000000000
=0.002057354918974498... plus payments. Neither (1) nor (2) earns any
part of it. Prime-to-Weil, band-interface and zero-side obligations remain
separate. Strict >79 remains unproved.

## Decision and single missing theorem

The zero component is an unresolved weighted short-interval semiprime
correlation with residual source phases, not an evaluated main term or a
proved signed identity. The single new input needed by THIS approach is a
uniform source-weighted dilated prime-product strip estimate for the
COMPLETE Z+NZ root/path sum (including the fifth contraction), overcoming
the X^(1/10) loss with aggregate logarithms paid. An absolute o(1) estimate
would remove this window but would still earn no negative constant for the
global consumer. No such estimate is supplied here. **STOP / NO-GO.**
No alternative search is initiated.

Reproduce: `python src/wp84_zero_mode_arithmetic_replay.py`.
Certificate: `WP84_ZERO_MODE_ARITHMETIC_CERTIFICATE.json`. The finite
exact tests certify the completion algebra and rational exponent ledger;
the analytic bounds above supply the asymptotic reasoning.

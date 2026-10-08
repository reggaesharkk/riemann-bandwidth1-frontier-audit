# WP84 high-product signed arithmetic: feasibility decision

Input `d8b2746e437ae7e8f9e681ef172fc286e11a6698`, 2026-10-08.
**NO-GO for closing the consumer with the estimates audited here.** One
additional part of the shared cubic alias sector is o(1). No constant signed
saving follows. This is a diagnosis of the current method, not an
impossibility theorem about the arithmetic inequality.

## 1. Frozen target and evidence boundary

The [preceding report](WP84_JOINT_THIRD_FIFTH_SIXTH_ARITHMETIC_OBSTRUCTION.md)
and its exact certificate are pinned by blob and SHA-256 in this certificate.
Keep R=6000, X=T/(2pi), L=log X, N=floor(exp(L-sqrt L)), h=2pi/L,
d=floor(XL), and the original contiguous I=[a,a+n-1], n/d->1.
No cutoff, source mask, consumer or model moment is changed.

The full coefficient vector of the frozen squared cubic, degrees 0 through 6,
is

    (364848201/34410250000, -18356061/344102500,
     -26060119/430128125, 21981971/46375000,
     0, -11501/12500, 137641/250000).

Write c3=21981971/46375000, A=11501/12500, B=137641/250000.
The sufficient same-section gate remains

    limsup[c3 mu3-A mu5+B mu6] <= Jcap-kappa-eta, eta>0,
    Jcap=51835308978310574561/457924342652122500000.          (1)

The improved second-moment payment is 208480952/203775517378125;
the band payment is 128952763/92407500000. Independent squaring and budget
replay recover the conditional reference margin

    Mref=8558084052085891/91584868530424500000
        =0.00009344430132847649... .                         (2)

Thus (1) is equivalently the upper bound Mref-kappa-eta on
c3 mu3+A(1/36-mu5)+B(mu6-34/135). The reference values are bookkeeping,
not actual moment assumptions. Under the still-unproved reference fifth/
sixth inequalities, the zero-extra-cost third boundary is
8558084052085891/43411664130988764996=0.00019713789423651305...;
subtract (kappa+eta)/c3. Without a fifth/sixth bound this is not sufficient.

After all established removals the ordinary-prime residual is

    Re[c3 D3*-A(D5*+Q3*)+B(D6*+Q4*)],                       (3)

with required upper bound Jcap-B Pair6_6000-kappa-eta. Dk denotes k
distinct visible primes; Q3/Q4 have one additional hidden balanced pair
and the original fifth/sixth paths. The actual filtered Pair6 is retained.
Its proved lower bound makes the necessary negative saving exceed

    g=15909857470864664470267332031322977/
      7733161315109907280429056000000000000
     =0.002057354918974498...,

plus kappa+eta. Replacing Pair6 by its lower bound is only a necessary test.

D3*/Q3* presently retain mixed U=pq>N, V=r, |log(U/V)|>1, and same-sign
U=pqr>N^2, with their conjugates. Exact nonzero cubic aliases are removed;
approximate aliases and all far tails remain. D5*,D6*,Q4* retain the prior
signed-ledger populations after their proved central-window removals.
No previously closed equality classification is reopened.

## 2. Exact near-product arrays and legal dyadic partition

For each original closed path ell, |ell_j|<=6000, set q_j=sum_(t<=j)ell_t,
rho=max(0,n-max q+min q), i_min=a-min q. Use the original factors
c_p=-log(p)/(a_phi L sqrt p), a_phi->1,
f_0^eps(s)=1-s, f_l^+(s)=(1-exp(2pi i l s))/(2pi i l),
f_l^-=conj(f_l^+), and every prefix phase exp(2pi i eps_j q_(j-1)s_p).

Split each prime variable into half-open intervals [2^j,2^(j+1)), intersected
with its ORIGINAL masks and p<=N. Split U=product of positive visible primes
and V=product of negative visible primes into half-open product intervals.
V=1 for an empty negative side. All distinctness and hidden-prime exclusions
remain literal. These partitions are disjoint; no smoothing error is incurred.

Let Gamma_(F,ell,eps,cell)(u,v) be the sum of the ORIGINAL coefficient product
and prefix factors over precisely these tuples with U=u,V=v. For Q3/Q4 sum
the hidden balanced prime with its two original factors, both orientations
and exclusions. In particular Gamma need not factor into independent arrays.
For each alias m put

    delta=log(u/(X^m v)), z=u-X^m v,
    K_m(delta)=exp(iT mL) exp(i(T+h*i_min)delta)
                         *sum_(j=0)^(rho-1)exp(i h j delta)/n.
    S_(F,ell,eps,cell,m;E)
       = sum_(u,v) Gamma(u,v) K_m(delta) 1_E(delta).         (4)

Choose the nearest m with delta in [-L/2,L/2), then partition E into the
unit window and its COMPLEMENT. Formula (3) is the real part of (4) summed
with weights c3,-A,-A,B,B. Each term keeps its own rho and i_min.
The carrier exp(iT mL) is indispensable. z is REAL in general: if X^m=a0/b0
in lowest terms, only b0*z=b0*u-a0*v is an integer, with its congruences.
There is no legal rounding to an unrestricted shift sum.

The effective product lengths for r positive/s negative visible primes are
N^r and N^s: k=r+s is 3,5,3,6,4 for D3,D5,Q3,D6,Q4 respectively.
The hidden prime does not change frequency length. In a unit alias window,
U asy X^m V. At exponent scales U=X^alpha,V=X^beta this requires
alpha-beta=m+O(1/L). Individual prime exponents must remain below
1-1/sqrt L, not merely satisfy the product constraint.

Use the geometric kernel only for the contiguous or canonical full section.
For arbitrary o(d) principal deletions, transfer the COMPLETE bounded signed
gate using the inherited Schatten theorem; do not transfer frequency-masked
estimates by inventing an interval kernel for the deleted section.

## 3. Quantitative unconditional bounds and a new application

The argument below specializes the integer-window method in
[the earlier near-alias audit](WP84_SIGNED_NEAR_ALIAS_ATTACK.md), Section 5.
Its new application is to the complete unit-log shared cubic window with
a summed denominator threshold; it is not a new general mean-value theorem.

For sufficiently large T, n>=XL/2 and the exact geometric series gives

    |K_m(delta)|<=min(1,1/(X*|delta|)).

On |delta|<=1, Y0=X^m v, one has u in [Y0/e,eY0] and
|log(u/Y0)|>=|u-Y0|/(eY0). There are at most three integers at distance
<=1 from Y0, and at most two per successive unit distance shell. Hence

    sum_u min(1,3Y0/(X*|u-Y0|))
      <=3+6Y0/X*(1+log(3Y0+2)).                            (5)

The summand is interpreted as 1 at equality. This treats exact and
arbitrarily close aliases uniformly, without a Diophantine premise.
For k distinct visible primes, coefficients have modulus <=2^k/sqrt(uv).
There are at most r!s! ordered representations, and sqrt(e)<2. Put
C=2^(k+1)r!s!. For a dyadic V0<=v<2V0 the COMPLETE unit window is bounded by

    C X^(-m/2) [3+6 X^(m-1) V0*(1+log(6X^m V0+2))].       (6)

This holds for m>=1; conjugate negative aliases exchange the sides. For m=0,
the forbidden exact equality u=v removes the nearest-integer term, leaving
the harmonic bound 6 C V0/X*(1+log(6V0+2)). Thus generic subcritical boxes
alpha+beta<2 by a fixed gap close, even after polynomially many dyadic boxes.
At alpha+beta>=2 these bounds do not vanish. Count first, sum second:
no wordwise-to-global inference is used. The Q terms have an additional
factor at most 2 for the complete hidden mass, eventually, because
2 sum |c_p|^2<=2. All path and pair placements are finite at fixed R.

For the cubic mixed first alias, sum (5) directly over ALL v<=Z, using its
two semiprime representations. Per path and mixed sign word the bound is

    E(X,Z)=96 X^(-1/2) H_Z
           +192 X^(-1/2) Z*(1+log(3XZ+2)),                  (7)
    Z=floor(sqrt X/L^3), H_Z=sum_(v=1)^Z 1/v.

This is O(L/sqrt X)+O(L^-2)=o(1). The absolute contribution to the joint
cubic sector is <=6*(c3*12001^2+20*A*12001^4)*E(X,Z).
It retains the entire unit-log first-alias window, original masks and all
phases. It removes an additional source-legal subset of D3* and Q3*.
It does NOT remove their |delta|>1 tails, even when v<=Z.
More generally (7) closes any Z=o(sqrt X/L), with Z<=N. For the stated
choice, once L>=24 and the source's eventual normalization/section bounds
hold, a completely explicit upper bound for E is
96 exp(-L/2)+48 L exp(-L/2)+192/L^3+384/L^2.
Indeed H_Z<=1+L/2 and log(3XZ+2)<=2L. No effective onset for a_phi->1 or
the section asymptotics is claimed, and the large fixed path multiplier
precludes inferring practical finite-height accuracy from this o(1) result.

For the same-sign cubic second alias, V=1,m=2,C=96. The per-path/orientation
unit-window bound is 288/X+576*(1+log(3X^2+2)). On the narrower
|delta|<=1/X it improves to 288+96/X: the integer interval has length <=3X
for X>=2, each coefficient including representations is <=96/X, and K<=1.
These are conservative absolute bounds, not positive lower bounds or signs.

## 4. Where the estimates stop, and literature applicability

| Legal range | Coherent integer width | Bulk divisor bound, ignoring fixed/log factors |
|---|---:|---:|
| cubic pq~X^(8/5), r~X^(3/5), alias 1 | X^(3/5) | X^(1/10) |
| cubic pqr~X^2, each prime ~X^(2/3), alias 2 | X | 1 in the core; O(L) in unit window |
| fifth 2:3, both products ~X^(6/5) | X^(1/5) | X^(1/5) |
| sixth 3:3 or Q4 2:2, both products ~X^(6/5) | X^(1/5) | X^(1/5) |

The certificate lists individual exponents, all strictly below 1, proving
these boxes are eventually allowed by the natural cutoff. It asserts no
fabricated count of prime solutions. In the first row, fixing p~X^(4/5)
leaves a q interval of width X^(-1/5); ordinary PNT on q is no estimate
for the dilated thin-strip correlation. At alias 2, fixing two primes
~X^(2/3) leaves width X^(-1/3) in the third. This explains why the marginal
PNT measure cannot replace the actual product correlation.

The following applicability checks use primary sources; no unmatched
theorem constant is imported into the budget.

* [Montgomery--Vaughan, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
  Theorems 1--2 and Corollaries 2--3, requires the appropriate modular or real
  frequency gaps. The sampled problem uses log(u/v)/L modulo 1. In the first
  hard box, distinct ratios only have the integer-determinant guarantee at
  scale X^(-11/5), below 1/T; a spacing-only normalized loss can grow like
  X^(6/5). A continuous mean value does not erase a sampled alias. Product
  polynomial lengths N^2 or N^3 are not o(T). No useful negative charge follows.
* [Evans, Correlations of Almost Primes](https://arxiv.org/pdf/2102.12297),
  Theorems 1.3--1.4, gives almost-all additive-shift correlations, including
  prime/E2 with shift-average length at least x^(1/6+epsilon). Here the
  relation is pq near X*r, at unequal scales, with the exact path weights,
  carrier and selected exclusions. Neither this dilation nor exceptional
  shifts with these weights has been transferred to that theorem.
* [Teravainen, Almost Primes in Almost All Short Intervals](https://arxiv.org/abs/1510.06005)
  concerns almost-all interval existence. It supplies no uniform signed
  weighted value at this prescribed moving center. No such value is inferred.
* Type I/II or multilinear exponential methods require a proved estimate
  for these coupled thin supports. On |delta|<=1/(100T), canonical root times
  t in [T,2T] satisfy cos(t delta)>=4999/5000. Root oscillation alone cannot
  supply cancellation there; the common carrier can rotate the sum.
* Dispersion/Cauchy produces off-diagonal correlations between two of the
  same masked arrays and a product of their carrier kernels. Their estimate
  is an additional theorem, not a consequence of covariance or second mass.
  Character/spectral large sieves require a justified modulus/spectral
  transform, not available in this reduction. The existing detailed
  [restricted-correlation audit](WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md),
  Sections 7--8, records those unresolved interfaces.

These checks reject the stated applications, not every conceivable use of
bilinear analysis. No literature-derived numeric constant is claimed where
its hypotheses fail. Equations (5)--(7) have explicit source-normalized
constants and complete proofs, independent of such an import.

## 5. Shared cubic sign: precise unknown correlation

The exact covariance contraction from the previous audit remains

    c3 D3-A Q3 = tau[(c3 I-5A D)Y^3]-5A tau[V(Y)Y^2]+o(1),
    D=E W^2, V(H)=E[W H W],                                (8)

conditional on the proved bounded-gate PNT replacement. Equation (8) is
UNMASKED: no near-alias projection of its o(1) error is presumed. W has the actual
source pair covariance, not a proposed law of Y. Although D>=I/6 and
c3-5A/6=-20362931/69562500<0, Y^3 is indefinite. The centered period-four
Loewner-form counterexample and its negation in the preceding report preserve
the first two moments and reverse (8). They refute a covariance-only sign
inference, not the prime arithmetic claim.

The actual sampled kernel is a Gram kernel on the union of product
frequencies, but the cubic mixed expression is a CROSS block between
semiprime and prime feature vectors, with the original masks. Even the
positive definite matrices [[1,1/2],[1/2,1]] and [[1,-1/2],[-1/2,1]] have
opposite cross signs and the same diagonal and determinant 3/4. A near-alias
restriction gives no extra positivity. Thus the missing quantity is the
real, carrier-weighted cross-correlation of these specific arithmetic
vectors, together with its fifth-order path contraction; coefficient
negativity supplies no bound on it. The same-sign sector similarly pairs
a triple-product vector with the constant sampled vector after folding.

## 6. Numerical ledger and decision

| Established step | Asymptotic consumer error | Constant signed saving |
|---|---|---:|
| previous low-product and exact cubic-alias removals | o(1) | 0 |
| new v<=sqrt X/L^3 mixed unit-window removal | explicit (7) times joint multiplier ->0 | 0 |
| Gram/covariance identity | conditional algebraic equality | 0 |
| remaining critical/supercritical boxes and far tails | no small one-sided bound | none proved |

The earned second-moment margin (2) is preserved, not earned again. After
the new removal, the narrowest required theorem is still the one-sided
bound (3) by Jcap-B Pair6_6000-kappa-eta, with the starred cubic terms now
excluding the subset in (7). The first unresolved cubic ranges are the
first-alias mixed window v>sqrt X/L^3 and the same-sign second-alias window,
plus all surviving tails. An upper estimate of zero for the entire residual
would itself fall short by MORE than g=0.002057354918974498...+kappa+eta.
No proved constant improvement reduces this gap.

**Recommendation: NO-GO for further formal regrouping or norm-only work on
this route.** Resume only with a source-matched signed dilated prime-product
correlation theorem, or a proved aggregate signed estimate paying these
windows AND the tails in the joint budget. Their failure is presently an
unavailable estimate, not an explicit counterexample to the prime inequality.
Stop speculative branches here.

Prime-to-Weil identification and zero-side block/tail/count transfer remain
separate obligations. Proper-power and arbitrary good-section high-moment
transfer retain their bounded-complete-gate hypotheses. No Gaussian/GUE
substitution, new consumer, or unconditional strict >79 claim is made.

## Replay

Run `python src/wp84_high_product_feasibility.py` and independently
`python src/wp84_high_product_feasibility_replay.py`. The latter recomputes
the consumer and margin, verifies five exact exponent budgets, rational
distance-shell tests, denominator clearing, the Gram obstruction and ten
hostile mutations without importing the producer. These finite checks
supplement the analytic proof of (5)--(7); they do not extrapolate prime data.

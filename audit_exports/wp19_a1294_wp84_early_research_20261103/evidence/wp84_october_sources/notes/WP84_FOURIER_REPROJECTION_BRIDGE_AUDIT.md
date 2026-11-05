# WP84 — Fourier reprojection bridge audit

Date: 2026-10-06. Base: 908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5.

Status: **CLOSED deterministic sharp-word bridge; OPEN its unbanded weighted
prime aggregation; FALSIFIED exact finite-d identification.**

The prior audit commit c3f38619c4d1b534c58b91e990b5a44fd220e599 was inspected
with git show, not cherry-picked. Its finite-d counterexample and frozen
consumer budget are correct. The counterexample does not disprove asymptotic
reprojection. This note supplies that deterministic asymptotic theorem.

## 1. CLOSED: Fourier coefficients from first principles

Use H=L2([0,L]), e_n(x)=L^(-1/2) exp(2pi i n x/L), n in Z. Translations
below may be read as circular translations on H; their interval multipliers
ensure that sharp partial translations agree with zero-extension translations.
Let J=[a,a+ell] subset [0,L], 0<=ell<=L, and W=M_(1_J) T_Y. For a partial
translation require x+Y to stay in [0,L] whenever x in J. Then

    <e_m,W e_n> = exp(2pi i n Y/L) j_(n-m),
    j_0 = ell/L,
    j_r = [exp(2pi i r(a+ell)/L)-exp(2pi i r a/L)]/(2pi i r), r!=0.

Proof: substitute e_n(x+Y) into L^(-1) int_J exp(-2pi i m x/L) e_n(x+Y)
with the normalizing square roots canceled. In particular

    |j_r| = |sin(pi r ell/L)|/(pi |r|) <= 1/(pi |r|).

Empty intervals give zero. Unit-modulus prime carriers do not change norms.
No prime distribution theorem is used here.

## 2. CLOSED: exact leakage series and rigorous uniform constant

Let P_d project onto any d consecutive Fourier modes and Q_d=I-P_d. Put
theta=ell/L. Then exactly

    ||Q_d W P_d||_HS^2
      = (2/pi^2) sum_(r>=1) min(d,r) sin^2(pi r theta)/r^2.

For positive lag r exactly min(d,r) pairs (m,n) cross one end of the mode
interval; negative lag gives the other end. The n-dependent translation
phase has modulus one. This proves the formula by Parseval and pair counting.

Therefore, writing H_d=sum_(r=1)^d 1/r,

    ||Q_d W P_d||_HS^2
      <= (2/pi^2)[H_d + d sum_(r>d) 1/r^2]
      <= 2(H_d+1)/pi^2 = B_d.

The last step is the integral bound sum_(r>d) r^-2 <= 1/d. The same estimate
holds for Q_d W* P_d since the adjoint is another interval translation.
The candidate constant in the request is thus rigorous, though not claimed
optimal. At theta=1/2 the series is pi^(-2) log d+O(1), so a uniform O(1)
leakage bound is FALSIFIED. The logarithmic order is necessary.

## 3. CLOSED: fixed-b sharp-word reprojection theorem

Let U_1,...,U_b be sharp partial translations, each a contraction, and define

    C_b=P U_1 P U_2 P ... P U_b P,
    F_b=P U_1 U_2 ... U_b P.

Products of consecutive sharp partial translations are again M_J T_Y with
J an interval (possibly empty): J is the intersection of the translated
admissible intervals. Thus the leakage theorem applies to every suffix.

An exact telescoping identity is

    C_b-F_b
      = -sum_(j=1)^(b-1)
          P U_1 P ... P U_j Q (U_(j+1)...U_b) P.

For a summand put A=P U_1 P ... P U_j Q and B=Q(U_(j+1)...U_b)P.
Then ||A||_HS=||A*||_HS <= ||Q U_j* P||_HS <= sqrt(B_d), since the other
compressed factors are contractions. The suffix estimate gives
||B||_HS<=sqrt(B_d). Schatten Cauchy--Schwarz gives |tr(AB)|<=B_d. Hence

    |tau_d(C_b)-tau_d(F_b)|
      <= (b-1)B_d/d
      = 2(b-1)(H_d+1)/(pi^2 d).

This is uniform in shifts, interval lengths, carrier phases, and the location
of the consecutive Fourier section. It is O_b(log d/d). For b=1 the error is
zero. It concerns actual repeated compression; it is not merely an overlap
identity.

## 4. CLOSED: independent finite-d counterexample check

For d=2, Y=L/2 and J=[0,L/2], the matrix of P U_Y P is

    [ 1/2   -i/pi ]
    [ -i/pi -1/2  ].

The closed pair satisfies

    tau((P U_Y P)(P U_-Y P))=1/4+1/pi^2,
    tau(P U_Y U_-Y P)=1/2.

The discrepancy is exactly ||Q U_-Y P||_HS^2/d=1/4-1/pi^2. It tends to zero
when the section dimension grows; for general d the exact leakage series
gives the difference. No correction to the prior finite-d witness is needed.

## 5. OPEN: unbanded weighted prime aggregation

For the sharp prime operator

    A=sum_(n<=N) sum_(epsilon=+,-) c_n exp(i epsilon T log n) U_(epsilon log n),
    c_n=-Lambda(n)/(a_phi L sqrt(n)),

the exact unbanded aggregate error is

    E_b = d^(-1) tr((P A P)^b-P A^b P)
        = -d^(-1) sum_(j=1)^(b-1) tr(P A P ... P A Q A^(b-j) P).

The j-th term has j copies of A in its prefix. Equivalently it is the finite
sum over signed prime-power tuples of product_j c_(n_j) exp(i T Y), times
the difference of the repeated and single-compression word traces.

Applying Section 3 wordwise gives only

    |E_b| <= (b-1)B_d/d * [2 sum_(n<=N)|c_n|]^b.

For ordinary primes, partial summation of the PNT gives
sum_(p<=N) log(p)/sqrt(p) ~ 2sqrt(N), so the coefficient l1 mass is
asymptotic to 2sqrt(N)/(a_phi L). At N=T exp(-sqrt(L)+o(1)), L~log T,
the displayed upper bound has scale

    O_b( N^(b/2)/(T L^b) ),

which diverges for b=5,6. This demonstrates failure of this estimate, not a
counterexample to the aggregate error itself. Prime-square second mass does
not control powers of A in the unbanded Schatten bound. That weighted sharp
bridge remains OPEN.

## 6. CLOSED: fixed R is an operator filter, not just endpoint compression

Let B_R keep Fourier matrix entries with |m-n|<=R on the ENTIRE Fourier
space (m,n in Z), and put V_(y,R)=B_R U_y. If J_y is the sharp admissible
interval, then exactly

    V_(y,R)=M_(phi_(y,R)) T_y,
    phi_(y,R)=F_R(1_(J_y)),

where F_R is the Fourier partial-sum operator on the circle. This follows
directly by cutting off j_(n-m) in Section 1. Thus the finite hard-band block
is P V_(y,R) P, and the natural single-compression comparison is the product
of these FILTERED translations, not the original sharp U_y word.

For a filtered word, with physical prefixes p_0=0, p_j=sum_(h<=j)y_h,

    Omega_(b,R)(y)
      = L^(-1) int_0^L product_(j=1)^b phi_(y_j,R)(x+p_(j-1)) dx,
    tau_d(P product_j V_(y_j,R) P)
      = Omega_(b,R)(y) D_d(Y/L).

A section starting at Fourier index k_- adds exp(2pi i k_- Y/L). Prime
carriers add exp(i T Y). These are exact identities. The new Omega is not
the sharp spread overlap, and finite Fourier partial sums need not be positive.

## 7. FALSIFIED: sharp-overlap replacement at fixed R has o_T(1) error

Take a single closed pair y=L/2,-y. For d>R,

    tau_d((P V_(y,R) P)(P V_(-y,R) P))
      = 1/4+(2/pi^2) sum_(1<=r<=R, r odd) (1-r/d)/r^2.

Its limit is 1/2-g_R, where

    g_R=(2/pi^2) sum_(r>R, r odd) 1/r^2 > 0.

The sharp single-compression trace is 1/2. At R=0 the gap is exactly 1/4;
at R=1 it is 1/4-2/pi^2 > 0. These are minimal two-factor witnesses.
At the working even R=6000, integral comparison gives

    1/(pi^2*6001) <= g_6000
      <= 1/(pi^2*6001)+2/(pi^2*6001^2).

So even at R=6000 the sharp-kernel replacement carries a nonvanishing fixed-R
loss, approximately 1.6887e-5 for this pair. This is not a fifth- or sixth-
moment loss estimate. It cannot be inserted as eps5 or eps6.

Filtering also removes the sharp no-wrap support restriction. For the
same-sign pair y=L/2,y=L/2 the sharp product is zero (its admissible interval
is empty), but the filtered overlap is exactly g_R. Its total shift is L,
so D_d(Y/L)=D_d(1)=1, with prime carrier exp(i T L). Thus sharp same-sign
annihilation cannot be imported into the fixed-band expansion. Whether
arithmetic summation suppresses these wrap terms is OPEN.

The deterministic sharp-word bridge is CLOSED. The weighted fixed-band bridge
to FILTERED words is treated separately in WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md.
Transport to the public sharp C5/C6 kernels remains OPEN.

## 8. CLOSED algebra / CONDITIONAL consumer budget

Independently squaring the frozen centered cubic reproduces c4=0,
c5=-11501/12500 and c6=137641/250000. Subtracting its exact moment cap,
variance-deficit charge and full-to-band charge from 21/200 gives

    (11501/12500) eps5+(137641/250000) eps6
      < 52897896569489/572357731837500000.

The single-error limits are respectively

    52897896569489/526614901909047000 = 0.00010044891699366519...,
    52897896569489/315119562271381350 = 0.0001678661146524863... .

The scalar budget is CLOSED; its application to a zero theorem is CONDITIONAL
on the analytic and arithmetic inputs. Neither the one-word estimate nor the
two-factor g_R witness supplies aggregate fifth/sixth losses.

## 9. R400 impact audit

The requested SAFE / NEEDS BRIDGE / NOT LOAD-BEARING terms below classify uses,
not theorem evidence status; evidence labels remain CLOSED / CONDITIONAL /
OPEN / FALSIFIED.

| Source/use | Classification | Evidence / reason |
| --- | --- | --- |
| CONTINUOUS_SPREAD_DIRICHLET_TRACE Sections 1–2, single compression formula | NOT LOAD-BEARING in isolation | CLOSED for P(product U)P |
| Same note Sections 3–6, identifying that expression with actual matrix words and arithmetic selection | NEEDS BRIDGE | Exact identification FALSIFIED; sharp one-word asymptotic now CLOSED; weighted and fixed-R sharp matching OPEN |
| FIXED_SCALE_CONNECTED_KERNEL Sections 1–3, Brownian factorization | NOT LOAD-BEARING in isolation | CLOSED kernel algebra; no repeated projections retained |
| Same note Sections 4–6, actual connected trace sign | NEEDS BRIDGE | OPEN for the actual fixed-band filtered kernel |
| CROSS_SCALE_SHARP_DETUNING Sections 1–6, sharp overlap formulas | NOT LOAD-BEARING in isolation | CLOSED model geometry |
| Same note Sections 7–8, identifying actual residual | NEEDS BRIDGE | OPEN filter-to-sharp and connected-sector identification |
| DETUNING_COMMUTATOR_ENDPOINT Sections 1–2, rank-two identity for K | SAFE | CLOSED algebra for that exact Dirichlet Gram matrix; no projections removed |
| Same note Section 3, asserting the actual remainder is E o K | NEEDS BRIDGE | OPEN identification, independent of the valid commutator identity |
| GOOD_ENDPOINT_TRIMMING Sections 1–2, bounded-consumer row deletion | SAFE | CLOSED finite rank comparison; moments are not directly rank-stable |
| Same note Sections 3–5, conditional endpoint mean-square bound | SAFE as a statement about its stated Dirichlet families | CONDITIONAL on the correct families and their coefficient norm |
| Same note Sections 6–7, Connected_4<=o(1) and w_400 ceiling | NEEDS BRIDGE | OPEN actual filtered-word matching |
| R400_COMPLETE_WORD_LEDGER_REPLAY Section 6, pair covariance with finite lags | SAFE with respect to reprojection | Repeated finite matrix lags retained; other arithmetic assumptions are not certified by this classification |
| Same note Sections 3–5, importing spacing/proper-power conclusions into complete sums | NEEDS BRIDGE / aggregate estimates | OPEN unless summed estimates are proved in the retained finite convention |
| Same note Section 7, identifying nonpair trace with sharp connected overlap | NEEDS BRIDGE | OPEN; new selected-section filtered reprojection does not restore sharp-kernel sign |
| Same note Sections 8–9 and R400_FIRST_RECORD_ASSEMBLY | NEEDS BRIDGE for theorem use; arithmetic ledger SAFE | Numerical 68.820273... consequence is CONDITIONAL on the unproved connected bound |

Therefore the R400 connected-sector theorem also depends on a missing bridge.
It is not repaired just by proving the sharp one-word O(log d/d) estimate.
The 68.82% numerical assembly remains valid conditional algebra, not an
unconditional theorem.

## 10. Verification and what remains OPEN

The verifier independently checks interval Fourier entries, the exact
half-interval leakage series, finite-d counterexample, fixed-b numerical
words at degrees 2/5/6, the joint budget, and the fixed-R obstruction. Its
finite checks supplement the proofs above; they are not asymptotic proofs.

OPEN: unbanded weighted sharp aggregation; fixed-R filtered connected-kernel
transport; sufficient fifth/sixth moment bounds; unconditional R400 promotion.
No merge, rebase, push, cherry-pick, or change to main/Downloads is needed.

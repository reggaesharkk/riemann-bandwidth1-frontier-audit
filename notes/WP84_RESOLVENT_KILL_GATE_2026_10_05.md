# WP84 resolvent kill gate -- 2026-10-05

Status: **PARAMETRIC BOUNDED SIX-POLE FAMILY ACTIVE; FULL 79.627 FRONTIER RECOVERABLE WITHOUT AN UNBOUNDED FINITE-T CONSUMER**

No unconditional >79 theorem is claimed.

## 1. Exact structural facts already closed

- Every intermediate matrix in the Lindeberg path is Hermitian, so for
  nonreal z

      ||(H-zI)^(-1)|| <= 1/|Im z|

  deterministically.

- Prime-power blocks satisfy

      max_j ||B_j|| = O(1/L),
      sum_j ||B_j||^2 = O(1),
      sum_j ||B_j||^3 = O(L^-3)=o(1).

- The exact one-block resolvent identity reduces the bounded fixed-z problem
  to conditional first/second-order operators plus an o(1) cubic remainder.

- Non-cyclic translation-word traces obey the exact spread law

      tr(word)=max(0,N-(max partial_sum-min partial_sum))

  for closed words.

- o(d)-rank perturbations are invisible to the weak/Stieltjes limit:

      |m_A(z)-m_B(z)|
        <= pi rank(A-B)/(d Im z).

## 2. Closures already rejected

- scalar covariance/multiplication closure:
      centered m4=7/30 instead of 1/4;

- finite F/G unitary state:
      repeated evolution generates longer translation words;

- Radau beta values:
      surrogate evaluations, not moment-forced lower bounds;

- prolate sharp-window counting-statistic spectral identification:
      failed its low-order gates;

- raw finite higher-even moment route:
      exposed to the Proposition-R amplification barrier.

## 3. Exact polynomial half-line certificate

Let

    P(x)
      = 1
        - (43428/13891)x
        + (37704/13891)x^2
        - (9660/13891)x^3,

    g(x)=P(x)^2.

For the pinned model moments through degree six,

    integral g dnu = 1415/13891,

and the coefficient-sign identity gives

    g(x)>=1 for x<=0.

Therefore every representing probability measure on R satisfies

    nu((-infinity,0]) <= 1415/13891.

This is support-free.

## 4. Active bounded consumer family

For every fixed delta>=61 define

    F_delta(x)
      = (delta+1) g(x)/(g(x)+delta).

The delta=61 member remains the easiest baseline instance.

Then

    F_delta(x)>=1 for x<=0,

and

    0 <= F_delta(x) <= (1+1/delta) g(x).

Hence every pinned-moment model law satisfies

    integral F_delta dnu
      <= (1+1/delta) * 1415/13891.

The exact simple-zero ledger is

    S(delta)
      = 11061/13891 - 2830/(13891 delta).

Examples:

    delta=161    -> 79.5005569... percent
    delta=752    -> 79.6000051... percent
    delta=2871   -> 79.6200006... percent
    delta=9717   -> 79.6250001... percent
    delta=18577  -> 79.6260000... percent.

For a theorem valid for every fixed delta>=61,

    sup_delta S(delta)
      = 11061/13891
      = 79.62709668... percent.

Thus the full Christoffel headline is recoverable as the supremum of fixed
bounded rational consumers; no delta(T)->infinity and no unbounded finite-T
functional is required.

## 5. Six simple fixed poles for every fixed delta

For every delta>=61 the denominator

    P(z)^2+delta

has six simple nonreal roots satisfying the exact uniform strip bound

    |Im z_j|>1.

This is certified by an exact real/imaginary elimination and Sturm gate at
delta=61 together with continuity of the three real branches of Re P=0;
larger delta only increases the required |Im P| target.

With residues

    c_j(delta)
      = -delta(delta+1)/[2 P(z_j)P'(z_j)],

we have

    F_delta(x)
      = delta+1 + sum_j c_j(delta)/(x-z_j).

Thus for each fixed delta the theorem target is one bounded statistic

    L_delta(T)
      = delta+1 + sum_j c_j(delta) m_{H_T}(z_j(delta)).

A sufficient theorem is

    limsup_T L_delta(T)
      <= (1+1/delta) * 1415/13891.

If proved for every fixed delta>=61, the final asymptotic coefficient reaches
79.62709668... percent by taking the supremum over the already-proved fixed
parameter inequalities.

No contour derivatives and no full limiting spectral law are required.

## 6. Order-four consistency gate

Any proposed operator-valued closure used to prove the six-pole inequality
must pass the exact order-four model check.

The pair sector is

    2*t_adj + t_opp
      = 2*(7/60)+1/30
      = 4/15.

The connected core is

    Phi4=-1/60.

Therefore

    centered m4
      = 4/15 - 1/60
      = 1/4.

The exact latest-block decomposition locates:

- every 2+2 pair word in the second-order sector A2;
- every four-distinct word in the first-order history A1;
- mixed 2+1+1 words across both.

Hence a static covariance-only law cannot close the theorem.

## 7. Proposition-R firewall

The order-four coefficient is a **model/generator consistency gate only**.
Do not prove the theorem by extracting finite-T raw theta^4 derivatives.

The theorem itself stays at the six fixed nonreal poles of F_61.

Bounded rational probes may recover moments only **after** a limiting law has
been identified; see

    notes/WP84_BOUNDED_RATIONAL_MOMENT_RECOVERY.md.

## 8. Current analytic debt

For arbitrary fixed delta>=61, at each of its six poles z_j(delta), use the exact permutation-Lindeberg identity

    m_H(z_j)-m_S(z_j)
      = -A1(z_j)+A2(z_j)+o(1).

The remaining task is to prove the **weighted six-pole inequality**

    limsup_T
      [delta+1 + sum_j c_j(delta)(
          m_S(z_j)-A1(z_j)+A2(z_j)
      )]
      <= (1+1/delta) * 1415/13891.

The active attack must preserve:

1. the alternating/crossing 2+2 word geometry;
2. the connected non-pair state memory;
3. the actual prime-block arithmetic interface.

That six-pole scalar inequality is the current kill gate.


## 9. Parametric bounded-frontier principle

The full headline does not require a single nearly-unbounded consumer.

It is enough to prove one theorem schema:

    for every fixed delta>=61,
    the six-pole bounded resolvent comparison holds.

Then each fixed delta gives one valid asymptotic simple-zero lower bound and
the supremum over delta recovers

    11061/13891
      = 79.62709668... percent.

See:

    notes/WP84_BOUNDED_CHRISTOFFEL_LADDER.md
    src/wp84_bounded_christoffel_ladder.py
    src/wp84_bounded_christoffel_family_pole_gate.py


## 11. Jensen-sharpened bounded frontier

The exact bounded optimum associated with the degree-6 Christoffel square is

    F_star(x)=min(P(x)^2,1).

It satisfies

    0<=F_star<=1,
    F_star(x)=1 for x<=0,

and concavity of h(t)=min(t,1) gives

    integral F_star dnu
      <= min(integral P^2 dnu,1)
      = 1415/13891.

Thus the full 79.62709668... coefficient already has a bounded continuous
consumer.

For the analytic rational family

    F_delta=(delta+1)P^2/(P^2+delta),

the sharper universal model cap is

    h_delta(w0)
      = (delta+1)w0/(delta+w0),

not merely (1+1/delta)w0.

The rational family remains the preferred fixed-resolvent interface because
each member has only six simple nonreal poles.

See:

    notes/WP84_BOUNDED_CHRISTOFFEL_JENSEN.md
    src/wp84_bounded_christoffel_jensen.py

## 12. Connected-memory provenance

The permutation state at subset size k is a uniform k-subset of the fixed
block family.

For every fixed block word using r distinct labels,

    E inclusion weight
      = (k)_r/(M)_r.

The one-step generator weight is exactly

    Delta[(k)_r/(M)_r]
      = r (k)_(r-1)/(M)_r.

At order four this leaves the r=3 and r=4 distinct-label sectors alive in the
exact evolving first/second-order state.

Therefore

    sum_j ||B_j||^3=o(1)

does not force a Wick/Gaussian fourth moment.  The connected model value
Phi4=-1/60 can be carried by state memory inside the exact D1/D2 evolution.

The still-open theorem is to transport the retained arithmetic symmetric word
sums to that connected model value.

See:

    notes/WP84_FINITE_POPULATION_STATE_LAW.md
    src/wp84_finite_population_word_weights.py

## 13. Bounded >80 extension

The order-4 Christoffel minimizer Q for the one-sided k=8 surrogate obeys,
throughout the feasible parametrization

    L=L0+t,
    U=F8(L)+eta,
    t,eta>=0,

the exact sign pattern

    q1<=0,
    q2>=0,
    q3<=0,
    q4>=0.

Hence

    Q(x)>=1 for x<=0,

so the one-sided k=8 certificate is support-free.

If

    m7_actual>=L,
    m8_actual<=U<T80(L),

then

    integral Q^2 dnu_actual
      <= lambda4(L,U)
      < 1/10.

Thus the conditional >80 consumer is valid on the whole real spectral line.

Moreover for fixed delta define

    F_{delta;L,U}
      =(delta+1)Q^2/(Q^2+delta).

This bounded consumer certifies >80 whenever

    delta
      > 9 lambda4/(1-10 lambda4).

At the exact midpoint diagnostic

    L=19.136,
    U=(F8(L)+T80(L))/2,

one has

    lambda4=1415/14409

and delta=50 already gives the exact bounded simple-zero ledger

    115507/144373
      = 80.00595679... percent.

This is a consumer-side theorem only.  The new analytic debt is a
rank-robust bounded transport of one-sided m7/m8 information.

See:

    notes/WP84_BOUNDED_K8_SUPPORT_FREE_80.md
    src/wp84_bounded_k8_support_free_80_gate.py


## 14. Same-sign branch must remain active

An exact finite sharp-model calculation now falsifies automatic V-sum
cancellation once the intermediate resolvent is the true inverse of a shift
operator.

For the five-dimensional non-cyclic shift S, with

    H=S+S^*,
    R=(H-iI)^(-1),

exact Q(i) arithmetic gives

    tau(RSR)+tau(RS^*R) = 7 i/20,

    V_sum
      = tau(RSRSR)+tau(RS^*RS^*R)
      = 17 i/80,

    V_diff
      = tau(RSRS^*R)+tau(RS^*RSR)
      = 3 i/80.

Thus V_sum can exceed V_diff.  Carrier oscillation, adjoint symmetry, and the
diagonal multiplication surrogate cannot justify removing it.

See:

    notes/WP84_VSUM_EXACT_FALSIFIER.md
    src/wp84_vsum_exact_falsifier.py

## 15. Model-first >80 gate

Before opening any new k=8 arithmetic transport, compute the exact model pair

    (M7,M8)

and evaluate the exact degree-4 Christoffel gate.

PASS requires

    M8<T80(M7).

FAIL means the present k=8 consumer cannot cross 80 and must be redesigned.

See:

    notes/WP84_K8_MODEL_GONOGO.md
    src/wp84_k8_model_gonogo.py

## 16. Arithmetic raw m7/m8 transport is optional on the bounded route

If the exact model pair passes the >80 gate, freeze its degree-4 minimizer Q
and one finite bounded rationalization

    F=(delta+1)Q^2/(Q^2+delta)

with model expectation below 0.1.

The arithmetic theorem may then compare this bounded functional directly at
its eight fixed nonreal poles.

Finite-T arithmetic m7/m8 bounds are therefore sufficient but not necessary
for the rank-robust >80 route.

See:

    notes/WP84_K8_BOUNDED_RESOLVENT_BYPASS.md


## 14. Same-sign order-four resonance gate

The exact noncommuting witness shows that V-sum need not vanish for an
arbitrary state. The actual permutation path has an additional arithmetic
selection rule: the current block is excluded from the previous subset and
sharp translation trace requires exact displacement closure.

For a current prime p, two same-sign insertions contribute p-exponent +2.
At theta^4 there are two previous block occurrences. Unique factorization
forces any resonance to use proper powers p^b,p^c with

    2 + eps1 b + eps2 c = 0,
    b,c>=2.

The complete solution pattern has

    |b-c|=2,
    b+c>=6.

Hence the resonant fixed-degree weight is

    O((log p)^4/(L^4 p^4)),

and summing over p is O(L^-4).

Current proper-prime-power blocks have total square mass O(L^-2).

Therefore the sharp order-four V-sum sector is o(1). The crossing repair
t_opp=1/30 and Phi4=-1/60 must be carried by the mixed-sign / evolving-state
sectors, not by order-four same-sign variance.

This is only a fixed-degree result. The full bounded-resolvent V-sum still
requires control of longer resonance families.

See:

    notes/WP84_ORDER4_VSUM_PRIME_RESONANCE.md
    src/wp84_order4_vsum_prime_resonance.py

## 15. k=8 model screening before transport

Write

    L=L0+t,
    m8=F8(L)+eta.

The exact >80 corridor is

    eta < (2666160/10471) t^2.

This should be used as a model-side screening test before theorem-grade
transport.

The exact C7 / {5,2} model program is valuable because it can decide the
actual (m7,m8) location. If lambda4(m7_model,m8_model)>=1/10, the present
degree-4 consumer cannot cross 80 regardless of transport quality.

See:

    notes/WP84_K8_80_GONOGO_MAP.md
    src/wp84_k8_80_gonogo_map.py


## 16. Self-contained endpoint closure from boundary evaluation channels

The endpoint quarantine no longer depends on a published DPSS theorem.

For a boundary strip I of physical width W, the concentration matrix

    Q_I=T_I^*T_I

has entries

    (Q_I)_{kl}
      =(1/L) int_I exp(i2*pi(l-k)x/L) dx.

A p-node Gauss-Legendre rule on I gives the positive rank-p matrix

    R_p
      =(1/L) sum_s omega_s v(x_s)v(x_s)^*.

With

    Z=pi(d-1)W/L <= TW/2,

polynomial exactness through degree 2p-1 and the real Taylor remainder imply

    ||Q_I-R_p||op
      <= (2dW/L) Z^(2p)/(2p)!.

Taking

    p=ceil(e Z)

gives the explicit bound

    ||Q_I-R_p||op
      <= (TW/pi) 4^(-p).

Hence the restriction map has a p-dimensional singular subspace with tail

    ||T_I(I-Pi_I)||op
      <= sqrt((TW/pi)4^(-p)),

while

    p/d
      <= e*pi*W/L+1/d.

For W=K log L, this is o(1) rank fraction and exponentially small norm tail.

Inserted into

    E_plus=T_left^* K_W T_right,

the real endpoint operator decomposes as

    E_endpoint=E_rank+E_small,

with

    rank(E_rank)/d=o(1),
    ||E_small||op=o(1),

even under the crude polynomial middle-operator bound and with no prime
cancellation.

This proof is self-contained except for standard p-node Gauss-Legendre
existence.  The previous DPSS argument is retained only as independent
corroboration.

The infinitesimal identity

    d/da Q([-a,a])
      = L^(-1)[v(a)v(a)^*+v(-a)v(-a)^*]

is the continuous reflection-pair boundary update underlying the construction.

See:

    notes/WP84_LRSC_BOUNDARY_QUADRATURE_TRANSFER.md
    src/wp84_boundary_quadrature_gate.py


## 17. Global taper-edge quarantine

The boundary-channel construction closes more than the endpoint layer.

Write

    phi=chi-r,

where chi is the sharp interval indicator and r is supported on the two fixed
physical taper ramps.

Retaining the finite-compression carrier omega_y=exp(iTy),

    A_y=omega_y M_phi U_y M_phi,
    S_y=omega_y M_chi U_y M_chi,

and exactly

    A_y-S_y
      = -M_r U_y M_chi
        -M_chi U_y M_r
        +M_r U_y M_r.

Summing over every prime first gives one middle translation operator K_+.
Every term in the complete ramp error still contains the **same fixed
boundary multiplier** M_r.

The self-contained boundary quadrature on the two width-w ramp strips gives

    P_actual
      = P_sharp + D_rank + D_small,

with

    rank(D_rank)/d=O(w/L)=o(1),

and

    ||D_small||op=o(1)

under only the crude polynomial bound on ||K_+||.

Therefore all bounded fixed-resolvent consumers may be analyzed on the sharp
**carrier-bearing finite-band** partial-translation operator.  The full-space
gauge does not preserve the compressed Fourier band and may not be used to
delete the factors exp(±iT log n).  This closes the old first-order
drift ramp-transfer debt as well as the variance ramp transfer.

See:

    notes/WP84_GLOBAL_RAMP_SHARP_BOUNDARY_QUARANTINE.md
    src/wp84_global_ramp_sharp_boundary_gate.py

## 18. Adaptive endpoint deletion

The endpoint strip width need not be K log L.

For every

    W->infinity,
    W/L->0,

the endpoint family y>=L-W has

    rank fraction O(W/L)=o(1)

and exponentially small complementary norm.

Thus one may choose, for example,

    W=sqrt(L),

and remove

    n>=X exp(-sqrt(L))

at zero asymptotic coefficient cost.

At lambda=1,

    X_ret/T
      <= exp(-sqrt(log T)+o(1)),

which beats every fixed negative power of log T.

More generally W=L^alpha, 0<alpha<1, gives retained ratio exp(-L^alpha).

This means any retained-range obstruction consisting only of fixed
polylogarithmic endpoint losses can be discharged before the arithmetic
resolvent analysis begins.

See:

    notes/WP84_TAPER_UNIVERSALITY_ADAPTIVE_ENDPOINT.md


## 19. Carrier-gauge correction

A hostile audit found that the full-space identity

    Q_T^* U_s Q_T
      = exp(iTy) U_s

does not yield a unitary equivalence inside the d-dimensional Gabor
compression, because Q_T does not preserve the projection P_d.

Therefore the active sharp finite operator retains the factors

    exp(+iT log n), exp(-iT log n).

This correction does **not** reopen the LRSC-derived boundary quarantine:
those phases have unit modulus and are absorbed into K_W/K_+ in every
absolute norm and rank factorization.

It does reopen any argument that attempted to dismiss carrier oscillation as
a pure gauge in the finite theorem problem.

See:

    notes/WP84_SHARP_CARRIER_GAUGE.md


## 16. LRSC-assisted displacement closure

The strongest transferable mechanism from the LRSC odd-ring work is not
ordinary low matrix rank.  It is boundary-evaluation / displacement rank.

For the sharp retained one-sided partial shift U_y^+ on the d-mode Fourier
band,

    [D,U_y^+]
      = i/(2*pi)
          [u_y 1^T - 1 u_y^T],

with

    D=diag(0,...,d-1).

Thus every current subset prime operator P_S satisfies exactly

    rank[D,P_S] <= 2,

independently of how many prime blocks are present.

The fixed-pole resolvent inherits the same structure:

    [D,R_S]
      = -R_S[D,P_S]R_S,

so

    rank[D,R_S] <= 2.

See:

    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md
    src/wp84_lrsc_displacement_rank_gate.py

## 17. Scalar Loewner / Calderon representation

Define the subset prime Dirichlet polynomial

    Q_S(tau)
      = sum_{n in S} c_n exp(i tau log n),

and write

    a=Im Q_S,
    b=Re Q_S.

On the Gabor grid tau_k=T+2*pi*k/L, the whole sharp subset prime matrix is

    P_S
      = M_{2b-2a'/L}
        + [M_a,J],

where

    J_kl = 1/[pi(l-k)]  (k!=l),
    J_kk = 0.

Equivalently,

    (P_S)_kl
      = [a(tau_k)-a(tau_l)]/[pi(l-k)]
      for k!=l,

and

    (P_S)_kk
      = 2b(tau_k)-2a'(tau_k)/L.

Thus the full d^2 matrix state is generated by one scalar analytic
Dirichlet polynomial and its first derivative.

See:

    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
    src/wp84_sharp_loewner_dirichlet_gate.py

## 18. D1/D2 no longer require a generic Gamma law

For one current block B and intermediate resolvent R put

    X=BR.

Then

    D1
      = d/dz tau(BR),

and

    D2
      = (1/2) d/dz tau((BR)^2).

Moreover

    rank[D,X] <= 4.

If

    C=[D,X],

then

    X_ij=C_ij/(i-j),  i!=j,

and exactly

    tr(X^2)
      = sum_i X_ii^2
        - sum_{i!=j} C_ij C_ji/(i-j)^2.

Hence the second-order Lindeberg state reduces to:

- diagonal entries of BR;
- at most four displacement generators;
- scalar discrete 1/(i-j)^2 transforms of those generators.

The previous bivariate transition measure Gamma is therefore not a necessary
state representation for the sharp model.

The open theorem is now the permutation-averaged limit of these scalar
generator statistics, not an arbitrary d^2 operator local law.

See:

    notes/WP84_D1_D2_DISPLACEMENT_REDUCTION.md
    src/wp84_d1_d2_displacement_gate.py

No unconditional >79 theorem is claimed.


## 20. Sign-balance near-resonance reduction

The exact continuous spread/Dirichlet trace identity can be sharpened using
integer spacing on the **smaller sign side** of a nonclosed translation word.

If

    Y=log(A/B)

and the positive/negative products use r_plus and r_minus retained factors,
put

    m=min(r_plus,r_minus).

When |Y|<=1 and A!=B, the side with only m factors is at most N^m.  Near
equality then forces both integers to be O(N^m), so

    |Y| >= c/N^m

and therefore

    |tau_d(word)| <= C N^m/T.

After the adaptive endpoint deletion N/T->0, every nonclosed sector with
m=1 vanishes uniformly.  This includes every nonclosed word through degree
three and every 3-vs-1 sign pattern at degree four.

The first finite-compression sector not killed by elementary spacing is
therefore the balanced degree-four window

    |log(n1*n2/(n3*n4))| <= O(1/T).

More generally, for N=T^(lambda+o(1)) the automatic-spacing condition is

    m*lambda<1.

For balanced degree k=2m this is exactly

    k*lambda<2,

matching the independently identified Rudnick--Sarnak / Proposition-R
threshold.

Thus the theorem-side arithmetic debt is now narrower: at lambda=1 the first
genuine near-resonance problem is the bounded-resolvent-weighted 2-vs-2
product-collision sector.  LRSC boundary/rank transfer does not remove this
balanced core and should not be asked to.

See:

    notes/WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE.md

No unconditional >79 theorem is claimed.


## 21. Connected Phi4 is purely supercritical product mass

The first balanced 2-vs-2 obstruction can now be localized exactly.

For a closed four-step vector define

    s=(|v0|+|v1|+|v2|+|v3|)/2.

This is the normalized balanced product logarithm:

    s=log A/L=log B/L.

An exact 32-chamber rational audit proves that the untruncated 26-term
connected b=4 kernel vanishes identically.

Every ordered-partition path has spread at most s.  Therefore when s<=1 no
positive-part cutoff activates, and the **actual** connected kernel vanishes
pointwise.

Consequently

    boxed:
    Phi4|_{s<=1}=0,
    Phi4|_{s>1}=-1/60.

Moreover the turn-on is quantitatively bounded by

    |C4(v)| <= 26 (s-1)_+.

This identifies the connected correction as a purely supercritical
product-length phenomenon, exactly beyond the k*lambda=2 wall.

See:

    notes/WP84_PHI4_SUPERCRITICAL_SUPPORT_THEOREM.md
    src/wp84_phi4_untruncated_cancellation.py

## 22. Published almost-prime correlation route for the supercritical sector

The balanced product kernel collapses exactly to a Dirichlet polynomial in
the product index m with coefficients given by a weighted two-almost-prime
convolution.

On a product block M<m<=2M the finite-compression near-resonance window is

    |h| ~< M/T.

Thus the connected supercritical sector is a weighted average of additive
correlations of Lambda*Lambda.

This is the same dispersion object isolated independently in WP70.

A published unconditional average-correlation theorem for E2 numbers
(N. Evans, 2023) treats weighted products of two primes over shift ranges

    log^(19+eps) M <= H <= M log^(-A) M

and its proof supplies an L2-in-h error estimate, which is the correct norm
for our bounded smooth Dirichlet kernel.

For every fixed s>1,

    M=T^(s+o(1)),
    H=M/T=T^(s-1+o(1)),

so the supercritical scale eventually lies well inside that theorem's
long-shift range.

For the **degree-four calibration sector**, the remaining bridge debt is:

1. adapt the E2 weight to the exact Lambda*Lambda / taper-cell coefficients;
2. sum factor slices with the finite-population weights;
3. control the shrinking threshold layer immediately above s=1, where
   |C4|<=26(s-1).

This does not yet close the full fixed-pole theorem: the bounded resolvent
contains all word degrees through the evolving intermediate state.  A direct
bounded generator/resolvent summation or a theorem-grade finite approximation
is still required.

See:

    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    src/wp84_balanced_product_kernel_gate.py

No unconditional >79 theorem is claimed.


## 23. Priority theorem rung: bounded four-pole delta=9

Before forcing the full six-pole 79.627% comparison, use the degree-2
Christoffel minimizer

    P2(x)=1-(7/4)x+(2/3)x^2,

for which

    integral P2^2 dnu = 5/36,
    P2(x)^2>=1 for x<=0.

The bounded family

    F_delta^(4)
      =(delta+1)P2^2/(P2^2+delta)

has four fixed nonreal poles and Jensen cap

    integral F_delta^(4)dnu
      <= 5(delta+1)/(36delta+5).

At delta=9 the model simple-zero ledger is exactly

    boxed:
    229/329
      = 69.604863222...%.

This is about 2.25 percentage points above the audited 67.3500037 level and
about 2.32 points above the 67.28005676 public/formalized level.

The four poles satisfy an exact strip bound

    |Im z_j|>1,

and numerically

    min |Im z_j| ~= 1.463361.

This rung remains Proposition-R safe because the theorem target is one
bounded combination of four fixed resolvents, not a finite-T raw fourth
moment.

Strategically this becomes the first record-beating theorem target:

    close F_9^(4)
      -> generalize fixed delta toward 13/18
      -> transfer the same bounded generator theorem to the six-pole
         degree-6 family
      -> 79.62709668... target.

See:

    notes/WP84_FOUR_POLE_RECORD_BEATING_RUNG.md
    src/wp84_four_pole_record_rung.py

No unconditional 69.6049% theorem is claimed yet.


## 24. D2 is now a one-dimensional 4x4 Fourier channel

The LRSC displacement reduction can be pushed one step further.

For

    X=BR,
    C=[D,X],
    rank C<=4,

the old formula

    tr(X^2)
      = sum_i X_ii^2
        - sum_{i!=j} C_ij C_ji/(i-j)^2

contained an apparent two-dimensional squared-Cauchy transform.

Let

    S2(t)=pi^2/3-pi t+t^2/2,
    0<=t<=2*pi,

so that

    S2(t)=sum_{r!=0} e^(irt)/r^2.

If C=G H^T with r<=4 and

    A(t)=H^T e^(itD) G,

then exactly

    boxed:
    sum_{i!=j} C_ij C_ji/(i-j)^2
      =
      (1/(2*pi)) int_0^(2*pi)
        S2(t) tr_r[A(t)A(-t)] dt.

Thus D2 no longer needs an O(d^2) transition object.  It needs a scalar
diagonal term plus a one-dimensional integral of matrices of size at most
4 by 4.

This is the strongest LRSC-style state compression obtained so far.

For the F9 record gate the next arithmetic object is therefore the
prime/subset average of a handful of 4 by 4 Fourier transforms at four fixed
nonreal poles, with

    |S2(t)|<=pi^2/3

available for one-sided domination.

See:

    notes/WP84_D2_FOUR_BY_FOUR_FOURIER_CHANNEL.md
    src/wp84_d2_fourier_channel_gate.py


## 25. Both D1 and D2 primitives are now small Fourier channels

The rank-four D2 reduction extends to a cross-displacement identity.

For arbitrary A,B,

    tr(AB)
      = sum_i A_ii B_ii
        - sum_{i!=j}
            [D,A]_ij [D,B]_ji/(i-j)^2.

Using the same periodic Bernoulli kernel S2, the cross term is one
one-dimensional Fourier integral.

Since

    rank[D,B_current] <= 2,
    rank[D,R] <= 2,

the primitive

    tau(BR)

whose z-derivative is D1 reduces to a diagonal pairing plus a 2 by 2 Fourier
channel.

Likewise

    rank[D,BR] <= 4,

so the primitive

    tau((BR)^2)

whose z-derivative gives D2 reduces to a diagonal-square term plus a 4 by 4
Fourier channel.

At the four F9 poles, ordinary Cauchy differentiation on fixed small circles
controls the z-derivatives without reintroducing a large matrix state.

The surviving theorem state is therefore:

    four fixed spectral poles
      x one scalar Fourier variable t
      x matrices of size at most 4 by 4
      + diagonal scalar statistics.

This is now the preferred analytic representation for the
69.6048632... model rung.

See:

    notes/WP84_D1_D2_SMALL_CHANNEL_CLOSURE.md
    src/wp84_cross_displacement_fourier_gate.py


## 26. Exact Bernoulliization removes fixed-cardinality subset combinatorics

The permutation average has an exact beta-integral representation.

For any current-base functional F(S,p),

    E_pi sum_k F(S_{k-1},p_k)

equals

    boxed:
    sum_p int_0^1
      E_{xi_q~Bernoulli(t), q!=p}
        F(S_t^(p),p) dt.

Thus the subset state is now encoded by the independent-mask scalar field

    Q_{t,-p}(tau)
      = sum_{q!=p} xi_q(t) Q_q(tau).

No approximation is involved, and the current base p remains excluded.

See:

    notes/WP84_BERNOULLI_PERMUTATION_BRIDGE.md
    src/wp84_bernoulli_permutation_bridge.py

## 27. BR displacement rank sharpens from four to three

For state scalar field a=Im Q_S and current field alpha=Im Q_B, put

    u=R1,
    v=Ra,
    w=R alpha.

Then exactly

    [D,BR]
      =(1/pi)[
        1 w^T
        +(Bv-alpha)u^T
        -(Bu)v^T
      ].

Hence

    boxed:
    rank[D,BR] <= 3.

Moreover with

    L_alpha=M_alpha K2-K2 M_alpha,
    (K2 f)_i=sum_{j!=i}f_j/(i-j)^2,

the D1 primitive is

    boxed:
    tr(BR)
      = sum_i beta_i R_ii
        +(2/pi^2) u^T L_alpha v,

and

    (BR)_ii
      = beta_i R_ii
        +pi^(-2)[
          u_i(L_alpha v)_i
          -v_i(L_alpha u)_i
        ].

So D1 is scalar and D2 needs at most a 3 by 3 Fourier channel.

See:

    notes/WP84_BR_RANK3_SCALAR_D1.md
    src/wp84_br_rank3_scalar_d1_gate.py

## 28. Current D2 block is ordinary-prime only up to o(1)

For one prime base p,

    Q_p(tau)
      = -(log p)/(aL)
          z_p(1-z_p^M)/(1-z_p),

    z_p=p^(-1/2)e^(i tau log p).

Thus grouped current blocks are exact finite geometric series.

Writing

    G_p=B_p+H_p

with B_p the ordinary-prime block and H_p the proper-power tail,

    sum_p
      ||G_p A G_p-B_p A B_p||
      =O(||A||/L^2).

Therefore the accumulated current D2/variance slot may use ordinary primes
only, with o(1) total error at fixed nonreal poles.

D1 does not admit this deletion by the same absolute argument and retains the
exact grouped Q_p.

See:

    notes/WP84_PRIME_BASE_GEOMETRIC_Q.md
    src/wp84_prime_base_geometric_q_gate.py

## 29. Exact Gaussian quadrature bridge removes same-sign variance by design

There is now an alternative to the permutation path.

For the ordinary-prime positive branch A_p define the two Hermitian
quadratures

    C_p=A_p+A_p^*,
    S_p=i(A_p-A_p^*).

Then exactly

    (1/2)(C_p X C_p+S_p X S_p)
      =A_p X A_p^*+A_p^* X A_p.

Hence an artificial Gaussian bridge with noise

    W=(1/sqrt2)sum_p(g_pc C_p+g_ps S_p)

has a **mixed-sign-only** covariance map.

Put

    H_t=S+tP_full+sqrt(t(1-t))W.

The endpoints are exactly S and S+P_full.

Gaussian integration by parts gives the exact identity

    boxed:
    m_{S+P_full}(z)-m_S(z)

      =int_0^1 [
          -E tau(R_t P_full R_t)
          +(1-2t)
            E tau(R_t V_mix(R_t) R_t)
        ] dt.

There is no Taylor remainder.

The bridge remains inside the same scalar-Loewner/displacement-rank-two class
sample by sample, but the old same-sign p^(+/-2iT) variance channel is absent
from this representation.

This does not solve the deterministic drift.  It removes one previously hard
variance object without changing the endpoint matrix.

See:

    notes/WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
    src/wp84_gaussian_quadrature_bridge_gate.py

## 30. Active choice of attack

Two exact representations now coexist:

A. **Bernoulli/current-exclusion path**
   - preserves the p-adic valuation firewall in D1;
   - current D2 reduces to ordinary primes;
   - no fixed-cardinality subset combinatorics.

B. **Gaussian quadrature bridge**
   - removes same-sign variance completely;
   - replaces subset combinatorics by a Gaussian scalar Dirichlet field;
   - leaves the deterministic full-prime drift as the central hard term.

The next kill test should attack the drift in both representations and keep
whichever gives the smaller source-closed bound at the four F9 poles.

No unconditional 69.6049% theorem is claimed yet.


## 31. Bernoulli D1 collapses to one complement operator

Under the full Bernoulli mask define

    P_sel=sum_p xi_p G_p,
    P_rem=sum_p(1-xi_p)G_p,

so

    H_t=S+P_sel,
    Q_rem=Q_full-Q_sel.

Conditioning on xi_p=0 reproduces the exact leave-one-out current-p state.

Because D1 is linear in the current block,

    boxed:
    A1(z)
      =
      int_0^1
        (1/(1-t))
        E[
          tau(R_t P_rem R_t)
        ] dt.

Thus the entire current-prime sum is replaced by one remaining sharp
Loewner operator with scalar field

    Q_rem
      =(1-t)Q_full-Z_t,

while

    Q_sel
      =tQ_full+Z_t.

The stochastic state therefore contains one centered scalar field Z_t, not a
family of current-prime functionals.

See:

    notes/WP84_BERNOULLI_D1_COMPLEMENT_COLLAPSE.md

## 32. Quadrature noise is a circular Gaussian Q-field

In the Gaussian bridge the two Hermitian quadratures combine into one
circular complex coefficient

    gamma_p=(g_pc+i g_ps)/sqrt2.

Hence

    Z_L(tau)
      =sum_p gamma_p q_p(tau)

has

    E[Z_L(tau)Z_L(sigma)]=0

and carrier-free conjugate covariance

    E[
      Z_L(tau) conjugate(Z_L(sigma))
    ]

      =
      1/(a^2L^2)
      sum_p (log p)^2/p
        exp(i(tau-sigma)log p).

On the Fourier grid this covariance is Toeplitz.

For fixed lag r it converges to

    K_infty(0)=1/(2a^2),

    K_infty(r)=1/(2*pi*i*r*a^2),
    r!=0,

whose physical symbol is simply

    s/a^2 on [0,1].

Thus the artificial noise is a fully explicit long-range Gaussian scalar
field and still satisfies rank[D,W]<=2 sample by sample.

See:

    notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md

## 33. Standard correlated-Gaussian MDE theorems do not black-box close the route

The Ajanki--Erdos--Kruger matrix-Dyson framework is a useful design guide,
but its standard hypotheses include flatness and fast correlation decay.

The WP84 mixed covariance is not flat, and its natural Fourier-grid
correlation has 1/|r| Cauchy decay.

Therefore those local laws cannot simply be cited as the missing theorem.

The advantage specific to WP84 is different:

    fixed pole distance about 1.46
      + exact displacement rank two
      + explicit covariance symbol.

The next candidate is a bespoke fixed-imaginary-part Dyson equation for the
small displacement generators, not a generic local law.

See:

    notes/WP84_MATRIX_DYSON_LITERATURE_AUDIT.md


## 26. D1 current average is one scalar complement polynomial

For a subset S of inserted prime bases, let

    Q_rem,S
      = (1/(M-|S|))
        sum_{p notin S} Q_p.

Then the conditional D1 current average is encoded exactly by

    alpha_bar=Im Q_rem,S,
    beta_bar=2 Re Q_rem,S - 2(Im Q_rem,S)'/L.

With

    u=R_S 1,
    v=R_S Im Q_S,

the primitive is

    E_{p|S} tr(G_p R_S)
      =
      sum_i beta_bar_i (R_S)_{ii}
      + (2/pi^2) u^T L_{alpha_bar} v.

Thus D1 has no per-current-prime state.

See:

    notes/WP84_D1_AGGREGATE_D2_PRIME_ONLY.md

## 27. Proper powers disappear from D2

Write

    G_p=B_p+E_p,

where B_p is the ordinary-prime block and E_p contains p^a, a>=2.

Uniformly at every fixed nonreal pole,

    sum_p
      |
        D2(H;G_p,z)-D2(H;B_p,z)
      |
      = O(L^-2).

This follows from absolute convergence of

    sum_p (log p)^2/p^(3/2)

and the fixed resolvent bound.

Therefore the theorem-side D2 current field may be taken to be one ordinary
prime exponential

    Q_p(tau)=c_p exp(i tau log p).

No proper-power covariance theorem remains.

## 28. D2 current/state exclusion decouples at o(1)

The actual permutation stage has p notin S.

A one-swap coupling to an independent current p and uniform k-subset S0
changes the state by G_p-G_q.

Because D2 contains G_p twice, the accumulated coupling error is controlled
by the block cube mass:

    total error
      =
      O_eta(
        L^-3 + X^(-1/2)
      )
      = o(1).

Hence the complete D2 path uses one deterministic full variance map

    V(A)=sum_p B_p A B_p,

with the current p independent of the subset state up to o(1).

See:

    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md

## 29. Exact continuous Bernoulli/Shapley flow

The permutation average itself has an exact Boolean-cube representation:

    F(full)-F(empty)
      =
      sum_p int_0^1
        E[
          F(S_t^(-p)+p)-F(S_t^(-p))
        ] dt,

where every q!=p is included independently with probability t.

Thus the theorem path can be indexed by one continuous parameter

    t in [0,1],

rather than M discrete hypergeometric stages.

After the one-block resolvent expansion, the accumulated cubic remainder is
still O(L^-3).

See:

    notes/WP84_SHAPLEY_BERNOULLI_FLOW.md

## 30. Resonant prime-square covariance constants are explicit

For the ordinary-prime current field

    alpha_p=c_p sin(tau log p),
    beta_p=2c_p(1-s_p) cos(tau log p),

the difference-frequency covariance at lattice displacement r has the exact
continuum values

    C_aa(0)=1/(4a^2),
    C_aa(r)=0                    (r!=0),

    C_ab(r)=0                    (all r),

    C_bb(0)=1/(6a^2),

    C_bb(r)
      = -1/(2a^2 pi^2 r^2)      (r!=0).

Thus the resonant beta covariance is literally a diagonal term plus the same
squared-Cauchy K2 kernel that arose from the LRSC displacement algebra.

There are no unknown resonant covariance constants.

See:

    notes/WP84_RESONANT_SCALAR_COVARIANCE.md

## 31. PNT upgrade removes the old fixed-r K2 objection

The classical PNT with zero-free-region error implies the stronger ordinary
prime-square asymptotic

    sum_{p<=x} (log p)^2/p
      =
      (1/2)(log x)^2
      + C0
      + exponentially small remainder.

After scaling x=e^(Ls), the cumulative prime-square measure differs from
s ds by only

    O(L^-2),

not merely O(L^-1).

Therefore any K2-weighted bilinear of state vectors with bounded normalized
l2 norms has discrete-to-continuum substitution error

    O(log d/L^2)
      = O(L^-1)
      = o(1).

This closes the growing-section passage for every resonant contribution that
can be rearranged into the K2 class.

The remaining resonant task is now purely algebraic:

    put the alpha/J pieces into K2-weighted bilinear form
    while using J only through its bounded l2 operator norm.

The carrier-2T fast/Hankel channel remains separate and open.

See:

    notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md

No unconditional record theorem is claimed yet.

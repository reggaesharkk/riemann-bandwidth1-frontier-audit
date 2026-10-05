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


## 32. Resonant D2 is now uniform over the growing Fourier section

The fixed-r covariance formulas have been upgraded to a uniform theorem for
the actual d~TL section.

For the sharp partial translations U_s^+, U_s^-,

    dU_s^+/ds
      = i 2*pi U_s^+ D - e(s) 1^T,

    dU_s^-/ds
      = -i 2*pi D U_s^- - 1 e(s)^*.

Therefore, for

    g_R(s)=tau(R U_s^+ R U_s^-),

the derivative collapses to one displacement-commutator term plus two
rank-one endpoint terms:

    g_R'(s)
      =
      i2*pi tau(
        U_s^- R U_s^+ [D,R]
      )
      - boundary_1
      - boundary_2.

The Montgomery--Vaughan large sieve applied to the subset Dirichlet
polynomial gives uniformly over every subset state

    ||Im Q_S(tau_k)||_2/sqrt(d)=O(1),

because retained prime-power frequencies have spacing
delta^{-1}=O(NL)=o(d) after endpoint quarantine.

Hence

    d^{-1}||[D,R]||_1=O_eta(1),

and both

    ||g_R||_infinity,
    Var(g_R)

are uniformly O_eta(1).

Abel summation against the square-prime measure therefore gives the
resonant continuum substitution with O_eta(L^-1)+o(1) error uniformly in
the state.

Thus the old fixed-r/growing-d gap in D2-res is closed.

See:

    notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md

## 33. The carrier-2T D2 channel is o(1)

The complementary same-sign covariance has frequencies

    tau_i+tau_j ~ 2T,...,4T.

A Vinogradov--Korobov prime-polynomial estimate (QJM 77 (2026), Lemma 2.6)
gives on every sufficiently large dyadic prime block

    |
      sum_{p~P} p^(-1-it)
    |
      <<
      P^(-sigma0)
      + L^3/T,

uniformly for the required |t|.

Choose

    log P0
      =
      K L^(2/3)(log L)^(4/3)

with K sufficiently large.

The normalized square-prime mass below P0 is o(1), while above P0 the
zero-free-region term is an arbitrarily strong negative power of L.

Restoring the log-square and degree-two slow weights costs only O(L^-1).

Consequently every fast alpha/beta covariance entry satisfies

    sup_{i,j}|C_fast(i,j)|=o(1).

Since the D2 primitive is quadratic in alpha,beta and every contraction is
against products of bounded resolvents and the uniformly bounded discrete
Hilbert transform J, Hilbert--Schmidt Cauchy--Schwarz gives

    boxed:
    D2_fast=o(1)

uniformly over the actual subset state.

Therefore:

    boxed:
    all current-prime arithmetic in D2 is closed.

The only surviving D2 main is the explicit resonant state functional.

See:

    notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md

## 34. Common-state Bernoulli generator

D1 and D2 combine more cleanly before taking the continuum limit.

Let H_t be the independent Bernoulli(t) subset state and R_t its resolvent.
Replacing the leave-one-out state by the common Bernoulli state inside D1
costs a second-order term; when combined with D2 it produces exactly the
factor

    1-2t.

Uniformly at fixed nonreal z,

    boxed:

    d/dt E tau(R_t)

      =
      - E tau(
          R_t P R_t
        )

      + (1-2t)
        E tau(
          R_t V_res(R_t) R_t
        )

      + o(1),

where

    P=sum_p G_p

is the full deterministic sharp prime operator and V_res is now an explicit
continuum variance channel.

Equivalently for any fixed bounded rational consumer f,

    d/dt E tau f(H_t)

      =
      E D[tau f(H_t)][P]

      + (1-2t)/2
        E sum_p
          D^2[tau f(H_t)][G_p,G_p]

      + o(1).

The current-prime leave-one-out state is gone from both terms.

See:

    notes/WP84_BERNOULLI_COMMON_STATE_GENERATOR.md

## 35. Frontier after the D2 closure

The arithmetic frontier is now materially smaller.

Closed:

- cubic-and-higher one-block Lindeberg debt;
- taper/ramp boundary quarantine;
- proper-prime-power D2 debt;
- current-prime exclusion in D2;
- D2 current dependence beyond second covariance;
- resonant prime-square continuum substitution;
- carrier-2T fast D2 covariance;
- D1/D2 large-matrix algebra down to displacement/small channels.

Still open:

1. the deterministic first-order drift
       E tau(R_t P R_t)
   for the full scalar-Loewner prime operator P;

2. the Bernoulli-state average/evolution of the explicit resonant D2
   functional coupled to that drift;

3. insertion of the resulting four-pole bound into the
       tau F9 < 0.1632499815
   record inequality.

So the kill gate has moved from
"prove a nonlinear prime-side resolvent law"
to
"close one explicit Bernoulli Loewner-resolvent flow with known second-order
generator."

No unconditional record theorem is claimed yet.


## 36. The full first-order drift is also a scalar Loewner statistic

The common-state drift

    tau(R_t P R_t)

contains the full deterministic prime operator P, but P has the same exact
scalar Loewner representation as every subset block.

Let

    alpha_*=Im Q_*,

    beta_*
      =2 Re Q_* - 2(Im Q_*)'/L,

for the full retained scalar prime polynomial Q_*.

For the Bernoulli state put

    a_t=Im Q_t,
    r_t=diag R_t,
    u_t=R_t 1,
    v_t=R_t a_t.

Then

    tau(P R_t)

      =
      d^(-1)
      [
        beta_*^T r_t
        + (2/pi^2)
          u_t^T L_{alpha_*} v_t
      ],

and therefore

    boxed:

    tau(R_t P R_t)

      =
      d/dz
      {
        d^(-1)
        [
          beta_*^T r_t
          + (2/pi^2)
            u_t^T L_{alpha_*} v_t
        ]
      }.

Thus the final D1 drift is not a generic d by d matrix operation.

Introducing

    m(t,theta,z)
      =
      E tau(
        H_t+theta P-zI
      )^(-1),

the common-state equation has the characteristic form

    partial_t m
      =
      partial_theta m
      + (1-2t)
        E D2_res_state
      + o(1).

The remaining theorem is now a limiting-state theorem for a finite list of
Loewner/displacement generator statistics at four fixed poles.

See:

    notes/WP84_FULL_DRIFT_SCALAR_LOEWNER.md


## 37. Bernoulli self-consistency removes the independent D1 theorem

The common-state equation from Section 34 can be sharpened again.

Let

    H_t=s_0 I + X_t,
    R_t=(H_t-zI)^(-1),

and define

    C_t=E tau(R_t X_t R_t).

Because X_t=H_t-s_0 I commutes with H_t,

    C_t
      =
      m_t(z)
      +(z-s_0) partial_z m_t(z)

exactly.

A one-coordinate Bernoulli calculation gives

    C_t
      =
      t A_t
      -2t(1-t)B_t
      +o(1),

where

    A_t=E tau(R_t P R_t),

and

    B_t=E sum_p tau(R_t G_p R_t G_p R_t).

Combining this with

    partial_t m_t
      =
      -A_t+(1-2t)B_t+o(1)

eliminates A_t completely:

    boxed:

    t partial_t m_t
      +m_t
      +(z-s_0) partial_z m_t
      +t B_t

      =
      o(1).

Since the D2 arithmetic work already gives

    B_t
      =
      E Xi_res(R_t)
      +o(1),

the common-state evolution is

    boxed:

    t partial_t m_t
      +m_t
      +(z-s_0) partial_z m_t

      =
      -t E Xi_res(R_t)
      +o(1).

Thus there is no separate D1 arithmetic theorem left.

Important warning: the characteristics send z toward the real axis as
t->0.  A proof must not integrate blindly to t=0 with only fixed-strip
resolvent bounds.

See:

    notes/WP84_BERNOULLI_DRIFT_ELIMINATION.md
    src/wp84_bernoulli_drift_elimination_gate.py

## 38. Matched Gaussian replacement of every intermediate Bernoulli state

Write the centered Bernoulli state as

    H_t
      =
      H_0+tP
      +sum_p eta_p(t)G_p,

with

    E eta_p=0,
    E eta_p^2=t(1-t).

Replace eta_p by

    sqrt(t(1-t)) g_p,

with independent standard real Gaussians g_p.

At every fixed nonreal spectral parameter the two scalar coefficients match
through second order, while one-coordinate resolvent replacement costs

    O_eta(||G_p||^3).

Since

    sum_p ||G_p||^3=o(1),

Lindeberg replacement yields uniformly for t in [0,1]

    boxed:

    E tau(H_t-zI)^(-1)

      =
      E tau(H_t^G-zI)^(-1)
      +o(1).

The same holds for every fixed z-derivative and every fixed bounded rational
consumer whose poles stay a fixed distance from the real axis.

Therefore the remaining state theorem may be studied in the Gaussian
Loewner ensemble with the same mean field and the already-explicit covariance
map.

This does not imply a scalar semicircle closure: the Gaussian matrix series
is still built from noncommuting partial-translation/Loewner blocks, so
crossing/connected geometry survives.

See:

    notes/WP84_BERNOULLI_GAUSSIAN_INVARIANCE.md
    src/wp84_bernoulli_gaussian_invariance_gate.py

## 39. Parallel one-point record rung

In addition to the four-simple-pole F9 consumer, there is now a smaller
parallel bounded consumer

    r_{2,a}(x)
      =
      1-
      [
        (x-a)^2/(x^2+a^2)
      ]^2.

It satisfies

    1_{x>0} >= r_{2,a}(x)

for every real x and is globally bounded in [-3,1].

At

    a=3/2,

the consumer is determined by only one upper-half-plane point and its first
z derivative:

    tau r_{2,3/2}(H)

      =
      2 Re[
        (3/2)(2+i)m_H(3i/2)
        -(9/4)m_H'(3i/2)
      ].

Against the current pinned six-moment extremal model its exact value is

    q
      =
      506616611216431521048
      /
      593746460699485818169

      =
      0.8532541156027985...,

giving model simple-zero ledger

    2q-1
      =
      0.706508231205597...
      =
      70.65082312...%.

To beat the audited 67.3500037 comparison it only needs

    tau r_{2,3/2}(H_T)
      >
      0.8367500185,

leaving model consumer margin

    0.0165040971027985... .

This is a model/consumer certificate, not an unconditional theorem.

It should be carried in parallel with F9:

- F9: four simple poles, no z derivative;
- scaled r2: one upper-half-plane point, one z derivative, larger model margin.

See:

    notes/WP84_SCALED_R2_RECORD_RUNG.md
    src/wp84_scaled_r2_record_rung.py

## 40. Authoritative frontier after the recovered failed-chat commits

The chat session that produced Sections 37--39 terminated at the UI layer,
but the Git commits landed successfully.  The branch state, not the failed
chat display, is authoritative.

The current mathematical frontier is now:

1. no independent D1 arithmetic theorem;
2. all current-prime D2 arithmetic closed;
3. Bernoulli intermediate states replaceable by matched Gaussian Loewner
   states at fixed bounded consumers;
4. remaining task: control the explicit noncommutative Gaussian/Loewner state
   functional strongly enough for either
       F9
   or
       r_{2,3/2}
   to cross the audited record threshold.

No unconditional record theorem is claimed yet.


## 37. Co-moving scaled-r2 update

For the Gaussian bridge

    H_t=s0 I+tP+sqrt(t(1-t))W,

transport the test function by

    f_t(x)=f(s0+(x-s0)/t).

Then

    t partial_t f_t+(x-s0)partial_x f_t=0,

and Gaussian integration by parts gives

    d/dt E tau f_t(H_t)
      =
      -1/2 E sum_j D^2[tau f_t(H_t)][E_j,E_j].

With u=(1-t)/t this is exactly

    E tau f_t(H_t)
      =
      E tau f(H_1+sqrt(u)W).

So the moving deterministic mean and first-order drift disappear together.

For

    r_2(x)=1-[ (x-1)^2/(x^2+1) ]^2,

the exact one-point identity is

    tau r_2(H)
      =
      2 Re[(2+i)m_H(i)-m_H'(i)].

The pinned model value is

    2575059657047327248/2914998924731524849
      =0.8833827124943086...,

giving model simple-zero ledger

    76.67654249886171...%.

Against the public 67.3500037087... line the positive-index threshold is

    0.8367500185439279...,

so the model consumer margin is

    0.0466326939503807....

This is now the preferred first bounded theorem rung.  F9 and a=3/2 remain
cross-checks.

The remaining analytic target is the one-point mixed-covariance heat flow at

    z=i

plus a uniform large-u truncation/boundary estimate.

See:

    notes/WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md

No unconditional record theorem is claimed.


## 37. Preferred first rung is now r2 at a=1

The scaled r2 reconnaissance has been superseded by the simpler member

    r2(x)
      = 1 - [ (x-1)^2/(x^2+1) ]^2.

Its exact model positive-index consumer value is

    0.8833827124943086...,

giving model simple-zero ledger

    76.67654249886171...%.

Against the audited 67.3500037 comparison, the positive-index threshold is

    0.8367500185439279...,

so the model consumer margin is

    0.0466326939503807....

The theorem consumes only

    z=i

and one z derivative:

    tau r2(H)
      =
      2 Re[
        (2+i)m(i)-m'(i)
      ].

Equivalently, with the Cayley defect

    B
      =
      I-Im[(H+iI)(H-iI)^(-1)],

one has exactly

    tau r2(H)
      =
      1-tau(B^2).

Thus the first record crossing is the positive energy estimate

    limsup tau(B_T^2)
      <
      0.163249981456072....

See:

    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_R2_CAYLEY_DEFECT_GATE.md

## 38. Long displacement tails can be removed before any word expansion

For the sharp Loewner form

    H
      =
      M_beta+[M_alpha,J],

let H^(R) keep only displacements |i-j|<=R.

Then

    Delta_R
      =
      H-H^(R)

satisfies exactly

    tau(Delta_R^2)
      <=
      8/(pi^2 R)
      [||alpha||_2^2/d].

The retained full prime field has

    ||alpha||_2^2/d
      =
      1/4+o(1)

after the already-closed degree-two nonresonance and high-frequency gates.

Therefore

    limsup_T tau(Delta_R^2)
      <=
      2/(pi^2 R).

Since r2 is globally Lipschitz, Hoffman--Wielandt gives

    lim_{R->infinity}
    limsup_{T->infinity}
    |
      tau r2(H_T)
      -
      tau r2(H_T^(R))
    |
      =0.

Thus the preferred bounded theorem does not require controlling arbitrarily
long Loewner displacements.

Large alpha sites can then be clipped by an o(d)-rank perturbation because

    |{i:|alpha_i|>M}|/d
      =
      O(M^-2).

This reduction is performed at the bounded-consumer level and does not
revive the Proposition-R raw-moment problem.

See:

    notes/WP84_R2_DISPLACEMENT_TAIL_TRUNCATION.md
    src/wp84_r2_displacement_tail_gate.py

## 39. After fixed-band truncation the one-point resolvent is exponentially local

With fixed displacement bandwidth R and clipped |alpha_i|<=M, the
off-diagonal hopping has row sum

    J0(R,M)
      <=
      (4M/pi)
      sum_{r=1}^R 1/r.

Choose

    theta
      =
      R^(-1)
      log(
        1+1/[2J0(R,M)]
      ).

Exponential conjugation gives the finite-section Combes--Thomas estimate

    boxed:
    |(H-iI)^(-1)_{jk}|
      <=
      2 exp(-theta|j-k|).

No bound on the diagonal beta field is needed.

Consequently both

    R_{jj}(i)

and

    (R(i)^2)_{jj}

are approximable from a finite window of radius S with error

    O_{R,M}(exp(-c_{R,M}S)).

Hence, after arbitrarily small band-tail and rank-quarantine errors,

    tau r2(H_T)

is the empirical average of one bounded local observable depending on only

    alpha_{j-S},...,alpha_{j+S},
    beta_{j-S},...,beta_{j+S}

for fixed finite R,M,S.

The remaining theorem is therefore a **finite local arithmetic law**, not a
global long-range matrix-Dyson law.

The recommended limit order is

    T -> infinity at fixed R,M,S,
    then S -> infinity,
    M -> infinity,
    R -> infinity.

At fixed R,M,S one may either:

1. prove the finite local joint law directly, preserving the known
   near-product connected corrections; or

2. approximate the bounded local observable by a fixed finite polynomial and
   invoke finitely many translation-word / almost-prime correlation gates.

This is now the preferred first-strike architecture.

See:

    notes/WP84_R2_FINITE_BAND_LOCALITY.md
    src/wp84_r2_finite_band_locality_gate.py

No unconditional record theorem is claimed yet.


## 40. One-point resolvent structure sharpens the band-tail error to O(1/R)

The earlier bounded-consumer truncation used Hoffman--Wielandt and gave only

    O(R^(-1/2))

for the r2 trace error.

For the preferred one-point consumer this is not sharp.

Let H_R keep only |i-j|<=R and put

    Delta=H-H_R,
    G=(H-zI)^(-1),
    S=(H_R-zI)^(-1).

Iterating the resolvent identity once gives

    G-S
      =
      -S Delta S
      + S Delta S Delta G.

The quadratic term is

    O_eta(
      tau(Delta^2)
    )
      =
      O_eta(R^-1).

For the linear term,

    tau(Delta S^2),

both factors acquire one displacement denominator:

    Delta_ij
      =
      (alpha_i-alpha_j)/
      [pi(j-i)],

    (S^2)_ji
      =
      [D,S^2]_ji/(j-i).

The banded commutator satisfies

    ||[D,H_R]||_F^2/d
      <=
      8 R q_alpha/pi^2,

while

    tau(Delta^2)
      <=
      8 q_alpha/(pi^2 R).

Cauchy--Schwarz therefore yields

    |
      tau(Delta S^2)
    |

      <=
      16 q_alpha/
      (pi^2 eta^3 R).

Together,

    boxed:

    |
      m_H(z)-m_{H_R}(z)
    |

      <=
      24 q_alpha/
      (pi^2 eta^3 R).

With q_alpha=1/4+o(1),

    |
      m_H(z)-m_{H_R}(z)
    |

      <=
      6/
      (pi^2 eta^3 R)
      +o(R^-1).

A fixed Cauchy circle around z=i gives the same O(R^-1) control for m'(i),
hence

    boxed:

    |
      tau r2(H)
      -
      tau r2(H_R)
    |

      =
      O(R^-1).

So the preferred r2 architecture needs displacement bandwidth proportional
to epsilon_band^(-1), not epsilon_band^(-2).

See:

    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    src/wp84_r2_resolvent_tail_o1_over_r_gate.py

## 41. The diagonal beta field can also be rank-quarantined

The full ordinary-prime diagonal field obeys

    ||beta||_2^2/d
      =
      1/6+o(1).

This follows from:

- the square-prime diagonal contribution;
- degree-two nonclosed suppression;
- the already-closed carrier-2T fast channel.

Therefore, clipping beta to [-B,B] changes only a fraction

    <=1/(6B^2)+o(1)

of diagonal sites.

Since r2 has total variation 8,

    boxed:

    r2 beta-clip error
      <=
      4/(3B^2)+o(1).

Combined with fixed displacement R and alpha clip M, the operator then has
compact spectral support

    ||H||op
      <=
      B+(4M/pi)H_R.

This makes a finite polynomial/local-word reduction formally legitimate if
the direct local-resolvent route stalls.

The note deliberately does **not** claim that the resulting polynomial
degree is currently small enough for the available arithmetic gates.

See:

    notes/WP84_R2_BETA_RANK_QUARANTINE.md
    src/wp84_r2_beta_quarantine_gate.py

No unconditional record theorem is claimed yet.


## 42. The preferred r2 scale should now be conditioned against proof constants, not model value alone

The raw model ledger is largest at a=1 among the simple scales tested, but
the new one-point O(R^-1) displacement theorem has explicit pole-height
dependence.

For

    r_{2,a}(x)
      =
      1-
      [ (x-a)^2/(x^2+a^2) ]^2,

the optimized Cauchy-circle band-tail constant is

    C_band(a)
      =
      12/pi^2
      [
        sqrt(5)+256/27
      ]
      a^(-2)

      ~=14.24683177/a^2.

Thus proof conditioning depends naturally on

    Delta_a a^2,

where Delta_a is the positive-index consumer margin over the audited record
threshold.

Exact model reduction at

    a=6/5

gives

    q_{6/5}
      =
      113898001480425765678720
      /
      130234262317191955294681

      =
      0.8745624957203779...,

with model simple-zero ledger

    74.912499144...%

and positive-index record margin

    0.03781247717645....

The quantity Delta_a a^2 is about 16.8% larger at a=6/5 than at a=1.

A continuous reconnaissance maximum occurs near a=1.21038.

Therefore:

- keep a=1 as the maximal raw-margin rung;
- use a=6/5 as the current better-conditioned theorem candidate;
- do not freeze the scale permanently until the final local arithmetic error
  is written with its exact a-dependence.

See:

    notes/WP84_R2_SCALE_CONDITIONING.md
    src/wp84_r2_a6_5_conditioning.py

## 43. The finite-local fallback has modern published correlation inputs

The new fixed-band/local reduction should not be followed by inventing an
arbitrary correlation theorem from scratch.

Published short-interval results already cover substantial supercritical
ranges.

If the balanced product scale is

    M=T^s,
    s>1,

then its additive near-collision window is

    H=M/T
      =M^((s-1)/s).

Useful inputs:

1. Evans' almost-prime correlation theorem reaches E2 correlations down to
   polylogarithmic H under factor-size restrictions.  Hence every fixed
   supercritical semiprime cell is eventually in its long-shift range after
   the already-identified weight adaptation.

2. Matomaki--Radziwill--Shao--Tao--Teravainen (Invent. Math. 244, 2026)
   prove higher uniformity for Lambda and d_k in almost all short intervals.
   Their one-average Hardy--Littlewood theorem for Lambda applies in the
   range H>=X^(1/3+epsilon), while the d_k correlation theorem reaches
   H>=X^epsilon.

These do not automatically prove the exact WP84 weighted
Lambda^{*m}-type correlations.  An explicit coefficient/Heath--Brown bridge
is still required.

But they materially narrow the finite-degree fallback:

    source-match each fixed word first,
    then prove only the unmatched transition sectors.

See:

    notes/WP84_LOCAL_ARITHMETIC_LITERATURE_INTERFACE.md

No unconditional record theorem is claimed yet.


## 44. Two simple poles are enough to beat the conservative record line

The r2 repeated-pole route is no longer the smallest bounded consumer.

Define

    f_2(x)
      =
      1
      -
      [
        x^2-(17/5)x+9/4
      ]^2
      /
      [
        (x^2+1)(x^2+81/16)
      ].

For x>0, f_2<=1 trivially.

For x=-y<=0,

    [y^2+(17/5)y+9/4]^2
      -(y^2+1)(y^2+81/16)

      =
      y(
        2720y^2+3999y+6120
      )/400
      >=0,

so

    f_2(x)<=0
    for x<=0.

Thus f_2 is a global support-free positive-index minorant.

Its exact partial fraction expansion consumes only

    z=i,
    z=9i/4,

with simple poles and no z derivative.

The exact pinned model value is

    q_2
      =
      298046731976058910350368
      /
      343933139638869493768225

      =
      0.8665833489875636...,

giving model simple-zero ledger

    73.3166697975...%.

Against the conservative positive-index threshold

    q_rec=0.8367500185439279...,

the model margin is

    Delta_2
      =
      0.0298333304436357....

Using the O(1/R) simple-resolvent tail theorem at the two pole heights gives

    C_2
      =
      2.3515890423...

in

    |
      tau f_2(H)-tau f_2(H_R)
    |
      <=
      C_2/R
      +o(R^-1).

Hence

    Delta_2/C_2
      ~=0.01268646,

which is the best explicit margin/band-tail ratio among the currently
certified first-strike consumers.

The immediate theorem target should therefore be reduced to the two
Stieltjes values

    m(i),
    m(9i/4).

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md
    src/wp84_two_simple_pole_minorant.py

## 45. Three simple poles recover a much higher model rung without repeated poles

A second exact minorant is

    f_3(x)
      =
      1
      -
      [
        x^3-20x^2+(81/2)x-18
      ]^2
      /
      [
        (x^2+1)(x^2+9)(x^2+36)
      ].

It is globally support-free by a coefficientwise-positive negative-half-line
identity.

It uses only the three simple poles

    i,
    3i,
    6i.

Its exact pinned model value is

    q_3
      =
      0.8873368070783458...,

giving model simple-zero ledger

    77.4673614157...%.

Its positive-index margin over q_rec is

    0.0505867885344...,

and the explicit O(1/R) band constant is

    C_3
      =
      4.8634168148....

So

    Delta_3/C_3
      ~=0.01040149.

This is slightly less band-efficient than the two-pole rung but has a much
larger raw model margin.

See:

    notes/WP84_THREE_SIMPLE_POLE_RECORD_RUNG.md
    src/wp84_three_simple_pole_minorant.py

## 46. Updated first-strike hierarchy

The proof-oriented ordering is now:

1. two-simple-pole f_2:
       model simple ledger 73.31667...%;
       poles i and 9i/4;
       no derivatives;
       best current explicit tail-conditioning ratio;

2. three-simple-pole f_3:
       model simple ledger 77.46736...%;
       poles i,3i,6i;
       no derivatives;
       larger raw margin;

3. r2,a=1 / a=6/5:
       one spectral point but one repeated-pole derivative;

4. full Christoffel / higher simple-pole constructions:
       target near 79.62710...%.

No unconditional record theorem is claimed yet.


## 47. Conditioned two-pole first strike is essentially optimal under the current simple-resolvent tail metric

For the fixed poles

    a=1,
    b=9/4,

the model-optimal coefficient A is not quite the proof-optimal one.

Retuning to

    A=82/25

gives

    f_{2,*}(x)
      =
      1-
      [
        x^2-(82/25)x+9/4
      ]^2
      /
      [
        (x^2+1)(x^2+81/16)
      ].

The exact global minorant identity is

    [y^2+(82/25)y+9/4]^2
      -(y^2+1)(y^2+81/16)

      =
      y(
        65600y^2+91959y+147600
      )/10000
      >=0.

Its exact model value is

    q_{2,*}
      =
      7443419191454660716613888
      /
      8598328490971737344205625

      =
      0.8656821147587309...,

with model simple-zero ledger

    73.1364229517...%.

The positive-index record margin is

    0.0289320962148030....

The simple-resolvent O(1/R) constant is

    C_{2,*}
      =
      2.2079400595...,

so

    Delta_{2,*}/C_{2,*}
      =
      0.01310366017....

A continuous reconnaissance with min pole height >=1 puts the optimum near

    a=1,
    b=2.26263,
    A=3.29207,

with ratio

    0.01310447....

Thus the fully rational choice

    a=1,
    b=9/4,
    A=82/25

is effectively at the conditioned optimum for this theorem metric.

See:

    notes/WP84_TWO_SIMPLE_POLE_RECORD_RUNG.md

## 48. The second pole can be eliminated: finite Cayley hierarchy at z=i

Let

    U
      =
      (H+iI)(H-iI)^(-1).

Then U is unitary and

    R(i)
      =
      (U-I)/(2i).

For b>1,

    R(ib)
      =
      (U-I)
      /
      [
        i(1+b)
      ]
      *
      (I-q_bU)^(-1),

where

    q_b=(b-1)/(b+1).

At

    b=9/4,

    q_b=5/13.

Therefore

    R(9i/4)

      =
      4/(13i)
      (U-I)
      sum_{n>=0}
        (5/13)^n U^n.

Truncating after N terms gives the uniform operator error

    boxed:

    ||R(9i/4)-R_b^[N]||
      <=
      (5/13)^N.

For the conditioned two-pole residue

    |c_b|
      =
      1108881/325000,

the total consumer truncation cost is

    epsilon_N
      =
      2(1108881/325000)(5/13)^N.

In particular

    epsilon_8
      ~=0.00326772,

    epsilon_10
      ~=0.00048339.

Hence, after spending only a small fraction of the record margin, the entire
first-strike consumer becomes a polynomial in one unitary U of degree at
most 8 or 10.

Every U^k is bounded by one and

    rank[D,U^k]
      <=2k.

This is Proposition-R safe and converts the two-pole theorem to a finite
bounded-unitary hierarchy at the single spectral point z=i.

See:

    notes/WP84_TWO_POLE_CAYLEY_FINITE_REDUCTION.md
    src/wp84_two_pole_cayley_reduction_gate.py

No unconditional record theorem is claimed yet.


## 49. Two-pole first strike is a positive rank-four displacement energy

For the conditioned two-pole minorant define

    h(x)
      =
      [
        x^2-(82/25)x+9/4
      ]
      /
      [
        (x-i)(x-(9/4)i)
      ].

For real x,

    |h(x)|^2
      =
      1-f_{2,*}(x).

Hence for the sharp real-symmetric matrix H,

    K=h(H)

satisfies exactly

    boxed:
    tau f_{2,*}(H)
      =
      1-tau(K^*K).

The record crossing is therefore equivalent to

    boxed:
    limsup tau(K_T^*K_T)
      <
      0.163249981456072....

The pinned model energy is

    0.1343178852412691...,

leaving margin

    0.0289320962148030....

Moreover

    K
      =
      I
      + d_1 R(i)
      + d_b R(9i/4),

with

    d_1
      =
      328/125+i,

    d_b
      =
      -738/125+(9/4)i.

Because each sharp Loewner resolvent has displacement rank at most two,

    C_K=[D,K]

has

    rank C_K<=4.

Therefore

    boxed:

    tau(K^*K)

      =
      d^(-1)
      sum_i |K_ii|^2

      +
      d^(-1)
      sum_{i!=j}
        |(C_K)_ij|^2/(i-j)^2.

Both terms are nonnegative.

The off-diagonal energy has a one-dimensional S2 Fourier representation
whose internal matrix size is at most 4x4.

So the first theorem has now been reduced to one positive diagonal energy
plus one positive rank-four squared-Cauchy energy.

See:

    notes/WP84_TWO_POLE_POSITIVE_DISPLACEMENT_ENERGY.md
    src/wp84_two_pole_positive_energy_gate.py

This is currently the cleanest one-sided theorem interface.

No unconditional record theorem is claimed yet.


## 44. Conditioned two-pole first strike collapses to one Cayley point and degree three

The theorem-conditioned two-pole defect

    g_*(x)
      =
      [x^2-(82/25)x+9/4]^2
      /
      [(x^2+1)(x^2+81/16)]

admits an exact global degree-3 majorant in the Cayley variable

    u=(x+i)/(x-i).

Define

    p_3(e^{i theta})
      =
      1.6895
      +0.2101 cos(theta)
      -2.2720 sin(theta)
      -0.6312 cos(2theta)
      -0.3306 sin(2theta)
      -0.1525 cos(3theta)
      +0.0439 sin(3theta).

Then exactly

    p_3(u(x))-g_*(x)
      =
      N(x)
      /
      [
        positive denominator
      ],

where the degree-eight integer polynomial

    N(x)
      =
      18544 x^8
      +153120 x^7
      -141929 x^6
      -1672190 x^5
      +3748517 x^4
      -2772972 x^3
      +737557 x^2
      -34542 x
      +567

has zero real roots by exact Sturm count and N(0)>0.

Therefore

    boxed:
    1-p_3(U)
      <=
      f_*(H)
      <=
      1_{H>0}

in functional calculus.

The pinned-model expectation is exactly

    E p_3(U)
      =
      6816992961687106121191829211903
      /
      49768849157495700216914692570000

      =
      0.13697308812816694....

So the induced model positive-index lower bound is

    0.8630269118718330...,

and the induced model simple-zero ledger is

    boxed:
    72.6053823744...%.

The conservative positive-index margin is

    boxed:
    0.0262768933279051....

This is smaller than the exact two-pole model margin but still ample.

The preferred hybrid architecture is now:

1. use the two simple poles only to compare H with a fixed-band H_R:

       tau f_*(H)
         >=
         tau f_*(H_R)
         -
         2.2079400595/R
         +o(R^-1);

2. on H_R use

       f_*(H_R)
         >=
         1-p_3(U_R);

3. prove one finite-band inequality for

       tau p_3(U_R),

   where

       U_R
         =
         (H_R+iI)(H_R-iI)^(-1).

Thus the post-band arithmetic theorem consumes only

    U_R,
    U_R^2,
    U_R^3

at the single point z=i.

For example:

    R=256

spends about

    0.00862477

on the full-to-band comparison and leaves roughly

    0.01765213

for the remaining finite-band arithmetic theorem.

This supersedes the previous degree-8 Cayley-geometric fallback as the
smallest currently certified bounded-unitary first strike.

See:

    notes/WP84_CONDITIONED_DEGREE3_CAYLEY_MAJORANT.md
    src/wp84_conditioned_degree3_cayley_majorant.py

No unconditional record theorem is claimed yet.

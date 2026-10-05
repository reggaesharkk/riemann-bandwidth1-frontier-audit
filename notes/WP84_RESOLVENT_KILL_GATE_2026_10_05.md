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

After the common carrier gauge,

    A_y=M_phi U_y M_phi,
    S_y=M_chi U_y M_chi,

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
carrier-free partial-translation operator.  This closes the old first-order
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

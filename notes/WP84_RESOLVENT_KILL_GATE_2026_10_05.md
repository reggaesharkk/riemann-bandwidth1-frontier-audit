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

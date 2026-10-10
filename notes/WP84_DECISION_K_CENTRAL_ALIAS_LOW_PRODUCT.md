# WP84 Decision K — central alias exclusion and low-product cubic discharge

**Decision K2.** The nonzero central coherence window is eventually empty for the full three-prime-power carrier. For every fixed 0 < theta < 2/3, the complete nonzero-carrier cubic endpoint contribution with n1*n2*n3 <= X^theta is o(d), by an absolute source-weighted bound. The remaining nonzero-carrier triples have total product > X^(2/3-epsilon) for every fixed 0 < epsilon < 2/3. The high-product endpoint discrepancy remains unbounded by available estimates. This is a sector removal, not signed cancellation or a complete deletion theorem.

Starting state: branch codex/c5-c6-attack-20261006, HEAD 8f6b508569e4b4c481ff77b1afb3d305709dc3dd. The pre-existing untracked notebooklm_packet/ was left untouched. No push or merge.

## 1. Source and exact partition

Use Decision I's full source:

    X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L)))
    d=floor(X*L), M=ceil(d*exp(-sqrt(L)/2))
    P(N)={p^v<=N: p prime, v>=1}
    c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)), alpha_n=log(n)/L.

All proper prime powers are retained. Use the actual finite J, the Decision J entry filters f^sigma_l(alpha_n), and the exact finite root interval K_l. No R=6000 truncation or ordinary-prime moment estimate is imported.

For an ordered source triple and signs sigma_j in {+1,-1}, put

    A=product_{sigma_j=+1} n_j, B=product_{sigma_j=-1} n_j,
    Omega=log(A/B).

The full cubic endpoint formula is partitioned disjointly into:

* zero carrier: Omega=0, exactly Decision I's sector;
* low nonzero: Omega!=0 and n1*n2*n3<=X^theta;
* residual: Omega!=0 and n1*n2*n3>X^theta.

Equality at the product boundary belongs to the low sector. Each term keeps (product c_nj)*exp(i*T*Omega), all three exact f filters, the lag displacement phase, and K_center(E,l,Omega). The full centering subtraction remains present. Decision I proves the zero-carrier operator norm O(L^-3), hence its two endpoint payments are O(M*L^-3)=o(d). It is not merged with a nonzero sector.

## 2. Nonzero central coherence is impossible

The proposed window is 0<|Omega|<=L/M. From the exact scales,

    M/(N*L) >= (1-1/(X*L))*exp(sqrt(L)/2) -> infinity,
    L/M ~ exp(sqrt(L)/2)/X.

For all sufficiently large T, the explicit sufficient conditions

    L/M < min(1,3*log(2)),       M > L*(e*N+1)                 (K.1)

hold. The second gives L/M < 1/(e*N+1) <= log(1+1/(e*N)), since log(1+x)>=x/(1+x).

If all signs have the same orientation, |Omega|=log(n1*n2*n3)>=3*log(2), so the central window is excluded. In a mixed orientation the two integer products are A=n1*n2 and B=n3, or the reverse. If |Omega|<=L/M<1, their ratio is at most e and the singleton side is at most N; thus both products are at most e*N. If A!=B, distinct integers then give

    |log(A/B)| >= log(1+1/(e*N)),

contradicting (K.1). If A=B, Omega=0, excluded by the nonzero condition. Therefore no nonzero-carrier triple lies in the central coherence window for sufficiently large T.

This empties only the m=0 coherent window |Omega|<=L/M. It does not assert that every nonzero carrier is large or remove nonzero frequencies outside that narrow interval.

## 3. Low-total-product absolute bound

Fix 0<theta<2/3, set Y=X^theta, and require n1*n2*n3<=Y. Both signed integer products A,B are at most Y (an empty sign side has product 1). For Omega!=0 they are distinct, so

    log(1+1/Y) <= |Omega| <= log(Y)=theta*L.                 (K.2)

Thus 0<|Omega|/L<=theta<1: no nonzero integer alias occurs in this sector.

For any integer interval of roots, a geometric sum at omega=Omega/L has modulus at most 1/|sin(pi*omega)|. Since |omega|<=theta<1,

    |sin(pi*omega)| >= sin(pi*theta)*|omega|/theta,
    1/|sin(pi*omega)| <= (theta/sin(pi*theta))*L/|Omega|
                       <= (2*theta/sin(pi*theta))*L*Y,

using log(1+1/Y)>=1/(Y+1). K_center is an endpoint root sum minus u_E/d times a full root sum, with u_E/d<=1. Uniformly in endpoint position, endpoint length, and admissible finite-J lags,

    |K_center(E,l,Omega)| <= (4*theta/sin(pi*theta))*L*Y.   (K.3)

This estimate does not apply near nonzero integer aliases; theta<1 is essential.

Let d3(m) count ordered factorizations m=abc. Since Lambda(n)<=log(n), each tuple of product m<=Y satisfies

    |c_n1*c_n2*c_n3| <= log(Y)^3/(|a_phi(T)|^3*L^3*sqrt(m)).

Prime-power tuples form a subset of all ordered factorizations, giving

    sum_{n_j in P(N), n1*n2*n3<=Y} |c_n1*c_n2*c_n3|
      <= log(Y)^3/(|a_phi(T)|^3*L^3) * sum_{m<=Y} d3(m)/sqrt(m).      (K.4)

For A3(t)=sum_{m<=t}d3(m), elementary counting gives

    A3(t)=sum_{abc<=t}1 <= t*(1+log(t))^2.

Partial summation yields sum_{m<=Y}d3(m)/sqrt(m)=O(sqrt(Y)*(1+log(Y))^2). (K.5)

Decision J's full, untruncated cubic lag mass is

    W3 <= (1+2*zeta(3/2)/pi^(3/2))^2,
    w_0=1, w_l=1/(pi*|l|) for l!=0, |f^sigma_l|<=w_l.

Combining (K.3)-(K.5), all eight sign triples, and the exact path restrictions (dropping only restrictions for an upper bound), gives for each endpoint interval

    |Y_E,low,nonzero| = O_theta(Y^(3/2)*log(Y)^5/L^2)
                      = O_theta(L*Y^(3/2)*log(Y)^2).       (K.6)

The second form uses log(Y)=theta*L, with theta fixed. Since d~X*L,

    |Y_E,low,nonzero|/d
        = O_theta(X^(3*theta/2-1)*L^2)=o(1), theta<2/3.    (K.7)

This is an absolute upper bound, not a favorable-sign assertion. It covers all prime-power tuples and every finite-J lag.

## 4. Alias support and surviving population

These are necessary support ranges only; no claim is made that every interval is occupied by prime-power triples.

| Sign pattern | Product ratio | Central m=0 | Nonzero aliases that can approach |
|---|---|---|---|
| all plus | 8<=P<=N^3, Omega=log(P) | excluded | m=1,2 may; m=3 excluded since log(N^3)<=3L-3sqrt(L) |
| all minus | reciprocal of all-plus | excluded | m=-1,-2 may; m=-3 excluded |
| two plus, one minus | 4/N<=A/B<=N^2/2 | equality is Decision I; nonzero central excluded | m=1 may; m=-1,2,-2 excluded |
| one plus, two minus | reciprocal: 2/N^2<=B/A<=N/4 | equality is Decision I; nonzero central excluded | m=-1 may; m=1,2,-2 excluded |

For the mixed pattern, N^2/2=X^2*exp(-2*sqrt(L))/2*(1+o(1)), separated from the m=2 target by 2*sqrt(L)+log(2)+o(1); its reciprocal excludes m=-2. The lower endpoint 4/N excludes m=-1 in the two-plus orientation; the reciprocal excludes m=+1 in the other. The all-same-sign m=3 gap is at least 3*sqrt(L)+o(1).

After Decision I's exact zero carrier and (K.7), the only unbounded source sector is nonzero-carrier triples with total product >X^theta. For each fixed 0<epsilon<2/3, choose theta=2/3-epsilon; every residual tuple then has product strictly >X^(2/3-epsilon). Tuples exactly on the boundary were assigned to the low sector. No single theta removes all products below X^(2/3) simultaneously.

## 5. High-product feasibility and first missing estimate

Partition residual tuples into exact half-open dyadic blocks

    D_j={ordered tuples: 2^j < n1*n2*n3 <= 2^(j+1),
         n_i=p_i^v_i<=N, Omega!=0},

intersected with the exact finite path-root constraints. Each signed block sum retains termwise (product c_nj)*exp(i*T*Omega), all three f filters, displacement phase, K_center, and global centering. No block is replaced by surrogate coefficients.

The full lag/coefficient absolute estimate uses |K_center|<=2M and the source mass S(T)=sum_{P(N)}|c_n|=O(sqrt(N)/L). Its normalized envelope is

    O((M/d)*S(T)^3)=O((M/d)*N^(3/2)/L^3)
                   =O(X^(3/2)*exp(-2*sqrt(L))/L^3),

which grows. On a fixed-gap sector dist(Omega/L,Z)>=delta>0, the geometric kernel is O_delta(1), but the normalized bound is only

    O_delta(N^(3/2)/(X*L^4))
       =O_delta(X^(1/2)*exp(-3*sqrt(L)/2)/L^4),

which also grows. These are insufficient upper bounds, not lower bounds or counterexamples. Dyadic decomposition alone gives no cancellation. The ordinary-prime R=6000 consumer estimates do not transfer to this full prime-power finite-J source.

The first missing input is a source-weighted signed multilinear estimate for the exact D_j sums, split into remaining m=+/-1,+/-2 alias windows and their fixed-gap complement, uniform in T, endpoint position, and the full finite lag/root weights, whose combined endpoint averages are o(d). Near aliases retain actual width L/M in Omega (equivalently 1/M in Omega/L); the m=0 nonzero coherent window is empty by Section 2. No random-phase assumption, abstract norm estimate, or R=6000 transfer supplies this estimate. No actual-prime lower bound or signed saving is proved.

**Still OPEN:** m3=2, conditioned Cayley energy <0.105, signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict >79%.

## Verification

The deterministic producer writes certificates/WP84_DECISION_K_CENTRAL_LOW_PRODUCT_CERTIFICATE.json. The independent replay re-derives the integer bounds and does not import the producer. Finite checks validate divisor multiplicity and integer separation only; they are not asymptotic prime-source computations.

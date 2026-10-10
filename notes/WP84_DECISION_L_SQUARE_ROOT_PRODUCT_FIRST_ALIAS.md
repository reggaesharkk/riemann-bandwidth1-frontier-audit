# WP84 Decision L — square-root product separation and first-alias discharge

**Decision L2.** Both proposed improvements are valid. For every fixed \(0<\theta<1\), the complete nonzero-carrier cubic endpoint sector with \(n_1n_2n_3\le X^\theta\) is \(o(d)\). Also the complete same-sign first-alias bin \(X^{1/2}\le P=n_1n_2n_3\le X^{3/2}\), including exact and arbitrarily near integer aliases, is \(o(d)\) by an absolute bound. Mixed-sign high-product correlations, same-sign higher aliases, shrinking alias fringes, and the far complement remain open. Decision L does not establish full cubic deletion or strict \(>79\%\).

Starting branch and HEAD: codex/c5-c6-attack-20261006, c53eaebd18d9da95eefc629d46677798cc699063. The only pre-existing untracked path was notebooklm_packet/, which is untouched. No push or merge.

## 1. Scope and inherited formulas

The target is the full prime-power finite-section cubic of Decisions I/J, with

    X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L)))
    d=floor(X*L), M=ceil(d*exp(-sqrt(L)/2))
    P(N)={p^v<=N: p prime, v>=1}
    c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)), alpha_n=log(n)/L.

We use Decision J's exact finite root-path representation and its full lag mass

    W3 <= (1+2*zeta(3/2)/pi^(3/2))^2,
    |f_l^sigma(alpha)| <= w_l, w_0=1, w_l=1/(pi*|l|) for l!=0.

All finite-J root intersections, the displacement phase, global centering, all proper prime powers, and the carrier exp(i*T*Omega) are retained. Absolute bounds below discard only complex phases and path restrictions after writing the exact sum. No R=6000 ordinary-prime consumer statement is imported.

For a triple, define A as the product of n_j over positive signs and B as the product over negative signs; Omega=log(A/B). Empty products equal 1. The centered endpoint kernel remains

    K_center(E,l,Omega)
      = sum_{k in E intersect K_l} exp(2*pi*i*k*Omega/L)
        - (|E|/d)*sum_{k in K_l} exp(2*pi*i*k*Omega/L).

This is the same-section quantity from Decision J, not a new trace decomposition.

## 2. Square-root product separation and theta<1 discharge

For mixed signs, A and B are positive integers with AB=n1*n2*n3<=Y. If A!=B, set h=max(A,B), l=min(A,B). Then

    |Omega|=log(h/l)>=log(1+1/l)
           >=1/(l+1)>=1/(sqrt(Y)+1),

because l<=sqrt(AB)<=sqrt(Y), and log(1+x)>=x/(1+x). Equality A=B is exactly the zero-carrier sector already assigned to Decision I. For all signs equal, |Omega|=log(n1*n2*n3)>=3*log(2), a stronger fixed lower bound.

Fix 0<theta<1 and Y=X^theta. For all triples with product at most Y,

    |Omega|<=log(Y)=theta*L.

When Omega!=0, the preceding integer argument gives |Omega|>=1/(sqrt(Y)+1). Hence 0<|Omega|/L<=theta<1: no nonzero integer sampling alias is possible. For |omega|<=theta, |sin(pi*omega)|>=sin(pi*theta)*|omega|/theta. Each interval geometric sum is at most 1/|sin(pi*omega)|, so

    |K_center| <= 2*theta/sin(pi*theta) * L*(sqrt(Y)+1)
               = O_theta(L*sqrt(Y)).

The factor two includes both endpoint and globally centered root sums; |E|/d<=1. This holds uniformly for every finite-J lag path and endpoint position. It does not apply at theta=1 or near a nonzero integer alias.

For m=n1*n2*n3<=Y, Lambda(n_j)<=log(n_j)<=log(Y), and the number of ordered triples of positive integers with product m is d3(m). Thus

    sum_{prime-power triples, product<=Y} |c_n1*c_n2*c_n3|
      <= log(Y)^3/(|a_phi(T)|^3*L^3)
           * sum_{m<=Y} d3(m)/sqrt(m).

For each a,b, the number of c with abc<=t is floor(t/(ab)); hence

    A3(t)=sum_{m<=t}d3(m)=sum_{ab<=t} floor(t/(ab))
         <=t*(sum_{a<=t}1/a)^2<=t*(1+log(t))^2.

Partial summation gives sum_{m<=Y}d3(m)/sqrt(m)=O(sqrt(Y)*(1+log(Y))^2). Combining this with W3 and the eight sign triples gives

    |Y_E,low,nonzero|
      =O_theta(Y*log(Y)^5/L^2),
    |Y_E,low,nonzero|/d
      =O_theta(X^(theta-1)*L^2)=o(1).

This is the complete nonzero-carrier low-product sector, with an absolute-value proof. It is not a signed saving. Decision I separately gives the exact zero-carrier endpoint payment O(M/L^3)=o(d).

## 3. Same-sign first alias, including the exact alias

For (+++) let P=n1*n2*n3 and Omega=log(P); for (---), Omega=-log(P). Group exactly by integer P. Before taking absolute values, the source expression in either orientation is the sum over ordered prime-power factorizations n1*n2*n3=P of

    (c_n1*c_n2*c_n3) * exp(+- i*T*log(P))
    * product_j f_{l_j}^{sigma_j}(alpha_nj)
    * exp(displacement phase) * K_center(E,l,+-log(P)).

Thus the grouping retains the common carrier and kernel but does not identify or cancel factorization-dependent filters or displacement phases. For an upper bound, use Lambda(n)<=log(n), multiplicity at most d3(P), and the full lag mass W3. Repeated prime bases and proper powers are included.

On the first-alias bin X^(1/2)<=P<=X^(3/2), write delta=log(P/X). Then |delta|<=L/2 and

    |sin(pi*log(P)/L)|=|sin(pi*delta/L)|>=2*|delta|/L.

For E of length at most M, the endpoint geometric sum is at most min(M,1/|sin(pi*omega)|); the centered full-section term, multiplied by |E|/d, obeys the same bound. In the near region X/e<=P<=eX, if P!=X, the mean-value inequality gives |delta|>=|P-X|/(eX), yielding the requested sharp bound

    |K_center|<=C*min(M,L*X/|P-X|),  X/e<=P<=eX, P!=X.     (L.1)

At P=X use |K_center|<=2M; never divide by zero. For noninteger X, there are at most two integers P with |P-X|<1; charge each by 2M, so an arbitrarily close integer causes no loss.

The standard fixed-divisor estimate d3(P)<=C_epsilon P^epsilon is sufficient here. One elementary proof writes d3(P)=product_q binom(a_q+2,2): for all sufficiently large primes q, each local factor is at most q^(epsilon*a_q); the finitely many smaller primes contribute a bounded product after enlarging C_epsilon. On X/e<=P<=eX, coefficient log factors divided by L^3 are bounded and P^(-1/2)d3(P)=O_epsilon(X^(-1/2+epsilon)). The integer-distance harmonic sum gives

    sum_{X/e<=P<=eX} min(M,LX/|P-X|)
      <= C*(M+LX*log(X+2)).

Together with (L.1), the near-alias endpoint bound divided by d~XL is

    O_epsilon(X^(epsilon-1/2)*(L+exp(-sqrt(L)/2)))=o(1)

for any fixed epsilon<1/2. This includes P=X when X is integer, and the closest integers on both sides when X is noninteger.

Away from [X/e,eX] but inside [X^(1/2),X^(3/2)], |delta|>=1 and |delta|<=L/2, so the same sine bound yields |K_center|=O(L) uniformly. The weighted divisor estimate proved above gives

    sum_{P<=X^(3/2)} d3(P)/sqrt(P)
      =O(X^(3/4)*L^2).

Since log(P)<=3L/2 on this bin, the coefficient logarithms divided by L^3 are bounded. The far endpoint sum is O(X^(3/4)*L^3), hence after division by d it is

    O(X^(-1/4)*L^2)=o(1).

The estimates hold for both all-plus and all-minus populations. Therefore the complete same-sign first-alias bin, exact and near aliases included, is o(d). The proof does not apply to mixed signs.

## 4. Exact disjoint partition and arithmetic alias support

Fix one theta in (0,1). Assign each tuple to exactly one of:

1. Z: Omega=0, Decision I exact UFD sector.
2. L_theta: Omega!=0 and total product<=X^theta, discharged in Section 2.
3. S1: all signs equal, X^(1/2)<=P<=X^(3/2), and P>X^theta; discharged in Section 3. Any overlap with L_theta is assigned to L_theta.
4. MIX: mixed signs and total product>X^theta, all frequencies retained.
5. SAME_REST: all signs equal, total product>X^theta, and outside the first-alias bin; all frequencies retained.

No product boundary is omitted. For each fixed epsilon in (0,1), choosing theta=1-epsilon shows that any remaining tuple must have total product>X^(1-epsilon). No single fixed theta proves a bound at theta=1.

Necessary support ranges, not occupancy claims:

* all plus: 8<=P<=N^3; m=1 and m=2 can approach; the m=3 center is inaccessible since 3L-log(N^3)>=3*sqrt(L). The frequency nevertheless approaches 3 within O(L^(-1/2)); its shrinking fringe is not removed.
* all minus: reflected m=-1,-2 may approach; m=-3 center is inaccessible but its shrinking fringe remains.
* two plus, one minus: 4/N<=A/B<=N^2/2. The m=+1 alias can approach. The m=-1 and m=+/-2 coherence centers are inaccessible; in particular 2L-log(N^2/2)>=2*sqrt(L)+log(2). The m=2 frequency can approach within O(L^(-1/2)), so its fringe remains.
* one plus, two minus: reciprocal support; m=-1 may approach, while m=+1 and m=+/-2 centers are inaccessible. Its m=-2 fringe remains.

The strict center exclusions refer to width L/M in Omega. They do not bound an intermediate fringe whose distance from an integer frequency tends to zero more slowly than 1/M. Keep all such fringes, and all fixed-gap tails, in MIX or SAME_REST.

## 5. High-product estimates and first missing analytic input

The available class-by-class absolute envelopes are:

| Remaining class | Best justified envelope here | Status |
|---|---|---|
| Mixed m=+1/-1 coherence core and central nonzero fringe | Global full-mass bound O((M/d)*S(T)^3)=O(X^(3/2)*exp(-2*sqrt(L))/L^3) after normalization | grows |
| Mixed m=+/-2 inaccessible-center fringe | Cutoff separation gives |K_center|=O(sqrt(L)); normalized full-mass bound O(N^(3/2)/(X*L^(7/2)))=O(X^(1/2)*exp(-3*sqrt(L)/2)/L^(7/2)) | grows |
| Same-sign m=2 core | Pointwise d3 near estimate O_epsilon(X^(2*epsilon)*L) | grows |
| Same-sign m=2 off-neighborhood within [X^(3/2),X^(5/2)] | Weighted d3 estimate O(X^(1/4)*L^2) | grows |
| Same-sign m=3 cutoff fringe | Natural cutoff keeps distance at least 3/sqrt(L) in frequency; kernel O(sqrt(L)); weighted-d3 full-mass bound O(X^(1/2)*exp(-3*sqrt(L)/2)*L^(3/2)) | grows |
| Any fixed-gap complement | Decision J estimate O_delta(X^(1/2)*exp(-3*sqrt(L)/2)/L^4) | grows |

The first open class after this partition is the mixed-sign high-product correlation, particularly the two-plus/one-minus m=+1 neighborhood and its reflected m=-1 neighborhood. These are necessarily high total product: in the m=+1 coherence window, A/B>=X*exp(-L/M), and B>=2, so AB=(A/B)B^2>=4X*exp(-L/M)>X^theta for every fixed theta<1 eventually. Also unresolved are the nonzero central fringe, inaccessible m=+/-2 fringes, same-sign m=2 coherence/fringe, same-sign m=3 cutoff fringe, and the fixed-gap high-product complement.

The full absolute and fixed-gap estimates and the same-sign m=2 estimates in the table are insufficient. The inaccessible m=2 or m=3 centers do not remove their shrinking fringes. These are limitations of upper bounds, not lower bounds or counterexamples.

The next theorem must bound the actual signed dyadic multilinear sums, with prime-power coefficients c_n, all finite-J f filters and displacement phases, exact K_center and centering, full carrier exp(i*T*Omega), the indicated alias/fringe widths, and uniformity in T and endpoint position, strongly enough that their combined endpoint averages are o(d). Absolute mass, generic norm bounds, random phases, and fixed-R ordinary-prime results do not supply it.

Decision I's zero sector and the new L2 removals are the only endpoint cubic populations discharged here. m3=2, conditioned Cayley energy<0.105, signed fifth/sixth gate, prime-to-Weil, zero-side transfer, determinant compatibility, and strict >79% remain OPEN.

## Reproduction

Run the deterministic producer and independent replay named in the certificate. Also run the Decision I/J and inherited K/high-product replay suites. Finite diagnostics do not constitute asymptotic prime-source evidence.

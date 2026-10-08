# WP84: signed arithmetic ledger, a central-window theorem, and the obstruction

2026-10-08. Input local HEAD
`d6e5de5b1247f8fe1c7b64b235c81b186115d82e`, branch
`codex/c5-c6-attack-20261006`. Additive local audit; no push, merge, historical
edit, main change, or NotebookLM alteration.

**Decision:** a new source-matched central-window estimate removes every
remaining sector with one prime on one product side in that window. The
joint signed budget is preserved. **No negative saving of positive magnitude
is proved.** The first unproved step remains a signed estimate on the
remaining multi-product central cells, nonzero aliases, and far tails.
This is insufficiency of the current estimates, not a counterexample to the
arithmetic theorem and not a claim that no literature theorem could exist.

## 1. Independent two-pair audit and evidence boundary

Retain X=T/(2*pi), L=log X, N=floor(exp(L-sqrt L)), h=2*pi/L,
d=floor(TL/(2*pi)), I=[a,a+n-1], n/d->1, R=6000, and
c_m=-Lambda(m)/(a_phi(T)*L*sqrt m), a_phi->1. The original object initially
contains every m=p^v<=N. The ordinary-prime gate and complete prime-power
gate are equivalent under a bounded gate by the preceding proved Schatten
argument. This is a conditional bounded-gate reduction, not permission to
drop individual power correlations or to assume the desired negative cap.

For a closed ordered path ell, |ell_j|<=6000, q_0=0,
q_j=sum_(t<=j)ell_t, let rho=max(0,n-max q+min q), i_min=a-min q. Use

    f_0^eps(s)=1-s,
    f_l^+(s)=(1-exp(2*pi*i*l*s))/(2*pi*i*l), f_l^-=conjugate(f_l^+),
    K_ell(lambda)=exp(i*(T+h*i_min)*lambda)/n
                        *sum_(j=0)^(rho-1) exp(i*h*j*lambda).       (1)

In the balanced 2+2+1+1 population the two pair fields are static and
bounded. The remaining *distinct* singleton primes p,q have frequencies
log(p/q) or +/-log(pq). Opposite signs have no nonzero near alias:
|log(p/q)|<=L-sqrt L. At zero alias, p!=q gives the harmonic bound
O_R(N log N/T), and outside its unit window the contribution is O_R(N/T).

For same signs, u=pq has at most two ordered representations and coefficient
O(1/sqrt u). The only possible near alias is +/-L, u~X. In its unit window
the exact geometric kernel obeys

    |K_ell(log u)| <= C min(1,X/(T*|u-X|)).

The nearest integer u, including u=X exactly when X is an integer, costs
O(X^-1/2); all other u cost O(L/sqrt X) by the harmonic sum. There is no
near alias 2L, since log(pq)<=2L-2sqrt L. Outside the first alias window
the O(1/T) kernel and prime coefficient l1 norm give O(N/T). Root deletion
changes neither geometric denominator nor these bounds: n~TL/(2*pi).
The carrier exp(i*T*mL) has modulus one and is never suppressed.

Consequently the complete population is

    O_R(N log N/T+L/sqrt X)=o(1).                  (2)

Slot prime windows, if used as an exact partition, only restrict coefficient
supports; the proof keeps them. Cross-collisions between paired and singleton
primes create the previously controlled heavy-block populations. The
singleton equality p=q is retained as an exclusion: allowing it with opposite
signs would create the **three balanced pairs** and hence Pair6_6000. Thus
(2) does not dispose of that non-negligible Wick term. This verifies the
previous result without assuming negligible near aliases or Gaussian laws.
Its scope is the complete population, not arbitrary masked subpieces of
other populations. The preceding independent exhaustive replay also passes.

## 2. Fully signed source ledger

For each original b-path let J be the set of visible singleton slots, k=|J|.
With pairwise distinct visible ordinary primes and epsilon_j in {+1,-1}, put

    U=product_(j in J,eps_j=+) p_j,
    V=product_(j in J,eps_j=-) p_j,
    w_J=product_(j in J) c_(p_j) f_(ell_j)^(eps_j)(log p_j/L)
                   *exp(2*pi*i*sum_(j in J)eps_j*q_(j-1)*log p_j/L).

Define D_b by summing w_J*K_ell(log(U/V)) over all original b-paths,
all signs, and all distinct b-prime tuples, J={1,...,b}.
For one balanced pair in slots u,v, its exact pre-PNT coefficient is

    k_(uv,T;visible)=sum_(p<=N,p not among visible primes) c_p^2 phi_uv(log p/L),
    phi_uv(s)=2 Re[f_(ell_u)^+(s) f_(ell_v)^-(s)
                         *exp(2*pi*i*(q_(u-1)-q_(v-1))*s)].       (3)

The two opposite pair orientations are included in phi; do not multiply by
another 2. Define Q_(b-2) by summing k_(uv,T;visible)*w_J*K over all
choose(b,2) pairs, all original paths, and all distinct visible prime tuples.
If original prime windows are inserted, their exact indicators also stay in
(3); the hidden prime belongs to the intersection of its two slot windows.
No unrestricted divisor sequence replaces these masks.

The complete orientation-summed reduced residual is

    F_T=-A*(D5+Q3)+B*(D6+Q4),
    A=11501/12500, B=137641/250000.                 (4)

In a bounded signed gate, the preceding self-bounding proof removes all
other nonexact populations by o(1). One may then replace (3) with the exact
fixed-filter constant k_uv=integral_0^1 s*phi_uv(s) ds, using the proved
PNT transfer and its norm-controlled error. It is also legal to keep (3);
the central-window theorem below does so and is not conditional on t=O(1).
All root constraints and prefixes are those of the **original b-path**, not
a newly chosen k-path. Formula (4) uses actual kernels, not sharp overlaps.

The machine ledger enumerates each r-positive/s-negative sector, r+s=k:

| Family | k | Pair choices | Signed coefficient | Sign counts r=0,...,k |
|---|---:|---:|---|---|
| D5 | 5 | 1 | -11501/12500 | 1,5,10,10,5,1 |
| Q3 | 3 | 10 | -11501/12500 | 1,3,3,1 |
| D6 | 6 | 1 | 137641/250000 | 1,6,15,20,15,6,1 |
| Q4 | 4 | 15 | 137641/250000 | 1,4,6,4,1 |

All k-prime products retain the full cutoff; factor lengths are N^r,N^s.
For each sector partition EXACTLY into central 0<|lambda|<=1, nonzero
near-alias |lambda-mL|<=1, m!=0, and the remaining tail. For large T these
unit windows are disjoint. Possible near-alias integers lie strictly between
-s and r. Zero is included only if r,s>0; exact lambda=0 is impossible for
distinct visible primes. The tail includes 1<|lambda|<=L/2 and all far parts
of nonzero and endpoint aliases. No tail is dropped. At every alias retain

    K_ell(mL+delta)=exp(i*T*mL)*exp(i*(T+h*i_min)*delta)/n
                              *sum_j exp(i*h*j*delta).           (5)

In particular Q3 mixed signs have central plus +/-first-alias and tails;
its all-same signs have further nonzero aliases and tails, not central cells.

## 3. New unconditional central-window theorem

For any sector above with min(r,s)=1, its complete CENTRAL contribution is
o(1), including arbitrary original slot-prime window restrictions. This is
an absolute bound on that explicitly defined central cell, not a negative
saving. It is sharper than the generic full-product weighted Hilbert bound.

Proof. For sufficiently large T, L>=2, n>=TL/(4*pi), |a_phi|>=1/2.
The geometric series in (1) and sin(pi*lambda/L)>=2|lambda|/L give

    |K_ell(lambda)|<=L/(2n|lambda|)<=2*pi/(T|lambda|).

In the central window U/V is between e^-1 and e, so
|log(U/V)|>=|U-V|/max(U,V). Therefore

    |K_ell(log(U/V))|/sqrt(UV)
                           <=88/(7T*|U-V|).       (6)

Here sqrt(e)<2 and pi<22/7; there is no approximate time integral.
One side is a prime <=N. The other is an integer <3N, even if its nominal
support is N^(k-1). Unique factorization gives at most r!s! ordered
factorizations per integer pair. Every visible coefficient is <=2/sqrt p
in modulus, and |f_l^eps|<=1. For Q, the sum of absolute hidden-prime
weights is <=2*sum c_p^2<=2 eventually; its visible exclusions/windows
can only reduce this bound. This last estimate uses source prime-square
normalization, not a sign assertion for phi.

For each prime side, sum 1/|U-V| over all integers <3N other than itself
is <=2H_(3N). Sum over all integers on the small side as an upper bound
for primes. Thus each ordered path/sign-placement contribution has size

    <= (176/7)*2^k*r!*s!*N*(1+log(3N))/T,          (7)

with an additional factor 2 for a Q pair. There are at most
(2R+1)^(b-1) closed paths, since the final displacement is determined.
Multiply by choose(k,r) sign placements and choose(b,2) pair choices for
Q. This proves an explicit bound in the original normalized trace, uniformly
over section endpoints and prime windows. N log N/T->0 by the natural
sqrt L quarantine. No conjecture about prime patterns is used.

Consequences: central D5 1:4/4:1, D6 1:5/5:1, Q3 1:2/2:1,
and Q4 1:3/3:1 vanish. All-same-sign central cells are empty, since their
|lambda|>=k log 2>1. The remaining central populations are exactly D5
2:3/3:2, D6 2:4/4:2 and 3:3, and Q4 2:2. Nothing here removes their
near aliases or tails. In particular Q3 survives there.

## 4. Joint grouping, sign tests, and mean-value obstruction

Unique factorization provides a useful hostile check on a suggested exact
joint cancellation. After the balanced pair cancels, every visible frequency
has exactly k distinct ordinary primes with nonzero valuation +/-1. Equality
of real frequencies forces equality of their full prime valuation vectors.
Hence supports k=3,4,5,6 are disjoint: there is no direct coefficient-level
cancellation across the four families in (4). This does not rule out a joint
*averaging* estimate. Modulo L their frequencies can meet at aliases; it is
incorrect to transfer this disjointness to sampled phases. Equation (5) then
retains the carrier, and no signed alias cancellation has been proved.

Nor are balanced-pair coefficients uniformly favorable. For two diagonal
slots separated by integer prefix difference j,

    k_uv=2*integral_0^1 s*(1-s)^2*cos(2*pi*j*s) ds
        =1/6, j=0;
        =-1/(2*pi^2*j^2), j!=0.                  (8)

Both occur on source-legal R=6000 paths. For example pair slots 1 and 3
on ell=(0,1,0,-1,0) have j=-1; ell=(0,0,0,0,0) has j=0.
The analogous sixth paths append a zero. These are exact filter coefficients,
not fabricated prime evaluations. Negative k does not imply a negative Q
correlation, since the visible correlation has no certified sign. Even the
scalar joint polynomial Bx^6-Ax^5 is negative at x=1 and positive at x=-1.
This falsifies a universal algebraic sign shortcut; it is not a source-matrix
or zero-proportion counterexample.

For completeness, (8) follows by two integrations by parts at a=2*pi*j:
the integrals of s*cos(a*s), s^2*cos(a*s), s^3*cos(a*s) are respectively
0, 2/a^2, 3/a^2. Twice the combination 0-4/a^2+3/a^2 is -2/a^2.

No new literature estimate is imported here: theorem (7) is proved directly.
The existing repository weighted-Hilbert estimate has factors N^(k/2)/T
(and fixed logarithmic factors in the sampled version); applying it to the
remaining sectors at the current scale is insufficient:

    N^(k/2)/T = exp((k/2-1)L-(k/2)sqrt L)/(2*pi),
                    -> infinity for k=3,4,5,6.    (9)

Even the sharper central near-product integer bound scales with
N^min(r,s)/T times a logarithm: every remaining central sector has min>=2,
so that bound also fails to vanish. These diverging majorants are not lower
bounds on the actual arithmetic sums. A continuous mean value cannot replace
the grid and erase its aliases, and an absolute norm estimate cannot create
a negative constant. Joint Cauchy-Schwarz loses precisely the sign needed
for (4). No source-matched joint inequality repairing those defects has been
established. We do not assert that all possible harmonic-analysis methods
are ruled out, only that these estimates and algebraic groupings do not give
the desired improvement.

## 5. Exact budget after every bound and the first unproved step

Let F_remaining denote (4) after the eight central removals. For large T the
exact conservative absolute error budget is

    |F_T-F_remaining| <= Ecentral(T),
    Ecentral(T)= (248111647871392518744574838784/625)
                         *N*(1+log(3N))/T = o(1).                (10)

The certificate gives the four separate signed-coefficient absolute budgets
and all eight cell budgets as exact rationals. These constants are purposely
conservative; asymptotic o(1) is all that is claimed. No finite T accuracy is
inferred from them, and no numerical prime data is sampled.

| Proved step | Asymptotic payment | Negative constant saving |
|---|---|---|
| Complete balanced 2+2+1+1 removal | o(1), bound (2) | 0 |
| Eight one-prime-side central cells | Ecentral(T)->0 | 0 |
| Exact frequency support grouping | no removal/payment | 0 |
| Filter-sign audit (8) | no bound on visible correlations | 0 |

Preserve Jstar=64788151489666079/572357731837500000 and the frozen
reference margin 52897896569489/572357731837500000; neither changes after
an o(1) removal. The single sharpest remaining inequality is

    limsup Re F_remaining <= Jstar-B*Pair6_6000-eta,
                                   eta>0.         (11)

The exact Pair6_6000 is the original finite Fourier three-pair integral,
not a sharp continuum number. The independent preceding certificate proves
Pair6_6000>31498340500050746323/150466924118016000000. Therefore (11)
necessarily requires a negative saving strictly exceeding

    g9=43770221409581023769108432686241
            /21264421581420459982848000000000000
       =0.0020583781807554428...,

plus eta. This is a necessary minimum, not the sufficient cap replacing
the full Pair6_6000. The new bounds prove **zero** of that positive-magnitude
saving. Candidate suppliers are only the retained D5/Q3 and D6/Q4 signed
central/alias/tail combinations; none has a proved favorable sign or a
certified dominance. Fifth terms can help through positive D5+Q3, sixth
terms through negative D6+Q4, or a joint effect; these are conditions, not
assertions about their signs. Proving all residuals o(1) would instead fail
the cap, as the previous source-matched pair lower bound demonstrates.

The first unproved step is an upper estimate on precisely this remaining
joint signed sum with negative constant margin. Its status is **insufficient
current estimates / missing signed arithmetic theorem**. Explicit
counterexamples invalidate the positivity and algebraic shortcuts, not
inequality (11) for the source. Scalar third-moment, full-to-band,
source-normalization, and zero-side obligations retain their separately
inherited status; no new result here discharges them. Strict >79 is OPEN.

## 6. Independent reproduction

Run `src/wp84_strict79_signed_ledger.py`, then the independent
`src/wp84_strict79_signed_ledger_replay.py`. The replay verifies all 22 cells,
their exact coefficients/error budgets, factorial representation counts,
harmonic majorants, UF support degrees, the opposite signs in (8), input git
blobs/bytes, packet hashes, and hostile mutations of R, cutoff, windows,
carrier, claimed saving and proof status. Finite prime examples test only
the exact UF identity; they are not source pools or numerical moment evidence.
The preceding independent two-pair/Wick certificate was also replayed.

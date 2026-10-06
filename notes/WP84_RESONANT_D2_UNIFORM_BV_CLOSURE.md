# WP84 — theorem-grade uniform BV closure of the resonant D2 channel

Date: 2026-10-05

Status: **RESONANT / DIFFERENCE-FREQUENCY D2 PRIME-SQUARE SUBSTITUTION CLOSED UNIFORMLY OVER THE SUBSET RESOLVENT STATE; FAST CARRIER-2T CHANNEL REMAINS OPEN**

No percentage theorem is claimed here.

This note closes a gap left by the fixed-displacement covariance calculation.

The earlier exact formulas identified the resonant current-prime covariance
for every fixed lattice displacement.  The actual Fourier section has
dimension d asymptotic to T L, so a fixed-r statement alone was not enough.

The missing uniformity follows directly in the physical partial-translation
representation.  The key points are:

1. the mixed-sign branch is a one-parameter family of contractions U_s^+,
   U_s^-;
2. its derivative has only one displacement-commutator term plus two
   rank-one boundary terms;
3. the subset resolvent displacement commutator has rank two;
4. the scalar subset Dirichlet polynomial has a uniform l2 grid bound by the
   large sieve;
5. therefore the branch amplitude has uniformly bounded variation in s.

Ordinary square-prime Mertens plus Abel summation then gives the continuum
s ds law with o(1) error **uniformly over every subset state**.

## 1. Sharp partial translations

On the unit interval use the Fourier basis

    e_k(x)=exp(i 2*pi*k*x),
    0<=k<d.

For 0<=s<=1 define

    U_s^+ f(x)
      = 1_[0,1-s](x) f(x+s),

and

    U_s^-=(U_s^+)^*.

Let

    D=diag(0,1,...,d-1),

and let the endpoint evaluation vector be

    e(s)
      = (1,e^(i2*pi*s),...,e^(i2*pi*(d-1)*s))^T.

Direct differentiation of the exact Fourier matrix gives

    boxed:
    dU_s^+/ds
      =
      i 2*pi U_s^+ D
      - e(s) 1^T,

and, by adjunction,

    boxed:
    dU_s^-/ds
      =
      -i 2*pi D U_s^-
      - 1 e(s)^*.

Also

    ||U_s^+||op,
    ||U_s^-||op
      <= 1,

and

    ||e(s)||_2=||1||_2=sqrt(d).

These are exact finite-section statements.

## 2. The resonant branch amplitude

Fix any sharp subset state H_S and nonreal z with

    eta=|Im z|>0,

and put

    R=(H_S-zI)^(-1).

Consider the mixed-sign scalar

    g_R(s)
      =
      tau_d(
        R U_s^+ R U_s^-
      ).

The reverse branch is handled identically.

Differentiate using Section 1.  The two interior derivative terms combine by
cyclicity into the displacement commutator:

    boxed:
    g_R'(s)
      =
      i 2*pi
      tau_d(
        U_s^- R U_s^+ [D,R]
      )

      - tau_d(
          R e(s) 1^T R U_s^-
        )

      - tau_d(
          R U_s^+ R 1 e(s)^*
        ).

Thus every derivative consists of:

- one rank-two displacement term;
- two rank-one endpoint terms.

There is no derivative factor d.

## 3. Uniform l2 control of every subset prime field

Write the sharp subset scalar polynomial as

    Q_S(tau)
      =
      sum_{n in S}
        c_n exp(i tau log n),

where the retained prime powers satisfy

    n<=N,
    N/T=o(1)

after adaptive endpoint quarantine, and

    sum_n |c_n|^2 = O(1)

by the square-prime Mertens ledger and the L^-2 normalization.

On the Fourier grid

    tau_k=T+2*pi*k/L,

remove the harmless carrier exp(iT log n) and set

    s_n=log n/L.

Distinct retained integers have circular spacing

    delta
      >= c/(N L)

for an absolute c>0 once T is large.  The wrap-around gap is larger because

    s_n <= 1-W/L

with W->infinity.

The Montgomery--Vaughan large sieve therefore gives, uniformly for every
subset S,

    sum_{k<d}
      |Q_S(tau_k)|^2

      <=
      (d + O(delta^-1))
      sum_{n in S}|c_n|^2.

Since

    d asymp T L,
    delta^-1 = O(N L),
    N/T=o(1),

we obtain

    boxed:
    ||Q_S(tau_k)||_{l2(k)}
      = O(sqrt(d))

uniformly over **all** subsets S.

Hence for

    a_k=Im Q_S(tau_k),

    boxed:
    ||a||_2/sqrt(d)=O(1)

uniformly on the entire permutation/Bernoulli path.

Source:
H. L. Montgomery and R. C. Vaughan,
"The large sieve", Mathematika 20 (1973), 119--134.

## 4. Uniform trace-norm bound for the resolvent commutator

The exact Loewner displacement law is

    [D,H_S]
      =
      pi^(-1)
      (1 a^T-a 1^T)

up to the frozen sign convention.

Therefore

    [D,R]
      =
      -R[D,H_S]R.

Using the rank-two factorization,

    ||[D,R]||_1

      <=
      (2/pi)
      ||R1||_2
      ||Ra||_2

      <=
      (2/pi)
      eta^(-2)
      sqrt(d) ||a||_2.

By Section 3,

    boxed:
    d^(-1)||[D,R]||_1
      = O_eta(1)

uniformly over every subset state.

## 5. Uniform bounded variation of the mixed branch

The interior term in Section 2 satisfies

    |
      tau_d(
        U_s^- R U_s^+ [D,R]
      )
    |

      <=
      ||R||op
      d^(-1)||[D,R]||_1

      = O_eta(1).

For the first rank-one boundary term,

    |
      tau_d(
        R e(s) 1^T R U_s^-
      )
    |

      =
      d^(-1)
      |
        1^T R U_s^- R e(s)
      |

      <= eta^(-2),

and the second has the same bound.

Therefore

    boxed:
    sup_S sup_{0<=s<=1}
      |g_R(s)|
      <= eta^(-2),

and

    boxed:
    sup_S Var_[0,1](g_R)
      <= C_eta

for a fixed constant C_eta independent of T,d,S.

The same estimates hold for the reverse mixed-sign branch.

## 6. Abel summation closes the discrete prime-square substitution

For ordinary primes define the normalized square-prime measure

    nu_L
      =
      L^(-2)
      sum_{p<=N}
        (log p)^2/p
        delta_{log p/L}.

The source-closed square-prime Mertens estimate gives cumulative discrepancy

    sup_s
    |
      nu_L([0,s])
      - s^2/2
    |
      = O(L^-1)

on the retained range, with the deleted endpoint layer already charged as
o(1) in bounded spectral rank.

For every bounded-variation g,

    |
      int g dnu_L
      - int_0^1 s g(s) ds
    |

      <=
      O(L^-1)
      [
        ||g||_infinity+Var(g)
      ].

Applying Section 5 gives, uniformly over the entire subset path,

    boxed:
    sum_p
      (log p)^2/(L^2 p)
      g_R(log p/L)

      =
      int_0^1
        s g_R(s) ds
      + O_eta(L^-1)
      + o(1)_endpoint.

Thus the resonant D2 current-prime average has a theorem-grade continuum
limit for **arbitrary actual intermediate resolvents R_S**.

No fixed-r interchange remains.

## 7. Identification with the previously derived resonant state functional

The continuum integral in Section 6 is exactly the mixed-sign sharp variance
channel.

Expanding it in the Fourier basis reproduces the covariance fingerprint

    C_aa(0)=1/(4a_phi^2),
    C_aa(r)=0 for r!=0,

    C_ab(r)=0,

    C_bb(0)=1/(6a_phi^2),

    C_bb(r)
      = -1/(2a_phi^2*pi^2*r^2).

Consequently it is the same resonant state functional Xi_res(R) derived in

    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md.

The physical-space proof supplies the missing **uniform growing-section
justification** for that formula.

## 8. What is now closed and what is not

Closed for D2-res:

- proper powers removed at o(1);
- current prime decoupled from subset state at o(1);
- current-prime dependence reduced to second covariance;
- covariance constants exact;
- growing Fourier section controlled uniformly;
- discrete prime-square sum replaced by continuum mixed-sign channel with
  O_eta(L^-1)+o(1) error.

Still open:

1. the same-sign / sum-frequency channel carrying the 2T prime carrier;
2. the Bernoulli-state average of the resulting deterministic state
   functional;
3. the first-order D1 drift.

Therefore the active D2 arithmetic obstruction is no longer the resonant
Mertens channel.  It is the carrier-2T fast/Hankel channel.

This is a genuine narrowing of the theorem frontier.

See:

    notes/WP84_D2_LEAVE_ONE_OUT_DECOUPLING.md
    notes/WP84_SHAPLEY_BERNOULLI_FLOW.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
    notes/WP84_TAPER_UNIVERSALITY_ADAPTIVE_ENDPOINT.md

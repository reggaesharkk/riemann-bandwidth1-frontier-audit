# WP83 — SC4 via Turan--Nazarov: spacing-free signed floor for a small depth cluster

Date: 2026-10-04
Status: **ONE-COMPONENT SIZE<=4 SIGNED ENERGY FLOOR CLOSED IN ANALYTIC WRITE-OUT; NOT MACHINE-FORMALIZED**

Reference used here: F. L. Nazarov, *Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type*, St. Petersburg Math. J. 5 (1994), 663--717. We use the Turan--Nazarov inequality in the standard form

    sup_I |p|
      <= exp(|I| max_j |Re lambda_j|)
         * (A |I|/|E|)^(s-1)
         * sup_E |p|,

for an exponential polynomial p(t)=sum_{j=1}^s c_j exp(lambda_j t), an interval I, and measurable E subset I of positive measure; A is an absolute constant.

## 1. Reflection-paired cluster scalar

Let C contain s<=4 off-line reflection pairs, with positive integer multiplicities m_j, depths

    delta_j in [delta_* - eta, delta_*],

where

    eta = D log L / L.

Write omega_j=gamma_j-T. On positive v the cluster scalar from the exact full-lattice Frobenius identity is

    F_C(v)
      = sum_j m_j [exp((delta_j+i omega_j)v)
                    + exp((-delta_j+i omega_j)v)].

Split

    F_C=P_+ + P_-.

Normalize the growing half by

    q(v)=exp(-delta_* v) P_+(v)
        =sum_j m_j exp(a_j v),

where

    a_j=-(delta_*-delta_j)+i omega_j

and therefore

    max_j |Re a_j| <= eta.

Most importantly,

    q(0)=M_C:=sum_j m_j >0.

This positivity is what prevents the arbitrary-coefficient near-collision counterexample from applying to an actual reflection-paired cluster.

## 2. First Turan--Nazarov pass: force mass into the endpoint interval

Fix 0<theta<1/4 and set

    I=[0,(1-theta)L],
    J=[(1-2theta)L,(1-theta)L].

Then |J|=theta L. Since sup_I |q| >= q(0)=M_C, Turan--Nazarov gives

    sup_J |q|
      >= M_C
         * exp(-eta(1-theta)L)
         * [theta/(A(1-theta))]^(s-1).

For s<=4 and eta=D log L/L,

    boxed:
    sup_J |q| >= c(theta,A) M_C L^(-D(1-theta)).

No spacing between the gamma_j is used.

## 3. Second pass: the lower bound occupies positive measure

Let M_J=sup_J |q|. Define the low-value set

    E0={v in J: |q(v)| <= eps M_J}.

If |E0|>=|J|/2, applying Turan--Nazarov on J with E0 gives

    M_J
      <= exp(eta theta L) (2A)^(s-1) eps M_J.

Choose

    eps = [2 exp(eta theta L)(2A)^3]^-1.

Then this is impossible. Hence the complementary high-value set J_hi has

    |J_hi|>=|J|/2

and on J_hi

    |q(v)|
      >= c'(theta,A) M_C L^(-D).

The two logarithmic exponents add exactly:

    D(1-theta)+D theta = D.

Therefore

    boxed:
    integral_J |q(v)|^2 dv
      >= c''(theta,A) M_C^2 L^(1-2D).

## 4. Restore the off-line amplification

On J,

    v >= (1-2theta)L.

Hence

    |P_+(v)|
      = exp(delta_* v)|q(v)|
      >= X^(delta_*(1-2theta)) |q(v)|.

The recessive half satisfies

    |P_-(v)|
      <= M_C exp(-(delta_*-eta)v).

For every fixed delta_*>=delta0>0 this is exponentially smaller than the high-set lower bound for P_+, even after the L^D loss. Thus for sufficiently large T, on J_hi

    |F_C(v)| >= |P_+(v)|/2.

Consequently

    boxed:
    integral_J |F_C(v)|^2 dv
      >= c(theta,A,delta0)
         M_C^2 L^(1-2D)
         X^(2 delta_*(1-2theta)).

This floor is completely independent of zero spacing inside C.

## 5. Convert scalar energy to matrix energy

The formal taper bound gives

    g(v)>=L-2w-|v|.

On J and for large T with 2w<=theta L/2,

    g(v)>=theta L/2.

The exact full-lattice identity therefore yields

    ||Q_C||_F^2
      = L^2 int g(v)|F_C(v)|^2 dv
      >= c M_C^2 L^(4-2D)
         X^(2 delta_*(1-2theta)).

Since rank(Q_C)<=2s<=8,

    boxed:
    ||Q_C||_op
      >= c L^(2-D)
         X^(delta_*(1-2theta)).

up to the fixed constants above.

After converting to the paper's normalized Gtilde units, only powers of L change; the power of X is unchanged.

## 6. Why this closes the near-collision regime

The raw-column two-window frame floor was false because arbitrary coefficients (1,-1) can kill two nearby analytic columns.

The actual zero cluster does not carry arbitrary coefficients. Its reflection-paired growing scalar has positive multiplicities and satisfies q(0)=sum m_j>0. Turan--Nazarov propagates that noncancellation to the exponentially amplified endpoint region.

Thus no divided-difference spacing hypothesis is needed to prove the **internal signed floor** for s<=4.

The confluent Hilbert calculation remains useful as an independent local certificate and for block coordinates, but it is no longer the only protection against coalescing zeros.

## 7. SC4 assembly status

Combine this one-component floor with:

- `WP83_BLOCK_INGHAM_SC4.md` for separated comparable-depth small components;
- `WP83_FAR_FIELD_DECOUPLING.md` for absolute far tails;
- the depth band eta=D log L/L, choosing D large enough to absorb the O(polylog) nearby shallower population;
- `WP83_FINITE_PAIR_CAPTURE.md` / the same Fourier-tail argument for finite sections.

This proves the <=4-component branch of the Proposition-R reconstruction **provided every component in the top depth band has size <=4**.

If a component has size >=5, this argument deliberately stops and hands control to EC-star in `WP83_ENERGY_COUNTING_SIEVE.md`.

## 8. Evidence grade

The Gabor identities and taper bounds are source-backed; the Turan--Nazarov theorem is classical literature. The assembly in this note is our analytic write-up and has not been Lean-formalized or externally reviewed.

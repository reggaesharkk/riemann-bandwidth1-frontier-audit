# WP84 executable source-to-response bridge recovery audit

**Decision C: source information is insufficient to instantiate the fixed-
R source-to-response bridge.** Some ordinary-prime, prime-adic and trace-grid
formulas are recoverable from prose and symbolic certificates. The checked-in
repository still does not provide an executable fixed-(R) constructor for
the actual first- and second-response contractions. No dual-mass theorem is
repeated here, and no new (A_1), (A_2), (D_1), or (D_2) bound is claimed.
Strict (>79\%) remains **OPEN**.

The audit began at `a0dc9a4d604e13f21df57468523d74b489c1b7d1`, branch
`codex/c5-c6-attack-20261006`. The initial status had only the already
untracked `notebooklm_packet/`; it was not read or changed by the new
inspector and remains untouched. No remote operation or history rewrite was
performed.

## Recovered pieces and limits

The localize note records the ordinary-prime vector
\[
 V_p(K)=c_p e^{iT\log p}e^{2\pi iKs_p}
 (e^{2\pi irs_p},\;i s_p e^{2\pi irs_p})_{|r|\le R},\qquad
 c_p=-\frac{\log p}{a_\phi L\sqrt p},\quad s_p=\frac{\log p}{L}.
\]
This is a formula in prose. It is not an executable realified row tensor
with the original gates and complete grouped proper powers instantiated.
The prime-adic firewall records the common phase (z_p^a), the frequencies
of the first and second response terms, and the exact resonance equation
\[
 \lambda_\nu+r\log p=mL
 \quad\Longleftrightarrow\quad
 p^r\prod_{q\ne p}q^{\nu_q}=X^m.
\]
It also records the trace-grid kernel
\[
 \mathcal K_I(\omega)=\frac1{d'}\sum_{k\in I}
 e^{i(T+2\pi k/L)\omega}.
\]
These identities identify the arithmetic phase skeleton. They do not specify
the source data needed to evaluate the actual coefficients.

The contour-mixture producer stores the (K_1) and (K_2) definitions as
JSON strings. The resulting `Gamma` quantities explicitly stand for the
realified, masked, lag/root/path-weighted source tensors; they are not built
by executable code. The formulas retain the common trace index and remove
only the justified opposite-sign equal-power covariance diagonal. Neither
the response Fourier arrays nor an equivalent direct contraction are
constructed. Accordingly the actual (K_{1,p,\nu}), (K_{2,p,\nu}),
(D_{1,T}), and (D_{2,T}) are not instantiated.

The `source_mask(...)` parameter in
`src/wp84_fifth_full_pool_amplitude.py` belongs to a separate determinant
atom iterator and is caller-supplied. The q-mask extractor is a different
reconstructed determinant helper. Neither defines the fixed-(R)
Lindeberg gates; transferring either would conflate distinct mathematical
objects. A historically unique section selector is not automatically
necessary: a uniform theorem over a fully specified admissible section class
would suffice. For a concrete replay, however, one needs an actual section
and its endpoint/order, (d'), and root-count inputs, or a uniform certificate
that removes that dependence.

The machine-readable certificate records the recovered formula checks,
source hashes, missing inputs, and this scope boundary. The independent
replay verifies those source hashes and rejects mutations that shorten
(R=6000), replace the natural prime cutoff, import a determinant mask,
fabricate a contractor or section selector, or promote the theorem status.

## Minimum source specification still required

1. For every base prime (p) and power (p^a\le N), an executable exact
   realified fixed-(R) coordinate tensor, including normalization and one
   unambiguous carrier-placement convention.
2. The actual fixed-(R) masks and row-dependent source gates, with every
   lag, root/path factor and alias indicator. They must be the gates for the
   Lindeberg vector itself.
3. Either a source-backed allowable trace section (I(T)), endpoints/order,
   (d'), and root-count data for a replayable instance, or a precise
   admissible section class and a proof uniform over that class. No
   historical endpoint selector is invented.
4. Executable (p)-excluded response Fourier coefficients, or a direct exact
   contraction that computes the same (K_1,K_2) without materializing the
   arrays.
5. A source-backed fixture retaining the natural full prime and prime-power
   cutoff and (R=6000), suitable for independent comparison of the
   instantiated (A_1,A_2,D_1,D_2).

The next analytic statement after supplying these data remains the
source-matched limit
\[
 A_{1,T,R}+A_{2,T,R}\longrightarrow0
 \quad(T\to\infty),\qquad R=6000\text{ fixed},
\]
uniformly over the stated admissible sections and with all periodic and near
aliases retained. The sufficient dual-mass conditions
\(D_{1,T}=o(1)\), \(D_{2,T}=o(L^4)\) are not established by this audit.

## Reproduction

From repository root:

```powershell
python src/wp84_executable_source_response_bridge_inspector.py
python src/wp84_executable_source_response_bridge_replay.py
python src/wp84_contour_mixture_prime_mass_replay.py
python src/wp84_analytic_response_trace_grid_transfer_replay.py
python src/wp84_dependent_phase_prime_adic_firewall_replay.py
```

The two new programs are a completeness inspector and an independent
certificate replay; they do not numerically approximate the missing source
objects. The final three commands replay the earlier finite identities and
evidence certificates only. Passing them does not prove an asymptotic
trace-grid estimate or the strict (>79\%) theorem.

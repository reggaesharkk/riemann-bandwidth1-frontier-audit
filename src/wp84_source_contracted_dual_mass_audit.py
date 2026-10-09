"""Source-completeness audit for WP84's contour-mixture dual masses.

The certificate distinguishes executable formulas from symbolic source
placeholders and does not infer an actual zeta-side contribution from a
formal alias or an adversarial response sequence.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
START = "93959b4e429d7bc02aaec8fd535acf2075bd877b"
BRANCH = "codex/c5-c6-attack-20261006"

SOURCES = {
    "mixture_note": "notes/WP84_CONTOUR_MIXTURE_PRIME_MASS.md",
    "mixture_certificate": "notes/WP84_CONTOUR_MIXTURE_PRIME_MASS_CERTIFICATE.json",
    "mixture_producer": "src/wp84_contour_mixture_prime_mass.py",
    "mixture_replay": "src/wp84_contour_mixture_prime_mass_replay.py",
    "analytic_note": "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER.md",
    "analytic_certificate": "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER_CERTIFICATE.json",
    "analytic_producer": "src/wp84_analytic_response_trace_grid_transfer.py",
    "analytic_replay": "src/wp84_analytic_response_trace_grid_transfer_replay.py",
    "firewall_note": "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL.md",
    "firewall_certificate": "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL_CERTIFICATE.json",
    "firewall_producer": "src/wp84_dependent_phase_prime_adic_firewall.py",
    "firewall_replay": "src/wp84_dependent_phase_prime_adic_firewall_replay.py",
    "localize_note": "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md",
    "grouped_note": "notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md",
    "amplitude_source": "src/wp84_fifth_full_pool_amplitude.py",
}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def build():
    src = {k: (ROOT / p).read_text(encoding="utf-8") for k, p in SOURCES.items()}
    acert = json.loads((ROOT / SOURCES["analytic_certificate"]).read_text(encoding="utf-8"))
    fcert = json.loads((ROOT / SOURCES["firewall_certificate"]).read_text(encoding="utf-8"))
    pcount = "pi(N)-1"  # all response primes except current p
    return {
        "schema": "wp84-source-contracted-dual-mass-audit-v1",
        "starting_head": START,
        "branch": BRANCH,
        "decision": "E",
        "frozen": {"K": 32, "delta": "1/100000", "cutoff": "N=floor(X*exp(-sqrt(log X)))", "quantifiers": "fixed R, then T->infinity", "strict_gt79": "OPEN"},
        "prior_replays": {
            "contour_mixture": "PASS: exact contour identities and mass checks; 12 hostile mutations rejected; 9 source hashes verified; dual targets explicitly OPEN.",
            "analytic_response": "PASS: exact rational replay; 22 mutated certificates rejected; 10 source hashes verified; aggregate response mass OPEN.",
            "prime_adic_firewall": "PASS: independent rational replay, source hashes, 21 hostile-inference evidence checks; actual trace-grid transfer OPEN.",
            "scope": "These replays validate their stated finite identities, hashes and evidence fields; none proves D1=o(1) or D2=o(L^4)."
        },
        "source_object_inventory": {
            "section_kernel": {
                "status": "FORMULA_EXECUTABLE_GIVEN_I",
                "definition": fcert["trace_grid_discrepancy"]["kernel"],
                "boundary": "The finite geometric sum is evaluable when I, d', T and L are supplied. No executable selected-section endpoint/root selector is part of the current dual-mass artifacts."
            },
            "ordinary_prime_vector": {
                "status": "PROSE_FORMULA_ONLY",
                "location": "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md:144-153",
                "definition": "V_p(K)=c_p exp(i*T*log p) exp(2*pi*i*K*log(p)/L) times the lag vector (exp(2*pi*i*r*log(p)/L), i*log(p)/L*exp(...)) for |r|<=R.",
                "boundary": "A source formula is present; no executable vector evaluator tied to the full original masks/section is supplied by this audit's inputs."
            },
            "proper_power_vectors": {
                "status": "GROUPED_SYMBOLIC_WITH_NORM_ENVELOPE",
                "definition": "All p^a<=N share base phase z_p^a; ||B_(p^a)||<=4 log(p)/(L*p^(a/2)).",
                "boundary": "The full coordinate tensors/gates for every a and lag are not enumerated as executable arrays in the governing notes or scripts."
            },
            "Gamma_source_tensors": {
                "status": "SYMBOLIC_PLACEHOLDER",
                "evidence": "The prior producer stores K1/K2 definitions as strings in JSON; it does not define an executable Gamma constructor. The dependent-phase certificate describes gamma_{p,a} and its factors in prose.",
                "exact_missing": ["coordinate-level realification for every retained p^a", "mask/source-gate value at each selected row", "root/path summation order and divisor", "one-time carrier placement verified against the row gates"]
            },
            "response_coefficients": {
                "status": "BOUNDED_BUT_NOT_INSTANTIATED",
                "evidence": "The polystrip artifacts provide M1_R/M2_R and Parseval/pointwise bounds, but do not generate the actual c1_(p,nu) or c2_(p,nu) arrays for the full prime pool and section.",
                "boundary": "Analytic coefficient upper bounds do not identify which alias coefficients are present or nonzero."
            },
            "source_mask_callback": {
                "status": "EXTERNAL_IN_SEPARATE_FULL_POOL_ATOM_ITERATOR",
                "evidence": "src/wp84_fifth_full_pool_amplitude.py requires source_mask(...) in iter_source_atoms; no def source_mask implementation is checked in.",
                "scope_warning": "That atom-iterator callback belongs to the separate determinant/near-alias source population. It is not silently identified with the fixed-R Lindeberg V_p masks."
            },
            "selected_section": {
                "status": "NOT_INSTANTIATED_FOR_DUAL_MASS",
                "evidence": "The K_I formula is recorded for a supplied contiguous I, but the dual-mass scripts contain no executable selected I, endpoint gate, or root-count map.",
                "dprime": "d' appears symbolically; no selected-section input object is serialized."
            },
            "K1_K2": {
                "status": "FORMAL_DEFINITIONS_ONLY",
                "evidence": "src/wp84_contour_mixture_prime_mass.py lines 76-87 writes the K1/K2 formulas as JSON string values. Its executable work is certificate construction, not contraction of source tensors or dual-mass evaluation.",
                "covariance_diagonal": "The existing justified deletion is only opposite-sign equal powers a=b; other pairs remain symbolically."
            }
        },
        "mathematical_results_rechecked": {
            "mixture": "Integrating each finite Parseval sum against a probability measure preserves M_j,R^2; monotone convergence extends the nonnegative sum. Independent contour signs give product cosh and cosh(x)>=exp(|x|)/2, hence the 2^(-support) pointwise penalty.",
            "finite_dual_optimization": "For finite F, D_mu is convex and an optimizer can be represented on at most |F|+1 contours by Caratheodory. This does not supply a uniform infinite-F limit.",
            "prime_masses": "g_p=4 log(p)/(L*(sqrt(p)-1)); max g_p=O(L^-1), sum g_p^2=8+o(1), sum g_p^3=O(L^-3), sum g_p^4=O(L^-4), using the documented grouped-block bound and PNT for the square mass.",
            "conditional_dual_estimates": {
                "M1_R": acert["complex_resolvent_domain"]["consumer_bounds"]["M1_R1_upper"],
                "M2_R": acert["complex_resolvent_domain"]["consumer_bounds"]["M2_R2_upper"],
                "A1": "If the instantiated source-contracted D1_T=o(1) holds, then |A1|<=M1_R*sqrt(8+o(1))*sqrt(D1_T)=o(1); M1_R=43212226464/16375.",
                "A2": "If the instantiated D2_T=o(L^4) holds after deleting only Sigma_p's opposite/equal-power diagonal, then |A2|<=M2_R/2*sqrt(C4)*L^-2*sqrt(D2_T)=o(1), where M2_R=166449403229184/429025 and C4=256*sum_p log^4(p)/(sqrt(p)-1)^4<infinity.",
                "extra_hypotheses": "These are sufficient conditions, not proved estimates; they require the actual K arrays, common source section, and the stated limits."
            }
        },
        "falsification_matrix": {
            "exact_m0": "CLOSED: p-adic valuation excludes lambda_nu+r log(p)=0 for r!=0.",
            "nonzero_periodic_alias": "POSSIBLE: the exact m=1 primorial frequency label is retained; its response coefficient and source-contracted contribution are UNKNOWN.",
            "near_alias": "UNKNOWN aggregate: a single sampled kernel can be order one in an O(1/T) window; no count or actual coefficient list is present.",
            "intermediate_far": "Pointwise geometric decay is known; source-weighted summation is UNKNOWN.",
            "support_multiplicity": "Known obstacle to the crude lower bound on W: 2^(-support) remains. Whether the actual alias family's multiplicity overcomes optimized mixture decay is UNKNOWN.",
            "row_dependent_masks": "UNKNOWN: no fixed-R row-gate value table/implementation is supplied, so a cancellation test cannot be run.",
            "generic_reciprocal_weight_test": {
                "status": "CRUDE_MAJORANT_FAILS_UNIFORMLY_FOR_THIS_SCHEDULE",
                "proof": f"Take all s={pcount} response primes, rho_q=eta log(q), eta=min(1/4,131L/(51200s)). The certified cost is feasible. Since s~N/log N, eta*log N->0. For large T rho_q<=1, and the sign-mixture weight obeys sum_{{nu in Z^S}}1/W(nu)=product_q sum_n sech(2rho_q n)>= (1+2/cosh(2))^s, which diverges. Thus |K|<=1 alone gives no uniform summable majorant. This does not show the actual K-weighted dual mass diverges or that another measure fails.",
                "optimized_arbitrary_measure": "UNKNOWN; this calculation is only for the stated explicit sign mixture and trivial |K|<=1 majorant."
            },
            "infinite_limit_order": "Parseval mixtures pass to all Fourier indices by monotone convergence. The source pairing limit follows only if the dual mass is finite for the truncations; no uniform-in-T dual bound permits exchange with T->infinity."
        },
        "countermodel_boundary": {
            "abstract_L2_atom": "The earlier 2/3/5 near-alias atom is a countermodel to a norm-only response lemma, not an actual coefficient and not a counterexample to D1/D2.",
            "source_legal_counterexample": "NONE ESTABLISHED",
            "uniform_from_documented_constraints": "UNKNOWN: pointwise grouped-power envelopes and response Parseval/strip bounds do not instantiate the contracted kernels; the admissible row-mask/section class is not specified sufficiently to quantify a supremum or test an actual cancellation."
        },
        "decision": "E",
        "first_missing_exact_input": [
            "an executable fixed-R current-power tensor constructor for every p^a<=N, including the exact coordinate normalization and one-time carrier convention",
            "the actual row-dependent mask/source-gate and root/path summation maps for each allowed section, with selected row identities/order and d'",
            "the concrete selected-section endpoint/root-count object used in K_I",
            "a reproducible construction of the p-excluded response Fourier coefficients or an executable exact contraction that avoids materializing them"
        ],
        "first_unproved_analytic_lemma_after_source_recovery": "For those actual source tensors and each fixed R, prove D1_T=o(1) and D2_T=o(L^4) uniformly over the allowed sections, retaining nonzero periodic, near, intermediate and far frequencies.",
        "strict_gt79": "OPEN",
        "source_sha256": {p: sha(p) for p in SOURCES.values()}
    }


def main():
    cert = build()
    out = ROOT / "notes/WP84_SOURCE_CONTRACTED_DUAL_MASS_AUDIT_CERTIFICATE.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Decision E: source-contracted Gamma tensors and selected-section data are not instantiated in the checked-in dual-mass artifacts.")
    print("Known: m=0 valuation exclusion, contour mixture identity, grouped prime masses; actual D1/D2 and strict >79 remain OPEN.")


if __name__ == "__main__":
    main()

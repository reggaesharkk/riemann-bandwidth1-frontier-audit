"""Build a source-pinned certificate for physical endpoint bounds and the jet gate.

No selected row, endpoint selector, source_mask callback, or rank is invented.
The universal formulas proved in the accompanying note are the analytic input.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT = "307fe32651d0378e439b69f110060d6c94ee1a15"
BLOCKS = [
    [15, 20, 26, 28, 31, 32],
    [10, 12, 16, 17, 21, 22, 25, 29],
    [36, 38, 42, 46, 47, 48, 49, 50, 54, 59, 61, 62, 64, 65, 68, 69],
    [34, 37, 39, 43, 53, 56, 60, 63],
]
SOURCES = [
    "notes/WP84_GOOD_ENDPOINT_TRIMMING.md",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "notes/WP84_R400_SAME_NORMALIZATION_REPLAY.md",
    "notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md",
    "notes/WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md",
    "notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md",
    "notes/WP84_EXACT_Q_MASK_AND_DETERMINANT_VISIBLE_MOMENT_BASIS.md",
    "notes/WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md",
    "notes/WP84_FIFTH_LEGAL_STENCIL_AND_PRIME_REALIZATION.md",
    "notes/WP84_FIFTH_FULL_POOL_LARGE_SECTION_LIFT.md",
    "notes/WP84_LRSC_PHASE_NETWORK_FUNCTIONAL_RANK_TRANSPLANT.md",
    "notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md",
    "notes/WP84_NEAR_ALIAS_SURVIVOR_ORBIT_COMPRESSION.md",
    "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json",
    "src/wp84_r400_first_record_assembly.py",
    "src/wp84_r400_same_normalization_replay.py",
    "src/wp84_r400_pair_layer_exact.py",
    "src/wp84_detuning_commutator_endpoint.py",
    "src/wp84_cross_scale_sharp_detuning.py",
    "src/wp84_fifth_full_pool_amplitude.py",
    "src/wp84_fifth_full_pool_replay.py",
    "src/wp84_source_q_mask_extractor.py",
    "src/wp84_exact_q_mask_replay.py",
    "src/wp84_exact_determinant_coefficient_builder.py",
    "src/wp84_wedge_support_reducer.py",
    "src/wp84_visible_prime_minor_builder.py",
    "src/wp84_full_weight_evaluation_map.py",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def field_record(f: dict) -> dict:
    pi = list(map(int, f["equality_partition"].split(",")))
    eps = [1 if s == "+" else -1 for s in f["sign_word"]]
    nu = [pi.count(b) for b in range(max(pi) + 1)]
    net = [sum(eps[s] for s in range(5) if pi[s] == b) for b in range(len(nu))]
    hidden = next(b for b in range(len(nu)) if nu[b] > abs(net[b]))
    assert sum(abs(e) for e in net) == 3
    return {
        "id": f["id"], "pi": pi, "signs": eps, "nu": nu,
        "net": net, "aliases": f["aliases"],
        "independent_canceled_prime": net[hidden] == 0,
        "exact_consumer_alpha": f["exact_alpha"],
        "pool": "all ordinary primes <=N, injective on equality blocks",
        "source_mask": "exact descriptor, cutoff, distinctness, nearest allowed alias, 0<abs(lambda-mL)<=H/T, positive source root count",
        "source_mask_callback_status": "externally supplied; not newly implemented",
        "R": 6000,
        "prefix_order": "v0=0; v_s=sum_(r=1)^s ell_r; original ordered slots",
        "root_order": "increasing i from a0-min(v) through b0-max(v), inclusive",
        "normalization": "slot -log(p)/(a_phi*L*sqrt(p)); positive-carrier factor 1/2; exact root divisor n",
        "boundary_lower": "(1/2) sum_full_source w(P,ell) exp(i*(T+h*(k-min(v)))*lambda)",
        "boundary_upper": "(1/2) sum_full_source w(P,ell) exp(i*(T+h*(k-max(v)))*lambda)",
        "jet_rows": "exact [u^h] source root/filter product, NOT evaluation at u=1/L",
    }


def build() -> dict:
    funcs = json.loads((ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json").read_text())
    fields = [field_record(funcs[fid]) for ids in BLOCKS for fid in ids]
    w2 = sum((Q(f["exact_consumer_alpha"]) ** 2 for f in fields), Q(0))
    pins = {}
    for path in SOURCES:
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{PARENT}:{path}"], cwd=ROOT, text=True
        ).strip()
        pins[path] = {"commit": PARENT, "blob": blob, "sha256": digest(ROOT / path)}
    packet = {
        path.relative_to(ROOT).as_posix(): digest(path)
        for path in sorted((ROOT / "notebooklm_packet").rglob("*")) if path.is_file()
    }
    # Read-only semantic inspection. Counts are inventory, not mathematical premises.
    from pypdf import PdfReader
    packet_hits = {}
    for path in sorted((ROOT / "notebooklm_packet").glob("*.pdf")):
        text = "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
        packet_hits[path.name] = {
            term: text.lower().count(term)
            for term in ("commutator", "rank-two", "wedge", "gauge", "principal section", "lrsc")
        }
    return {
        "decision": "E",
        "status": "PHYSICAL_ENDPOINT_BOUND_CLOSED_SOURCE_JET_INTERTWINING_OPEN",
        "input_head": PARENT,
        "uniform_old_schema": {
            "coefficients": "arbitrary finite Hilbert family with finite total energy, fixed as k varies",
            "frequency_hypotheses": "bounded real frequencies; distinct frequencies collapsed; minimum separation delta",
            "mean_score_bound": "2*(1+h^2*Omega^2)*(1+2pi/(q*h*delta))*B",
            "historical_integer_specialization": "m<=T^2, delta>=1/(T^2+1), Omega=O(L), B=O(1)",
        },
        "fields": fields,
        "score": {
            "kind": "physical boundary score; determinant-jet score not substituted",
            "joint": True, "adjacent_offsets": [0, 1],
            "candidate_line": "a0=k; b0=k+d-q; k=0,...,q-1; q=floor(d/sqrt(L))",
            "dimension": "n=d-q+1, independent of k, n/d->1",
            "pool_truncation": False, "centered_heuristic": False,
            "selected_endpoint": None,
            "determinant_selector_certified": False,
        },
        "physical_bound": {
            "W2": str(w2), "R": 6000,
            "P_R_rational_upper": str(Q(158171, 243)),
            "K": "6*M*P_R/a_phi^3",
            "energy_one_edge": "W2*K^2*(4pi+8H*(1+a_phi^2*M))/T",
            "Omega_upper": "3L", "delta_lower": "1/(N^3+1)",
            "joint_adjacent_mean_score": "8*(1+36pi^2)*(1+2pi*(N^3+1)/(q*h))*B_native",
            "normalized_endpoint_rate": "O_R,H(exp(-3sqrt(L))/sqrt(L))+o(1)",
            "determinant_jet_bound": None,
        },
        "jet_gate": {
            "root_jet": "(c0*lambda)^h/(n*h!) * sum_(r=0)^(n-span-1) (a0-min(v)+r)^h",
            "translation": "J_h(a0+s)=sum_(r=0)^h (c0*s*lambda)^(h-r)/(h-r)! * J_r(a0)",
            "complete_complex_stack_determinant": "1",
            "complete_realification_invertible": True,
            "frozen_real_row_stencil_closed": None,
            "alias_reduction_commutes_with_jet": False,
            "remaining_lemma": "source-legal real row space invariant under the nilpotent realified jet-translation generator, yielding column- and S-independent invertible U_B(s)",
            "finite_test": "ker(P_B restricted to the actual coefficient-column Krylov space V_jet) is invariant under every G_x",
            "generator_subdiagonal": "2pi*lambda_x * [[0,-1],[1,0]]",
            "ambient_dimension_upper": "18 times the number of frozen source cells",
            "intertwining_matrices_H_x": None,
        },
        "linear_transfer": {
            "old_support": "even ordinary-semiprime carrier degree 2",
            "native_support": "odd reduced carrier degree 3",
            "endpoint_independent_support_transfer_rank": 0,
            "residual": "D on disjoint native carrier support; actual rank unknown",
            "sharp_Score_det_to_Score_trim_constant": None,
        },
        "budget": {
            "joint_cushion": str(Q(52897896569489, 572357731837500000)),
            "retained_l1_mass": str(Q(163444421, 31250)),
            "paid_bulk_arithmetic_charge": None,
            "strict_gt79": "OPEN",
        },
        "determinant_visible_K": None, "correction_ranks": None,
        "source_legal_minors": None, "fifth_rank_bounds": [38, 72],
        "source_pins": pins, "packet_sha256": packet,
        "packet_read_only_semantic_hits": packet_hits,
    }


if __name__ == "__main__":
    out = build()
    target = ROOT / "notes/WP84_DETERMINANT_NATIVE_ENDPOINT_CERTIFICATE.json"
    target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("Physical endpoint energy O_R,H(T^-1); source-jet intertwining OPEN")
    print("Exact squared consumer weight mass:", out["physical_bound"]["W2"])
    print("Packet inspected and hashed read-only; no source selector or determinant promotion")

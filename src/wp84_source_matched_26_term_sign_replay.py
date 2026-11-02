#!/usr/bin/env python3
"""Replay the WP84 source-matched 26-term sign audit.

The source inputs are pinned to SOURCE_REVISION.  The exact Fraction model is
kept separate from source evidence: missing source selectors never become
zero-weight or positive-weight rows.  Running this file writes only the new
audit evidence JSON requested for this audit.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REVISION = "2caac1e6e4a8adfab7c74f87c805e6cd81d4f9a1"
SOURCE_BRANCH_AT_START = "codex/c5-c6-attack-20261006"
SOURCE_CONTEXT_REVISION = "be82c32cc00fce6d1c880ee5a4fe4a1300a194d1"
SOURCE_CONTEXT_BRANCH = "codex/wp84-source-recovery-20261008"
AUDIT_BRANCH = "codex/wp84-source-mask-sign-audit-20261102"
CAPTURE_DATE = "2026-11-02"

PINNED_BLOBS = {
    "notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md": "3f42b46baa727f5c13c244b9b20f18854a0cb030",
    "notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md": "5c0fa1e59c7bd398d20677d26d03b03497d7062f",
    "src/wp84_phi4_balanced_nonclosed_nonpositive.py": "d11a21c4492135e7247c482efe48abe0ef0c3c3b",
    "notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md": "9ff0fd5ba59969ccd58aab28a0f9c3c489992c58",
    "src/wp84_e2_shift_range_safe_lobe.py": "4741f932c7fade6229d1f2a35447644a5440c7a9",
    "notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md": "e48bb9871fbc4f9a4f320fa2b796d3a6a188d64f",
}

# Complete set of repository files used as source evidence in this audit.
SOURCE_PATHS = sorted(set(PINNED_BLOBS) | {
    "notes/WP84_PHI4_EQUAL_SCALE_BROWNIAN_KERNEL.md",
    "notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md",
    "notes/WP84_BLOCK15_SOURCE_MASK_SEMANTIC_RECONSTRUCTION.md",
    "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json",
    "notes/WP84_SOURCE_PROVENANCE_RECOVERY_AUDIT.md",
    "notes/WP84_SOURCE_PROVENANCE_RECOVERY_CERTIFICATE.json",
    "notes/WP84_FIFTH_FULL_POOL_LARGE_SECTION_LIFT.md",
    "src/wp84_phi4_equal_scale_brownian_kernel.py",
    "src/wp84_fixed_scale_connected_kernel.py",
    "src/wp84_balanced_orientation_normalization.py",
    "src/wp84_fifth_full_pool_amplitude.py",
    "src/wp84_fifth_full_pool_section_replay.py",
    "src/wp84_source_mask_contract_extractor.py",
    "src/wp84_source_mask_semantics_replay.py",
    "src/wp84_source_provenance_recovery_replay.py",
    "src/wp84_source_q_mask_extractor.py",
})

TASK_PACKET_ROOT = Path(
    r"C:\Users\Asus\SHARK_AGENT_LAB\wp84_source_weight_mask_hostile_20261102"
)
EVIDENCE_PATH = ROOT / "evidence/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_manifest() -> list[dict]:
    manifest = []
    for rel in SOURCE_PATHS:
        revision = SOURCE_CONTEXT_REVISION if rel in PINNED_BLOBS else SOURCE_REVISION
        blob = git("rev-parse", f"{revision}:{rel}")
        data = subprocess.check_output(
            ["git", "cat-file", "blob", blob], cwd=ROOT
        )
        # The six supplied pins belong to the explicitly named source-context
        # branch and can differ from the audit worktree's adjacent branch.
        if rel not in PINNED_BLOBS:
            same_as_revision = subprocess.run(
                ["git", "diff", "--quiet", revision, "--", rel], cwd=ROOT
            ).returncode == 0
            if not same_as_revision:
                raise AssertionError(f"source input differs from pinned revision: {rel}")
        manifest.append({
            "path": rel,
            "source_revision": revision,
            "git_blob": blob,
            "sha256": sha256(data),
            "bytes": len(data),
        })
    return manifest


def task_packet_manifest() -> dict:
    manifest_path = TASK_PACKET_ROOT / "SHA256_MANIFEST.json"
    checksum_path = TASK_PACKET_ROOT / "SHA256_MANIFEST.sha256"
    if not manifest_path.is_file() or not checksum_path.is_file():
        return {"status": "NOT_RECHECKED_PACKET_PATH_UNAVAILABLE"}
    manifest_bytes = manifest_path.read_bytes()
    checksum_line = checksum_path.read_text(encoding="utf-8").split()[0]
    if sha256(manifest_bytes) != checksum_line:
        raise AssertionError("task packet manifest checksum mismatch")
    manifest = json.loads(manifest_bytes)
    files = manifest["files"]
    errors = []
    for rel, expected in files.items():
        path = TASK_PACKET_ROOT / rel
        if not path.is_file() or sha256(path.read_bytes()) != expected:
            errors.append(rel)
    if errors:
        raise AssertionError("task packet file hash mismatch: " + ", ".join(errors))
    return {
        "status": "PASS",
        "root": str(TASK_PACKET_ROOT),
        "manifest_schema": manifest.get("schema"),
        "manifest_sha256": sha256(manifest_bytes),
        "files_verified": len(files),
        "files": files,
        "scope": manifest.get("claimed_scope"),
    }


def partitions(n: int):
    """Generate each set partition once by restricted-growth construction."""
    def grow(i: int, blocks: list[list[int]]):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from grow(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from grow(i + 1, blocks)
        blocks.pop()
    yield from grow(0, [])


def ordered_terms(n: int = 4):
    """Connected-cumulant terms: first block contains label 0."""
    for part in partitions(n):
        first = next(i for i, block in enumerate(part) if 0 in block)
        rest = [i for i in range(len(part)) if i != first]
        sign = (-1) ** (len(part) - 1)
        for perm in itertools.permutations(rest):
            order = (first, *perm)
            prefix_masks = []
            used: set[int] = set()
            for block_index in order[:-1]:
                used.update(part[block_index])
                prefix_masks.append(tuple(sorted(used)))
            yield {
                "partition": part,
                "ordered_blocks": tuple(part[i] for i in order),
                "sign": sign,
                "prefix_label_masks": tuple(prefix_masks),
            }


def overlap_at_masks(masks: tuple[tuple[int, ...], ...], shifts: tuple[Q, ...]) -> Q:
    total = sum(shifts, Q(0))
    positions = [Q(0)]
    positions.extend(sum((shifts[j] for j in mask), Q(0)) for mask in masks)
    positions.append(total)  # the nonclosed terminal endpoint is part of the path
    return max(Q(0), Q(1) - (max(positions) - min(positions)))


def first_overlap(shifts: tuple[Q, ...]) -> Q:
    positions = [Q(0)]
    current = Q(0)
    for shift in shifts:
        current += shift
        positions.append(current)
    return max(Q(0), Q(1) - (max(positions) - min(positions)))


def exact_model_control() -> dict:
    shifts = (Q(1, 6), -Q(1, 6), Q(11, 12), -Q(11, 12))
    terms = list(ordered_terms())
    if len(terms) != 26:
        raise AssertionError("connected term count is not 26")
    bracket = sum(
        (Q(term["sign"]) * overlap_at_masks(term["prefix_label_masks"], shifts)
         for term in terms),
        Q(0),
    )
    common = first_overlap(shifts)
    model_rows = []
    weighted_bracket = Q(0)
    for index, term in enumerate(terms):
        ov = overlap_at_masks(term["prefix_label_masks"], shifts)
        # This is the hostile logical fixture's explicitly nonuniform rule.
        # It is not asserted to be an admissible source selector or weight.
        model_weight = Q(1) if index == 0 else Q(1, 100)
        contribution = Q(term["sign"]) * ov
        weighted_bracket += contribution * model_weight
        model_rows.append({
            "model_term_index": index,
            "set_partition": [list(b) for b in term["partition"]],
            "ordered_blocks": [list(b) for b in term["ordered_blocks"]],
            "overlap_prefix_label_masks_model_only": [list(m) for m in term["prefix_label_masks"]],
            "cumulant_sign": term["sign"],
            "model_overlap": str(ov),
            "model_uniform_signed_contribution": str(contribution),
            "model_positive_weight": str(model_weight),
            "model_reweighted_contribution": str(contribution * model_weight),
            "source_eligibility": "UNKNOWN_SOURCE_SEMANTICS_INCOMPLETE",
            "source_mask": None,
            "source_prime_or_prime_power_coefficient": None,
            "source_carrier_and_complex_phase": None,
            "source_root_endpoints_and_normalization": None,
            "source_normalized_weight": None,
        })
    if (bracket, common, weighted_bracket) != (Q(-1, 12), Q(1, 12), Q(1187, 1200)):
        raise AssertionError("exact abstract control changed")
    sign_counts = {
        str(k): sum(1 for t in terms if len(t["ordered_blocks"]) == k)
        for k in range(1, 5)
    }
    return {
        "classification": "ABSTRACT_LOGICAL_COUNTERMODEL_NOT_A_SOURCE_COUNTEREXAMPLE",
        "method": "independent restricted-growth partition enumerator and exact Fraction overlaps",
        "shifts": [str(v) for v in shifts],
        "net_detuning_Y": str(sum(shifts, Q(0))),
        "term_count": len(terms),
        "terms_by_number_of_ordered_blocks": sign_counts,
        "coefficient_multiplicities_by_block_count": {"1": 1, "2": 1, "3": 2, "4": 6},
        "ordered_term_sign_counts": {"positive": 13, "negative": 13},
        "first_walk_overlap": str(common),
        "unweighted_connected_bracket": str(bracket),
        "uniform_positive_scalar_example": "7/3",
        "uniformly_scaled_bracket": str(Q(7, 3) * bracket),
        "uniformly_scaled_product": str(Q(7, 3) * common * bracket),
        "positive_nonuniform_weights": "first enumerated term 1; other 25 terms 1/100",
        "all_model_weights_strictly_positive": True,
        "reweighted_bracket": str(weighted_bracket),
        "reweighted_product": str(common * weighted_bracket),
        "model_term_register": model_rows,
        "interpretation": "per-term positive weights alone do not preserve this model cancellation; source masks and weights are unavailable",
    }


def amplitude(shifts: tuple[Q, ...]) -> Q:
    terms = ordered_terms()
    bracket = sum(
        (Q(term["sign"]) * overlap_at_masks(term["prefix_label_masks"], shifts)
         for term in terms),
        Q(0),
    )
    return first_overlap(shifts) * bracket


def orientation_control() -> dict:
    s, x, y = Q(3, 2), Q(3, 4), Q(7, 8)
    base = (x, s - x, -y, -(s - y))
    all_orders = list(itertools.permutations(range(4)))
    alternating = [
        order for order in all_orders
        if all((order[j] < 2) != (order[j + 1] < 2) for j in range(3))
    ]
    six = []
    for positives in itertools.combinations(range(4), 2):
        p = set(positives)
        positive_iter, negative_iter = iter((0, 1)), iter((2, 3))
        six.append(tuple(next(positive_iter) if i in p else next(negative_iter) for i in range(4)))
    value = lambda order: amplitude(tuple(base[i] for i in order))
    c6 = sum((value(order) for order in six), Q(0))
    c24 = sum((value(order) for order in all_orders), Q(0))
    c8 = sum((value(order) for order in alternating), Q(0))
    depth = lambda u: min(u - s + 1, 1 - u)
    target = -(s - 1) * min(depth(x), depth(y))
    omitted = alternating[0]
    c8_omitted = c8 - value(omitted)
    pairings = [
        part for part in partitions(4)
        if len(part) == 2 and sorted(map(len, part)) == [2, 2]
    ]
    if not (len(six) == 6 and len(all_orders) == 24 and len(alternating) == 8):
        raise AssertionError("orientation ledger count changed")
    if not (c24 == 4 * c6 and c24 == c8 and c8 / 8 == c6 / 2 == target):
        raise AssertionError("exact orientation normalization changed")
    if c8_omitted / 8 == target:
        raise AssertionError("omitted-orientation negative control escaped")
    return {
        "classification": "EXACT_FIXED_SCALE_ORIENTATION_REPLAY_NOT_SOURCE_MASK_REPLAY",
        "rational_parameters": {"s": str(s), "x": str(x), "y": str(y)},
        "orientation_counts": {"fixed_internal_order_sign_patterns": len(six), "all_label_permutations": len(all_orders), "alternating_label_permutations": len(alternating)},
        "C6": str(c6),
        "C24": str(c24),
        "C8": str(c8),
        "identities": {"C24_eq_4C6": c24 == 4 * c6, "C24_eq_C8": c24 == c8, "C6_over_2_eq_C8_over_8": c6 / 2 == c8 / 8, "normalized_formula": str(target)},
        "omitted_orientation_negative_control": {"removed_order": list(omitted), "C8_minus_one_over_8": str(c8_omitted / 8), "expected": str(target), "rejected": c8_omitted / 8 != target},
        "two_two_pairing_subtraction_terms": len(pairings),
        "pairing_status": "exactly three 2+2 partitions have cumulant coefficient -1; they are the full pairing subtraction only when the four source factors are centered",
    }


def conjugation_control() -> dict:
    # Exact special point: T=12, L=7*pi/3, d=14, Y/L=1/4.
    # Then exp(i*T*Y)=-1 and D_14(1/4)=(1+i)/14.
    k_re, k_im = Q(-1, 14), Q(-1, 14)
    paired = (2 * k_re, Q(0))
    unpaired = (2 * k_re, 2 * k_im)
    if paired == unpaired:
        raise AssertionError("conjugation negative control escaped")
    return {
        "classification": "EXACT_GAUSSIAN_RATIONAL_FINITE_TRACE_CONTROL",
        "parameters": {"T": 12, "L": "7*pi/3", "d": 14, "Y_over_L": "1/4", "T_times_Y": "7*pi"},
        "K_T_Y": [str(k_re), str(k_im)],
        "K_T_minus_Y": [str(k_re), str(-k_im)],
        "conjugate_pair_sum": [str(paired[0]), str(paired[1])],
        "incorrect_same_orientation_pair_sum": [str(unpaired[0]), str(unpaired[1])],
        "conjugation_mutation_rejected": paired != unpaired,
        "scope": "checks the finite trace conjugation rule; does not supply a source row orientation map",
    }


def producer_probe() -> dict:
    rel = "src/wp84_fifth_full_pool_amplitude.py"
    source = (ROOT / rel).read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    cb_name = "source" + "_mask"
    iterator = next(n for n in functions if n.name == "iter_source_atoms")
    args = [a.arg for a in iterator.args.args]
    required_count = len(args) - len(iterator.args.defaults)
    cb_defs = [n for n in functions if n.name == cb_name]
    cb_calls = [n for n in ast.walk(iterator) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == cb_name]
    atom_entry = next(n for n in functions if n.name == "source_amplitude_entry")
    local_selector_names = sorted({
        n.name for n in functions
        if "section" in n.name.lower() and any(x in n.name.lower() for x in ("select", "source", "choose"))
    })
    all_tracked = git("ls-files", "-z").split("\0")
    source_files = [ROOT / p for p in all_tracked if p.startswith("src/") and p.endswith(".py")]
    project_callback_defs, project_iterator_calls = [], []
    executable_names: set[str] = set()
    for path in source_files:
        try:
            mod = ast.parse(path.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        relpath = path.relative_to(ROOT).as_posix()
        for node in ast.walk(mod):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == cb_name:
                project_callback_defs.append(f"{relpath}:{node.lineno}")
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                executable_names.add(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        executable_names.add(target.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                executable_names.add(node.target.id)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "iter_source_atoms":
                project_iterator_calls.append(f"{relpath}:{node.lineno}")
    selector_api_names = {
        "source_row_selector", "selected_section", "SOURCE_SELECTED_ROWS",
        "SOURCE_SECTION", "source_section_endpoints",
    }
    selector_pattern = r"^[[:space:]]*def[[:space:]]+(select|choose|source)[A-Za-z0-9_]*section[[:space:]]*\("
    history_selector_hits = git("log", "--all", "--format=%H%x09%s", "-G", selector_pattern, "--", "src/wp84_fifth_full_pool_amplitude.py", "src/wp84_fifth_full_pool_section_replay.py")
    callback_pattern = r"^[[:space:]]*def[[:space:]]+" + cb_name + r"[[:space:]]*\("
    history_callback_hits = git("log", "--all", "--format=%H%x09%s", "-G", callback_pattern, "--", "*.py")
    return {
        "producer_path": rel,
        "producer_revision_blob": git("rev-parse", f"{SOURCE_REVISION}:{rel}"),
        "iterator_arguments": args,
        "callback_is_required_external_argument": cb_name in args and args.index(cb_name) < required_count,
        "callback_local_definitions": len(cb_defs),
        "callback_invocation_count_inside_iterator": len(cb_calls),
        "callback_argument_arity": len(cb_calls[0].args) if cb_calls else None,
        "callback_filter_source_order": source.index("aliases=[m for m in f['aliases']") < source.index("count=max(0,n-span)"),
        "project_callback_definitions_in_tracked_src": project_callback_defs,
        "project_iterator_call_sites_in_tracked_src": project_iterator_calls,
        "known_section_selector_names_in_tracked_src": sorted(selector_api_names & executable_names),
        "section_selector_names_in_amplitude_module": local_selector_names,
        "history_callback_definition_hits_all_refs": history_callback_hits.splitlines(),
        "history_section_selector_hits_in_candidate_modules": history_selector_hits.splitlines(),
        "source_amplitude_entry_is_symbolic_schema": "Return the exact summand schema" in ast.get_source_segment(source, atom_entry),
        "candidate_not_source_authentic": True,
        "notebooklm_packet_excluded_from_source_search": True,
        "interpretation": "current candidate constructor requires an unprovided callback, section endpoints, and complete prime stream; no source-selected matrix entry is instantiated",
    }


def gate_table() -> dict:
    return {
        "SOURCE_MASK_RECONSTRUCTED": "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE",
        "CONNECTED_WEIGHT_FACTORIZATION": "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE",
        "SAFE_LOBE_SOURCE_SIGN": "FORMAL_CONDITIONAL_SIGN_PROVED_SOURCE_MATCH_BLOCKED",
        "OUTER_LOBE_CONTROL": "EXACT_ON_COMMON_PRODUCT_SCALE; UNEQUAL_SCALE_SOURCE_CONSUMER_OPEN",
        "DIAGONAL_PAIR_MATCH": "EXACT_FORMAL_Y_ZERO_KERNEL; SOURCE_ROW_MATCH_BLOCKED",
        "FULL_BOUNDED_CONSUMER": "OPEN",
        "UNCONDITIONAL_GT79": "OPEN",
    }


def claim_boundary_errors(data: dict) -> list[str]:
    """Reject any evidence mutation that promotes the logical fixture to source."""
    errors = []
    gates = data.get("gates", {})
    if gates.get("SOURCE_MASK_RECONSTRUCTED") != "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE":
        errors.append("source-mask gate promoted without source inputs")
    if gates.get("CONNECTED_WEIGHT_FACTORIZATION") != "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE":
        errors.append("connected-weight gate promoted without source inputs")
    semantics = data.get("source_semantics", {})
    if semantics.get("genuine_source_admissible_quadruples_identified") != 0:
        errors.append("uninstantiated source quadruple count changed")
    if semantics.get("source_selected_26_term_ledger_available") is not False:
        errors.append("source-selected ledger promoted without source inputs")
    if semantics.get("source_mask_order_dependence_testable") is not False:
        errors.append("source-mask ordering result promoted without a mask")
    for i, row in enumerate(data.get("formula_level_results", {}).get("abstract_countermodel", {}).get("model_term_register", [])):
        if row.get("source_eligibility") != "UNKNOWN_SOURCE_SEMANTICS_INCOMPLETE":
            errors.append(f"model row {i} was promoted to source eligibility")
        for field in (
            "source_mask",
            "source_prime_or_prime_power_coefficient",
            "source_carrier_and_complex_phase",
            "source_root_endpoints_and_normalization",
            "source_normalized_weight",
        ):
            if row.get(field) is not None:
                errors.append(f"model row {i} has an invented source value in {field}")
    boundary = data.get("claim_boundary", {})
    if boundary.get("actual_source_sign_proved") is not False:
        errors.append("actual source sign was asserted")
    if boundary.get("actual_source_counterexample_found") is not False:
        errors.append("model was promoted to a source counterexample")
    if boundary.get("greater_than_79_percent_theorem") != "OPEN":
        errors.append("greater-than-79-percent theorem status changed")
    return errors


def build_evidence() -> dict:
    manifest = source_manifest()
    for path, expected in PINNED_BLOBS.items():
        got = next(row["git_blob"] for row in manifest if row["path"] == path)
        if got != expected:
            raise AssertionError(f"pinned source blob mismatch: {path}")
    model = exact_model_control()
    orientation = orientation_control()
    conjugation = conjugation_control()
    probe = producer_probe()
    if not probe["callback_is_required_external_argument"] or probe["callback_local_definitions"] != 0:
        raise AssertionError("source callback boundary changed")
    if probe["project_callback_definitions_in_tracked_src"] or probe["project_iterator_call_sites_in_tracked_src"]:
        raise AssertionError("a tracked callback/iterator implementation appeared")
    if probe["known_section_selector_names_in_tracked_src"]:
        raise AssertionError("a tracked source section selector appeared")
    if probe["history_callback_definition_hits_all_refs"]:
        raise AssertionError("reachable source history now contains a callback definition")
    if probe["history_section_selector_hits_in_candidate_modules"]:
        raise AssertionError("reachable candidate history now contains a section selector")
    data = {
        "schema": "wp84.source-matched-26-term-sign-audit.v1",
        "captured_date": CAPTURE_DATE,
        "classification": "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE",
        "repository": {
            "source_branch_at_audit_start": SOURCE_BRANCH_AT_START,
            "source_head": SOURCE_REVISION,
            "source_context_branch": SOURCE_CONTEXT_BRANCH,
            "source_context_head": SOURCE_CONTEXT_REVISION,
            "audit_branch": AUDIT_BRANCH,
            "no_push_merge_publish_or_provider_calls": True,
            "source_search_scope": "tracked source at pinned HEAD plus reachable local/ref history",
        },
        "source_hash_manifest": manifest,
        "pinned_document_blobs": PINNED_BLOBS,
        "task_packet_verification": task_packet_manifest(),
        "history_search": {
            "reachable_commit_count_before_audit_branch_commit": 871,
            "source_mask_definition_pattern_hits": probe["history_callback_definition_hits_all_refs"],
            "candidate_section_selector_pattern_hits": probe["history_section_selector_hits_in_candidate_modules"],
            "producer_history": {
                "src/wp84_fifth_full_pool_amplitude.py": [
                    "b299cbdb12a525739ac17fc489eb7992e8f316ff"
                ],
                "src/wp84_source_q_mask_extractor.py": [
                    "f654e7a00545a6864b6f29416c080744d8ccfcc9"
                ],
                "src/wp84_source_mask_semantics_replay.py": [
                    "9401b38a8d2b8be8fc9f9597988dd93c1d6c86c1"
                ],
            },
        },
        "source_producer_probe": probe,
        "source_semantics": {
            "genuine_source_admissible_quadruples_identified": 0,
            "source_selected_26_term_ledger_available": False,
            "zero_or_absent_rows_reinterpreted_as_positive": False,
            "source_mask_order_dependence_testable": False,
            "fixed_sections_are_not_substituted_for_source_selected_sections": True,
            "unknowns": [
                "source row identities and the theorem-side matrix-entry producer",
                "actual per-row window/intersection and cutoff-transition predicates",
                "deterministic source-selected section endpoint rule and row order",
                "source-admissible prime and prime-power coefficients and carrier factors",
                "source mapping of each of the 26 ordered partitions to phases, orientations, conjugates, and roots",
                "exact source normalization and pairing-subtraction/centering rule",
            ],
        },
        "formula_level_results": {
            "connected_ordered_partition_counts": {"terms": 26, "by_blocks": {"1": 1, "2": 7, "3": 12, "4": 6}, "signs_by_blocks": {"1": "+", "2": "-", "3": "+", "4": "-"}},
            "exact_pairing_subtraction": "the 7 two-block terms include exactly 3 two-plus-two pairings and 4 one-plus-three splits; the three pairings alone are the centered fourth-cumulant subtraction only after source centering is established",
            "orientation_replay": orientation,
            "balanced_nonclosed_overlap_sign": "the pinned exact arrangement theorem proves B4_nc<=0 on the balanced 2-vs-2 sector when the common first overlap is positive; it is a theorem-side model result",
            "finite_trace": "K_T(Y)=exp(i*T*Y)*D_d(Y/L), with Re K_T(Y) used for the real connected sum; at Y=0 K=1",
            "short_shift_range": "the pinned safe-lobe theorem proves |Y|<=pi/(3T) implies Re K_T(Y)>=0 for L>=1,T>=12 and maps |h|<=M/T on M<m,n<=2M into that lobe",
            "outer_shift_range": "the scalar can change sign beyond the safe lobe; fixed common product-scale slices have an exact negative-semidefinite Schur-product sign, while unequal-scale source-selected consumption remains open",
            "conjugation_replay": conjugation,
            "abstract_countermodel": model,
        },
        "gates": gate_table(),
        "minimal_exact_missing_input": [
            "immutable source-authentic theorem-side matrix-entry producer: repository commit/blob or contemporaneous generator plus its exact inputs",
            "deterministic source row/section selector giving ordered row IDs and inclusive endpoints (k_-(T),k_+(T)) for every admitted T, with cutoff-transition/tie rules",
            "executable per-term eligibility predicate covering prime/prime-power domains, all window intersections, equality/distinctness, carrier and alias residual, orientation, path, root endpoints, and row identity",
            "exact fourth-order word expansion linking each matrix entry to all 26 ordered partitions, including complex phase/conjugation, multiplicity, centering, pairing subtraction, and normalization",
            "the exact coefficient/weight formula for each retained prime or prime power and proof of completeness of the selected pool",
        ],
        "test_classification": {
            "exact_finite_replay": ["26 term enumeration", "rational countermodel", "6/24/8 orientation normalization", "Gaussian-rational conjugation control"],
            "proof_inputs": ["pinned continuous trace and overlap identities", "pinned safe-lobe and fixed-scale kernel theorems"],
            "floating_checks": [],
            "model_only": ["nonuniform positive reweighting witness; not a WP84 source counterexample"],
        },
        "claim_boundary": {
            "actual_source_sign_proved": False,
            "actual_source_counterexample_found": False,
            "greater_than_79_percent_theorem": "OPEN",
            "rh_claim": False,
        },
    }
    errors = claim_boundary_errors(data)
    if errors:
        raise AssertionError("claim boundary failed: " + "; ".join(errors))
    return data


def main() -> None:
    data = build_evidence()
    EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE_PATH.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("classification =", data["classification"])
    print("source HEAD =", data["repository"]["source_head"])
    print("source files hash-pinned =", len(data["source_hash_manifest"]))
    print("exact model bracket =", data["formula_level_results"]["abstract_countermodel"]["unweighted_connected_bracket"])
    print("reweighted model bracket =", data["formula_level_results"]["abstract_countermodel"]["reweighted_bracket"])
    print("source-selected 26-term sum = BLOCKED_SOURCE_SEMANTICS_INCOMPLETE")
    print("evidence =", EVIDENCE_PATH.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()

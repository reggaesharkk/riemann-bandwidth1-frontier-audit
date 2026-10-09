"""Extract the checked-in source_mask callback contract for WP84 block 15.

This is a source inspection utility, not a selector reconstruction.  It only
parses current source files and pinned current mathematical notes; it does not
search Git history, refs, attachments, or notebooklm_packet/.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "src/wp84_fifth_full_pool_amplitude.py"
CANON = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
BLOCK = [15, 20, 26, 28, 31, 32]
AUDIT_SELF = {
    "wp84_source_mask_contract_extractor.py",
    "wp84_source_mask_constraint_builder.py",
    "wp84_source_mask_semantics_replay.py",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def names(node: ast.AST) -> list[str]:
    return [n.id for n in ast.walk(node) if isinstance(n, ast.Name)]


def extract_contract() -> dict:
    tree = ast.parse(TARGET.read_text(encoding="utf-8"), filename=str(TARGET))
    functions = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    defs = [n for n in functions if n.name == "source_mask"]
    iterator = next(n for n in functions if n.name == "iter_source_atoms")
    args = [a.arg for a in iterator.args.args]
    callback_calls = [
        n for n in ast.walk(iterator)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "source_mask"
    ]
    callback_call = callback_calls[0]
    call_args = [ast.unparse(a) for a in callback_call.args]
    list_filters = [
        ast.unparse(gen.ifs[0])
        for n in ast.walk(iterator) if isinstance(n, ast.ListComp)
        for gen in n.generators if gen.ifs and any("source_mask" in names(f) for f in gen.ifs)
    ]
    aliases_used = any(
        isinstance(n, ast.Name) and n.id == "aliases" and isinstance(getattr(n, "ctx", None), ast.Load)
        for n in ast.walk(iterator)
    )
    # Count exact executable AST names in existing project Python, excluding
    # these new audit utilities so their self-description cannot inflate counts.
    pyfiles = [p for p in (ROOT / "src").glob("*.py") if p.name not in AUDIT_SELF]
    project_defs = []
    project_calls = []
    iterator_calls = []
    for path in pyfiles:
        try:
            mod = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError:
            continue
        for node in ast.walk(mod):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "source_mask":
                project_defs.append(f"{path.relative_to(ROOT).as_posix()}:{node.lineno}")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == "source_mask":
                    project_calls.append(f"{path.relative_to(ROOT).as_posix()}:{node.lineno}")
                if node.func.id == "iter_source_atoms":
                    iterator_calls.append(f"{path.relative_to(ROOT).as_posix()}:{node.lineno}")

    data = json.loads(CANON.read_text(encoding="utf-8"))
    descriptors = []
    for fid in BLOCK:
        f = next(row for row in data if row["id"] == fid)
        descriptors.append({
            "id": fid,
            "degree": f["degree"],
            "sign_word": f["sign_word"],
            "equality_partition": f["equality_partition"],
            "aliases": f["aliases"],
            "raw_orbit_members": len(f["raw_orbit_members"]),
            "definition": f["definition"],
        })
    return {
        "scope": "current checked-in source only; no Git history/ref/attachment/packet search",
        "target": TARGET.relative_to(ROOT).as_posix(),
        "target_sha256": sha256(TARGET),
        "iterator_signature_arguments": args,
        "callback_parameter_position_zero_based": args.index("source_mask"),
        "callback_parameter_has_annotation": next(a for a in iterator.args.args if a.arg == "source_mask").annotation is not None,
        "callback_local_definitions_in_target": len(defs),
        "project_python_source_mask_definitions": project_defs,
        "project_python_source_mask_calls": project_calls,
        "project_python_iter_source_atoms_calls": iterator_calls,
        "callback_call_count_inside_iterator": len(callback_calls),
        "callback_call_arguments": call_args,
        "callback_call_keyword_arguments": [kw.arg for kw in callback_call.keywords],
        "callback_result_list_comprehension_filter": list_filters,
        "callback_result_consumed_as_boolean_filter": bool(list_filters),
        "aliases_truthiness_checked_after_filter": "if not aliases" in ast.unparse(iterator),
        "callback_output_used_to_weight_or_rewrite_atom": False,
        "callback_output_type_annotation_assertion_or_runtime_type_check": False,
        "callback_mathematical_argument_meanings": [
            {"position": 0, "name": "fid", "meaning": "canonical functional id; descriptor loaded from canonical JSON"},
            {"position": 1, "name": "slots", "meaning": "five actual slot primes derived from the injective equality-block assignment"},
            {"position": 2, "name": "lag", "meaning": "one five-displacement path generated by paths(R)"},
            {"position": 3, "name": "T", "meaning": "height supplied to iterator"},
            {"position": 4, "name": "section", "meaning": "inclusive endpoint pair (k_-, k_+) supplied to iterator"},
            {"position": 5, "name": "m", "meaning": "one alias from the descriptor's finite alias list"},
        ],
        "callback_does_not_receive": [
            "carrier as an explicit argument (though iterator has it and filters exact valuation before call)",
            "prime_stream or N",
            "R as a separate argument (only the already-generated lag is passed)",
            "root index, root interval, prefix vector, or root count (computed after callback)",
            "d or d' as named variables",
            "a_phi or any normalization object",
            "selected row/cell identity or row order",
            "Fourier alias residual/delta as a precomputed value",
        ],
        "outer_iterator_checks_before_callback": [
            "prime-stream entries lie in [2,N] (not primality or completeness)",
            "prime stream sorted and duplicate-free",
            "distinct primes on equality blocks",
            "optional hidden excess-pair core-prime restriction when core_primes is passed",
            "exact signed valuation carrier equals requested carrier",
            "path is generated with coordinates in [-R,R] and sum zero",
        ],
        "outer_iterator_checks_after_callback": [
            "root count max(0,n-span) is positive; otherwise atom skipped",
            "root interval and symbolic root sum are then constructed",
        ],
        "normalization_state_at_callback": "none applied by callback call; a_phi^-5 is retained later in the yielded expression schema",
        "block_descriptors": descriptors,
        "pinned_canonical_json_sha256": sha256(CANON),
    }


if __name__ == "__main__":
    print(json.dumps(extract_contract(), indent=2, sort_keys=True))

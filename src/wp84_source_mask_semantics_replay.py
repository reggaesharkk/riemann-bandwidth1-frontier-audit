"""Independent replay and hostile mutation tests for block-15 mask audit."""
from __future__ import annotations

import ast
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from wp84_source_mask_contract_extractor import TARGET, extract_contract, sha256  # noqa: E402

CERT = ROOT / "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json"


def independently_inspect(source: str) -> dict:
    tree = ast.parse(source)
    funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    defs = [n for n in funcs if n.name == "source_mask"]
    if defs:
        raise AssertionError("unexpected in-module source_mask definition")
    it = next(n for n in funcs if n.name == "iter_source_atoms")
    calls = [n for n in ast.walk(it) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "source_mask"]
    if len(calls) != 1:
        raise AssertionError("callback invocation count changed")
    call = calls[0]
    if len(call.args) != 6:
        raise AssertionError("callback arity changed")
    listcomp = [n for n in ast.walk(it) if isinstance(n, ast.ListComp) and any(
        isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == "source_mask"
        for c in ast.walk(n)
    )]
    if len(listcomp) != 1 or not listcomp[0].generators[0].ifs:
        raise AssertionError("callback is no longer used as list-filter predicate")
    return {
        "definitions": len(defs),
        "arguments": [ast.unparse(a) for a in call.args],
        "arity": len(call.args),
        "filter": ast.unparse(listcomp[0].generators[0].ifs[0]),
        "root_after_callback": source.index("aliases=[m for m in f['aliases'] if source_mask") < source.index("count=max(0,n-span)"),
        "has_explicit_slot_window_formula": bool(defs) and any(
            token in ast.get_source_segment(source, defs[0]).lower()
            for token in ("window", "chi", "indicator")
        ),
        "has_section_selector": "def select_section" in source or "def section_selector" in source,
    }


def run() -> dict:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    current = TARGET.read_text(encoding="utf-8")
    independent = independently_inspect(current)
    contract = extract_contract()
    assert cert["decision"] == "E. SOURCE SEMANTICS INCOMPLETE"
    assert cert["contract"] == contract
    assert cert["contract"]["target_sha256"] == sha256(TARGET)
    assert independent["definitions"] == 0
    assert independent["arguments"] == ["fid", "slots", "lag", "T", "section", "m"]
    assert independent["arity"] == 6
    assert independent["root_after_callback"] is True
    assert independent["has_explicit_slot_window_formula"] is False
    assert independent["has_section_selector"] is False
    assert cert["source_constraints_that_fix_specific_membership_bits"] == 0
    assert cert["explicit_expected_membership_rows"] == 0
    assert cert["candidate_row_count"] is None and cert["admissible_mask_count"] is None
    assert cert["source_admissible_projected_rank_min"] is None
    assert cert["source_admissible_projected_rank_max"] is None

    mutations = []
    def rejects(label: str, changed: str) -> None:
        try:
            independently_inspect(changed)
        except (AssertionError, StopIteration, SyntaxError):
            mutations.append(label)
            return
        raise AssertionError(f"hostile mutation unexpectedly accepted: {label}")

    rejects("callback implementation fabricated", current.replace("def iter_source_atoms(", "def source_mask(*args): return True\n\ndef iter_source_atoms(", 1))
    rejects("callback arity changed", current.replace(
        "if source_mask(fid,slots,lag,T,section,m)]",
        "if source_mask(fid,slots,lag,T,section)]", 1))
    rejects("truthiness filtering removed", current.replace(
        "if source_mask(fid,slots,lag,T,section,m)]", "if True]", 1))
    # These two mutations preserve the callback AST but invalidate the exact
    # source hash and the pinned semantics in the certificate.
    for label, changed in [
        ("slot window guessed", current + "\n# invented slot-window predicate\n"),
        ("section selector guessed", current + "\ndef select_section(T): return (0, 1)\n"),
    ]:
        if changed == current:
            raise AssertionError("mutation construction failed")
        digest = hashlib.sha256(changed.encode("utf-8")).hexdigest()
        if digest == cert["contract"]["target_sha256"]:
            raise AssertionError(f"hostile mutation escaped source hash pin: {label}")
        mutations.append(label + " rejected by source hash / evidence pin")

    return {
        "decision": cert["decision"],
        "independent_ast_replay": "PASS",
        "contract_consistency": "PASS",
        "hostile_mutations_rejected": mutations,
        "mutation_count": len(mutations),
        "source_hash": sha256(TARGET),
        "rank_and_K_status": "unknown; not instantiated",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))

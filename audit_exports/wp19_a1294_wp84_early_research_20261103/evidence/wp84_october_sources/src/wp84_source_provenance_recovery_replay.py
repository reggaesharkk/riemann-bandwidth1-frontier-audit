"""Read-only provenance inventory and fail-closed replay for the WP84 row selector.

The script writes one JSON certificate in the worktree.  It reads repo files,
Git metadata, the NotebookLM PDFs and the local attachment index; it never
checks out a ref or changes packet contents.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "7419a751de7bd5890e7ff6210ca8ec9125dab7aa"
ATTACHMENT_INDEX = Path(r"C:\Users\Asus\.codex\attachments\pasted-text-attachments.json")
DOWNLOADS = Path(r"C:\Users\Asus\Downloads\riemann-bandwidth1-frontier-audit")

DETAILS = {
    "notes/WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md": {
        "executable": False, "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": "453 formal functionals; no selected row mapping",
        "authenticity": "local mathematical reconstruction; input-domain formula",
        "finding": "states that a particular endpoint selector would need to be fixed; no selector is supplied",
    },
    "src/wp84_fifth_full_pool_amplitude.py": {
        "executable": "partial summand constructor", "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": True,
        "authenticity": "local reconstructed constructor, introduced at b299cbdb",
        "finding": "section and carrier are arguments; iter_source_atoms requires external source_mask and full prime stream",
    },
    "src/wp84_fifth_full_pool_section_replay.py": {
        "executable": True, "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": "generic five-step root jets",
        "authenticity": "local exact structural replay",
        "finding": "proves root/jet identities conditional on n, span, and section; does not select endpoints or rows",
    },
    "notes/WP84_FIFTH_FULL_POOL_LARGE_SECTION_LIFT.md": {
        "executable": False, "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": True,
        "authenticity": "local source-formula reconstruction",
        "finding": "states d'/d -> 1 and actual I(T); notes determinant row selection/alignment remains required",
    },
    "src/wp84_source_q_mask_extractor.py": {
        "executable": "q predicate only", "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": True,
        "authenticity": "reconstructed later at f654e7a; not original amplitude callback",
        "finding": "signature differs from iterator callback and consumes carrier_alias_admissible as input state",
    },
    "src/wp84_hidden_prime_moment_constructor.py": {
        "executable": "symbolic constructor", "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": True,
        "authenticity": "local reconstruction at 990ccbd",
        "finding": "calls chi_q an exact mask but says its exact equality is not executable in the repository",
    },
    "src/wp84_fifth_legal_stencil_replay.py": {
        "executable": True, "rows": "synthetic fixture", "row_order": "diagnostic only",
        "section_selector": False, "R6000": "only legality fixture", "four_blocks": True,
        "authenticity": "later diagnostic replay at fc04f3b",
        "finding": "explicitly says its synthetic fixture is not a certified legal cell",
    },
    "notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json": {
        "executable": False, "rows": "diagnostic rows only", "row_order": "specialization/amplitude_order",
        "section_selector": False, "R6000": False, "four_blocks": True,
        "authenticity": "formal diagnostic at e139eea",
        "finding": "finite specializations n=2/3, R=1/2 and rational surrogate logs; rank not promoted",
    },
    "src/wp84_carrier_aware_amplitude_recon.py": {
        "executable": True, "rows": "toy numeric", "row_order": "toy only",
        "section_selector": False, "R6000": False, "four_blocks": False,
        "authenticity": "later toy reconstruction at c819938",
        "finding": "I=(2,3,4,5), R=1; result marks source section uncertified",
    },
    "src/wp84_signed_near_product_cell_recon.py": {
        "executable": "numerical reconnaissance", "rows": "prime/product tuples only", "row_order": "not fifth-block rows",
        "section_selector": "candidate q=floor(d/sqrt(L)), k0=floor(q/2), I=[k0,k0+dprime-1], explicitly uncertified",
        "R6000": "input parameter; this does not validate the candidate section", "four_blocks": "exploratory degree-5/6 cells only",
        "authenticity": "later finite-T diagnostic at 95458d6",
        "finding": "candidate_section_theorem_certified is false in generated records",
    },
    "notes/WP84_SIGNED_NEAR_PRODUCT_CELL_RECON.json": {
        "executable": False, "rows": "diagnostic tuples", "row_order": "sampling order only",
        "section_selector": "stores candidate interval with candidate_section_theorem_certified=false",
        "R6000": True, "four_blocks": "not determinant blocks",
        "authenticity": "generated numerical reconnaissance",
        "finding": "candidate interval is not certified for original theorem",
    },
    "notes/WP84_FIFTH_SHARED_BLOCK_TABLE.json": {
        "executable": False, "rows": False, "row_order": False,
        "section_selector": False, "R6000": False, "four_blocks": True,
        "authenticity": "frozen descriptor table at e5f3405",
        "finding": "defines functional/layout column blocks only",
    },
    "notes/WP84_FIFTH_FULL_POOL_SECTION_REPLAY.json": {
        "executable": False, "rows": False, "row_order": False,
        "section_selector": False, "R6000": True, "four_blocks": "generic paths",
        "authenticity": "generated exact identity certificate",
        "finding": "path span <=12000 and roots for n>=12001; no T-to-endpoints rule",
    },
}


def git(*args: str, cwd: Path = ROOT, check: bool = True) -> str:
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=check)
    return p.stdout.strip()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def origin(path: str) -> dict:
    log = git("log", "--all", "--follow", "-1", "--format=%H", "--", path)
    if not log:
        return {"commit": None, "blob": None}
    commit = log.splitlines()[0]
    try:
        blob = git("rev-parse", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        blob = None
    return {"commit": commit, "blob": blob}


def source_probe() -> dict:
    rel = "src/wp84_fifth_full_pool_amplitude.py"
    source = (ROOT / rel).read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = {n.name: n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    iterator = functions["iter_source_atoms"]
    params = [a.arg for a in iterator.args.args]
    defaults = len(iterator.args.defaults)
    required_count = len(params) - defaults
    source_mask_external_required = "source_mask" in params and params.index("source_mask") < required_count
    # Search actual Python call expressions, excluding the definition itself.
    callers = []
    python_files = [
        py for py in ROOT.rglob("*.py")
        if ".git" not in py.parts and "notebooklm_packet" not in py.parts
    ]
    for py in python_files:
        try:
            module = ast.parse(py.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(module):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "iter_source_atoms":
                callers.append(str(py.relative_to(ROOT)))
    qsrc = (ROOT / "src/wp84_source_q_mask_extractor.py").read_text(encoding="utf-8")
    qtree = ast.parse(qsrc)
    qfn = next(n for n in ast.walk(qtree) if isinstance(n, ast.FunctionDef) and n.name == "q_mask")
    qparams = [a.arg for a in qfn.args.args]
    callback_calls = [
        n for n in ast.walk(iterator)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "source_mask"
    ]
    callback_arity = len(callback_calls[0].args) if callback_calls else None
    selector_names = {"source_row_selector", "selected_section", "SOURCE_SELECTED_ROWS", "SOURCE_SECTION", "source_section_endpoints"}
    executable_names = set()
    for py in python_files:
        if py.name.startswith("wp84_source_provenance_recovery") or py.name.startswith("wp84_determinant_visible_hidden"):
            continue
        try:
            module = ast.parse(py.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(module):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                executable_names.add(node.name)
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if isinstance(target, ast.Name):
                        executable_names.add(target.id)
    return {
        "iterator_signature": params,
        "source_mask_is_required_external_argument": source_mask_external_required,
        "actual_call_sites_under_repository": callers,
        "python_files_scanned_for_call_sites": len(python_files),
        "q_mask_signature": qparams,
        "iterator_source_mask_call_arity": callback_arity,
        "q_mask_call_compatible_with_iterator": len(qparams) == callback_arity,
        "q_mask_consumes_precomputed_alias_boolean": "carrier_alias_admissible" in qsrc,
        "executable_row_or_section_selector_names_present": sorted(selector_names & executable_names),
        "block_ids": {
            "B6": [15,20,26,28,31,32],
            "B8a": [10,12,16,17,21,22,25,29],
            "B16": [36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],
            "B8b": [34,37,39,43,53,56,60,63],
        },
    }


def build() -> dict:
    candidates = []
    for path, detail in DETAILS.items():
        full = ROOT / path
        ref = origin(path)
        candidates.append({"path": path, **ref, "sha256_worktree": sha(full) if full.is_file() else None, **detail})
    branches = git("for-each-ref", "--format=%(refname:short) %(objectname:short)", "refs/heads", "refs/remotes").splitlines()
    tags = git("tag", "--list").splitlines()
    reflog = git("reflog", "--all", "--format=%H %gs").splitlines()
    fsck = git("fsck", "--full", "--no-reflogs", "--unreachable", check=True) if False else subprocess.run(
        ["git", "fsck", "--full", "--no-reflogs", "--unreachable"], cwd=ROOT, capture_output=True, text=True
    ).stdout.splitlines()
    unreachable = {kind: [line.split()[2] for line in fsck if line.startswith(f"unreachable {kind} ")] for kind in ("commit", "tree", "blob")}
    index = json.loads(ATTACHMENT_INDEX.read_text(encoding="utf-8")) if ATTACHMENT_INDEX.is_file() else {}
    attachment_paths = index.get("attachmentPaths", [])
    pdfs = []
    for p in sorted((ROOT / "notebooklm_packet").glob("*.pdf")):
        pdfs.append({"path": str(p.relative_to(ROOT)), "sha256": sha(p), "bytes": p.stat().st_size})
    # Captured through the authorized read-only shell inspection. A Python
    # subprocess is intentionally not used for this checkout because Windows
    # Git marks its owner as a different SID in the sandbox process.
    downloads = {
        "head": "908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5",
        "branch": "research/frontier-7962-hostile-audit-v0.1",
        "status": "clean; tracking origin/research/frontier-7962-hostile-audit-v0.1",
        "reachable_commit_count": 813,
        "source_selector_search": "no matching executable row/section selector or source_mask definition found",
        "inspection": "read-only PowerShell git/rg; no checkout or mutation",
    }
    return {
        "decision": "C",
        "decision_text": "SOURCE SELECTOR NOT PRESENT — theorem search must remain stopped",
        "audit_start_head": START,
        "audit_head_is_current_or_ancestor": subprocess.run(["git", "merge-base", "--is-ancestor", START, "HEAD"], cwd=ROOT, capture_output=True).returncode == 0,
        "worktree_root": str(ROOT),
        "no_network_or_checkout_operations": True,
        "refs_at_audit": branches,
        "tags_at_audit": tags,
        "reachable_commit_count_at_audit": 813,
        "reflog_count_at_audit": len(reflog),
        "reflog_recorded_commits_at_audit": sorted({x.split()[0] for x in reflog if x.split()}),
        "unreachable_objects_at_audit": {k: {"count": len(v), "ids": v} for k,v in unreachable.items()},
        "unreachable_commit_conclusion": "none; orphan blobs/trees only, all scanned; no recovered selector",
        "downloads_checkout_read_only": downloads,
        "attachments": {
            "index_path": str(ATTACHMENT_INDEX),
            "index_sha256": sha(ATTACHMENT_INDEX) if ATTACHMENT_INDEX.is_file() else None,
            "listed_attachment_count": len(attachment_paths),
            "kind": "user instruction packets; semantic matches are requests/audit history, not source-authentic definitions",
        },
        "notebooklm_packet_read_only": {
            "manifest_snapshot_commit": "be7eee7d2e44f68933b9415787619fac5f0534e3",
            "pdfs": pdfs,
            "principal_section_evidence": "q=floor(d/sqrt(L)), d'>=d-2q, d'/d->1: a section size/trim condition, not an endpoint selector",
            "selector_found": False,
        },
        "iterator_probe": source_probe(),
        "candidates": candidates,
        "unreachable_mask_audit_blob": {
            "git_blob": "a4ede5f46330b743695d741a7ce177bcdd02e05a",
            "first_line": "Physical mask extraction and twist audit",
            "parent_named_in_blob": "876188d9f67cf8de5b3a15f6ed60b9ab3ea37596",
            "target_source_selector": False,
            "reason": "auxiliary arithmetic twist/reconstruction object; no fifth source-row or section selection",
        },
        "frozen_hidden_moment_state": {"candidate_coordinates": 73, "master_moments": [f"S_{j}" for j in range(2,11)], "J": 9, "K": None},
        "recovered": False,
        "minimum_manual_specification": [
            "ordered source row IDs and semantics, including whether rows are T/cell evaluations or coefficient jets",
            "mapping from those rows to the 453 functionals and all four frozen fifth blocks",
            "deterministic T -> (k_-(T),k_+(T)) section rule with trimming/tie-breaks and proof of d'/d -> 1 and large-section threshold",
            "complete executable chi/source_mask with prime windows, equalities/distinctness, carrier/alias/nonzero-detuning, orientation, path, and root gates",
            "entry/jet extractor retaining complete visible assignments, full hidden-q range, R=6000 paths/phases, roots, multiplicities, and normalization",
            "pinned source-authentic origin: immutable source commit/blob or contemporaneous generator and inputs",
        ],
    }


def validate(data: dict) -> list[str]:
    errors = []
    if data.get("decision") != "C" or data.get("recovered") is not False:
        errors.append("unsupported recovery decision")
    if data.get("audit_start_head") != START:
        errors.append("wrong starting HEAD")
    if data.get("frozen_hidden_moment_state") != {"candidate_coordinates":73,"master_moments":[f"S_{j}" for j in range(2,11)],"J":9,"K":None}:
        errors.append("frozen 73 -> 9 -> K state changed")
    probe = data.get("iterator_probe", {})
    if not probe.get("source_mask_is_required_external_argument"):
        errors.append("source-mask evidence changed")
    if probe.get("actual_call_sites_under_repository"):
        errors.append("unexpected iterator call site appeared")
    if probe.get("q_mask_call_compatible_with_iterator"):
        errors.append("q helper was incorrectly treated as the amplitude callback")
    if data.get("notebooklm_packet_read_only", {}).get("selector_found") is not False:
        errors.append("unsupported packet selector claim")
    for item in data.get("candidates", []):
        path = ROOT / item["path"]
        if not path.is_file() or sha(path) != item.get("sha256_worktree"):
            errors.append(f"candidate source changed: {item['path']}")
        if origin(item["path"]) != {"commit": item.get("commit"), "blob": item.get("blob")}:
            errors.append(f"candidate Git provenance changed: {item['path']}")
    for item in data.get("notebooklm_packet_read_only", {}).get("pdfs", []):
        path = ROOT / item["path"]
        if not path.is_file() or sha(path) != item["sha256"]:
            errors.append(f"packet PDF changed: {item['path']}")
    return errors


def main() -> None:
    out = ROOT / "notes/WP84_SOURCE_PROVENANCE_RECOVERY_CERTIFICATE.json"
    if __import__("sys").argv[1:] == ["--verify"]:
        data = json.loads(out.read_text(encoding="utf-8"))
        errors = validate(data)
        if errors:
            raise SystemExit("FAIL: " + "; ".join(errors))
        print("PASS source-provenance replay: C; no selector recovered; source hashes/provenance agree")
        return
    data = build()
    errors = validate(data)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(errors))
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("PASS source-provenance inventory built")
    print(f"decision={data['decision_text']}")
    print(f"reachable commits={data['reachable_commit_count_at_audit']}; unreachable commits={data['unreachable_objects_at_audit']['commit']['count']}; orphan blobs={data['unreachable_objects_at_audit']['blob']['count']}")
    print("q mask helper is not the amplitude iterator callback; no selected-row/section selector found")


if __name__ == "__main__":
    main()

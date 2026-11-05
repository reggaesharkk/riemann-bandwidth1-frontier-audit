from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Callable

Plugin = Callable[[Path, dict], tuple[bool, str]]


def verify_text_status(path: Path, spec: dict) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    required = spec.get("required_strings", [])
    missing = [s for s in required if s not in text]
    if missing:
        return False, f"missing required strings: {missing}"
    forbidden = spec.get("forbidden_strings", [])
    present = [s for s in forbidden if s in text]
    if present:
        return False, f"forbidden strings present: {present}"
    return True, f"matched {len(required)} required strings"


def verify_lrsc_coverage_log(path: Path, spec: dict) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    k = int(spec["K"])
    n = int(spec.get("N", 50))
    expected = math.comb(n, k)
    m = re.search(rf"K={k} covered=(\d+) expected=(\d+)", text)
    if not m:
        return False, "coverage line missing"
    covered, logged_expected = map(int, m.groups())
    if logged_expected != expected:
        return False, f"logged expected {logged_expected} != comb({n},{k}) {expected}"
    if covered != expected:
        return False, f"covered {covered} != expected {expected}"
    if "STATUS=PROVED_NO_PASS_AT_K" not in text:
        return False, "proof status marker missing"
    if re.search(rf"K={k} .*capped=[1-9]", text):
        return False, "search was capped"
    if re.search(rf"K={k} .*unresolved=[1-9]", text):
        return False, "search has unresolved branches"
    return True, f"exact combinatorial coverage {covered}/{expected}; no passing subset at K={k}"


def verify_lrsc_witness_summary(path: Path, spec: dict) -> tuple[bool, str]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    upper_r2 = int(obj["residual_r2_interval_scaled_1e35"][1])
    c_lower = int(obj["target_norm2_lower_scaled_1e35"])
    tolerance = float(obj["relative_tolerance"])
    # R^2/c < tolerance^2, all evaluated as integers for 1e-3 -> 1e-6.
    scale = int(round(1.0 / (tolerance * tolerance)))
    ok = upper_r2 * scale < c_lower
    if not ok:
        return False, f"witness fails integer gate: {upper_r2}*{scale} >= {c_lower}"
    subset = obj["subset"]
    if len(subset) != int(spec.get("K", len(subset))):
        return False, "witness cardinality mismatch"
    return True, f"witness passes: R^2/c < {tolerance**2:g}; |S|={len(subset)}"


PLUGINS: dict[str, Plugin] = {
    "text_status": verify_text_status,
    "lrsc_coverage_log": verify_lrsc_coverage_log,
    "lrsc_witness_summary": verify_lrsc_witness_summary,
}


def verify_lrsc_definition_v3(path: Path, spec: dict) -> tuple[bool, str]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        expected = {
            "M": 99,
            "k_idx": 49,
            "A": "1/2",
            "theta": "7/100",
            "relative_L2_tolerance": "1/1000",
        }
        if obj.get("schema") != "intentseal-vrk-lrsc-definition-v1":
            return False, "definition schema mismatch"
        if obj.get("system") != "LRSC" or obj.get("kind") != "finite_benchmark":
            return False, "definition system/kind mismatch"
        if obj.get("parameters") != expected:
            return False, f"definition parameters mismatch: {obj.get('parameters')}"
        c = obj.get("construction", {})
        required = {
            "X_t", "stress_C_t", "shedding_J_t", "mask_m_t", "dft_normalization",
            "stencil_q", "target_q", "channel_0_q", "channel_r_q", "residual_metric", "predicate",
        }
        if not required.issubset(c):
            return False, f"definition construction missing: {sorted(required-set(c))}"
        if obj.get("scope") != {"finite_only": True, "continuum_implication": False}:
            return False, "definition scope firewall mismatch"
        return True, "formal LRSC finite benchmark definition matches v0.3 adapter"
    except Exception as e:
        return False, f"malformed LRSC definition: {e}"


def verify_lrsc_replay_witness(path: Path, spec: dict) -> tuple[bool, str]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if obj.get("schema") != "intentseal-vrk-lrsc-witness-v1":
            return False, "witness schema mismatch"
        if (obj.get("M"), obj.get("k_idx"), obj.get("A"), obj.get("theta"), obj.get("relative_tolerance")) != (99,49,"1/2","0.07","1e-3"):
            return False, "witness parameters mismatch"
        subset = obj.get("subset", [])
        if len(subset) != int(spec.get("K", 14)) or len(set(subset)) != len(subset):
            return False, "witness cardinality/uniqueness mismatch"
        upper = int(obj["residual_r2_interval_scaled_1e35"][1])
        lower = int(obj["target_norm2_interval_scaled_1e35"][0])
        if upper * 10**6 >= lower or obj.get("gate_pass") is not True:
            return False, "direct outward-rounded K14 integer gate failed"
        return True, f"direct interval witness passes integer gate; |S|={len(subset)}"
    except Exception as e:
        return False, f"malformed replay witness: {e}"


def verify_lrsc_full_replay_manifest(path: Path, spec: dict) -> tuple[bool, str]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if obj.get("schema") != "intentseal-vrk-lrsc-full-replay-v1" or obj.get("result") != "CERTIFICATE_REPLAY_PASS":
            return False, "full replay result/schema mismatch"
        if obj.get("canonical_lrsc_commit") != "0d59b323a06d386e81843a50db7604cec314e3f9":
            return False, "canonical LRSC commit mismatch"
        con = obj.get("construction", {})
        if con.get("active_nodes") != 83 or con.get("mask_cell_verified") != ["0.055791974", "0.071206343"]:
            return False, "mask/cell replay mismatch"
        perm = con.get("channel_permutation", [])
        if sorted(perm) != list(range(50)) or con.get("permutation_exact_audit") is not True:
            return False, "channel permutation audit failed"
        if obj.get("K0", {}).get("covered") != 1 or obj.get("K0", {}).get("expected") != 1:
            return False, "K0 exclusion/coverage missing"
        rows = obj.get("K1_to_K13", [])
        if [int(r.get("K", -1)) for r in rows] != list(range(1,14)):
            return False, "K1..K13 replay rows incomplete"
        total = 1
        for row in rows:
            k = int(row["K"]); expected = math.comb(50,k)
            if int(row.get("covered", -1)) != expected or int(row.get("expected", -1)) != expected:
                return False, f"K{k} exact coverage mismatch"
            if row.get("status") != "PROVED_NO_PASS_AT_K" or row.get("capped") or row.get("unresolved"):
                return False, f"K{k} search incomplete"
            total += expected
        expected_total = sum(math.comb(50,k) for k in range(14))
        if total != expected_total or obj.get("coverage_total_K0_to_K13") != expected_total or obj.get("coverage_expected_K0_to_K13") != expected_total:
            return False, "aggregate K0..K13 coverage mismatch"
        w = obj.get("K14_witness", {})
        upper = int(w["residual_r2_interval_scaled_1e35"][1]); lower = int(w["target_norm2_interval_scaled_1e35"][0])
        if len(w.get("subset", [])) != 14 or upper*10**6 >= lower:
            return False, "embedded K14 witness gate failed"
        if obj.get("independent_post_run_verification") is not True:
            return False, "post-run verification flag missing"
        prov = obj.get("source_provenance", {})
        required_blobs = {
            "lrsc_interval_certificate.py": "47258feb9fa91ee99a209e0a2a9004981a411603",
            "rigorous_coordinate_search.cpp": "94391832e7e08f6a1579f803debbcc7077dee46a",
        }
        for name, blob in required_blobs.items():
            if prov.get(name, {}).get("git_blob_sha") != blob:
                return False, f"vendored canonical source binding mismatch: {name}"
        return True, f"full local LRSC replay covers all {expected_total} subsets at K=0..13 and verifies K14 witness"
    except Exception as e:
        return False, f"malformed full replay manifest: {e}"


def verify_lrsc_independent_recheck(path: Path, spec: dict) -> tuple[bool, str]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if obj.get("schema") != "intentseal-vrk-lrsc-independent-recheck-v1" or obj.get("result") != "PASS":
            return False, "independent recheck result/schema mismatch"
        expected_total = sum(math.comb(50,k) for k in range(14))
        checks = (
            obj.get("active_nodes") == 83,
            obj.get("coverage_K0_to_K13") == expected_total,
            obj.get("K14_integer_witness_gate") is True,
            obj.get("permutation_exact") is True,
            obj.get("vendor_git_blobs_match") is True,
        )
        if not all(checks):
            return False, "independent recheck field failure"
        return True, "independent post-run recheck passes provenance, permutation, coverage and K14 gate"
    except Exception as e:
        return False, f"malformed independent recheck: {e}"


PLUGINS.update({
    "lrsc_definition_v3": verify_lrsc_definition_v3,
    "lrsc_replay_witness": verify_lrsc_replay_witness,
    "lrsc_full_replay_manifest": verify_lrsc_full_replay_manifest,
    "lrsc_independent_recheck": verify_lrsc_independent_recheck,
})

# v0.3 executable replay trust roots.  These are part of the kernel source
# fingerprint; changing a trusted driver changes the verification kernel.
_V03_REPLAY_DRIVER_SHA256 = "1b74da45b70f8fe1c453ecaef74833b762f706e9aff679098017ea8e7783f812"
_V03_RECHECK_DRIVER_SHA256 = "ff6431555b6ec16eb65723132a6f0f2abd88d2aef6a341ed36b7586732935f2d"
_V03_REPLAY_CACHE: dict[str, tuple[bool, str]] = {}


def _sha256_path(path: Path) -> str:
    import hashlib
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _normalized_replay_manifest(obj: dict) -> dict:
    # Runtime/host metadata and wall times are not mathematical certificate data.
    out = json.loads(json.dumps(obj))
    out.pop("environment", None)
    out.get("construction", {}).pop("build_seconds", None)
    for row in out.get("K1_to_K13", []):
        row.pop("seconds", None)
    return out


def verify_lrsc_execute_full_replay(path: Path, spec: dict) -> tuple[bool, str]:
    """Re-execute the full finite proof stack in a temporary output directory.

    The trusted replay driver and its canonical vendored LRSC sources are rooted
    in the running kernel tree, not in the claim directory.  The fresh replay is
    compared to the stored certificate after removing host/timing-only fields.
    """
    import os
    import subprocess
    import sys
    import tempfile

    kernel_root = Path(__file__).resolve().parents[2]
    driver = kernel_root / "tools" / "replay_lrsc_theta07.py"
    recheck = kernel_root / "tools" / "verify_lrsc_replay.py"
    if not driver.is_file() or _sha256_path(driver) != _V03_REPLAY_DRIVER_SHA256:
        return False, "trusted replay driver hash mismatch"
    if not recheck.is_file() or _sha256_path(recheck) != _V03_RECHECK_DRIVER_SHA256:
        return False, "trusted independent recheck driver hash mismatch"
    key = _sha256_path(path) + ":" + _V03_REPLAY_DRIVER_SHA256
    if key in _V03_REPLAY_CACHE:
        return _V03_REPLAY_CACHE[key]
    try:
        stored = json.loads(path.read_text(encoding="utf-8"))
        static_ok, static_detail = verify_lrsc_full_replay_manifest(path, spec)
        if not static_ok:
            result = (False, "stored replay manifest invalid before execution: " + static_detail)
            _V03_REPLAY_CACHE[key] = result
            return result
        with tempfile.TemporaryDirectory() as td:
            outdir = Path(td) / "replay"
            env = os.environ.copy()
            env["INTENTSEAL_VRK_REPLAY_OUT"] = str(outdir)
            proc = subprocess.run(
                [sys.executable, str(driver)], cwd=kernel_root, env=env,
                text=True, capture_output=True, timeout=int(spec.get("timeout_seconds", 60)),
            )
            if proc.returncode != 0:
                result = (False, f"fresh replay failed rc={proc.returncode}: {proc.stderr[-500:]}")
                _V03_REPLAY_CACHE[key] = result
                return result
            fresh_path = outdir / "full_replay_manifest.json"
            if not fresh_path.is_file():
                result = (False, "fresh replay did not produce manifest")
                _V03_REPLAY_CACHE[key] = result
                return result
            fresh = json.loads(fresh_path.read_text(encoding="utf-8"))
            if _normalized_replay_manifest(fresh) != _normalized_replay_manifest(stored):
                result = (False, "fresh full replay does not match stored deterministic certificate")
                _V03_REPLAY_CACHE[key] = result
                return result
            result = (True, "fresh isolated replay matched stored K0..K13 coverage and K14 interval witness")
            _V03_REPLAY_CACHE[key] = result
            return result
    except Exception as e:
        result = (False, f"executable replay exception: {e}")
        _V03_REPLAY_CACHE[key] = result
        return result


def verify_lrsc_execute_independent_recheck(path: Path, spec: dict) -> tuple[bool, str]:
    """Run the independent post-run checker on a temporary copy of the replay bundle."""
    import os
    import shutil
    import subprocess
    import sys
    import tempfile

    kernel_root = Path(__file__).resolve().parents[2]
    checker = kernel_root / "tools" / "verify_lrsc_replay.py"
    if not checker.is_file() or _sha256_path(checker) != _V03_RECHECK_DRIVER_SHA256:
        return False, "trusted independent recheck driver hash mismatch"
    static_ok, static_detail = verify_lrsc_independent_recheck(path, spec)
    if not static_ok:
        return False, "stored independent recheck invalid before execution: " + static_detail
    try:
        with tempfile.TemporaryDirectory() as td:
            temp_replay = Path(td) / "replay"
            shutil.copytree(path.parent, temp_replay)
            # Remove stored receipt so the trusted checker must regenerate it.
            generated = temp_replay / "independent_recheck.json"
            if generated.exists():
                generated.unlink()
            env = os.environ.copy()
            env["INTENTSEAL_VRK_REPLAY_OUT"] = str(temp_replay)
            proc = subprocess.run(
                [sys.executable, str(checker)], cwd=kernel_root, env=env,
                text=True, capture_output=True, timeout=int(spec.get("timeout_seconds", 30)),
            )
            if proc.returncode != 0 or not generated.is_file():
                return False, f"independent recheck execution failed rc={proc.returncode}: {proc.stderr[-500:]}"
            fresh = json.loads(generated.read_text(encoding="utf-8"))
            stored = json.loads(path.read_text(encoding="utf-8"))
            if fresh != stored:
                return False, "fresh independent recheck receipt differs from stored receipt"
            return True, "trusted independent checker regenerated an identical recheck receipt"
    except Exception as e:
        return False, f"independent recheck exception: {e}"


PLUGINS.update({
    "lrsc_execute_full_replay": verify_lrsc_execute_full_replay,
    "lrsc_execute_independent_recheck": verify_lrsc_execute_independent_recheck,
})

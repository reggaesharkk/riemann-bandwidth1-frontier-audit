# Shark Protocol v1.3.3 — Technical Audit, Defect Remediation, Lean-to-Python Correspondence, and Benchmark Report

**Author:** Prince Upadhyay (ORCID: `0009-0002-1170-4487`)  
**Date:** 26 October 2026  
**Baseline Release Preserved Untouched:** `v1.3.2` (`DOI: 10.5281/zenodo.23618032`, MIT / CC BY 4.0)  
**Candidate Status:** Private Engineering Candidate (`v1.3.3.dev0` -> `source_v1.3.3_hardened`) — Public Release Not Authorized Until Production Signing Ceremony & External Review  

---

## 1. Executive Summary & Scope

This report documents the continuation and adversarial hardening of the private **Shark Protocol `v1.3.3`** candidate, building directly on the published `v1.3.2` foundation (42 Lean 4 theorem declarations, VRK/Ed25519 hash-chained ledger, 4D soft-wall ODE governor, LRSC $11/99$ spectral projection, and multi-provider AI gateway) and the 26 October 2026 workspace update (`SHARK_PROTOCOL_V133_WORKSPACE_UPDATE_20261026.zip`, including `REPRO_CACHED_EVIDENCE.py` and `prior_security_results.zip`).

All original artifacts—including the published `v1.3.2` release, all 42 Lean 4 theorem declarations, the `source_v1.3.3_dev0` snapshot (`54/54` manifest entries), `prior_security_results.zip`, `REPRO_CACHED_EVIDENCE.py`, and the two separate 26 October 2026 `TEST-ONLY` live provider evidence records—are preserved byte-for-byte unchanged.

---

## 2. Resolved Implementation Weaknesses & Before/After Verification

### 2.1 Defect 1: Metadata-Keyed Evidence-Hash Cache Vulnerability (`REPRO_CACHED_EVIDENCE.py`)
- **Vulnerability Reproduced (`Before`):** The prior `source_v1.3.3_hardened` implementation cached on-disk evidence SHA-256 digests in `SharkProtocolEngine._EVIDENCE_STAT_CACHE` keyed by `(file_path, st_mtime_ns, st_size)`. A same-size modification (`b'AAAA'` -> `b'BBBB'`) followed by restoring the original modification timestamp via `os.utime(fixture, ns=(st.st_atime_ns, st.st_mtime_ns))` bypassed the cache check and caused `verify_exported_ledger(check_disk_evidence=True)` to falsely return `True` (`REPRODUCED_CACHE_BYPASS`).
- **Root-Cause Fix (`After`):** Removed all `(st_mtime_ns, st_size)` cache lookups and storage from `SharkProtocolEngine.verify_and_hash_evidence_list`. Whenever `check_disk=True`, the verifier unconditionally reads the live file bytes from disk (`f_path.read_bytes()`) and computes `hashlib.sha256(raw_bytes).hexdigest()`. `_EVIDENCE_STAT_CACHE` is retained solely as an unused empty dictionary so existing callers invoking `.clear()` do not raise `AttributeError`.
- **Exact Reproduction Output (`REPRO_CACHED_EVIDENCE.py`):**
  - **Before (`source_v1.3.3_hardened_prior`):**
    ```text
BEFORE_CHANGE_ACCEPTED True
AFTER_CHANGE_WITH_CACHE_ACCEPTED True
AFTER_CACHE_CLEAR_ACCEPTED False
REPRODUCED_CACHE_BYPASS
    ```
  - **After (`source_v1.3.3_hardened`):**
    ```text
BEFORE_CHANGE_ACCEPTED True
AFTER_CHANGE_WITH_CACHE_ACCEPTED False
AFTER_CACHE_CLEAR_ACCEPTED False
BEHAVIOR_DIFFERS_REVIEW_RESULTS
    ```
- **Regression Test:** `tests/test_v133_adversarial_hardening.py::test_17_same_size_timestamp_restored_evidence_tamper_rejected`.

### 2.2 Defect 2: Interrupted `.jsonl` Ledger Writes, Transactional State Update & Restart Recovery (`BF-2`)
- **Vulnerability Reproduced (`Before`):**
  1. In `source_v1.3.3_dev0` and `source_v1.3.3_hardened_prior`, `seal_claim` appended `sealed_entry` to `self.ledger` in memory *before* calling `self._append_entry_fsync(self.ledger_path, sealed_entry)`. When an `ENOSPC` / short-write fault occurred mid-append (`partial_append_fault` in `audit_tools/security_probes.py`), `self.ledger` retained the uncommitted entry in memory (`memory_ledger_entries: 1`) and the child signer advanced its tip while the on-disk `.jsonl` file contained a 743-byte truncated line.
  2. On restart, `SharkProtocolEngine.__init__` failed with `JSONDecodeError` / `ValueError` without distinguishing an interrupted trailing partial write at EOF from mid-file corruption or cryptographic tampering, leaving prior valid committed entries unrecoverable without manual file editing.
- **Root-Cause Fix (`After`):**
  1. **Transactional Commit & Child Signer Rollback:** `seal_claim` now executes `self._append_entry_fsync(self.ledger_path, sealed_entry)` *before* appending to `self.ledger`. Inside `_append_entry_fsync`, if an `OSError` occurs during `write`/`flush`/`fsync`, the file is truncated back to its pre-append byte offset (`orig_size`). If `_append_entry_fsync` raises any exception (including under fault-injected short writes), `self.ledger` is left untouched (`memory_ledger_entries: 0`) and `IsolatedSignerSubprocess.rollback_last_sign` restores the child signer's `(last_signed_digest, signed_count)` to its pre-sign state.
  2. **Interrupted Trailing Write Detection, Quarantine & Prefix Recovery (`_load_or_recover_disk_ledger`):** On startup, `SharkProtocolEngine` inspects raw `.jsonl` lines:
     - Any non-final malformed JSON line (`idx < len(raw_lines) - 1`), duplicate JSON object key, or any complete JSON record that fails full `verify_chain_list` verification (`expected_pubkey`, SHA-256 digest, Ed25519 signature, sequential index, `prev_hash`, and live disk evidence) raises `LedgerCorruptionError(ValueError)` fail-closed.
     - If the final line at EOF is an interrupted incomplete write (truncated JSON or missing trailing newline that fails verification) while all preceding lines $0 \dots k-1$ pass full cryptographic `verify_chain_list` verification:
       - With `recover_interrupted_writes=True` (default): the incomplete trailing bytes are quarantined to `<ledger_path>.quarantine` (with `fsync`), `<ledger_path>` is atomically rewritten to the $k$ verified committed prefix records (with `fsync`), `self.ledger` loads the $k$ valid entries, and `self.last_recovery_report` records `incomplete_write_detected=True`, `recovered=True`, `committed_entries_preserved=k`, and `quarantined_bytes`.
       - With `recover_interrupted_writes=False`: raises `InterruptedLedgerWriteError(ValueError)` without modifying `<ledger_path>`.
- **Regression Test:** `tests/test_v133_adversarial_hardening.py::test_18_interrupted_partial_jsonl_append_rollback_and_restart_recovery`.

### 2.3 Defect 3: Authenticated Non-Default Tenant `GET /health` Metadata Exposure (`BF-3`)
- **Vulnerability Reproduced (`Before`):** In `create_gateway_http_server` (`GatewayHTTPHandler.do_GET`), `GET /health` called `self._authenticate_request()` but ignored the returned `authed_tenant` and always queried `gw.engine` (the `"default"` tenant engine), exposing `"default"`'s `ledger_length`, `worker_epoch`, and `vrk_chain_status` to authenticated non-default tenants (`cross_tenant_health_metadata_exposure: True` in `security_probes.py`).
- **Root-Cause Fix (`After`):** `GET /health` now binds `norm_tenant = (authed_tenant or "default").strip() or "default"`, retrieves `target_eng = gw.get_tenant_engine(norm_tenant)`, acquires that tenant's execution lock `gw._tenant_exec_locks[norm_tenant]`, and returns `tenant_id`, `vrk_chain_status`, `ledger_length`, and `worker_epoch` exclusively for `target_eng`.
- **Before vs. After (`security_probes.py` `tenant_auth` probe):**
  - **Before:** `alpha_own_ledger_len: 1`, `default_engine_len: 3`, `health_visible_ledger_len: 3`, `health_is_default_engine: True`, `cross_tenant_health_metadata_exposure: True`.
  - **After:** `alpha_own_ledger_len: 1`, `default_engine_len: 3`, `health_visible_ledger_len: 1`, `health_is_default_engine: False`, `cross_tenant_health_metadata_exposure: False`.
- **Regression Test:** `tests/test_v133_adversarial_hardening.py::test_19_cross_tenant_health_endpoint_isolation`.

### 2.4 Defect 4: Per-Tenant Execution Lock Exception Safety on `begin_request()`
- **Vulnerability Reproduced (`Before`):** In `MultiProviderGateway.process_request`, `tenant_exec_lock.acquire()` was called before `slot = target_engine.epoch_guard.begin_request()`, while the `try ... finally: tenant_exec_lock.release()` block began *after* `begin_request()`. Any exception raised inside `begin_request()` stranded `tenant_exec_lock` in the locked state (`lock_stranded_before: True`), permanently deadlocking subsequent requests for that tenant.
- **Root-Cause Fix (`After`):** Initialized `slot = None` and moved `slot = target_engine.epoch_guard.begin_request()` inside the `try:` block protected by `finally: tenant_exec_lock.release()`, guarding `if slot is not None: target_engine.epoch_guard.finish_request(slot, abort=True)` in the `except BaseException:` handler (`lock_stranded_after: False`).
- **Regression Test:** `tests/test_v133_adversarial_hardening.py::test_20_begin_request_exception_releases_tenant_exec_lock`.

### 2.5 Defect 5: Signer Authorization, Replay Freshness, Strict JSON Parsing & Provenance Hardening (`BF-5`, `BF-6`)
- **Child Signer Structured Record Validation (`IsolatedSignerSubprocess`):** Added `record_body` validation on `SIGN` and `head_body` validation on `SIGN_HEAD` inside the child daemon, plus `require_structured_record: bool = False`. When `record_body` is supplied (which `SharkProtocolEngine.seal_claim` now always passes), or when `require_structured_record=True`, the child process independently recomputes `sha256_canonical(record_body)` and verifies `schema == "intentseal-vrk-claim-v2"`, `trust_root == VRK_TRUST_ROOT_DIGEST`, `signer_pubkey == child.public_key_hex`, `prev_hash == child.last_signed_digest`, and sequential `index == child.signed_count + 1` before signing.
  - *Explicit Architectural Boundary:* Even with structured record validation in the child process, because the parent gateway constructs claim fields and handles network I/O, a compromised parent process can still submit false semantic claims that conform to the `intentseal-vrk-claim-v2` schema. Thus, child-process signing proves key non-extraction, schema conformance, and forward hash-chain continuity—not independent semantic truth.
- **Replay Freshness Gates (`verify_exported_ledger` & `tools/verify_exported_ledger.py`):** Added `require_freshness_anchor: bool = False` (which rejects verification calls that omit both `min_issued_at` and `expected_head_hash`) and `max_issued_at: Optional[str] = None` (which rejects far-future `issued_at` or entry `timestamp_utc` timestamps exceeding `max_issued_at`).
- **Strict JSON Parsing (`strict_json_loads`):** Rejects duplicate JSON object keys (`{"tenant_id": "alpha", "tenant_id": "beta"}`) and non-finite constants (`NaN`, `Infinity`) across HTTP request parsing (`POST /v1/execute`), `.jsonl` ledger loading, and `tools/verify_exported_ledger.py`.
- **Regression Tests:** `tests/test_v133_adversarial_hardening.py` tests `21`, `22`, `23`, and `24`.

---

## 3. Exact Offline Test Suite & Probe Results (No Skipped Tests Counted as Executed Passes)

| Test Suite / Verification Probe | Discovered | Executed & Passed | Failed / Errors | Skipped | Skip / Environment Qualification |
|---|---:|---:|---:|---:|---|
| `source_v1.3.3_hardened` (`python -m unittest discover -s tests -p 'test_*.py'`) | 90 | 89 | 0 | 1 | 1 test (`test_owner_wrapper_python_and_detached_ledger_verifier_offline_end_to_end`) skipped on Linux because `pwsh` (PowerShell 7) is not installed; passed `66/66` on Windows 11 ARM64. |
| `tests/test_v133_adversarial_hardening.py` (standalone adversarial suite) | 24 | 24 | 0 | 0 | All 24 adversarial and regression tests executed and passed on Linux (`0` skipped). |
| `live_evidence_closure_v1_1` (`tests/test_live_evidence_closure.py`) | 4 | 3 | 0 | 1 | 1 test (`test_actual_powershell_wrapper_offline_boundary`) skipped on Linux because `pwsh` is not installed; passed `4/4` on Windows 11 ARM64. |
| `REPRO_CACHED_EVIDENCE.py` (against `source_v1.3.3_hardened`) | 1 | 1 | 0 | 0 | `BEFORE_CHANGE_ACCEPTED True`, `AFTER_CHANGE_WITH_CACHE_ACCEPTED False`, `AFTER_CACHE_CLEAR_ACCEPTED False`. |
| `audit_tools/security_probes.py` (against `source_v1.3.3_hardened`) | 7 | 7 | 0 | 0 | `concurrency`: `16/16` HTTP 200 (`0` HTTP 500); `cross_tenant_health_metadata_exposure`: `False`; `partial_append_fault`: `memory_ledger_entries: 0`, restart recovers cleanly (`recovered: True`). |
| `audit_tools/crypto_attack_vectors.py` (independent verifier vectors) | 12 | 12 | 0 | 0 | All 12 positive/negative cryptographic and freshness vectors verified. |
| `tools/check_lean_axioms.py --source-only` | 42 | 42 | 0 | 0 | Lexical/source census of all 42 Lean 4 theorem declarations passed (`0` forbidden tokens); fresh `lake build` remains blocked offline by toolchain/mathlib lock mismatch. |

---

## 4. Lean 4 Formal Declarations vs. Executable Python Runtime Correspondence

All 42 Lean 4 theorem declarations across `lean/BoundaryVerification.lean` (9 declarations), `lean/ExistenceVerification.lean` (17 declarations), and `lean/TypestateLifecycle.lean` (16 declarations), audited by `lean/AxiomsCheck.lean`, remain byte-for-byte unchanged from `v1.3.2`.

**Critical Epistemic Distinction:** The Lean 4 files prove properties of abstract mathematical definitions over $\mathbb{R}$, inductive finite-state types, and abstract finite sets. **No formal refinement proof or verified compiler connects the Lean 4 kernel to the executable Python 3 runtime.** The Python tests (`unittest` and differential trace checks) provide software regression evidence, not formal verification of Python execution.

| Lean 4 Module & Declarations | Formal Mathematical Statement Proven in Lean 4 | Executable Python Analogue (`shark_protocol/`) | Exact Verification Boundary & Unproven Gap |
|---|---|---|---|
| `lean/BoundaryVerification.lean` (`9` declarations: `face_1_gamma_zero` .. `nagumo_8face_positively_invariant_certificate`) | Pointwise algebraic sign inequalities ($\ge 0$ on lower faces, $\le 0$ / $< 0$ on upper faces) for the rational/real model vector field on the 8 boundary faces of compact box $B_4 = [0, \gamma_{\max}] \times [0, H_{\max}] \times [0, I_{\max}] \times [0, 1]$. | `SharkProtocolEngine.rhs_4d`, `step_ode`, `verify_nagumo_boundary_certificate` (`kernel.py`). | Lean proves algebraic face inequalities over $\mathbb{R}$; it does **not** prove IEEE-754 `float64` RK4 discretization accuracy, substepping stability, or absence of floating-point rounding drift. |
| `lean/ExistenceVerification.lean` (`17` declarations: `ExistenceState`, `waking_drive_floor`, `separatrix_clearance`, etc.) | Pointwise algebraic bounds, positive drive floors, and compact domain invariance properties under explicit parameter hypotheses over $\mathbb{R}$. | `SharkProtocolEngine.evaluate_basin_separatrix_guard`, `compute_i_max_4d` (`kernel.py`). | Python evaluates floating-point exponentials (`math.exp`) and thresholds; no formal theorem proves IEEE-754 evaluation preserves the real-field inequalities for arbitrary runtime inputs. |
| `lean/TypestateLifecycle.lean` — Lifecycle Automaton (`stepLifecycle`, `zeroed_freed_is_absorbing`, `poisoned_cannot_dereference`, `typestate_and_epoch_security_certificate`) | Inductive 6-state automaton (`UNINIT`, `PARTIAL_INIT`, `SEALED_ACTIVE`, `SHUTDOWN_CLEAN`, `ABORTED_POISONED`, `ZEROED_FREED`) over 5 events; proves `ZEROED_FREED` is absorbing and `ABORTED_POISONED` cannot transition to `SHUTDOWN_CLEAN`. | `RequestSlot.transition`, `step_total_automaton`, `atomic_lifecycle_scope` (`kernel.py`), differentially tested against `data/lean_transition_table.json` (`test_36`). | Differential testing confirms the Python state-transition table matches the JSON table across all $6 \times 5 = 30$ pairs and 200 random traces, but does not formally prove thread-scheduling or CPython memory reclamation. |
| `lean/TypestateLifecycle.lean` — Worker Epoch Guard (`stale_epoch_read_rejected`, `epoch_monotonic_increase`) | Abstract integer comparison lemma: if `slot_epoch != worker_epoch`, read access is rejected; incrementing epoch invalidates prior epoch IDs. | `WorkerEpochGuard.begin_request`, `read_slot`, `finish_request` (`kernel.py`) + per-tenant `tenant_exec_lock` (`gateway.py`). | The Lean lemma models a single integer comparison; safe multi-threaded HTTP request serialization relies on Python's `threading.RLock` (`tenant_exec_lock`) in `gateway.py`, tested empirically under 16-thread contention. |
| `lean/TypestateLifecycle.lean` — Patankar & Duhamel Bounds (`patankar_interval_rounding_in_box`, `duhamel_piecewise_contraction_bound`, `psi_decay_floor_bound`) | Algebraic positivity/upper-bound preservation for fractional production-destruction steps and linear recurrence inequalities over $\mathbb{R}$. | `step_ode_patankar_interval` (`float64`), `step_ode_patankar_mp_interval` (200-bit `mpmath.iv`), `evaluate_wp19_piecewise_duhamel_study` (`kernel.py`). | `mpmath.iv` provides outward-rounded interval arithmetic in Python; `evaluate_wp19_piecewise_duhamel_study` is an illustrative parameter study using assumed rates from `data/wp19_segments.json`, not a proof of 3D Navier-Stokes regularity. |
| `lean/TypestateLifecycle.lean` — Merkle-DAG Join & Projection (`merkle_dag_merge_commutative`, `merkle_dag_semilattice_laws`, `projection_independent_of_secret`, `perturbation_budget_scaling`) | Set-union commutativity, associativity, and idempotence (`Finset` / `Set`); projection `(a, b).1 = a` independence from `b`; linear scaling $L \cdot \delta$. | `SharkProtocolEngine.merge_divergent_ledgers`, `IsolatedSignerSubprocess`, `LRSCCompressor.compress` (`kernel.py`). | `projection_independent_of_secret` is a pure tuple-projection lemma, **not** an OS-level proof of subprocess memory/pipe isolation. `merkle_dag_semilattice_laws` proves set-union laws, whereas canonical JSON sorting and Ed25519 signature verification are tested in Python. |

**Lean Build Status (`BF-7`):** In offline environments without GitHub DNS access, running `lake build` fails because `lean-toolchain` specifies `leanprover/lean4:v4.36.0-rc1` while `lakefile.lean` requests `mathlib` `v4.15.0` and `lake-manifest.json` is flagged by Lake as out of date. Reconciling the Lean toolchain and Mathlib lock requires an online environment when preparing a future Lean rebuild; no Lean files or manifests were silently altered in this package.

---

## 5. Reconciled Benchmark Measurements (Exact JSON Alignment)

To eliminate any discrepancy between narrative prose and raw JSON artifacts, both offline benchmark datasets included in this workspace package are reported separately below with their exact JSON values. Neither benchmark contacts external cloud APIs or measures commercial third-party AI gateways; both measure local verification overhead against deliberately minimal pass-through baselines using deterministic in-process mock transports.

### 5.1 Benchmark A: 80-Request Sequential & 4-Tenant Concurrent Suite (`source_v1.3.3_hardened/CONVENTIONAL_VS_SHARK_BENCHMARK_RESULTS.json`)
Generated by `tools/benchmark_vs_conventional_gateway.py` using a `1.0 ms` deterministic mock HTTP transport (`DeterministicMockTransport(delay_sec=0.001)`) and live uncached disk-byte evidence hashing (`_EVIDENCE_STAT_CACHE` disabled):

| Configuration (`n = 80` sequential requests) | Mean (ms) | Stdev (ms) | Min (ms) | Median / p50 (ms) | p95 (ms) | p99 (ms) | Max (ms) | Sequential Throughput (req/s) | Peak Traced Heap (KiB) | Median Added Overhead vs. Baseline (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ConventionalPassThroughGateway` (minimal baseline) | 2.2915 | 0.3375 | 1.7607 | 2.1987 | 2.9694 | 3.4636 | 3.8159 | 434.64 | 206.38 | 0.0000 |
| `SharkProtocolGateway` (`Ed25519AuthoritySigner`, in-memory) | 42.2383 | 6.8249 | 34.5166 | 40.9430 | 55.3508 | 66.5050 | 70.6049 | 23.67 | 788.85 | +38.7443 |
| `SharkProtocolGateway` (`IsolatedSignerSubprocess`, IPC + structured check) | 41.7318 | 5.5227 | 35.1912 | 40.6145 | 52.3788 | 59.8452 | 69.8726 | 23.95 | 797.64 | +38.4158 |

- **8-Thread, 4-Tenant Concurrent Throughput (`80` requests total):**
  - Minimal Conventional Pass-Through Baseline: `1664.10 req/s`
  - Shark Protocol (`IsolatedSignerSubprocess` with per-tenant lock serialization): `109.50 req/s`
- **Post-Hoc 80-Entry Exported-Ledger Verification (`10` iterations, cache disabled):**
  - Full cryptographic + live disk-byte evidence SHA-256 verification (`check_disk_evidence=True`): mean `124.0710 ms`, p50 `122.6427 ms`, p95 `149.8175 ms`
  - Cryptographic hash-chain + Ed25519 signature verification only (`check_disk_evidence=False`): mean `66.0972 ms`, p50 `67.2908 ms`, p95 `79.4594 ms`

### 5.2 Benchmark B: Preserved 60-Pair Loopback HTTP Benchmark (`prior_security_results/results/benchmark_summary.json`)
Generated by `audit_tools/benchmark_compare.py` (`seed = 1337026`, `60` shuffled request pairs over local `ThreadingHTTPServer` loopback with `0.0 ms` in-process mock provider):

| Metric (`n = 60` paired HTTP loopback requests) | Minimal Pass-Through Handler (`baseline`) | Shark Protocol HTTP Gateway (`candidate`) | Paired Difference (`candidate - base`) |
|---|---:|---:|---:|
| Mean latency (ms) | 4.7395 | 41.8104 | +37.0709 (95% bootstrap CI: `33.8223`–`40.5757`) |
| Median (`median_ms`) | 1.6024 | 37.1947 | +34.7554 |
| p50 (`p50_ms`) | 1.6050 | 37.2774 | +34.8320 |
| p95 (`p95_ms`) | 23.8626 | 71.9501 | +61.0758 |
| Min / Max (ms) | 1.2086 / 25.9471 | 32.3816 / 89.1370 | 12.4066 / 87.9284 |
| Sequential Throughput (inverse mean, req/s) | 210.99 | 23.92 | — |

- **Trade-Off Interpretation:** Shark Protocol adds ~`38.74–38.42 ms` median per-request processing cost (primarily RK4 + Patankar ODE sub-stepping, LRSC spectral projection, live disk-evidence hashing, Ed25519 signing, and `os.fsync`) and reduces local mock throughput from `434.64 req/s` to `23.95 req/s`. In exchange, it provides tamper-evident SHA-256 hash-chaining, pinned Ed25519 signatures, signed head truncation detection, and isolated per-tenant state that a plain JSONL pass-through logger does not implement.

---

## 6. Established Guarantees, Remaining Limitations & Strongest Defensible Claims

### 6.1 What Is Established & Verified in `source_v1.3.3_hardened`
1. **Live Disk-Evidence Integrity Without Metadata-Cache Trust:** `verify_and_hash_evidence_list(check_disk=True)` reads and SHA-256 hashes the actual file bytes on disk on every call, defeating same-size timestamp-restored tampering (`REPRO_CACHED_EVIDENCE.py`).
2. **Transactional Ledger Append & Interrupted-Write Recovery:** Disk write failures roll back in-memory and child-signer state cleanly (`memory_ledger_entries: 0` on first-write failure), and startup recovery quarantines incomplete trailing EOF writes while preserving cryptographically verified prefix entries (`recover_interrupted_writes=True`) or failing closed (`recover_interrupted_writes=False`). Mid-file or cryptographic tampering always fails closed (`LedgerCorruptionError`).
3. **Per-Tenant Concurrency, Lock Safety & `/health` Isolation:** Concurrent requests on the same tenant serialize via `tenant_exec_lock` (`16/16` HTTP 200 in `security_probes.py`), exceptions inside `begin_request()` release `tenant_exec_lock` without deadlocking, and `GET /health` reports only the authenticated caller tenant's ledger length, worker epoch, and chain status (`cross_tenant_health_metadata_exposure: False`).
4. **Strict JSON & Provenance Validation:** Duplicate JSON keys and `NaN`/`Infinity` constants are rejected across HTTP payloads, `.jsonl` ledgers, and exported bundles; upstream provider `response_model` and `request_id` fields are validated against delimiter injection; and `IsolatedSignerSubprocess` validates canonical `record_body` and `head_body` structures in the child process.
5. **Scoped Three-Provider `TEST-ONLY` Live Evidence:** Across two separate persistent runs on 26 October 2026 (`20261026T144902610Z-28aa158902184f929e05cbb95de059b9` for Groq + Together, and `gemini-gateway-20261026T163340Z-b11a1a8e8a4c4ef491b126ce569267fd` for Gemini, with the initial Gemini timeout preserved as a failure record), three live HTTP 200 gateway executions were sealed and verified under an independently pinned `TEST-ONLY` Ed25519 public key (`f17e04254ca4a42fee79971559fb3b9dbe111e953c9c18b2e7b42be16dd08593`).

### 6.2 Remaining Architectural & Operational Limitations
1. **No Formal Refinement Proof Between Lean 4 and Python (`BF-8`):** The 42 Lean 4 theorems verify abstract mathematical and finite-state models; they do not formally verify the Python runtime, IEEE-754 floating-point solver, or OS process boundaries.
2. **Offline Lean Rebuild Gate (`BF-7`):** `lean-toolchain` (`v4.36.0-rc1`) and `lakefile.lean` / `lake-manifest.json` (`mathlib` `v4.15.0`) require an online `lake update` / lock reconciliation before a fresh offline `lake build` can execute without network access.
3. **Parent-Controlled Child Signer Boundary (`BF-6`):** While `IsolatedSignerSubprocess` keeps the Ed25519 private seed out of parent memory and validates `intentseal-vrk-claim-v2` schema/hash-chain continuity, a compromised parent process still controls prompt/response inputs and can request signatures for forward-linked records containing false semantic claims.
4. **Caller-Supplied Trust Pin & Freshness Anchors (`BF-5`):** Verification requires the caller to supply an out-of-band trusted public-key pin and, to prevent whole-bundle replay or future-timestamp assertions, to supply `min_issued_at`, `max_issued_at`, and/or `expected_head_hash` (`require_freshness_anchor=True`).
5. **No Built-In TLS on `ThreadingHTTPServer` (`BF-4`):** Remote binding (`allow_remote=True`) uses plain HTTP; any non-loopback deployment must sit behind a trusted TLS-terminating reverse proxy.
6. **Separate `TEST-ONLY` Runs vs. Production Signing Authority:** The two 26 October 2026 live runs remain separate ledgers signed with a `DEVELOPMENT_TEST_ONLY` key and do not constitute production signing authority or external security certification.

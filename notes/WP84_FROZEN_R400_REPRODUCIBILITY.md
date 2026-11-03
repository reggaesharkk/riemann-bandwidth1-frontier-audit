# WP84 frozen R400 theorem inventory — reproducibility

Base commit: `99712a495db3258f938f2509d1eaa37cbc966a03`  
Branch: `codex/wp84-frozen-theorem-inventory-20261103`

All commands below are read-only with respect to predecessor evidence. The new manifest generator writes only files named in its `ARTIFACTS` list under `evidence/`.

## Parent audit-chain hash replay

```powershell
python src/wp84_physical_kernel_manifest.py --verify
python src/wp84_r400_endpoint_near_product_manifest.py --verify
python src/wp84_r400_physical_endpoint_averaging_manifest.py --verify
python src/wp84_r400_cumulant_endpoint_tensor_manifest.py --verify
python src/wp84_r400_theorem_feasibility_manifest.py --verify
python src/wp84_r400_endpoint_restricted_attack_manifest.py --verify
python src/wp84_frozen_r400_theorem_inventory_manifest.py --verify
```

The earlier Schatten manifest has a hard-coded branch-name guard for its original branch. Do not edit that historical script or switch away from the frozen branch just to satisfy its guard. The new verifier independently replays its manifest sidecar and every artifact hash, checks its stored base/source inventory, and records that the original branch guard is the only reason the legacy command is not valid on this branch.

## Mathematical regression and certificate replay

Core exact suites, in each Python mode:

```powershell
python -m unittest tests.test_wp84_physical_kernel_reconciliation tests.test_wp84_r400_schatten_absorption_audit tests.test_wp84_r400_cumulant_endpoint_tensor -v
python -O -m unittest tests.test_wp84_physical_kernel_reconciliation tests.test_wp84_r400_schatten_absorption_audit tests.test_wp84_r400_cumulant_endpoint_tensor -v
python -OO -m unittest tests.test_wp84_physical_kernel_reconciliation tests.test_wp84_r400_schatten_absorption_audit tests.test_wp84_r400_cumulant_endpoint_tensor -v
```

Additional scoped checks:

```powershell
python -m unittest tests.test_wp84_r400_physical_endpoint_averaging tests.test_wp84_r400_endpoint_near_product_audit tests.test_wp84_r400_theorem_feasibility tests.test_wp84_r400_endpoint_restricted_attack -v
python src/wp84_r400_pair_layer_exact.py
python src/wp84_r400_filtered_connected_kernel.py --certificate
python src/wp84_fixed_scale_connected_kernel.py
python src/wp84_cross_scale_sharp_detuning.py
python src/wp84_balanced_orientation_normalization.py
python src/wp84_phi4_equal_scale_brownian_kernel.py
```

The random reconnaissance mode is intentionally excluded. The interval certificate is run without optimization because its existing entry point deliberately fails closed when assertions are optimized away. Passing regressions verifies the finite calculations and stored evidence only; it is not evidence for the open asymptotic connected aggregate.

## Hashes and scope

`evidence/WP84_FROZEN_R400_SOURCE_HASHES.json` records raw SHA-256 hashes, base Git blob IDs, and line-ending-normalized immutability checks for the cited source/evidence inputs at the base. `evidence/WP84_FROZEN_R400_SHA256_MANIFEST.json` covers all new inventory files, checks and logs; its `.sha256` sidecar is computed over the manifest bytes. Run the generator without `--verify` to rerun the finite checks and rebuild the additive evidence. No original theorem claim or source hash inventory is rewritten.

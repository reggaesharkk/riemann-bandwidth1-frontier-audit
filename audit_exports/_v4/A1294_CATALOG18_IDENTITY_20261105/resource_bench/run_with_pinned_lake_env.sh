#!/usr/bin/env bash
set -euo pipefail
cd /home/reggaeshark/a1294_lean_formalization_20261104/formal-math/zeta23
AUDIT=/mnt/c/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit/audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105
BENCH="$AUDIT/resource_bench"
PREV="$AUDIT/reference/previous_objects"
export LEAN_PATH="$BENCH:$AUDIT:$PREV${LEAN_PATH:+:$LEAN_PATH}"
exec /home/reggaeshark/.elan/bin/elan run leanprover/lean4:v4.33.0-rc2 lake env bash "$BENCH/run_bench.sh" "$@"

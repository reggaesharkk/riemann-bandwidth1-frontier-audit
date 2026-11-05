#!/usr/bin/env bash
set -euo pipefail
MODE=${1:?mode required}
RUN=${2:-run1}
AUDIT=/mnt/c/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit/audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105
BENCH="$AUDIT/resource_bench"
PREV="$AUDIT/reference/previous_objects"
if [[ "$MODE" == mnt_c ]]; then
  ROOT="$BENCH"
  EXTRA="$AUDIT:$PREV"
elif [[ "$MODE" == ext4 ]]; then
  ROOT=/home/reggaeshark/a1294_catalog18_bench_20261105
  EXTRA="$AUDIT:$PREV"
else
  echo "unknown mode: $MODE" >&2; exit 2
fi
export LEAN_PATH="$ROOT:$EXTRA${LEAN_PATH:+:$LEAN_PATH}"
for TARGET in "${@:3}"; do
  LOG="$BENCH/${TARGET}_${MODE}_${RUN}.log"
  OUT="$ROOT/${TARGET}_${MODE}_${RUN}.olean"
  set +e
  /usr/bin/time -v timeout 150 lean -M6800 --root "$ROOT" "$ROOT/$TARGET.lean" -o "$OUT" >"$LOG" 2>&1
  STATUS=$?
  set -e
  cat "$LOG"
  echo "RECORDED_EXIT=$STATUS"
  [[ $STATUS -eq 0 ]] || exit "$STATUS"
done

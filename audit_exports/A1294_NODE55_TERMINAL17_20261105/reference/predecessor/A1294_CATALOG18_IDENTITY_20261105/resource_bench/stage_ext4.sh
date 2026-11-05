#!/usr/bin/env bash
set -euo pipefail
EXT=/home/reggaeshark/a1294_catalog18_bench_20261105
AUDIT=/mnt/c/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit/audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105
PREV="$AUDIT/reference/previous_objects"
if [[ -e "$EXT" ]]; then echo "EXT4_STAGE_EXISTS=$EXT" >&2; exit 3; fi
mkdir -p "$EXT"
cp "$AUDIT/resource_bench/ImportOnlyCatalog18.lean" "$EXT/"
cp "$AUDIT/resource_bench/Catalog18AllLookups.lean" "$EXT/"
cp "$AUDIT/Catalog18Identity.olean" "$EXT/"
cp "$PREV/Catalog18Lookup.olean" "$PREV/BoundaryBlocks.olean" "$EXT/"
{
  echo "EXT4_STAGE=$EXT"
  sha256sum "$EXT/ImportOnlyCatalog18.lean" "$EXT/Catalog18AllLookups.lean" "$EXT/Catalog18Identity.olean" "$EXT/Catalog18Lookup.olean" "$EXT/BoundaryBlocks.olean"
} | tee "$AUDIT/resource_bench/stage_ext4.log"

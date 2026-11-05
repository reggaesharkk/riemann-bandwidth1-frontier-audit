#!/bin/bash
set -eu
cd "$(dirname "$0")"
root="$PWD"
export LEAN_PATH="$root:$LEAN_PATH"
/usr/bin/time -v timeout 240 lean -M 6800 --root "$root/baseline" baseline/Zeta23/ThmD/Sextuple/CompositionalLeaf.lean -o Baseline.olean > baseline_build.log 2>&1
/usr/bin/time -v timeout 180 lean -M 6800 --root "$root" ImportAudit.lean > import_audit.log 2>&1
python3 resolve_closure.py import_audit.log standalone_closure.json > standalone_closure_summary.log
/usr/bin/time -v timeout 180 lean -M 6800 --root "$root" BaselineImportAudit.lean > baseline_import_audit.log 2>&1
python3 resolve_closure.py baseline_import_audit.log baseline_closure.json > baseline_closure_summary.log

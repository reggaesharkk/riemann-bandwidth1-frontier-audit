set -euo pipefail
target='/mnt/c/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit/audit_exports/a1294_lean_formalization_20261104/formal-math'
test ! -e "$target"
git init "$target"
git -C "$target" remote add origin https://github.com/anthropics/formal-math.git
git -C "$target" fetch --depth 1 --filter=blob:none origin fba91d214655aaa1fd0504bb893c8859c20c79f9
git -C "$target" sparse-checkout init --cone
git -C "$target" sparse-checkout set zeta23
git -C "$target" checkout --detach FETCH_HEAD
git -C "$target" rev-parse HEAD

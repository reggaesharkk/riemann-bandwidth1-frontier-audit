from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULES = [
    "Catalog15", "Catalog15Identity", "Catalog15BoundaryBlocks",
    "Catalog15AllLookups", "Terminal15Compositional", "Node51Replay",
]


def require(value: bool, msg: str) -> None:
    if not value:
        raise SystemExit(msg)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def time_seconds(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 1:
        return float(parts[0])
    if len(parts) == 2:
        return 60 * int(parts[0]) + float(parts[1])
    return 3600 * int(parts[0]) + 60 * int(parts[1]) + float(parts[2])


def field(text: str, pattern: str) -> str | None:
    m = re.search(pattern, text, re.M)
    return m.group(1).strip() if m else None


def main() -> None:
    rows = []
    for module in MODULES:
        lean = ROOT / f"{module}.lean"
        olean = ROOT / f"{module}.olean"
        build_log = ROOT / f"{module}.build.log"
        resource_log = ROOT / f"{module}.resource.log"
        log_parts = [p.read_text(encoding="utf-8", errors="replace")
                     for p in (build_log, resource_log) if p.is_file()]
        text = "\n".join(log_parts)
        require(lean.is_file() and olean.is_file(), f"missing source/object for {module}")
        wall = field(text, r"Elapsed .*?:\s*([0-9:]+\.[0-9]+)")
        rss = field(text, r"Maximum resident set size \(kbytes\): (\d+)")
        exit_status = field(text, r"Exit status: (\d+)")
        require(wall is not None and rss is not None and exit_status == "0",
                f"missing successful timed build record for {module}")
        rows.append({
            "module": module,
            "exit_status": int(exit_status),
            "wall_time_seconds": time_seconds(wall),
            "user_time_seconds": float(field(text, r"User time \(seconds\): ([0-9.]+)") or "nan"),
            "system_time_seconds": float(field(text, r"System time \(seconds\): ([0-9.]+)") or "nan"),
            "peak_rss_kib": int(rss),
            "major_page_faults": int(field(text, r"Major \(requiring I/O\) page faults: (\d+)")),
            "minor_page_faults": int(field(text, r"Minor \(reclaiming a frame\) page faults: (\d+)")),
            "swap_outs": int(field(text, r"Swaps: (\d+)")),
            "source_bytes": lean.stat().st_size,
            "source_sha256": sha(lean),
            "olean_bytes": olean.stat().st_size,
            "olean_sha256": sha(olean),
            "build_log": build_log.name,
            "resource_log": resource_log.name if resource_log.is_file() else build_log.name,
        })
    result = {
        "environment": {
            "lean": "4.33.0-rc2 (d8b18978322de05a8f3dba51ef03cf5461676c17)",
            "lake": "5.0.0-src+d8b1897",
            "build_memory_cap_mib": 6400,
            "sequential": True,
            "mathlib_rebuilt": False,
        },
        "modules": rows,
        "new_task_object_bytes": sum(r["olean_bytes"] for r in rows),
        "aggregate_wall_time_seconds": round(sum(r["wall_time_seconds"] for r in rows), 2),
        "maximum_peak_rss_kib": max(r["peak_rss_kib"] for r in rows),
        "note": "The recorded resident set includes the shared Lean/Mathlib import environment; this is not a full external dependency-object size measurement.",
    }
    (ROOT / "RESOURCE_BENCHMARK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("new_task_object_bytes", "aggregate_wall_time_seconds", "maximum_peak_rss_kib")}, sort_keys=True))


if __name__ == "__main__":
    main()

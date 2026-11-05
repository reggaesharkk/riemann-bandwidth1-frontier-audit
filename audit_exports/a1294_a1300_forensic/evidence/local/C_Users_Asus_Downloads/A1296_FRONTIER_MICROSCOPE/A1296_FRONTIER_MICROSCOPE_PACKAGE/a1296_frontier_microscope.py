from __future__ import annotations
import json, math, os, sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

def q(x):
    return x if isinstance(x, F) else F(str(x))

def f(x):
    return float(x)

def mean(xs):
    return sum(xs)/len(xs) if xs else 0.0

def load():
    base = Path(sys.argv[1])
    sys.path.insert(0, str(base))
    from a1294_seam_pilot import Checker, PARTIALS, model_min

    result_path = base/"results"/"A1296_FULLROOT_5M_DIAGNOSTIC_RESULT.json"
    if not result_path.exists():
        raise SystemExit(f"Missing {result_path}")

    raw = json.loads(result_path.read_text())
    A, B = q(raw["A"]), q(raw["B"])
    checker = Checker(
        base/"data"/"macro-data-exact.json",
        base/"data"/"refinement-catalog-v1-exact.json",
        base/"data"/"refinement-catalog-v3.json",
        A, B
    )
    return base, raw, checker, PARTIALS, model_min

def center(box):
    return [(q(lo)+q(hi))/2 for lo,hi in box]

def classify_box(checker, PARTIALS, model_min, item):
    box=[(q(lo),q(hi)) for lo,hi in item["box"]]
    c=center(item["box"])
    partials=[]
    seam_count=0
    direct_count=0
    piece_ids=[]
    owners=[]
    for k,(li,ri) in enumerate(PARTIALS):
        lo=sum((box[j][0] for j in range(li,ri+1)),F(0))
        hi=sum((box[j][1] for j in range(li,ri+1)),F(0))
        chi=min(hi,checker.cutoff)
        piece=checker.containing_best(lo,chi) if lo<=chi else None
        mode="scalar"
        idx=None
        owner=None
        stable_min=None
        scalar_min=None

        if piece is not None:
            idx=piece.idx
            owner=piece.owner
            stable_min=model_min(piece,lo,chi)
            if piece.idx < 56 and checker.groups.get(piece.owner):
                scalar_min=checker.scalar_min(lo,hi)
                if scalar_min > stable_min:
                    mode="seam_scalar"
                    seam_count += 1
                else:
                    mode="direct"
                    direct_count += 1
                    piece_ids.append(idx); owners.append(owner)
            else:
                mode="direct"
                direct_count += 1
                piece_ids.append(idx); owners.append(owner)
        else:
            scalar_min=checker.scalar_min(lo,hi)
            mode="seam_scalar"
            seam_count += 1

        partials.append({
            "partial_index":k,
            "interval":[li,ri],
            "sum_lo":str(lo),
            "sum_hi":str(hi),
            "mode":mode,
            "piece_idx":idx,
            "owner":owner,
            "direct_model_min":None if stable_min is None else str(stable_min),
            "scalar_min":None if scalar_min is None else str(scalar_min),
        })

    return {
        "depth":item["depth"],
        "center":[str(x) for x in c],
        "center_float":[float(x) for x in c],
        "seam_count":seam_count,
        "direct_count":direct_count,
        "piece_ids":piece_ids,
        "owners":owners,
        "partials":partials,
    }

def main():
    base, raw, checker, PARTIALS, model_min = load()
    boxes=raw["deepest_pending_boxes"]

    analyzed=[classify_box(checker,PARTIALS,model_min,item) for item in boxes]

    # Two very clear geometric families in the uploaded frontier:
    # middle gap low (~6.5) vs high (~12.6).
    low=[x for x in analyzed if x["center_float"][2] < 9]
    high=[x for x in analyzed if x["center_float"][2] >= 9]

    def summarize(group,name):
        piece_counter=Counter()
        owner_counter=Counter()
        seam_partial_counter=Counter()
        direct_partial_counter=Counter()
        depths=[]
        centers=[]
        seam_counts=[]
        for x in group:
            piece_counter.update(x["piece_ids"])
            owner_counter.update(x["owners"])
            depths.append(x["depth"])
            centers.append(x["center_float"])
            seam_counts.append(x["seam_count"])
            for p in x["partials"]:
                if p["mode"]=="seam_scalar":
                    seam_partial_counter[p["partial_index"]]+=1
                else:
                    direct_partial_counter[p["partial_index"]]+=1
        ctr=[mean([c[i] for c in centers]) for i in range(5)] if centers else []
        return {
            "name":name,
            "count":len(group),
            "depth_min":min(depths) if depths else None,
            "depth_max":max(depths) if depths else None,
            "depth_mean":mean(depths),
            "center_mean":ctr,
            "seam_count_mean":mean(seam_counts),
            "top_piece_indices":piece_counter.most_common(30),
            "top_owner_indices":owner_counter.most_common(30),
            "seam_by_partial_index":sorted(seam_partial_counter.items()),
            "direct_by_partial_index":sorted(direct_partial_counter.items()),
        }

    summaries=[
        summarize(low,"LOW_MIDDLE_GAP"),
        summarize(high,"HIGH_MIDDLE_GAP"),
    ]

    # Global diagnostic: which partial sums most often force seam-scalar fallback?
    global_seam=Counter()
    global_piece=Counter()
    for x in analyzed:
        global_piece.update(x["piece_ids"])
        for p in x["partials"]:
            if p["mode"]=="seam_scalar":
                global_seam[p["partial_index"]]+=1

    # Compare to frozen exact catalog witness from prior research state.
    witness=[
        F(6912667,1048576),
        F(6541989,524288),
        F(860015,131072),
        F(13083885,1048576),
        F(6912651,1048576),
    ]
    wfloat=[float(x) for x in witness]
    distances=[]
    for i,x in enumerate(analyzed):
        c=x["center_float"]
        d=math.sqrt(sum((c[j]-wfloat[j])**2 for j in range(5)))
        distances.append((d,i))
    distances.sort()

    out={
        "schema":"a1296-frontier-microscope-v1",
        "source_result":str(base/"results"/"A1296_FULLROOT_5M_DIAGNOSTIC_RESULT.json"),
        "source_pending_total":raw["pending"],
        "analyzed_deepest_box_count":len(boxes),
        "note":"The source file stores only the deepest 200 of 1024 pending boxes, so this is a structural microscope, not a complete frontier reconstruction.",
        "families":summaries,
        "global_top_piece_indices":global_piece.most_common(40),
        "global_seam_by_partial_index":sorted(global_seam.items()),
        "witness_point":[str(x) for x in witness],
        "nearest_boxes_to_witness":[
            {"distance":d,"index":i,"depth":analyzed[i]["depth"],"center":analyzed[i]["center_float"],
             "seam_count":analyzed[i]["seam_count"]}
            for d,i in distances[:25]
        ],
        "analyzed_boxes":analyzed,
    }

    outpath=base/"results"/"A1296_FRONTIER_MICROSCOPE_RESULT.json"
    outpath.write_text(json.dumps(out,indent=2),encoding="utf-8")

    summary=base/"results"/"A1296_FRONTIER_MICROSCOPE_SUMMARY.txt"
    lines=[
        "A1296 frontier microscope",
        f"Pending total in 5M run: {raw['pending']}",
        f"Deepest boxes analyzed: {len(boxes)}",
        "",
    ]
    for s in summaries:
        lines += [
            f"{s['name']}: count={s['count']} depth={s['depth_min']}..{s['depth_max']} mean_depth={s['depth_mean']:.2f}",
            "  center mean: " + ", ".join(f"{x:.6f}" for x in s["center_mean"]),
            f"  mean seam-scalar partials per box: {s['seam_count_mean']:.2f}",
            "  top piece indices: " + ", ".join(f"{i}:{n}" for i,n in s["top_piece_indices"][:12]),
            "  seam partial indices: " + ", ".join(f"{i}:{n}" for i,n in s["seam_by_partial_index"]),
            "",
        ]
    lines += [
        "Global seam partial indices:",
        ", ".join(f"{i}:{n}" for i,n in sorted(global_seam.items())),
        "",
        "Nearest box center to exact frozen-catalog witness:",
        json.dumps(out["nearest_boxes_to_witness"][0],indent=2),
        "",
        "Send A1296_FRONTIER_MICROSCOPE_RESULT.json to ChatGPT / sync results folder to Drive."
    ]
    summary.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))

if __name__=="__main__":
    main()

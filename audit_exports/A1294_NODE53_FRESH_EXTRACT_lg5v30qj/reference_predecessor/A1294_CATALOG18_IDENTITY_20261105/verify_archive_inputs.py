from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "reference/input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip": ("3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5", 5672384),
    "reference/checkpoints/A1294_VRK_INTENTSEAL_BRIDGE_CHECKPOINT_20261105.zip": ("efd9bb37ad16d5c843df454921f7145115e9dc39e08d347b55c79e3e860dff4f", 415555),
    "reference/checkpoints/A1294_NODE57_AUTHENTIC_TERMINAL18_INCOMPLETE_20261105.zip": ("ec9eca5910487d096edbfc142ee781762e8c4a16bc1db21c399886b55e35d13c", 188281),
    "reference/checkpoints/A1294_NODE59_TERMINAL19_SOURCE_CONNECTED_20261105.zip": ("1c7af665c1c70ddd46bfe966c963658846bee212163f70cc531d044d111f1b24", 4291776),
    "reference/releases/IntentSeal_Verifiable_Research_Kernel_v0_3_1.zip": ("c18c4c697d8188490e96530cfb5ddcb2e63f7c65aa560415401b1541e575cd79", 177783),
    "reference/lineage/IntentSeal_lineage_final_published.zip": ("05ba923c90dfc481a70a3784b72d1cd71a0adeac2c34a22631169f545ae5d4c0", 161324),
    "reference/lineage/IntentSeal_lineage_historical_inventory.zip": ("14f920b5fcb970f8a97eaf98aa80c83e8ff4125bb85e311705f86edad5dd56db", 148371),
}
for rel, (expected_hash, expected_size) in EXPECTED.items():
    path = ROOT / rel
    data = path.read_bytes()
    if len(data) != expected_size:
        raise RuntimeError(f"size mismatch: {rel}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected_hash:
        raise RuntimeError(f"SHA-256 mismatch: {rel}")
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
    if bad is not None:
        raise RuntimeError(f"ZIP CRC mismatch in {rel}: {bad}")
    print(f"PASS {rel} bytes={len(data)} sha256={digest} CRC=OK")

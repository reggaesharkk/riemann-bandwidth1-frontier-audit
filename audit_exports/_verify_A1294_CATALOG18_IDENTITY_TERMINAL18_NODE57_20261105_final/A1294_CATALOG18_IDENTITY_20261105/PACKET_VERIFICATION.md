# Packet verification

`SHA256SUMS.txt` covers all regular packet files other than itself. `source_hash_inventory.json` independently inventories the checkpoint's sources, proof objects, logs, archives, and evidence files. The ZIP's CRC is checked separately.

After extraction into a new empty directory, run:

```powershell
python verify_extracted_packet.py .
```

This recomputes the manifest and inventory hashes and reruns the catalog, exact terminal-18 provenance, and VRK claim-record checks under normal Python, `-O`, and `-OO`.

The independent extraction replay result is recorded in `PACKET_VERIFICATION_RESULTS.txt`. The final ZIP hash is reported outside the archive because embedding a ZIP's own SHA-256 in itself would be self-referential.

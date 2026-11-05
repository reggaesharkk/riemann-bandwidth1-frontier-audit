# Pinned source snapshot check

The 16 upstream files included in the packet were compared by SHA-256 with the isolated WSL checkout used for the successful build. The checkout reported commit `fba91d214655aaa1fd0504bb893c8859c20c79f9`; all 16 hashes matched. The exact read-only command output is preserved in `upstream_checkout_hashes.txt`, and the same file hashes are listed in `source_hash_inventory.json` after packet assembly.

The compared files are the Lean toolchain file, Lake project and dependency lockfiles, the sextuple energy/interval/kernel/certificate modules, the stable catalog, and both refinement catalogs. This check does not hash all files in the large upstream repository; it covers the included source files relevant to this leaf module and catalog comparison.

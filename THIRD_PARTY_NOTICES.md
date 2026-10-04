# Third-party notices

This repository is a mixed-provenance research repository. The root
all-rights-reserved notice applies only to original copyrightable material for
which Prince Upadhyay holds the relevant rights. It does not override any
third-party license.

## Anthropic formal-math / Zeta23 material

Pinned upstream used by the A1294 audit:

- repository: `anthropics/formal-math`
- pinned commit:
  `fba91d214655aaa1fd0504bb893c8859c20c79f9`

Relevant upstream Lean files contain notices of the form:

> Copyright (c) 2026 Anthropic, PBC. All rights reserved.  
> Released under Apache 2.0 license as described in the file LICENSE.  
> SPDX-License-Identifier: Apache-2.0

Any copied/vendored upstream source, generated catalog data derived from that
source, or other third-party material remains under its applicable upstream
license and copyright terms. The root restrictive notice does not relicense
those files.

The repository's provenance and audit notes identify the exact pinned upstream
objects and hashes used by the A1294 certificate.

## External papers, formulas, and public facts

References to published papers, theorem statements, numerical constants,
public facts, or mathematical ideas do not imply ownership of those items.

## Distribution rule for releases

Every GitHub/Zenodo release must preserve:

1. this `THIRD_PARTY_NOTICES.md`;
2. upstream copyright/SPDX notices in copied files;
3. the original upstream license text when redistribution requires it;
4. provenance identifying third-party source material.

Do not label third-party Apache-2.0 material itself as proprietary or
all-rights-reserved.

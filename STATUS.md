# Release status

**Current status: PUBLICATION CANDIDATE / NOT YET v1.0**

## Completed publication-candidate checks

- [x] Seven recoverable valid outputs are present as raw + normalized pairs.
- [x] All seven normalized JSON files pass `Canonical_Evaluation_Output_Schema_v0.2.json`.
- [x] The analysis script reproduces the reported test–retest summaries: 11/16 exact ordinal agreement (68.75%), 16/16 within ±1 point (100%), and a mean absolute scientific-recognition probability difference of 0.0775 (7.75 percentage points).
- [x] All 11 prepared run prompts are present: 7 primary and 4 retest.
- [x] `SHA256SUMS.txt` has been recomputed for the 47 files in the publication candidate, and the local integrity check passes 47/47.
- [x] No publisher PDF, CED PDF, or third-party supplementary scientific file is included in the public repository.

## Remaining before v1.0

1. Recover and add the four valid primary raw outputs not yet repackaged:
   - `SP-VF058-P1`
   - `SP-VF064-P1`
   - `SP-VF068-P1`
   - `SP-VF073-P1`
2. Add their normalized counterparts, update the provenance/normalization manifests as needed, re-run schema validation, and recompute `SHA256SUMS.txt`.
3. Tag the complete package `v1.0-technical-pilot`.
4. Archive that GitHub release in Zenodo and add the DOI to `CITATION.cff` and `README.md`.

No missing model output should be regenerated or reconstructed and presented as an original raw artifact.

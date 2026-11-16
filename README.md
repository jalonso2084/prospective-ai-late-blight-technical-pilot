# Prospective AI Evaluation of Potato Late Blight Research — Technical Pilot

This repository is the public reproducibility package supporting the LinkedIn article **“Can AI Recognize Important Research in Real Time? Lessons from a Technical Pilot in Potato Late Blight.”**

## What this repository represents

The materials document **Step 3: Technical AI Evaluation Pilot** in a larger prospective research project asking whether a frontier AI model can anticipate which newly public potato late blight research contributions will later receive substantive scientific recognition.

The pilot tested the measurement machinery. It did **not** test prospective predictive validity. All pilot outputs are labeled:

- `TECHNICAL_PILOT_ONLY`
- `NOT_A_PROSPECTIVE_VALIDATION_RECORD`

Seven Version Families were evaluated once, and four preselected cases were independently retested, giving 11 valid reported runs. Present-paper assessments used a 1–4 ordinal scale for scientific quality, methodological rigor, strength of evidence, and perceived novelty.

## Main pilot findings reported in the article

For the four test–retest cases, 11/16 ordinal scores were identical (68.75%) and all 16/16 were within ±1 point. The absolute differences in 36-month scientific-recognition probabilities were 0.10, 0.03, 0.03, and 0.15, for a mean absolute difference of 0.0775 (7.75 percentage points).

Run `python analysis/reproduce_summary.py` to reproduce these arithmetic summaries from the reported-results table.

## Repository map

- `ARTICLE.md` — LinkedIn article draft supported by this package.
- `protocol/` — Step 3 execution protocol, frozen rubric, and Amendments AM-01 to AM-03.
- `schema/` — canonical structured-output schema used in the technical pilot.
- `prompts/` — preserved primary/retest prompt templates or prepared prompts.
- `outputs/raw/` — raw output files that are currently recoverable.
- `outputs/normalized/` — minimally normalized JSON counterparts; raw files are never overwritten.
- `outputs/NORMALIZATION_LOG.csv` — every normalization applied.
- `data/pilot_results_reported.csv` — compact table of the 11 valid reported runs, with provenance flags.
- `data/test_retest_pairs.csv` — paired ordinal scores for the four preselected retests.
- `data/invalid_runs_log.csv` — known excluded/interrupted attempts and their disposition.
- `analysis/reproduce_summary.py` — reproduces the 68.8% and 7.8-percentage-point summaries.

## Important completeness note

This is a **pre-release publication candidate**, not yet the final archival v1.0. Seven of the eleven valid model outputs are present here as recoverable raw files. Four valid primary outputs (`SP-VF058-P1`, `SP-VF064-P1`, `SP-VF068-P1`, `SP-VF073-P1`) were supplied and validated during the project but are not currently available as standalone raw source files in the accessible project store. Their reported values are retained in the results table and marked accordingly. See `outputs/MISSING_RAW_OUTPUTS.md`.

No missing output has been regenerated or reconstructed and presented as a raw artifact.

## Evidence files and copyright

The original scientific papers, publisher PDFs, and Controlled Evaluation Documents (CEDs) are **not redistributed here**. The public package contains prompts, manifests, hashes, methodological documents, and model outputs. This avoids redistributing third-party scientific content unless a license is separately verified.

## Model and execution environment

The valid pilot condition used OpenAI **GPT-5.6 Sol**, High reasoning, through ChatGPT Work after AM-02. Web browsing and external tools were not intentionally invoked during the scientific evaluations. The exact backend model snapshot was not exposed by the UI. The Work environment cannot provide the same independently verifiable isolation guarantees as an API-level container; that limitation is part of the study record.

## Prospective phase

The prospective phase is not represented by these pilot forecasts. Before prospective activation, the project still needs to freeze (1) outcome adjudication procedures, including protection from forecast-aware judgment, and (2) an external timestamp/deposit mechanism establishing that each prospective forecast existed before downstream outcomes.

## Citation

See `CITATION.cff`. A DOI should be added after the first complete public release is archived in Zenodo.

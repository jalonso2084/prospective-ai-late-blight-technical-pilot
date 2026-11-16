# Protocol Amendment AM-01 — Single-Provider Technical Pilot

**Project:** Prospective AI Evaluation of Potato Late Blight Research  
**Step:** Step 3 — Technical AI Evaluation Pilot  
**Amendment ID:** AM-01  
**Version:** 1.0  
**Date:** 2026-09-30  
**Human decision:** APPROVED — single-provider execution path  
**Evaluation Set:** n=7 (VF038, VF051, VF058, VF064, VF068, VF073, VF084)

## 1. Reason for amendment

The original Step 3 design included independent execution across multiple frontier-model providers in order to characterize provider/model procedural comparability. Pre-execution work established that the scientific-document pipeline, controlled evaluation documents (CEDs), supplemental-material handling, hashing, archival, schema, validator, and single-model execution logic are operationally ready. However, completing the originally planned multi-provider API panel would require continued API provisioning, billing, credential management, and provider-specific operational work that the investigator does not wish to undertake.

This amendment narrows Step 3 from a multi-provider technical pilot to a **single-provider / single-model technical pilot executed through the ChatGPT user interface without API use**.

This is an explicit scope reduction, not a silent substitution.

## 2. What remains unchanged

The following frozen elements remain unchanged:

- prospective-project rationale and Step 2 Information Boundary;
- `TECHNICAL_PILOT_ONLY` and `NOT_A_PROSPECTIVE_VALIDATION_RECORD` labels;
- Pilot Evaluation Set n=7;
- CED binaries and hashes;
- supplemental scientific evidence included in the frozen evaluation packages;
- AI Scientific Evaluation Rubric — Pilot v0.2;
- Canonical Evaluation Output Schema v0.2;
- deterministic semantic validation rules;
- retry logic in principle (technical failure only, never because an answer is surprising);
- raw-response preservation;
- UTC timestamping;
- immutable/frozen evaluation records;
- within-model test–retest requirement;
- prohibition on claims of predictive validity, accuracy, or prospective success from Step 3.

## 3. What changes

### 3.1 Model panel
The multi-provider panel is replaced by one execution condition:

**Provider:** OpenAI / ChatGPT  
**Execution surface:** ChatGPT user interface, not API  
**Model family:** GPT-5.6 Sol, when that model label is available to the investigator at execution time  
**Tools/web:** disabled / not used  
**Conversation context:** fresh isolated temporary or non-project chat with no prior project discussion supplied  
**Memory/project context:** must not be intentionally supplied; use Temporary Chat where available, or a fresh non-project chat with Memory disabled  
**Evidence supplied:** only the frozen CED and any frozen supplemental files assigned to that Version Family, plus frozen instructions  
**Output language:** English  
**Output target:** canonical structured JSON-compatible response

The exact visible model label, date/time, interface surface, and any visible model-mode setting must be recorded for every run.

Because the ChatGPT UI does not expose a provider API snapshot identifier or guarantee a fixed backend revision, `exact_backend_snapshot` is recorded as:

`NOT_EXPOSED_BY_UI`

This is a documented limitation.

### 3.2 Cross-provider objectives
The following original objective is removed from Step 3 execution and deferred:

- model-to-model / provider-to-provider procedural comparability.

The pilot will not estimate or describe cross-provider agreement, disagreement, ranking, relative stability, or relative scientific judgment.

### 3.3 Input-delivery comparability
The original cross-provider input-delivery comparison is replaced by:

> Characterize the single ChatGPT UI evidence-delivery condition sufficiently to reconstruct what scientific files and instructions were supplied in each run.

### 3.4 Test–retest
Within-model test–retest remains required.

- Select approximately 4 varied Version Families from the n=7 Evaluation Set.
- Execute a second independent run for each selected case in a new isolated chat.
- Use the exact same frozen evidence package and instructions.
- Treat repeat runs as technical repeatability observations, not ensembles and not opportunities to choose a preferred answer.

## 4. Scientific meaning and comparability impact

**Scientific meaning of each individual model forecast:** unchanged in intended construct.

**Cross-provider comparability:** removed from Step 3.

**Within-model comparability:** retained, subject to the documented limitation that the UI may not expose exact backend snapshots.

**Generalizability:** reduced. Results characterize one provider/model execution condition only.

**Future multi-provider comparison:** would require a separate extension or replication and must not be inferred from this pilot.

## 5. Claims explicitly prohibited after amendment

Step 3 must not claim:

- that multiple frontier models were compared;
- that findings generalize across providers;
- that OpenAI performs better or worse than another provider;
- that cross-model agreement or disagreement was assessed;
- that AI prospectively predicted scientific importance;
- that the pilot validates scientific judgment;
- that retrospective 2026 cases constitute prospective validation.

## 6. Highest permissible Step 3 exit state

Under AM-01, the pilot may not receive the unqualified exit state:

`TECHNICAL PILOT PASSED — READY FOR STEP 4`

The strongest permissible exit state is:

`TECHNICAL PILOT PASSED WITH REQUIRED REVISIONS — READY FOR STEP 4`

provided all amended technical exit criteria are met.

The required revision carried into Step 4 is that cross-provider procedural comparability remains untested.

## 7. Retesting requirement

No re-testing of CED fidelity is required solely because of this amendment.

Re-testing is required if:

- the frozen CED is changed;
- the rubric/schema changes materially;
- the single-provider execution surface changes in a way that changes evidence representation;
- a future multi-provider extension is added and claims of provider comparability are contemplated.

## 8. Human approval record

The investigator explicitly selected the single-provider alternative on 2026-09-30 after being informed that it weakens the original multi-provider design.

Status:

`AMENDMENT AM-01 APPROVED`

Model execution remains subject to the amended Human Pre-Execution Gate.

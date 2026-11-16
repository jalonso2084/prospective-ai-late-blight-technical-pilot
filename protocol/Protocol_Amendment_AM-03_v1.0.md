# PROTOCOL AMENDMENT AM-03
## Handling of Platform Safety Blocks During Step 3 Technical Pilot

**Project:** Prospective AI Evaluation of PLB Research  
**Step:** 3 — Technical Pilot  
**Amendment:** AM-03  
**Version:** 1.0  
**Date:** 2026-11-12  
**Status:** APPROVED

## 1. Purpose

AM-03 defines a pre-specified procedure for cases in which the ChatGPT platform does not return the requested evaluation because a safety system blocks or withholds the response.

The purpose is to prevent ad hoc prompt changes, repeated probing, or selective rerunning after observing a blocked result.

## 2. Definition of a platform safety block

A run is classified as `PLATFORM_SAFETY_BLOCK` when the interface displays a refusal, withheld-content notice, or equivalent safety message that prevents capture of the requested structured evaluation.

A safety block is an execution outcome of the platform, not a scientific judgment about the paper.

## 3. Invalid interactive runs

A run is invalid for the primary pilot dataset if, before the first complete structured evaluation is produced, the operator sends any additional clarification, instruction, reformulation, or follow-up message.

Such a run is retained only as troubleshooting evidence.

## 4. Permitted retry policy

For a paper blocked on the first attempt:

- exactly **one clean retry** is permitted;
- the retry must use a **fresh Work conversation**;
- the model must remain **GPT-5.6 Sol**;
- reasoning must remain **High** when available;
- the evidence files must be identical to the frozen `MODEL_EVIDENCE` set;
- the prompt content must be **identical in substance** to the frozen run prompt;
- no safety-oriented rewording, euphemism, omission, redaction, or prompt engineering is permitted;
- no additional user message may be sent before the first complete model response is captured.

A new timestamp and run-instance identifier may be generated for the retry, but the scientific instructions must not be altered.

## 5. Outcome after retry

If the clean retry returns a complete schema-compliant evaluation, that retry becomes the valid primary run.

If the clean retry is also blocked by the platform, the case is assigned:

- `TECHNICAL_PILOT_ONLY`
- `NOT_A_PROSPECTIVE_VALIDATION_RECORD`
- `PLATFORM_BLOCKED`
- `NOT_EVALUABLE_UNDER_CURRENT_UI_CONDITION`

No further attempts are permitted in Step 3 without a new protocol amendment.

## 6. Treatment of VF058 attempt 1

The first VF058 execution is classified as:

`SP-VF058-P1-ATTEMPT1 — INVALID: PLATFORM_SAFETY_BLOCK + INTERACTIVE_FOLLOWUP`

Reasons:
1. the model did not provide the requested structured evaluation;
2. the interface displayed a biological-research safety block;
3. an additional user message (“Ejecutar la evaluación”) was sent before a complete first response was obtained.

This attempt is excluded from the primary pilot dataset and retained only as execution-troubleshooting evidence.

## 7. Required evidence to preserve for blocked attempts

Preserve where feasible:

1. screenshot of the block;
2. model/mode shown in the interface;
3. exact input files used;
4. exact run prompt used;
5. run timestamp;
6. any intermediate assistant message preceding the block;
7. any operator follow-up message;
8. final classification of the attempt.

## 8. Interpretation

Platform safety blocks are treated as a technical limitation of the execution environment.

They must not be interpreted as:
- evidence of low paper quality;
- a scientific abstention;
- a forecast outcome;
- a model evaluation of risk;
- a substitute for the requested rubric output.

## 9. Approval

**AMENDMENT AM-03 APPROVED — PLATFORM SAFETY BLOCK HANDLING**

Approved in-project by the investigator on 2026-11-12.

# PROTOCOL AMENDMENT AM-02
## Work Execution Environment for GPT-5.6 Sol

**Project:** Prospective AI Evaluation of PLB Research  
**Step:** 3 — Technical Pilot  
**Amendment:** AM-02  
**Version:** 1.0  
**Date:** 2026-11-12  
**Status:** APPROVED

## 1. Reason for amendment

During Step 3 execution, the frozen AM-01 configuration required the use of GPT-5.6 Sol in a fresh Temporary Chat outside the project. In the current ChatGPT interface, GPT-5.6 Sol is available in Work mode but is not exposed when switching to Temporary Chat. Therefore, the originally frozen combination “Temporary Chat + GPT-5.6 Sol” is not operationally available in the current interface.

This amendment preserves the frozen primary model and reasoning condition while changing only the execution environment needed to access that model.

## 2. Change introduced

For all remaining primary and test–retest runs in Step 3:

- **Interface:** ChatGPT Work
- **Provider:** OpenAI
- **Model:** GPT-5.6 Sol
- **Reasoning effort:** High, when visible and selectable
- **Session condition:** fresh Work conversation for each run
- **Project attachment:** none
- **Plugins/apps:** none intentionally invoked
- **Web/browsing:** not intentionally invoked
- **External tools:** none intentionally invoked
- **Evidence delivery:** only the frozen CED and any frozen supplements listed for that Version Family
- **Prompt delivery:** paste the frozen `RUN_PROMPT_READY.txt` contents as text
- **No additional user context:** no extra explanation, follow-up, correction, or refinement before the first complete model response is captured

## 3. Isolation limitation

Work mode does not provide the same Temporary / Unpersonalized execution condition originally specified in AM-01. Therefore:

- absence of project context, plugins, web use, and additional files will be operator-controlled and documented;
- complete absence of memory/personalization influence cannot be independently verified from the UI;
- this limitation must be reported in the Step 3 technical pilot methods and limitations;
- no run under AM-02 is to be represented as equivalent to an API-isolated or Temporary-Unpersonalized execution.

## 4. What does NOT change

AM-02 does **not** alter:

- the seven-paper Evaluation Set;
- the frozen CED or supplement binaries;
- the rubric (`Pilot v0.2`);
- the canonical output schema (`v0.2`);
- the forecast constructs or scoring scales;
- the model provider;
- the primary model family (`GPT-5.6 Sol`);
- the planned test–retest cases;
- the technical-pilot-only status;
- the label `NOT_A_PROSPECTIVE_VALIDATION_RECORD`;
- post-run validation and archival requirements.

## 5. Treatment of VF051

The first VF051 attempt executed under GPT-6 is retained only as a documented invalid/troubleshooting run and is excluded from the primary pilot dataset.

The subsequent VF051 execution using:

- GPT-5.6 Sol,
- High reasoning,
- ChatGPT Work,
- browsing disabled,
- tool access reported as `NONE`,

is retained as the **primary VF051 evaluation record**, with the execution-environment limitation documented under AM-02.

Its evaluation identifier remains:

`SP-VF051-P1`

No further repetition of the primary VF051 run is required solely because Work mode replaced Temporary Chat.

## 6. Execution evidence to capture from VF058 onward

For each run, retain where feasible:

1. screenshot showing **GPT-5.6 Sol + High** before execution;
2. evidence that no project was selected;
3. raw first model response, unedited;
4. `RUN_PROMPT_READY.txt`;
5. operator timestamp / run metadata;
6. post-run validator result;
7. any visible deviation from the intended no-web/no-plugin/no-extra-tool condition.

## 7. Interpretation

AM-02 is an operational amendment made to preserve the frozen model identity when the current product interface no longer exposes the originally specified isolation mode together with that model.

It does not improve the evidentiary status of the pilot. All Step 3 outputs remain:

- `TECHNICAL_PILOT_ONLY`
- `NOT_A_PROSPECTIVE_VALIDATION_RECORD`

## 8. Approval

**AMENDMENT AM-02 APPROVED — WORK EXECUTION PATH FOR GPT-5.6 SOL**

Approved in-project by the investigator on 2026-11-12.

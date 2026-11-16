# Revised Model Execution Policy — Single-Provider UI Condition v1.0

**Applies under:** Protocol Amendment AM-01  
**Evaluation Set:** VF038, VF051, VF058, VF064, VF068, VF073, VF084

## Primary execution condition

Each primary evaluation must be performed in a **fresh isolated ChatGPT conversation outside the project conversation**.

Preferred isolation method:

1. Temporary Chat, if available; otherwise a fresh non-project chat.
2. Memory disabled for the run when possible.
3. No browsing, web search, connected apps, project files, prior chats, or external context.
4. Supply only the frozen execution instructions, the assigned frozen CED, and frozen supplementary files for that case, if any.
5. Do not mention authors, journal, DOI, publication date, later citation history, later uptake, or known outcomes.
6. Request the frozen canonical output format.
7. Preserve the first complete response as the raw response.
8. Do not ask the model to improve, reconsider, or change a surprising forecast.
9. Retry only for a documented technical failure.

## Required run metadata

Record:

- Evaluation ID
- Version Family ID
- CED filename and SHA-256
- supplement filenames and SHA-256, if applicable
- visible model label
- visible mode / reasoning setting, if shown
- execution surface: ChatGPT UI
- `exact_backend_snapshot = NOT_EXPOSED_BY_UI`
- UTC start and completion timestamps
- raw response filename
- parsed response filename
- validator result
- retry count and reason
- test–retest link, when applicable
- freeze status
- technical limitation flags

## Isolation limitation

The UI route cannot prove absence of all latent model knowledge from training. The model must be instructed not to use later/future information, and outputs must be audited for overt external/future-knowledge intrusion.

## Test–retest

Use four varied cases selected before viewing any primary output. Repeat each in a new isolated chat with the exact same frozen evidence package and instructions. Repeats are technical repeatability observations, not ensembles.

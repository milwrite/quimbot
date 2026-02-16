# Scoring (POC)

Rule-based scoring is the quickest path to a debuggable shortlist.

## Inputs

- comment velocity (preferred) + upvote velocity (optional)
- cross-subreddit echoes (same theme appearing in multiple subs)
- novelty (penalize repeats)
- feasibility (can it be explained in 20–40 seconds?)
- risk flags (penalize or require human approval)

## POC formula (suggested)

Normalize each component to 0–1, then:

`score = 0.45*v_comments + 0.15*v_upvotes + 0.15*echo + 0.15*feasible + 0.10*novelty - 0.25*risk`

Where:
- `risk` is 0 for safe, 1 for hard-block categories; or treat risk as a gate.

## Novelty store

Maintain a rolling window (e.g., last 7–14 days) of:
- `topic_id`
- title fingerprint

Then apply penalty if already used.

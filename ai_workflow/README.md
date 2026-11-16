# AI workflow: SPGI pitch (CNID Investment Challenge 2026)

> Outline for me to write in my own words. The notes under each heading are reminders; delete them when writing.

## What this is

- One paragraph: the pitch (BUY SPGI), the competition, and the role AI played (research, stress-testing, valuation checks). The recommendation and judgement are mine.

## Why structure an AI workflow at all

- Without structure, AI drifts: numbers change between chats, sources get mixed up, and criticism gets softened.
- The goal is AI as a sparring partner and research assistant, with a clear record of what it changed.

## Design choices

- **Context file (`context/CLAUDE.md`):** every session starts with the same rules: scorecard, data standards, GAAP vs adjusted, the CME minority stake.
- **Written philosophy (`../philosophy.md`):** stress tests check against my principles, not generic ones.
- **One source of truth per kind of content:** numbers only in the model, the argument only in the thesis, decisions only in the log.
- **Build and attack in separate sessions:** one stress test per session, so the AI doesn't defend its own work.
- **Verify against primary sources:** secondary coverage is treated as a lead, not a fact (see the errors table in `decision-log.md`).
- **Licensed material stays private:** the provided sell-side research and models shaped the framework but aren't reproduced here.

## The process

- Link to `context/workflow.md`: framework → Q3 refresh → thesis → stress tests → deck → Q&A.

## What the AI changed

- The 3–5 best entries from `decision-log.md` and `stress-tests/`, one sentence each.

## Where the AI was wrong

- The best examples from the errors table: what was claimed, what was true, how I caught it.

## What stayed human

- The recommendation, the philosophy, the final model numbers, what goes in front of judges.

## Lessons

- What I'd do differently; what worked better than expected.

## Folder map

| Path | What |
|---|---|
| `context/` | Files the AI loads: project rules and process (philosophy is at `../philosophy.md`) |
| `stress-tests/` | One file per stress test (`_template.md` to start) |
| `decision-log.md` | Every challenge, correction and outcome |

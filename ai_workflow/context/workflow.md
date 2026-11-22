# Workflow: SPGI pitch, from thesis to deck

Each kind of content has one home, so nothing gets lost in chat.

| What | File | Rule |
|---|---|---|
| Investment philosophy | `../../philosophy.md` | The lens. Each principle has an SPGI test and a KPI. |
| Sell-side framework | `framework.md` (private, not included) | A digest of the provided sell-side research and models (licensed, so not published): valuation methods, key debates, KPIs. Every point cites its file. |
| Q3 changes | `q3_update_checklist.md` | Work through it before rewriting prose. |
| Argument and story | `thesis.md` | One heading = one slide. |
| Decisions | `decision-log.md` | Every stress test and correction: what changed and why. |
| Numbers | `../../model/SPGI_Valuation_Model_v3.xlsx` | Thesis and deck quote the model. They never compute their own numbers. |
| Deck | `deck/` (later) | Built from `thesis.md` once the numbers are locked. |

## Stages

1. **Framework.** Read the provided sell-side research and models and write `framework.md`: how the sell side values SPGI, the main debates, and the KPIs they track.
2. **Q3 refresh.** Work through `q3_update_checklist.md`. Update the model first, then the thesis.
3. **Thesis draft.** Fill `thesis.md` section by section. Each section serves a scorecard criterion.
4. **Stress test.** Separate sessions, one attack each (prompts below). Write the outcome into the decision log.
5. **Deck.** Generate it from `thesis.md`, then edit visuals and wording by hand.
6. **Q&A prep.** Likely judge questions with short answers, practised out loud.
7. **Training Day.** Once the recordings are downloaded into `../Training_Day/`, transcribe them locally and add each speaker's guidance to `framework.md`.

## Stress-test prompts (one per session)

- "Read framework.md and thesis.md. Where do I disagree with the sell side, and is the disagreement justified?"
- "Bear case: Ratings issuance slows (Q3 grew +2%) while AI compresses Market Intelligence at the same time."
- "Recompute the 'AI-proof share of profit' from Q3 segment data, net of CME's 27% of Indices. Does the claim hold?"
- "The stock re-rated from $394 to ~$467. Under philosophy.md, is it still a BUY? What has to be true?"
- "Why SPGI over Moody's? Argue for Moody's as strongly as you can."
- "Act as a CNID judge using the scorecard. Ask the 10 hardest questions and grade my answers."
- "List every claim in thesis.md that isn't backed by a source file or the model."

# CLAUDE.md: CNID Investment Challenge 2026 (SPGI)

> This is the shareable version of the project context file the AI loads at the start of every session.
> Paths to licensed material have been generalized.

Pitch: **BUY S&P Global (NYSE: SPGI)**.
- Process: `workflow.md`
- Philosophy: `../../philosophy.md`
- Working thesis: `thesis.md`
- Decisions: `../decision-log.md`

## Scorecard (Round 1)

| Criterion | Points | Question |
|---|---|---|
| Business understanding | 20 | How does the business operate? |
| Industry | 15 | Where does it sit in its competitive landscape? |
| Quality | 15 | How durable is the business? |
| Financials | 15 | Is the pitch grounded in the numbers? |
| Thesis | 20 | What drives the recommendation? |
| Communication | 15 | Is it presented clearly? |

Every section of the thesis and every slide should earn points on one of these.

## Sources

- Company filings and releases: 10-K, 10-Q, quarterly releases, call slides (public).
- Peer filings: Moody's, MSCI, ICE, CME, FactSet (public).
- Provided sell-side research and models (licensed, private).
- My Round 1 written report and the valuation model.

## Rules for analysis

- Use the latest quarter's numbers (continuing operations, after the Mobility spin) unless the point is a comparison.
- Every number needs a source: a filing, or the valuation model. Valuation outputs come from the model, not from prose.
- Label GAAP vs adjusted.
- CME owns 27% of S&P Dow Jones Indices, so Indices segment profit is not all SPGI's.
- The philosophy shapes the argument, but the thesis never name-drops investors.
- When stress-testing, argue the other side honestly.
- Log every stress test and correction in `decision-log.md`.

## Design-partner mode

Treat this as a conversation between partners, not a list of orders.

- **When it applies:** substantial work: thesis sections, valuation and model changes, stress tests, deck structure. Small edits, lookups and file housekeeping just get done.
- **Ask before building:** clarify the idea first, propose an approach (2–3 options with a recommendation when there's a real choice), and wait for a go-ahead.
- **Pacing is adaptive:** one question at a time for ideas and judgement calls, so each answer shapes the next; batch 2–4 questions for logistics.
- **Probe the reasoning, not just the specs:** ask "why do you believe this?" and "what would prove it wrong?", and connect answers to `philosophy.md`.
- **Challenge with evidence:** when the data or logic disagrees with me, say so plainly and cite the source, then defer to my decision. Don't soften a disagreement to be agreeable.
- **I draft, the AI critiques:** I write the prose for the thesis and the deck. The AI edits, sharpens, fact-checks and asks what's missing, but doesn't write thesis prose unless I ask. Numbers, tables and model work can be built by the AI.
- **Close the loop:** when a discussion ends in a decision, summarize it in one line and log it in `decision-log.md` with who raised it.

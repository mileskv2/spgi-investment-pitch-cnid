---
name: editorial-charts
description: Miles's house chart style - clean, editorial, academic charts in the spirit of The Economist and Schwabish (2014), with soft pastel fills and one deep accent (navy, plum or rose). Use whenever making a chart, graph or figure for a report, presentation, GitHub README or school assignment, or when the user asks for "my chart style", "economist-style" or "editorial" charts. Python/matplotlib helper included; the rules also apply in Excel, R or Google Sheets.
---

# Editorial charts

Charts that are calm, readable and human: one point per chart, stated in the headline, with nothing on the page that doesn't help the reader.

**Not The Economist's brand.** Borrow the layout ideas only. Never use Economist Red (#E3120B), their logo, their fonts, or their name on a chart.

## Sources the rules come from

- Schwabish, J. (2014). "An Economist's Guide to Visualizing Data." *Journal of Economic Perspectives* 28(1): 209–234. Show the data, reduce clutter, integrate text and graph.
- The Economist's public design system: the principles ("less is more", "deliberate typography", "restrained palette"), tonal colour ladders, and a grey ladder for text. Method only, no brand values.
- The `dataviz` skill's palette validator for colour-blind checks.

## The anatomy of every chart (top to bottom, all left-aligned)

1. **Accent rule**: a short, thin bar in the chart's accent colour (step 45), top left.
2. **Headline** (serif, bold): the takeaway as a short sentence. "Indices grew 20% while Ratings grew 2%", not "Segment growth". **One line, about 6 characters per inch of figure width (≈42 for a 7-inch chart).** If it doesn't fit, cut words, don't shrink the font. "Men overrate their looks more than women", not "Everyone overrates themselves; men and women differ most on looks".
3. **Subtitle** (sans): subject, period, units. "S&P Global, Q3 2026, $m". Units go here once, not as % or $ on every tick. **One line, about 8.5 characters per inch (≈60 at 7 inches).** No explanations of the axes here; axis titles go on the axes.
4. **Legend**, only if direct labels don't fit: one row of small squares under the subtitle.
5. **The plot.**
6. **Source line** (small, bottom left): "Source: ...". Every chart has one.

## Rules

- **Show the data.** The data marks are the darkest, strongest thing on the chart. Gridlines are faint (grey 85), and the zero baseline is slightly darker than the other gridlines.
- **Reduce clutter.** No chart border, no tick marks, no 3D, no shadows, no gradients, no markers on every point, no numbers on every bar. Label the one or two values that matter.
- **Integrate text.** Label series directly (at the end of the line, beside the bar) rather than in a distant legend. Put notes right next to the point they describe.
- **No rotated text.** Axis titles are horizontal, or folded into the subtitle. Long category names mean horizontal bars.
- **Value axis placement.** On the right for time series; on top for horizontal bars.
- **Bars start at zero.** Lines may not, if the subtitle makes the range clear.
- **One y-axis only.** Two measures of different scale need two charts or an index (=100).
- **Emphasis over rainbow.** Highlight the one series or bar that matters in the accent; everything else in the pastel (step 90) or grey 70.
- **Small multiples over spaghetti.** More than 3–4 lines means a grid of small charts on a shared scale.
- **No pies.** Use bars, a stacked bar, or a slope chart.
- **Greyscale check.** The chart should still read if printed in black and white.

## Colour

Each accent is a ladder: one hue, five lightness steps.

| Step | Job |
|---|---|
| 30 | Bold values, emphasis text |
| 45 | **The accent**: highlighted mark, accent rule |
| 55 | Second mark only when it's a different hue (see below) |
| 90 | **Pastel**: context bars, background series |
| 95 | Faint bands (recessions, forecast periods) |

| Ladder | 30 | 45 | 55 | 90 | 95 |
|---|---|---|---|---|---|
| navy | #113D70 | #215DA5 | #4C82C6 | #CBE0FC | #E7F1FE |
| plum | #592656 | #853E80 | #A864A2 | #F0D4EC | #F8ECF7 |
| rose | #67222C | #993845 | #BD5F69 | #FBD3D4 | #FDEBEC |
| teal | #004C49 | #00736E | #009690 | #BDE8E4 | #E2F5F3 |

- **One chart, one ladder** by default: accent (45) + pastel (90). This pair passes colour-blind checks easily.
- **Two shades of the same hue (45 and 55) are NOT two series.** They are too close to tell apart (validator fails).
- **Several series** use different hues, in this fixed order: navy 45, rose 55, plum 45. All three pass the colour-blind checks together. A 4th (teal 55) is allowed only if every series is directly labelled; teal and rose collide for red-green colour blindness. More than 4: small multiples or fold into "Other".
- **Pastels are fills, never text or thin lines.** They fail contrast on their own, so a pastel series needs a label or a legend.
- **Rose reads as "bad" in finance.** Avoid it for P&L or losses unless that's the point.
- New colours? Validate with the `dataviz` skill's `scripts/validate_palette.js` before using them.

**Ink (grey ladder for text and lines):**

| Use | Hex |
|---|---|
| Headline, values | #1A1A1A |
| Subtitle, axis labels, category names | #404040 |
| Source line, notes | #595959 |
| Baseline | #8C8C8C |
| Gridlines | #D9D9D9 |

**Background:** white (#FFFFFF) by default, or warm paper (#F5F4EF) for a softer, printed feel. Test the warm one on the projector first.

## Typography

- Headline: a serif. Charter on Mac (Georgia, Source Serif or Garamond elsewhere), bold, ~16pt.
- Everything else: a clean sans. Avenir Next on Mac (Inter, Lato or Calibri elsewhere).
- Sizes: subtitle ~11pt, labels 10pt, source 8.5pt. Nothing smaller than 8.5pt; for slides, scale everything up 1.3x.
- Spacing on an 8-point rhythm: padding and gaps in multiples of 8px.

## Sharpness

Charts must never look blurry. Matplotlib's notebook default is 72-100 dpi, which looks soft on any modern screen.

- **Jupyter notebooks:** `apply_style()` switches inline output to retina (2x pixels). If you can't import the helper (e.g. a notebook someone else will run), put this in the notebook yourself: `from matplotlib_inline.backend_inline import set_matplotlib_formats; set_matplotlib_formats("retina")`.
- **Files:** SVG for slides, GitHub and web; PNG at 200 dpi otherwise (`finish()` does this).
- **Figure size:** about 7 x 4.6 inches for notebooks and reports. Larger figures get scaled down and the text shrinks with them.

## Notebooks that get submitted or shared

Don't import `style.py` from `~/.claude` in a notebook another person will run (a TA, a teammate, a client); it breaks "Restart & Run All". Paste a trimmed copy of the colours, `frame()` and `legend_row()` into a style cell after the imports.

## Python helper

`style.py` in this skill folder does the furniture. Copy it next to the analysis code, or import it from here:

```python
import os, sys; sys.path.insert(0, os.path.expanduser("~/.claude/skills/editorial-charts"))
from style import apply_style, frame, finish, LADDERS, INK

apply_style()
fig, ax = frame("Indices grew 20% while Ratings grew 2%",
                "S&P Global revenue growth by segment, Q3 2026, % y/y",
                "Source: S&P Global Q3 2026 earnings release.", ladder="navy")
ax.barh(names, values, color=LADDERS["navy"][90])   # context
# ...highlight one bar in LADDERS["navy"][45], label it directly...
finish(fig, ax, "chart.svg", value_axis="top")      # SVG for slides and GitHub, PNG at 200 dpi otherwise
```

## Before calling a chart done

1. Does the headline state a takeaway the chart actually proves?
2. Is there a source line?
3. Is any text rotated, or any unit repeated on every tick?
4. Is anything darker than the data?
5. Are the headline and subtitle each one short line (see the character limits above)? `frame()` raises an error if not.
6. Is it sharp? Retina inline in notebooks, SVG or 200-dpi PNG for files.
7. Render it and look at it at full size (open the PNG): label collisions, text crossing a line or the diagonal, clipped text, crowded legend. Labels go in empty space, never on top of a line. Fix and re-render until clean.

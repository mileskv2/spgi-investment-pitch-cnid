"""House chart style: editorial layout, pastel fills, one deep accent."""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# One hue per ladder, five lightness steps (see SKILL.md for the job of each step)
LADDERS = {
    "navy": {30: "#113D70", 45: "#215DA5", 55: "#4C82C6", 90: "#CBE0FC", 95: "#E7F1FE"},
    "plum": {30: "#592656", 45: "#853E80", 55: "#A864A2", 90: "#F0D4EC", 95: "#F8ECF7"},
    "rose": {30: "#67222C", 45: "#993845", 55: "#BD5F69", 90: "#FBD3D4", 95: "#FDEBEC"},
    "teal": {30: "#004C49", 45: "#00736E", 55: "#009690", 90: "#BDE8E4", 95: "#E2F5F3"},
}

# Fixed order for multi-series charts; validated together for colour blindness.
# The 4th (teal) only with direct labels on every series.
SERIES = ["#215DA5", "#BD5F69", "#853E80", "#009690"]

INK = {
    "strong": "#1A1A1A",    # headline, values
    "body": "#404040",      # subtitle, axis and category labels
    "soft": "#595959",      # source line, notes
    "baseline": "#8C8C8C",
    "grid": "#D9D9D9",
}

PAPER = {"white": "#FFFFFF", "warm": "#F5F4EF"}

SERIF = ["Charter", "Georgia", "Source Serif 4", "DejaVu Serif"]
SANS = ["Avenir Next", "Inter", "Lato", "Helvetica Neue", "DejaVu Sans"]


def apply_style(paper="white"):
    """Set matplotlib defaults once per script."""
    # default inline output is low-res and looks blurry; use 2x pixels in notebooks
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            from matplotlib_inline.backend_inline import set_matplotlib_formats
            set_matplotlib_formats("retina")
    except ImportError:
        pass
    plt.rcParams.update({
        "figure.dpi": 110,
        "font.family": "sans-serif",
        "font.sans-serif": SANS,
        "font.serif": SERIF,
        "font.size": 10,
        "text.color": INK["strong"],
        "axes.labelcolor": INK["body"],
        "axes.edgecolor": INK["grid"],
        "xtick.color": INK["body"],
        "ytick.color": INK["body"],
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "figure.facecolor": PAPER[paper],
        "axes.facecolor": PAPER[paper],
        "svg.fonttype": "path",   # SVGs render the same on any machine
    })


def frame(title, subtitle, source, ladder="navy", figsize=(7, 4.6), plot_top=0.76):
    """Figure with the accent rule, headline, subtitle and source line in place."""
    # long headlines run off the figure; the limit scales with the figure width
    max_title, max_sub = int(6 * figsize[0]), int(8.5 * figsize[0])
    if len(title) > max_title:
        raise ValueError(f"Headline is {len(title)} chars; keep it to {max_title} at this width: {title!r}")
    if len(subtitle) > max_sub:
        raise ValueError(f"Subtitle is {len(subtitle)} chars; keep it to {max_sub} at this width: {subtitle!r}")
    fig, ax = plt.subplots(figsize=figsize)
    fig.subplots_adjust(left=0.08, right=0.92, top=plot_top, bottom=0.13)
    fig.add_artist(Rectangle((0.03, 0.965), 0.06, 0.012, transform=fig.transFigure,
                             color=LADDERS[ladder][45], linewidth=0))
    fig.text(0.03, 0.90, title, family="serif", fontsize=16, fontweight="bold")
    fig.text(0.03, 0.845, subtitle, fontsize=11, color=INK["body"])
    fig.text(0.03, 0.03, source, fontsize=8.5, color=INK["soft"])
    for side in ["top", "right", "left", "bottom"]:
        ax.spines[side].set_visible(False)
    return fig, ax


def legend_row(fig, items, y=0.785):
    """One row of small squares under the subtitle. Use only when direct labels don't fit."""
    x = 0.03
    for label, colour in items:
        fig.add_artist(Rectangle((x, y), 0.016, 0.026, transform=fig.transFigure,
                                 color=colour, linewidth=0))
        fig.text(x + 0.022, y + 0.003, label, fontsize=9.5, color=INK["strong"])
        x += 0.04 + 0.0115 * len(label)  # rough width of the label


def finish(fig, ax, path, value_axis="right"):
    """Gridlines along the value axis, darker baseline, then save (SVG or 200-dpi PNG)."""
    if value_axis == "right":
        ax.yaxis.tick_right()
        ax.grid(axis="y", color=INK["grid"], linewidth=0.8, zorder=0)
        if ax.get_ylim()[0] <= 0:
            ax.axhline(0, color=INK["baseline"], linewidth=1, zorder=1)
    elif value_axis == "top":
        ax.xaxis.tick_top()
        ax.grid(axis="x", color=INK["grid"], linewidth=0.8, zorder=0)
        if ax.get_xlim()[0] <= 0:
            ax.axvline(0, color=INK["baseline"], linewidth=1, zorder=1)
    ax.set_axisbelow(True)
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path

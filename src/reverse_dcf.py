"""Reverse DCF: what FCF growth does today's enterprise value imply?"""

import argparse

# Inputs at the Nov 6, 2026 close ($467.80), Q3 2026 data, continuing operations.
# EV = 289.9M shares x $467.80 + debt $13.062B - cash $2.441B (Q3 2026 exhibits p.8).
# It values SPGI holders' claim only, so FCF is after distributions to CME's 27% of
# S&P Dow Jones Indices (Q3 exhibits p.18). FY26E FCF grosses up 9M 2026 by the
# prior-year Q4 share of FCF, which is approximate (about +/-6%).
INPUTS = {
    "ev_bn": 146.236,         # enterprise value, $bn
    "fcf_bn": 5.1204,         # FY26E adjusted FCF after NCI, $bn (reported: 4.8126)
    "discount_rate": 0.085,
    "terminal_growth": 0.03,
    "years": 10,
}

# Round 1 (Sept 30, 2026), kept for the record. It paired FCF before CME's share
# with an EV that excludes CME's stake, which understated implied growth (~6.1%).
ROUND1 = {"ev_bn": 127.9, "fcf_bn": 5.35}


def dcf_value(fcf, growth, discount_rate, terminal_growth, years):
    """Present value of `years` of FCF growing at `growth`, plus a Gordon terminal value."""
    pv = 0.0
    for t in range(1, years + 1):
        fcf *= 1 + growth
        pv += fcf / (1 + discount_rate) ** t
    terminal = fcf * (1 + terminal_growth) / (discount_rate - terminal_growth)
    return pv + terminal / (1 + discount_rate) ** years


def implied_growth(ev, fcf, discount_rate, terminal_growth, years):
    """Solve for the growth rate that makes the DCF value equal today's EV (bisection)."""
    low, high = -0.20, 0.40
    for _ in range(100):
        mid = (low + high) / 2
        if dcf_value(fcf, mid, discount_rate, terminal_growth, years) < ev:
            low = mid
        else:
            high = mid
    return mid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key, default in INPUTS.items():
        parser.add_argument(f"--{key.replace('_', '-')}", type=type(default), default=default)
    args = parser.parse_args()

    g = implied_growth(args.ev_bn, args.fcf_bn, args.discount_rate, args.terminal_growth, args.years)
    print(f"Implied {args.years}-year FCF growth: {g:.1%}")

    # The answer is sensitive to the terminal assumption, so always show the range.
    print("\nSensitivity (rows: discount rate, columns: terminal growth)")
    terminal_rates = [0.02, 0.025, 0.03]
    print("        " + "".join(f"{tg:>8.1%}" for tg in terminal_rates))
    for r in [0.08, 0.085, 0.09]:
        row = [implied_growth(args.ev_bn, args.fcf_bn, r, tg, args.years) for tg in terminal_rates]
        print(f"{r:>7.1%} " + "".join(f"{x:>8.1%}" for x in row))


if __name__ == "__main__":
    main()

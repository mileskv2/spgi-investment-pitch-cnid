"""Reverse DCF: what FCF growth does today's enterprise value imply?"""

import argparse

# Round 1 inputs (Sept 30, 2026). Refresh with Q3 numbers before using in the pitch.
ROUND1 = {
    "ev_bn": 127.9,          # enterprise value, $bn
    "fcf_bn": 5.35,          # FY26E adjusted FCF, $bn (before CME's noncontrolling share)
    "discount_rate": 0.085,
    "terminal_growth": 0.03,  # not stated in the Round 1 report; 3% reproduces its ~6% result
    "years": 10,
}


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
    for key, default in ROUND1.items():
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

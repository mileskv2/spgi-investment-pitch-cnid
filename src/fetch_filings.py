"""Download S&P Global's reported financials from SEC EDGAR (free, public XBRL data)."""

import json
import os
import sys
import urllib.request
from pathlib import Path

import pandas as pd

SPGI_CIK = "0000064040"
URL = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{SPGI_CIK}.json"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Headline metrics. Companies switch XBRL tags over time (SPGI moved revenue to the
# ASC 606 tag in 2018), so each metric lists its tags in order of preference.
CONCEPTS = {
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"],
    "operating_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquireProductiveAssets", "PaymentsToAcquirePropertyPlantAndEquipment"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}


def fetch_company_facts():
    """Fetch the raw companyfacts JSON. The SEC requires a contact in the User-Agent."""
    user_agent = os.environ.get("SEC_USER_AGENT")
    if not user_agent:
        sys.exit('Set SEC_USER_AGENT first, e.g. export SEC_USER_AGENT="Your Name you@example.com"')
    request = urllib.request.Request(URL, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def is_calendar_year(entry):
    """True for full-year values. The SEC's 'frame' field (e.g. CY2024) marks one
    deduplicated value per period; 10-K 'FY' entries alone also include quarters."""
    frame = str(entry.get("frame", ""))
    return frame.startswith("CY") and len(frame) == 6


def annual_table(facts):
    """Collect full-year values for each metric into one table (rows: years)."""
    gaap = facts["facts"]["us-gaap"]
    rows = []
    for metric, tags in CONCEPTS.items():
        for tag in tags:
            for unit, entries in gaap.get(tag, {}).get("units", {}).items():
                for e in entries:
                    if is_calendar_year(e):
                        rows.append({"metric": metric, "year": int(e["frame"][2:]),
                                     "value": e["val"], "preference": tags.index(tag)})
    df = pd.DataFrame(rows)
    # When two tags cover the same year, keep the preferred one.
    df = df.sort_values("preference").drop_duplicates(subset=["metric", "year"], keep="first")
    return df.pivot(index="year", columns="metric", values="value")


def main():
    facts = fetch_company_facts()
    table = annual_table(facts)
    DATA_DIR.mkdir(exist_ok=True)
    out = DATA_DIR / "spgi_annual.csv"
    table.to_csv(out)
    print(table.tail(6).to_string())
    print(f"\nSaved {out}")


if __name__ == "__main__":
    main()

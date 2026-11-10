"""
Sales Data Analysis
-------------------
Practice project for my data-analysis skills (I worked in marketing
in India for 3 years, and I am now studying Excel and Python).

Reads sales.csv (date, product, units, revenue) and prints:
  * Total units sold and total revenue
  * Revenue by product, and the best-selling product
  * Monthly revenue trend, with the change vs the previous month
  * Average revenue per order (per row)

All amounts are in Japanese yen (JPY).

Built by Kaushik Shivam while learning Python.
Standard library only (csv).
"""

import csv

SALES_FILE = "sales.csv"


def load_sales(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append({
                "date": row["date"],
                "month": row["date"][:7],          # "2026-08-01" -> "2026-08"
                "product": row["product"],
                "units": int(row["units"]),
                "revenue": float(row["revenue"]),
            })
    return rows


def main():
    rows = load_sales(SALES_FILE)

    total_units = sum(r["units"] for r in rows)
    total_revenue = sum(r["revenue"] for r in rows)

    print(f"Sales analysis - {len(rows)} orders")
    print(f"Period: {rows[0]['date']} to {rows[-1]['date']}")
    print("-" * 52)
    print(f"Total units sold:    {total_units:,}")
    print(f"Total revenue:       {total_revenue:,.0f} JPY")
    print(f"Average per order:   {total_revenue / len(rows):,.0f} JPY")

    # Revenue and units per product
    by_product = {}
    for r in rows:
        p = by_product.setdefault(r["product"], {"units": 0, "revenue": 0.0})
        p["units"] += r["units"]
        p["revenue"] += r["revenue"]

    print("\nBy product:")
    print(f"{'Product':<20}{'Units':>8}{'Revenue':>14}{'Share':>9}")
    for name, p in sorted(by_product.items(),
                          key=lambda item: item[1]["revenue"], reverse=True):
        share = p["revenue"] / total_revenue
        print(f"{name:<20}{p['units']:>8,}{p['revenue']:>14,.0f}{share:>9.1%}")

    best = max(by_product, key=lambda name: by_product[name]["revenue"])
    print(f"\nBest product by revenue: {best} "
          f"({by_product[best]['revenue']:,.0f} JPY)")

    # Monthly trend
    by_month = {}
    for r in rows:
        by_month[r["month"]] = by_month.get(r["month"], 0.0) + r["revenue"]

    print("\nMonthly revenue trend:")
    previous = None
    for month in sorted(by_month):
        change = ""
        if previous is not None:
            pct = by_month[month] / previous - 1
            change = f"({pct:+.1%} vs last month)"
        print(f"  {month}:  {by_month[month]:>10,.0f} JPY  {change}")
        previous = by_month[month]


if __name__ == "__main__":
    main()

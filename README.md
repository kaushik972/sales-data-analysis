# Sales Data Analysis

A small analysis of a sample sales dataset: totals, revenue by product, the best seller, and the monthly trend.

## Why I built this

Before coming to Japan I worked in marketing at a logistics company in India for 3 years, and analysing sales numbers was part of my everyday work — promotions I ran based on the data lifted sales by 25–30%. I'm now studying Excel and Python for data analysis, and this project is me re-doing, in Python, the kind of summary I used to build in spreadsheets.

## What it does

Reads `sales.csv` (date, product, units, revenue — 30 orders over Aug–Oct 2026) and prints:

- Total units, total revenue, and average revenue per order
- Units, revenue and revenue share per product
- The best product by revenue
- Monthly revenue with the change vs the previous month

## How to run

```bash
cd sales-data-analysis
python sales_analysis.py
```

Point it at your own data by replacing `sales.csv` (keep the same columns).

## Sample output

```
Sales analysis - 30 orders
Period: 2026-08-01 to 2026-10-30
----------------------------------------------------
Total units sold:    1,466
Total revenue:       1,518,600 JPY
Average per order:   50,620 JPY

By product:
Product                Units       Revenue    Share
Coffee Beans 1kg         485       727,500    47.9%
Rice 5kg                 251       401,600    26.4%
Green Tea Box            341       272,800    18.0%
Snack Pack               389       116,700     7.7%

Best product by revenue: Coffee Beans 1kg (727,500 JPY)

Monthly revenue trend:
  2026-08:     479,000 JPY
  2026-09:     475,700 JPY  (-0.7% vs last month)
  2026-10:     563,900 JPY  (+18.5% vs last month)
```

One thing that jumps out: Snack Pack sells the second-most units but earns the least revenue — a classic case where unit sales alone would mislead you. (Data is sample data created for practice.)

## Files

- `sales_analysis.py` — the program
- `sales.csv` — sample sales data (30 orders, 4 products, 3 months)

## Next steps

- Add charts with matplotlib once I'm comfortable with libraries
- Compare the same analysis done in Excel and in Python, side by side
- Group by week as well as by month, and add a per-product monthly trend

*Standard library only for now. Built while learning Python.*

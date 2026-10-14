# Car sales analytics dashboard

Power BI dashboard with YTD/MTD sales, unit counts, weighted average selling price, regional views and vehicle/dealer filters.

![Dashboard preview](Car-Sales-Dashboard.png)

## Files and source
- [Power BI report](Cars%20Sales%20Dashboard.pbix)
- [Excel source](Car%20Sales..xlsx)
- [Audited KPI reference DAX](dax/Measures.dax) and [calendar table DAX](dax/Calendar.dax)
- [Independent source audit](audit_dashboard.py) and [measured results](results/)

The data and report began as a learning exercise using [this tutorial](https://www.youtube.com/watch?v=XnPo5Ft7RzQ). The report is tutorial-based; the independent source audit, explicit KPI definitions, reproducible result tables and refresh documentation were added in this repository. No independent authorship of the tutorial design is claimed.

The source contains 23,906 transactions dated January 2, 2022 through December 31, 2023. Car_id is unique and populated. One customer name is missing; this does not change sales/unit KPIs. The workbook filename is preserved so the existing report's source reference remains recognizable.

## KPI verification
| Calendar year | Sales | Cars sold | Average price |
| --- | ---: | ---: | ---: |
| 2022 | $300,340,345 | 10,645 | $28,214.22 |
| 2023 | $371,185,120 | 13,261 | $27,990.73 |

2023 sales grew 23.59%; cars sold grew 24.57%. Austin led 2023 unit sales with 2,296 cars. Using Sunday-start WEEKNUM(Date,1), week 36 had $14,854,928 in sales. Week numbering must be consistent when comparing results. These are full-calendar-year source totals, not a claim about today's YTD.

Average price is total sales divided by cars sold, so grouped averages are weighted by transactions. YTD/MTD follow the date context selected in the report. YoY measures compare the corresponding prior-year period and return blank where the prior-year denominator is unavailable. Filter dates through the calendar rather than treating missing previous-year data as zero.

## Model and DAX
The report visuals reference car_data and Calendar Table, plus the KPI names recorded in [results/audit.json](results/audit.json). A reproducible reference model uses a single-direction one-to-many relationship from Calendar Table[Date] to car_data[Date]. Mark Calendar Table as a date table and sort Month by Month Number. Preserve date-only values and make the relationship active.

The DAX files provide reconstructed, auditable formulas for these KPI definitions. The PBIX model is compressed; its exact internal formulas and active relationship settings were not exported or verified here. Compare the reference DAX with the existing measures in Power BI Desktop before replacing them. The independent audit validates the source totals, not the Power BI engine's filter behavior.

## Refresh and validate
1. Open the PBIX in Power BI Desktop.
2. In Transform data / Data source settings, change the Excel source path to your local Car Sales..xlsx. Retain the worksheet/table used by car_data and check column types.
3. Confirm Date is Date and Price ($) is numeric; trim trailing whitespace in column labels if rebuilding the query.
4. Check the calendar relationship, mark the date table, then refresh.
5. Select the complete 2023 calendar year and compare sales, unit count and average price with the audited totals above. Test YTD/MTD and prior-year comparisons at a partial-year cutoff. Clear other slicers for a full-source comparison.

Python 3.12 independent audit:
```bash
python -m pip install -r requirements.txt
python audit_dashboard.py
```
The audit also exports annual metrics, regional counts, weekly sales and color revenue shares. These source tables support reproducibility without requiring viewers to download/open Power BI.

## License
Repository additions are MIT licensed. External tutorial and dataset rights remain with their respective owners.

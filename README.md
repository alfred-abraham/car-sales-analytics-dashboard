# Car Sales Analytics Dashboard

## Overview

An executive-style Power BI dashboard for exploring automotive sales performance through KPI reporting, trends, regional comparisons, and interactive filters.

## Objective

Monitor year-to-date (YTD) and month-to-date (MTD) sales, average prices, and cars sold. Compare performance across manufacturers, dealer regions, body styles, and colors.

## Data

The repository includes [the Excel dataset](Car%20Sales..xlsx) supplied alongside [the original tutorial](https://www.youtube.com/watch?v=XnPo5Ft7RzQ). This is a learning project; the dataset and tutorial belong to their respective owners.

## Approach

1. Prepare and transform sales data with Power Query.
2. Build a data model and calendar table.
3. Calculate time-based KPIs with DAX, including `TOTALYTD()`, `TOTALMTD()`, and `SAMEPERIODLASTYEAR()`.
4. Present trends, regional sales, and manufacturer comparisons with interactive slicers.

## Results

Reported findings for the most recent year in the dataset:

- Sales totaled approximately **$371.2 million**, about **24%** above the previous year.
- Approximately **13.3 thousand cars** were sold, about **25%** above the previous year.
- Weekly sales peaked at approximately **$14.6 million** in week 36.
- Austin led regional car sales with **2,296 cars sold**.
- Pale white cars accounted for approximately **47%** of sales.

![Car sales dashboard](Car-Sales-Dashboard.png)

The dashboard includes YTD and MTD KPI cards, weekly sales trends, body-style and color breakdowns, a regional view, and a manufacturer performance table. Slicers cover engine, body style, dealer, year, and model.

## Tools

Microsoft Power BI Desktop, Power Query, DAX, and data modeling.

## How to Run

1. Clone or download this repository.
2. Open [`Cars Sales Dashboard.pbix`](Cars%20Sales%20Dashboard.pbix) in Power BI Desktop.
3. If a refresh cannot find the source workbook, update the Excel source path in Power Query to your local [`Car Sales..xlsx`](Car%20Sales..xlsx).
4. Refresh the data and use the slicers to explore the report.

For a quick preview without Power BI, open [the dashboard image](Car-Sales-Dashboard.png).

## Limitations and Next Steps

- The insights describe the supplied learning dataset and its historical period.
- Dashboard comparisons depend on the selected filters and date context.
- Future work could extend the report with profitability metrics or additional reporting periods.

## License

Repository content is covered by [the MIT license](LICENSE). The external dataset and tutorial retain their respective owners' rights.

from pathlib import Path
import argparse,json,zipfile
import pandas as pd
ROOT=Path(__file__).parent
def run():
    df=pd.read_excel(ROOT/'Car Sales..xlsx')
    df.columns=df.columns.str.strip()
    if df.Car_id.isna().any() or df.Car_id.duplicated().any(): raise ValueError('Car_id must be unique and populated')
    df['Date']=pd.to_datetime(df.Date)
    if df[['Date','Price ($)']].isna().any().any(): raise ValueError('Missing date or price')
    annual=df.assign(Year=df.Date.dt.year).groupby('Year').agg(sales=('Price ($)','sum'),cars=('Car_id','count'),average_price=('Price ($)','mean'))
    annual['sales_yoy_pct']=annual.sales.pct_change()*100
    annual['cars_yoy_pct']=annual.cars.pct_change()*100
    output=ROOT/'results'; output.mkdir(exist_ok=True)
    annual.to_csv(output/'annual_metrics.csv')
    latest=df[df.Date.dt.year==df.Date.dt.year.max()]
    regions=latest.groupby('Dealer_Region').agg(sales=('Price ($)','sum'),cars=('Car_id','count')).sort_values('cars',ascending=False)
    regions.to_csv(output/'latest_year_regions.csv')
    # Sunday-start WEEKNUM(Date,1), matching the documented reference DAX.
    latest=latest.copy()
    start=pd.Timestamp(int(latest.Date.dt.year.iloc[0]),1,1)
    latest['week']=((latest.Date-start).dt.days+(start.dayofweek+1)%7)//7+1
    weekly=latest.groupby('week')['Price ($)'].sum()
    weekly.to_csv(output/'latest_year_weekly_sales.csv')
    colors=latest.groupby('Color')['Price ($)'].sum()
    (100*colors/colors.sum()).rename('sales_share_percent').to_csv(output/'latest_year_colors.csv')
    # Exact formulas are not readable from the PBIX's compressed model.
    # Record actual visual references; reference DAX is documented as reconstructed.
    names=set()
    def walk(o):
        if isinstance(o,dict):
            for k,v in o.items():
                if k in ['Entity','Property']: names.add(str(v))
                walk(v)
        elif isinstance(o,list):
            for value in o: walk(value)
    with zipfile.ZipFile(ROOT/'Cars Sales Dashboard.pbix') as z:
        for name in z.namelist():
            if name.endswith('visual.json'): walk(json.loads(z.read(name)))
    summary={'rows':len(df),'date_min':str(df.Date.min().date()),'date_max':str(df.Date.max().date()),
        'missing_values':{k:int(v) for k,v in df.isna().sum().items() if v},
        'referenced_tables_and_fields':sorted(names),'source':'Car Sales..xlsx','report':'Cars Sales Dashboard.pbix',
        'measure_formula_status':'Reference formulas reconstructed for documented KPIs; not an export of compressed PBIX formulas.'}
    (output/'audit.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(annual.to_string()); print(regions.head().to_string()); print('Peak week',weekly.idxmax(),weekly.max()); print(summary)
if __name__=='__main__': run()

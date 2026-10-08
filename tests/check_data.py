from pathlib import Path
import pandas as pd
p=Path(__file__).resolve().parents[1]
df=pd.read_csv(p/'data/GSF_Geography_Country_ResearchIntensity_v1.csv')
assert len(df)==86, f'Unexpected number of country entries: {len(df)}'
assert df.Country.is_unique
for c in ['Records','As','F','U','Cr']:
    assert df[c].notna().all() and (df[c]>=0).all(), c
expected={'India':(222,25,177,31,10),'China':(140,33,96,7,13),'United States':(64,32,5,21,10)}
for name,values in expected.items():
    row=df.set_index('Country').loc[name]
    assert tuple(int(row[k]) for k in ['Records','As','F','U','Cr'])==values
for ext in ['png','pdf','svg']:
    assert (p/'figures'/f'GSF_Integrated_Global_Evidence_Code_600dpi.{ext}').exists()
print('PASS: 86 country entries, key counts, and 3 figure exports verified')

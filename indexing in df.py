import pandas as pd
GDP={"india":{2020:3.8,2025:5},"USA":{2020:13.5,2025:15}}
frame3=pd.DataFrame(GDP)
frame3.index.name="YEAR"
frame3.columns.name="COUNTRY"
print(frame3)
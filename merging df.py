import pandas as pd
import numpy as np

df1=pd.DataFrame({'lkey':[1,2,3],'Name':['ram','sita','devi']})
print(df1)
df2=pd.DataFrame({'rkey':[1,2,4],'marks':[85,90,75]})
print(df2)
r=pd.merge(df1,df2,left_on='lkey',right_on='rkey')
print(r)
import pandas as pd
s=pd.Series(['a','b','c','d'])
r=s.map({'a':'apple','b':'ball','c':'cat','d':'dog'})
print(r)
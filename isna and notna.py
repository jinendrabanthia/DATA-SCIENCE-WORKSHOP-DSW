import pandas as pd
import numpy as np
data=pd.Series([1.2,3.5,np.nan,0,None])
print(data)
print(data.isna())
print(data.notna())
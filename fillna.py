#fillna is used to replace missiing values nan with another value
import pandas as pd 
import numpy as np
data=pd.Series([1,2,np.nan,4,5])
print(data)
print(data.fillna(0))

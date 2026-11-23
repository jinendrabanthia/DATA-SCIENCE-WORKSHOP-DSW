import numpy as np
import pandas as pd
data=pd.Series(np.random.randn(9),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,3,1,2,2,3]])
data['b']
data.loc[['b','d']]
data.loc[:,2]

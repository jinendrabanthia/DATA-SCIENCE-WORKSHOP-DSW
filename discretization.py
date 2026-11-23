'''why does 0.994 appear instead of 1 
=when you use integer value for bins pandas entend the range slightly

'''
import numpy as np
import pandas as pd
x = np.array([1,2,3,7,4])
pd.cut(x,bins=2) #Used for discretization(binning)

x = np.array([1,2,3,7,4])
y = [0,3,5,8]
pd.cut(x,bins=y)

bins = pd.IntervalIndex.from_tuples([(0,2),(2,3),(3,7)])
pd.cut(x,bins)

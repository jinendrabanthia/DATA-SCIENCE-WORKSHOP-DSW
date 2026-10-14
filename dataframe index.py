import numpy as np
import pandas as pd
a=np.array([[1,2],[3,4],[5,6]])
a=pd.DataFrame(a,index=['r1',"r2","r3"],columns=["c1","c2"])
print(a)
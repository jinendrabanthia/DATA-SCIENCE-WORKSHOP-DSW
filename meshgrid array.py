# pyrefly: ignore [missing-import]
import numpy as np
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=[]
for x,y,c in zip(xarr,yarr,cond):
    if c:
        result.append(x)
    else:
        result.append(y)
print(result)
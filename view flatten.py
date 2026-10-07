import numpy as np

a=np.array([[1,2],[3,4]])
c=a.flatten()
c[0]=10
print(a)
print(c)
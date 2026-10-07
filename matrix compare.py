import numpy as np
a=np.eye(4)
b=np.eye(4,k=1)+np.eye(4,k=1)
a==b
print(a)
print(b)
print(a==b)

#create identity matrix of order 4 ,create a 4x4 matrix where subdiagonal elements =1
#super diagonal elemenrs are 1 and all other are 0 
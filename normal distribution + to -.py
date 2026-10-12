#Create a randomly generated 4 × 4 matrix, where each data is from the
#standard normal distribution. Replace all positive values with 2 and all
#negative values with –2


import numpy as np
a = np.random.randn(4, 4)

print("Original Matrix:")
print(a)
a[a > 0] = 2
a[a < 0] = -2

print("\nModified Matrix:")
print(a)


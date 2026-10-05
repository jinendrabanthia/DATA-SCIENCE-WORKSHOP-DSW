import numpy as np
import timeit

l = np.arange(5)
m = list(range(5))

l1 = l * 2

print("NumPy array:", l)
print("After multiplication:", l1)

time_taken = timeit.timeit(lambda: l * 2, number=100000)

print("Time taken:", time_taken, "seconds")


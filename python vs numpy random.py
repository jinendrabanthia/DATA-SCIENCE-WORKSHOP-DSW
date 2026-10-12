from random import sample
import timeit
from random import normalvariate
N=1000000
%timeit samples=[normalvariate(0,1) for _ in range(N)]
#% is a special function for jupyter

#random.normalvariate number generates a normal number uses gausian distribution
#gaussian distribution means bell curve 

#normalvariate method belongs to python build in random module,not numpy 
#0-mean 1- standard deviation 

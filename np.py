import numpy as np
import time
import sys

a = range(1000)
print(sys.getsizeof(1)*len(a))


array = np.arange(1000)
print(array.size*array.itemsize)
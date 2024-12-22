import numpy as np
import time
import sys

SIZE = 1000000 


#Native Python
l1 = range(SIZE)
l2 = range(SIZE)
start = time.time()
result= [(x+y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

#numpy
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
result = a1+a2
print((time.time()-start)*1000)
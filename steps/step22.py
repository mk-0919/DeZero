import numpy as np
from Variable import Variable
from Function import *

x = Variable(np.array(2.0))
y = -x
print(y)

y1 = 2.0 - x
y2 = x - 1.0
print(y1)
print(y2)

y = x ** 3
print(y)
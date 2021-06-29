import numpy as np
from Variable import Variable
from Function import *

x = Variable(np.array(2.0))
y = x + np.array(3.0)
print(y)

y = x + 3.0
print(y)

y = 3.0 * x + 1.0
print(y)

x = Variable(np.array([1.0]))
y = np.array([2.0]) + x
print(y)
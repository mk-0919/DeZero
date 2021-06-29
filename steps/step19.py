import numpy as np
from Variable import Variable
from Function import *

x = Variable(np.array([[1,2,3],[4,5,6]]))
print(x.shape)

x = Variable(np.array([[1,2,3,],[4,5,6]]))
print(len(x))
import numpy as np
from Variable import Variable
from Function import *

for i in range(10):
    x = Variable(np.random.randn(10000))
    y = square(square(square(x)))
    print(x.data,y.data)
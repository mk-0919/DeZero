import numpy as np
from Variable import Variable
from Function import *

a = Variable(np.array(3.0))
b = Variable(np.array(2.0))
c = Variable(np.array(1.0))

#y = add(mul(a,b),c)
y = a * b + c

y.backward()

print(y)
print(a.grad)
print(b.grad)
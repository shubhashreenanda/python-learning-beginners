from numpy import *

a1 = arange(1,10)
a2 = a1.view()

print('a1',a1)
print('a2',a2)

a2[3] = 40
print('after modification')
print('a1',a1)
print('a2',a2)
from numpy import *

a1 = array([10,30,50,70,90])
a2 = array([20,40,60,80,100])

print(a1>a2)
print(all(a1>a2))
print(any(a1>a2))

print(logical_and(a1>10,a1<101))

print(where(a1%2!=0,a1,0))
print(where(a1>a2,a1,a2))
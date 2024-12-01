from functools import reduce

from datatype import billingAmount


def cube(n):
    return n**3

print(cube(3))

x=lambda n:n**3
print(x(5))


l=lambda x:'YES' if x%2==0 else 'NO'
print(l(9))

def add(a,b):
    return a+b
print(add(10,20))

l1=lambda a,b:a+b
print(l1(1,6))

#filter
list1=[10,39,878,7,87]
result=list(filter(lambda x:x%2==0,list1))
print(result)

for i in result:
    print(i)

#map
l2=[2,3,4,5,6,7,8,9]
result=list(map(lambda y:y*2,l2))
print(result)

l3=[3,5,7,8,9,54,65]
result=reduce(lambda x,y:x+y,l3)
print(result)
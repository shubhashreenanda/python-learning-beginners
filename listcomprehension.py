#cubes
# list=[]
# for x in range(1,11):
#     list.append(x**3)
# print(list)

list=[]
list=[x**3 for x in range(1,11)]
print(list)

#even
list=[]
list=[x for x in range(1,20) if x%2==0]
print(list)

#product
a=[1,2,3,4,5]
b=[2,3,5,6,7]
list=[]

# for i in range(len(a)):
#     list.append(a[i]*b[i])
# print(list)


list=[a[i]*b[i] for i in range(len(a))]
print(list)
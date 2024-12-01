a=[2,4,5,6,7]
b=[8,4,5,6]
result=[]

# for i in a :
#     if i in b:
#         result.append(i)
# print(result)

result=[i for i in a if i in b]
print(result)
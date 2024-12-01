from os.path import exists

s={10,23,3,4,56,6,10,"xyz"}
print(s)
print(type(s))
s.update([556,98,88])

s.remove(6)
print(s)

f=frozenset(s)


list=["india","nepal","bhutan"]
list.append("australia")
print(list)
list.remove(list[0])
print(list)
list.insert(2,"china")
print(list)

my_tuple=(1,2,3,"x","y","z")
print(my_tuple[1])
print(my_tuple[3])
print(len(my_tuple))
print(2 in my_tuple)


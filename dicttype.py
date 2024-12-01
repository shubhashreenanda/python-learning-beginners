dict1={1:"john",2:"ambika"}
print(dict1)

print(dict1.items())

k=dict1.keys()
for i in k:
    print(i)

v=dict1.values()
for i in v:
    print(i)

print(dict1[2])

del dict1[2]
print(dict1)

student_info={"name":"jimmy","age":23,"major":"yes"}
print("student information dictionary", student_info)

print("name of the student:", student_info["name"])
print("age of the student:", student_info["age"])

student_info.update({"email":"abc@gmail.com"})
print(student_info)

del student_info["major"]

print(student_info)

k=student_info.keys()
for i in k:
    print(i)

v=student_info.values()
for i in v:
    print(i)
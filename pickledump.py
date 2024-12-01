import my_pickle,Student

f = open("student.dat","wb")
s= Student.Student(123,"John Kumar",90)
pickle.dump(s,f)
f.close()
# f = open("myfile.txt","w")
# s = input("enter text:")
# f.write(s)
# f.close()

# f = open("myfile.txt", 'r')
# s = f.read()
# print(s)
# f.close()

f = open("myfile.txt","w")
print("Enter text (type . when you are done)")
s=''
while s !=".":
    s = input()
    f.write(s+"\n")
f.close()
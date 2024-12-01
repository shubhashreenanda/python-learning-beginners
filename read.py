import os,sys

if os.path.isfile('myfile.txt'):
    f=open('myfile.txt','r')
else:
    print('file doesnot exist')
    sys.exit()

s=f.read()
print(s)
f.close()
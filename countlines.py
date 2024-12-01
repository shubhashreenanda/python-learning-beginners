f = open("sample.txt","r")
print(len(f.readlines()))
print(len(f.read().split('\n')))
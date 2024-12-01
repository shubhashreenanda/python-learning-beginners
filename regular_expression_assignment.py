import re
t=int(input())
while(t>0):
    str = input("enter a string")
    pattern=re.search(r'\d+',str)
    if pattern:
        print("true")
    else:
        print("false")
    t=t-1
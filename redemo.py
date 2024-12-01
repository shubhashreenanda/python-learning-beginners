import re

from generator import result

str ="Take up on 1-2-2014 one idea at a time"
result= re.search(r'o\w\w',str)
print(result.group())

result= re.findall(r'o\w\w',str)
print(result)

result= re.match(r'T\w\w',str)
print(result.group())

result= re.sub(r'one','two',str)
print(result)

result= re.findall(r'o\w{1,2}', str)
print(result)

result= re.split(r'\d+', str)
print(result)

result= re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)


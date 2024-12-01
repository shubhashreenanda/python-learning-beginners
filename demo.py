import logging
from logging import Logger

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f=open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    logging.info("division in progress")
    c=a/b
    f.write("writing %d into file" %c)
except ZeroDivisionError:
    print("DIvision by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("division by zero")
else:
    print("you have entered a non zero number")
finally:
    f.close()
    print("file closed")
print("Code after the exception")
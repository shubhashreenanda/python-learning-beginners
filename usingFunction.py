from locale import currency
from threading import current_thread, Thread

from usingFunction import *

def displayNumbers():
    i = 0
    print(current_thread().getName())
    while(i<=10):
        print(i)
        i+=1

print(current_thread().getName())
t = Thread(target = displayNumbers())
t.start()
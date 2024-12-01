from turtledemo.penrose import start

import time
from datetime import date

startTime = time.perf_counter()
ldates = []

d1 = date(2011,8,9)
d2 = date(2062,6,19)
d3 = date(2021,3,29)
d4 = date(2024,1,8)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)

ldates.sort()
#time.sleep(3)
for d in ldates:
    print(d)

endTime = time.perf_counter()
print("Execution Time", endTime-startTime)
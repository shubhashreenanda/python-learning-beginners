from datetime import *

d = date(2024,8,9)
t = time(12,34,56)

dt= datetime.combine(d,t)
print(dt)
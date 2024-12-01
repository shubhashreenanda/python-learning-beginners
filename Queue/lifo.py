import queue

lq = queue.LifoQueue()
lq.put("Python")
lq.put("Java")
lq.put("Docker")
lq.put("Selenium")

print(lq.queue)

while not lq.empty():
    print(lq.get())

print(lq.qsize())
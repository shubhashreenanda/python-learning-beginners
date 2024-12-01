import queue

q = queue.Queue()
q.put("Python")
q.put("Java")
q.put("Docker")
q.put("Selenium")


print(q.queue)
q.queue.clear()

print(q.qsize())

while not q.empty():
    print(q.get())

print(q.qsize())
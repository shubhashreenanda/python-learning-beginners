import queue

q = queue.Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)

while not q.empty():
    print(q.get(), end=' ')

print()

lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)

while not lq.empty():
    print(lq.get(), end=' ')

print()

pq = queue.PriorityQueue()
pq.put(400,"Bharat")
pq.put(100,"Ahmed")
pq.put(500,"Som")
pq.put(50,"Krishna")

while not pq.empty():
    print(pq.get(), end=' ')

print()

import queue
import random
from threading import *

import Queue.my_queue
import time


def producer(q):
    while True:
        print('Producing')
        q.put(random.randint(1,50))
        print('Produced')
        time.sleep(3)

def consumer(q):
    while True:
        print('Ready to consume')
        print('Consume Data:',q.get())
        time.sleep(3)

q = queue.Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()
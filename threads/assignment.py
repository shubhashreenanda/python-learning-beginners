from threading import *


class evennumbers:

    def display(self):
        i = 0

        while i <= 100:
            i += 2

            print(i)


class oddnumbers:

    def display(self):
        i = 1

        while i < 100:
            print(i)

            i += 2


e = evennumbers()

o = oddnumbers()

t1 = Thread(target=e.display)

t2 = Thread(target=o.display)

print("Thread: ", current_thread().name, ". Number: ", e.display())

print("Thread: ", current_thread().name, ". Number: ", o.display())

t1.start()

t2.start()
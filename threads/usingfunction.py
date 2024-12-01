from threading import Thread, current_thread


def displayNumbers():
    i=0
    while(i<=10):
        print(i)
        i+=1

#creating a new thread on its own
print(current_thread().name)
t = Thread(target=displayNumbers)
t.start()
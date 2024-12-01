import threading

print("current thread that is running:",threading.current_thread().name)


if threading.current_thread() == threading.main_thread():
    print("main thread")
else:
    print("some other thread")
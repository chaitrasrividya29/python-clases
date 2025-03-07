import threading
import time

print("the main thread is started")

def first_task():
    print("this is the first sub task")
    time.sleep(2)
    print("first sub task execution started")
    time.sleep(2)
    print("first sub task execution completed")

def second_task():
    print("this is the second sub task")
    time.sleep(2)
    print("second sub task execution started")
    time.sleep(2)
    print("second sub task execution completed")

thread1=threading.Thread(target=first_task)
thread2=threading.Thread(target=second_task)
thread1.start()
print("in between thread1 and thread2")
thread1.join()
thread2.start()
thread2.join()
print("main thread execution completed")


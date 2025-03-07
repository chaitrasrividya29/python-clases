import threading 
import time
import queue

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(i)
        print(f"produced : {i}")
    q.put(None)
    
def comsumer(q):
    while True:
        val=q.get()
        if val is None:
            break
        print(f"consumed : {val}")
        time.sleep(2)

q=queue.Queue()
producer_thread=threading.Thread(target=producer, args=(q,))
consumer_thread=threading.Thread(target=comsumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
print("execution completed")
q.put(None)
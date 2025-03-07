import threading
def get_result(chunk):
    result=sum(chunk)
    print(f"the sum of the chunk : {result}")

data_chunk=[
    list(range(10)),
    list(range(10,20)),
    list(range(20,30))
]
threads=[]

for chunk in data_chunk:
    thread=threading.Thread(target=get_result , args=(chunk, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


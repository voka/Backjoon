from queue import Empty, Queue
queue = Queue()
for i in range(10):
    queue.put([i,i])
while not queue.empty():
    k = queue.get()
    print(k)
    
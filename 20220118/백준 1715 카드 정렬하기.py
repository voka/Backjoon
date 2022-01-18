from sys import stdin 
from queue import PriorityQueue 
N = int(stdin.readline())
que = PriorityQueue()
for i in range(N):
    que.put(int(stdin.readline()))
if N == 1:
    print(0)
elif N == 2:
    print(que.get()+que.get())
else:
    com = 0
    while not que.empty():
        cur = que.get() 
        if not que.empty() :
            cur += que.get()
            if not que.empty() : que.put(cur)
        com += cur
    print(com)
    
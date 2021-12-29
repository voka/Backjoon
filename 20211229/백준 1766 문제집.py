from queue import PriorityQueue
from sys import stdin

N,M = map(int,stdin.readline().split())
indegree = [0]*(N+1)
Nodes = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,stdin.readline().split())
    Nodes[a].append(b)
    indegree[b] += 1
myqueue = PriorityQueue()
for i in range(1,N+1):
    if indegree[i] == 0 :
        myqueue.put(i)
result = []
while myqueue:
    cur = myqueue.get()
    result.append(cur)
    if len(result) == N :
        break
    for i in Nodes[cur]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            myqueue.put(i)
            
for i in result:
    print(i,end = ' ')
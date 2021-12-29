from queue import Queue
from sys import stdin

N,M = map(int,stdin.readline().split())
indegree = [0]*(N+1)
Nodes = [[] for _ in range(N+1)]
for i in range(M):
    Pd_list = list(map(int,stdin.readline().split()))
    num = Pd_list[0]
    for k in range(1,num):
        Nodes[Pd_list[k]].append(Pd_list[k+1])
        indegree[Pd_list[k+1]] += 1
myqueue = Queue()
for i in range(1,N+1):
    if indegree[i] == 0 :
        myqueue.put(i)
result = []
while not myqueue.empty():
    cur = myqueue.get()
    result.append(cur)
    for i in Nodes[cur]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            myqueue.put(i)
if(len(result) != N):
    print(0)
else:          
    for i in result:
        print(i)
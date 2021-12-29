from queue import Queue
from sys import stdin

N = int(stdin.readline())
indegree = [0]*(N+1)
Nodes = [[] for _ in range(N+1)]
times = [0]
dp = [0] * (N+1)
for i in range(N):
    infos = list(map(int,stdin.readline().split()))
    num = infos[1]
    times.append(infos[0])
    for k in range(2,num+2):
        Nodes[infos[k]].append(i+1)
        indegree[i+1] += 1
myqueue = Queue()
for i in range(1,N+1):
    if indegree[i] == 0 :
        myqueue.put(i)
        dp[i] = times[i]
result = []
while not myqueue.empty():
    cur = myqueue.get()
    result.append(cur)
    for i in Nodes[cur]:
        dp[i] = max(dp[i], dp[cur] + times[i])
        indegree[i] -= 1
        if indegree[i] == 0 :
            myqueue.put(i)
            
print(max(dp))
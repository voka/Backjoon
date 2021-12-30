from sys import stdin
from queue import Queue
N,M = map(int,stdin.readline().split())
Nodes = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for i in range(M):
    A,B = map(int,stdin.readline().split())
    Nodes[A].append(B) # tuple 형식으로 넣으면 for문 작성시 편함
    indegree[B] += 1
dp = [0]*(N+1)
que = Queue()
for i in range(1,N+1):
    if(indegree[i]==0):
        que.put(i)
        dp[i] = 1
result = []
# 점화식 -> dp[i] = dp[cur] + 1
while not que.empty():
    cur = que.get()
    for i in Nodes[cur]:
        dp[i] = dp[cur] + 1
        indegree[i] -= 1
        if indegree[i] == 0:
            que.put(i)
for i in range(1,N+1):
    print(dp[i],end=' ')
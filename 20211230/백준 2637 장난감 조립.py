from sys import stdin
from queue import Queue
N = int(stdin.readline())
M = int(stdin.readline())
Nodes = [[]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)
mydict = {}
for i in range(M):
    X,Y,K = map(int,stdin.readline().split())
    Nodes[X].append((Y,K)) # tuple 형식으로 넣으면 for문 작성시 편함
    mydict[X] = 1
    indegree[Y] += 1
que = Queue()
for i in range(1,N+1):
    if(indegree[i]==0):
        que.put(i)
dp = [0 for _ in range(N+1)]
dp[N] = 1
# 점화식 -> dp[i] = dp[i] + dp[cur]*k
while not que.empty():
    cur = que.get()
    for i,k in Nodes[cur]:
        dp[i] += dp[cur]*k
        indegree[i] -= 1
        if indegree[i] == 0:
            que.put(i)
            
for i in range(1,N+1):
    if i not in mydict:
        print("{0} {1}".format(i,dp[i]))
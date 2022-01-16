from sys import stdin 
from queue import Queue
import math

N = int(stdin.readline())
maps = []
graph = [[] for _ in range(N)]
dp = [[math.inf]*(N) for _ in range(N)]

for i in range(N):
    maps.append(list(map(int,stdin.readline().split())))
    for j in range(N):
        if maps[i][j] == 0 : continue
        graph[i].append(j)
        
que = Queue()    
que.put(0)
visited = [[0]*(N) for _ in range(N)]
while not que.empty():
    cur = que.get()
    for next in graph[cur]:
        if visited[cur][next] == 0:
            que.put(next)
            visited[cur][next] = 1
            dp[cur][next] = min(maps[cur][next],dp[cur][next])
"""
    for k in range(N):
        if maps[i][k] != 0:
            dp[i][k] = maps[i][k]
#myQue = Queue.put()
for i in range(N):
    for j in range(N):
        for k in range(i,j):
            dp[i][j] = min(dp[i][k] + dp[k][j],dp[i][j])

for d in dp:
    print(d)
"""
import sys,pprint
from collections import deque
ip = sys.stdin.readline
max_int = 1000000001
n = int(ip())
m = int(ip())
dist = [[max_int]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i] = 0
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,cost = map(int,ip().split())
    if dist[a][b] > cost:
        graph[a].append((b,cost))
        dist[a][b] = cost

traceij = [[-1]*(n+1) for _ in range(n+1)]

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
               dist[i][j] = dist[i][k] + dist[k][j]
               traceij[i][j] = k # k를 구해두면 backtrace에서 사용가능 

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == max_int:
            dist[i][j] = 0
        print(dist[i][j], end = " ")
    print()

def backtrace(start,end):
    if traceij[start][end] == -1:
        return []
    k = traceij[start][end]
    return backtrace(start, k) + [k] + backtrace(k, end)

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == 0:
            print(dist[i][j])
        else:
            temp = [i] + backtrace(i, j) + [j]
            print(len(temp),end=" ")
            print(*temp)
        
            


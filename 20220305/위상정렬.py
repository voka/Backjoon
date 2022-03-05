import sys
from collections import deque
ip = sys.stdin.readline
N,M = map(int,ip().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1) 

for _ in range(M):
    a,b = map(int,ip().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        result.append(cur)
        for g in graph[cur]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    print(*result)

topology_sort()
            

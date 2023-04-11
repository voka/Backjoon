from collections import deque
import sys
ip = sys.stdin.readline


N, M = map(int, ip().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, ip().split())
    graph[a].append(b)
    indegree[b] += 1


def TopologySort():
    result = []
    myque = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            myque.append(i)
    while myque:
        cur = myque.popleft()
        result.append(cur)
        for ne in graph[cur]:
            indegree[ne] -= 1
            if indegree[ne] == 0:
                myque.append(ne)
    print(*result)


TopologySort()

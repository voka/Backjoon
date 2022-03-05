import sys,heapq
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
    q = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q:
        cur = heapq.heappop(q)
        result.append(cur)
        for g in graph[cur]:
            indegree[g] -= 1
            if indegree[g] == 0:
                heapq.heappush(q,g)
    print(*result)

topology_sort()
            

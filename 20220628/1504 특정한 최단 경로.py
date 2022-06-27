from re import L
import sys,heapq,math
ip = sys.stdin.readline
N,E = map(int,ip().split())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a,b,w = map(int,ip().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

v1,v2 = map(int,ip().split())

def di(start,end):
    que = []
    heapq.heappush(que,(0,start))
    distance = [math.inf] * (N+1)
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for cur in graph[now]:
            cost = dist + cur[1]
            if cost < distance[cur[0]]:
                distance[cur[0]] = cost
                heapq.heappush(que, (cost, cur[0]))
    return distance[end]
path1 = di(1,v1) + di(v1,v2) + di(v2,N)
path2 = di(1,v2) + di(v2,v1) + di(v1,N)
answer = min(path1,path2)
if answer >= 1e9:
    print(-1)
else:
    print(answer)

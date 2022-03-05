import sys,heapq
ip = sys.stdin.readline
INF = int(1e9)
V,E = map(int,ip().split())
graph = [[] for _ in range(V+1)]
dis = [INF]*(V+1)
start = int(ip())
dis[start] = 0
for i in range(E):
    u,v,w = map(int,ip().split())
    graph[u].append((v,w))
que = []
heapq.heappush(que,(0,start))
while que:
    dist , now = heapq.heappop(que)
    if dis[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            heapq.heappush(que,(cost,i[0]))

for i in range(1,V+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])



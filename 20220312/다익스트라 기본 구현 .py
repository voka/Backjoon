import sys, heapq 
ip = sys.stdin.readline 
V,E = map(int,ip().split())
start = int(ip())
graph = [[] for _ in range(V+1)]
dist = [1e9]*(V+1)
for i in range(E):
    a,b,d = map(int,ip().split())
    graph[a].append((b,d))

myque = []
heapq.heappush(myque,(0,start))
dist[start] = 0
while myque:
    cur_d, cur = heapq.heappop(myque)
    if dist[cur] < cur_d:
        continue
    for nx,d in graph[cur]:
        cost = cur_d + d
        if cost < dist[nx]:
            dist[nx] = cost
            heapq.heappush(myque,(cost,nx))

for i in range(1,V+1):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])
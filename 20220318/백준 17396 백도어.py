import sys, heapq
INF = sys.maxsize
ip = sys.stdin.readline
V,E = map(int,ip().split())
checking = list(map(int,ip().split()))
graph = [[] for _ in range(V)]
for i in range(E):
    a,b,t = map(int,ip().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
dist = [INF] * (V)
dist[0] = 0
checking[-1] = 0
myque = []
heapq.heappush(myque,(0,0))
while myque:
    cur_dist,cur_v = heapq.heappop(myque)
    if cur_dist > dist[cur_v]:
        continue
    for next_v,next_dist in graph[cur_v]:
        cost = next_dist + cur_dist
        if dist[next_v] > cost and checking[next_v] == 0:
            dist[next_v] = cost
            heapq.heappush(myque,(cost,next_v))
if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])

import sys,heapq
INF = sys.maxsize
ip = sys.stdin.readline
V,E = map(int,ip().split())
graph = [[] for _ in range(V+1)]
dist = [INF]*(V+1)
for i in range(E):
    a,b,c = map(int,ip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
myque = []
heapq.heappush(myque,(0,1))
dist[1] = 0
while myque:
    cur_dist,cur_id = heapq.heappop(myque)
    if dist[cur_id] < cur_dist:# 이미 방문함
        continue
    for next_id,next_dist in graph[cur_id]:
        cost = cur_dist + next_dist
        if dist[next_id] > cost:
            dist[next_id] = cost
            heapq.heappush(myque,(cost,next_id))
print(dist[-1])

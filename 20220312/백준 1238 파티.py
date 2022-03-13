import sys, heapq 
ip = sys.stdin.readline 
V,E,start = map(int,ip().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b,d = map(int,ip().split())
    graph[a].append((b,d))
def di(start,end):
    dist = [1e9]*(V+1)
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
    #print(start,end, dist)
    return dist[end]
max_ = -1
for i in range(1,V+1):
    if start != i:
        max_ = max(max_,di(start,i) + di(i,start))
print(max_)
 
import sys, heapq
ip = sys.stdin.readline 
V,E = map(int,ip().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b,c = map(int,ip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def di(start,end):
    dist = [1e9]*(V+1)
    myque = []
    dist[start] = 0
    heapq.heappush(myque,(0,start))
    while myque:
        cur_d,cur = heapq.heappop(myque)
        if dist[cur] < cur_d:
            continue
        for nx,d in graph[cur]:
            cost = d + cur_d
            if dist[nx] > cost:
                dist[nx] = cost
                heapq.heappush(myque,(cost,nx))
    return dist[end]
v1,v2 = map(int,ip().split())

path1 = di(1,v1) + di(v1,v2) + di(v2,V)
path2 = di(1,v2) + di(v2,v1) + di(v1,V)
answer = min(path1,path2)
if answer >= 1e9:
    print(-1)
else:
    print(answer)
import sys, heapq
ip = sys.stdin.readline 
T = int(ip())
def dijkstra(graph,start,N):
    myque = [(0,start)]
    dist = [1e9]*(N+1)
    dist[start] = 0
    while myque:
        cost,cur = heapq.heappop(myque)
        if dist[cur] < cost:
            continue
        for _next,_cost in graph[cur]:
            tcost = cost + _cost
            if tcost < dist[_next]:
                dist[_next] = tcost 
                heapq.heappush(myque,(tcost,_next))
    return dist
    
while T:
    T-=1
    N,M = map(int,ip().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a,b,c = map(int,ip().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    K = int(ip())
    friends = list(map(int,ip().split()))
    answer = N+1
    min_cost = 1e9
    for i in range(1,N+1):
        temp = dijkstra(graph,i,N)
        tempCost = 0
        for f in friends:
            tempCost += temp[f]
        if min_cost > tempCost:
            answer = i
            min_cost = tempCost
        elif min_cost == tempCost:
            answer = min(answer,i)
    print(answer)    
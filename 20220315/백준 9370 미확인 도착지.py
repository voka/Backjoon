import sys, heapq
ip = sys.stdin.readline 
T = int(ip())
def dijkstra(start):
    dist = [1e9]*(n+1)
    dist[start] = 0
    myque = []
    heapq.heappush(myque,(0,start))
    while myque:
        cur_dist, cur_id = heapq.heappop(myque)
        if dist[cur_id] < cur_dist:
            continue
        for next_id,next_dist in graph[cur_id]:
            cost = cur_dist + next_dist
            if dist[next_id] > cost:
                dist[next_id] = cost
                heapq.heappush(myque,(cost,next_id))
    return dist
for _ in range(T):
    n,m,t = map(int,ip().split())
    s,g,h = map(int,ip().split())
    hubos = []
    graph = [[] for _ in range(n+1)]
    smell = 0
    for i in range(m):
        a,b,d = map(int,ip().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    for i in range(t):
        hubos.append(int(ip()))
    start = dijkstra(s)
    g_start = dijkstra(g)
    h_start = dijkstra(h)
    answer = []
    for hubo in hubos:
        # s -> g -> h -> 후보군  == s -> 후보군 or s -> h -> g -> 후보군 == s ->  후보군 
        if start[g] + g_start[h] + h_start[hubo] == start[hubo] or start[h] + h_start[g] + g_start[hubo] == start[hubo]:
            answer.append(hubo)
    answer.sort()
    print(*answer)
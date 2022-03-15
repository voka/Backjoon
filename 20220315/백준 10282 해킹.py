import sys,heapq
ip = sys.stdin.readline
T = int(ip())
for _ in range(T):
    N,D,start = map(int,ip().split())
    graph = [[] for _ in range(N+1)]
    dist = [1e9]*(N+1)
    for i in range(D):
        a,b,s = map(int,ip().split())
        graph[b].append((a,s))
    myque = []
    dist[start] = 0
    heapq.heappush(myque,((0,start)))
    answer = 0
    total_time = -1
    while myque:
        cur_s,a = heapq.heappop(myque)
        if dist[a] < cur_s:
            continue
        for next_id,useTime in graph[a]:
            if cur_s + useTime < dist[next_id] :
                dist[next_id] = cur_s + useTime
                heapq.heappush(myque,(dist[next_id],next_id))
    for d in dist:
        if d != 1e9:
            answer += 1
            total_time = max(total_time,d)

    print(answer,total_time)

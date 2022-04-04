import sys,heapq
ip = sys.stdin.readline 
n = int(ip())
m = int(ip())

myque = []

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,ip().split())
    graph[a].append((b,c))
    
    
start,end = map(int,ip().split())

dist = [1e9]*(n+1)
trace = [0]*(n+1)

heapq.heappush(myque, (0,start))
while myque:
    cost,cur = heapq.heappop(myque)
    if dist[cur] < cost:
        continue
    for next_i,cost_i in graph[cur]:
        curcost = cost_i + cost
        if dist[next_i] > curcost:
            dist[next_i] = curcost
            trace[next_i] = cur
            heapq.heappush(myque, (curcost,next_i))

answer = []
tmp = end
while tmp != start: # 여기 True로 하고 trace[tmp] == 0 : break 하면 메모리 초과 발생함 .. 
    answer.append(tmp)
    tmp = trace[tmp]    
answer.append(start)
answer.reverse()
"""
# 재귀함수 방법은 메모리 초과 남 ..
def backtrace(end):
    if trace[end] == 0:
        return []
    k = trace[end]
    return [k] + backtrace(k)
"""
#print(trace)
#print(dist)
print(dist[end])
print(len(answer))
print(*answer)

from queue import Empty, Queue
from sys import stdin
que = Queue()

N = int(stdin.readline())
M = int(stdin.readline())
graph = [[]*(N+1) for _ in range(N+1)]
back_graph = [[]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(M):
    p,q,r = map(int,stdin.readline().split())
    graph[p].append((q,r))
    back_graph[q].append((p,r))
    indegree[q] += 1

que.put(1) # 시작은 1번 노드부터
dp = [0]*(N+1) # 
checking = [0]*(N+1)
#print(graph,indegree)
while not que.empty():
    if(checking[1] == 1): # 1번 노드를 재방문 할 경우 종료 
        break
    cur = que.get()
    for i,q in graph[cur]:
        indegree[i] -= 1 
        dp[i] = max(dp[i],dp[cur] + q)
        if indegree[i] == 0 and checking[i]==0:
            checking[i] = 1
            que.put(i)
#print(result,dp)
que.put(1)
final_result = [1]
checking = [0]*(N+1)
while not que.empty():
    cur = que.get()
    for i,q in back_graph[cur]:
        if dp[cur] - dp[i] == q and checking[i]==0:
            checking[i] = 1
            final_result.append(i)
            que.put(i)
final_result.append(1)
final_result.reverse()

print(max(dp))
for i in final_result:
    print(i,end = " ")
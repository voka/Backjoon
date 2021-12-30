from queue import Queue
from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
Nodes = [[]*(N+1) for _ in range(N+1)]
inverse_Nodes = [[]*(N+1) for _ in range(N+1)]
indegree = [0]*(N+1)
cur_time = {}
for i in range(M):
    a,b,t = map(int,stdin.readline().split())
    Nodes[a].append((b,t))
    inverse_Nodes[b].append((a,t))
    indegree[b] += 1
start,end =  map(int,stdin.readline().split())
que = Queue()
que.put(start)
result = []
for i in range(N+1):
    cur_time[i] = 0
while not que.empty(): # 최장시간 탐색
    cur = que.get()
    result.append(cur)
    for i,t in Nodes[cur]:
        indegree[i] -= 1
        # 최종 시간  -> if문 안에 안들어가는 이유 : 관계가 있는 모든 점들에 대해 시간을 업데이트 해줘야하기 때문
        cur_time[i] = max(cur_time[i], cur_time[cur] + t)
        if(indegree[i] == 0):
            que.put(i)

# 거쳐간 간선을 세기 위한 백트래킹 시작
bridge = 0
checking = [0]*(N+1)
que.put(end)
while not que.empty():
    cur = que.get()
    for i,t in inverse_Nodes[cur]: # 역방향 그래프에서 탐색
        # 위상정렬로 구한 결과(cur_time)를 사용해  
        # cur과 i 사이의 비용을 계산해 그 비용이 간선비용과 같으면 지나간 도로로 판정
        if cur_time[cur] - cur_time[i] == t:
            bridge += 1
            if checking[i] == 0:
                que.put(i)
                checking[i] = 1

print(cur_time[end],bridge)
# 1->2->6->7 : 4 + 3 + 5 => 12
# 1->3->5->6->7 : 2 + 1 + 2 + 5 -> 10
# 1->4->6->7 : 3 + 4 + 5 => 12
import sys
from collections import deque
ip = sys.stdin.readline
N, M = map(int, ip().split())
king = ip().strip()
graph = {}
parent = {}
value = {}
for i in range(N):
    child, f, m = map(str, ip().split())
    graph[child] = (f, m)
    if f in parent:
        parent[f].append(child)
    else:
        parent[f] = [child]
    if m in parent:
        parent[m].append(child)
    else:
        parent[m] = [child]
    value[f] = 0
    value[m] = 0
    value[child] = 0

score = float(1)
value[king] = score
myque = deque()
myque.append((king, score))
visited = {}
visited[king] = 1
while myque:  # 왕의 자식부터 시작해 모든 왕족에게 혈통값 부여하기
    cur, score = myque.popleft()
    for c in parent[cur]:
        value[c] = score/2
        if c in parent and c not in visited:
            myque.append((c, score/2))
            visited[c] = 1
# print(graph)
for child in graph:  # 모든 자식들의 값을 부모의 혈통값을 더해 2로 나누어 구함
    f, m = graph[child]
    value[child] = (value[f] + value[m])/2
max_answer = -1
# print(value)
for i in range(M):  # 혈통값 제일 큰놈 구함
    cur = str(ip().rstrip())
    if cur in value:
        if max_answer < value[cur]:
            answer = cur
            max_answer = value[cur]
print(answer)

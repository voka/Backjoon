# 해당 문제의 핵심은 Cost가 작은 놈들이 부모가 되는 것 !
import sys
ip = sys.stdin.readline
N,M,K = map(int,ip().split())
parents = [i for i in range(N+1)]
costs = list(map(int,ip().split()))
costs.insert(0,0)
def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union_parent(a,b):
  pOa = find_parent(a)
  pOb = find_parent(b)
  if costs[pOa] > costs[pOb]: # Cost가 작은 친구들이 부모가 되어야 한다. !!!!!
    parents[pOa] = pOb 
  else:
    parents[pOb] = pOa
for i in range(M):
  a,b = map(int,ip().split())
  if find_parent(a) != find_parent(b):
    union_parent(a,b)
answer = 0
rests = list(set(parents[1:]))
rests.sort(key = lambda x : costs[x]) # Cost가 작은 부모부터 시작해야함
keys = []
for p in rests:
  if find_parent(p) not in keys: # 해당 노드의 부터가 이미 keys안에 존재하면 그 노드의 비용은 더하지 않아야 한다.
    keys.append(p)
    answer += costs[p]
print(answer if answer <= K else "Oh no")

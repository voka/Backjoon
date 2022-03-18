import sys 
ip = sys.stdin.readline
N,M = map(int,ip().split())
parent = [i for i in range(N+1)]
def find_parent(x):
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
edges = []
for i in range(M):
    a,b,cost = map(int,ip().split())
    edges.append((cost,a,b))
edges.sort()
answer = 0
total = 0
count = 1
for cost,a,b in edges:
    total += cost
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        answer += cost
        count += 1
if count != N:
    print(-1)
else:
    print(total - answer)
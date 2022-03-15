import sys 
ip = sys.stdin.readline 
N = int(ip())
E = N*N
parent = [i for i in range(N+1)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges = []
for i in range(N):
    lines = list(map(int,ip().split()))
    for j in range(N):
        edges.append((lines[j],i,j))
edges.sort()
answer = 0
for cost,a,b in edges:
    if find_parent(a) != find_parent(b):
        answer += cost
        union_parent(a,b)
print(answer)

import sys
ip = sys.stdin.readline
V = int(ip())
E = int(ip())

parent = [i for i in range(V+1)]
Edges = []
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(E):
    a,b,w = map(int,ip().split())
    Edges.append((w,a,b))
Edges.sort()
answer = 0
for e in Edges:
    w,a,b = e
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        answer += w

print(answer)
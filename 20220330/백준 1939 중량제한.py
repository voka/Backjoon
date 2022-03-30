import sys
ip = sys.stdin.readline 
N,M = map(int, ip().split())
parent = [i for i in range(N+1)]
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
graph = []
for _ in range(M):
    A,B,C = map(int,ip().split())
    graph.append((-C,A,B))
graph.sort()

LA,LB = map(int,ip().split()) 
for path in graph: # 다익스트라
       c,a,b = path
       c = abs(c)
       union_parent(a, b)
       if find_parent(LA) == find_parent(LB):
           print(c)
           exit()
           
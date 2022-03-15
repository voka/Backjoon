import sys
ip = sys.stdin.readline 
while True:
    V,E = map(int,ip().split())
    parent = [i for i in range(V)]
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
    if V == E == 0 :
        break
    edges = []
    original = 0
    for i in range(E):
        X,Y,Z = map(int,ip().split())
        original += Z
        edges.append((Z,X,Y))
        edges.append((Z,Y,X))
    edges.sort()
    result = 0
    for cost,a,b in edges:
        if find_parent(a) != find_parent(b):
            union_parent(a,b)
            result += cost
    print(original-result)

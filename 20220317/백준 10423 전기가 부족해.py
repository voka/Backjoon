import sys
ip = sys.stdin.readline 
N,M,K = map(int,ip().split())
batterys = list(map(int,ip().split()))
parent = [i for i in range(N+1)]
def find_parent(x):
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a in batterys and b not in batterys:
        parent[b] = a
    elif b in batterys and a not in batterys:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
def same_parent(a,b):
    fa = find_parent(a)
    fb = find_parent(b)
    if fa in batterys and fb in batterys : return True
    else: return fa == fb
edges = []
for i in range(M):
    u,v,w = map(int,ip().split())
    edges.append((w,u,v))
edges.sort()
answer = 0
for cost,s,e in edges:
    if (same_parent(s,e) != True):
        union_parent(s,e)
        answer += cost
print(answer)
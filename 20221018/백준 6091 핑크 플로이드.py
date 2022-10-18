import sys 
ip = sys.stdin.readline

N = int(ip())

parent = [i for i in range(N+1)]

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


for i in range(1,N):
    costs = list(map(int,ip().split()))
    for j in range(i+1,N+1):
        Edges.append((costs[j-i-1],i,j))
Edges.sort()

j_dict = {i : [] for i in range(1,N+1)}

for e in Edges:
    w,a,b = e
    if find_parent(a) != find_parent(b):
        j_dict[b].append(a)
        j_dict[a].append(b)
        union_parent(a,b)

for key in j_dict.keys():
    j_dict[key].sort()
    result = j_dict[key]
    print(len(result), *result)
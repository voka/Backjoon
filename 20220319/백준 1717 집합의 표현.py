import sys
sys.setrecursionlimit(10**5)
ip = sys.stdin.readline 
n,m = map(int,ip().split())
parent = [i for i in range(n+1)]
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


for i in range(m):
    command,a,b = map(int,ip().split())
    if command == 0 :
        if find_parent(a) != find_parent(b):
            union_parent(a,b)
    elif command == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

import sys
ip = sys.stdin.readline 
V,E = map(int,ip().split())
parent = [i for i in range(1001)]
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
def process(earray):
    ans = 0
    for c,a,b  in earray:
        if find_parent(a) != find_parent(b):
            union_parent(a,b)
            ans += c
    return ans

edges = []
for i in range(E+1):
    a,b,c = map(int,ip().split())
    C = 1 if c == 0 else 0 
    edges.append((C,a,b))
edges.sort()
ans1 = process(edges)
edges.reverse()
parent = [i for i in range(1001)]
ans2 = process(edges)
print(ans2*ans2-ans1*ans1)
# 0이 오르막길임 ㅇ
# 문제를 똑바로 읽자고 ㅋ

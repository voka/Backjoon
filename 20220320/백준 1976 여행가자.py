import sys
ip = sys.stdin.readline 
N = int(ip())
M = int(ip())
parent = [i for i in range(N+1)]
infos = []
for i in range(N):
    checks = list(map(int,ip().split()))
    for j in range(N):
        check = checks[j]
        if check == 1:
            infos.append((i+1,j+1))
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    fa = find_parent(a)
    fb = find_parent(b)
    if fa < fb:
        parent[fb] = fa
    else:
        parent[fa] = fb

for a,b in infos:
    if find_parent(a) != find_parent(b):
        union_parent(a,b)

course = list(map(int,ip().split()))
fc = find_parent(course[0])
answer = "YES"
for c in course:
    if fc != find_parent(c):
        answer = "NO"
        break
print(answer)
        
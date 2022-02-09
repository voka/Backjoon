import sys
K,N,F = map(int,sys.stdin.readline().split())
graph = [[0 for j in range(N+1)] for _ in range(N+1)]
group = []
for f in range(F):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
#print(graph)
def DFS(f):
    if len(group) == 0:
        group.append(f)
    else:
        for i in group:
            if graph[i][f] == 0:
                return 
        group.append(f)
        return
    for j in range(1,N):
        if f == j : continue
        if graph[f][j] == 1:
            DFS(j)
for i in range(1,N+1):
    DFS(i)
    if len(group) < K :
        group.clear()
    else:
        k = group[:K]
        k.sort()
        for t in k:
            print(t)
        exit()
print(-1)




import sys,math,pprint
ip = sys.stdin.readline 
N,M = map(int,ip().split())
dist = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,ip().split())
    dist[a][b] = 1
#pprint.pprint(dist)
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (dist[i][k] and dist[k][j]):
                dist[i][j] = 1
answer = 0
#pprint.pprint(dist)
for i in range(1,N+1):
    flag = True
    for j in range(1,N+1):
        if i != j and dist[i][j] == 0 and dist[j][i] == 0:
            #print(i,j)
            flag = False
            break
    if flag:
        answer += 1     
print(answer)        
import sys,math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

dp = [[math.inf]*(N) for _ in range(N)]
for i in range(M):
    a,b,w = map(int,sys.stdin.readline().split())
    dp[a-1][b-1] = min(w,dp[a-1][b-1])
    
for k in range(N):
    for j in range(N):
        for i in range(N):
            if i == j :
                dp[i][j] = 0
            else :
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
for i in dp:
    for j in i:
        if j == math.inf:
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()
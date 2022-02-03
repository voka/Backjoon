import sys,math

N = int(sys.stdin.readline())

dp = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for j in range(N):
        for i in range(N):
            if dp[i][k] == 1 and dp[k][j] == 1:
                dp[i][j] = 1
for i in dp:
    print(*i)
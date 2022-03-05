import sys
ip = sys.stdin.readline
T = int(ip())
while T:
    T-=1
    n,m = map(int,ip().split())
    Golds = list(map(int,ip().split()))
    maps = [[Golds[i*4 + j] for j in range(m)] for i in range(n)]
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        dp[i][0] = maps[i][0]
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j],max(dp[i][j-1],dp[i+1][j-1]) + maps[i][j] )
            elif i == n-1:
                dp[i][j] = max(dp[i][j],max(dp[i][j-1],dp[i-1][j-1]) + maps[i][j] )
            else:
                dp[i][j] = max(dp[i][j],max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1]) + maps[i][j] )
            
            # for a in range(n):
            #     for b in range(m):
            #         print(dp[a][b],end = " ")
            #     print()
            # print("====================")
    answer = 0
    for i in range(n):
        answer = max(answer,dp[i][m-1])
    print(answer)

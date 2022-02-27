import sys
ip = sys.stdin.readlines
lines = ip()
for line in lines:
    N = int(line)
    if N == 0:
        print(1)
    elif N == 1:
        print(1)
    else:
        dp = [[0]*(N+1) for _ in range(N+1)]
        dp[1][1] = 1
        dp[2][1] = 1
        dp[2][0] = 2
        for i in range(3,N+1):
            dp[i][1] = sum(dp[i-1])
            dp[i][0] = sum(dp[i-2])*2
        print(sum(dp[N]))
    
    
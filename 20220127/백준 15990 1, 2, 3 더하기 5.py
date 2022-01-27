import sys

T = int(input())
Ns = []
for i in range(T):
    Ns.append(int(sys.stdin.readline()))
N = max(Ns)
dp = [[0]*4 for _ in range(N+1)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
#dp[4] = [0,2,0,1]
for i in range(4,N+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009
for i in Ns:
    print(sum(dp[i])% 1000000009)


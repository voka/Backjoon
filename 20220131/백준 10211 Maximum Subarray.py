import sys,math,pprint
def main():
    N = int(sys.stdin.readline())
    X = list(map(int,sys.stdin.readline().split()))
    dp = [[-math.inf]*(N+1) for _ in range(N+1)]
    maxnum = -math.inf
    for i in range(N):
        dp[i][i] = X[i]
        for j in range(i+1,N):
            if dp[i][j-1] + X[j] >= X[j] :
                dp[i][j] = dp[i][j-1] + X[j]
            else:
                dp[i][j] = X[j]
            maxnum = max(maxnum,dp[i][j])
        maxnum = max(maxnum,dp[i][i])
                
    #pprint.pprint(dp)
    print(maxnum)
                
T = int(input())
for _ in range(T) : main()


from sys import stdin 
n,m = map(int,stdin.readline().split())

dp = [[]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    temp = list(map(int,stdin.readline().split()))
    temp.insert(0,0)
    dp[i] = temp[:]
    
dp[0] = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
       
#for i in dp:
    #print(i) 
for i in range(m):
    sx,sy,ex,ey = map(int,stdin.readline().split())
    answer = dp[ex][ey] - dp[sx-1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1]
    #print(dp[ex][ey],dp[sx-1][ey],dp[ex][sy-1],dp[sx-1][sy-1]) 
    print(answer)
"""
1 2 3
1 2 3
1 2 3

1 3 6
2 6 6 + 6 + 3 -3 =12
3 9 6 + 9 + 3 - 6 = 18      
"""
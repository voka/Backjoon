import sys
N = int(sys.stdin.readline())
dp = [0]*(1001)
dp[1] = 1
dp[3] = 1
dp[4] = 1
for i in range(5,N+1):
    if (dp[i-1]+dp[i-3]+dp[i-4]) == 3:
        dp[i] = 0
    else:
        dp[i] = 1
    #print(i,dp[i])
if dp[N] == 0:
    print("CY")
else:
    print("SK")    

""" 
1 : 1 상근
1 -1 -1 
2 : 1,1  창영
1 -1 -1
3 : 1,1,1 상근

4 : 3,1 창영
5 : 3,1,1 상근
4,1
3,1,1
1,1,1,1,1
6 : 
7 : 1,4, -> 창영
8 : 

dp[1][1] = 1
dp[1][3] = -1
dp[1][4] = -1
dp[2][]
dp[i][1]
rest >= 4
dp[i+1][3] = dp[i]
dp[i][4]


"""

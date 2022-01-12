# T초에 1번 나무에 있을떄, 
# dp[T][1] = (dp[T-1][0][0] + 1,c+1)
# dp[T][0] = (dp[T-1][1][0] + 1,c+1)
# T초에 움직이지 않을 때 
# dp[T][0] = (dp[T-1][0][0]+1,c)
from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
T,W = map(int,stdin.readline().split())
dp = [[0]*(W+1) for _ in range(T+1)]
num = [0]  
for i in range(T):
    num.append(int(stdin.readline()))
#print(dp,num)
for i in range(1,T+1):
    for j in range(W+1):
        if j == 0 :
            if num[i] == 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]
        else: # 1번 나무에서 먹기 위해서는 짝수번 카운트를 해야하고 2번 나무에서 먹기 위해서는 홀수번 카운트가ㅏ 되어야 한다. 
            if num[i] == 1 and j%2 == 0: # 가만히 있었을때, 움직여서 먹을때 
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) +1
            elif num[i] == 2 and j%2 == 1: # 가만히 있었을때, 움직여서 먹을때 
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
            else: # 움직여서 못먹거나 안움직여서 못먹을떄 
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])
            
        
print(max(dp[T])) 

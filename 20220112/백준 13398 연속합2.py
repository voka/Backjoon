from sys import stdin 
N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [[0]*2 for _ in range(N)]
#dp[i][0] # 특정원소 제거 X 한 경우
#dp[i][1] # 특정원소 제거한 경우
dp[0][0] = nums[0]
answer = nums[0]
for i in range(1,N):
    # 제거 안한 경우
    dp[i][0] = max(dp[i-1][0] + nums[i],nums[i])
    
    # 제거 한 경우
    # 1. i번째 원소를 제거하는 경우
    # 2. 그 이전에 이미 원소를 제거 했던 경우 
    dp[i][1] = max(dp[i-1][0],dp[i-1][1]+nums[i])
    
    answer = max(answer,max(dp[i]))
    
print(answer)
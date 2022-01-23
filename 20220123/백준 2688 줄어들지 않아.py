# 1 : 9, 2 : 8 3:7 -> i : 10-i
"""  
dp[0] = 0
dp[1] = 10
dp[2] = 55
dp[3] = 
"""
def solution(N):
    nums = [1 for _ in range(10)]
    for _ in range(N-1):
        for last_num in range(1,10):
            nums[last_num] += nums[last_num-1] 
    print(sum(nums))

T = int(input())
for _ in range(T): solution(int(input()))
"""
1 3 6 10 15 21 28 36 45 55 

"""
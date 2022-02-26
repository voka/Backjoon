import sys
ip = sys.stdin.readline
N, K = map(int,ip().split())
nums = list(map(int,ip().split()))
nums.insert(0,0)
for i in range(1,N):
    nums[i+1] += nums[i]
max_ = -100 * 100001
for i in range(N-K+1):
    j = i + K
    max_ = max(max_,nums[j] - nums[i])
print(max_)
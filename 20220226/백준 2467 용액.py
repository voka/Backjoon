import sys
ip = sys.stdin.readline
N = int(ip())
nums = list(map(int,ip().split()))
i = 0
j = N-1
min_i,min_j,min_ = 0,0,2000000001
while i < j:
    cur = nums[i] + nums[j]
    if min_ > abs(cur):
        min_ = abs(cur)
        min_i = nums[i]
        min_j = nums[j]
    if cur == 0:
        print(nums[i],nums[j])
        exit()
    elif cur < 0:
        i += 1
    else:
        j -= 1
print(min_i,min_j)    
            
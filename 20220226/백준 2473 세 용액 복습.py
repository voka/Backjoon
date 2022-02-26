import sys
ip = sys.stdin.readline
N = int(ip())
nums = list(map(int,ip().split()))
nums.sort()
#print(nums)
min_i,min_j,min_k,min_ = 0,0,0,3000000001
for i in range(N-2):
    j = i + 1
    k = N-1
    while j < k:
        cur = nums[i] + nums[j] + nums[k]
        if min_ > abs(cur):
            min_i = nums[i]
            min_j = nums[j]
            min_k = nums[k]
            min_ = abs(cur)
        if cur == 0 :
            print(nums[i],nums[j],nums[k])
            exit()
        elif cur < 0:
            j += 1
        else:
            k -= 1
print(min_i,min_j,min_k)
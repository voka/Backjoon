import sys
ip = sys.stdin.readline
N,S = map(int,ip().split())
nums = list(map(int,ip().split()))
nums.insert(0,0)
#print(nums)
for i in range(1,N+1):
    nums[i] += nums[i-1]

#print(len(nums))

i = 0
j = 1
min_lenght = N+1
while i != N:
    if nums[j] - nums[i] >= S:
        if j - i < min_lenght:
            min_lenght = j - i
        i += 1
    else:
        if j != N:
            j += 1
        else:
            i += 1
if min_lenght == N+1:
    print(0)
else:
    print(min_lenght)
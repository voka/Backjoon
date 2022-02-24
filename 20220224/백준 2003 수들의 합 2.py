import sys
ip = sys.stdin.readline
N,M = map(int,ip().split())
nums = list(map(int,ip().split()))
i = 0
j = 0
answer = 0
min_lenght = N
while True:
    if i > N or i > j:
        break
    cur = sum(nums[i:j])
    if cur >= M:
        answer += 1
        i += 1
    elif cur < M :
        if j < N : j += 1
        else: break
    else:
        i += 1    
print(answer)
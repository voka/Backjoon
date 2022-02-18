from re import I
import sys
ip = sys.stdin.readline
N = int(ip())
nums = list(map(int,ip().split()))
X = int(ip())
nums.sort()
i = 0
j = N-1
answer = 0
while True:
    if i >= j :
        break
    cur = nums[i] + nums[j]
    if cur == X:
        answer += 1
        i += 1 
        j -= 1
    elif cur < X:
        i += 1
    else:
        j -= 1
print(answer)
        
        
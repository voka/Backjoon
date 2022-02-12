import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
check = [100001 for _ in range(100001)]
dp = [0 for _ in range(1000001)]
myque = deque()
myque.append(N)
answer = 0
check[N] = 0
while myque:
    cur = myque.popleft()
    if cur == K:
        answer += 1
    for n in (cur+1,cur-1,cur*2):
        if -1 < n < 100001 and check[n] >= check[cur] + 1:
            check[n] = check[cur] + 1
            myque.append(n)

print(check[K])
print(answer)             
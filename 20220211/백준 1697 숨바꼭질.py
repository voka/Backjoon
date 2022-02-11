import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
check = [-1 for _ in range(100001)]
myque = deque()
myque.append(N)
check[N] = 0
while myque:
    cur = myque.popleft()
    if cur == K:
        print(check[cur])
    for n in (cur+1,cur-1,cur*2):
        if -1 < n < 100001 and check[n] == -1:
            check[n] = check[cur] + 1
            myque.append(n)

             
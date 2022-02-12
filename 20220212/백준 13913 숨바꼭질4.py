from importlib.resources import path
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
        break
    for n in (cur+1,cur-1,cur*2):
        if -1 < n < 100001 and check[n] == -1:
            check[n] = check[cur] + 1
            myque.append(n)
answer = check[K]
print(answer)
paths = deque()
cur = K
paths.append(cur)
#answer -= 1
while answer:
    if cur%2 == 0:
        if check[cur//2] + 1 == check[cur]:
            cur = cur//2
            paths.appendleft(cur)
            answer -= 1
            continue
    for n in (cur+1,cur-1):
        if check[n] + 1 == check[cur]:
            cur = n 
            paths.appendleft(cur)
            answer -= 1
            break
print(*paths)    
        
        
             
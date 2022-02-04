import sys,pprint
from collections import deque
M,N,H = map(int,sys.stdin.readline().split())
dp = [[[0]*M for __ in range(N)] for _ in range(H)]
#pprint.pprint(dp)
myque = deque()
zero_count = 0
for h in range(H):
    for n in range(N):
        temp = list(map(int,sys.stdin.readline().split()))
        for m in range(M):
            if temp[m] == 1 :
                myque.append((h,n,m))
            elif temp[m] == 0:
                zero_count += 1
            dp[h][n][m] = temp[m]
            
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
day = 0
if zero_count == 0:
    print(0)
    exit()
else:
   
    while True:
        cur = len(myque)
        for _ in range(cur):
            h,n,m = myque.popleft()
            for j in range(6):
                nh,nn,nm = h+dz[j],n+dy[j],m+dx[j]
                if nh < 0 or nn < 0 or nm < 0 or nh >= H or nn >= N or nm >= M:
                    continue
                #if dp[nh][nn][nm] == 1 or dp[nh][nn][nm] == -1:
                #    continue
                if dp[nh][nn][nm] == 0:
                    zero_count -= 1
                    dp[nh][nn][nm] = 1
                    myque.append((nh,nn,nm))
        if len(myque) == 0:
            break
        day += 1
#pprint.pprint(dp)
if zero_count == 0:
    print(day)
else:
    print(-1)

#print(zero_count,day)
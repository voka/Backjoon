import sys,pprint
from collections import deque
m, n, o, p, q, r, s, t, u, v, w = map(int,sys.stdin.readline().split())
zero_count = 0
myque = deque()
dp = [
    [
        [
            [
                [
                    [
                        [
                            [
                                [
                                    [
                                        [0]*m for b in range(n)
                                    ] for c in range(o)
                                ] for d in range(p)
                            ] for e in range(q)
                        ] for f in range(r)
                    ] for g in range(s)
                ] for h in range(t)
            ] for i in range(u)
        ] for j in range(v)
    ] for k in range(w)
]
#print(dp)
for k in range(w):
    for j in range(v):
        for i in range(u):
            for h in range(t):
                for g in range(s):
                    for f in range(r):
                        for e in range(q):
                            for d in range(p):
                                for c in range(o):
                                    for b in range(n):
                                        temp = list(map(int,sys.stdin.readline().split()))
                                        for a in range(m):
                                            if temp[a] == 1 :
                                                myque.append((k,j,i,h,g,f,e,d,c,b,a))
                                            elif temp[a] == 0:
                                                zero_count += 1
                                            dp[k][j][i][h][g][f][e][d][c][b][a] = temp[a]
                  
            
da = [1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
db = [0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dc = [0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd = [0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
de = [0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0]
df = [0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0]
dg = [0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0]
dh = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0]
di = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0]
dj = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0]
dk = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1]
#print(myque)
day = 0
if zero_count == 0:
    print(0)
    exit()
else:
    while True:
        cur = len(myque)
        for _ in range(cur):
            k,j,i,h,g,f,e,d,c,b,a = myque.popleft()
            for l in range(22):
                nk,nj,ni,nh,ng,nf,ne,nd,nc,nb,na = k + dk[l],j + dj[l],i + di[l],h + dh[l],g + dg[l],f + df[l],e + de[l],d + dd[l],c + dc[l],b + db[l],a + da[l]
                #print(nk,nj,ni,nh,ng,nf,ne,nd,nc,nb,na)
                if  (0 <= na < m) & (0 <= nb < n) & (0 <= nc < o) & (0 <= nd < p) & (0 <= ne < q) & (0 <= nf < r) & (0 <= ng < s) & (0 <= nh < t) & (0 <= ni < u) & (0 <= nj < v) & (0 <= nk < w) :
                    if dp[nk][nj][ni][nh][ng][nf][ne][nd][nc][nb][na] == 0:
                        zero_count -= 1
                        dp[nk][nj][ni][nh][ng][nf][ne][nd][nc][nb][na] = 1
                        myque.append((nk,nj,ni,nh,ng,nf,ne,nd,nc,nb,na))
        if len(myque) == 0:
            break
        day += 1
#pprint.pprint(dp)
if zero_count == 0:
    print(day)
else:
    print(-1)

#print(zero_count,day)
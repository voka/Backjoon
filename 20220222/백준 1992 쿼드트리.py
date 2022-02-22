import sys
ip = sys.stdin.readline
N = int(ip())
maps = [[0 for __ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    tmp = ip().strip()
    for j in range(N):
        maps[i+1][j+1] = int(tmp[j])
#print(maps)

def divideAndExecute(sx,sy,ex,ey):
    #print(sx,sy,ex,ey)
    cur = maps[sx][sy]
    for x in range(sx,ex):
        for y in range(sy,ey):
            if maps[x][y] == cur:
                continue
            else:
                midx = (sx+ex)//2
                midy = (sy+ey)//2
                return "(" + divideAndExecute(sx,sy,midx,midy) + divideAndExecute(sx,midy,midx,ey)+ divideAndExecute(midx,sy,ex,midy)  + divideAndExecute(midx,midy,ex,ey) + ")"
    return str(cur)
print(divideAndExecute(1,1,N+1,N+1))
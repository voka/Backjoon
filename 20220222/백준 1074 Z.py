import sys,pprint
sys.setrecursionlimit(1000000)
ip = sys.stdin.readline
N,r,c = map(int,ip().split())
N = pow(2,N)
#print(N)
count = 0
dx = [0,0,1,1]
dy = [0,1,0,1]
def find_rc(sx,sy,ex,ey):
    global count
    if (ex-sx)*(ey-sy) == 4:
        #print(count)
        for n in range(4):
            nx = sx+dx[n]
            ny = sy+dy[n]
            count += 1
            if nx == r+1 and ny == c+1:
                print(count-1)
                exit()
    else:
        midx = (sx+ex)//2
        midy = (sy+ey)//2
        if sx <= r+1 < midx:
            if sy <= c+1 <midy:
                find_rc(sx,sy,midx,midy)
            else:
                count += (midx - sx)*(midy-sy)
                find_rc(sx,midy,midx,ey)
        else:
            if sy <= c+1 < midy:
                count += (ex - sx)*(midy-sy)
                find_rc(midx,sy,ex,midy) 
            else:
                count += (midx - sx)*(midy-sy)
                count += (ex - sx)*(midy-sy)
                find_rc(midx,midy,ex,ey)
        
find_rc(1,1,N+1,N+1)
#pprint.pprint(maps)
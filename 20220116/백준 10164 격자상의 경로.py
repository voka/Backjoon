
N,M,K = map(int,input().split())
maps = [[M*(i-1) + j for j in range(1,M+1)] for i in range(1,N+1)]
#print(maps)
dp = [[1]*(M) for _ in range(N) ]
def find_way(ex,ey):
    for i in range(1,ey):
        for j in range(1,ex):
            # 왼쪽에서 오는 경우의 수 + 위쪽에서 오는 경우의 수 
            dp[i][j] = dp[i][j-1] + dp[i-1][j] 
    #for i in dp:
    #    print(i)
""" from queue import Queue
    Queue 버전 - 시간초과
    myque = Queue()
    myque.put((sx,sy))
    while not myque.empty():
        cx,cy = myque.get()
        if cy == 0:
            dp[cy][cx] = 1
        elif cx == 0:
            dp[cy][cx] = 1
        else:
            dp[cy][cx] = max(dp[cy][cx],dp[cy-1][cx] + dp[cy][cx-1])
        nx,ny = cx+1,cy+1
        if nx <= ex:
            myque.put((nx,cy))
        if ny <= ey:
            myque.put((cx,ny))
"""
if K == 0:
    find_way(M,N)
    answer = dp[N-1][M-1]
else:
    mid_y = int((K-1)/M)
    mid_x = K - mid_y*M -1 
    dif_x = M - mid_x - 1
    dif_y = N - mid_y - 1
    #print(mid_x,mid_y,dif_x,dif_y)
    # 0,0 에서 중간점 까지 좌표와 중간점에서 M,N 까지의 좌표를 비교해서 큰 좌표까지만 dp 수행 
    find_way(max(mid_x,dif_x)+1,max(mid_y,dif_y)+1)
    answer = dp[mid_y][mid_x] * dp[dif_y][dif_x]
    #print(mid_y,mid_x)
    #print(maps[mid_y][mid_x])
print(answer)

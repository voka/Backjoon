import sys,bisect
ip = sys.stdin.readline 
N, H = map(int,ip().split())
bottom,top = [],[]
for i in range(N//2):
    bottom.append(int(ip()))
    top.append(int(ip()))
bottom.sort()
top.sort()

cur_min = N + 1
answer = -1
for i in range(1,H+1):
    #print(top,bottom)
    up = bisect.bisect_left(top, i)
    down = bisect.bisect_left(bottom, H - i + 1)
    #print(i,H-i)
    #print(i, N - up - down,up,down)
    cur = N - up - down
    #print(cur,cur_min)
    if cur_min > cur:
        cur_min = cur
        answer = 1
    elif cur_min == cur:
        answer += 1
        
print(cur_min,answer)
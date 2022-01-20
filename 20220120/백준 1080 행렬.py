from sys import stdin 
N,M = map(int,stdin.readline().split())

maps = [list(map(int,list(stdin.readline().strip()))) for _ in range(N)]
target = [list(map(int,list(stdin.readline().strip()))) for _ in range(N)]
# 서로 불일치 하는 자리마다 계속 바꿔주면 됨 ㅇ 
def process(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            maps[i][j] = 1- maps[i][j]
if N <= 2 or M <= 2:
    if maps == target:
        print(0)
    else:
        print(-1)
elif N == 3 and M == 3:
    if maps == target:
        print(0)
    else:
        process(0,0)
        if maps == target:
            print(1)
        else:
            print(-1)
else:
    count = 0
    for i in range(N-2):
        for j in range(M-2):
            if maps[i][j] != target[i][j]:
                process(i,j)
                count += 1
    for i in range(N):
        for j in range(M):
            if maps[i][j]!= target[i][j] :
                print(-1)
                exit()
    print(count)
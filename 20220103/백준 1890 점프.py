from queue import Queue # queue로 해봤는데 시간초과 걸림 ... 
from sys import stdin
N = int(stdin.readline()) 
maps = [ [] for _ in range(N)]
dp = [[0]*(N) for _ in range(N)]
#print(maps)
#print(dp)
for i in range(N):
    maps[i] = list(map(int,stdin.readline().split()))
dp[0][0] = 1
for cur_y in range(N):
    for cur_x in range(N):
    #print(cur_y,cur_x)
        if dp[cur_y][cur_x] == 0 or (cur_x == N-1 and cur_y == N-1):
            continue
        jump_x = cur_x + maps[cur_y][cur_x]
        jump_y = cur_y + maps[cur_y][cur_x]
    
        if(jump_x < N):
            dp[cur_y][jump_x] += dp[cur_y][cur_x]

    
        if(jump_y < N):
            dp[jump_y][cur_x] += dp[cur_y][cur_x]

    
print(dp[N-1][N-1])



# 구글링 
# 처음에 queue로 했는데 시간초과가 나서 구글링 했더니
# 이중 반복문으로 돌리는게 정답이 됐다...

"""
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
"""
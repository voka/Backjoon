import sys

durumary = sys.stdin.readline().strip()
angel = sys.stdin.readline().strip()
devil = sys.stdin.readline().strip()
paack = [angel,devil]
goal = len(durumary)
maximum = len(angel)
#print(durumary,angel,devil,goal,maximun)
def cross(start_balpan):
    dp = [[[0]*(goal) for j in range(101)] for i in range(2)]
    for i in range(maximum):
        if paack[start_balpan][i] == durumary[0]:
            dp[start_balpan][i][0] = 1
    next_balpan = (start_balpan + 1)%2
    for g in range(1,goal):
        cur = durumary[g]
        for j in range(maximum):
            if cur == paack[next_balpan][j]:
                pre_balpan = (next_balpan+1)%2
                for p in range(j):
                    if paack[pre_balpan][p] == durumary[g-1]:
                        dp[next_balpan][j][g] += dp[pre_balpan][p][g-1]
        next_balpan = (next_balpan+1)%2
    answer = 0
    for j in range(2):
        for p in range(maximum):
            answer += dp[j][p][goal-1]
    return answer
answer = 0
answer += cross(0)
answer += cross(1)
print(answer)
""" 완전탐색 -> 시간초과
def DFS(x,d,pre): # pre = 1 -> devil에서 찾아야 함, pre = -1 -> angel에서 찾아야 함.
    #print(x,d,pre)
    if d == goal:
        dp[0] += 1
        return
    if x >= maximum:
        return
    if pre == 1:
        for j in range(x,maximum-(goal-d)+1):
            if devil[j] == durumary[d] :
                DFS(j+1,d+1,-1)
    else:
        for j in range(x,maximum-(goal-d)+1):
            if angel[j] == durumary[d]:
                DFS(j+1,d+1,1)
DFS(0,0,-1)
DFS(0,0,1)"""


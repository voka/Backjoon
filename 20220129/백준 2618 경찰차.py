""" 
해당 문제의 핵심 아이디어는 좌표가 아닌 
사건 번호로 문제를 해결하는 방법이다.
dp[A][B]를 첫번째 차량이 A번째 사건, 두번째 차량이 B번째 사건을 해결했을때
움직인거리의 최소값이라고 생각하고 문제를 푸는 것이다.

그리고 백트래킹은 dp_trace[A][B]라는 배열을 만들어 
1. 첫번째 차량 해결
dp_trace[A][B] = 1
2. 두번째 차량 해결
dp_trace[A][B] = 2
이런식으로 만들어 나중에 찾을때는
f = 0
s = 1
로 설정하고 
dp_trace[f][s]가 1이면 dp_trace[max(f,s)+1][s]로 해서 
다음번 사건을 해결한 차량을 찾고 
dp_trace[f][s]가 2이면 dp_trace[f][max(f,s)+1]로
다음번 사건을 해결한 차량을 찾으면 된다. 
 
"""

import sys
sys.setrecursionlimit(10000000) 
N,W = int(input()),int(input())
work = []
work.append((1,1)) # 첫번째 차량 시작점 
work.append((N,N)) # 두번째 차량 시작점 
for i in range(W):
    work.append(tuple(map(int,sys.stdin.readline().split())))
dp = [[-1]*(W+2) for _ in range(W+2)] # 사건 번호로 문제를 해결한다. 
dp_trace = [[0]*(W+2) for _ in range(W+2)]

def dist(a,b):
    return abs(work[a][0] - work[b][0]) + abs(work[a][1] - work[b][1])

def move(A,B):
    # 현재 사건 번호 
    cur = max(A,B) + 1
    if cur == W+2:
        return 0
    if dp[A][B] != -1 :
        return dp[A][B]
    f_car = move(cur,B) + dist(A,cur)
    s_car = move(A,cur) + dist(cur,B)
    if f_car < s_car:
        dp[A][B] = f_car
        dp_trace[A][B] = 1
    else:
        dp[A][B] = s_car
        dp_trace[A][B] = 2
    return dp[A][B]
 
print(move(0,1))
f = 0
s = 1
while True:
    if max(f,s) + 1 == W+2:
        break
    print(dp_trace[f][s])
    # 이번에 해결한 차량이 1번일 경우 
    # f의 사건 번호를 1 증가시켜 다음 사건을 해결한 차량을 찾는다.
    if dp_trace[f][s] == 1: # 1번차량 문제 해결
        f = max(f,s) + 1
    else: # 2번차량이 문제를 해결한 경우 
        s = max(f,s) + 1
    
     
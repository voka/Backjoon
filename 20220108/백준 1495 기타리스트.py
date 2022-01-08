from sys import stdin 

N,S,M = map(int,stdin.readline().split())

dp = [[0]*(M+1) for _ in range(N+1)] # i번째 음악곡을 연주했을때 가능한 볼륨 저장하는 곳
volums = list(map(int,stdin.readline().split()))
dp[0][S] = 1
for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 0 : # 가능한 방법이 없으면 넘어간다.
            continue
        if ( j + volums[i] )<= M: # 연주할 수 있다면
            dp[i+1][j + volums[i]] = 1 # 다음 곡에게 시작 볼륨의 정보를 넘겨준다. 
        if 0 <= (j - volums[i]):  # 연주할 수 있다면
            dp[i+1][j - volums[i]] = 1 # 다음 곡에게 시작 볼륨의 정보를 넘겨준다. 
answer = -1
for j in range(M, -1, -1):
    if dp[-1][j] :
        answer = j
        break
print(answer)
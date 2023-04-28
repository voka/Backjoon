import sys
ip = sys.stdin.readline
N, M, H = map(int, ip().split())
blocks = [list(map(int, ip().split())) for _ in range(N)]
# dp[i][h] -> i 번째 학생의 블록을 사용했을때 높이 h 를 만들 수 있는 경우의 수
dp = [[0]*(H+1) for _ in range(N+1)]

for i in range(1, N+1):
    for h in range(H+1):
        dp[i][h] = dp[i-1][h]
    for block in blocks[i-1]:
        dp[i][block] += 1
        for j in range(1, H+1):
            if j >= block:
                dp[i][j] = (dp[i][j] + dp[i-1][j-block]) % 10007
print(dp[N][H])

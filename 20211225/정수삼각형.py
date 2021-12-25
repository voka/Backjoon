N = int(input())
triangle = []
dp = []
for i in range(N):
    cur_data = list(map(int,input().split()))
    triangle.append(cur_data)
    dp.append([0]*len(cur_data))
# cur = 현재 층 값, up  = 선택할 수 있는 윗층 값 
# 반복문 돌면서 최대값 찾기 
dp[0] = [triangle[0][0]]
for i in range(1,N):
    cur_N = len(triangle[i])
    for j in range(cur_N):
        cur = triangle[i][j]
        if j == 0 :
            up = dp[i-1][j]
        elif j == cur_N-1:
            up = dp[i-1][cur_N-2]
        else:
            up = max(dp[i-1][j-1],dp[i-1][j])
        dp[i][j] = max(dp[i][j], cur + up)

print(max(dp[N-1]))
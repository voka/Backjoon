# N번째에 빨간색으로 칠할 경우 이전 층(?)에 초록색과 파란색으로 칠한 경우 중 작은 값을 선택하도록 점화식을 구성했습니다.
# 나머지 색도 동일합니다.(이전 층과 색이 겹치치 않도록)
N = int(input())
RGB_List = [[0,0,0]]
for i in range(N):
    RGB_List.append(list(map(int,input().split())))
dp = {}
dp[1] = RGB_List[1]
for i in range(2,N+1):
    cur_R = min(dp[i-1][1],dp[i-1][2]) + RGB_List[i][0]
    cur_G = min(dp[i-1][0],dp[i-1][2]) + RGB_List[i][1]
    cur_B = min(dp[i-1][0],dp[i-1][1]) + RGB_List[i][2]
    dp[i] = [cur_R,cur_G,cur_B]

print(min(dp[N]))
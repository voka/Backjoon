from sys import stdin 
N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [[0]*(21) for _ in range(N-1)]
dp[0][nums[0]] = 1
for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] == 0 : #가능한 경우에 수가 없는 경우 
            continue
        else:# 경우의 수가 있는 경우
            if 0 <= j + nums[i] <= 20:
                dp[i][j+nums[i]] += dp[i-1][j]
            if 0 <= j - nums[i] <= 20:
                dp[i][j-nums[i]] += dp[i-1][j]
        
print(dp[N-2][nums[-1]])

#구글링

# 나도 처음에는 DFS로 완전탐색을 하려고 했다.
# 그런데 시간초과나 나버려서 구글링을 해서 문제를 해결했다.
# 1차원 DP로는 이전의 점수 정보를 알아야 하므로 2차원 Dp가 되어야 한다. 
# 그리고 j 자체가 이전의 결과값을 나타내기 때문에 j에 nums[i]의 값을 더하거나 뺴서 값의 범위를 체크할 수 있다.
# 범위가 1부터 N-1까지인 이유는 nums[N-1] 마지막 두 숫자 사이에는 '등식'을 넣기 때문에 N-2번째와 N-1번째 값 사이에는 고정적으로 '='이 들어가기 때문이다. 
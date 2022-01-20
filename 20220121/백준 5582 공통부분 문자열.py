from sys import stdin 
one = stdin.readline().strip()
two = stdin.readline().strip()
dp=[[0] * (len(two) + 1) for _ in range(len(one) + 1)] # dp의 대각선을 통해서 구함 .
# 참고 사이트 https://dailylifeofdeveloper.tistory.com/114?category=790222
#print(small,big)
answer = 0
for i in range(1,len(one)+1):
    for j in range(1,len(two)+1):
        if one[i-1] == two[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j]) 
print(answer)

# Python3로 제출하면 시간제한  , PYPY로 제출해야 통과
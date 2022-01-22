N,M,K = map(int,input().split())
dp = [[1]*(M+1) for _ in range(N+1)]
# 0,1 1,0 은 사전에 문자열이 하나씩 존재한다.
for i in range(1,N+1):
    for j in range(1,M+1):
        # a가 i개 z가 j개 있는 문자의 수는 
        # a가 i-1개 z가 j개 + a가 i개 z가 j-1개 들어있는 문자열의 수의 합과 같다. 
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

a,z = N,M
if K > dp[N][M]:
    print(-1)
else:
    answer = ""
    while True:
        if a == 0 or z == 0:
            answer += "a"*a
            answer += "z"*z
            break
        str_num = dp[a-1][z]
        if K <= str_num:
            answer += "a"
            a -= 1
        else:
            answer += "z"
            z -= 1
            K -= str_num
    print(answer)
            
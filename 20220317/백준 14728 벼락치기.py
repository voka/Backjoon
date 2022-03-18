import sys
ip = sys.stdin.readline 
N, T = map(int,ip().split())
Times, values = [], []
for i in range(N):
    K,S  = map(int,ip().split())
    Times.append(K)
    values.append(S)
dp = [0]*(T+1)
for i in range(N):
    # 역방향으로 하면 배열 Times, values 요소당 1개씩 사용, 정방향으로 하면 여러개 사용 
    for j in range(T,0,-1):
        if j >= Times[i] :
            dp[j] = max(dp[j], dp[j - Times[i]] + values[i])
print(dp[-1])
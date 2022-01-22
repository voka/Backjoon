N = int(input())
dp = [N] * (1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2 
"""
graph = [[] for _ in range(1000001)]
graph[1] = [1]
graph[2] = [2,1]
graph[3] = [3,1]
graph[4] = [4,2,1]

for i in range(5,N+1):
    i_1 = i-1
    if i%2 == 0 and i%3 == 0:
        i_3 = i//3
        i_2 = i//2
        if dp[i_3] <= dp[i_2] and dp[i_3] <= dp[i_1]:
            dp[i] = dp[i_3] + 1
            graph[i] = [i] + graph[i_3] 
        elif dp[i_2] <= dp[i_3] and dp[i_2] <= dp[i_1]:
            dp[i] = dp[i_2] + 1
            graph[i] = [i] + graph[i_2]
        elif dp[i_1] <= dp[i_2] and dp[i_1] <= dp[i_3] :
            dp[i] = dp[i_1] + 1
            graph[i] = [i] + graph[i_1] 
    elif i%3 == 0:
        i_3 = i//3
        if dp[i_3] < dp[i_1]:
            dp[i] = dp[i_3] + 1
            graph[i] = [i] + graph[i_3] 
        else:
            dp[i] = dp[i_1] + 1
            graph[i] = [i] + graph[i_1] 
    elif i%2 == 0:
        i_2 = i//2
        if dp[i_2] < dp[i_1]:
            dp[i] = dp[i_2] + 1
            graph[i] = [i] + graph[i_2]
        else:
            
            dp[i] = dp[i_1] + 1
            graph[i] = [i] + graph[i_1] 
    else:
        dp[i] = dp[i_1] + 1
        graph[i] = [i] + graph[i_1] 

print(dp[N])
for i in graph[N] : print(i,end=" ")
"""
# 위의 답 => 조건 분기 너무 많고, Graph가 메모리 양도 많이 잡아 먹음 . 
# 밑에 -> dp + 백트래킹
for i in range(5,N+1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[N])
while N != 1:
    print(N,end = " ")
    if N%3 == 0 and dp[N]-1 == dp[N//3]:
        N = N//3
    elif N%2 == 0 and dp[N]-1 == dp[N//2]:
        N = N//2
    elif dp[N] -1 == dp[N-1]:
        N -= 1
        
print(1)
        
    
    

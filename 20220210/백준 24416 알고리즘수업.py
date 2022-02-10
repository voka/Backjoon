from collections import deque
N = int(input())
answer = [0,N-2]
fibo = [0 for i in range(N+1)]
fibo[1] = 1
fibo[2] = 1
for i in range(3,N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
answer[0] = fibo[N]   
print(*answer)
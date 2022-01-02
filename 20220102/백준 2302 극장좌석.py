from sys import stdin
fibo = {}
fibo[0] = 1
fibo[1] = 1
fibo[2] = 2
N = int(stdin.readline())
for i in range(3,N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
M = int(stdin.readline())
if M == 0:
    print(fibo[N])
    exit()
fixed = []
for i in range(M):
    a = int(stdin.readline())
    fixed.append(a)
answers = []
pre = 0
for k in fixed:
    #print(k,pre)
    answers.append(k-pre -1)
    pre = k
answers.append(N-pre)
answer = 1
for j in answers:
    answer *= fibo[j]
print(answer)
"""
n = 1 --> 1
n = 2 --> 2
n = 3 --> 3
n = 4 --> 5 
n = 5 --> 8

1 2 3 4
1 2 4 3
2 1 3 4
2 1 4 3
1 3 2 4

1 2 3 4 5
1 2 4 3 5
1 2 3 5 4
1 3 2 4 5
1 3 2 5 4
2 1 3 4 5
2 1 4 3 5
2 1 3 5 4


dp[n] --> 피보나치 수열
"""

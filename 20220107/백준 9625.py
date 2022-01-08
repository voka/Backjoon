"""
A 1
B 1
BA 2
BAB 3
BABBA 5
BABBABAB 8
BABBABABBABBA 13 
피보나치 수
"""
fibo = {}
fibo[0] = 0
fibo[1] = 1
fibo[2] = 2
fibo[3] = 3
fibo[4] = 5
N = int(input())
for i in range(5,N):
    fibo[i] = fibo[i-1] + fibo[i-2]
if N == 1:
    print(0,1)
elif N == 2:
    print(1,0)
else:
    print(fibo[N-2], fibo[N-1])

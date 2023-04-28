import sys
import math


def is_prime(money):
    if money == 1:
        return False
    max_i = int(math.sqrt(money))
    for i in range(2, max_i+1):
        if money % i == 0:
            return False
    return True


prime = [is_prime(i) for i in range(500001)]
ip = sys.stdin.readline
N = int(ip())
candy = [0 for _ in range(10001)]
for i in range(N):
    candy[int(ip())] += 1

dp = [0]*(500001)
for i in range(N):
    dp[candy[i]] += 1
for i in range(N):
    for j in range(i+1, N):
        dp[candy[i] + candy[j]] += 1
answer = 0
for i in range(500001):
    if dp[i] != 0 and prime[i]:
        print(dp[i], i)
        answer += dp[i]
print(answer)
'''
1 1 2 7
2
7
1 2
1 2
1 1 2 7

2
7


    1 2 3 4
1   0 
1   0 1 
2
7


'''

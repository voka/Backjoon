N = int(input())
# 에라토스테네스의 체 
primes = []
check = [False,False] + [True]*(N-1)
for i in range(2,N+1):
    if check[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            check[j] = False
# 부분합 dp
primes.insert(0,0)
n = len(primes)
for i in range(1,n):
    primes[i] += primes[i-1]

# 투포인터 알고리즘 start
i = 0
j = 1
answer = 0
while i != n-1:
    #print(i,j)
    cur = primes[j] - primes[i]
    if cur == N:
        answer += 1 
        i += 1
    elif cur < N:
        if j != n-1:
            j += 1
        else:
            i += 1
    else:
        i += 1
print(answer)
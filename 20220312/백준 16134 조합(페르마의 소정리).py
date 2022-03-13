import sys
ip = sys.stdin.readline 
M = 1000000007
N,R = map(int,ip().split())
def fac(N):
    n = 1
    for i in range(2,N+1):
        n = (n*i)%M
    return n 
def square(n,k) :
    if k == 0:
        return 1
    elif k == 1:
        return n
    temp = square(n,k//2)
    if k%2 == 1:
        return temp * temp * n % M
    else:
        return temp * temp % M
top = fac(N)
bot = fac(N-R) * fac(R)%M

print(top* square(bot, M-2) % M)
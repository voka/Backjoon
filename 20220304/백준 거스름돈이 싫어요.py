import sys, math
ip = sys.stdin.readline 
N = int(ip())
up = 0
bottom = 1
for i in range(N):
    a,b = map(int,ip().split())
    gcd = math.gcd(a,b)
    a = int(a/gcd)
    b = int(b/gcd)
    up = math.gcd(up,a)
    bottom = math.lcm(bottom,b)

print(up,bottom)
from sys import stdin 
import math
n,m = map(int, stdin.readline().split())
X = math.factorial(n)
Y = (math.factorial(n-m)) * (math.factorial(m))
answer = X//Y
print(answer)
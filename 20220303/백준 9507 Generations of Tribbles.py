import sys
ip = sys.stdin.readline 
T = int(ip())
Q = [int(ip()) for _ in range(T)]
Q_max = max(Q)

koong = [0]*70
koong[0] = 1
koong[1] = 1
koong[2] = 2
koong[3] = 4

for i in range(4,Q_max+1):
    koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]
for q in Q:
    print(koong[q])
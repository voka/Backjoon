import sys
N = int(sys.stdin.readline())
floats = [float(sys.stdin.readline()) for _ in range(N)]
for i in range(1,N):
    floats[i] = max(floats[i],floats[i]*floats[i-1])
print("{:.3f}".format(max(floats)))